screen finishingflash(say):
    image "black" at pausedim
    add "flashline" at flashtrans

    text "{size=25}[say]{/size}" xalign 0.5 yalign 0.80

    add "diamondblue" at diamondtrans xanchor 0.5 yanchor 0.5 xpos 0.3 ypos 0.25
    add "diamondblue2" at diamondtrans xanchor 0.5 yanchor 0.5 xpos 0.7 ypos 0.75
    add "diamondred" at diamondtrans xanchor 0.5 yanchor 0.5 xpos 0.8 ypos 0.2
    add "diamondred2" at diamondtrans xanchor 0.5 yanchor 0.5 xpos 0.2 ypos 0.8
    add "diamondwhite" at diamondtrans xanchor 0.5 yanchor 0.5 xpos 0.1 ypos 0.9
    add "diamondwhite2" at diamondtrans xanchor 0.5 yanchor 0.5 xpos 0.9 ypos 0.1
    # if anim_done:
    key 'mouseup_1' action Return()
    key 'K_RETURN' action Return()
    key 'K_SPACE' action Return()
    key 'K_KP_ENTER' action Return()
    key 'K_SELECT' action Return()
    key 'z' action Return()
    key 'Z' action Return()
    key 'x' action Return()
    key 'X' action Return()
transform flashtrans:
    alpha 0.0
    pause 0.35
    xpos 0.0 xanchor 1.0 yalign 0.5 alpha 1.0
    linear 0.1 xalign 0.5
    pause 0.1
    linear 0.1 yzoom 1.1
    linear 0.08 yzoom 1.0
image flashline:
    "images/battle/flashpanel/bar.png"
    pause 0.8
    "images/battle/flashpanel/frame.png"
    yzoom 0.5
    pause 0.1
    "images/battle/flashpanel/frame.png"
    yzoom 1.1
    pause 0.1
    "images/battle/flashpanel/[flashuser].png"
    yzoom 1.0
image diamondblue:
    "images/battle/flashpanel/diamondblue.png"
    zoom 0.5
image diamondblue2:
    "diamondblue"
    zoom 0.8
image diamondred:
    "images/battle/flashpanel/diamondred.png"
    zoom 0.7
image diamondred2:
    "diamondred"
    zoom 0.9
image diamondwhite2:
    "images/battle/flashpanel/diamondwhite.png"
    zoom 0.7
image diamondwhite2:
    "diamondwhite"
    zoom 0.9

transform diamondtrans:

    alpha 0.0
    pause 0.8
    block:
        alpha 1.0
        xoffset 10 yoffset -16
        pause 0.08
        xoffset 0 yoffset 20
        pause 0.08
        xoffset -10 yoffset -17
        pause 0.08
        repeat
label battlecry_Ave:
    if enemyName=="Ave":
      python:
        burndmg = 0
        for fxns in PlayerSts:
          if fxns=="burn":
            burndmg = burndmg +40
      $ playerburndamage = burndmg
      $ damagecard = (currentcardFXN[0].name =="attack" or currentcardFXN[1].name=="attack")
      $ Magnitude = (currentcardMAG)
      $ enemydamagetoplayer=int(enemyATK_m*Magnitude)+playerburndamage
      if (enemydamagetoplayer>=(playerHP+playerSP)) and (damagecard==True):

        $flashuser="Ave"
        voice "voice/Ave_voice/No, I won't lose!.ogg"
        $ anim_done=False
        pause 0.1
        call screen finishingflash("No, I won't lose, It's over ILY!")

      elif (enemyHP <=2800):# and 'POW_Up' not in PlayerFxn:
        $ avcount=avcount+1
        if avcount == 1:
          voice "voice/Ave_voice/Heeaah.ogg"
          a"Heeaah!"
        elif avcount == 2:
          voice "voice/Ave_voice/Hhaagh.ogg"
          a"Hhagh!!"
        elif avcount == 3:
          voice "voice/Ave_voice/Hrrah!.ogg"
          a"Hrrah!"
        elif avcount == 4:
          voice "voice/Ave_voice/Hah!.ogg"
          a"Hah!"
        elif avcount >= 5:
          voice "voice/Ave_voice/It's Over, ILY!.ogg"
          a"It's over, ILY!"
          $avcount=1
    return
label battlecry_Melissa:
    if enemyName=="Melissa":
      python:
        burndmg = 0
        for fxns in PlayerSts:
          if fxns=="burn":
            burndmg = burndmg +40
      $ playerburndamage = burndmg
      $ damagecard = (currentcardFXN[0].name =="attack" or currentcardFXN[1].name=="attack")
      $ Magnitude = (currentcardMAG)
      $ enemydamagetoplayer=int(enemyATK_m*Magnitude)+playerburndamage
      if (enemydamagetoplayer>=(playerHP+playerSP)) and (damagecard==True):

        $flashuser="Melissa"
        # voice "voice/Melissa_voice/batlecry1.ogg"
        $ anim_done=False
        pause 0.1
        call screen finishingflash("You can't stop us!")
    return
label battlecry_CodeRed:
    if enemyName=="Code Red":
      python:
        burndmg = 0
        for fxns in PlayerSts:
          if fxns=="burn":
            burndmg = burndmg +40
      $ playerburndamage = burndmg
      $ damagecard = (currentcardFXN[0].name =="attack" or currentcardFXN[1].name=="attack")
      $ Magnitude = (currentcardMAG)
      $ enemydamagetoplayer=int(enemyATK_m*Magnitude)+playerburndamage
      if (enemydamagetoplayer>=(playerHP+playerSP)) and (damagecard==True):

        $flashuser="CodeRed"
        # voice "voice/CodeRed_voice/batlecry1.ogg"
        $ anim_done=False
        pause 0.1
        call screen finishingflash("I'll destroy you!!")
    return
label battlecry_Vira:
    if enemyName=="Vira":
      python:
        burndmg = 0
        for fxns in PlayerSts:
          if fxns=="burn":
            burndmg = burndmg +40
      $ playerburndamage = burndmg
      $ damagecard = (currentcardFXN[0].name =="attack" or currentcardFXN[1].name=="attack")
      $ Magnitude = (currentcardMAG)
      $ enemydamagetoplayer=int(enemyATK_m*Magnitude)+playerburndamage
      if (enemydamagetoplayer>=(playerHP+playerSP)) and (damagecard==True):

        $flashuser="Vira"
        # voice "voice/Vira_voice/batlecry1.ogg"
        $ anim_done=False
        pause 0.1
        call screen finishingflash("Fine! My next attack will definitely take you down!!")
    return
label battlecry:
    python:
      burndmg = 0
      for fxns in EnmySts:
        if fxns=="burn":
          burndmg = burndmg +40
    $ damagetoenemy += burndmg
    if ((enemyHP+enemySP)<=damagetoenemy) and (damagecard==True):
    # or EnemyHP<=(damagetoenemy+burndmg) and 'Recover' not in PlayerFxn) and 'POW_Up' not in PlayerFxn:
      voice "voice/ILY24B - Break down & disappear!.mp3"
      $ anim_done=False
      $ flashuser = "ILY"
      call screen finishingflash("Break down and disappear!")

    elif (playerHP <=1500):# and 'POW_Up' not in PlayerFxn:
      $ vcount=vcount+1
      if vcount == 1:
        voice "voice/ILY26 - I won't let you.mp3"
        i"I won't let you!"
      elif vcount == 2:
        voice "voice/ILY08 - This attack, receive it!.mp3"
        i"This attack, receive it!"
      elif vcount == 3:
        voice "voice/ILY05D - Swing heavy sword sounds.mp3"
        i"Hnnngg--Yah!"
      elif vcount == 4:
        voice "voice/ILY05C - Swing medium sword sounds.mp3"
        i"Hnnngg--Hah!"
      elif vcount >= 5:
        voice "voice/ILY05 - Swing light sword sounds.mp3"
        i"Nnnhhhh!"
        $vcount=0
    return
label hurtnoise_Ave:
    if enemyName=="Ave":
      $ ahcount=ahcount+1
      if ahcount ==1:
        play sound "voice/Ave_voice/hurt/Eugh!.ogg" channel "voice"
      elif ahcount == 2:
        play sound "voice/Ave_voice/hurt/Euh!.ogg" channel "voice"
        $ ahcount=0
    return
label hurtnoise:
    $ hcount=hcount+1
    if hcount ==1:
      play sound "voice/hurt/ILY13D - Light Bullet Grazed, punched or hit.wav" channel "voice"
    elif hcount == 2:
      play sound "voice/hurt/ILY13B - Light Bullet Grazed, punched or hit.wav" channel "voice"
    elif hcount == 3:
      play sound "voice/hurt/ILY13C - Light Bullet Grazed, punched or hit.wav" channel "voice"
    elif hcount == 4:
      play sound "voice/hurt/ILY05B - Swing light sword sounds.wav" channel "voice"
    elif hcount == 5:
      play sound "voice/hurt/ILY12J - Bullet Grazed, punched or hit.wav" channel "voice"
      $ hcount=0
    return
