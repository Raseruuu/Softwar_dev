transform playerattack:
    zoom 1.0 xanchor 0.5 yanchor 0.5
    linear 0.2 zoom 1.2 xpos (tarx+origx)/2 ypos (tary+origy)/2
    linear 0.2 zoom 1.0 xpos (tarx+origx)/2 ypos tary+((origy-tary)/2)
    linear 0.2 zoom 1.0 xpos origx ypos origy
label damageleft:
    play sound "sfx/Damage2.wav"
    show damageeffect:
        xalign 0.05
        rotate -90
    pause 0.5
    hide damageeffect
    return
label damageright:
    play sound "sfx/Damage2.wav"    
    show damageeffect:
        xalign 0.95
        rotate 90 
    pause 0.5
    hide damageeffect
    return
label damageright4:
    $ slashcount = 0
    label damagerightagain:
    play sound "sfx/Damage2.wav" volume 2.0   
    show damageeffect:
        xalign 0.95
        rotate 90 
    pause 0.5
    hide damageeffect
    $ slashcount+=1
    
    if slashcount >=4:
        return
    else:
        jump damagerightagain
    
play sound "sfx/noise.wav"
label damageleftblocked:
    play sound "sfx/noise.wav"
    show damageeffect:
        xalign 0.1
        rotate -90
    pause 0.5
    hide damageeffect
    return
label damagerightblocked:
    play sound "sfx/noise.wav"
    show damageeffect:
        xalign 0.9
        rotate 90 
    pause 0.5
    hide damageeffect
    return
transform leapright:
    linear 0.1 yoffset -40 xoffset 50
    linear 0.1 xoffset 100 yoffset 0
transform leapright2:
    linear 0.1 yoffset -40 xoffset 500
    linear 0.1 xoffset 100 yoffset 0
transform leapleft:
    linear 0.1 yoffset -40 xoffset -50
    linear 0.1 xoffset -100 yoffset 0
# transform cardpos1:
transform bumpleft:
    xoffset 0
    linear 0.1 xoffset -80
    linear 0.1 xoffset 0
transform bumpright:
    xoffset 0
    linear 0.1 xoffset 80
    linear 0.1 xoffset 0
    
transform sway:
    transform_anchor True
    linear 0.25 rotate 5
    linear 0.5 rotate -5
    linear 0.20 rotate 1
    linear 0.05 rotate 0
transform alpha05:
    alpha 0.5
transform alpha08:
    alpha 0.8
transform dright: # Smooth dissolve with motion at the extreme right, from near side
    alpha 0.0 xpos 0.9 yalign 1.0 xanchor 0.5 xzoom 1.0
    linear 0.4 alpha 1.0 xanchor 0.5 xpos 0.85
transform dright2: # Smooth dissolve with motion at the mid right, from near side
    alpha 0.0 xpos 0.7 yalign 1.0 xanchor 0.5 xzoom 1.0
    linear 0.4 alpha 1.0 xanchor 0.5 xpos 0.65


transform dleft: # Smooth dissolve with motion at the extreme left, from near side
    alpha 0.0 xpos 0.1 yalign 1.0 xanchor 0.5 xzoom -1.0
    linear 0.4 alpha 1.0 xanchor 0.5 xpos 0.15
transform dleft2: # Smooth dissolve with motion at the mid left, from near side
    alpha 0.0 xpos 0.3 yalign 1.0 xanchor 0.5 xzoom -1.0
    linear 0.4 alpha 1.0 xanchor 0.5 xpos 0.35

transform rsurprise: #surprised and moved backward while facing Right
    alpha 1.0 rotate 0 yanchor 1.0 transform_anchor True
    linear 0.05 rotate 0 transform_anchor True yzoom 1.05 yanchor 0.95 xoffset 70
    linear 0.05 rotate 5 transform_anchor True yzoom 1.1 yanchor 0.95 xoffset 75
    linear 0.2 rotate -10 transform_anchor True yzoom 1.0 yanchor .90 xoffset 100
    linear 0.5 rotate 0 transform_anchor True yanchor 1.0 xoffset .10

transform lsurprise: #surprised and moved backward while facing Left
    alpha 1.0 rotate 0 yanchor 1.0 transform_anchor True
    linear 0.03 rotate -20 transform_anchor True yzoom 1.1 yanchor 0.95 xoffset -50
    linear 0.2 rotate 10 transform_anchor True yzoom 1.0 yanchor .90 xoffset -100
    linear 0.5 rotate 0 transform_anchor True yanchor 1.0 xoffset .10


transform raffirm: #upper body nodding at right
    alpha 1.0 rotate 0 yanchor 1.0 transform_anchor True
    linear 0.25 rotate -10 yanchor 0.9 transform_anchor True yanchor .90 xoffset 50
    linear 0.3 rotate 0 yanchor 1.0 transform_anchor True yanchor 1.0 xoffset 0
    linear 0.25 rotate -10 yanchor 0.9 transform_anchor True yanchor .90 xoffset 50
    linear 0.3 rotate 0 yanchor 1.0 transform_anchor True yanchor 1.0 xoffset 0
transform laffirm: #upper body nodding at left
    alpha 1.0 rotate 0 yanchor 1.0 transform_anchor True
    linear 0.25 rotate 15 yanchor 0.9 transform_anchor True yanchor .95 xoffset -20
    linear 0.3 rotate 0 yanchor 1.0 transform_anchor True yanchor 1.0 xoffset 0
    linear 0.25 rotate 15 yanchor 0.9 transform_anchor True yanchor .95 xoffset -20
    linear 0.3 rotate 0 yanchor 1.0 transform_anchor True yanchor 1.0 xoffset 0


transform rdown: #brief lowering of body while at right
    alpha 1.0 rotate 0 yanchor 1.0 transform_anchor True
    linear 0.2 rotate -5 yanchor .95 yzoom 0.9 transform_anchor True
    linear 0.4 rotate 0 yanchor .96 yzoom 0.90  transform_anchor True
    linear 0.5 rotate 0 yanchor 1.0 yzoom 1.0  transform_anchor True
transform ldown: #brief lowering of body while at left
    alpha 1.0 rotate 0 yanchor 1.0 transform_anchor True
    linear 0.2 rotate 5 yanchor .95 yzoom 0.9 transform_anchor True
    linear 0.4 rotate 0 yanchor .96 yzoom 0.90  transform_anchor True
    linear 0.5 rotate 0 yanchor 1.0 yzoom 1.0  transform_anchor True


transform dance: #Dancing, flipping left and right
    xalign 0.5 alpha 1.0
    xzoom 0.95 yzoom 1.02 transform_anchor True
    linear 0.2 xzoom 1.0 yzoom 1.0 transform_anchor True
    linear 0.2 xzoom 0.95 yzoom 1.02 transform_anchor True
    xzoom -0.95 yzoom 1.02 transform_anchor True
    linear 0.2 xzoom -1.0 yzoom 1.0 transform_anchor True
    linear 0.2 xzoom -0.95 yzoom 1.02 transform_anchor True
    repeat




transform boing: #here I am
    yanchor 0.0
    ypos 1.0
    xzoom 1.5
    yzoom 0.5
    linear 0.2 yanchor 1.0 yzoom 0.5 xzoom 1.5
    linear 0.2 yzoom 1.5 xzoom 0.5 yzoom 1.5
    linear 0.2 yzoom 1.0 xzoom 1.0

transform kickedaway: #whaaaaaa
    rotate 0
    zoom 1.0
    # ypos 1.0
    # yanchor 0.7
    parallel:
        rotate 0
        linear 0.2 rotate 360
        repeat
    parallel:
        linear 0.8 zoom 0.0
    parallel:
        linear 0.8 yalign 0.2 xpos 1.0
transform excitement: #oh my gawd, it's coming!!
    parallel:
        xzoom -1.0
        pause 0.6
        xzoom 1.0
        pause 0.6
        repeat
    parallel:
        linear 0.6 xpos 0.4
        linear 0.6 xpos 0.3
        repeat
    parallel:
        ypos 1.0
        linear 0.3 ypos 1.1
        linear 0.3 ypos 1.0
        repeat

transform cardflash_bright(image_path):
    contains:
        (image_path)
        xalign 0.5 yalign 0.46 alpha 0.4 matrixcolor BrightnessMatrix(1.0) * OpacityMatrix(0.5)
        linear 0.3 xzoom 1.5 yzoom 1.5
        # pause 0.2 
        linear 0.3 xzoom 2.0 yzoom 2.0 alpha 0.0 
    contains:
        (image_path)
        zoom 1.0 xalign 0.5 yalign 0.46
    contains:
        (image_path)
        xalign 0.5 yalign 0.46 alpha 0.4 matrixcolor BrightnessMatrix(0.8) * SaturationMatrix(0.6) * OpacityMatrix(0.5)
        xzoom 1.1 yzoom 1.1
        pause 0.2 
        linear 0.2 alpha 0.0 xzoom 1.0 yzoom 1.0
transform landing:
    yanchor 1.0 ypos 1.0
    ease 0.2 yalign 0.08
    ease 0.2 yalign 0.05
transform jumpoff:
    ease 0.2 yalign 0.05
    ease 0.1 yanchor 1.2 ypos 0.0
transform tremors:
    
    yoffset 1
    pause 0.02
    yoffset -1
    pause 0.02
    repeat
transform tremors_side:
    xoffset 2
    pause 0.1
    xoffset -2
    pause 0.1
    repeat
transform reddening:
    parallel:
        yoffset 1
        pause 0.02
        yoffset -1
        pause 0.02
        repeat
    parallel:

        matrixcolor IdentityMatrix()
        pause renpy.random.choice([1.0,2.0])
        matrixcolor TintMatrix('#f00') 
        pause 0.02
        matrixcolor IdentityMatrix()
        pause 0.02
        matrixcolor TintMatrix('#f00') 
        pause 0.06
        matrixcolor IdentityMatrix()
        pause 0.02


    
        repeat
transform redlightning(image_path):
    contains:
        "lightning"

transform surgeofpower():
    
    contains:
        "powerflow"
        transform_anchor True
        alpha 1.0 yanchor 1.7 
        # pause renpy.random.choice([0.0,0.01,0.02])
        xoffset renpy.random.choice([-20,0,20])
        yoffset 100+renpy.random.choice([-20,0,20])
        rotate renpy.random.choice([-20,-10,0,10,20])
        xzoom renpy.random.choice([1.0,0.9,-0.9,-1.0])
        linear 0.4 alpha 0.0
        # repeat
    contains:
        "powerflow"
        transform_anchor True
        alpha 1.0 yanchor 1.2 
        # pause renpy.random.choice([0.0,0.01,0.02])
        xoffset renpy.random.choice([-20,0,20])
        yoffset 100+renpy.random.choice([-20,0,20])
        rotate renpy.random.choice([-20,-10,0,10,20])
        xzoom renpy.random.choice([1.0,0.9,-0.9,-1.0])

        linear 0.4 alpha 0.0
    contains:
        "powerflow"
        transform_anchor True
        alpha 1.0 yanchor 1.4 
        # pause renpy.random.choice([0.0,0.01,0.02])
        xoffset renpy.random.choice([-20,0,20])
        yoffset 100+renpy.random.choice([-20,0,20])
        rotate renpy.random.choice([-20,-10,0,10,20])
        xzoom renpy.random.choice([1.0,0.9,-0.9,-1.0])

        linear 0.3 alpha 0.0
    contains:
        "powerflow"
        transform_anchor True
        alpha 1.0 yanchor 1.5 
        # pause renpy.random.choice([0.0,0.01,0.02])
        xoffset renpy.random.choice([-20,0,20])
        yoffset 100+renpy.random.choice([-20,0,20])
        rotate renpy.random.choice([-20,-10,0,10,20])
        xzoom renpy.random.choice([1.0,0.9,-0.9,-1.0])

        linear 0.3 alpha 0.0
    contains:
        "powerflow"
        transform_anchor True
        alpha 1.0 yanchor 1.8 
        # pause renpy.random.choice([0.0,0.01,0.02])
        xoffset renpy.random.choice([-20,0,20])
        yoffset 100+renpy.random.choice([-20,0,20])
        rotate renpy.random.choice([-20,-10,0,10,20])
        xzoom renpy.random.choice([1.0,0.9,-0.9,-1.0])

        linear 0.3 alpha 0.0
    contains:
        "powerflow"
        transform_anchor True
        alpha 1.0 yanchor 1.0 
        # pause renpy.random.choice([0.0,0.03,0.4])
        xoffset renpy.random.choice([-20,0,20])
        yoffset 100+renpy.random.choice([-20,0,20])
        rotate renpy.random.choice([-20,-10,0,10,20])
        xzoom renpy.random.choice([1.0,0.9,-0.9,-1.0])

        linear 0.1 alpha 0.0
    contains:
        "powerflow"
        transform_anchor True
        alpha 1.0 yanchor 2.0 
        # pause renpy.random.choice([0.0,0.01,0.02])
        xoffset renpy.random.choice([-20,0,20])
        yoffset 100+renpy.random.choice([-20,0,20])
        rotate renpy.random.choice([-20,-10,0,10,20])
        xzoom renpy.random.choice([1.0,0.9,-0.9,-1.0])

        linear 0.2 alpha 0.0
    pause 0.2
    repeat
    

#     
# transform sidesteps_effect(image_path, start_pos, end_pos, duration):
#     subpixel True
#     yalign 1.0
#     contains:
#         Image(image_path)
#         xalign start_pos alpha 0.2
#         easein duration + 0.4 xalign end_pos
#     contains:
#         Image(image_path)
#         xalign start_pos alpha 0.4
#         easein duration + 0.3 xalign end_pos
#     contains:
#         Image(image_path)
#         xalign start_pos alpha 0.6
#         easein duration + 0.2 xalign end_pos
#     contains:
#         Image(image_path)
#         xalign start_pos alpha 0.8
#         easein duration + 0.1 xalign end_pos
#     contains:
#         Image(image_path)
#         xalign start_pos alpha 1
#         easein duration xalign end_pos




transform sidesteps_effect(image_path, start_pos, end_pos, duration):
    subpixel True

    contains:
        image_path
        xalign start_pos alpha 0.1 
        easein duration + 0.4 xalign end_pos
        block:
            image_path
            xalign end_pos alpha 0.1
            easein duration xalign start_pos
            image_path
            xalign start_pos alpha 0.1
            easein duration  xalign end_pos
            repeat
    contains:
        image_path
        xalign start_pos alpha 0.2 
        easein duration + 0.3 xalign end_pos
        block:
            image_path
            xalign end_pos alpha 0.2 
            easein duration xalign start_pos
            image_path
            xalign start_pos alpha 0.2 
            easein duration  xalign end_pos
            repeat
    contains:
        image_path
        xalign start_pos alpha 0.3  
        easein duration + 0.2 xalign end_pos
        block:
            image_path
            xalign end_pos alpha 0.3 
            easein duration xalign start_pos
            image_path
            xalign start_pos alpha 0.3 
            easein duration  xalign end_pos
            repeat

    contains:
        image_path
        xalign start_pos alpha 0.5 
        easein duration + 0.1 xalign end_pos
        block:
            image_path
            xalign end_pos alpha 0.5 
            easein duration  xalign start_pos
            image_path
            xalign start_pos alpha 0.5 
            easein duration  xalign end_pos

            repeat

    contains:
        image_path
        xalign start_pos alpha 0.9 
        easein duration xalign end_pos
        image_path
        xalign end_pos alpha 0.9 
        easein duration xalign start_pos

        repeat
transform sidesteps_effect_dodge(image_path, start_pos, end_pos,duration,y_anch=0.32,y_pos=0.3, ):
    subpixel True
    
    contains:
        image_path
        yanchor y_anch ypos y_pos
        xalign start_pos alpha 0.1 
        easein duration + 0.4 xalign end_pos 
        block:
            image_path
            yanchor y_anch ypos y_pos
            xalign end_pos alpha 0.1
            easein duration xalign start_pos  
            image_path
            yanchor y_anch ypos y_pos
            xalign start_pos alpha 0.1
            easein duration  xalign end_pos  
            repeat 3
    contains:
        image_path
        yanchor y_anch ypos y_pos
        xalign start_pos alpha 0.2 
        easein duration + 0.3 xalign end_pos  
        block:
            image_path
            yanchor y_anch ypos y_pos
            xalign end_pos alpha 0.2 
            easein duration xalign start_pos  
            image_path
            yanchor y_anch ypos y_pos
            xalign start_pos alpha 0.2 
            easein duration  xalign end_pos  
            repeat 3
    contains:
        image_path
        yanchor y_anch ypos y_pos
        xalign start_pos alpha 0.3  
        easein duration + 0.2 xalign end_pos  
        block:
            image_path
            yanchor y_anch ypos y_pos
            xalign end_pos alpha 0.3 
            easein duration xalign start_pos 
            image_path
            yanchor y_anch ypos y_pos
            xalign start_pos alpha 0.3 
            easein duration  xalign end_pos 
            repeat 3

    contains:
        image_path
        yanchor y_anch ypos y_pos
        xalign start_pos alpha 0.5 
        easein duration + 0.1 xalign end_pos 
        block:
            image_path
            yanchor y_anch ypos y_pos
            xalign end_pos alpha 0.5 
            easein duration  xalign start_pos
            image_path
            yanchor y_anch ypos y_pos
            xalign start_pos alpha 0.5 
            easein duration  xalign end_pos

            repeat 3

    contains:
        image_path
        yanchor y_anch ypos y_pos
        xalign start_pos alpha 0.9 
        easein duration xalign end_pos
        image_path
        yanchor y_anch ypos y_pos
        xalign end_pos alpha 0.9 
        easein duration xalign start_pos
        
        repeat 3
    


init python:
    import math
    class Shaker(object):
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child
        def __call__(self, t, sizes):
            # Float to integer... turns floating point numbers to
            # integers.
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x
            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]
            xpos = xpos - xanchor
            ypos = ypos - yanchor
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            return (int(nx), int(ny), 0, 0)
    def _Shake(start, time, child=None, dist=100.0, **properties):
        move = Shaker(start, child, dist=dist)
        return renpy.display.layout.Motion(move,
            time,
            child,
            add_sizes=True,
            **properties)
    Shake = renpy.curry(_Shake)
    shake = Shaker((0, 0, 0, 0), 0.5, dist=8)
