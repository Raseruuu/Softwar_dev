
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
    $ILYSprite("O")
    "Program-kun""Sorry, you can't pass here now... We're working on the highway!"
    i"What's going on?"
    "Program-kun""It's under maintenance!"
    $ILYSprite("mad")
    i"..."
    "Program-kun""You gotta follow the rules!"
    i"...{w} ... {w} Fine."
    


    return
default Stella_talk=0
default shop_active=False
label maptalk_Stella:
    
    if Stella_talk==0:
        $ Stoned_w=True
        $ ILY_w=True
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
        i"I see!... wait, no I don't! It's invisible!"
        s"Heh!"
        s"You should come here often. I have lots of items for sale."
        i"Woah! That's pretty cool!"

        $ILYSprite("smile")
        $ Stella_talk+=1
    else:
        $ Stoned_m="open2"
        $ Stoned_e="up"
        $ Stoned_eyes="open"
        
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
    be"Hi! Have you seen a small red robot around anywhere? Her name is Tetra!"
    $ILYSprite("smile")
    i"A Red Robot named Tetra? huh... Sorry, I didn't see her."
    be"Please tell me if you find her!"
    i"Got it!"
    return
label maptalk_Tetra_1:
    $ ILY_m="O"
    $ ILY_e="up"
    "Tetra" "I'm lost."
    i "Ah! By any chance are you the Red Robot named Tetra?"
    "Tetra" "Yes! how did you know?"
    $ ILY_m="smile3"
    $ ILY_e="up"
    i "A pink-haired girl with a sleek red battle suit was just looking for you!"
    "Tetra" "That must have been Bella!! "
    $ ILY_m="O"
    $ ILY_e="up"
    i "What happened? How did you get separated?"
    "Tetra" "We must have been split when we reached this narrow street while exploring."
    i"But this is the Undernet!!"
    "Tetra" "The Undernet? Yikes! So that's why I saw a bunch of viruses everyhwere!"
    j "(Could it be that Tetra was tricked by some virus?)"
    i "Let's go back and see her!"

    return
label maptalk_Guy_cheese:
    $ ILY_m="smile3"
    $ ILY_e="up"
    "Guy" "OK, this is wild, I discovered this virtual world has food items.."
    "Guy" "I'm trying to collect whatever I can, I have bread, some apples, tomatoes... and.. fish?"
    "Guy" "Do you think this place has cheese too?"
    i "How curious!"
    j "(Cheese? It would be quite the interesting find. If the simulation follows real world facts... If cheese exists, milk does too.)"
    i "If there's milk, then there's cheese too!"
    "Guy" "You might be right. Never seen a cow either."

    i "I'll come here if I find one!"
    "Guy""Awesome!! I'll definitely pay you back!"
    return

label maptalk_ProgramKun2:
    $ ILY_m="smile3"
    $ ILY_e="normal"
    "Program-Kun" "Hey! Do you like the battle system so far?"
    "Program-Kun" "Far... Far... Ahh! I remembered. {b}Short-range{/b} attacks will miss if the opponent is {b}too FAR{/b}."
    i "The attack missed? A short-range attack?"
    "Program-Kun" "Yeah.. You gotta watch out for the DISTANCE variable in battle!"
    "Program-Kun" "If your battleware's {b}\"attack()\"{/b} function doesn't have enough {b}\"range\"{/b} to match the distance, your attack will {b}MISS!{/b}"
    "Program-Kun" "Some examples of short-range attack Battleware are the Saber cards."
    i "I see! How do I get the attacks to hit?"
    "Program-Kun" "You would try to use the {b}\"advance()\"{/b} or {b}\"pull()\"{/b} functions!"
    i "Alrighty! I use swords in my deck, so this will definitely be useful!"
    "Program-Kun" "If you miss with an attack that has less than the current distance, you will move closer to the enemy, and the distance will automatically reduce."
    $ ILY_m="O"
    $ ILY_e="up"
    i "Even if I don't use an advancing card? That's neat!"
    
    $ ILY_m="smile3"
    $ ILY_e="up"
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
    if gameprogress<=1:
        call Melissascript2
        $ gameprogress+=1
        return
    elif gameprogress==2:
        call hideMapview
        jump payMelissa
        return

label whatactor:
    # "[actornum]"
    
    if len(actornum)>=2:
        $ spritelabel=actornum
        $ pausemenu=True
        $ labels_in_spritelist=[sprite.dialogue for sprite in spritelist]
        python:
            for labels in labels_in_spritelist:
                if actornum in labels:
                    spritelabel=labels
        # "[spritelabel]"
        if actornum in samedialog:
            $ renpy.call("maptalk_"+str(spritelabel))
        elif "dialog" not in spritelabel    :
            $ renpy.call("maptalk_"+str(spritelabel)+"_"+str(chapternum))
        $ map_active=True
        if "story" in spritelabel:
            $ map_active=False
            return
        elif game_over or playerHP==0:
            $ map_active=False
            # "over is game"
            return 
        else:
            $ mapbuttons_visible= True
            call mapresume
        # else:
        #     $ renpy.call("maptalk_"+str(actornum))

    if game_over:
        return 
    $ mapbuttons_visible= True
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
                if infobroker_Melissa:
                    i"We gotta pay Melissa 1000 Zenny, John!"
                    j"Ah, right, If we don't get her that much, we'll never know how to pass through that Gate."
                    j"How do we earn 1000 Zenny?"
                    i"Leave it to me! Let me bust some viruses! FAI viruses drop them when you beat them in a SoftWar."
                else:
                    j "Do you think Melissa can tell us how to pass through the gate without fighting Bitwulf?"
                    i "We wouldn't know unless we try!"
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
