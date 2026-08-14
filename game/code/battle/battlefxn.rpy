init python:
    runnumber=0
    maxstatuslength=16
    class Card:
        def __init__(self,name,magnitude):
            self.name = name
            self.magnitude = magnitude
    def statusAppend(stslist,statusstring):
        if len(stslist)==maxstatuslength:
            stslist.pop(0)
            #FIFO First in, First out.
        stslist.append(statusstring)
        return stslist
default enemyHP_stay =enemyHP
default playerHP_stay =playerHP
image bit:
    "gui/Bit.png"
    zoom 4.0
label TYPE_sfx:
    if currentcardTYPE == "Sword" or "Saber" in currentcardTYPE or "Sword" in currentcardTYPE:
        play sound "sfx/slashswing.wav" channel 1
        pause 0.02
        play sound "sfx/slash4.wav" channel 1
    elif "Slash" in currentcardTYPE:
        play sound "sfx/slash2.wav" channel 1
    elif currentcardTYPE == "Axe":
        play sound "sfx/slash3.wav" channel 1
    elif currentcardTYPE == "Gun":
        play sound "sfx/gun2.wav" channel 1
    elif currentcardTYPE == "Buster":
        play sound "sfx/Bust.wav" channel 1
    elif currentcardTYPE == "Bomb":
        play sound "sfx/bomb.wav" channel 1
    elif currentcardTYPE == "Drill":
        play sound "sfx/drill.wav" channel 1
    if "Fire" in currentcardTYPE:
        play sound "sfx/fire2.wav" channel 1
    elif currentcardTYPE == "Wind":
        play sound "sfx/wind.wav" channel 1
    $ attacknumber+=1
    if attacknumber<=3:
        play sound "sfx/Damage2.wav"
    elif attacknumber>3:    
        play sound "sfx/sfx_exp_short_hard8.wav"  
    else:
        play sound "sfx/sfx_exp_short_hard8.wav" 
    return
label TYPE_delay:
    if "Drill" in currentcardTYPE or "LambdaSaber" in currentcard.NAME :
            $ renpy.pause(0.1,hard=True)
    elif "MailSword" in currentcardTYPE or "RecursiveSlash" in currentcard.NAME:
        $ renpy.pause(0.2,hard=True)
    elif "Eraser" or "GUNVAR" in currentcardTYPE:
        
        $ renpy.pause(0.15,hard=True)
    else:
        $ renpy.pause(0.6,hard=True)
    return
image damageeffect:
    xalign 0.5 yanchor 0.32 ypos 0.23
    choice:
        "images/battle/dmgeffect1.webp"
        pause 0.025
        "images/battle/dmgeffect2.webp"
        pause 0.025
        "images/battle/dmgeffect3.webp"
        pause 0.025
    choice:
        "images/battle/dmgeffect1.webp"
        rotate 10+renpy.random.randint(0,100)
        pause 0.025
        "images/battle/dmgeffect2.webp"
        pause 0.025
        "images/battle/dmgeffect3.webp"
        pause 0.025
    choice:
        "images/battle/dmgeffect1.webp"
        rotate -60
        pause 0.025
        "images/battle/dmgeffect2.webp"
        pause 0.025
        "images/battle/dmgeffect3.webp"
        pause 0.025
    choice:
        "images/battle/dmgeffect1.webp"
        rotate 30+renpy.random.randint(0,100)
        xzoom -1.0
        pause 0.025
        "images/battle/dmgeffect2.webp"
        xzoom -1.0
        pause 0.025
        "images/battle/dmgeffect3.webp"
        xzoom -1.0
        pause 0.025
    choice:
        "images/battle/dmgeffect1.webp"
        rotate 80+renpy.random.randint(0,100)
        xzoom -1.0
        pause 0.025
        "images/battle/dmgeffect2.webp"
        xzoom -1.0
        pause 0.025
        "images/battle/dmgeffect3.webp"
        xzoom -1.0
        pause 0.025
    linear 0.3 alpha 0.0

# label RemoveTokenEnemy:
#     $ tokenname = currentcard_fxn_params[0]
#     $ remove_target = currentcard_fxn_params[1]
#     if remove_target=="Self":
#         $ EnmySts.remove(tokenname)
#         show screen tokenremove_anim(tokenname,"enemy")
#         $ renpy.pause(0.4,hard=True)
#         hide screen tokenremove_anim
#     elif remove_target=="Enemy":
#         $ PlayerSts.remove(tokenname)
#         show screen tokenremove_anim(tokenname,"player")
#         $ renpy.pause(0.4,hard=True)
#         hide screen tokenremove_anim
    
#     return
# label RemoveTokenPlayer:
#     if currentcardFXN[fxnindex].name=="While" or currentcardFXN[fxnindex].name=="For" or currentcardFXN[fxnindex].name=="ForInRange" or currentcardFXN[fxnindex].name=="If" or (len(currentcardFXN[fxnindex].params)>=5):
#         pass
#     else:    
#         $ currentcard_fxn_params=currentcardFXN[fxnindex].params
#     $ tokenname = currentcard_fxn_params[0]
#     $ remove_target = currentcard_fxn_params[1]
#     if remove_target=="Self":
#         $ PlayerSts.remove(tokenname)
#         show screen tokenremove_anim(tokenname,"player")
#         $ renpy.pause(0.4,hard=True)
#         hide screen tokenremove_anim
#     elif remove_target=="Enemy":
#         $ EnmySts.remove(tokenname)
        
#         show screen tokenremove_anim(tokenname,"enemy")

#         $ renpy.pause(0.4,hard=True)
#         hide screen tokenremove_anim

#     return
label Damageenemy(params):
    
    if currentcardFXN[fxnindex].name=="While" or currentcardFXN[fxnindex].name=="For" or currentcardFXN[fxnindex].name=="ForInRange" or currentcardFXN[fxnindex].name=="If" or (currentcardFXN[fxnindex].name=="Attack" and len(currentcardFXN[fxnindex].params)>5):
        $ block_functions_ATK=[]
        pass
    else:    
        $ currentcard_fxn_params=currentcardFXN[fxnindex].params
    if currentcardFXN[fxnindex].name=="Attack" and len(currentcardFXN[fxnindex].params)>3:
        $ block_functions_ATK=currentcard_fxn_params[3]
    else:
        $ block_functions_ATK=[]
    # if currentcard_fxn_params[0]!="POWR" and currentcard_fxn_params[0]: 
    $ damagemultiplier = currentcard_fxn_params[0]
    $ absolutedamage = currentcard_fxn_params[2]
    # "ATTACK BLOCK [block_functions]"
    $ Power = (currentcardPOW)
    if absolutedamage:
        $ damagetoenemy=int(damagemultiplier)
    else: 
        if damagemultiplier=="POWR":
            $ damagetoenemy=int(playerATK_m*Power)
        elif damagemultiplier!="POWR": 
            $ damagetoenemy=int(playerATK_m*damagemultiplier)
    $ attackrange = currentcard_fxn_params[1]
    $ attackhit=True
    $ battle_distance_old=battle_distance
    ## EVADE
    
    # elif attackhit:
    if battle_distance>attackrange:
            
        $ attackhit=False
        # show Enemy:
        #     xalign 0.5 yanchor 0.32 ypos 0.3
        $ enemy_evasion_active=True
        
        play sound "sfx/miss.wav" channel 1
        show Enemy at sidesteps_effect_dodge("Enemy", 0.5, renpy.random.choice([0.6,0.4]), 0.12)
            # yanchor 1.0 ypos 0.5
            # yanchor 0.32 ypos 0.3
            # yoffset 1.0
        pause 0.24
        $ enemy_evasion_active=False
        show Enemy:
            alpha 1.0
            xalign 0.5 yanchor 0.3 ypos 0.3 
        call battlemessage("MISSED!")
        call Advance(params={"quantity":1})
        if battle_distance==0 and battle_distance_old>0:
            call battlemessage("DISTANCE:ZERO")
        $ renpy.pause(0.2,hard=True)
        return
        
    if "Evade" in EnmySts:
    #     $ attackhit=False
    # if not attackhit:
        $ EnmySts.remove('Evade') 
        $ enemy_evasion_active=True
        pause 0.1
        show screen tokenremove_anim("Evade","enemy")
        $ renpy.pause(0.4,hard=True)
        hide screen tokenremove_anim
        play sound "sfx/miss.wav" channel 1
        show Enemy at sidesteps_effect_dodge("Enemy", 0.5, renpy.random.choice([0.6,0.4]), 0.12)
        pause 0.24
        $ enemy_evasion_active=False
        show Enemy:
            xalign 0.5 yanchor 0.3 ypos 0.3 
        call battlemessage("EVADED")
    # NO EVADE    
    else:
        $ enemy_being_damaged=True
        $ enemyHP_stay = enemyHP
        call TYPE_sfx
        call hurtnoise_enemy
        python:
            if enemySP>0:
                enemySP-=damagetoenemy
                if enemySP<0:
                    enemyHP+=enemySP
                    enemySP = 0
            else:
                enemyHP-=damagetoenemy

            if enemyHP <=0:
                enemyHP = 0
                
                battle_done=True
            dmgdist = ((currentcard.POW*100)/20)
            dmgdist = int(dmgdist*2.7)
        hide damageeffect
        show damageeffect
        show dmgpoint onlayer overlay
        show Enemy:
            linear 0.05 zoom 0.94
            xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
            pause .05
            xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.8
            pause .05
            xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
            pause 0.05
            xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
            pause 0.05
            xoffset 0 yoffset 0
            linear 0.05 zoom 1.0

        $ renpy.pause(0.6,hard=True)
        call TYPE_delay
        show Enemy:
            alpha 1.0
            xalign 0.5 yanchor 0.3 ypos 0.3
            
        hide damageeffect
        $ enemy_being_damaged=False
        if block_functions_ATK !=[]:
            $ block_count_ATK = 0
            label block_loopatk:
                $ runfxnstringatk = block_functions_ATK[block_count_ATK].name
                $ newfunctionparam=block_functions_ATK[block_count_ATK].params
                call functioneffects(runfxnstringatk,newfunctionparam)
                $ block_count_ATK+=1
                if block_count_ATK<len(block_functions_ATK):
                    jump block_loopatk
    
    
    return

label DamageSPplayer(params={}):
    # EVADE
    if "Evade" in PlayerSts:
        $ attackhit=False
        $ PlayerSts.remove('Evade')
        call battlemessage("EVADED")
    ## NO EVADE
    else:
        if playerSP>0:
            $ Magnitude = (currentcardPOW)
            $ damagetoplayer=int(enemyATK_m*Magnitude)
            
            call TYPE_sfx
            play sound "sfx/noise.wav"
            
            $ playerSP-=damagetoplayer
            if playerSP<0:
                $ playerSP=0

            $ dmgdist = ((currentcard.POW*100)/20)
            $ dmgdist = int(dmgdist*2.7)

            show playerdmgpoint onlayer overlay
            # call hurtnoise
            call hurtnoise
            # with Shake((0, 0, 0, 0), 0.5, dist=dmgdist)
            # $ renpy.pause(0.6,hard=True)
    return
label DamageSPenemy(params={}):
    ## EVADE
    if "Evade" in EnmySts:
        $ attackhit=False
        $ EnmySts.remove('Evade')
        play sound "sfx/miss.wav" channel 1
        show Enemy at sidesteps_effect_dodge("Enemy", 0.5, renpy.random.choice([0.6,0.4]), 0.12)
        pause 0.2
        show Enemy
        call battlemessage("EVADED")
    ## NO EVADE
    else:
        if enemySP>0:
            $ Magnitude = (currentcardPOW)
            $ damagetoenemy=int(playerATK_m*Magnitude)
            call TYPE_sfx
            call hurtnoise_enemy
            $ enemySP-=damagetoenemy
            if enemySP<0:
                $ enemySP=0
            $ dmgdist = ((currentcard.POW*100)/20)
            $ dmgdist = int(dmgdist*2.7)
            show dmgpoint onlayer overlay
            show Enemy:
                linear 0.05 zoom 0.94
                xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
                pause .05
                xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.8
                pause .05
                xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
                pause 0.05
                xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
                pause 0.05
                xoffset 0 yoffset 0
                linear 0.05 zoom 1.0
            $ renpy.pause(0.6,hard=True)
            show Enemy:
                alpha 1.0
                xalign 0.5 yanchor 0.3 ypos 0.3 
    return
label DamageSPselfenemy(params={}):
    if enemySP>0:
        $ Magnitude = (currentcardPOW)
        $ damagetoenemy=int(enemyATK_m*Power)

        call TYPE_sfx
        call hurtnoise_enemy
        $ enemySP-=damagetoenemy
        if enemySP<0:
            $ enemySP=0
        $ dmgdist = ((currentcard.POW*100)/20)
        $ dmgdist = int(dmgdist*2.7)
        show dmgpoint
        show Enemy:
            linear 0.05 zoom 0.94
            xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
            pause .05
            xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.8
            pause .05
            xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
            pause 0.05
            xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
            pause 0.05
            xoffset 0 yoffset 0
            linear 0.05 zoom 1.0
        $ renpy.pause(0.6,hard=True)
        show Enemy:
                alpha 1.0
                xalign 0.5 yanchor 0.3 ypos 0.3 
    return
label Burnenemy:
    play sound "sfx/fire.wav"
    # $ EnmySts.append("Burn")
    $ EnmySts=statusAppend(EnmySts,"Burn")
    show Brnsts:
        zoom 1.3 xalign 0.5 yanchor 1.0 ypos 0.35 alpha 1.0
        linear 0.1 zoom 0.98
        linear 0.2 zoom 1.0 alpha 0.0
    call updatestats_enemy
    call TYPE_delay
    hide Brnsts
    
    return
# label Retreatplayer(distanceamount=0,params={}):
#     if currentcardFXN[fxnindex].name=="While" or currentcardFXN[fxnindex].name=="If" or (currentcardFXN[fxnindex].name=="Attack" and len(currentcardFXN[fxnindex].params)<5):
#         pass
#     else:    
#         $ currentcard_fxn_params=currentcardFXN[fxnindex].params

#     # $ currentcard_fxn_params=currentcardFXN[fxnindex].params
#     if distanceamount==0:
#         $ distance_quantity = currentcard_fxn_params[0]
#     else:
#         $ distance_quantity = distanceamount
#     python:
#         for dist in range(0,distance_quantity):

#             battle_distance=battle_distance+1
#             renpy.show("Enemy")
#             renpy.play("sound/stepfar.wav","sound")
#             renpy.pause(0.3,hard=True)
        
#     call updatestats_player
#     return



label ReduceBitself(params={}):
    play sound "sfx/sfx_exp_odd3.wav"
    $ playerbits-=params["quantity"]
    $ dmgdist = 10
    show bit onlayer overlay:
        xalign 0.5 ypos 0.78 yanchor 0.5
        linear 0.05 zoom 0.96
        xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
        pause .05
        xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.6
        pause .05
        xoffset (dmgdist) yoffset (dmgdist) alpha 0.5
        pause 0.05
        xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
        pause 0.05
        ease 0.2 xoffset 0 yoffset 0 alpha 0.0
    $ renpy.pause(0.6,hard=True)
    hide bit
    return
label ReduceBit(params={}):
    play sound "sfx/sfx_exp_odd3.wav"
    $ enemybits-=params["quantity"]
    $ dmgdist = 10
    show bit onlayer overlay:
        xalign 0.5 ypos 0.25 yanchor 0.5
        linear 0.05 zoom 0.96
        xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
        pause .05
        xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.6
        pause .05
        xoffset (dmgdist) yoffset (dmgdist) alpha 0.5
        pause 0.05
        xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
        pause 0.05
        ease 0.2 xoffset 0 yoffset 0 alpha 0.0
    $ renpy.pause(0.6,hard=True)
    hide bit
    return

# label Burnself:
#     play sound "sfx/fire.wav"
#     # $ PlayerSts.append("Burn")
#     $ PlayerSts=statusAppend(PlayerSts,"Burn")
#     show Brnsts onlayer overlay:
#         zoom 1.3 xpos 0.15 xanchor 0.5 yanchor 1.0 ypos 0.35 alpha 1.0
#         linear 0.1 zoom 0.98
#         linear 0.2 zoom 1.0 alpha 0.0
#     # $ renpy.pause(0.6,hard=True)
#     if "Drill" in currentcardTYPE:
#         $ renpy.pause(0.2,hard=True)
#     else:
#         $ renpy.pause(0.8,hard=True)
#     hide Brnsts
#     return
# label Emailenemy:
    play sound "sfx/sfx_coin_cluster6.wav"
    # $ EnmySts.append("Burn")
    $ EnmySts=statusAppend(EnmySts,"email")
    show Emailsts:
        zoom 1.3 xalign 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
        linear 0.1 zoom 0.98
        linear 0.2 zoom 1.0 alpha 0.0
    $ renpy.pause(0.6,hard=True)
    hide Emailsts
    return
screen tokenappend_anim(tokenname,target="player"):
    text "[tokenname]" at tokenappend_trans(target):
        style "statusoutlines"
screen tokenremove_anim(tokenname,target):
    text "[tokenname]" at tokenremove_trans(target):
        style "statusoutlines"
transform tokenappend_trans(appendtarget):
    zoom 1.3 xalign 0.5 yanchor 1.0 ypos (0.41 if appendtarget=="enemy" else 0.97)alpha 0.0
    linear 0.1 zoom 0.98 alpha 1.0
    pause 0.2
    ease 0.1 zoom 1.0 yoffset 24 alpha 0.0
transform tokenremove_trans(removetarget):
    zoom 0.9 xalign 0.5 yanchor 1.0 ypos (0.41 if removetarget=="enemy" else 0.97) alpha 1.0
    linear 0.1 zoom 1.0
    pause 0.2
    ease 0.1 zoom 1.2 yoffset -24 alpha 0.0


label GainTokenEnemy(params={}):
    $ tokenname = params[tokenname]
    $ quantity = params[quantity]
    # $ EnmySts.append("Burn")
    $ counter=0
    label tokenquant_loop3:
        play sound "sfx/tokengain.mp3"
        $ EnmySts=statusAppend(EnmySts,tokenname)
        show screen tokenappend_anim(tokenname,"enemy")
        $ renpy.pause(0.4,hard=True)
        hide screen tokenappend_anim
        hide text
        $ counter+=1
        if counter<quantity:
            jump tokenquant_loop3
    call updatestats_enemy
    return

label EvadeEnemy(params={}):
    $ tokenname = params["tokenname"]
    $ quantity = params["quantity"]
    # $ EnmySts.append("Burn")
    $ counter=0
    label tokenquant_loop4:
        play sound "sfx/tokengain.mp3"
        $ EnmySts=statusAppend(EnmySts,tokenname)
        show screen tokenappend_anim(tokenname,"enemy")
        $ renpy.pause(0.4,hard=True)
        hide screen tokenappend_anim

        $ counter+=1
        if counter<quantity:
            jump tokenquant_loop4
    return

label EvadePlayer(params={}):
    
    $ tokenname = params["tokenname"]
    $ quantity = params["quantity"]
    $ counter=0
    label tokenquant_loop5:
        play sound "sfx/tokengain.mp3"
        $ PlayerSts=statusAppend(PlayerSts,tokenname)
        show screen tokenappend_anim(tokenname,"player")
        $ renpy.pause(0.4,hard=True)
        hide screen tokenappend_anim
        hide text
        
        $ counter+=1
        if counter<quantity:
            jump tokenquant_loop5
    return
label IncreaseATK(params={}):

    play sound "sfx/sfx_sounds_powerup16.wav"
    $ Power=currentcardPOW
    # $ PlayerSts.append("IncreaseATK")
    $ currentcard_fxn_params=currentcardFXN[fxnindex].params

    # $ PlayerSts=statusAppend(PlayerSts,["IncreaseATK",currentcard_fxn_params[1]])
    $ PlayerSts=statusAppend(PlayerSts,"IncreaseATK")
    call updatestats_player
    show IncreaseATKsts onlayer overlay:
        zoom 1.3 xpos 0.5 xanchor 0.5 yanchor 1.0 ypos 0.8 alpha 1.0
        linear 0.1 zoom 0.98
        linear 0.2 zoom 1.0 alpha 0.0
      
    $ renpy.pause(0.6,hard=True)
    hide text
    return
label IncreaseDEF(params={}):

    play sound "sfx/sfx_sounds_powerup16.wav"
    $ Power=currentcardPOW
    # $ PlayerSts.append("IncreaseDEF")
    $ PlayerSts=statusAppend(PlayerSts,"IncreaseDEF")
    call updatestats_player from _call_updatestats_player_1
    show IncreaseDEFsts onlayer overlay:
        zoom 1.3 xpos 0.5 xanchor 0.5 yanchor 1.0 ypos 0.8 alpha 1.0
        linear 0.1 zoom 0.98
        linear 0.2 zoom 1.0 alpha 0.0
    $ renpy.pause(0.6,hard=True)
    hide IncreaseDEFsts
    return
# label IncreasePOWenemy:
#     play sound "sfx/sfx_sounds_powerup16.wav"
#     $ Power=currentcardPOW
#     # $ PlayerSts.append("IncreaseATK")
#     $ PlayerSts=statusAppend(PlayerSts,"IncreasePOW")
#     call updatestats_enemy from _call_updatestats_enemy
#     show IncreasePOWsts onlayer overlay:
#         zoom 1.3 xpos 0.85 xanchor 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
#         linear 0.1 zoom 0.98
#         linear 0.2 zoom 1.0 alpha 0.0
#     $ renpy.pause(0.6,hard=True)
#     hide IncreasePOWsts
#     return

label WhileTokenInStatusEnemy(params={}):
#Enemy Activates While Loop
    # $ runfxnstring = currentcardFXN[fxnindex].name
    $ tokenname=params["tokenname"]
    $ block_functions=params["fxns"]
    $ targetsts=params["target"]
    # label WhileLoop:
    if targetsts == "Self":
        while tokenname in EnmySts:
            # if tokenname in PlayerSts:
            $ block_count = 0
            label block_loop:
                $ runfxnstring = block_functions[block_count].name
                $ newfunctionparam=block_functions[block_count].params
                call enemyfunctioneffects(runfxnstring,newfunctionparam)
                $ block_count+=1
                if block_count<len(block_functions):
                    jump block_loop
                # jump WhileLoop
    if targetsts == "Enemy":
        while tokenname in PlayerSts:
            # if tokenname in PlayerSts:
            $ block_count = 0
            label block_loop1:
                $ runfxnstring = block_functions[block_count].name
                $ newfunctionparam=block_functions[block_count].params
                call enemyfunctioneffects(runfxnstring,newfunctionparam)
                $ block_count+=1
                if block_count<len(block_functions):
                    jump block_loop1
                # jump WhileLoop
    return

label ForInRangePlayer(params={}):
#Player Activates For Loop
   
    $ for_iterations=params["iterations"]
    $ block_functions=params["fxns"]
    if for_iterations=="targetHP/80":
        $ for_iterations=enemyHP/80
    elif type(for_iterations)==list:
        $ tokenname = for_iterations[0]
        $ target_list = for_iterations[1]
        
        if target_list=="Self_Status":
            $ for_iterations=PlayerSts.count(tokenname)
        elif target_list=="Target_Status":
            $ for_iterations=EnmySts.count(tokenname)
    else:
        #for_iterations is an integer
        $ for_iterations=for_iterations 
    $ for_index = 0
    while for_index < for_iterations:
        # if tokenname in PlayerSts:
        $ block_count = 0
        label block_loop8:
            $ runfxnstring = block_functions[block_count].name
            $ newfunctionparam=block_functions[block_count].params
            call functioneffects(runfxnstring,newfunctionparam)
            $ block_count+=1
            if block_count<len(block_functions):
                jump block_loop8
                # jump WhileLoop
        $ for_index+=1  
    
    return
label ForInRangeEnemy(params={}):
#Enemy Activates For Loop
    
    $ for_iterations=params["iterations"]
    $ block_functions=params["fxns"]
    if for_iterations=="targetHP/80":
        $ for_iterations=playerHP/80
    elif type(for_iterations)==list:
        $ tokenname = for_iterations[0]
        $ target_list = for_iterations[1]
        
        if target_list=="Self_Status":
            $ for_iterations=EnmySts.count(tokenname)
        elif target_list=="Target_Status":
            $ for_iterations=PlayerSts.count(tokenname)
    # $ targetsts=FXN.params[2]
    # label WhileLoop:
    $ for_index = 0
    while for_index < for_iterations:
        # if tokenname in PlayerSts:
        $ block_count = 0
        label block_loop9:
            $ runfxnstring = block_functions[block_count].name
            $ newfunctionparams=block_functions[block_count].params
            call enemyfunctioneffects(runfxnstring,newfunctionparams)
            $ block_count+=1
            if block_count<len(block_functions):
                jump block_loop9
                # jump WhileLoop
        $ for_index+=1  
    return
label IfTokenInStatusEnemy(params={}):
#Enemy Activates If
    $ runfxnstring = currentcardFXN[fxnindex].name
    $ tokenname=params["tokenname"]
    $ block_functions=params["fxns"]
    $ targetsts=params["target"]
    # label WhileLoop:
    if targetsts == "Self":
        if tokenname in EnmySts:
            # if tokenname in PlayerSts:
            $ block_count = 0
            label block_loop2:
                $ runfxnstring = block_functions[block_count].name
                $ currentcard_fxn_params=block_functions[block_count].params
                call enemyfunctioneffects(runfxnstring,params=currentcard_fxn_params)
                $ block_count+=1
                if block_count<len(block_functions):
                    jump block_loop2
                # jump WhileLoop
    if targetsts == "Enemy":
        if tokenname in PlayerSts:
            # if tokenname in PlayerSts:
            $ block_count = 0
            label block_loop3:
                $ runfxnstring = block_functions[block_count].name
                $ currentcard_fxn_params=block_functions[block_count].params
                call enemyfunctioneffects(runfxnstring,params=currentcard_fxn_params)
                $ block_count+=1
                if block_count<len(block_functions):
                    jump block_loop3
                # jump WhileLoop
    return
label IfTokenInStatusPlayer(params={}):
#Player Uses If
    $ tokenname=params["tokenname"]
    $ block_functions=params["fxns"]
    $ targetsts=params["target"]
    # label WhileLoop:
    if targetsts == "Self":
        if tokenname in PlayerSts:
            # if tokenname in PlayerSts:
            $ block_count = 0
            label block_loop4:
                
                $ runfxnstring = block_functions[block_count].name
                $ newfunctionparam=block_functions[block_count].params
                call functioneffects(runfxnstring,newfunctionparam)
                $ block_count+=1
                if block_count<len(block_functions):
                    jump block_loop4
                
    elif targetsts == "Enemy":
        if tokenname in EnmySts:
            # if tokenname in PlayerSts:
            $ block_count = 0
            label block_loop5:
                $ runfxnstring = block_functions[block_count].name
                $ newfunctionparam=block_functions[block_count].params
                call functioneffects(runfxnstring,newfunctionparam)
                $ block_count+=1
                if block_count<len(block_functions):
                    jump block_loop5
            # jump WhileLoop
    return
label WhileTokenInStatusPlayer(params={}):
#Player Activates While Loop
    
    $ tokenname=params["tokenname"]
    $ block_functions=params["fxns"]
    $ targetsts=params["target"]

    if targetsts == "Self":
        while tokenname in PlayerSts:
            $ block_count = 0
            label block_loop6:
                $ runfxnstring = block_functions[block_count].name
                $ newfunctionparam=block_functions[block_count].params
                call functioneffects(runfxnstring,newfunctionparam)
                $ block_count+=1
                if block_count<len(block_functions):
                    jump block_loop6

    elif targetsts == "Enemy":
        while tokenname in EnmySts:
            $ block_count = 0
            label block_loop7:
                $ runfxnstring = block_functions[block_count].name
                $ newfunctionparam=block_functions[block_count].params

                call functioneffects(runfxnstring,newfunctionparam)
                $ block_count+=1
                if block_count<len(block_functions):

                    jump block_loop7

    return
label IncreaseATKenemy(params={}):
    play sound "sfx/sfx_sounds_powerup16.wav"
    $ Power=currentcardPOW

    # $ EnmySts.append("IncreaseDEF")
    $ EnmySts=statusAppend(EnmySts,"IncreaseATK")
    call updatestats_enemy from _call_updatestats_enemy_1
    show IncreaseATKsts onlayer overlay:
        zoom 1.3 xpos 0.85 xanchor 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
        linear 0.1 zoom 0.98
        linear 0.2 zoom 1.0 alpha 0.0
    $ renpy.pause(0.6,hard=True)
    hide IncreaseDEFsts
    return
label IncreaseDEFenemy(params={}):
    play sound "sfx/sfx_sounds_powerup16.wav"
    $ Power=currentcardPOW

    # $ EnmySts.append("IncreaseDEF")
    $ EnmySts=statusAppend(EnmySts,"IncreaseDEF")
    call updatestats_enemy from _call_updatestats_enemy_2
    show IncreaseDEFsts onlayer overlay:
        zoom 1.3 xpos 0.85 xanchor 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
        linear 0.1 zoom 0.98
        linear 0.2 zoom 1.0 alpha 0.0
    $ renpy.pause(0.6,hard=True)
    hide IncreaseDEFsts
    return
label updatestats_player:
    python:
        playerATK_m=playerATK
        playerDEF_m=playerDEF
        for fxns in PlayerSts:
                if fxns == 'IncreaseATK':
                    # boostvalue = fxns[1]
                    boostvalue = 0.25
                    playerATK_m+=playerATK*boostvalue
                    playerATK_m = int(playerATK_m)
                    # "This shit happened"
                elif fxns == 'IncreaseDEF':
                    boostvalue = 0.25
                    playerDEF_m+=playerDEF*boostvalue
                    playerDEF_m = int(playerDEF_m)
                    # "This shit happened"
    hide screen battlestats
    show screen battlestats

    return
label updatestats_enemy:
    python:
        enemyATK_m=enemyATK
        enemyDEF_m=enemyDEF
        for fxns in EnmySts:
                if fxns == 'IncreaseATK':
                    # boostvalue = fxns[1]
                    boostvalue = 0.25
                    enemyATK_m+=enemyATK*boostvalue
                    enemyATK_m = int(enemyATK_m)
                    # "This shit happened"
                elif fxns == 'IncreaseDEF':
                    # boostvalue = fxns[1]
                    boostvalue = 0.25
                    enemyDEF_m+=enemyDEF*boostvalue
                    enemyDEF_m = int(enemyDEF_m)
    hide screen battlestats
    show screen battlestats              

    return


image shieldbit = "images/battle/Shield_bit.png"
image shieldlight = "images/battle/Shield_light.png"
image SPText:
    Text("{b}SP + "+str(shieldtoplayer)+"{/b}",style='statusoutlines')
image HPText:
    Text("{b}HP + "+str(healtoplayer)+"{/b}",style='statusoutlines_red')
image SPTextenemy:
    Text("{b}SP + "+str(shieldtoenemy)+"{/b}",style='statusoutlines')
image HPTextenemy:
    Text("{b}HP + "+str(healtoenemy)+"{/b}",style='statusoutlines_red')
    
label Shieldplayer(params={}):
    play sound "sfx/defense.wav"
    # $ multiplier = currentcardFXN[fxnindex].params[0]
    $ Power = (currentcardPOW)
   
    $ multiplier = params["multiplier"]
    if multiplier=="POWR":
        $ shieldtoplayer=int(playerDEF_m*Power)
    elif multiplier!="POWR": 
        $ shieldtoplayer=int(playerDEF_m*multiplier)
    python:
        playerSP+=shieldtoplayer
        # if playerSP>=playerSPMax:
        #     playerSP=playerSPMax
    #Animation
    show shieldlight onlayer overlay:
        alpha 0.0
        ease 0.3 alpha 1.0
        ease 0.3 alpha 0.0
    show shieldbit onlayer overlay:
        alpha 0.0 xpos 0.5 ypos 0.68 yanchor 0.5 xanchor 0.5
        ease 0.2 alpha 1.0
        ease 0.4 alpha 0.0
    show SPText onlayer overlay:
        alpha 0.0 zoom 0.0 xpos 0.5 ypos 0.85 yanchor 0.5 xanchor 0.5
        ease 0.1 alpha 1.0 zoom 1.2
        pause 0.55
        ease 0.05 alpha 0.0 zoom 1.1
    $ renpy.pause(0.6,hard=True)
    return
label ReduceSPself(params={}):
    # play sound "sfx/defense_loss.wav"
    
    $ multiplier = params["multiplier"]
    $ Power = params["POW"]
    if multiplier=="POWR":
        $ shieldtoplayer=int(playerDEF_m*Power)
    elif multiplier!="POWR": 
        $ shieldtoplayer=int(playerDEF_m*multiplier)
    python:
        playerSP-=shieldtoplayer
        # if playerSP>=playerSPMax:
        #     playerSP=playerSPMax
    #Animation
    show shieldlight:
        alpha 0.0
        ease 0.3 alpha 1.0
        ease 0.3 alpha 0.0
    show shieldbit onlayer overlay:
        alpha 0.0 xpos 0.5 ypos 0.7 yanchor 0.5 xanchor 0.5
        ease 0.2 alpha 1.0
        ease 0.4 alpha 0.0
    show text "{size=70}SP-=[shieldtoplayer]{/size}"  onlayer overlay:
        alpha 0.0 zoom 0.0 xpos 0.5 ypos 0.9 yanchor 0.5 xanchor 0.5
        ease 0.1 alpha 1.0 zoom 1.2 
        pause 0.55
        ease 0.05 alpha 0.0 zoom 1.1 yoffset -25
    $ renpy.pause(0.6,hard=True)
    return
image healbit = "images/battle/Heal_bit.png"
image heallight = "images/battle/Heal_light.png"
label Recoverplayer(params={}):
    play sound "sfx/heal.ogg"
    # $ Power = (currentcardPOW)
    # if currentcardFXN[fxnindex].name=="While" or currentcardFXN[fxnindex].name=="For" or currentcardFXN[fxnindex].name=="If":
    #     pass
    # else:    
    #     $ currentcard_fxn_params=currentcardFXN[fxnindex].params
    
    # $ multiplier = currentcard_fxn_params[0]
    # if multiplier=="POWR":
    #     $ shieldtoplayer=int(playerDEF_m*Power)
    # elif multiplier!="POWR": 
    #     $ shieldtoplayer=int(playerDEF_m*multiplier)
    $ Power = (currentcardPOW)
    
    $ healtoplayer=int(playerHPMax*Power)
    python:
        playerHP+=healtoplayer
        if playerHP>=playerHPMax:
            playerHP=playerHPMax
    #Animation
    show heallight onlayer overlay:
        alpha 0.0
        ease 0.3 alpha 1.0
        ease 0.3 alpha 0.0
    show healbit onlayer overlay:
        alpha 0.0 xpos 0.5 ypos 0.7 yanchor 0.5 xanchor 0.5
        ease 0.2 alpha 1.0
        ease 0.4 alpha 0.0
    show HPText onlayer overlay:
        alpha 0.0 zoom 0.0 xpos 0.5 ypos 0.9 yanchor 0.5 xanchor 0.5
        ease 0.1 alpha 1.0 zoom 1.2
        pause 0.55
        ease 0.05 alpha 0.0 zoom 1.1
    $ renpy.pause(0.6,hard=True)
    return
label Recoverenemy(params={}):
    play sound "sfx/heal.ogg"
    $ Power = (currentcardPOW)
    $ healtoenemy=int(enemyHPMax*Power)
    python:
        enemyHP+=healtoenemy
        if enemyHP>=enemyHPMax:
            enemyHP=enemyHPMax
    #Animation
    show heallight onlayer overlay:
        alpha 0.0
        ease 0.3 alpha 1.0
        ease 0.3 alpha 0.0

    show healbit onlayer overlay:
        alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.35
        ease 0.2 alpha 1.0
        pause 0.1
        ease 0.4 alpha 0.0
    show HPTextenemy onlayer overlay:
        alpha 0.0 zoom 0.0 xalign 0.5 yanchor 0.5 ypos 0.45
        ease 0.1 alpha 1.0 zoom 1.2
        pause 0.2
        ease 0.05 alpha 0.0 zoom 1.1
    $ renpy.pause(0.6,hard=True)
    return
label Shieldenemy(params={}):
    play sound "sfx/defense.wav"
    $ Power = (currentcardPOW)
    $ shieldtoenemy=int(enemyDEF_m*Power)
    python:
        enemySP+=shieldtoenemy
        # if enemySP>=enemySPMax:
        #     enemySP=enemySPMax
    show shieldlight onlayer overlay:
        alpha 0.0 yzoom -1.0
        ease 0.3 alpha 1.0
        ease 0.3 alpha 0.0
    show shieldbit onlayer overlay:
        alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.35
        ease 0.2 alpha 1.0
        pause 0.1
        ease 0.4 alpha 0.0
    show SPTextenemy onlayer overlay:
        alpha 0.0 zoom 0.0 xalign 0.5 yanchor 0.5 ypos 0.45
        ease 0.1 alpha 1.0 zoom 1.2
        pause 0.2
        ease 0.05 alpha 0.0 zoom 1.1
    $ renpy.pause(0.6,hard=True)
    return
label DoNothing(params={}):
    pass
    return

default player_being_damaged=False
default enemy_being_damaged=False

label Damageplayer(params={}):
    $ paramsvar=params
    # if currentcardFXN[fxnindex].name=="While" or currentcardFXN[fxnindex].name=="If" or currentcardFXN[fxnindex].name=="For" or currentcardFXN[fxnindex].name=="ForInRange" or (len(currentcardFXN[fxnindex].params)>=5):
    $ block_functions_ATK=params["onhit"] 
    $ damagemultiplier = params["multiplier"]
    $ absolutedamage = params["absolute"]
    
    $ Power = (currentcardPOW)
    
    if absolutedamage:
        $ damagetoplayer=int(damagemultiplier)
    else:
        if damagemultiplier=="POWR":
            $ damagetoplayer=int(enemyATK_m*Power)
        elif damagemultiplier!="POWR": 
            $ damagetoplayer=int(enemyATK_m*damagemultiplier)
    $ attackrange = params["rangevalue"]
    $ attackhit=True
    $ battle_distance_old=battle_distance
    ## EVADE
    
    ## NO EVADE
    
    if battle_distance>attackrange:
        call Advance(params={"quantity":1})
        $ renpy.show("Enemy")
        $ attackhit=False
        # show Enemy:
        #     xalign 0.5 yanchor 0.3 ypos 0.3
        $ evasion_active=True
        play sound "sfx/miss.wav" channel 1
        pause 0.05
        $ evasion_active=False
        call battlemessage("MISSED!")
        $ renpy.pause(0.1,hard=True)
        if battle_distance==0 and battle_distance_old>0:
            call battlemessage("DISTANCE:ZERO")
        $ renpy.pause(0.1,hard=True)
        return
    if "Evade" in PlayerSts:
        $ attackhit=False
        # $ renpy.show("Icon_[playerName]", at_list=([sidesteps_effect_dodge("Icon_[playerName]", 0.5, renpy.random.choice([0.6,0.4]), 0.12)]))
        $ evasion_active=True
        
        play sound "sfx/miss.wav" channel 1
        pause 0.05
        $ evasion_active=False
        $ PlayerSts.remove('Evade')
        show screen tokenremove_anim("Evade","player")
        $ renpy.pause(0.4,hard=True)
        hide screen tokenremove_anim
        call battlemessage("EVADED")
        $ renpy.pause(0.1,hard=True)
    else:
        $ player_being_damaged = True
        $ playerHP_stay= playerHP
        call TYPE_sfx
        hide damagetheplayer
        show damageeffect as damagetheplayer:
            yzoom 1.0 yoffset 400 zoom 2.0
        if playerSP>0:
            play sound "sfx/noise.wav" channel 2
            
            $ playerSP-=damagetoplayer
            if playerSP<0:
                #playerSP becomes a negative value if damage exceeds its value
                $ playerHP+=playerSP
                $ playerSP = 0
        else:
            play sound "sfx/Damage2.wav"

            $ playerHP-=damagetoplayer
    
        if playerHP <=0:
            $ playerHP = 0
            $ battle_done=True
        $ dmgdist = ((currentcard.POW*100)/20)
        $ dmgdist = int(dmgdist*2)
        show playerdmgpoint onlayer overlay
        # show damagenoise
        
        call hurtnoise
        hide damagenoise
        hide screen battlestats
        show screen battlestats
            
        $ attackhit=True
        $ player_being_damaged = False
        if block_functions_ATK !=[]:
            $ block_count_ATK = 0
            label block_loopatkofenemy:
                $ runfxnstringatkofenemy = block_functions_ATK[block_count_ATK].name
                $ newfunctionparam=block_functions_ATK[block_count_ATK].params
                call enemyfunctioneffects(runfxnstringatkofenemy,params=newfunctionparam)
                $ block_count_ATK+=1
                if block_count_ATK<len(block_functions_ATK):
                    jump block_loopatkofenemy
    
    hide screen battlestats
    show screen battlestats
    return
label DeckChangePlayer(params={}):
    info"[playerName]'s Deck is changed to \"GUNVAR\"."
    $ actual_playerDeck = playerDeck
    $ playerDeck=deckGUNVAR["content"]
    $ import random
    $ random.shuffle(playerDeck)
    $ playerbits=16
    $ playerbitsmax=16
    hide screen battlestats
    show screen battlestats
    return
label DeckChangeEnemy(params={}):
    info"[enemyName]'s Deck is changed to \"GUNVAR\"."
    $ enemyDeck=deckGUNVAR["content"]
    $ import random
    $ random.shuffle(enemyDeck)
    $ enemybits=16
    $ enemybitsmax=16
    hide screen battlestats
    show screen battlestats
    return
transform ringtransform:
    zoom 0.0 xpos 0.34 xanchor 0.5 ypos 0.7 yanchor 0.5 rotate 0
    linear 0.15 zoom 1.4 rotate 180 alpha 0.8
transform ringtransform2:
    zoom 0.0 xpos 0.66 xanchor 0.5 ypos 0.3 yanchor 0.5
    linear 0.15 zoom 1.4
screen cardflashscreen:
    # key "mousedown_5" action Return()
    # key "K_PAGEDOWN" action Return()
    add "ring" at ringtransform
    add "cardflash"
    key 'mouseup_1' action Return()
    key 'dismiss' action Return()
    key 'K_RETURN' action Return()
    key 'K_SPACE' action Return()
    key 'K_KP_ENTER' action Return()
    key 'K_SELECT' action Return()
    key 'z' action Return()
    key 'Z' action Return()
screen cardflashscreen2:
    # key "mousedown_5" action Return()
    # key "K_PAGEDOWN" action Return()
    # add "ring" at ringtransform
    add "cardflash2"
        # xalign 0.2 yalign 0.98

screen cardflashscreenenemy:
    # key "mousedown_5" action Return()
    # key "K_PAGEDOWN" action Return()
    add "ring2" at ringtransform2
    add "cardflashenemy"
    key 'mouseup_1' action Return()
    key 'dismiss' action Return()
    key 'K_RETURN' action Return()
    key 'K_SPACE' action Return()
    key 'K_KP_ENTER' action Return()
    key 'K_SELECT' action Return()
    key 'z' action Return()
    key 'Z' action Return()

screen cardflashscreenenemy2:
    # key "mousedown_5" action Return()
    # key "K_PAGEDOWN" action Return()
    # add "ring2" at ringtransform2
    add "cardflashenemy2"
        

label Concatenation:
    
    # "[playerbattlecode]"
    python:
        battlecodetypes=""
        for battlewarecode in playerbattlecode:
            battlecodetypes+=battlewarecode.TYPE

    # "[battlecodetypes]"   
    python:    
        concat_true=False
        card3concatenation=False
        playerbattlecode_b4concat=copy.deepcopy(playerbattlecode)
        for battle_index,card in enumerate(playerbattlecode):

            prefix_card=card
            for concat_index,Concat_str in enumerate(Concat_strings):

                if card.TYPE in Concat_str and not concat_true:
                    if battle_index<len(playerbattlecode)-1:
                        suffix_card=playerbattlecode[battle_index+1]
                        suffix_card2 = None
                        suffix_card2TYPE=""
                        if len(playerbattlecode)>battle_index+2:
                            suffix_card2=playerbattlecode[battle_index+2]
                            suffix_card2TYPE=suffix_card2.TYPE
                        nextcard=suffix_card
                        concatenated=(card.TYPE)+(nextcard.TYPE)+suffix_card2TYPE
                        # renpy.say("","[concatenated]")
                        typelength=len(card.TYPE)
                        concatword1=Concat_str[:typelength]
                        concat_true =(card.TYPE==concatword1 and Concat_str in battlecodetypes and card.TYPE!=nextcard.TYPE)
                        
                        # battlecodereduced=replace_whole_word_from_string("",battlecodetypes)
                        if suffix_card2TYPE!="" and concat_true and suffix_card2TYPE!=suffix_card.TYPE and nextcard.TYPE!=suffix_card2TYPE and card.TYPE!=suffix_card2TYPE and suffix_card2TYPE in Concat_str:
                            card3concatenation=True
                        # concat_true=(concatenated==Concat_str)
                        if concat_true:
                            concat_result= Concatenations[concat_index]
                            concat_card = Concatenations[concat_index]
                            concat_card_name = concat_card.NAME
                            renpy.call("Concat_anim",prefix_card,suffix_card,suffix_card2,concat_result)

                            
                           
    return
style concatoutlines:
    size 40
    outlines [(2, "#022168", -1, 1),(2, "#022168", 0, 0)]
label Concat_anim(prefix,suffix,suffix2,concat_result):
    call showphasemsg("CONCATENATE!") from _call_showphasemsg_2
    $ flashuser = playerName
    if card3concatenation:
        $ flashdialogue = prefix.TYPE+"-type Battleware "+prefix.NAME+",\n "+suffix.TYPE+"-type Battleware "+suffix.NAME+",\n"+suffix2.TYPE+"-type Battleware "+suffix2.NAME+"\n Concatenate! " +concat_card_name+"!"
    else:
        $ flashdialogue = prefix.TYPE+"-type Battleware "+prefix.NAME+",\n "+suffix.TYPE+"-type Battleware "+suffix.NAME+",\n Concatenate! " +concat_card_name+"!"
    $ renpy.call("FinishingFlash",flashdialogue)
    $ anim_done=False
    if concat_result.NAME=="Virtual Mobile Armor GUNVAR":
        call cutscene_gunvar
    
    call updatestats_player
    hide screen battlestats
    show screen battlestats
    $ noscreentransformsfornow=True
    play sound "sfx/swing.wav"
    show screen concat_anim(prefix,suffix,suffix2)
    pause 1.0
    show screen whiteflash
    python:

        playerbattlecode.pop(battle_index)
        playerbattlecode.pop(battle_index)
        if card3concatenation:
            playerbattlecode.pop(battle_index)
        playerbattlecode.insert(battle_index,concat_result)
    pause 0.5
    hide screen whiteflash
    hide screen concat_anim
    show white:
        alpha 1.0 xzoom 0.0 xalign 0.5 yzoom 1.0
        linear 0.2 xzoom 1.0 alpha 0.0
    play sound "sfx/slash.wav"
    show screen concatresultscreen
    pause
    hide screen concatresultscreen
    
    return
screen concatresultscreen():
    add CardDisplay(concat_result):
        xalign 0.5 yalign 0.9
screen concat_anim(prefix,suffix,suffix2):
    image "black" at pausedim2
    # add 
    # use Card(prefix,(200,400),1.0)
    # use Card(suffix,(780,400),1.0)
    # if card3concatenation:
    
    #     use Card(suffix,(780,400),1.0)
    hbox:
        xalign 0.5 yalign 0.9
        add CardDisplay(prefix)
        text " " at concat_spacing()
        add CardDisplay(suffix)
        
        if card3concatenation:
            text " " at concat_spacing()
            add CardDisplay(suffix2)
    hbox:
        xalign 0.5 yalign 0.4
    
        text "[prefix.TYPE]" style "concatoutlines"
        text " " at concat_spacing()
        text "[suffix.TYPE]" style "concatoutlines"
        
        if card3concatenation:
            text " " at concat_spacing()
            text "[suffix2.TYPE]" style "concatoutlines"

screen whiteflash:
    image "white" at flashbang2
transform concat_spacing:
    xzoom 5.0
    pause 0.8
    linear 0.2 xzoom 0.0
    
transform prefixanim:
    yalign 0.7 xalign 0.2 zoom 2.0
    pause 0.1
    linear 0.2 xpos 0.5 xanchor 1.0
    # pause 0.5
transform suffixanim:
    yalign 0.7 xalign 0.8 zoom 2.0
    pause 0.1
    linear 0.2 xpos 0.5 xanchor 0.0
    # pause 0.5
label FinishingFlash(dialogue):
    play sound "sfx/Mechasounds/Glare2.wav"
    call screen finishingflash(dialogue)
    return
transform handcard_rotator(rotateint):
    rotate rotateint transform_anchor True
    on show:
        xoffset 20 
        ease 0.1 xoffset 0 
transform handcard_positioning(phase,cardxpos,cardindex):
    xpos (0.1+cardxpos if phase=="drawphase" else cardxpos) 
    xanchor 0.5 
    ypos 0.98+(cardindex*0.02)
    yanchor 1.0
screen handcardsscreen(phase="common"):
    python:
        phand = []
        if usedcards!=[]:
            for (handindex, hand_cards) in enumerate(playerhand):
                if handindex in usedcards:
                    pass
                else:
                    phand.append(hand_cards)   
        else:
            phand=playerhand
    # text "[phase]"
    
    for cardindex,playercardobj in enumerate(phand):
        $ card_distance = (0.06 if phase=="drawphase" else (0.07*0.5))
        $ cardxpos=((0.1)+(cardindex*card_distance))

        add CardDisplayNormal(playercardobj):
            # action Play("sound","sound/Phase.wav"), Hide("cardhover"), Return("card"+str(cardindex+1))
            # hovered Show("cardhover",cardobject=playercardobj,cardhoverxpos=cardxpos), Play("sound","sfx/select.wav")
            # unhovered Hide("cardhover")
            at zoomtrans(0.8 if phase=="drawphase" else 0.6 ),handcard_rotator((cardindex-1)*10), handcard_positioning(phase,cardxpos,cardindex)
        # elif clickedcard[cardindex]:
            
        #     add "images/Cards/cardblank2.png" xpos cardxpos xanchor 0.5 yalign 0.945
        # else:
        #     add CardDisplay(playercardobj) xpos cardxpos xanchor 0.5 yalign 0.92 at zoomBattlecards
        #     add "images/Cards/cardblank2.png" at alpha08 xpos cardxpos xanchor 0.5 yalign 0.945


label Execution:
    $ runnumber = 0
    $ attacknumber = 0
    $ log_shown = True
    call remaininghand
    show screen handcardsscreen
    #Index of looper
    call Concatenation
    # call playbattlemusic(enemyName)
    
    show battlering:
        xalign 0.5 ypos 0.4 yanchor 0.5
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
        xalign 0.5 yanchor 0.3 ypos 0.3
    $ iterations =len(playerbattlecode)
    show screen phasemsg("EXECUTE")
    $ renpy.pause(0.5,hard=True)
    hide screen phasemsg

    label exec_loop:
        
        $ currentcard = playerbattlecode[0]
        call duel_log_append("card_played",currentcard,"player",PFAI)
        $ playerbattlecode.pop(0)
        # $ currentcard = (playerbattlecode[runnumber])
        $ currentcardFXN = currentcard.FXN
        $ currentcardPOW = currentcard.POW
        $ currentcardTYPE = currentcard.TYPE
        $ Power = (currentcardPOW)
        $ damagetoenemy=int(playerATK_m*Power)
        $ currentcardfunctions=[a.name for a in currentcardFXN]
        $ damagecard = ("attack" in currentcardfunctions) 
        
        hide screen battlestats
        show screen battlestats
        call battlecry from _call_battlecry
        # show ring onlayer overlay:
        #     zoom 0.0 xalign 0.5 ypos 0.7 yanchor 0.5 rotate 0
        #     linear 0.15 zoom 1.4 rotate 180 alpha 0.8

        # show cardflash onlayer overlay
        play sound "sound/swing.wav"
        call screen cardflashscreen
        show screen cardflashscreen2
        
        ##
        $ fxnindex=0
        $ loopingcard=False
        $ execution_active=True
        
        label runfunctions:
            
            $ runfxnstring = currentcardFXN[fxnindex].name
            $ runfxnparam = currentcardFXN[fxnindex].params
            hide screen cardflashscreen2
            show screen cardflashscreen2
            call functioneffects(runfxnstring,runfxnparam)
            $fxnindex+=1
            if fxnindex<len(currentcardFXN):
                jump runfunctions
        
        hide screen cardflashscreen2
        hide ring
        $ execution_active=False
        $ fxnindex=0
        $ runnumber+=1
        if (runnumber<iterations) and (battle_done==False):
            
            jump exec_loop
        else:

            call PlayerEndPhase from _call_PlayerEndPhase
            # info"[playerName]'s turn has ended."
            if not battle_done:
                call enemyattack from _call_enemyattack_1
        hide screen handcardsscreen
    return
label hurtnoise_enemy:
    call hurtnoise_Ave
    call hurtnoise_Vira
    call hurtnoise_CodeRed
    return
label PlayerEndPhase:
    if "Burn" in EnmySts:
            play sound "sfx/fire.wav"
            python:
                burndmg = 0
                for fxns in EnmySts:
                    if fxns=="Burn":
                        burndmg = burndmg +80
            
            show Brnsts:
                zoom 1.3 xalign 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
                linear 0.1 zoom 0.98
                linear 0.2 zoom 1.0 alpha 0.0
            $ enemyHP = enemyHP-burndmg
            if enemyHP <=0:
                $enemyHP = 0
                $battle_done=True
            # $ EnmySts.remove('burn')
            $ dmgdist = (burndmg/20)
            $ dmgdist = int(dmgdist*2)

            show dmgpointb onlayer overlay
            call hurtnoise_enemy
            show Enemy:
                linear 0.1 zoom 0.96
                xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
                pause .05
                xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.8
                pause .05
                xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
                pause 0.1
                xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
                pause 0.05
                xoffset 0 yoffset 0
                linear 0.1 zoom 1.0
            $ renpy.pause(0.6,hard=True)
            show Enemy:
                alpha 1.0
                xalign 0.5 yanchor 0.3 ypos 0.3 
            hide Brnsts
    $ playerbits = playerbitsmax
    return
label EnemyEndPhase:
    
    if "Burn" in PlayerSts:
            python:
                burndmg = 0
                for fxns in PlayerSts:
                    if fxns=="Burn":
                        burndmg = burndmg +80

            # i"[playerName] receives [burndmg] burn damage!"
           
            
            play sound "sfx/fire.wav"

            $ damagetoplayer = burndmg
            $ playerHP = playerHP-burndmg
            if playerHP <=0:
                $ playerHP = 0
                $ battle_done=True
            # $ EnmySts.remove('burn')
            $ dmgdist = (burndmg/20)
            $ dmgdist = int(dmgdist*2)
            $ damagetoplayer = burndmg
            show Brnsts:
                zoom 1.3 xpos 0.5 xanchor 0.5 yanchor 0.5 ypos 0.75 alpha 1.0
                linear 0.1 zoom 0.98
                linear 0.2 zoom 1.0 alpha 0.0

            show playerdmgpoint onlayer overlay
            call hurtnoise
            # with Shake((0, 0, 0, 0), 0.5, dist=dmgdist)
            # $ renpy.pause(0.6,hard=True)


            hide Brnsts
    $ enemybits= enemybitsmax
    hide screen battlestats
    show screen battlestats
    return
label enemyexecutecard:
    if enemybits>=currentcardCOST:
        # $ enemyrunnumber=enemynumberofattacks
    # else:
        $ enemybits-=currentcardCOST
        # show ring2 onlayer overlay:
        #   zoom 0.0 xalign 0.5 ypos 0.3 yanchor 0.5
        #   linear 0.15 zoom 1.4
        # show cardflashenemy onlayer overlay
        call battlecry_Ave
        call battlecry_Melissa
        call battlecry_CodeRed
        call battlecry_Vira
        play sound "sound/swing.wav"
        call screen cardflashscreenenemy
        show screen cardflashscreenenemy2
        $ fxnindex=0
        $ execution_active=True
        call duel_log_append("card_played",currentcard,"enemy",EFAI)
        label runfunctions2:
            $ runfxnstring = currentcardFXN[fxnindex].name
            $ runfxnparam = currentcardFXN[fxnindex].params
            hide screen cardflashscreenenemy2
            show screen cardflashscreenenemy2
            
            call enemyfunctioneffects(runfxnstring,runfxnparam) 

            $fxnindex+=1
            if fxnindex<len(currentcardFXN):
                jump runfunctions2
        $ execution_active=False

        hide screen cardflashscreenenemy2
        hide ring2
    return
default enemyhand=[]
default enemyreturncards=[]
label enemyattack:
    $ log_shown = True
    $ enemyrunnumber = 0
    $ enemynumberofattacks = 5 #renpy.random.randint(1,3)+renpy.random.randint(0,2)
    
    # $ enemyhand = [enemyDeck[0],enemyDeck[1],enemyDeck[2],enemyDeck[3],enemyDeck[4]]
    python:
        #Enemy hand draw
        for cardindex in range(0,5-len(enemyhand)):
            enemyhand.append(enemyDeck[0])
            enemyDeck.pop(0)
            
    show screen phasemsg(enemyName+"'S TURN")
    call duel_log_append("turn_change",None,"enemy",EFAI)
    $renpy.pause(0.9,hard=True)
    hide screen phasemsg
    
    #Buffs Priority
    $ enemyhand.sort(key=lambda x: x.FXN[0].name)
    if playerHP<= int(playerHPMax/2) or ("IncreaseATK" in EnmySts) or ("Saber" in EnmySts):
        #Damage priority
        $ enemyhand.sort(key=lambda x: x.FXN[0].name)
    elif (enemySP==0) and (enemyHP<=enemyHPMax):
        #Strongest card priority

        $ enemyhand.sort(key=lambda x: x.COST,  reverse = True)
    if "Shield" in enemyhand[0].FXN and "IncreaseATK" in [handcard.FXN for handcard in enemyhand]:
        $ enemyhand.sort(key=lambda x: x.FXN[0].name)
    # python:
    #     for cardindex in range(0,5):

            
    $ choicecount=0
    $ enemyreturncards=[]
    label enemyattackloop:
        # $ enemycardtoexecute = enemyDeck[0]

        $ currentcard = enemyhand[0]
        
        # $ enemyhand.append(currentcard)
        # $ currentcard = (playerbattlecode[runnumber])
        $ currentcardFXN = currentcard.FXN
        $ currentcardPOW = currentcard.POW
        $ currentcardTYPE = currentcard.TYPE
        $ currentcardCOST = currentcard.COST

        call enemyexecutecard from _call_enemyexecutecard
        $ enemyreturncards.append(enemyhand[0])
        $ enemyhand.pop(0)
        $ enemyrunnumber+=1
        
        if enemyrunnumber<enemynumberofattacks and (battle_done==False):
            jump enemyattackloop
        else:
            python:
                for returncard in enemyreturncards:
                    enemyDeck.append(returncard)
            call EnemyEndPhase from _call_EnemyEndPhase
            # info"[enemyName]'s turn has ended."
    return


init python:
    FxnDirectoryPlayer={
        "Attack":"Attack",
        "AttackSP":"DamageSPenemy",
        "ReduceSPself":"DamageSPplayer",
        "Defend":"Shieldplayer",
        "Recover":"Recoverplayer",
        "Burn":"Burnenemy",
        "GiveToken":"GiveToken",
        "GainToken":"GainTokenPlayer",
        "BurnSelf":"Burnself",
        "If":"IfTokenInStatusPlayer",
        "While":"WhileTokenInStatusPlayer",
        "For":"ForInRangePlayer",
        "RemoveToken":"RemoveTokenPlayer",
        "IncreaseATK":"IncreaseATK",
        "IncreaseDEF":"IncreaseDEF",
        "Increase":"IncreasePlayer",
        "ReduceBit":"ReduceBit",
        "Evade":"EvadePlayer",
        "Block":"Blockplayer",
        "Retreat":"Retreat",
        "Push":"Retreat",
        "Advance":"Advance",
        "Pull":"Advance",
        "DeckChange":"DeckChangePlayer",
        "":"DoNothing"
    }
label functioneffects(runfxnstring,params={}):
    $ renpy.call(FxnDirectoryPlayer[runfxnstring],params)
    pause 0.005
    return
init python:
    FxnDirectoryEnemy={
        "Attack":"Damageplayer",
        "AttackSP":"DamageSPplayer",
        "ReduceSPself":"DamageSPselfenemy",
        "Defend":"Shieldenemy",
        "Recover":"Recoverenemy",
        "Burn":"Burnself",
        "GiveToken":"GainTokenPlayer",
        "GainToken":"GiveToken",
        "BurnSelf":"Burnenemy",
        "If":"IfTokenInStatusEnemy",
        "While":"WhileTokenInStatusEnemy",
        "For":"ForInRangeEnemy",
        "RemoveToken":"RemoveTokenEnemy",
        "IncreaseATK":"IncreaseATKenemy",
        "IncreaseDEF":"IncreaseDEFenemy",
        "Increase":"IncreaseEnemy",
        "ReduceBit":"ReduceBitself",
        "Evade":"EvadeEnemy",
        "Block":"BlockEnemy",
        "Retreat":"Retreat",
        "Push":"Retreat",
        "Advance":"Advance",
        "Pull":"Advance",
        "DeckChange":"DeckChangeEnemy",
        
        # "":"",
        "":"DoNothing"
    }
label enemyfunctioneffects(runfxnstring,params={}):
    $ renpy.call(FxnDirectoryEnemy[runfxnstring],params)
    pause 0.005
    return
