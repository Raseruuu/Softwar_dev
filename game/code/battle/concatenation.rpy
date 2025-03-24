image speedbg:
    "Characters/GUNVAR/speedbg.png"
image radialbg:
    "Characters/GUNVAR/radialbg.png"
image speedspikes:
    "Characters/GUNVAR/speedspikes.png"
image GUNVARcloseup:
    "Characters/GUNVAR/GUNVARcloseup.png"
    zoom 5.0 xalign 0.5 yalign 0.5
    easein 1.2 zoom 1.0
image GearframeUnitron:
    "Characters/GUNVAR/GearframeUnitron.png"
image NucleusVernier:
    "Characters/GUNVAR/NucleusVernier.png"
image AccelRiser:
    "Characters/GUNVAR/AccelRiser.png"
image GattaiBeam:
    "Characters/GUNVAR/GattaiBeam.png"
image GUNVAR:
    "Characters/GUNVAR/GUNVAR.png"
image GUNVARLockInBottom:
    "Characters/GUNVAR/GUNVARLockInBottom.png"

image GUNVARLockInBottom_Activate:
    "Characters/GUNVAR/GUNVARLockInBottom_Activate.png"

image GUNVARLockInDim:
    "Characters/GUNVAR/GUNVARLockInDim.png"
    alpha 1.0
    linear 1.0 alpha 0.0

image GUNVARLockInTop:
    "Characters/GUNVAR/GUNVARLockInTop.png"

image GUNVARLockInTop2:
    "Characters/GUNVAR/GUNVARLockInTop2.png"

image GUNVARLockInEyes:
    "Characters/GUNVAR/GUNVARLockInEyes1.png"
    pause 0.05
    "Characters/GUNVAR/GUNVARLockInEyes2.png"
    pause 0.03
    Null()
    pause 0.01
    "Characters/GUNVAR/GUNVARLockInEyes1.png"
    pause 0.02
    "Characters/GUNVAR/GUNVARLockInEyes2.png"
    pause 0.05
    "Characters/GUNVAR/GUNVARLockInEyes3.png"
    pause 0.02
    Null()
    pause 0.01
    "Characters/GUNVAR/GUNVARLockInEyes2.png"
    pause 0.05
    Null()
    pause 0.01
    "Characters/GUNVAR/GUNVARLockInEyes4.png"
    pause 0.05
    "Characters/GUNVAR/GUNVARLockInEyes3.png"
    pause 0.02
    "Characters/GUNVAR/GUNVARLockInEyes4.png"
    pause 0.05
    easein 0.7 alpha 0.0

image GattaiLightning:
    choice:
        "Characters/GUNVAR/GattaiLightning1.png"
        pause 0.05
        Null()
        pause 0.05
        "Characters/GUNVAR/GattaiLightning1.png"
        pause 0.05
        Null()
        pause 0.05
        "Characters/GUNVAR/GattaiLightning2.png"
        pause 0.05
    choice:
        "Characters/GUNVAR/GattaiLightning2.png"
        pause 0.05
        Null()
        pause 0.05
        "Characters/GUNVAR/GattaiLightning2.png"
        pause 0.05
        Null()
        pause 0.05
        "Characters/GUNVAR/GattaiLightning3.png"
        pause 0.05
    choice:
        "Characters/GUNVAR/GattaiLightning3.png"
        pause 0.05
        Null()
        pause 0.05
        "Characters/GUNVAR/GattaiLightning3.png"
        pause 0.05
        Null()
        pause 0.05
        "Characters/GUNVAR/GattaiLightning1.png"
        pause 0.05
    repeat

    
label cutscene_gunvar:
    hide screen battlestats
    scene black
    $ ILY_m="smile"
    $ ILY_e="normal"
    show ILY
    
    play music "bgm/ost/BOSSBATTLE-C_by_StarryMarshmell_0.ogg"
    i"Engage!"
    $ ILY_m="frown"
    $ ILY_e="down"
    # $ EquipDress("outfit","bladearmor")
    $ ILY_outfit="bladearmor"
    pause 0.02
    show ILY 
    show white:
        alpha 1.0
        pause 0.1
        linear 0.2 alpha 0.0
    pause 0.7
    i"Initiate Combination Algorithm!{w=0.7}{nw}"
    # show ILY:
    #     easein 0.7 zoom 0.4
    # show white onlayer overlay:
    #     alpha 0.0
    #     linear 0.3 alpha 1.0
    
    i"Concatenate!{w=0.5}{nw}"
    $ILY_w=True    
    scene speedbg
    show speedspikes:
        ypos 1.0 yanchor 0.0 xzoom -1.0
        linear 0.3 ypos 0.0 yanchor 1.0  
        repeat
    show speedspikes as speedspikes2:
        pause 0.15
        xoffset 40
        block:
            ypos 1.0 yanchor 0.0 xzoom -1.0
            linear 0.3 ypos 0.0 yanchor 1.0
            repeat
    pause 0.5
    
    show GearframeUnitron:
        xalign 0.40 yalign 0.5 zoom 0.3 
        linear 0.4 zoom 0.1
    pause 0.4
    with Shake((0, 0, 0, 0), 0.5, dist=40)
    i"Gearframe Unitron!{w=0.4}{nw}"
    show GearframeUnitron:
        linear 0.4 xalign 0.3 
    show NucleusVernier:
        xalign 0.5 yalign 0.5 zoom 0.3 
        linear 0.4 zoom 0.1
    pause 0.4
    with Shake((0, 0, 0, 0), 0.5, dist=40)
    i"Nucleus Vernier!{w=0.4}{nw}"
    show AccelRiser:
        xalign 0.78 yalign 0.5 zoom 0.3 
        linear 0.4 zoom 0.1
    pause 0.4
    with Shake((0, 0, 0, 0), 0.5, dist=40)
    i"Accel Riser!{w=0.4}{nw}"
    show AccelRiser:
        easein 0.5 xalign 0.5 yalign 0.04 zoom 0.08
    show NucleusVernier:
        easein 0.5 xalign 0.5 yalign 0.35 zoom 0.08
    show GearframeUnitron:
        easein 0.5 xalign 0.5 yalign 0.7 zoom 0.08
    i"Join Together!! {w=0.5}{nw}"
    # label cutscene_gunvar:
    # show screen whiteflash
    scene black
    show GattaiBeam:
        xzoom 0.1 xalign 0.5 yzoom 1.0
    hide AccelRiser
    hide NucleusVernier
    hide GearframeUnitron
    
    pause 0.2
    
    show GattaiBeam :
        xalign 0.5
        ease 0.4 alpha 1.0 xzoom 4.0 xalign 0.5 yzoom 1.0
    
    pause 0.4

    scene white
    show GUNVARLockInBottom:
        xalign 0.5 yalign 0.5
    show GUNVARLockInTop:
        yoffset 0 xalign 0.5 yalign 0.5
        easein 0.8 yoffset-30
    pause 0.8
    
    show GUNVARLockInBottom_Activate:
        xalign 0.5 yalign 0.5
    show GUNVARLockInTop2:
        xalign 0.5 yalign 0.5
    hide GUNVARLockInTop
    show GUNVARLockInDim:
        xalign 0.5 yalign 0.5
    show GUNVARLockInEyes:
        xalign 0.5 yalign 0.5


    pause 1.1
    scene white
    scene speedbg with Dissolve(0.1)
    show speedspikes:
        ypos 1.0 yanchor 0.0 xzoom -1.0
        linear 0.3 ypos 0.0 yanchor 1.0  
        repeat
    show speedspikes as speedspikes2:
        pause 0.15
        xoffset 40
        block:
            ypos 1.0 yanchor 0.0 xzoom -1.0
            linear 0.3 ypos 0.0 yanchor 1.0
            repeat
    show GUNVAR:
        xpos 0.5 xanchor 0.48 ypos 0.0 zoom 0.34 yanchor 1.0
        linear 2.0 ypos 0.5 yanchor 0.2
    

    pause 2.1
    scene white
    pause 0.1
    scene radialbg: 
        yalign 0.0
    show GattaiLightning:
        xalign 0.5 yanchor 0.3 ypos 0.3
    show GUNVAR:
        zoom 0.25 xpos 0.5 xanchor 0.48
    $ ILY_m="smile"
    $ ILY_e="down"
    
    i"Operation Complete! Enter, Virtual Mobile Armor - GUNVAR!"
    $ ILY_m="smile3"
    i"It's showtime!"
    scene battlebg
    show battlebg2
    with pixellate
    hide GUNVAR
    hide GattaiLightning
    hide radialbg
    
    show screen battlestats
    show battlering:
        xalign 0.5 ypos 0.20 yanchor 0.5
        block:
            rotate 0
            linear 15.0 rotate 360
            repeat
    show curve:
        xpos 0.5 xanchor 0.0 ypos 0.15 yanchor 0.5
    show curve as curve2:
        xpos 0.5 xanchor 1.0 ypos 0.17 yanchor 0.5
        zoom -1.0

    show battleroad:
        yalign 1.0 xalign 0.5
    show Enemy:
        xalign 0.5 yanchor 0.32 ypos 0.3 
    return
