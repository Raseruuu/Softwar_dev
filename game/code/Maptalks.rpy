
label maptalk_Ave_0:
    if objectbelow=="Ave":
      $ILY_m='smile'
      $ILY_e='2'
      i"SPECIAL MOVE: VIRUS ATTACK FROM BEHIND!!"
    a"YOU'RE A VIRUS!! I MUST DESTROY YOU!"
    hide screen mapB
    hide screen mapA
    call battlev3(ILY,Ave)
    if playerHP<=0:
        return
    $ enemy_encounter=False
    $ map_active=True
    call mapresume
    return
label maptalk_Melissa_0:
    $ ILYSprite("mad")
    i"Melissa Virus! You betrayed me!"
    m"So you've found out!"
    i"How could you!?"
    m"I'm a virus! what did you expect?"
    hide screen mapB
    hide screen mapA
    call battlev3(ILY,Melissa)
    if playerHP<=0:
        return
    $ enemy_encounter=False
    $ map_active=True
    call mapresume
    return
label maptalk_CodeRed_0:
    if objectbelow=="CodeRed":
        $ILY_m='smile'
        $ILY_e='2'
        i"SPECIAL MOVE: VIRUS ATTACK FROM BEHIND!!"
    $CodeRed_w=True
    c"I'm just doing my job!"
    hide screen mapB
    hide screen mapA
    call battlev3(ILY,CodeRed)
    if playerHP<=0:
      return
    $ enemy_encounter=False
    $ map_active=True
    call mapresume
    return
label maptalk_Vira_0:
    if objectbelow=="Vira":
        $ILY_m='smile'
        $ILY_e='2'
        i"SPECIAL MOVE: VIRUS ATTACK FROM BEHIND!!"
    $Vira_w=True
    v"Uguu! What do you want!!"
    hide screen mapB
    hide screen mapA
    call battlev3(ILY,Vira)
    if playerHP<=0:
      return
    $ enemy_encounter=False
    $ map_active=True
    call mapresume
    return
label maptalk_ProgramKun_0:
    $ILYSprite("smile")
    "Program-kun""Aren't you just curious to see what's on the other side of this door?"
    i"I'm curious too!"
    "Program-kun""I'm so curious, that I can't move aside!"
    $ILYSprite("mad")
    i"..."
    return
label maptalk_Stella_0:
    "Stella""Hey! You're like us."
    $ILYSprite("o")
    i"You're a virus...!"
    "Stella""They call me Stoned Virus, but Stella is a prettier name."
    $ILYSprite("smile")
    i"I love you already!"
    "Stella""Heh!"
    return
label maptalk_Virus_0:
  i"It's a stray virus!"
  $ John_m = "sad"
  $ John_e = "mad"
  j"Get Ready, Ily!"
  hide screen mapA
  hide screen mapB
  return
label maptalk_Melissa_1:
   call script2
   return
label whatactor:

    $ renpy.call("maptalk_"+str(actornum)+"_0")
    show screen mapB
    call screen mapA
    call Returns
    return

      # elif actornum == 'Bella':
      #   "Bella""Hello ILY from SOFTWAR."
      #   $ILYSprite("smile")
      #   i"Hello Bella from LunarLux!!"
      #
      #   "Bella""Heh!"
      #   return
      # elif actornum == 'Heart':
      #   i"Would you like to restore HP?"
      #   menu:
      #     "Would you like to restore HP?"
      #     "Yes":
      #       $playerHP=playerHPMax
      #       play sound "sfx/heal.ogg"
      #       "[playerName]'s Health Points have been restored."
      #     "No":
      #       i"OK."
      # elif actornum ==
    #   show screen mapB
    #   call screen mapA
    #   call Returns
    #   return
    # else:
    #   show screen mapB
    #   call screen mapA
    #   call Returns

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
