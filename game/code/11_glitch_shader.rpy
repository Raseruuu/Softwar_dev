# ==============================================================================
# PROFESSIONAL OPTIMIZED DYNAMIC GLITCH & RGB SPLIT SHADER FOR REN'PY (V2.0)
# Developed by: GRIMUMU (2026)
#
# LICENSE:
# Free for use in both commercial and non-commercial projects.
# Attribution is required. Please credit "GRIMUMU" in your project.
#
# SUPPORT & SOCIALS:
# - Itch.io:    https://grimumu.itch.io/
# - Instagram:  https://www.instagram.com/grimumu__/
# - X/Twitter:  https://x.com/Grimumu_
# - Patreon:    https://www.patreon.com/cw/Grimumu
#
# ==============================================================================
#
# A 100% GPU-driven, high-performance solution for real-time digital distortion.
# Features additive emissive blending, procedural WebGL noise, and a modular API.
# Specialized in horror, cyberpunk, and system-error visual effects for Ren'Py.
#
# ==============================================================================
#
# QUICK PRESETS (Legacy V1.0 - Fully Supported):
# ----------------------------------------------
# - at subtle_glitch, normal_glitch, intense_glitch, extreme_glitch
# - at subtle_broken_glitch, normal_broken_glitch, extreme_broken_glitch
# - at crashed_glitch, glitch_static_preset
#
# MODULAR API (V2.0):
# -------------------
# You can now combine 3 dimensions using simple string arguments:
# Syntax: at glitch("Intensity", "ColorPalette", "Fragmentation")
#
# 1. Intensity (Tier):  "subtle", "normal", "intense", "extreme"
# 2. Color (Palette):   "classic" (Red/Blue), "cyberpunk" (Cyan/Pink),
#                       "matrix" (Green), "ghost" (White), "toxic" (Green/Purple)
# 3. Fragmentation:     "thin" (fine lines), "thick" (standard), "huge" (blocks)
#
# Example: show character at glitch("intense", "toxic", "huge")
#
# SPECIALIZED TRANSFORMS:
# -----------------------
# - glitch_static(tier, color, slice, seed=X.X): Freezes the glitch on a specific seed.
# - glitch_hit(tier, color, slice, duration=0.5): Temporary burst effect for combat damage.
#
# ==============================================================================

init -1 python:
    # Defensive pad calculation based on maximum physical displacement
    def _calc_glitch_pad(strength, chroma, pad):
        if pad is not None:
            if isinstance(pad, (tuple, list)) and len(pad) == 4:
                return tuple(int(x) for x in pad)
            elif isinstance(pad, (int, float)):
                p = int(pad)
                return (p, 0, p, 0)
        
        # Base project width for coherent scaling relative to VRAM limits
        screen_w = getattr(config, "screen_width", 1920)
        pad_x = min(1000, int((max(0.0, strength) + max(0.0, chroma)) * screen_w * 1.25))
        return (pad_x, 0, pad_x, 0)

    renpy.register_shader("custom.glitch",
        variables="""
        uniform float u_time;
        uniform sampler2D tex0;
        varying vec2 v_tex_coord;
        uniform float u_glitch_strength;
        uniform float u_glitch_density;
        uniform float u_chroma_strength;
        uniform float u_glitch_rate;
        uniform float u_speed;
        uniform float u_seed;
        uniform vec3 u_c_base;
        uniform vec3 u_c_shift1;
        uniform vec3 u_c_shift2;
        """,
        fragment_functions="""
        // Fast 100% arithmetic hash (No trig). Safe for 16-bit MediumP
        float hash_fast(vec2 p) {
            vec2 q = fract(p * vec2(123.34, 456.21));
            q += dot(q, q + 45.32);
            return fract(q.x * q.y);
        }

        // Clamped fetch without divergent branching
        vec4 fetch_clamped(sampler2D tex, vec2 uv) {
            float in_bounds = step(0.0, uv.x) * step(uv.x, 1.0) * step(0.0, uv.y) * step(uv.y, 1.0);
            return texture2D(tex, clamp(uv, 0.0, 1.0)) * in_bounds;
        }
        """,
        fragment_300="""
        vec2 uv = v_tex_coord;
        
        // Overflow-protected early cyclical window
        float local_time = mod(u_time, 32.0);
        float is_moving = step(0.0001, abs(u_speed));
        float t = mix(mod(u_seed, 64.0), floor(mod(local_time * u_speed, 256.0)), is_moving);
        
        float block_id = floor(uv.y * max(1.0, u_glitch_density));
        float n_block = hash_fast(vec2(block_id, t));
        float is_glitched = step(1.0 - clamp(u_glitch_rate, 0.0, 1.0), n_block);
        
        vec4 final_col;
        
        // Uniform branching: Fast exit if block is clean (Fillrate Saver)
        if (is_glitched < 0.5) {
            final_col = texture2D(tex0, uv);
        } else {
            float micro_jitter = (hash_fast(vec2(floor(uv.y * u_glitch_density * 3.0), t)) - 0.5) * 0.25;
            float shift = ((hash_fast(vec2(t, block_id + 3.0)) - 0.5) * 2.0 + micro_jitter) * u_glitch_strength;
            float chroma = u_chroma_strength;
            
            vec4 col_base = fetch_clamped(tex0, uv + vec2(shift, 0.0));
            vec4 col_1    = fetch_clamped(tex0, uv + vec2(shift + chroma, 0.0));
            vec4 col_2    = fetch_clamped(tex0, uv + vec2(shift - chroma, 0.0));
            
            // Dynamic RGB matrix: Preserves PMA additivity but with custom colors
            vec3 rgb = col_base.rgb * u_c_base + col_1.rgb * u_c_shift1 + col_2.rgb * u_c_shift2;
            final_col = vec4(rgb, col_base.a);
        }
        
        gl_FragColor = final_col;
        """
    )


# ==============================================================================
# TRANSFORMS & PRESET API
# ==============================================================================

init -1 python:
    # --- Intensity Levels (Strength, Chroma, Rate, Speed) ---
    GLITCH_TIERS = {
        "subtle":  {"strength":0.015, "chroma":0.006, "rate":0.15, "speed":12.0},
        "normal":  {"strength":0.04,  "chroma":0.015, "rate":0.30, "speed":18.0},
        "intense": {"strength":0.08,  "chroma":0.03,  "rate":0.55, "speed":24.0},
        "extreme": {"strength":0.25,  "chroma":0.08,  "rate":0.70, "speed":30.0},
    }

    # --- Fragmentation (Block thickness / Y-Density) ---
    GLITCH_SLICES = {
        "thin":  80.0,  # Fine scanline-style lines
        "thick": 25.0,  # Standard blocks (Normal)
        "huge":  3.5,   # Massive fragments (Sprite breaks into 3-4 huge chunks)
    }

    # --- Color Palettes (Base, Shift 1, Shift 2) ---
    GLITCH_PALETTES = {
        "classic":   ((0.0, 1.0, 0.0), (1.0, 0.0, 0.0), (0.0, 0.0, 1.0)), # Red and Blue
        "cyberpunk": ((0.0, 0.0, 0.0), (1.0, 0.0, 1.0), (0.0, 1.0, 1.0)), # Magenta and Cyan
        "matrix":    ((0.0, 0.2, 0.0), (0.0, 1.0, 0.0), (0.0, 0.5, 0.0)), # Toxic Greens
        "ghost":     ((0.3, 0.3, 0.3), (0.8, 0.8, 0.8), (0.5, 0.5, 0.5)), # Whites and Grays
        "toxic":     ((0.0, 0.0, 0.0), (0.2, 1.0, 0.2), (0.6, 0.0, 1.0)), # Green and Purple
    }


# --- Main API for Non-Programmers ---

transform glitch(tier="normal", color="classic", slice="thick", pad=None):
    mesh True
    mesh_pad _calc_glitch_pad(GLITCH_TIERS[tier]["strength"], GLITCH_TIERS[tier]["chroma"], pad)
    shader "custom.glitch"
    u_glitch_strength GLITCH_TIERS[tier]["strength"]
    u_glitch_density GLITCH_SLICES[slice]
    u_chroma_strength GLITCH_TIERS[tier]["chroma"]
    u_glitch_rate GLITCH_TIERS[tier]["rate"]
    u_speed GLITCH_TIERS[tier]["speed"]
    u_seed 0.0
    u_c_base GLITCH_PALETTES[color][0]
    u_c_shift1 GLITCH_PALETTES[color][1]
    u_c_shift2 GLITCH_PALETTES[color][2]
    pause 0.05
    repeat

transform glitch_static(tier="normal", color="classic", slice="thick", seed=1.0, pad=None):
    mesh True
    mesh_pad _calc_glitch_pad(GLITCH_TIERS[tier]["strength"], GLITCH_TIERS[tier]["chroma"], pad)
    shader "custom.glitch"
    u_glitch_strength GLITCH_TIERS[tier]["strength"]
    u_glitch_density GLITCH_SLICES[slice]
    u_chroma_strength GLITCH_TIERS[tier]["chroma"]
    u_glitch_rate GLITCH_TIERS[tier]["rate"]
    u_speed 0.0
    u_seed float(seed)
    u_c_base GLITCH_PALETTES[color][0]
    u_c_shift1 GLITCH_PALETTES[color][1]
    u_c_shift2 GLITCH_PALETTES[color][2]

transform glitch_hit(tier="intense", color="classic", slice="thick", duration=0.25, pad=None):
    mesh True
    mesh_pad _calc_glitch_pad(GLITCH_TIERS[tier]["strength"], GLITCH_TIERS[tier]["chroma"], pad)
    shader "custom.glitch"
    u_glitch_strength GLITCH_TIERS[tier]["strength"]
    u_glitch_density GLITCH_SLICES[slice]
    u_chroma_strength GLITCH_TIERS[tier]["chroma"]
    u_glitch_rate GLITCH_TIERS[tier]["rate"]
    u_speed GLITCH_TIERS[tier]["speed"]
    u_seed 0.0
    u_c_base GLITCH_PALETTES[color][0]
    u_c_shift1 GLITCH_PALETTES[color][1]
    u_c_shift2 GLITCH_PALETTES[color][2]
    pause duration
    shader None
    mesh False

# ==============================================================================
# BACKWARD COMPATIBILITY (LEGACY V1 PRESETS)
# ==============================================================================
transform glitch_static_preset:
    glitch_static("normal", "classic", "thick")
transform subtle_glitch:
    glitch("subtle", "classic", "thick")
transform normal_glitch:
    glitch("normal", "classic", "thick")
transform intense_glitch:
    glitch("intense", "classic", "thick")
transform extreme_glitch:
    glitch("extreme", "classic", "thick")
transform subtle_broken_glitch:
    glitch("subtle", "classic", "thin")
transform normal_broken_glitch:
    glitch("normal", "classic", "thin")
transform intense_broken_glitch:
    glitch("intense", "classic", "thin")
transform extreme_broken_glitch:
    glitch("extreme", "classic", "thin")
transform crashed_glitch:
    glitch("extreme", "classic", "huge")