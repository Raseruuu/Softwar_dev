init python:
    class Card:
        def __init__(self,name,magnitude):
            self.name = name
            self.magnitude = magnitude
    def statusAppend(stslist,statusstring):
        if len(stslist)==16:
            stslist.pop(0)
            #FIFO First in, First out.
            # print(stslist)
            # print(statusstring)
        stslist.append(statusstring)

        return stslist
    runnumber=0
image bit:
    "gui/Bit.png"
    zoom 4.0

image damageeffect:
    xalign 0.5 yanchor 0.32 ypos 0.25
    choice:
        "images/battle/dmgeffect1.png"
        pause 0.1
        "images/battle/dmgeffect2.png"
        pause 0.1
        "images/battle/dmgeffect3.png"
        pause 0.1
    choice:
        "images/battle/dmgeffect1.png"
        xzoom -1.0
        pause 0.1
        "images/battle/dmgeffect2.png"
        xzoom -1.0
        pause 0.1
        "images/battle/dmgeffect3.png"
        xzoom -1.0
        pause 0.1

    linear 0.3 alpha 0.0

label RemoveTokenEnemy:
    $ token_name = currentcard_fxn_params[0]
    $ remove_target = currentcard_fxn_params[1]
    if remove_target=="Self":
        $ EnmySts.remove(token_name)
        show screen tokenremove_anim(token_name)
        $ renpy.pause(0.4,hard=True)
        hide screen tokenremove_anim
    elif remove_target=="Enemy":
        $ PlayerSts.remove(token_name)
    
    return
label RemoveTokenPlayer:
    $ token_name = currentcard_fxn_params[0]
    $ remove_target = currentcard_fxn_params[1]
    if remove_target=="Self":
        $ PlayerSts.remove(token_name)
    elif remove_target=="Enemy":
        $ EnmySts.remove(token_name)
        
        show screen tokenremove_anim(token_name)
        $ renpy.pause(0.4,hard=True)
        hide screen tokenremove_anim
    return
label Damageenemy:
    
    if currentcardFXN[fxnindex].name=="While" or currentcardFXN[fxnindex].name=="For" or currentcardFXN[fxnindex].name=="If":
        pass
    else:    
        $ currentcard_fxn_params=currentcardFXN[fxnindex].params
    
    # if currentcard_fxn_params[0]!="POWR" and currentcard_fxn_params[0]: 
    $ damagemultiplier = currentcard_fxn_params[0]
    
    $ Power = (currentcardMAG)
    if damagemultiplier=="POWR":
        $ damagetoenemy=int(playerATK_m*Power)
    elif damagemultiplier!="POWR": 
        $ damagetoenemy=int(playerATK_m*damagemultiplier)
    $ attackrange = currentcard_fxn_params[1]
    $ attackhit=True
    $ battle_distance_old=battle_distance
    ## EVADE
    if "Evade" in EnmySts:
        $ attackhit=False
    if not attackhit:
        $ EnmySts.remove('Evade') 
        $ enemy_evasion_active=True
        pause 0.1
        
        show Enemy at sidesteps_effect_dodge("Enemy", 0.5, renpy.random.choice([0.6,0.4]), 0.12)
        pause 0.24
        $ enemy_evasion_active=False
        show Enemy:
            xalign 0.5 yanchor 0.32 ypos 0.3 
        play sound "sfx/miss.wav"
        call showphasemsg("EVADED")
    ## NO EVADE
    elif attackhit:
        if battle_distance>=attackrange:
            
            $ attackhit=False
            # show Enemy:
            #     xalign 0.5 yanchor 0.32 ypos 0.3
            $ enemy_evasion_active=True
            
            show Enemy at sidesteps_effect_dodge("Enemy", 0.5, renpy.random.choice([0.6,0.4]), 0.12)
                # yanchor 1.0 ypos 0.5
                # yanchor 0.32 ypos 0.3
                # yoffset 1.0
            pause 0.24
            $ enemy_evasion_active=False
            show Enemy:
                xalign 0.5 yanchor 0.32 ypos 0.3 
            play sound "sfx/miss.wav"
            call showphasemsg("MISSED!")
            call Advanceenemy(1)
            if battle_distance==0 and battle_distance_old>0:
                call showphasemsg("DISTANCE:ZERO")
            $ renpy.pause(0.6,hard=True)
            return
        if attackhit:
            
            if currentcardTYPE == "Sword":
                play sound "sfx/slash.wav"
            elif currentcardTYPE == "FireSword":
                play sound "sfx/slash.wav"
                play sound "sfx/sfx_exp_short_hard8.wav"
            elif currentcardTYPE == "Axe":
                play sound "sfx/slash.wav"
            elif currentcardTYPE == "Fire":
                play sound "sfx/Bust.wav"
            elif currentcardTYPE == "Gun":
                play sound "sfx/Bust.wav"
            else:
                $ attacknumber+=1
            if attacknumber<=3:
                play sound "sfx/sfx_exp_short_hard9.wav"
            elif attacknumber>3:
                play sound "sfx/sfx_exp_short_hard8.wav"
            else:
                play sound "sfx/sfx_exp_short_hard8.wav"
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
                dmgdist = ((currentcard.MAG*100)/20)
                dmgdist = int(dmgdist*2)
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

            #   $ renpy.pause(0.6,hard=True)
            if "Drill" in currentcardTYPE:
                $ renpy.pause(0.2,hard=True)
            elif "MailSword" in currentcardTYPE:
                $ renpy.pause(0.25,hard=True)
            elif "Eraser" in currentcardTYPE:
                $ renpy.pause(0.01,hard=True)
            else:
                $ renpy.pause(0.6,hard=True)
            hide damageeffect
    return
label DamageSPplayer:
    # EVADE
    if "Evade" in PlayerSts:
        $ attackhit=False
        $ PlayerSts.remove('Evade')
        call showphasemsg("EVADED")
    ## NO EVADE
    else:
        if playerSP>0:
            $ Magnitude = (currentcardMAG)
            $ damagetoplayer=int(enemyATK_m*Magnitude)

            if currentcardTYPE == "Sword":
                play sound "sfx/slash.wav"
            elif currentcardTYPE == "Axe":
                play sound "sfx/slash.wav"
            elif currentcardTYPE == "Fire":
                play sound "sfx/Bust.wav"
            elif currentcardTYPE == "Gun":
                play sound "sfx/Bust.wav"
            else:
                if runnumber>1:
                    play sound "sfx/sfx_exp_short_hard8.wav"
                else:
                    play sound "sfx/sfx_exp_short_hard9.wav"
            call hurtnoise_enemy
            $ playerSP-=damagetoplayer
            if playerSP<0:
                $ playerSP=0

            $ dmgdist = ((currentcard.MAG*100)/20)
            $ dmgdist = int(dmgdist*2)

            show playerdmgpoint onlayer overlay
            # call hurtnoise
            with Shake((0, 0, 0, 0), 0.5, dist=dmgdist)
            $ renpy.pause(0.6,hard=True)
    return
label DamageSPenemy:
    ## EVADE
    if "Evade" in EnmySts:
        $ attackhit=False
        $ EnmySts.remove('Evade')
        show Enemy at sidesteps_effect_dodge("Enemy", 0.5, renpy.random.choice([0.6,0.4]), 0.12)
        pause 0.2
        show Enemy
        call showphasemsg("EVADED")
    ## NO EVADE
    else:
        if enemySP>0:
            $ Magnitude = (currentcardMAG)
            $ damagetoenemy=int(playerATK_m*Magnitude)
            if currentcardTYPE == "Sword":
                play sound "sfx/slash.wav"
            elif currentcardTYPE == "Axe":
                play sound "sfx/slash.wav"
            elif currentcardTYPE == "Fire":
                play sound "sfx/Bust.wav"
            elif currentcardTYPE == "Gun":
                play sound "sfx/Bust.wav"
            else:
                if runnumber>1:
                    play sound "sfx/sfx_exp_short_hard8.wav"
                else:
                    play sound "sfx/sfx_exp_short_hard9.wav"
            call hurtnoise_enemy
            $ enemySP-=damagetoenemy
            if enemySP<0:
                $ enemySP=0
            $ dmgdist = ((currentcard.MAG*100)/20)
            $ dmgdist = int(dmgdist*2)
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
    return
label DamageSPselfenemy:
    if enemySP>0:
        $ Magnitude = (currentcardMAG)
        $ damagetoenemy=int(enemyATK_m*Magnitude)

        if currentcardTYPE == "Sword":
          play sound "sfx/slash.wav"
        elif currentcardTYPE == "Axe":
          play sound "sfx/slash.wav"
        elif currentcardTYPE == "Fire":
          play sound "sfx/Bust.wav"
        elif currentcardTYPE == "Gun":
          play sound "sfx/Bust.wav"
        else:
          if runnumber>1:
            play sound "sfx/sfx_exp_short_hard8.wav"
          else:
            play sound "sfx/sfx_exp_short_hard9.wav"
        call hurtnoise_enemy
        $ enemySP-=damagetoenemy
        if enemySP<0:
            $ enemySP=0
        $ dmgdist = ((currentcard.MAG*100)/20)
        $ dmgdist = int(dmgdist*2)
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
    return
label Burnenemy:
    play sound "sfx/fire.wav"
    # $ EnmySts.append("Burn")
    $ EnmySts=statusAppend(EnmySts,"Burn")
    show Brnsts:
      zoom 1.3 xalign 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
      linear 0.1 zoom 0.98
      linear 0.2 zoom 1.0 alpha 0.0
    call updatestats_enemy
    if "Drill" in currentcardTYPE:
        $ renpy.pause(0.2,hard=True)
    else:
        $ renpy.pause(0.6,hard=True)
    hide Brnsts
    
    return
label Retreatenemy(distanceamount=0):
    if currentcardFXN[fxnindex].name=="While" or currentcardFXN[fxnindex].name=="If" or currentcardFXN[fxnindex].name=="For":
          pass
    else:    
          $ currentcard_fxn_params=currentcardFXN[fxnindex].params

    if distanceamount==0:
        $ distance_quantity = currentcard_fxn_params[0]
    else:
         $distance_quantity=distanceamount
    python:
        for dist in range(0,distance_quantity):
            # if battle_distance!=0:
            battle_distance=battle_distance+1
            renpy.play("sfx/sfx_movement_footstepsloop4_fast.wav","sound")
            
            renpy.pause(0.6,hard=True)
    call updatestats_enemy
    return
label Advanceenemy(distanceamount=0):
    if currentcardFXN[fxnindex].name=="If":
        $ whichfxnhasadvance=0
        python:
            for stuff in currentcardFXN[fxnindex].params[1]:
                if stuff.name=="Advance":
                    currentcard_fxn_params=stuff.params
    else:
        $ currentcard_fxn_params=currentcardFXN[fxnindex].params
    if distanceamount==0:
        $ distance_quantity = currentcard_fxn_params[0]
    else:
         $distance_quantity=distanceamount
    python:
        for dist in range(0,distance_quantity):
            if battle_distance!=0:
                battle_distance=battle_distance-1
                renpy.play("sfx/sfx_movement_footstepsloop4_fast.wav","sound")
                dist+=1
                renpy.pause(0.6,hard=True)
    call updatestats_enemy
    return
label Advanceplayer(distanceamount=0):
    $ currentcard_fxn_params=currentcardFXN[fxnindex].params
    if distanceamount==0:
        $ distance_quantity = currentcard_fxn_params[0]
    else:
         $distance_quantity=distanceamount
    python:
        for dist in range(0,distance_quantity):
            if battle_distance!=0:
                battle_distance=battle_distance-1
                renpy.play("sfx/sfx_movement_footstepsloop4_fast.wav","sound")
                renpy.pause(0.6,hard=True)
    call updatestats_player
    
    
    return
label Retreatplayer(distanceamount=0):
    $ currentcard_fxn_params=currentcardFXN[fxnindex].params
    if distanceamount==0:
        $ distance_quantity = currentcard_fxn_params[0]
    else:
         $distance_quantity=distanceamount
    python:
        for dist in range(0,distance_quantity):
            battle_distance=battle_distance+1
            renpy.play("sfx/sfx_movement_footstepsloop4_fast.wav","sound")
            renpy.pause(0.6,hard=True)
    call updatestats_player
    
    
    return
label ReduceBitself:
    play sound "sfx/sfx_exp_odd3.wav"
    $ playerbits-=1
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
label ReduceBit:
    play sound "sfx/sfx_exp_odd3.wav"
    $ enemybits-=1
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
label AddBitself:
    play sound "sfx/sfx_exp_odd3.wav"
    $ playerbits+=1
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
label Burnself:
    play sound "sfx/fire.wav"
    # $ PlayerSts.append("Burn")
    $ PlayerSts=statusAppend(PlayerSts,"Burn")
    show Brnsts onlayer overlay:
      zoom 1.3 xpos 0.15 xanchor 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
      linear 0.1 zoom 0.98
      linear 0.2 zoom 1.0 alpha 0.0
    # $ renpy.pause(0.6,hard=True)
    if "Drill" in currentcardTYPE:
        $ renpy.pause(0.2,hard=True)
    else:
        $ renpy.pause(0.6,hard=True)
    hide Brnsts
    return
label Emailenemy:
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
screen tokenappend_anim(tokenname):
    text "[tokenname]" at tokenappend_trans:
        style "statusoutlines"
screen tokenremove_anim(tokenname):
    text "[tokenname]" at tokenremove_trans:
        style "statusoutlines"
transform tokenappend_trans:
    zoom 1.3 xalign 0.5 yanchor 1.0 ypos 0.41 alpha 0.0
    linear 0.1 zoom 0.98 alpha 1.0
    pause 0.2
    ease 0.1 zoom 1.0 yoffset 24 alpha 0.0
transform tokenremove_trans:
    zoom 0.9 xalign 0.5 yanchor 1.0 ypos 0.41 alpha 1.0
    linear 0.1 zoom 1.0
    pause 0.2
    ease 0.1 zoom 1.2 yoffset -24 alpha 0.0
label GiveToken:
    play sound "sfx/sfx_sounds_powerup4.wav"
    $ currentcard_fxn_params=currentcardFXN[fxnindex].params
    $ token_name = currentcard_fxn_params[0]
    $ quantity = currentcard_fxn_params[1]
    # $ EnmySts.append("Burn")
    $ counter=0
    label tokenquant_loop:

        $ EnmySts=statusAppend(EnmySts,token_name)
        show screen tokenappend_anim(token_name)
        $ renpy.pause(0.4,hard=True)
        hide screen tokenappend_anim
        $ counter+=1
        if counter<quantity:

            jump tokenquant_loop
    
    call updatestats_enemy
    return
label GainTokenPlayer:
    play sound "sfx/sfx_sounds_powerup4.wav"
    $ currentcard_fxn_params=currentcardFXN[fxnindex].params
    $ token_name = currentcard_fxn_params[0]
    $ quantity = currentcard_fxn_params[1]
    # $ EnmySts.append("Burn")
    $ counter=0
    label tokenquant_loop2:

        $ PlayerSts=statusAppend(PlayerSts,token_name)
        show text "[token_name]":
          zoom 1.3 xpos 0.15 xanchor 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
          linear 0.1 zoom 0.98
          linear 0.2 zoom 1.0 alpha 0.0
        $ renpy.pause(0.6,hard=True)
        hide text
        $ counter+=1
        if counter<quantity:

            jump tokenquant_loop2
    return

label GainTokenEnemy:
    play sound "sfx/sfx_sounds_powerup4.wav"
    $ currentcard_fxn_params=currentcardFXN[fxnindex].params
    $ token_name = currentcard_fxn_params[0]
    $ quantity = currentcard_fxn_params[1]
    # $ EnmySts.append("Burn")
    $ counter=0
    label tokenquant_loop3:

        $ EnmySts=statusAppend(EnmySts,token_name)
        show text "{size=20}[token_name]{/size}":
          zoom 1.3 xpos 0.15 xanchor 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
          linear 0.1 zoom 0.98
          linear 0.2 zoom 1.0 alpha 0.0
        $ renpy.pause(0.6,hard=True)
        hide text
        $ counter+=1
        if counter<quantity:
            jump tokenquant_loop3
    call updatestats_enemy
    return

label EvadeEnemy:
    play sound "sfx/sfx_sounds_powerup4.wav"
    $ currentcard_fxn_params=currentcardFXN[fxnindex].params
    $ token_name = currentcard_fxn_params[0]
    $ quantity = currentcard_fxn_params[1]
    # $ EnmySts.append("Burn")
    $ counter=0
    label tokenquant_loop4:

        $ EnmySts=statusAppend(EnmySts,token_name)
        show text "{size=20}[token_name]{/size}":
          zoom 1.3 xpos 0.15 xanchor 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
          linear 0.1 zoom 0.98
          linear 0.2 zoom 1.0 alpha 0.0
        $ renpy.pause(0.6,hard=True)
        hide text
        $ counter+=1
        if counter<quantity:
            jump tokenquant_loop4
    return

label EvadePlayer:
    play sound "sfx/sfx_sounds_powerup4.wav"
    $ currentcard_fxn_params=currentcardFXN[fxnindex].params
    # $ token_name = currentcard_fxn_params[0]
    $ quantity = currentcard_fxn_params[1]
    $ token_name = "Evade"
    # $ EnmySts.append("Burn")
    $ counter=0
    label tokenquant_loop5:

        $ PlayerSts=statusAppend(PlayerSts,token_name)
        show text "{size=20}[token_name]{/size}":
          zoom 1.3 xpos 0.15 xanchor 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
          linear 0.1 zoom 0.98
          linear 0.2 zoom 1.0 alpha 0.0
        $ renpy.pause(0.6,hard=True)
        hide text
        
        $ counter+=1
        if counter<quantity:
            jump tokenquant_loop5
    return
label BoostATK:

    play sound "sfx/sfx_sounds_powerup16.wav"
    $ Magnitude=currentcardMAG
    # $ PlayerSts.append("BoostATK")
    $ currentcard_fxn_params=currentcardFXN[fxnindex].params

    # $ PlayerSts=statusAppend(PlayerSts,["BoostATK",currentcard_fxn_params[1]])
    $ PlayerSts=statusAppend(PlayerSts,"BoostATK")
    call updatestats_player
    show BoostATKsts onlayer overlay:
      zoom 1.3 xpos 0.15 xanchor 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
      linear 0.1 zoom 0.98
      linear 0.2 zoom 1.0 alpha 0.0
      
    $ renpy.pause(0.6,hard=True)
    hide text
    return
label BoostDEF:

    play sound "sfx/sfx_sounds_powerup16.wav"
    $ Magnitude=currentcardMAG
    # $ PlayerSts.append("BoostDEF")
    $ PlayerSts=statusAppend(PlayerSts,"BoostDEF")
    call updatestats_player from _call_updatestats_player_1
    show BoostDEFsts onlayer overlay:
      zoom 1.3 xpos 0.15 xanchor 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
      linear 0.1 zoom 0.98
      linear 0.2 zoom 1.0 alpha 0.0
    $ renpy.pause(0.6,hard=True)
    hide BoostDEFsts
    return
label BoostMAGenemy:
    play sound "sfx/sfx_sounds_powerup16.wav"
    $ Magnitude=currentcardMAG
    # $ PlayerSts.append("BoostATK")
    $ PlayerSts=statusAppend(PlayerSts,"BoostMAG")
    call updatestats_enemy from _call_updatestats_enemy
    show BoostMAGsts onlayer overlay:
      zoom 1.3 xpos 0.85 xanchor 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
      linear 0.1 zoom 0.98
      linear 0.2 zoom 1.0 alpha 0.0
    $ renpy.pause(0.6,hard=True)
    hide BoostMAGsts
    return

label WhileTokenInStatusEnemy:
#Enemy Activates While Loop
    $ runfxnstring = currentcardFXN[fxnindex].name
    $ FXN=currentcardFXN[fxnindex]
    $ token_name=FXN.params[0]
    $ block_functions=FXN.params[1]
    $ targetsts=FXN.params[2]
    # label WhileLoop:
    if targetsts == "Self":
        while token_name in EnmySts:
            # if token_name in PlayerSts:
            $ block_count = 0
            label block_loop:
                $ runfxnstring = block_functions[block_count].name
                $ currentcard_fxn_params=block_functions[block_count].params
                call enemyfunctioneffects(runfxnstring)
                $ block_count+=1
                if block_count<len(block_functions):
                    jump block_loop
                # jump WhileLoop
    if targetsts == "Enemy":
        while token_name in PlayerSts:
            # if token_name in PlayerSts:
            $ block_count = 0
            label block_loop1:
                $ runfxnstring = block_functions[block_count].name
                $ currentcard_fxn_params=block_functions[block_count].params
                call enemyfunctioneffects(runfxnstring)
                $ block_count+=1
                if block_count<len(block_functions):
                    jump block_loop1
                # jump WhileLoop
    return
label ForInRangePlayer:
#Enemy Activates For Loop
    $ runfxnstring = currentcardFXN[fxnindex].name
    $ FXN=currentcardFXN[fxnindex]
    $ for_iterations=FXN.params[0]
    $ block_functions=FXN.params[1]
    # $ targetsts=FXN.params[2]
    # label WhileLoop:
    $ for_index = 0
    while for_index < for_iterations:
        # if token_name in PlayerSts:
        $ block_count = 0
        label block_loop8:
            $ runfxnstring = block_functions[block_count].name
            $ currentcard_fxn_params=block_functions[block_count].params
            call functioneffects(runfxnstring)
            $ block_count+=1
            if block_count<len(block_functions):
                jump block_loop8
                # jump WhileLoop
        $ for_index+=1  
    
    return
label IfTokenInStatusEnemy:
#Enemy Activates If
    $ runfxnstring = currentcardFXN[fxnindex].name
    $ FXN=currentcardFXN[fxnindex]
    $ token_name=FXN.params[0]
    $ block_functions=FXN.params[1]
    $ targetsts=FXN.params[2]
    # label WhileLoop:
    if targetsts == "Self":
        if token_name in EnmySts:
            # if token_name in PlayerSts:
            $ block_count = 0
            label block_loop2:
                $ runfxnstring = block_functions[block_count].name
                $ currentcard_fxn_params=block_functions[block_count].params
                call enemyfunctioneffects(runfxnstring)
                $ block_count+=1
                if block_count<len(block_functions):
                    jump block_loop2
                # jump WhileLoop
    if targetsts == "Enemy":
        if token_name in PlayerSts:
            # if token_name in PlayerSts:
            $ block_count = 0
            label block_loop3:
                $ runfxnstring = block_functions[block_count].name
                $ currentcard_fxn_params=block_functions[block_count].params
                call enemyfunctioneffects(runfxnstring)
                $ block_count+=1
                if block_count<len(block_functions):
                    jump block_loop3
                # jump WhileLoop
    return
label IfTokenInStatusPlayer:
#Player Uses If
    $ runfxnstring = currentcardFXN[fxnindex].name
    $ FXN=currentcardFXN[fxnindex]
    $ token_name=FXN.params[0]
    $ block_functions=FXN.params[1]
    $ targetsts=FXN.params[2]
    # label WhileLoop:
    if targetsts == "Self":
        if token_name in PlayerSts:
            # if token_name in PlayerSts:
            $ block_count = 0
            label block_loop4:
                
                $ runfxnstring = block_functions[block_count].name
                $ currentcard_fxn_params=block_functions[block_count].params
                call functioneffects(runfxnstring)
                $ block_count+=1
                if block_count<len(block_functions):
                    jump block_loop4
                
    elif targetsts == "Enemy":
        if token_name in EnmySts:
            # if token_name in PlayerSts:
            $ block_count = 0
            label block_loop5:
                $ runfxnstring = block_functions[block_count].name
                $ currentcard_fxn_params=block_functions[block_count].params
                call functioneffects(runfxnstring)
                $ block_count+=1
                if block_count<len(block_functions):
                    jump block_loop5
            # jump WhileLoop
    return
label WhileTokenInStatusPlayer:
#Player Activates While Loop
    $ runfxnstring = currentcardFXN[fxnindex].name
    $ FXN=currentcardFXN[fxnindex]
    $ token_name=FXN.params[0]
    $ block_functions=FXN.params[1]
    $ targetsts=FXN.params[2]

    if targetsts == "Self":
        while token_name in PlayerSts:
            $ block_count = 0
            label block_loop6:
                $ runfxnstring = block_functions[block_count].name
                $ currentcard_fxn_params=block_functions[block_count].params
                call functioneffects(runfxnstring) from _call_functioneffects_4
                $ block_count+=1
                if block_count<len(block_functions):
                    jump block_loop6

    elif targetsts == "Enemy":
        while token_name in EnmySts:
            $ block_count = 0
            label block_loop7:
                $ runfxnstring = block_functions[block_count].name
                $ currentcard_fxn_params=block_functions[block_count].params

                call functioneffects(runfxnstring) from _call_functioneffects_5
                $ block_count+=1
                if block_count<len(block_functions):

                    jump block_loop7

    return
label BoostATKenemy:
    play sound "sfx/sfx_sounds_powerup16.wav"
    $ Magnitude=currentcardMAG

    # $ EnmySts.append("BoostDEF")
    $ EnmySts=statusAppend(EnmySts,"BoostATK")
    call updatestats_enemy from _call_updatestats_enemy_1
    show BoostATKsts onlayer overlay:
      zoom 1.3 xpos 0.85 xanchor 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
      linear 0.1 zoom 0.98
      linear 0.2 zoom 1.0 alpha 0.0
    $ renpy.pause(0.6,hard=True)
    hide BoostDEFsts
    return
label BoostDEFenemy:
    play sound "sfx/sfx_sounds_powerup16.wav"
    $ Magnitude=currentcardMAG

    # $ EnmySts.append("BoostDEF")
    $ EnmySts=statusAppend(EnmySts,"BoostDEF")
    call updatestats_enemy from _call_updatestats_enemy_2
    show BoostDEFsts onlayer overlay:
      zoom 1.3 xpos 0.85 xanchor 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
      linear 0.1 zoom 0.98
      linear 0.2 zoom 1.0 alpha 0.0
    $ renpy.pause(0.6,hard=True)
    hide BoostDEFsts
    return
label updatestats_player:
    python:
        playerATK_m=playerATK
        playerDEF_m=playerDEF
        for fxns in PlayerSts:
                if fxns == 'BoostATK':
                    # boostvalue = fxns[1]
                    boostvalue = 0.25
                    playerATK_m+=playerATK*boostvalue
                    playerATK_m = int(playerATK_m)
                    # "This shit happened"
                elif fxns == 'BoostDEF':
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
                if fxns == 'BoostATK':
                    # boostvalue = fxns[1]
                    boostvalue = 0.25
                    enemyATK_m+=enemyATK*boostvalue
                    enemyATK_m = int(enemyATK_m)
                    # "This shit happened"
                elif fxns == 'BoostDEF':
                    # boostvalue = fxns[1]
                    boostvalue = 0.25
                    enemyDEF_m+=enemyDEF*boostvalue
                    enemyDEF_m = int(enemyDEF_m)
    hide screen battlestats
    show screen battlestats              

    return


image shieldbit = "images/battle/Shield_bit.png"
image shieldlight = "images/battle/Shield_light.png"
label Shieldplayer:
    play sound "sfx/defense.wav"
    $ multiplier = currentcardFXN[fxnindex].params[0]
    $ Magnitude = (currentcardMAG)
    if multiplier=="POWR":
        $ shieldtoplayer=int(playerDEF_m*Magnitude)
    elif multiplier!="POWR": 
        $ shieldtoplayer=int(playerDEF_m*multiplier)
    python:
        playerSP+=shieldtoplayer
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
    show text "{size=70}SP+=[shieldtoplayer]{/size}"  onlayer overlay:
        alpha 0.0 zoom 0.0 xpos 0.5 ypos 0.9 yanchor 0.5 xanchor 0.5
        ease 0.1 alpha 1.0 zoom 1.2
        pause 0.55
        ease 0.05 alpha 0.0 zoom 1.1
    $ renpy.pause(0.6,hard=True)
    return
label ReduceSPself:
    # play sound "sfx/defense_loss.wav"
    $ multiplier = currentcardFXN[fxnindex].params[0]
    $ Magnitude = (currentcardMAG)
    if multiplier=="POWR":
        $ shieldtoplayer=int(playerDEF_m*Magnitude)
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
label Recoverplayer:
    play sound "sfx/heal.ogg"
    $ Magnitude = (currentcardMAG)
    $ healtoplayer=int(playerHPMax*Magnitude)
    python:
        playerHP+=healtoplayer
        if playerHP>=playerHPMax:
            playerHP=playerHPMax
    #Animation
    show heallight:
        alpha 0.0
        ease 0.3 alpha 1.0
        ease 0.3 alpha 0.0
    show healbit onlayer overlay:
        alpha 0.0 xpos 0.5 ypos 0.7 yanchor 0.5 xanchor 0.5
        ease 0.2 alpha 1.0
        ease 0.4 alpha 0.0
    show text "{size=70}HP+=[healtoplayer]{/size}" onlayer overlay:
        alpha 0.0 zoom 0.0 xpos 0.5 ypos 0.9 yanchor 0.5 xanchor 0.5
        ease 0.1 alpha 1.0 zoom 1.2
        pause 0.55
        ease 0.05 alpha 0.0 zoom 1.1
    $ renpy.pause(0.6,hard=True)
    return
label Recoverenemy:
    play sound "sfx/heal.ogg"
    $ Magnitude = (currentcardMAG)
    $ healtoenemy=int(enemyHPMax*Magnitude)
    python:
        enemyHP+=healtoenemy
        if enemyHP>=enemyHPMax:
            enemyHP=enemyHPMax
    #Animation
    show heallight:
        alpha 0.0
        ease 0.3 alpha 1.0
        ease 0.3 alpha 0.0

    show healbit onlayer overlay:
        alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.35
        ease 0.2 alpha 1.0
        pause 0.1
        ease 0.4 alpha 0.0
    show text "{size=40}SP+=[healtoenemy]{/size}" onlayer overlay:
        alpha 0.0 zoom 0.0 xalign 0.5 yanchor 0.5 ypos 0.45
        ease 0.1 alpha 1.0 zoom 1.2
        pause 0.2
        ease 0.05 alpha 0.0 zoom 1.1
    $ renpy.pause(0.6,hard=True)
    return
label Shieldenemy:
    play sound "sfx/defense.wav"
    $ Magnitude = (currentcardMAG)
    $ shieldtoenemy=int(enemyDEF_m*Magnitude)
    python:
        enemySP+=shieldtoenemy
        # if enemySP>=enemySPMax:
        #     enemySP=enemySPMax
    #Animation
    # show shieldlight:
    #     alpha 0.0
    #     ease 0.3 alpha 1.0
    #     ease 0.3 alpha 0.0
    show shieldbit onlayer overlay:
        alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.35
        ease 0.2 alpha 1.0
        pause 0.1
        ease 0.4 alpha 0.0
    show text "{size=40}SP+=[shieldtoenemy]{/size}" onlayer overlay:
        alpha 0.0 zoom 0.0 xalign 0.5 yanchor 0.5 ypos 0.45
        ease 0.1 alpha 1.0 zoom 1.2
        pause 0.2
        ease 0.05 alpha 0.0 zoom 1.1
    $ renpy.pause(0.6,hard=True)
    return
label DoNothing:
    pass
    return

label Damageplayer:
    if currentcardFXN[fxnindex].name=="While" or currentcardFXN[fxnindex].name=="If" or currentcardFXN[fxnindex].name=="For":
          pass
    else:    
          $ currentcard_fxn_params=currentcardFXN[fxnindex].params
    # if currentcard_fxn_params[0]!="POWR" and currentcard_fxn_params[0]: 
    $ damagemultiplier = currentcard_fxn_params[0]
    $ absolutedamage = currentcard_fxn_params[2]
    $ Power = (currentcardMAG)
    
    if absolutedamage:
        $ damagetoplayer=int(damagemultiplier)
    # $ currentcard_fxn_params=currentcardFXN[fxnindex].params
    else:
        if damagemultiplier=="POWR":
            $ damagetoplayer=int(enemyATK_m*Power)
        elif damagemultiplier!="POWR": 
            $ damagetoplayer=int(enemyATK_m*damagemultiplier)
    $ attackrange = currentcard_fxn_params[1]
    $ attackhit=True
    $ battle_distance_old=battle_distance
    ## EVADE
    if "Evade" in PlayerSts:
        $ attackhit=False
        # $ renpy.show("Icon_[playerName]", at_list=([sidesteps_effect_dodge("Icon_[playerName]", 0.5, renpy.random.choice([0.6,0.4]), 0.12)]))
        $ evasion_active=True
        pause 0.1
        $ evasion_active=False
        $ PlayerSts.remove('Evade')
        call showphasemsg("EVADED")
        
    ## NO EVADE
    if attackhit:
        if battle_distance>=attackrange:
            call Advanceplayer(1)
            $ attackhit=False
            # show Enemy:
            #     xalign 0.5 yanchor 0.32 ypos 0.3
            $ evasion_active=True
            pause 0.1
            $ evasion_active=False
            play sound "sfx/miss.wav"
            call showphasemsg("MISSED!")
            $ renpy.pause(0.3,hard=True)
            if battle_distance==0 and battle_distance_old>0:
                call showphasemsg("DISTANCE:ZERO")
            $ renpy.pause(0.3,hard=True)
            return
        else:
        
            if currentcardTYPE == "Sword":
                play sound "sfx/slash.wav" channel 1
            elif currentcardTYPE == "Axe":
                play sound "sfx/slash.wav" channel 1
            elif currentcardTYPE == "Fire":
                play sound "sfx/Bust.wav" channel 1
            elif currentcardTYPE == "Gun":
                play sound "sfx/Bust.wav" channel 1
            if playerSP>0:
                play sound "sfx/noise.wav" channel 1
                $ playerSP-=damagetoplayer
                if playerSP<0:
                    #playerSP becomes a negative value if damage exceeds its value
                    $ playerHP+=playerSP
                    $ playerSP = 0
            else:
                play sound "sfx/damage2.wav"

                $ playerHP-=damagetoplayer
        if playerHP <=0:
            $ playerHP = 0
            $ battle_done=True
        $ dmgdist = ((currentcard.MAG*100)/20)
        $ dmgdist = int(dmgdist*2)
        show playerdmgpoint onlayer overlay
        # show damagenoise
        call hurtnoise
        $ hurtface=(renpy.random.randint(0,1))
        if hurtface==0:
            $ ILY_m="O"
            $ ILY_e="up"
        elif hurtface==1:
            $ ILY_m="O"
            $ ILY_e="up2"
            $ ILY_eyes="closedup"
        hide damagenoise
        hide screen battlestats
        show screen battlestats
        
        with Shake((0, 0, 0, 0), 0.5, dist=dmgdist)
        
    #   if "Drill" in currentcardTYPE:
    #     $ renpy.pause(0.2,hard=True)
    #   else:
        $ renpy.pause(0.6,hard=True)
        $ ILY_m="frown"
        $ ILY_e="down"
        $ ILY_eyes="open"
    $ attackhit=True
    hide screen battlestats
    show screen battlestats
    return
label DeckChangePlayer:
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
label DeckChangeEnemy:
    "[enemyName]'s Deck is changed to \"GUNVAR\"."
    $ enemyDeck=deckGUNVAR["content"]
    $ import random
    $ random.shuffle(enemyDeck)
    $ enemybits=16
    $ enemybitsmax=16
    hide screen battlestats
    show screen battlestats
    return
transform ringtransform:
    zoom 0.0 xalign 0.5 ypos 0.7 yanchor 0.5 rotate 0
    linear 0.15 zoom 1.4 rotate 180 alpha 0.8
transform ringtransform2:
    zoom 0.0 xalign 0.5 ypos 0.3 yanchor 0.5
    linear 0.15 zoom 1.4
screen cardflashscreen:
    # key "mousedown_5" action Return()
    # key "K_PAGEDOWN" action Return()
    add "ring" at ringtransform
    add "cardflash"
    key 'mouseup_1' action Return()
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
    call screen finishingflash(dialogue)
    return
label Execution:
    $ runnumber = 0
    $ attacknumber = 0
    
    #Index of looper
    call Concatenation
    $iterations =len(playerbattlecode)
    show screen phasemsg("EXECUTE")
    $renpy.pause(0.5,hard=True)
    hide screen phasemsg

    label exec_loop:

        $ currentcard = playerbattlecode[0]
        $ playerbattlecode.pop(0)
        # $ currentcard = (playerbattlecode[runnumber])
        $ currentcardFXN = currentcard.FXN
        $ currentcardMAG = currentcard.MAG
        $ currentcardTYPE = currentcard.TYPE
        $ Magnitude = (currentcardMAG)
        $ damagetoenemy=int(playerATK_m*Magnitude)
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
        $fxnindex=0
        $loopingcard=False
        $execution_active=True
        label runfunctions:
            $ runfxnstring = currentcardFXN[fxnindex].name
            $ runfxnparam = currentcardFXN[fxnindex].params
            hide screen cardflashscreen2
            show screen cardflashscreen2
            label hitloop:
                call functioneffects(runfxnstring)
            $fxnindex+=1
            if fxnindex<len(currentcardFXN):
                jump runfunctions

        hide screen cardflashscreen2
        hide ring
        $execution_active=False
        $fxnindex=0
        $runnumber+=1
        if (runnumber<iterations) and (battle_done==False):
            jump exec_loop
        else:

            call PlayerEndPhase from _call_PlayerEndPhase
            # info"[playerName]'s turn has ended."
            if not battle_done:
                call enemyattack from _call_enemyattack_1
    return
label hurtnoise_enemy:
    call hurtnoise_Ave
    call hurtnoise_Vira
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
            with Shake((0, 0, 0, 0), 0.5, dist=dmgdist)
            $ renpy.pause(0.6,hard=True)


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
        label runfunctions2:
            $ runfxnstring = currentcardFXN[fxnindex].name
            hide screen cardflashscreenenemy2
            show screen cardflashscreenenemy2
            # $ hitindex=0
            label hitloop2:
                call enemyfunctioneffects(runfxnstring) 

            $fxnindex+=1
            if fxnindex<len(currentcardFXN):
                jump runfunctions2
        $ execution_active=False

        hide screen cardflashscreenenemy2
        hide ring2
    return
label enemyattack:
    $ enemyrunnumber = 0
    $ enemynumberofattacks = 5 #renpy.random.randint(1,3)+renpy.random.randint(0,2)
    
    $ enemyhand = [enemyDeck[0],enemyDeck[1],enemyDeck[2],enemyDeck[3],enemyDeck[4]]
    show screen phasemsg(enemyName+"'S TURN")
    $renpy.pause(0.9,hard=True)
    hide screen phasemsg
    python:
      for enemyhandcards in range(0,5):
        enemyDeck.pop(0)
    #Buffs Priority
    $ enemyhand.sort(key=lambda x: x.FXN[0].name)
    if playerHP<= int(playerHPMax/2) or ("BoostATK" in EnmySts) or ("Saber" in EnmySts):
      #Damage priority
      $ enemyhand.sort(key=lambda x: x.FXN[0].name)
    elif (enemySP==0) and (enemyHP<=enemyHPMax):
      #Strongest card priority

      $ enemyhand.sort(key=lambda x: x.COST,  reverse = True)
      if "Shield" in enemyhand[0].FXN and "BoostATK" in [handcard.FXN for handcard in enemyhand]:
        $ enemyhand.sort(key=lambda x: x.FXN[0].name)
    python:
      for cardindex in range(0,5):

        enemyDeck.append(enemyhand[cardindex])

    $ choicecount=0
    label enemyattackloop:
        # $ enemycardtoexecute = enemyDeck[0]

        $ currentcard = enemyhand[0]

        # $ enemyhand.append(currentcard)
        # $ currentcard = (playerbattlecode[runnumber])
        $ currentcardFXN = currentcard.FXN
        $ currentcardMAG = currentcard.MAG
        $ currentcardTYPE = currentcard.TYPE
        $ currentcardCOST = currentcard.COST

        
        # $ enemycannotaffordtoattack = currentcardCOST>enemybits

        # $ goodcardtouse = True

        # $ boostcard = ("Boost" in currentcardFXN[0].name or "Boost" in currentcardFXN[1].name)
        # $ goodcardtouse = boostcard and (enemySP>100) or (not boostcard  and enemySP<=100)
        # $ goodcardused = False
        # $ choicecount = 0
        # $ notprioritycard = not (goodcardtouse)
        # $ nochoice = (choicecount==5)
        # if (goodcardtouse ==True) and (goodcardused==False):
        #   $ goodcardused = True
        #   call enemyexecutecard

        # elif notprioritycard :
        #   $ choicecount+=1
        #   $ enemyrunnumber-=1
        #   $ enemyhand.append(enemyhand[0])
        #   $ enemyhand.pop(0)
        # elif choicecount ==4:
        #   call enemyexecutecard
        # else:
        call enemyexecutecard from _call_enemyexecutecard
        $ enemyhand.pop(0)
        $ enemyrunnumber+=1



        if enemyrunnumber<enemynumberofattacks and (battle_done==False):
            jump enemyattackloop

        else:
            call EnemyEndPhase from _call_EnemyEndPhase
            # info"[enemyName]'s turn has ended."
    return

label Saber:

    play sound "sfx/sfx_sounds_powerup16.wav"
    # $ Magnitude=currentcardMAG
    # # $ PlayerSts.append("BoostATK")
    $ PlayerSts=statusAppend(PlayerSts,"Saber")
    call updatestats_player 
    show BoostDEFsts onlayer overlay:
      zoom 1.3 xpos 0.15 xanchor 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
      linear 0.1 zoom 0.98
      linear 0.2 zoom 1.0 alpha 0.0
    $ renpy.pause(0.6,hard=True)
    hide BoostDEFsts
    return

init python:
    FxnDirectoryPlayer={
        "Attack":"Damageenemy",
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
        "ForInRange":"ForInRangePlayer",
        "RemoveToken":"RemoveTokenPlayer",
        "BoostATK":"BoostATK",
        "BoostDEF":"BoostDEF",
        "ReduceBit":"ReduceBit",
        "Evade":"EvadePlayer",
        "Block":"Blockplayer",
        "Retreat":"Retreatplayer",
        "Advance":"Advanceplayer",
        "DeckChange":"DeckChangePlayer",
        "":"DoNothing"
    }
label functioneffects(runfxnstring,params=[]):
    $ renpy.call(FxnDirectoryPlayer[runfxnstring])
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
        "GainToken":"GainTokenEnemy",
        "BurnSelf":"Burnenemy",
        "If":"IfTokenInStatusEnemy",
        "While":"WhileTokenInStatusEnemy",
        "RemoveToken":"RemoveTokenEnemy",
        "BoostATK":"BoostATKenemy",
        "BoostDEF":"BoostDEFenemy",
        "Boost":"Boost",
        "ReduceBit":"ReduceBitself",
        "Evade":"EvadeEnemy",
        "Block":"BlockEnemy",
        "Retreat":"Retreatenemy",
        "Advance":"Advanceenemy",
        "DeckChange":"DeckChangeEnemy",
        
        # "":"",
        "":"DoNothing"
    }
label enemyfunctioneffects(runfxnstring):
    $ renpy.call(FxnDirectoryEnemy[runfxnstring])
    return
