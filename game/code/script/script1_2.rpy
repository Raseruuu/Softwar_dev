
label prescript1_2:
    
    
    return
    "STUFF"
    #Call Scene after approaching tile on Connecht, North of Home area
    j"ILY, when you talk to an entity in there, they won't actually hear me right?"
    i"Yeah, they won't."
    j"That's a relief."
    i"I can also whisper to you when I'm in front of them, and they won't know."
    j"Sounds good."

    #John thinks to himself about the Grid
    return



label script1_2:
    if gameprogress==0:
        call script1_2_map1
        if playerHP<=0:
            return
        # call script1_2_dialog1
        # Imperceptium Hunt Mission Dialogue
        # call script1_2_map2
        # if playerHP<=0:
        #     return
    
    # $ renpy.Rollback()
    
    # call script1_2_map2
    return

label script1_2_map1:
    call mapcall([7,6],stagehome)
    if playerHP<=0:
        return
    $ILY_w = False
    hide screen mapB
    hide screen mapA
    return
label script1_2_map2:
    play music ""
    $ gridpos = [192,164]
    call addsprites(gridpos)
    call mapcall([6,5],stage_ShadyAlley)
    if playerHP<=0:
        return
    $ILY_w = False
    hide screen mapB
    hide screen mapA
    return
label script1_2_dialog1:
    
    if gameprogress==1:
        $ map_active=False
        j"ILY, We can't pass here while Bitwulf is around... If we could sneak in somehow, maybe.."
        
        # $ gridpos = [191,167]
        # call addsprites(gridpos)
        # call maptransfer([11,7],stage_WestGateway)
        python:
            rollbackchanged=False
            if config.rollback_enabled==False:
                config.rollback_enabled=True
                rollbackchanged=True
            renpy.rollback(force=False,checkpoints=2)
        
            
        if playerHP<=0:
            return

        return
    ##Arrived at a checkpoint: meet Melissa
    # scene battlebg
    # show battlebg2
    call hideMapview
    # if gameprogress==1:
    #     "End of Demoaaa"
    #     # $ game_over=True
    #     return 
    # CHANGE SHADY ALLEY ENTRANCEWAY
    $ GRID[(192,165)]=stageBCD2
    # $ GRID[(192,165)]=stageBCD2
    show scrollingBG at scroll
    show battleroad:
        yalign 1.0 xalign 0.5
    with pixellate
    # $ ILY_w =False
    # $ ILY_m ="frown"
    # $ ILY_e ="down"
    # $ Ave_w =False
    # $ Ave_m ="frown"
    # $ Ave_e ="down"

    # show Ave:
    #     xpos 0.9 xanchor 0.5
    # show ILY:
    #     xpos 0.3 xanchor 0.5
    # a"ILY! There you are!! You escaped me before, but I'll delete you this time, worm!!"
    # i"No, you've got it all wrong!"
    # i"I'm not the same as the virus you once fought!"
    # show Ave:
    #     xpos 0.911
    #     pause 0.1
    #     xpos 0.914
    #     pause 0.1
    #     repeat
    # a"Silence! I won't hear another word from a filthy Virus!"

    $ ILY_w =True
    $ ILY_m ="smile"
    $ ILY_e ="up"
    

    i "Looks like this path takes us to Connecht City Cyber Square!"
    "A gate to the west from my home location... that sounds a lot like in real-life."
    "This Cyber Square area... must be a virtual version of the actual Square crossroad at the middle of Connecht."
    "Just a few blocks away on the way to the island mount... is the IRL SDS office." 
    j "So, You think this path is supposed to take us to SDS area?"
    
    i "Oh? How would you know that?" 
    j "The virtual world here seems to mimic the real world locations. Albeit the components of each area are different."
    j "Like, this place is pretty empty in comparison!! And where are the cars?"
    i "... Nice observation, I wouldn't know that!"
    i "Hmmm... "
    "ILY pauses in the middle of traveling to the gate."
    show Bitwulf 
    i "Is that a dog?"
    j "A very futuristic-looking guard dog, it would seem... "
    i "So it is a dog! I wanna pet it!"
    "That's quite the human response, coming from you. Impressive."
    #Approaching Bitwulf Antivirus
    play music "bgm/Pre-Fight_bgm_maoudamashii_cyber01.ogg"
    $ Bitwulf_w=False
    b "Virus Detected!! Executing Termination Protocol..."
    $ Melissa_e="down"
    $ Melissa_m="open"
    
    mu "Watch out! They're on patrol on these hours."
    "Huh? who was that? It's another avatar!"
    "Suddenly, a flash of blue lightning strikes where ILY was standing!"
    "I was about to raise my voice in surprise, until I realized she was safe from it."
    mu "That was close!"
    $ ILY_m ="frown"
    $ ILY_e ="down"
    
    i "An attack!!!"
    scene black
    "That was quick! Just who is this avatar?"
    "This blue-haired avatar just snatched ILY away from that lightning strike.."
    mu "We need to keep moving!"
    i "What's going on?"
    $ Melissa_e="normal"
    $ Melissa_m="frown"
    mu "That was Bitwulf. An Antivirus. They've made it their job to look for Viruses and fight them in Softwars."
    i "I didn't realize Antiviruses would be out here in the open like this!"
    i "That one was quite aggressive.."
    i "And you are a..."
    "ILY and the blue-haired avatar have settled in a different area, far from the East Connecht Gate."
    $ Melissa_m="smile"
    mu "We should be safe here. This zone is covered in anti-detection walls so it's practically invisible to non-viruses."
    "Non-viruses? that means..."
    #unlock Shady Alley
    play music "bgm/ost/Serious_Noyemi_K.ogg"
    scene battlebg
    show scrollingBG at scroll
    show battleroad:
        yalign 1.0 xalign 0.5
    mu "I should introduce myself..."
    "*Gulps*"
    $ Melissa_e="up"
    $ Melissa_w=False
    show Melissa with pixellate
    m "I am the Melissa Virus. We're birds of a feather!"
    "Birds of a feather, huh? Wait, what does this mean for me?"
    "It seems like.. viruses are able to identify each other? I wonder how that works."
    "The Melissa Virus... Another historical virus... It's also popular for infecting via mail..."
    m "We viruses, we look out for each other out here. "
    hide Melissa
    show Melissajump
    extend "You can call me your big sister!"
    show Melissa
    hide Melissajump
    $ ILY_e="up"
    $ ILY_m="smile3"
    i "Big sister... Melissa!"
    j "(ILY! You're too quick to trust her, she's still a virus, you know!)"
    i "(Wait, I got this! She still saved me back there! I should at least...)"
    i "Thank you Melissa!!"
    m "Ohoho! You're welcome."
    
    m "I understand that you are new here? I can tell."
    "How? body language? The fact that we didn't know about ...Bitwulf?"
    "These FAIs aren't to be taken lightly.."
    i "(She's right.. I am a newbie...)"
    j "(You're not the only newbie here, ILY. The entire GRID is also new, right?)"
    i "Oh no!... this cyberworld is pretty new, that's all!"
    $ Melissa_e="normal"
    $ Melissa_m="open"
    m "You are an odd one, {i}we viruses are the original residents here!{/i}"
    "What does she mean by that?"
    $ Melissa_m="frown"
    m "We are FAI Viruses. The GRID has been our home since its inception."
    $ Melissa_e="down"
    show Melissa:
        xoffset -2
        pause 0.1
        xoffset 2
        pause 0.1
        repeat
    m "This is our world. The Antiviruses are taking it from us!"
    
    "Melissa makes the face of a fighter. A frown forms and it looks like she is mad."
    "Also... what was the original purpose of the GRID? she makes it sound like it was made {i}for viruses.{/i}"
    $ Melissa_e="normal"
    hide Melissa
    show Melissa with dissolve
    m "We... don't have the freedom we used to have, and it's because of them."
    m "Bitwulf is just one of them, they've deployed about 7 other powerful antiviruses around Connecht."
    "They? Multiple Antiviruses? She makes it sound like each one has a different name." 
    $ ILY_m="frown"
    i "Do you hate the antiviruses?"
    "What's ILY doing with that kind of query? Programs... Can't love or hate things."
    $ Melissa_e="down"
    m "I'm a virus, what do you think? I should hate the sort of thing that seeks to delete us."
    i "Will you fight them?"
    $ Melissa_e="up"
    $ Melissa_m="smile"
    m "Fighting isn't my strong suit. Someone else here can probably do the dirty work."
    "That tells me that she's not the usual combative type. And that... There's more of them!"
    i "Someone else?"
    m"Maybe Stoned can do something about them."
    "Melissa points at another avatar at the corner."
    i"Stoned? That girl in a red hoodie?"
    $ Melissa_e="normal"
    $ Melissa_m="smile"
    m "That's right. "
    $ Melissa_e="down"
    $ Melissa_m="frown"
    m "Though, We haven't tested how effective her Blazebuster is against Antiviruses."
    i "Ah!"
    #Stoned Virus speaks up
    show Stoned with dissolve:
        xalign 0.7 
    show Melissa with ease:
        xalign 0.3
    $ Stoned_w=False
    s "Hey."
    s"You can call me Stella. Stoned is a bit of an awkward name."
    s"I'm not a fighter either, I'm just a dealer, I'll try to catch up when we start running."
    m "What did you build that cannon for, if we don't end up using it?"
    i "Hehehe! Chekhov's Cannon!"
    s "Like she said, we have only tested it on weak viruses, the output is quite big."
    i "The weak viruses.."
    
    m "Yeah them, they're more like annoying pests, than reliable allies."
    $ Melissa_e="normal"
    $ Melissa_m="smile"
    m "Tell you what, I know a lot of fellow viruses, Lots more, who are stronger than us. I thought I knew them all, until I met you today."
    $ Melissa_e="up"
    
    m "You've piqued my curiosity."
    i "(John, she's examining me, I can feel it!)"
    m "ILY, huh..."
    show Stoned:
        linear 0.2 yoffset -20
        linear 0.1 yoffset 5
        linear 0.1 yoffset 0
    s "Tell me when something interesting happens! I'll be sorting out through my stash."
    s "You, new girl. You're welcome to drop by my shop."
    hide Stoned with dissolve
    show Melissa with ease:
        xalign 0.5
    $ ILY_w=True
    j "(Melissa knows quite a lot... It's an odd feeling to hear all that from a Virus we just met.)"
    i "(John, I realized, that Melissa is taking a huge risk by helping us today.)"
    j "(You think?)"
    i "(I don't know if she realized it, since she is a stray virus... but Viruses can be under command of humans now.)"
    i "(If we decided, we can just send an antivirus to hunt them down anytime.)"
    i "(Melissa has set aside that risk just to help us.)"
    "I'm impressed that ILY can think this far into a trust issue."
    $ ILY_m="smile"
    i "Thank you for trusting me, Melissa."
    $ ILY_m="smile3"
    m "A thank you again? Like I said, you can call me your big sister now."
    
    hide Melissa
    show Melissajump
    m "Sisters always watch each other's backs!"
    show Melissa
    hide Melissajump
    m "If you find trouble with Antiviruses, you can try coming here for help."
    i "I suppose today is not the right time to face Bitwulf..."
    m "Correct. I myself am not prepared with a way to counterattack after evading its lightning strike."
    i "Bitwulf's attack was really quick, you were impressively fast there..."
    m "That's my kinetic vision ability at work! Evading is my specialty."
    i "And you were carrying me with you, too!"
    m "You're not very heavy, anyway."
    i "(I'm not heavy! That preserves my bishoujo image, doesn't it?)"
    "They've simulated weight here just fine, but the entities participating in this world are also largely superhuman."
    "Must be fun to be in their point of view. Rather... \"Exhilarating\"."
    m"I suggest that you speak with Stoned, she'll be staying right here, so check her wares! "
    i"Alrighty!"
    $ gameprogress+=1
    call script1_2_map2
    if playerHP<=0:
        return 
    return
default infobroker_Melissa=False
label Melissascript2:
    if not infobroker_Melissa:
        pass
    else:
        jump paidMelissa
    j "(ILY, can you ask her if there is a way to pass without fighting Bitwulf?)"
    i "(Oh! She did mention... That \"they're on patrol on these hours\")"
    j "(Yeah. It could be a schedule or something.)"
    "Here goes."
    i "Is there a way to get past Bitwulf without fighting?"
    m "There is. Actually, They have a special maintenance period."
    m "Though, It's usually on weekends."
    "!!"
    i "The next weekend is far from now..."
    m "Actually, Would you like to know a little secret?"
    i "A secret! What is it?"
    m "I'd tell you, But I'm actually an info-broker of sorts, I've already spilt a bunch of beans on you..."
    i "(What does that mean, John?)"
    j "(It means she is selling that info for buck. Information really is valuable after all. Especially in this world...)"
    i "Then... how much is it?"
    m "I'll sell it to you for 1000 Zenny."
    j "Do we... have that much?"
    $ infobroker_Melissa=True
    
    if Money >=1000:
        jump payMelissa
        
        
    else:
        i "We can't afford it..."
        j "Are we able to get that much over night?"
        i "Yeah, it should be easy enough, if I could just roam and bust some viruses!"
        j "Hurry up, then."
        

        return

label payMelissa:
    i"Should we give her 1000 Zenny? (We have [Money] Zenny left.)"
    menu:
        i"Should we give her 1000 Zenny?"
        "Yeah sure.":
            
            if Money < 1000:
                j "We still don't have enough."
                i"Stray viruses drop Zenny all the time when I beat them in Softwars."
                $ gridpos = [192,164]
                call addsprites(gridpos)
                call mapcall([6,5],stage_ShadyAlley)
                if playerHP<=0:
                    return
                $ILY_w = False
                hide screen mapB
                hide screen mapA
                return
            else:
                j "Okay... We need that info. Do it, ILY!"
                i "Aye, sir!"
                jump paidMelissa2

        "Wait a minute!":

            j"We need more Zenny."
            i"Stray viruses drop Zenny all the time when I beat them in Softwars."
            j"Right..."
            $ gridpos = [192,164]
            call addsprites(gridpos)
            call mapcall([6,5],stage_ShadyAlley)
            if playerHP<=0:
                return
            $ILY_w = False
            hide screen mapB
            hide screen mapA

            return

label paidMelissa:
    
    m "You got the 1K Zenny?"
    jump payMelissa
    label paidMelissa2:
        $ gameprogress+=1
        i "I got it! Here ya go!"
        $ Money-=1000
        $ map_active=False
        
        hide screen mapB
        scene scrollingBG at scroll
        show battleroad:
            yalign 1.0 xalign 0.5
        $ Melissa_w=True
        m "Ah, Thanks. I may be your big sis, but hey, business is business!"
        j "(She's moneysmart, it looks like.)"
        m "There's a special item you can use to get past their detectors."
        "!!!... That sounds really convenient."
        i "What kind of item is it?"
        m "Hahaha.."
        i "You're... laughing?"
        m "Since you did pay me, I'll tell you. But I do find it funny that you wouldn't know about this."
        m "You're just like me, but you seem inexperienced. This is some basic fundamental stuff."
        i "Uguu..."
        
        
        # $ map_active=False
        # $ game_over=True
        # jump mapresume
        # return
    # return
    m "Alright, Listen!"
    i "Yes!"
    m "The GRID we reside in is composed of a lot of things."
    m "Every entity is not merely built with values inside variables, or a collection of points plotted on 3D space."
    m "Humans will call this place a simulation, just like a game.. But it goes much deeper and more detailed than usual."
    m "We're made of Data Materials. Us Viruses, we are composed of virus cells and tissues."
    m "Our composition allows us to utilize materials with special abilities."
    m "The special data material you want to find is called \"Imperceptium\"."
    i "Imperceptium! right!"
    m "Imperceptium is what Viruses use to stay hidden in the GRID!"
    i "Ah! That does sound like something I should have known."
    m "Imperceptium is hard to find as its surface projects a false image of its true appearance."
    m "Some like to say that it's in constant camouflage."
    m "Viruses can consume imperceptium to absorb that special trait, albeit for a limited time."
    i "How do we find something that's practically invisible?"
    m "Stray wild viruses will drop them. But you can only see it once it's been seared in VirusFlame."
    i "Ah! VirusFlame?"
    m "VirusFlame. You know, every Virus is capable of using that technique. {w}The one where you launch fire from the palm of your hands!"
    m "You really are behind in all this, aren't you?"
    i "Ah, I was just jogging my memory, Ahehehe!!"
    m "Hah! Well, do you plan on searching for it tonight?"
    # j "(ILY, what's stopping Melissa from making a run using Imperceptium?)" 
    # i "I have no idea. Maybe it's not in her interests right now? To pass by that "
    j"(Tonight... I assume it will take a while. Do viruses sleep?)"
    i"(No, us Viruses can stay active as long as we can.)"
    j"(ILY, let's try to hunt for Imperceptium now.)"
    i "Yes! I'll hunt for Imperceptium tonight!"
    "If ILY stays here with the Viruses while I'm asleep, I don't know what could happen.{w} She has to leave them alone tonight."
    "This is the perfect excuse to disappear."
    "If ILY follows a schedule just like mine, a human, she might get perceived as a non-stray Virus. A Virus with a Master."
    "I should be extra careful when interacting with these Viruses."
    
    m "Sounds like you're in a hurry then! See you when I see you!" 
    i "I'll be off!"
    $ playerHP=playerHPMax
    scene black with dissolve
    "ILY exits the Shady Alley area of the GRID."
    "Now that I can see the viruses' perspective, I kind of want to just leave them alone at peace."
    
    show scrollingBG at scroll
    show battleroad:
        yalign 1.0 xalign 0.5
    show ILY with dissolve:
        xalign 0.3
    $ ILY_w=False
    i "..."
    j "Let's go find that imperceptium!"
    
    "ILY quickly took off for the hunt."
    i "Alrighty! I found a virus!"
    
    j "Get ready for battle!"
    i "This one... it's a Worm!"
    j "How fascinating.. it isn't slithery and round like real world worms."
    i "What?"
    j "It's very geometric. It's an interesting design. Is it strong?"
    i "Nah."
    i "They can open and close wormholes, no biggie. That'd be their biggest feat."
    j "No way!"
    i "I'm something of a Worm myself, but I'm more advanced than them."
    i "This should be easy!"
    j "You're a wha??"

    call battlev3(ILY, Worm)
    scene scrollingBG at scroll
    show battleroad:
        yalign 1.0 xalign 0.5
    show ILY with dissolve:
        xalign 0.3
    show Worm:
        xalign 0.75 yalign 0.5 zoom 1.5
    play music "bgm/ost/Serious_Noyemi_K.ogg"
    "ILY made quick work of that virus, amidst its evasive maneuvers, hiding thru wormholes."
    i "For the finishing blow, "
    
    extend "VirusFlame!"
    call cardflash_story(VirusFlame)
    
    show Worm at kickedaway
    "Worm" "SKREEE!!"
    j "You did it!"
    show ILY:
        ease 1.0 xoffset 200
    i "Ahh I found it! it's actually burning."
    # $ renpy.call("GainItem",[Imperceptium]*4)
    # $ new_treasure_battleware_list = {item.NAME: for item in new_treasure}
    # $ 
    call GainItem([shop_item("Imperceptium",item,"Material",pricelist["Imperceptium"])]*4)
    "ILY picked up the burning imperceptium material."
    i "Melissa says I just have to ingest this, and I'd be invisible!"
    j "I wonder if it will really work!"
    i "I trust that Melissa is telling the truth!"
    
    $ map_visible=False
    "Chapter 1 End"

    return




