
label whatactor:
    if actornum == '2':
      i"That's the virus!"
      $ John_m = "sad"
      $ John_e = "mad"
      j"Get Ready, Ily!"
      hide screen mapA
      hide screen mapB
      return
    elif len(actornum)>1:
      if actornum == 'Ave':
        if objectbelow=="Ave":
          $ILY_m='smile'
          $ILY_e='2'
          i"SPECIAL MOVE: VIRUS ATTACK FROM BEHIND!!"
        a"YOU'RE A VIRUS!! I MUST DESTROY YOU!"
        hide screen mapB
        hide screen mapA
        call battlev3(ILY,Ave) from _call_battlev3_1
        if playerHP<=0:
            return
        $ enemy_encounter=False
        $ map_active=True
        call mapresume from _call_mapresume
        return
      elif actornum == 'Melissa':
        $ ILYSprite("mad")
        i"Melissa Virus! You betrayed me!"
        m"So you've found out!"
        i"How could you!?"
        m"I'm a virus! what did you expect?"
        hide screen mapB
        hide screen mapA
        call battlev3(ILY,Melissa) from _call_battlev3_2
        if playerHP<=0:
            return
        $ enemy_encounter=False
        $ map_active=True
        call mapresume from _call_mapresume_1
        return
      elif actornum == 'CodeRed':
        if objectbelow=="CodeRed":
          $ILY_m='smile'
          $ILY_e='2'
          i"SPECIAL MOVE: VIRUS ATTACK FROM BEHIND!!"
        $CodeRed_w=True
        c"I'm just doing my job!"
        hide screen mapB
        hide screen mapA
        call battlev3(ILY,CodeRed) from _call_battlev3_3
        if playerHP<=0:
            return
        $ enemy_encounter=False
        $ map_active=True
        call mapresume from _call_mapresume_2
        return
      elif actornum == 'Vira':
        if objectbelow=="Vira":
          $ILY_m='smile'
          $ILY_e='2'
          i"SPECIAL MOVE: VIRUS ATTACK FROM BEHIND!!"
        $Vira_w=True
        v"Uguu! What do you want!!"
        hide screen mapB
        hide screen mapA
        call battlev3(ILY,Vira) from _call_battlev3_4
        if playerHP<=0:
            return
        $ enemy_encounter=False
        $ map_active=True
        call mapresume from _call_mapresume_3
        return
      elif actornum == 'Program-kun':
        $ILYSprite("smile")
        "Program-kun""Aren't you just curious to see what's on the other side of this door?"
        i"I'm curious too!"
        "Program-kun""I'm so curious, that I can't move aside!"
        $ILYSprite("mad")
        i"..."
        return
      elif actornum == 'Stella':
        "Stella""Hey! You're like us."
        $ILYSprite("o")
        i"You're a virus...!"
        "Stella""They call me Stoned Virus, but Stella is a prettier name."
        $ILYSprite("smile")
        i"I love you already!"
        "Stella""Heh!"
        return
      elif actornum == 'Bella':
        "Bella""Hello ILY from SOFTWAR."
        $ILYSprite("smile")
        i"Hello Bella from LunarLux!!"

        "Bella""Heh!"
        return
      elif actornum == 'Heart':
        i"Would you like to restore HP?"
        menu:
          "Would you like to restore HP?"
          "Yes":
            $playerHP=playerHPMax
            play sound "sfx/heal.ogg"
            "[playerName]'s Health Points have been restored."
          "No":
            i"OK."
      elif actornum == 'Melissa':
         call script2 from _call_script2
      show screen mapB
      call screen mapA
      call Returns from _call_Returns
      return
    else:
      show screen mapB
      call screen mapA
      call Returns from _call_Returns_1
    return
label PlatformTalk:
    "Uguu"
    return
label MapTalk:
    # if boxsheet == stagehome:
    if boxsheet:
      $ maptalks+=1
      if maptalks==1:
        i"John! Let's try to locate SDS."
        j"Where is it again?"
        i"There should be a gateway to the west from here!"
      elif maptalks==2:
        i"Are you enjoying the GRID?"
        j"I'll say. it's quite interesting."
        i"How?"
        j"It resembles the real world, here at Connecht City."
        $ maptalks=0



      show screen mapB
      call screen mapA
      call Returns from _call_Returns_2
      return
    else:
      show screen mapB
      call screen mapA
      call Returns from _call_Returns_3
    return
