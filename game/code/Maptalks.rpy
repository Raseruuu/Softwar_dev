
label maptalk_Ave_1:
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
    i"Melissa! You betrayed me!"
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
label maptalk_CodeRed_1:
    if objectbelow=="CodeRed":
        $ILY_m='smile'
        $ILY_e='2'
        i"!!"
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
label maptalk_Vira_1:
    # if objectbelow=="Vira":
    #     $ILY_m='smile'
    #     $ILY_e='down'
    #     i"SPECIAL MOVE: VIRUS ATTACK FROM BEHIND!!"
    $Vira_w=True
    v"Uguu! What do you want!!"
    i"Gah, it's an Antivirus!"
    j"Brace yourself!!"
    v"Take this!!"
    "(Vira is here for DEMO ONLY)"
    hide screen mapB
    hide screen mapA
    call battlev3(ILY,Vira)
    if playerHP<=0:
      return
    $ enemy_encounter=False
    $ map_active=True
    call mapresume
    return
label maptalk_ProgramKun_1:
    $ILYSprite("smile")
    "Program-kun""Aren't you just curious to see what's on the other side of this door?"
    i"I'm curious too!"
    "Program-kun""I'm so curious, that I can't move aside!"
    $ILYSprite("mad")
    i"..."
    return
default Stella_talk=0
default shop_active=False
label maptalk_Stella:
    
    if Stella_talk==0:
        s"Hey! You're like us."
        $ILYSprite("o")
        i"You're a virus...!"
        s"They call me Stoned Virus, but Stella is a prettier name."
        $ILYSprite("smile")
        i"I love you already!"
        s"Heh!"
        i"What are you doing here?"
        s"This is our turf! Nobody goes by this alley. You're here because you're like us!"
        s"You don't see it, but there's a special invisible barrier there blocking regular avatars."
        s"To them, this place is blocked by a wall!"
        $ILYSprite("o")
        i"I see!... wait, no I don't! it's invisible!"
        s"Heh!"
        s"You should come here often. i have lots of items for sale."
        i"Woah! That's pretty cool!"

        $ILYSprite("smile")
        $ Stella_talk+=1
    else:
        $ Stoned_m="sad"
        $ Stoned_e="up"
        
        $ shop_page=0
        s"What do you want?"
        $ Stoned_m="happy"
        $ Stoned_e="normal"
        
    $ shop_active=True
    $ Stoned_w = False

    show screen item_shop()
    $ renpy.set_focus("item_shop", "shop_button0")

    while shop_active:
        window hide
        # show screen shop_image()


        pause
        hide screen shop_prompt
        # hide screen item_shop
        # if _return =="ItemModal":
        #     # show screen shop_image
        #     $ notransform=True
        #     $ noscreentransformsfornow=True
        #     call screen ItemModal

    hide screen shop_image
    hide screen item_shop
    $ say_shop_mode=False
    $ Stoned_w = True

    return
label maptalk_Virus_1:
  i"It's a stray virus!"
  $ John_m = "sad"
  $ John_e = "mad"
  j"Get Ready, ILY!"
  hide screen mapA
  hide screen mapB
  return
label maptalk_Bella_1:
      # elif actornum == 'Bella':
    # "Bella""Hello ILY from SOFTWAR."
    "Bella""Hi! Have you seen a small red robot around anywhere? Her name is Tetra!"
    $ILYSprite("smile")
    i"A Red Robot named Tetra? huh... Sorry, I didn't see her."
    "Bella""Please tell me if you find her!"
    i"Got it!"
    return
label maptalk_Tetra_1:
  
  "Tetra" "I'm lost."
  i "Ah! By any chance are you the Red Robot named Tetra?"
  "Tetra" "Yes! how did you know?"
  i "A pink-haired girl with a sleek red battle suit was just looking for you!"
  "Tetra" "That must have been Bella!! "
  i "What happened? How did you get separated?"
  "Tetra" "We must have been split when we reached this narrow street while exploring."
  i"But this is the Undernet!!"
  j "(Could it be that Tetra was tricked by some virus?)"
  "Tetra" "The Undernet? Yikes! So that's why I saw a bunch of viruses everyhwere!"
  i "Let's go back!
  "

  return
label maptalk_Heart:
    # i"Would you like to restore HP?"
    $ ILY_m="smile3"
    $ ILY_e="up"
    
    menu:
        i"Would you like to restore HP?"
        "Yes":
          $ HPalreadyfull=playerHP==playerHPMax
          $playerHP=playerHPMax
          play sound "sfx/heal.ogg"
          if HPalreadyfull:
            "[playerName]'s Health Points are already full."
          else:
            "[playerName]'s Health Points have been restored."

        "No":
          i"OK."
    return
label maptalk_Melissa_story_1:
   $ Melissa_w=True
   if gameprogress==0:
      call Melissascript2
      return
   elif gameprogress==1:
      return
    
   
define samedialog = ["Heart","Stella"]
label whatactor:
    $ pausemenu=True
    if len(actornum)>2:
      $ spritelabel=actornum
      $ labels_in_spritelist=[sprite.dialogue for sprite in spritelist]
      python:
          for labels in labels_in_spritelist:
            if actornum in labels:
              spritelabel=labels
      if actornum in samedialog:

        
        $ renpy.call("maptalk_"+str(spritelabel))
      else:
        
          
        $ renpy.call("maptalk_"+str(spritelabel)+"_"+str(chapternum))

      $ map_active=True
      if "story" in spritelabel:
        $ map_active=False
        return
      else:
        call mapresume
      # else:
      #     $ renpy.call("maptalk_"+str(actornum))

    if game_over:
        return 
    
    show screen mapB
    call screen mapA
    call Returns
    
    return


label PlatformTalk:
    "Uguu"
    return
default gameprogress=0
label MapTalk:
    # if boxsheet == stagehome:
    if boxsheet:
      $ maptalks+=1
      if gameprogress==0:
        if maptalks==1:
          $ ILY_m="frown"
          $ ILY_e="down"
          i"John! Let's try to locate SDS."
          $ John_m="frown"
          $ John_e="normal"
          j"Which direction was it again?"
          $ ILY_m="smile3"
          $ ILY_e="normal"
          i"There should be a gateway to the west from here!"
        elif maptalks==2:
          $ ILY_m="smile3"
          $ ILY_e="normal"
          i"Are you enjoying the GRID?"
          j"I'll say. it's quite interesting."
          i"How?"
          j"It resembles the real world, here at Connecht City."
          $ maptalks=0
############## MELISSA PAY QUEST
      elif gameprogress==1:
        if maptalks==1:
          i"We gotta pay Melissa 3000 Zenny, John!"
          j"Ah, right, If we don't get her that much, we'll never know how to pass through that Gate."
          j"How do we earn 3000 Zenny?"
          i"Leave it to me! Let me bust some viruses! FAI viruses drop them when you beat them in a SoftWar."

        elif maptalks==2:
          i"What do you think of Melissa?"
          j"She's pretty hot stuff."
          i"Whaaa!?"
          j"What's that reaction for?"
          $ maptalks=0




      show screen mapB
      call screen mapA
      call Returns
      return
    else:
      show screen mapB
      call screen mapA
      call Returns
    return
