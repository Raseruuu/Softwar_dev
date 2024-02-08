label hideMapview:
    $ map_active=False
    $ quick_menu=True
    hide screen mapB
    return
label prescript2:
    call hideMapview
    j"That means going North from there leads to SDS office."
    i"you figured that out already?"
    
    return
    "STUFF"
    #Call Scene after approaching tile on Connecht, North of Home area
    j"ILY, when you talk to an entity in there, they won't actually hear me right?"
    i"Yeah, they won't."
    j"That's a relief."
    i"I can also whisper to you when I'm in front of them, and they won't know."
    j"Sounds good."

    #John thinks to himself about the Grid
    

label script2:
    ##Arrived at a checkpoint: meet Melissa
    # scene battlebg
    # show battlebg2
    $ map_active=False
    hide screen mapB
    show scrollingBG at scroll
    show battleroad:
        yalign 1.0 xalign 0.5
    i "Looks like this path takes us to Connecht City Cyber Square!"
    "A gate to the west from my home location... that sounds a lot like in real-life."
    "This Cyber Square area... must be a virtual version of the actual Square crossroad at the middle of Connecht."
    "Just a few blocks away on the way to the island mount... is the IRL SDS office." 
    j "So, You think this path is supposed to take us to SDS area?"
    i "Oh? How would you know that?" 
    j "The virtual world here seems to mimic the real world locations. Albeit the components of each area is different."
    j "Like, this place is pretty empty in comparison!! And where are the cars?"
    i "... nice observation, I wouldn't know that!"
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
    
    mu "Watch out! they're on patrol on these hours."
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
    "The Melissa Virus... Another historical virus... It's also popular for infecting mail..."
    m "We viruses, we look out for each other out here. You can call me your big sister!"
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
    j "(You're not the only newbie here, ILY. the entire GRID is also new, right?)"
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
    i"That girl in a red hoodie?"
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
    s "Hey, I'm not a fighter either, I'm just a dealer, I'll try to catch up when we start running."
    m "What did you build that cannon for, if we don't end up using it?"
    i "Hehehe! Chekhov's Cannon!"
    s "Like she said, we have only tested it on weak viruses, the output is quite big."
    i "The weak viruses.."
    
    m "Yeah them, there more like annoying pests, than reliable allies."
    $ Melissa_e="normal"
    $ Melissa_m="smile"
    m "Tell you what, I know a lot of fellow viruses, Lots more, who are stronger than us. I thought I knew them all, until I met you today."
    $ Melissa_e="up"
    m "You've piqued my curiosity."
    i "(John, she's examining me, I can feel it)"
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
    j "(Melissa knows quite a lot... It's an odd feeling to hear all this from a Virus we just met.)"
    i "(John, I realized, that Melissa is taking a huge risk by helping us today.)"
    j "(You think?)"
    i "(I don't know if she realized it, since she is a stray virus... but Viruses can be under command of humans now.)"
    i "(If we decided, we can just send an antivirus to hunt them down anytime.)"
    i "(Melissa has set aside that risk just to help us.)"
    "I'm impressed that ILY can think this far into a trust issue."
    i "Thank you for trusting me, Melissa."
    m "A thank you again? Like I said, you can call me your big sister now."
    m "Sisters always watch each other's backs!"
    m "If you find trouble with Antiviruses, you can try coming here for help."
    i "I suppose today is not the right time to face Bitwulf..."
    m "Correct. I myself am not prepared with a way to counterattack after evading its lightning attack."
    i "Bitwulf's attack was really quick, you were impressively fast there..."
    m "That's my kinetic vision ability at work! Evading is my specialty."
    i "And you were carrying me with you, too!"
    m "You're not very heavy, anyway."
    i "(I'm not heavy! That preserves my bishoujo image, doesn't it?)"
    "They've simulated weight here just fine, but the entities participating in this world are also largely superhuman."
    "Must be fun to be in their point of view. Rather... \"Exhilarating\"."
    j "(ILY, can you ask her if there is a way to pass without fighting Bitwulf?)"
    i "(Oh! She did mention... That \"they were on patrol around these hours\")"
    j "(Yeah. It could be a schedule or something.)"
    i "Is there a way to get past Bitwulf without fighting?"
    m "There is. Actually, They have a special maintenance period."
    m "Though, It's usually on weekends."
    "!!"
    i "The next weekend is far from now..."
    m "Actually, Would you like to know a little secret?"
    i "A secret! What is it?"
    m "I'd tell you, But I'm kind of an info-broker of sorts, I've already spilt a bunch of beans on you..."
    i "(What does that mean, John?)"
    j "(It means she is selling that info for buck. Information really is valuable after all. Especially in this world...)"
    i "Then... how much is it?"
    m "I'll sell it to you for 3000 Zenny."
    j "Do we... have that much?"
    
    $ gameprogress+=1
    if Money >=3000:
        jump payMelissa
        
        
    else:
        i "We can't afford it..."
        j "Are we able to get that much over night?"
        i "Yeah, it should be easy enough, if I could just roam and bust some viruses!"
        j "Hurry up, then."
        $ gridpos = [192,164]
        call addsprites(gridpos)
        call mapcall([6,5],stage_ShadyAlley)
        if playerHP<=0:
            return
        $ILY_w = False
        hide screen mapB
        hide screen mapA

        return

label payMelissa:
        
        $ gameprogress+=1
        i"Should we give her 3000 Zenny? (We have [Money] Zenny left.)"
        menu:
            i"Should we give her 3000 Zenny?"
            "Yeah sure.":
                j "We still don't have enough."
                i"Stray viruses drop Zenny all the time when I beat them in Softwars."
                if Money < 3000:
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
                call addsprites(gridpos)
                call mapcall([6,5],stage_ShadyAlley)
                if playerHP<=0:
                    return
                $ILY_w = False
                hide screen mapB
                hide screen mapA

                return

label paidMelissa:
    $ map_active=False
    hide screen mapB
    scene scrollingBG at scroll
    show battleroad:
        yalign 1.0 xalign 0.5
    $ Melissa_w=True
    m "You got the 3K?"
    jump payMelissa
    label paidMelissa2:
    i "I got it! Here ya go!"
    $ Money-=3000
    
    m "Ah, Thanks. I may be your big sis, but hey, business never dies."
    j "(She's moneysmart, it looks like.)"
    m "There's a special item you can use to get past their detectors."
    "!!!... That sounds really convenient."
    i "What kind of item is it?"
    m "Hahaha.."
    i "You're... laughing?"
    m "Since you did pay me, I'll tell you. But I do find it funny that you wouldn't know about this."
    m "You're just like me, but you seem inexperienced. This is some basic fundamental stuff."
    i "Uguu..."
    m "Alright, Listen!"
    i "Yes!"
    m "The GRID we reside in is composed of a lot of things."
    m "Every entity is not merely built with values inside variables, or a collection of vertices on a 3D axis."
    m "We're made of Data Materials. Us Viruses, We are composed of virus cells, and tissues."
    m "Our composition allows us to utilize materials with special abilities."
    m "The special data material you want to find is called \"Imperceptium\"."
    i "Imperceptium! right!"
    m "Imperceptium is what Viruses use to stay hidden in the GRID!"
    i "Ah! That does sound like something I should have known."
    m "Imperceptium is hard to find as its surface projects a false image of its true appearance."
    m "Some like to say that it's in constant camouflage."
    m "Viruses can consume imperceptium to absorb that special trait, albeit for a limited time."
    i "If it's practically invisible.. How do we find something like that?"
    m "Stray wild viruses will drop them. But you can only see it once it's been seared in VirusFlame."
    i "Ah! VirusFlame?"
    m "VirusFlame. You know, every Virus is capable of using that technique. The one where you launch fire from the palm of your hands!"
    m "You really are behind in all this, aren't you?"
    i "Ah, i was just jogging my memory, Ahehehe!!"
    m ""
    j "ILY, what's stopping Melissa from making a run using Imperceptium?" 
    ""



label teammeeting:
    # "Now, if we could somehow get past Bitwulf and check out SDS tomorrow... All wil go smoothly."de
    "Now that I can see the viruses' perspective, I kind of want to just leave them alone at peace."
    #After this, John decides to review the day in his head and go to sleep.
    #TRANSITION TO MORNING
    #Morning

    #E-mail from Lisa appears
    i"John!! You have 1 new unread e-mail! It's Lisa!"
    # "Huh... Right. We were together yesterday..."
    "I wonder if it's true that her dad has a FAI Antivirus?"
    j"Please open it, ILY!"
    i"OK!"
    #(change to lnvl) for e-mail view
    #Show NVL window
    nvl show
    emailnvl"Subject: Update on Antivirus!"

    emailnvl"\n\nJohn!! I got my dad's Antivirus!!"
    emailnvl"Her name is Vira! From Vira Internet Solutions!"

    emailnvl"As I suspected, she was really a FAI Antivirus!"
    emailnvl"I'm going to your place today."
    emailnvl"We have to install her as soon as possible!"
    nvl hide


    "So it's true. What luck! So we do have a chance at saving our company from that Virus."
    "Vira Internet Solutions... Of course! Their brand is quite popular for their age."
    "A company of that caliber would know about something as secret as FAI Viruses. I didn't know they were working on AI as well!"
    "Are they simply making FAI to counteract the new Softwar system?"
    "Huh.. We have to install it, but why at my house?"
    "SDS is the one that needs it."
    "What am I gonna do?"
    "I should fix up the place!"
    i"John!! We're getting another new friend?"
    j"Well, yeah. But I don't think she'd be friends with you. You're a Virus, remember?"
    i"We wouldn't know until we try!!"

    #Hilbert arrives
    "Knock Knock!!"
    "Oh no, She's here already?"
    "I'm not ready yet! my room is still messy!!"
    i"There's someone on the door, John!"
    j"I can hear it, thank you!"
    "I set aside my broom and rush to the door."
    "???""Hello? anybody home?"
    "Eh?"
    "I take hold of the knob and open the door quite hastily."
    j"It's just Hilbert."
    h"Your pal, Hilbert!"
    h"I knew it! This is where you live!"
    "Hilbert suddenly appears as I open the door. "
    j"How'd you know?"
    h"Well of course! I'm a hacker!"
    "Hhmmmmm.. I don't think so."
    j"You snuck into my internship registration papers at SDS."
    h"N-no!!"
    "Right, it's his dad's company that I got Internship into, after all."
    j"You can't fool me!"
    h"Ehh!!"
    j"Why are you even here now?"
    "Lisa was supposed to come today, I don't have time to-"
    h"Straight to the questions already?"
    h"Aren't you gonna let me in first?"
    #John: "not enjoying this" face
    j"..."
    i"Who is it, John?"
    "Crap! Hilbert shouldn't see ILY! I should close the computer! He'd be so confused!"
    "Hilbert insists to get in, as I hold him out by the the door with a small opening gap."
    j"You stay right there."
    h"Is someone in there? I thought you lived alone."
    j"Nobody."
    "I shut the door before he can get to react."
    #Moving next to computer
    j"ILY, can you umm... be quiet for a sec?"
    i"I refuse."
    j"What?"
    h"Hey John?"
    
    h"Nice place you got here."
    j"HEY! Aren't you trespassing?"
    h"Come on, we're friends!"
    j"... How?"
    h"You left the door unlocked so I came in."
    "I really did?"
    "..."
    "Hilbert stares at my PC."
    h"A Virtual Streamer? I didn't know you were into that, John!"
    h"That's quite the impressive and cute avatar model!"
    i"I'm ILY! Nice to meet you!"
    
    h"Are you in a voice chat? Oh man I'm sorry to butt in, bro."
    j"Yeah. voice chat."
    i"This is not a voice chat."
    i"I am John's personal assistant AI. ILY!"
    j"No no no.. stop that. Don't introduce yourself!"
    h"Assistant AI?"
    h"That's super cool man! I thought you were friends with a V-streamer."
    j"No, it's not super cool."
    h"But like, she can talk, right?"
    "Hilbert moves closer to my computer."

    #Transition to ILY screen
    h "Hello there, I'm Hilbert, John's best friend!"
    i "Confirmed. You are indeed Hilbert, from John's contacts."
    j "I don't know about \"Best friend\"."
    h "Hey! She recognized my face!"
    j "Yeah, she's pretty high tech."
    h "Also, you ARE my best friend, because I'm your ONLY friend!"
    j "Wha, you don't know that for certain."
    h "It's true, at least at uni. I never see you with anyone else!"
    j "Stop giving me the creeps?"
    i "Oh, I see you are pretty close!"
    h "See, we're close friends at least!"
    # j"Umm, Hilbert, could you be a good visitor and-"
    "..."
    "Hilbert makes a nod, as if agreeing that this is normal now."
    h "I knew you were a genius when it comes to advanced tech."
    j "No, this isn't my AI."
    h "You didn't develop this?"
    j "No. I stopped working on my own AI some time ago."
    h "But you did work on AI! I knew it."
    j "It's an abandoned project now."
    h "That's kind of a waste. It's like we're living in a Sci-fi story with tech like that."
    j "Tell me about it.."
    h "Don't you think it's crazy, what's been going on at my Dad's company?"
    h "I bet some AI is involved with last night's events."
    j "!!!"
    "What does Hilbert know?"
    "I should ask him if he's heard of any clues about FAI. or the GRID."
    j ""

    #Lisa Arrives

    $ game_over=True
    return





label vscodered:
    "Now, Vira and Ily are together in the Hilbert's host computer."
    "I sent Ily over without Hilbert's knowledge,{w} He couldn't possibly be up all night right now,{w} waiting for the hacker."
    "I didn't tell him about the FAIs. but somehow, their company got Vira in there."
    "Hopefully this will go as planned!"
    v"Alert!! Threat has been detected!"
    i"John! Here it comes!!"
    return
