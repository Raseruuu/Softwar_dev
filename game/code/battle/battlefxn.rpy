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
    return
label Damageenemy:
  $ Magnitude = (currentcardMAG)
  $ damagetoenemy=int(playerATK_m*Magnitude)
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
    if runnumber>1:
      play sound "sfx/sfx_exp_short_hard8.wav"
    else:
      play sound "sfx/sfx_exp_short_hard9.wav"
  call hurtnoise_Ave from _call_hurtnoise_Ave
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
  show dmgpoint
  show Enemy:
    linear 0.05 zoom 0.96
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
  hide damageeffect
  return
label DamageSPplayer:
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
        call hurtnoise_Ave from _call_hurtnoise_Ave_1
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
        call hurtnoise_Ave from _call_hurtnoise_Ave_2
        $ enemySP-=damagetoenemy
        if enemySP<0:
            $ enemySP=0
        $ dmgdist = ((currentcard.MAG*100)/20)
        $ dmgdist = int(dmgdist*2)
        show dmgpoint
        show Enemy:
            linear 0.05 zoom 0.96
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
        call hurtnoise_Ave from _call_hurtnoise_Ave_3
        $ enemySP-=damagetoenemy
        if enemySP<0:
            $ enemySP=0
        $ dmgdist = ((currentcard.MAG*100)/20)
        $ dmgdist = int(dmgdist*2)
        show dmgpoint
        show Enemy:
            linear 0.05 zoom 0.96
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
    # $ EnmySts.append("burn")
    $ EnmySts=statusAppend(EnmySts,"burn")
    show Brnsts:
      zoom 1.3 xalign 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
      linear 0.1 zoom 0.98
      linear 0.2 zoom 1.0 alpha 0.0
    $ renpy.pause(0.6,hard=True)
    hide Brnsts
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
    # $ PlayerSts.append("burn")
    $ PlayerSts=statusAppend(PlayerSts,"burn")
    show Brnsts onlayer overlay:
      zoom 1.3 xpos 0.15 xanchor 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
      linear 0.1 zoom 0.98
      linear 0.2 zoom 1.0 alpha 0.0
    $ renpy.pause(0.6,hard=True)
    hide Brnsts
    return
label Emailenemy:
    play sound "sfx/sfx_coin_cluster6.wav"
    # $ EnmySts.append("burn")
    $ EnmySts=statusAppend(EnmySts,"email")
    show Emailsts:
      zoom 1.3 xalign 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
      linear 0.1 zoom 0.98
      linear 0.2 zoom 1.0 alpha 0.0
    $ renpy.pause(0.6,hard=True)
    hide Emailsts
    return
label GiveToken:
    play sound "sfx/sfx_coin_cluster6.wav"
    $ currentcard_fxn_params=currentcardFXN[fxnindex].params
    $ token_name = currentcard_fxn_params[0]
    $ quantity = currentcard_fxn_params[1]
    # $ EnmySts.append("burn")
    $ counter=0
    label tokenquant_loop:

        $ EnmySts=statusAppend(EnmySts,token_name)
        show text "[token_name]":
          zoom 1.3 xalign 0.5 yanchor 1.0 ypos 0.45 alpha 1.0
          linear 0.1 zoom 0.98
          linear 0.2 zoom 1.0 alpha 0.0
        $ renpy.pause(0.1,hard=True)
        hide text
        $ counter+=1
        if counter<quantity:

            jump tokenquant_loop
    return
label GainTokenPlayer:
    play sound "sfx/sfx_coin_cluster6.wav"
    $ currentcard_fxn_params=currentcardFXN[fxnindex].params
    $ token_name = currentcard_fxn_params[0]
    $ quantity = currentcard_fxn_params[1]
    # $ EnmySts.append("burn")
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
    play sound "sfx/sfx_coin_cluster6.wav"
    $ currentcard_fxn_params=currentcardFXN[fxnindex].params
    $ token_name = currentcard_fxn_params[0]
    $ quantity = currentcard_fxn_params[1]
    # $ EnmySts.append("burn")
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
                    

    return


image shieldbit = "images/battle/Shield_bit.png"
image shieldlight = "images/battle/Shield_light.png"
label Shieldplayer:
    play sound "sfx/defense.wav"
    $ Magnitude = (currentcardMAG)
    $ shieldtoplayer=int(playerDEF_m*Magnitude)
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
    show text "{size=70}SP+=[shieldtoplayer]{/size}" onlayer overlay:
        alpha 0.0 zoom 0.0 xpos 0.5 ypos 0.9 yanchor 0.5 xanchor 0.5
        ease 0.1 alpha 1.0 zoom 1.2
        pause 0.55
        ease 0.05 alpha 0.0 zoom 1.1
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
  # if currentcardTYPE == "Sword":
  #   play sound "sfx/slash.wav"
  # elif currentcardTYPE == "Fire":
  #   play sound "sfx/fire.wav"
  # else:
  #   if runnumber>1:
  #     play sound "sfx/sfx_exp_short_hard8.wav"
  #   else:
  #     play sound "sfx/sfx_exp_short_hard9.wav"

  $ Magnitude = (currentcardMAG)
  $ damagetoplayer=int(enemyATK_m*Magnitude)
  if currentcardTYPE == "Sword":
    play sound "sfx/slash.wav" channel 1
  elif currentcardTYPE == "Axe":
    play sound "sfx/slash.wav" channel 1
  elif currentcardTYPE == "Fire":
    play sound "sfx/Bust.wav" channel 1
  elif currentcardTYPE == "Gun":
    play sound "sfx/Bust.wav" channel 1
  if playerSP>0:
    play sound "sfx/noise.wav"
    $ playerSP-=damagetoplayer
    if playerSP<0:
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

  with Shake((0, 0, 0, 0), 0.5, dist=dmgdist)
  call hurtnoise from _call_hurtnoise_1
  $ renpy.pause(0.6,hard=True)
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


label Concatenation:
    # "[playerbattlecode]"
    python:
        concat_true=False
        playerbattlecode_b4concat=copy.deepcopy(playerbattlecode)
        for battle_index,card in enumerate(playerbattlecode):

            prefix_card=card
            for concat_index,Concat_str in enumerate(Concat_strings):

                if card.TYPE in Concat_str:
                    if battle_index<len(playerbattlecode)-1:
                        suffix_card=playerbattlecode[battle_index+1]
                        nextcard=suffix_card
                        concatenated=(card.TYPE)+(nextcard.TYPE)
                        concat_true=(concatenated==Concat_str)
                        if concat_true:
                            concat_result= Concatenations[concat_index]
                            concat_card = Concatenations[concat_index]
                            concat_card_name = concat_card.NAME
                            renpy.call("Concat_anim",prefix_card,suffix_card,concat_result)

                            
                           
    return

label Concat_anim(prefix,suffix,concat_result):
    call showphasemsg("CONCATENATE!") from _call_showphasemsg_2
    $ flashuser = "ILY"
    $ flashdialogue = prefix.TYPE+"-type Battleware "+prefix.NAME+",\n "+suffix.TYPE+"-type Battleware "+suffix.NAME+",\n Concatenate! " +concat_card_name+"!"
    $ renpy.call("FinishingFlash",flashdialogue)
    $ anim_done=False
    python:

        playerbattlecode.pop(battle_index)
        playerbattlecode.pop(battle_index)
        playerbattlecode.insert(battle_index,concat_result)
    $ noscreentransformsfornow=True
    play sound "sfx/swing.wav"
    show screen concat_anim(prefix,suffix)
    show screen whiteflash
    pause 0.5
    hide screen concat_anim
    pause 0.3
    hide screen whiteflash
    show white:
        alpha 1.0 xzoom 0.0 xalign 0.5 yzoom 1.0
        linear 0.2 xzoom 1.0 alpha 0.0
    play sound "sfx/slash.wav"
    show screen Card(concat_result,((640)-150,400),1.0)
    pause
    hide screen Card
    
    return
screen concat_anim(prefix,suffix):
    image "black" at pausedim2

    use Card(prefix,(200,400),1.0)
    use Card(suffix,(780,400),1.0)
    
    text "[prefix.TYPE]" at prefixanim
    text "[suffix.TYPE]" at suffixanim
screen whiteflash:
    image "white" at flashbang2

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
    #Index of looper
    call Concatenation from _call_Concatenation
    $iterations =len(playerbattlecode)
    show screen phasemsg("EXECUTE")
    $renpy.pause(0.5,hard=True)
    hide screen phasemsg

    label exec_loop:

        $ currentcard = playerbattlecode.pop(0)
        # $ currentcard = (playerbattlecode[runnumber])
        $ currentcardFXN = currentcard.FXN
        $ currentcardMAG = currentcard.MAG
        $ currentcardTYPE = currentcard.TYPE
        $ Magnitude = (currentcardMAG)
        $ damagetoenemy=int(playerATK_m*Magnitude)
        $ damagecard = True#("attack" in currentcardFXN[0].name or "attack" in currentcardFXN[1].name)
        call battlecry from _call_battlecry
        # show ring onlayer overlay:
        #     zoom 0.0 xalign 0.5 ypos 0.7 yanchor 0.5 rotate 0
        #     linear 0.15 zoom 1.4 rotate 180 alpha 0.8

        # show cardflash onlayer overlay
        play sound "sound/swing.wav"
        call screen cardflashscreen
        ##
        $fxnindex=0
        $loopingcard=False
        label runfunctions:
            $ runfxnstring = currentcardFXN[fxnindex].name
            label hitloop:
                call functioneffects(runfxnstring) from _call_functioneffects_6
            $fxnindex+=1
            if fxnindex<len(currentcardFXN):
                jump runfunctions

        hide cardflash
        hide ring
        $runnumber+=1
        if (runnumber<iterations) and (battle_done==False):
            jump exec_loop
        else:

            call PlayerEndPhase from _call_PlayerEndPhase
            # info"[playerName]'s turn has ended."
            if not battle_done:
                call enemyattack from _call_enemyattack_1
    return

label PlayerEndPhase:
    if "burn" in EnmySts:
            play sound "sfx/fire.wav"
            python:
              burndmg = 0
              for fxns in EnmySts:
                if fxns=="burn":
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

            show dmgpointb
            call hurtnoise_Ave from _call_hurtnoise_Ave_4
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
    $ playerbits = 8
    return
label EnemyEndPhase:
    if "burn" in PlayerSts:
            python:
              burndmg = 0
              for fxns in PlayerSts:
                if fxns=="burn":
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
            call hurtnoise from _call_hurtnoise_2
            with Shake((0, 0, 0, 0), 0.5, dist=dmgdist)
            $ renpy.pause(0.6,hard=True)


            hide Brnsts
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

        $ fxnindex=0
        label runfunctions2:
            $ runfxnstring = currentcardFXN[fxnindex].name

            # $ hitindex=0
            label hitloop2:
                call enemyfunctioneffects(runfxnstring) from _call_enemyfunctioneffects

            $fxnindex+=1
            if fxnindex<len(currentcardFXN):
                jump runfunctions2

        hide cardflashenemy
        hide ring2
    return
label enemyattack:
    $ enemyrunnumber = 0
    $ enemynumberofattacks = 5 #renpy.random.randint(1,3)+renpy.random.randint(0,2)
    $ enemybits= 8
    $ enemyhand = [enemyDeck[0],enemyDeck[1],enemyDeck[2],enemyDeck[3],enemyDeck[4]]
    show screen phasemsg(enemyName+"'S TURN")
    $renpy.pause(0.9,hard=True)
    hide screen phasemsg
    python:
      for enemyhandcards in range(0,5):
        enemyDeck.pop(0)
    #Buffs Priority
    $ enemyhand.sort(key=lambda x: x.FXN[1].name)
    if playerHP<= int(playerHPMax/2) or ("BoostATK" in EnmySts) or ("Saber" in EnmySts):
      #Damage priority
      $ enemyhand.sort(key=lambda x: x.FXN[0].name)
    elif (enemySP==0) and (enemyHP<=enemyHPMax):
      #Strongest card priority

      $ enemyhand.sort(key=lambda x: x.COST,  reverse = True)
      if "Shield" in enemyhand[0].FXN and "BoostATK" in [handcard.FXN for handcard in enemyhand]:
        $ enemyhand.sort(key=lambda x: x.FXN[1].name)
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
        "RemoveToken":"RemoveTokenPlayer",
        "BoostATK":"BoostATK",
        "BoostDEF":"BoostDEF",
        "ReduceBit":"ReduceBit",
        "":"DoNothing"
    }
label functioneffects(runfxnstring,params=[]):
    # if runfxnstring=="Damage(MAG)":
    #     call Damageenemy
    # elif runfxnstring=="  RemoveEmail()\n  Damage(MAG)":
    #     call RemoveEmailDamageenemy
    # elif runfxnstring=="DamageSP(MAG)":
    #     call DamageSPenemy
    # elif runfxnstring=="DamageSPself(MAG)":
    #     call DamageSPplayer
    # elif runfxnstring=="Shield(MAG)":
    #     call Shieldplayer
    # elif runfxnstring=="Recover(MAG)":
    #     call Recoverplayer
    # elif runfxnstring=="Burn()":
    #     call Burnenemy
    # elif runfxnstring=="Email()":
    #     call Emailenemy
    # elif runfxnstring=="Burnself()":
    #     call Burnself
    # elif runfxnstring=="while E has Email:":
    #     call ForEachEmail
    # elif runfxnstring=="BoostATK()":
    #     call BoostATK
    # elif runfxnstring=="BoostDEF()":
    #     call BoostDEF
    # elif runfxnstring=="ReduceBit()":
    #     call ReduceBit


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
        "GiveToken":"GiveTokenPlayer",
        "GainToken":"GainTokenEnemy",
        "BurnSelf":"Burnenemy",
        "If":"IfTokenInStatusEnemy",
        "While":"WhileTokenInStatusEnemy",
        "RemoveToken":"RemoveTokenEnemy",
        "BoostATK":"BoostATKenemy",
        "BoostDEF":"BoostDEFenemy",
        "Boost":"Boost",
        "ReduceBit":"ReduceBitself",
        "":"DoNothing"
    }
label enemyfunctioneffects(runfxnstring):
    # if runfxnstring=="Damage(MAG)":
    #     call Damageplayer
    # elif runfxnstring=="DamageSP(MAG)":
    #     call DamageSPplayer
    # elif runfxnstring=="DamageSPself(MAG)":
    #     call DamageSPselfenemy
    # elif runfxnstring=="Shield(MAG)":
    #     call Shieldenemy
    # elif runfxnstring=="Recover(MAG)":
    #     call Recoverenemy
    # elif runfxnstring=="Burn()":
    #     call Burnself
    # elif runfxnstring=="Burnself()":
    #     call Burnenemy
    # elif runfxnstring=="BoostATK()":
    #     call BoostATKenemy
    # elif runfxnstring=="BoostDEF()":
    #     call BoostDEFenemy
    # elif runfxnstring=="ReduceBit()":
    #     call ReduceBitself
    # elif runfxnstring=="ReduceBit()":
    #     call ReduceBitself
    $ renpy.call(FxnDirectoryEnemy[runfxnstring])
    return
