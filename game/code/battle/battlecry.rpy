screen finishingflash(say):
    image "black" at pausedim
    add "flashline" at flashtrans

    

    add "diamondblue" at diamondtrans xanchor 0.5 yanchor 0.5 xpos 0.3 ypos 0.25
    add "diamondblue2" at diamondtrans xanchor 0.5 yanchor 0.5 xpos 0.7 ypos 0.75
    add "diamondred" at diamondtrans xanchor 0.5 yanchor 0.5 xpos 0.8 ypos 0.2
    add "diamondred2" at diamondtrans xanchor 0.5 yanchor 0.5 xpos 0.2 ypos 0.8
    add "diamondwhite" at diamondtrans xanchor 0.5 yanchor 0.5 xpos 0.1 ypos 0.9
    add "diamondwhite2" at diamondtrans xanchor 0.5 yanchor 0.5 xpos 0.9 ypos 0.1
    # if anim_done:
    text "{size=25}[say]{/size}" xalign 0.5 ypos 0.74 yanchor 0.0 
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
      # $ damagecard = (currentcardFXN[0].name =="Attack" or currentcardFXN[1].name=="Attack")
      $ currentcardfunctions=[a.name for a in currentcardFXN]
      $ damagecard = ("attack" in currentcardfunctions) 
      $ Magnitude = (currentcardMAG)
      $ enemydamagetoplayer=int(enemyATK_m*Magnitude)+playerburndamage
      if (enemydamagetoplayer>=(playerHP+playerSP)) and (damagecard==True):

        $flashuser="Ave"
        voice "voice/Ave/No, I won't lose!.ogg"
        $ anim_done=False
        
        call screen finishingflash("No, I won't lose, It's over ILY!")
        
      elif (enemyHP <=2800):
        $ avcount=avcount+1
        if avcount == 1:
          voice "voice/Ave/Heeaah.ogg"
          a"Heeaah!"
        elif avcount == 2:
          voice "voice/Ave/Hhaagh.ogg"
          a"Hhagh!!"
        elif avcount == 3:
          voice "voice/Ave/Hrrah!.ogg"
          a"Hrrah!"
        elif avcount == 4:
          voice "voice/Ave/Hah!.ogg"
          a"Hah!"
        elif avcount >= 5:
          voice "voice/Ave/It's Over, ILY!.ogg"
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
      # $ damagecard = (currentcardFXN[0].name =="Attack" or currentcardFXN[1].name=="Attack")
      $ currentcardfunctions=[a.name for a in currentcardFXN]
      $ damagecard = ("attack" in currentcardfunctions) 
        
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
      # $ damagecard = (currentcardFXN[0].name =="Attack" or currentcardFXN[1].name=="Attack")
      $ currentcardfunctions=[a.name for a in currentcardFXN]
      $ damagecard = ("attack" in currentcardfunctions) 
       
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
      # $ damagecard = (currentcardFXN[0].name =="Attack" or currentcardFXN[1].name=="Attack")
      $ currentcardfunctions=[a.name for a in currentcardFXN]
      $ damagecard = ("attack" in currentcardfunctions) 
       
      $ Magnitude = (currentcardMAG)
      $ enemydamagetoplayer=int(enemyATK_m*Magnitude)+playerburndamage
      if (enemydamagetoplayer>=(playerHP+playerSP)) and (damagecard==True):

        $flashuser="Vira"
        # voice "voice/Vira_voice/batlecry1.ogg"
        $ anim_done=False
        pause 0.1
        voice "voice/Vira/My_next_attack_will_definitely_take_you_down.mp3"
        call screen finishingflash("Fine! My next attack will definitely take you down!!")
      else:
        $ avcount=avcount+1
        if avcount == 1:
          voice "voice/Vira/yeahah.mp3"
          v"Haahh!"
        elif avcount == 2:
          voice "voice/Vira/yah.mp3"
          v"Yah!!"
        elif avcount == 3:
          voice "voice/Vira/hah.mp3"
          v"Hah!"
        elif avcount == 4:
          voice "voice/Vira/hoh.mp3"
          v"Hoh!"
        elif avcount >= 5:
          voice "voice/Vira/toh.mp3"
          v"Toh!"
          $avcount=1
    return
init python:
  forcefinish=False
label battlecry:
    
    python:
      burndmg = 0
      for fxns in EnmySts:
        if fxns=="Burn":
          burndmg = burndmg +80
    $ battledamage = damagetoenemy
    $ battledamage += burndmg
    $ can_burn_to_death= (burndmg>=enemyHP) and len(playerbattlecode)==0
    # "[can_burn_to_death]"

    # $ damagecard = (currentcardFXN[0].name =="Attack" or currentcardFXN[1].name=="Attack")
    $ currentcardfunctions=[a.name for a in currentcardFXN]
    $ damagecard = ("attack" in currentcardfunctions) 
    if currentcard.NAME=="MailSaber" or currentcard.NAME=="RecursiveSlash" or currentcard.NAME=="FlameSaber":
      $ forcefinish = True
    
    if ((enemyHP+enemySP)<=battledamage) and (damagecard==True) or forcefinish or can_burn_to_death:
    # or EnemyHP<=(damagetoenemy+burndmg) and 'Recover' not in PlayerFxn) and 'POW_Up' not in PlayerFxn:
      # voice "voice/ILY/ILY24B - Break down & disappear!.mp3"
      
      if enemyName=="Vira" and not forcefinish:
        
        voice "voice/ILY/ILY23B - This is the end, Vira.mp3"
        $ anim_done=False
        $ flashuser = "ILY"
        call screen finishingflash("This is the end, Vira!\nPlease, Listen to me!")
        
      if forcefinish:
        voice "voice/ILY/ILY09 - Finishing move.mp3"
        $ anim_done=False
        $ flashuser = "ILY"
        call screen finishingflash("Finishing Move!")

    else :
      $ vcount=vcount+1
      if vcount == 1:
        voice "voice/ILY/ILY26 - I won't let you.mp3"
        i"I won't let you!"
      elif vcount == 2:
        voice "voice/ILY/ILY08 - This attack, receive it!.mp3"
        i"This attack, receive it!"
      elif vcount == 3:
        voice "voice/ILY/ILY05D - Swing heavy sword sounds.mp3"
        i"Hnnngg--Yah!"
      elif vcount == 4:
        voice "voice/ILY/ILY05C - Swing medium sword sounds.mp3"
        i"Hnnngg--Hah!"
      elif vcount >= 5:
        voice "voice/ILY/ILY05 - Swing light sword sounds.mp3"
        i"Nnnhhhh!"
        $vcount=0
    if forcefinish:
      $ forcefinish=False
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
label hurtnoise_Vira:
    
    if enemyName=="Vira":
      
      $ ahcount=ahcount+1
      if ahcount ==1:
        voice "voice/Vira/hurt/augh.mp3"
      elif ahcount == 2:
        voice "voice/Vira/hurt/ahhw.mp3" 
      elif ahcount == 3:
        voice "voice/Vira/hurt/oww.mp3" 
      elif ahcount == 4:
        voice "voice/Vira/hurt/ouugh.mp3" 
      elif ahcount == 5:
        voice "voice/Vira/hurt/owhw.mp3" 
      elif ahcount == 6:
        voice "voice/Vira/hurt/puppysound.mp3" 
        $ ahcount=0
    return
label hurtnoise:
    
    
    $ hcount=hcount+1
    if hcount ==1:
      play sound "voice/ILY/hurt/ILY13D - Light Bullet Grazed, punched or hit.wav" channel "voice"
    elif hcount == 2:
      play sound "voice/ILY/hurt/ILY13B - Light Bullet Grazed, punched or hit.wav" channel "voice"
    elif hcount == 3:
      play sound "voice/ILY/hurt/ILY13C - Light Bullet Grazed, punched or hit.wav" channel "voice"
    elif hcount == 4:
      play sound "voice/ILY/hurt/ILY05B - Swing light sword sounds.wav" channel "voice"
    elif hcount == 5:
      play sound "voice/ILY/hurt/ILY12J - Bullet Grazed, punched or hit.wav" channel "voice"
      $ hcount=0
    return
