


image ILY_Sword_Draw:
    zoom 0.75 
    block:
        "images/CG/ILY_Anim_1/ILYAnim1.png"
        pause .5
        "images/CG/ILY_Anim_1/ILYAnim2.png"
        pause .2
        "images/CG/ILY_Anim_1/ILYAnim3.png"
        pause .2
        "images/CG/ILY_Anim_1/ILYAnim4.png"
        pause .1
        "images/CG/ILY_Anim_1/ILYAnim5.png"
        pause .08
        "images/CG/ILY_Anim_1/ILYAnim6.png"
        pause .1
        "images/CG/ILY_Anim_1/ILYAnim7.png"
        pause .08
        "images/CG/ILY_Anim_1/ILYAnim8.png"
        pause .2
        "images/CG/ILY_Anim_1/ILYAnim9.png"
        pause .2
        "images/CG/ILY_Anim_1/ILYAnim10.png"
        pause .2
        "images/CG/ILY_Anim_1/ILYAnim11.png"
        pause .2
        "images/CG/ILY_Anim_1/ILYAnim12.png"
        pause .2
        "images/CG/ILY_Anim_1/ILYAnim13.png"
        pause .2
        "images/CG/ILY_Anim_1/ILYAnim14.png"
        pause .2
        "images/CG/ILY_Anim_1/ILYAnim15.png"
        pause .3
        "images/CG/ILY_Anim_1/ILYAnim16.png"
        pause .2
        "images/CG/ILY_Anim_1/ILYAnim17.png"
        pause .1
        "images/CG/ILY_Anim_1/ILYAnim18.png"
        pause .1
        "images/CG/ILY_Anim_1/ILYAnim19.png"
        pause .2
        "images/CG/ILY_Anim_1/ILYAnim20.png"
        pause .2
        "images/CG/ILY_Anim_1/ILYAnim21.png"
        pause .2
        "images/CG/ILY_Anim_1/ILYAnim22.png"
        pause .2
        "images/CG/ILY_Anim_1/ILYAnim23.png"
        pause .2
        "images/CG/ILY_Anim_1/ILYAnim24.png"
        pause .2
        "images/CG/ILY_Anim_1/ILYAnim25.png"
        pause 1.0 
image CodeRedLambdaSaber:
    zoom 0.39 xalign 0.5 yalign 0.5
    block:
        "images/CG/CodeRed_LambdaSaber/CodeRedlambdasaber_1.png"
        pause .08
        "images/CG/CodeRed_LambdaSaber/CodeRedlambdasaber_2.png"
        pause .08  
        "images/CG/CodeRed_LambdaSaber/CodeRedlambdasaber_3.png"
        pause .08  
        "images/CG/CodeRed_LambdaSaber/CodeRedlambdasaber_4.png"
        pause .08         
        repeat
        
        
    
label ILY_Draws_Sword:
    $ quick_menu = False
    scene black
    show ILY_Sword_Draw
    play sound ["<silence 0.5>","<from 1.0>voice/ILY/ILY05C - Swing medium sword sounds.mp3"] 
    pause 1.0
    
    play sound "sfx/shining.mp3" 
    play sound "sfx/magic-whoosh.mp3" channel 1
    pause 0.46
    play sound "sfx/Mechasounds/A013.wav"
    pause 1.0
    play sound "sfx/draw2.mp3"
    pause 0.01
    play sound "sfx/swing.wav" channel 1
    pause 0.9
    play sound "sfx/sword_schwing.mp3"
    pause 0.5
    play sound "sfx/slash.wav" channel 1
    pause 10.0
    # jump ILY_Draws_Sword
    hide ILY_Sword_Draw
    $ quick_menu = True
    return





label CodeRedLambdaSaber:
    show CodeRedLambdaSaber  
    show white:
        alpha 1.0
        linear 0.5 alpha 0.0
    

    return