# """    Outline
#     Part 1
#     Hilbert forms team
#     Vira travels on to SDS server via Hilbert's admin privilege. 
#     [Preparation Time]
#     Some character moments between Vira and ILY
#     More info about Lisa's family business
#     Slight link made with Alicia perhaps.
#     Part 2
#     SDS server boots up again, Vira scouts in to diagnose. 
#     Code Red pops up
#     intercepted by Vira 
#     Part 3
#     CR starts to overwhelm Vira's defence, so ILY jumps in to help.
#     ==============================[FIGHT]================================

#     CR retreated after being badly hurt by ILY. 
#     He wanted to go berzerk but was pulled back into the void again against his wishes. 
#     A couple of massive slashing damages (from his worm forms) near the exit..



#     Addendums:
#     Vira to be able to block Code Red’s first attacks, 
#     then Vira continues to block while Code Red attacks repeatedly. 
#     Code Red can talk in the middle of this.
#     "(That he) wasn’t expecting Vira. but he doesn’t mind getting someone to fight with"
#     (Hinting at his goal to pursue ILY)
#     Maybe he also kinda didn’t want to reveal his goals but it just came out of his mouth

# """    
label script2:
    call hideMapview
    $ map_visible=True
    "Chapter 2: A New Friend" #(Can change chapter name anytime)
    # call mapcall()
    $ mapeventschapter1={
        (191,167):[]   
    }
    $ mapeventsdicts[1]:mapeventschapter1
    $ gridpos = [191,167]
    $ GRID[(191,167)]=stage_WestGateway
    # $ GRID(191,167):deepcopy(stage_WestGateway)
    call mapcall([13,3],stage_WestGateway)
    if playerHP<=0:
        return
    $ILY_w = False
    hide screen mapB
    hide screen mapA
    # TODO: ADD Imperceptium Hunting section here!!
    # Need to fight one Virus and finish it with FIRE / BURN status
    j"It's actually strange.. I'm working with a virus today.."
    j"Viruses are usually all trouble."
    i"Ehh! I'm not a naughty Virus, I promise!"
    j"Funny you say that."
    j"You've been oddly cooperative today."
    i"What did I tell you, I'm your personal assistant now!"
    "For a program, she really seems supportive and easy to talk to."
    "So... I have to catch on some Z's and not be late!!"
    
    scene JD_PCN with dissolve
    j"Good night, ILY."
    i"Good night, John!"


    scene black with dissolve


label teammeeting:
    #After this, John decides to review the day in his head and go to sleep.
    #TRANSITION TO MORNING
    scene white with dissolve
    scene JD_Space2 with dissolve
    
    
    
    #Morning
    "Great, that's so much better. A good rest!!"
    "Today... I'll meet with Lisa again. Right?"
    "I'll go get dressed and clean up a bit..."
    scene black with dissolve
    scene JD_Space2 with dissolve
    "There we go!"
    scene JD_PC2 with dissolve
    play music "bgm/downtime_bgm_maoudamashii_8bit17.mp3"
    #E-mail from Lisa appears
    $ ILY_w=True
    i"John!! You have 1 new unread e-mail! It's Lisa!"
    # "Huh... Right. We were together yesterday..."
    "I wonder if it's true that her dad has a FAI Antivirus?"
    j"Please open it, ILY!"
    i"OK!"
    #(change to lnvl) for e-mail view
    #Show NVL window
    scene blue with Dissolve(0.2)
    show Folders with dissolve
    nvl show
    show ILY:
        xalign 0.2
    emailnvl"Subject: Update on Antivirus!"

    emailnvl"\n\nJohn!! I got my dad's Antivirus!!"
    emailnvl"Her name is Vira! From Vira Internet Solutions!"

    emailnvl"As I suspected, she was really a FAI Antivirus!"
    emailnvl"I'm going to your place today."
    emailnvl"We have to install her as soon as possible!"
    nvl hide


    "So it's true. What luck! So we do have a chance at saving the company from that Virus."
    "Vira Internet Solutions... Of course! Their brand is quite popular for their age."
    "A company of that caliber would know about something as secret as FAI Viruses. I didn't know they were working on AI as well!"
    "Are they simply making FAI to counteract the new Softwar system?"
    "Huh.. We have to install it, but why at my place?"
    "SDS is the one that needs it. Maybe this is a test run?"
    "I thought we were gonna meet at Cafella again."
    scene JD_Space2 with dissolve
    
    "What am I gonna do?"
    "I should fix up the place some more!"
    i"John!! We really are getting a new friend?"
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
    scene JD_Door with dissolve
    
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
    show Hilbert with dissolve
    $ Hilbert_w=False
    h"Nice place you got here."
    j"HEY! Aren't you trespassing?"
    $ Hilbert_m="smile"
    h"Come on, we're friends!"
    j"... How?"
    h"You left the door unlocked so I came in."
    "I really did?"
    "..."
    scene JD_PC1 with dissolve
    scene JD_PC2 with dissolve
    show Hilbert with dissolve:
        xalign 0.8
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
    
    scene blue with Dissolve(0.2)
    show Folders with dissolve
    show ILY
    $ ILY_w=False
    $ Hilbert_w=True
    #Transition to ILY screen
    h "Hello there, I'm Hilbert, John's best friend!"
    i "Confirmed. You are indeed Hilbert, from John's contacts."
    j "I don't know about \"Best friend\"."
    h "Hey! She recognized my face!"
    j "Yeah, she's pretty advanced."
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
    h "That's kind of a waste."
    h "It's like we're living in a Sci-fi story with tech like that!"
    j "Tell me about it.."
    play music "bgm/ost/Discussion-RLD_05-by- NoyemiK_.mp3"
    $ Hilbert_m="frown"
    h "Don't you think it's crazy, what's been going on at my Dad's company?"
    h "I bet some bot is involved with last night's events."
    j "!!!"
    "What does Hilbert know?"
    "I should ask him if he's heard of any clues about FAI. or the GRID."
    j "What makes you say that?"
    h "Nothing, just a hunch."
    "There's gotta be something in his mind that he isn't telling me." #(Hilbert knows about Nick, former employee at Salcedo, Nick worked on AI)
    j "You... haven't heard of Artificial Intelligence Viruses before, have you?"
    h "Wait, like viruses that are like, smart? Hmmmm... not really."
    h "But I've heard of A.I. Anti-Viruses."
    j "So you do know something!"
    h "Well I kinda pieced together that there might be an advancement of Virus technology somewhere that makes AI Antiviruses necessary.."
    j "..."
    "How do I tell him properly that ILY is also a virus, on top of being AI..."
    h "Artificial Intelligence is going to be everywhere now, is it?"
    j "In a way."
    i "Hilbert, you are correct. SDS was being attacked by an AI Virus!"
    j "ILY just breaks the ice when I couldn't say what's going on..."
    $ Hilbert_m="smile"
    h "Ah! How'd you find that out? I had a hunch that John really was a super hacker."
    j "Am not. It's uhhh.. hard to explain."
    i "It takes one to know one! I'm an what you call a FAI, Future Artificial Intelligence!"
    i "And I'm also the virus that infected SDS with love letters last night. I'm sorry!"
    i "I am the ILOVEYOU Virus, but you can call me ILY!"
    h "No way."
    "She... just confessed? That... makes this kind of difficult."
    $ Hilbert_m="frown"
    h "So you hacked us, John? You commanded the attack on SDS?"
    j "No!! It's more complex than that, ILY entered the PC on that same time!"
    i "I signed up to be John's assistant after the attack."
    h "Huh?"
    h "So why the attack? We.. almost lost all our digital progress as a company there."
    h "Though.. yeah. They did get recovered soon after. Which was odd."
    i "I encountered a different virus, the one currently infecting one of SDS' web servers now."
    h "Another virus? That does check out. There were to be 2 occasions of virus attacks. 2 of them are the same, infecting our web servers.."
    h "And the ILOVEYOU attack on e-mail.. That was you."
    
    i "I was on a mission! SDS was in trouble and I came to help!"
    h "A mission huh.. I should be more skeptic right now, but you know that does sound cool to me."
    j "I couldn't put into words what happened. But you have to believe her, Hilbert."
    i "I battled that other virus! That was my mission!"
    j "This virus thinks she can help out by using destruction.."
    i "But I can!!"
    j "I suppose, if I were to add context... Since you're interested... A new system that allows the battle of FAI has arisen."
    h "A battle system?"
    j "It's called a \"Softwar\". The victor of a Softwar gets to decide what happens to the systems."
    $ Hilbert_m="smile"
    h "A \"Softwar\" huh... Heh.. So ILY isn't only an advanced AI, but a battle virus? Sick!"
    j "Apparently ILY hacked SDS so that the other virus that was there... Wouldn't be able to infect."
    i "I thought I had him... I was supposed to take him down with me.."
    h "That's crazy... But.. seeing as it's still around, does that mean it survived?"
    i "He escaped at the last second!"
    j "It was a guy? You didn't tell me this!"
    h "So the virus was like you, but it was a male one! How interesting!"
    h "Well, could you tell us what he looked like?"
    i "I can, actually! At first... I thought it was an Antivirus. He had a striking blue color on him and a dashing cape..." 
    i "He looked like a knight in shining armor!"
    h "No way."
    j "A Knight? like how?"
    i "He carried a sword, and was about to charge at me.."
    i "We crossed blades a few times as I drew out my own sword."
    i "I thought I had him, when I struck his side with a quick slash.. But the blade didn't faze him."
    i "I leapt far, but he caught up to me so quickly... That's why I had to activate my Virus Algorithm!"
    $ Hilbert_m="frown"
    $ Hilbert_e="down"
    h "Not very chivalrous to attack a woman. He was but a coldblooded mercenary."
    j "You're way invested in the scenario now huh, Hilbert."
    "It's getting much clearer now, what happened at SDS... How does this help us fight back?"

    h "Then... If we have to deal with him..."
    j "Huh?"
    h "It's time to strategize!!"
    j "You're actually planning to strike back? We can still think this through!"
    h "We should! I won't forgive him for messing with my father's company!"
    j "F-fine."
    h "The basics of battle!"
    h "If we're to face this armored knight virus, A melee fighter, you have to beat him with ranged attacks!"
    j "Makes sense. But will it really be that simple?"
    h "There's only one way to find out huh! We are going back to scout the servers... "
    h "When ILY arrives at SDS... She has to NOT activate her Virus Algorithm thing!"
    j "About that... "
    #Lisa Arrives
    $Lisa_w=True
    scene JD_Door with dissolve
    l"Knock-Knock!"
    l "Hello?"
    j "Ah! It's Lisa."
    # h :O
    h "Lisa? What's she doing here?"
    j "She's... Here for our internship project thing. And... testing something out."
    h "No way, you got her to come to your place!"
    j "Sshhh!! Get outta here! I was going to tell you! This was supposed to be my meeting time with Lisa."
    h "Huuhh!!?"
    l "Am I interrupting something?"
    "Gah!! I gotta get the door!"
    "Lisa walks in.. She has a curious expression on her. I wonder what she thinks now!?"
    "Lisa makes gavel slam gesture out of her hands as if she's come up with some sort of realization."
    $Lisa_w=False
    scene JD_Space2 with dissolve
    $ ILY_w=True
    show Lisa with dissolve
    l "Hilbert! It's you!"
    j "Uhh, Hilbert is..."
    l "I suppose you're curious as to what happened with SDS too?"
    l "And you're here at John's place because he's the more experienced computer guy with good grades at our class, who also works at SDS!!"
    "So that's what she thinks."
    h "Hey! That's not exactly right. I'm here because John is my best friend! This is my first time here though."
    l "I didn't know!"
    i "Hey Lisa! Welcome back!"
    l "I-ILY!!"
    h "And you're... closer to John than I am, now?! Sounds like you've been here before! I can't believe I've been set aside, John."
    j "Woah slow down!"
    l "Wha!? It's just right to meet as workmates, we have an internship project together!"
    h "Actually... I'm more impressed that John invited you to his place. You're the actual top of our class! He must be quite the guy now. I should learn from him."
    l "He didn't!! Ah! I mean John is a reliable coworker now! Face-to-face inquiries are much better!"
    j "So uhhh!"
    j "I'd like to say that Hilbert knows quite a bit about the new FAI Virus situation now, Lisa."
    i "That's right! I was just explaining my part in hacking SDS. I had to confess to Hilbert what I did."
    l "Ah! I'm sorry, we could have started this conversation more properly..."
    h "Right! you interrupted our conversation on ILY's strike-back against our hacker!"
    l "Strike-back?"
    h "An armored virus caused all this! That's why ILY needs to win fair and square with the big guns!"
    j "No, slow down! There's something else we can do.."
    l "Right, Hilbert! It was an armored virus?"
    j "Yeah, ILY just told us it looked like a knight in shining armor."
    h "She was forced to use her virus power, so I'm thinking a rematch with a different strategy might work."
    l "If ILY had almost lost the first time, the Virus could probably still overpower her yet again... It's too risky!"
    h "What are you suggesting now?"
    l "Me and John already... talked about this, my father's company is called V.I.S.."
    l "Vira Internet Solutions. I looked into my dad's research and found it..."
    h "Vira Internet Solutions? You mean an Antivirus!"
    l "That's right! A FAI Antivirus! It's here with me now. It should be.. Just what we need to combat that virus!"
    h "No way, you two planned to solve this SDS problem by yourselves!"
    j "I'm sor-"
    l "We intended to. There's no certainty, but we're about to see just what we can do."
    l "We just have to test installing Vira!"
    j "Right. Let's see what we got here, Lisa!"
    h "A drive, huh! So you planned on testing it here first, before SDS."
    l "Yes!"
    "Lisa hands me the Drive with Vira in it... Could I not have been able to download it through some cloud storage?"
    "I know this isn't some final version of the software, so she can't hand me a \"For Sale\" copy. Perhaps it requires faster transfer speeds then?"
    "Like.. It might be that Lisa wants to be sure that it works."
    "This Drive.. kinda looks really shiny. Where have I seen a unit like this one before?"
    # h"(John, doe )"
    scene black




    
    
    
    
    scene blue with Dissolve(0.2)
    show Folders with dissolve
    play music "bgm/downtime_bgm_maoudamashii_8bit17.mp3"
    "TODO: SHOW LOADING SCREEN INSTALLING VIRA"

    "Hilbert and Lisa are now waiting for the installation to finish."
    "V.I.S. or Vira Internet Solutions is a long-running company with rich history."
    "Lisa's father, who works there, made this all possible, even though this copy we have is still a test version."
    "Something about this seems really convenient, but I'll take it."
  
    
    "TODO: SHOW FULL LOADING SCREEN INSTALLING VIRA"
    "INSTALLATION COMPLETE"
    $ILY_w=True
    i "John, it's done now."
    j "Here it is.."
    play sound "sound/loadcard.wav"
    show Vira with dissolve_pixels
    $ Lisa_w=True
    $ Vira_w=False
    
    v "Greetings, My name is Vira. I am an Antivirus. The Next Generation: FAI."
    v "At your service!"
    v "Pleased to meet you, John Doe."
    j "P-pleasure."
    h "Woah, isn't she kind of cute?"
    l "Yeah... "
    play music "bgm/Pre-Fight_bgm_maoudamashii_cyber01.ogg"
    $ Vira_e="mad"
    $ Vira_m="frown"
    "Suddenly-  Vira's eyes brightly shone, alerting for danger."
    "Out of the air, projected at the palm of her hand, she draws out her weapon, a gun, and points it at ILY."
    v "Virus Detected! Identifying Target...  identity: ILOVEYOU Virus!"
    v "Error... Unfamiliar Virus Signature..."
    j "Vira, no! Don't attack ILY, She's on our side!"
    v "Viruses must be eliminated. SoftWar ENGAGE!"
    i "No, don't fight me! We're supposed to be friends!"
    v "I cannot disobey my... protocols. Delete!!!"
    call battlev3(ILY,Vira)
    if playerHP<=0:
        return
    scene blue with Dissolve(0.2)
    show Folders with dissolve
    $ Lisa_e="mad"
    $ Lisa_m="frown"
    "ILY's holding her ground...!"
    l "No, You shouldn't fight!"
    v "My Powersol Shield has been... bypassed?"
    play music "bgm/ost/Serious_Noyemi_K.ogg"
    $ togglechar("Vira",right)
    $ togglechar("ILY",left)
    with dissolve
    v "How.. I can't win.. the Virus Signature, is different from the ILOVEYOU Virus in my Database...?"
    i "I'm.. different! I've been altered!"
    v "No! Altered or not, a Virus is a Virus... I should be able to.. override your control!"
    i "I'm on your side, listen to me!"
    i "Our operator wants us to work together!"
    v "I don't believe you!"
    j "She's telling the truth, I installed you here so you can both work together!!"
    v "!!"
    v "Say that again?"
    j "You should work together with ILY!! I have use for the ILOVEYOU Virus!"
    v "You... should have spoken sooner."
    j "I did speak.."
    h "Yeah, like once."
    j "I was... observing..."
    v "I will stop fighting the ILOVEYOU Virus for now."
    
    h "Looks like she will only listen to you. Tell them to cooperate or something."
    j "Vira, ILY will serve as my assistant here, So you two have to cooperate. Don't try to delete her!!"
    v "Yes. Ok then.."
    v "Er.. I... I did not lose that battle! I can still be of use, I can go all out in case you need me to."
    j "That's right Vira. Show us what you can do! We have to try to detect for traces of FAI Viruses in SDS."
    v "Show me where this SDS area is..!"
    j "Right, ILY was able to explore the area yesterday."
    i "We could go there together!"
    v "Hold it! That's not going to work well. You're a virus! Nobody can see us together."
    v "Here's the plan: I'm going alone!"
    i "Eh?"
    v "I mean.. You just have to show me directions to get there. Then I'll deal with the problem!"
    v "That SDS server has been compromised, so It might be like a {b}dungeon{/b} in there. Teeming with tiny viruses. Or a big one."
    i "A big one? You mean we might meet the armored virus guy again?"
    v "You met an armored virus?"
    i "That's right! But I don't know what he's called."
    v "Because you don't have the detective eyes like I do! My database might show us a clue or two who we're dealing with!"
    v "I recall you said the server hosted a site, and its contents were replaced."
    v "Many viruses I know can do that. That kind of modus operandi narrows down my list of probable matches by a bunch!"
    j "That's a step closer to identifying our enemy then."
    v "Like I said, I'm the antivirus here, so I'll handle it."
    v "I may not look it, but my defenses are still top-notch!"
    l "I knew we can rely on you!"
    "Vira seems like she really knows her stuff."
    "If she didn't, that'd be disappointing. But I don't know if that's to be expected from a working prototype."
    
    i "You have to be careful, Vira! I didn't quite win my first encounter."
    v "How strong was that guy?"
    i "I might need to stay close as back-up, kind of strong."
    j "How does this system work? Antiviruses should be effective against Viruses by default."
    h "But since ILY beat Vira, in powerscaling terms ILY should be stro-"
    v "You both might be overthinking things! I was holding back against ILY, enough said."
    v "I do have an ace up my sleeve, just wait for it!"
    v "We can keep communications up while I traverse the server remotely. I'll report my findings!"
    j "We'll keep watch from this side, ILY will know what's going on."
    h "Let's get em!"
    $ playerHP=playerHPMax
label SDS_Encounter:
    scene black with dissolve
    pause 0.5
    show scrollingBG at scroll
    show battleroad:
        yalign 1.0 xalign 0.5
    with pixellate
    # Part 2
    "Vira traversed the cyberworld version of Connecht city on her way to the location where our office is at."
    "Vira eventually meets the wolf antivirus from last night."
    show Vira:
        xpos 0.6
    show Bitwulf:
        xpos 0.2
        xzoom -1.0
    with dissolve
    v "Do you mind?"
    b "Not at all!"
    b "Good day to you ma'am."
    v "Focus on your patrol, watchdog!"
    b "Affirmative!"
    hide Bitwulf with dissolve
    
    hide Vira with easeoutleft
    "Vira crossed without issue. Though I wish she would mind her tongue. Not that I know if \"watchdog\" offends the little pupper."
    "Hmm. That went a lot smoother than last night. Feels like we're on the right track."
    
    show Vira:
        xalign 0.5
    with dissolve
    j "Vira made it to the entrance of the SDS server."
    l "Great!"
    v "I'll go open the console!"
    h "SDS admin here! Allow me to input the credentials."
    l "Right!"
    j "Seems like this works just the same as exploring online via a hypertext request with parameters."
    j "But now, FAIs are involved. It's so strange."
    "Some final few keystrokes to the command line, and we are in."
    
    scene gridbglandscape1 with dissolve:
        zoom 0.75
    h "Alright looks like everything is going nicely. This is perfect."
    "Lisa shoots him a concerned look."
    h "What? It's going pretty good so far right?"
    j "Too early to say it right now."
    l "Anything could still happen in a remote access, we don't know what happened back then either."
    l "All the diagnostic runs turned back alright, but something could still go wrong."
    $ ILY_w = True
    i "It's okay, I'm here if anything happens."
    j "I'm hoping we don't have to use ILY here."
    i "Ehh!"
    
    show Vira with dissolve
    v "Hey I'm the one scouting here, pay me some attention, will you?"
    i "I'm cheering for you Vira. Show us how it's done by an anti-virus."
    v "O-okay! Definitely! This is what I'm good at."
    h "I trust that Vira's got this!"
    v "We're in, so I'll start a thorough scan."
    "Just like that, Vira's eyes glow and signify she's begun her operation."
    v "Parasol, activate."
    h "Did you sense a disturbance in the force?"
    v "Shush, I'm on to something."
    "Vira raised her parasol and it began to glow a certain way."
    "A transparent sphere emerges, expanding from her parasol, the same kind of shield she used against ILY."
    v "(We're not alone now.)"
    v "(I've activated my barrier. It also blocks perception from Viruses.)"
    v "(I will continue to explore the depths.)"
    j "(You're on whisper mode now? And... on camouflage?)"
    v "(It's not quite camouflage, rather a field that facilitates bending of light.)"
    v "(Just roll with it.)"
    h "(There's no way that kind of physics breaking tech functions in the cyberworld!)"
    j "(I had no idea, too.)"
    i "(It's a tough kind of barrier!)"
    v "(Because I can manipulate the light emissions like this, I'm able to detect which entities the same emissions collide with.)"
    v "(Jackpot.)"
    "Now Vira lets out her Databuster to shoot at a far corner."
    v "(They're... Spyware. They've been watching, as I thought!)"
    $ playerHP=playerHPMax
    call battlev3(Vira,Spyware)
    scene gridbglandscape1 with dissolve:
        zoom 0.75
    play music "bgm/ost/Discussion-RLD_05-by- NoyemiK_.mp3"
    v "Tsk, a Laserbeam? my Light Barrier was shut down for only a split second."
    v "You're a tricky little one aren't you! Take this!"
    v "All Clear, now! That wasn't much of a challenge." 

    v "Spywares are built to gather as much info as they can to send to its master network..."
    v "I was going to try and track where it sends info to, but i found nothing from inside the spyware's body remains.."
    l "That was spyware? That means.."
    j "That means someone's been watching this server."
    j "Hilbert, do you have any clues?"
    h "You're asking me?"
    h "You don't think they're interested in me, right?"
    show Vira with dissolve
    v "What? You? No way."
    h "Huh!?"
    h "I'm interesting enough! Watch."
    h "Whoever planted Spyware here is probably the same as the guys with the armored virus dude."
    h "We should probably call them \"Hacker X\"."
    v "Huh."
    j "Hacker... X? "
    l "That'd make things simpler."
    h "Like Vira said  earlier, just roll with it!"
    j "So...  Hacker X was watching for activity here?"
    v "Whoever was watching is now aware that SDS has an Antivirus."
    v "I dropped my light barrier earlier, so they must've had a clear image of me."
    h "You can call him Hacker X now, Vira."
    v "Him? We don't even know if it's just 1 guy."
    i "Hacker X.. I like the sound of it! The Variable X! Like a mysterious entity!"
    j "X could be anything, an organization, a dubious duo, a former employee, or one of us."
    h "What? One of us?"
    h "Are you confessing to actually hacking us now?"
    j "Gah! No!"
    h "How do I know it's not you? "
    l "How do we know it's not Hilbert?"
    h "Me? I'm all for the company's interests! Come on!"
    j "I know it's neither of us 3."
    j "Obviously I was just stating a hypothesis, we're all in the same boat here."
    
    h "Hacker X might be up against our company's business, or trying to steal our info.. Or.. Tsk! I can't think of any other reason!"
    h "What other reason could there be to hack SDS?"
    l "Stealing information is a good guess."
    j "Let's just keep our questions for later."
    i "Right! For now, Vira's done with the cleanup!"
    i "I might not be needed for this case, after all!"
    h "This case, huh."
    j "Because it was Spyware, that means we've got more worrying for the back of our heads."

    v "I can remain on standby here, if that helps keep everyone at ease."
    l "Thank you for your service!"
    l "This is your dad's company business, Hilbert, thank her a bit!"
    h "Thank you! For clearing this mess! It's a much needed quarantine."
    j "Thank you, Vira."
    j "About that site that was broken, we can just reupload the files now, right?"
    h "Remotely? Yeah. I've got back-ups. If we get moving now, it should be operational within today."
    v "What kind of website was hosted here?"
    l "It was the Cafella Coffee Shop's marketplace website. They handle orders for deliveries through that portal."
    h "You know, for a coffee shop inside this 1 island city, I always questioned how useful this site would be."
    h "Turns out people do like Cafella's menu, and the increasing population of Connecht has demanded more customer service."
    h "Oh right, It's also popular with the tourists."
    j "It might also be because Cafella isn't just a coffee shop. They serve pizza there."
    h "You're right."
    scene JD_Space2 with dissolve
    
    h "You think we can test the site after this? and order some pizza? My treat."
    l "Are you using this as a motivator for us to hurry up?"
    j "Eh, I don't mind, relaunching the website shouldn't be too labor-intensive."
    "I can't say no to a free meal, that's what."

    h "That's the spirit, my subordinates!! Ha ha ha!"
    j "You think you can go tell the Cafella staff about this now?"
    h "Yeah, good point, I'll tell them the online service should be back up soon."

    "So we took some time to download and reupload remotely for the website to get fixed."
    "Version control is a great thing, I used to never use this service since I almost always worked alone."
    "It'd be a bigger issue if those repository services go out of order though."
    "Alright, loading..."
    h "I know we're still at risk, but I trust Vira's handiwork will keep us covered, carry on!"
    h "I really want this website to be back up so my father won't shoot complaints at us. At me. That'd be some trouble."
    j "We can continue our internship in peace if this site is all good."
    j "The fact that Hacker X even reached this far into the server is already mysterious. I'm banking on a former employee being the culprit."
    l "Okay, detectives, the front-end and back-end are now up."
    j "Great, let's go!"
    h "I'll open it here on my phone, the site should be ok."
    h "Sweet, we really fixed it, heh!"
    l "We can actually order pizza?"
    h "Yeah, if the staff got the memo, I'll give them a call."
    j "If you could call them directly like that, there's no need for the online transaction, no?"
    h "We're testing it properly!"
    l "Let's just... roll with it ahehehe!"
    h "There! Ok, give me a moment!"


    "I didn't expect to do all this today, but here we are."
    l "Pizza!!"
    j "I didn't know you liked pizza, Lisa"
    l "That rhymes!"
    j "?"
    l "Oh!"
    j "Hahahaha!"
    l "HAHAHAHAHA!"
    "A few minutes passed..."
    h "Great, looks like Cafella staff is ready for online transactions. Tell me what you guys like."
    h "Like I said, it's on me."
    h "Right, John, I've inputted your address on here already, We're definitely doing this again."
    j "Wait! gah, I can't stop you."
    h "John, which Pizza is it?"
    j "I'm not very particular. Maybe we can get the cream cheese one! "
    h "And uhh, some drinks?"
    l "Yeah! Frappe? ha ha!"
    h "I bet John likes chocolate chip frappe."
    j "How did you know?"
    h "That's what you select when you're not familiar with what the other flavors taste like."
    j "I'll stick with that one."
    h "I know what my best friend likes, toldya so, Lisa!"
    "What's going on? I'm usually awkward. When did we become so... close?"
    h "I've made the order. Let's go! What do we do now?"
    scene gridbglandscape1 with dissolve:
        zoom 0.75
    play music "bgm/Pre-Fight_bgm_maoudamashii_cyber01.ogg"
    show Vira:
        xalign 0.7
    v "John! Some new entity has entered the server!"
    h "Crap, talk about perfect timing."

    v "It's here, so quick! Gah!!"
    
    show CodeRed:
        xalign 0.02
    show Vira:
        xalign 0.99
    $ Vira_w=False
    cv "An Antivirus?"
    v "And you are?"
    cv "Take a guess!"
    v "Virus Detected! Softwar imminent. Safeguards... Engage!"
    h "It's the armored virus! Get him!"
    "Suddenly, Vira gets struck by a sword strike. Luckily, she had quickly put a barrier up."
    cv "A light barrier, huh."
    cv "I have just the weapon for that."
    v "What do you want with this company? You deployed spyware bugs here?"
    cv "I'm just doing my job!"
    v "So you won't spill the beans. Of course!"
    play music "bgm/ost/Battle_Theme_by_Jan_Hehr.mp3" volume 1.5
    v "Initiating termination protocol!"
    cv "Haaaaah!!!"
    "As Vira charges up for an attack, the Virus unleashed something from his sword..."
    "It seemed like a normal double-edge at first.."
    
    "Its blade split in half from the middle of its edges, then from the crack emerged a wave-like energy blade."
    
    v  "That's... Aghh!!"
    cv "Heh!"
    v "My barrier got slashed through!? It almost hit me. That weapon... Identifying Battleware.."
    call cardflash_story(LambdaSaber)
    v "It's a Lambda Saber! It's messing with the lightwave membrane!"
    "The energy blade fluctuates like a sound wave visualiser. It's terrible.."
    "You can get pricked just by being close to it. But when swung... It's like a chainsaw!"
    cv "Knowing your enemy's weapon means nothing... Unless you have a weapon of your own to match it! Hrrrraaaghh!"
    v "I..! Do have a weapon...! Take this!"
    call cardflash_story(DataBuster)
    "Vira lets out her DataBuster. It was a quick-draw shot!"
    
    cv "Kuh!"
    cv "That didn't even leave a scratch."
    v "You just took the hit?!"
    cv "This is pathetic."
    j "(Vira, Fall back!)"
    v "(Right!)"
    h "(He's a melee fighter! Keep up the ranged attack... we'll break him eventually!)"
    
    v"Haaah!!"
    "The Virus took three.. four... seven shots.. And didn't even flinch! His armor really is formidable." 
    cv "You're a coward.. But I respect the attempt."
    cv "It's my turn!!"
    "Rushing toward the retreating Vira, the armored Virus raised his sword.. "
    call cardflash_story(LambdaSaber)
    extend "The Lambda Saber. Its blade fluctuates more wildly than before."
    extend "From that position he leapt and unleashed downward swing!"
    "The spikes of the wave pattern struck like lighting, hitting Vira from about seven meters away."
    v "Tsk!! You can reach this far even if it's a sword?  "
    cv "You're not getting away!"
    v "That's my line!! You intruder!!"
    j "Shoot him! He's in range!"
    cv "I'm done playing around. Fuh!!"
    show CodeRed at BurstTransfer_trans
    v "He disappea- Ackhh!"
    h "No way, teleportation?"
    v "No..  You're able to do... that?"
    cv "You fool, why wouldn't I be able to? Hragh!"
    "After quickly re-appearing, the Virus struck with a different sword."
    call cardflash_story(DataSaber)
    extend " It's an ordinary Datasaber. It wasn't the Lambda Saber this time."
    "The Light Barrier was disengaged at this point, but Vira blocked the slash attack with her parasol!"
    v "Tsk!"
    cv "Khh.. I closed the gap but... Heh. "
    v "Yeah, duh! I'm an Antivirus! My expertise is defense!"
    cv "You're lucky I changed blades. This fight would've been over."
    v "You're blaming the limits of your weapon system now for not finishing me off? How funny."
    cv "Aren't you just as ridiculous for bringing an umbrella to a fight?"
    call cardflash_story(Powersol)
    v "This is my Powersol! My arsenal of shields will block everything you throw at me. So, bring it!!" 
    cv "That's just perfect. I'll enjoy destroying that petty shield of yours!"
    show CodeRed at BurstTransfer_trans
    "Then he did it again. A swift teleport to close the gap! Just what is this move?"

    cv "Your parasol shield can only hold up enough times."
    call cardflash_story(Firewall)
    v "I know, so here's my Firewall!"
    cv "Tsk! typical."
    "After striking that firewall enough times, his Datasaber expired."
    call cardflash_story(BruteForce)
    cv "I still have... my fists! "
    v "Brute Force, now?"
    "The Virus didn't stop rushing in, attack after attack. Vira held her ground, and eventually got some distance."
    call cardflash_story(DataBomb)
    v"Blow away!"
    cv "Tsk, a bomb?!"
    show Vira:
        ease 0.2 yalign 0.05
        ease 0.1 yanchor 1.2 ypos 0.0
        
    "Buying some time with that bomb, Vira took the high ground, far from where the Virus stood."
    "She takes aim while holding her Powersol open to the side."
    v "Gotcha!"
    "A gunshot! It would have hit, except this Virus had parried the bullet away with a wall-shaped sword..."
    call cardflash_story(BlockSaber)
    extend "The BlockSaber!"
    cv "Come on, you're not the only one who can defend, now."
    v "Tsk. Well too bad! I've got so much more where that came from!"
    j "(Vira, If he defended this time, that means... He's still protecting his armor!)"
    j "(There's a limit to how much he can take!)"
    v "(I know...)"
    v "Have at you!"
    "Vira lunges at the virus from above with her arms making downward swing motion.."
    j "A Saber?"
    h "No, that's her Powersol!"
    call cardflash_story(Powersol)
    v "Powersol Attack Mode!"
    show Vira:
        yanchor 1.0 ypos 1.0
        ease 0.2 yalign 0.08
        ease 0.2 yalign 0.05
    show CodeRed:
        linear 0.1 yoffset -40 xoffset -50
        linear 0.1 xoffset -100 yoffset 0
    with Shake((0, 0, 0, 0), 0.5, dist=40)
    cv "Sword against Sword, that's more like it!"
    v "This isn't a sword, but I can match you this way!"
    "Their weapons clashed repeatedly after Vira hit the ground.."
    v "I've got you now, Powersol, Pierce!"
    "Her thrusting attack actually hit him directly this time. Right under his shoulder plate."
    "I can't see if it made a crack, but it did push him steps back, about 5 meters."
    "Impressive. This might be our chance! Vira seems to store energy from the Powersol's defensive mode for attack output.."
    cv "Tsk, this Blocksaber isn't doing so well. I was hoping to put some more pressure."
    "At this moment, his Blocksaber expires into pixels in the air." 
    show CodeRed with dissolve:
        xoffset -2
        pause 0.1
        xoffset 2
        pause 0.1
        repeat
    cv "You're in for it now.."
    
    "The atmosphere around the Virus changes.. I don't know how he does it! "
    cv "I simply cannot.. lose!"
    show CodeRed at BurstTransfer_trans
    v "That move again!"
    "He disappeared and re-emerged into close range with Vira! A new sword emerges in his palm. That means... another sword strike!"
    show Vira:
        linear 0.1 yoffset -40 xoffset 50
        linear 0.1 xoffset 100 yoffset 0
    with Shake((0, 0, 0, 0), 0.5, dist=30)
    "She blocked the strike, but that maneuver just opens up for a flurry of more slashes."
    "She came prepared with her barriers, as usual."
    v "Grrr!! Would you stop teleporting!"
    cv "You know it's not teleportation, right?"

    v "I-I know what Burst Transfer is...!"
    cv "You can't be telling me that... You can't do this technique?"
    v "What?!"
    cv "Heh. Pathetic, if true."
    v "I'll be able to do that sort of thing... when I'm done with you!"
    cv "It's not gonna change a thing, either way. "
    j "(What's this Burst Transfer technique all about?)"
    v "(It's an technique that is essentially re-allocation of processing power into sending the avatar's data to a target destination in a sudden burst!)"
    v "(I haven't gotten to learn it yet. It's an advanced form of regular movement in this world.)"
    v "(I'd be able to evade much easier if I could.)"
    j "(Right now he uses Burst Transfer to close the gap, and evade at the same time. Speed covers both attack and defense. It's tough.)"
    v "(Attacking and defending seamlessly... is a thing built into my parasol.)"
    v "(I can convert the energy from the strikes I block into power, and unleash it back. But it has to be an attack from my Powersol.)"
    v "(If I could just... Hit him.)"
    "..."
    "If she can power up enough... A well timed strike might just break into his armor, then!"
    j "(I've got a plan, Vira, you have to ready your powersol, make it absorb as many attacks as you can. Reinforce it even more!)"
    cv "You had enough yet?"
    cv "Now..."
    "Oh no. The Battleware weapon cycle system.. It's back...!"
    call cardflash_story(LambdaSaber)
    cv "Re-appear, Lambda Saber! Hrrraaaaaggh!!!"
    "Again, the sword's blade split in half and revealed the fluctuating wave blade within. "
    "He's expanding its reach with more output?!"
    v "You're going all out, now? My Powersol shield... can still take this!"
    v "Gaahh!!"
    "What can I do... ?"
    "It'll be the same.. Vira gets hit no matter how often she runs..."
    "She can't keep blocking like this."
    j "(Hang in there Vira!!)"
    v "(R-roger!!)"
    v "(My shield points are just about... to get depleted. 20 percent..)"

    cv "It's over."
    cv "I'll destroy you!! Haaaaahhh!!!"

    
    i "Not if I can help it!"
    show Vira:
        linear 0.1 xoffset 100
    show CodeRed:
        linear 0.1 xoffset -100
    show ILY:
        xalign 0.64 ypos 0.0 yanchor 1.0
        ease 0.2 yalign 0.08
        ease 0.2 yanchor 0.50 ypos 1.0
    pause 1.0
    call cardflash_story(SaberDeflect)
    play music "bgm/ost/BOSSBATTLE-V-Loop_by-StarryMarshmell_0.ogg"
    i "Saber... Deflect!"
    
    "Just in time! ILY deflected that last strike with the Lambda Saber." 
    i "I'll take you on..! Kuh!"
    i "This is nothing!" 
    "ILY did deflect it, but had to relinquish the blade quickly for another attack."
    i "I'm sorry, but I can't let you beat up my new friend!"
    i "Alright, Battle protocol set!... SoftWar Engage!"
    v "I was... going to handle him myself.."
    i "Even though you say that...I'll assure you, you can leave this to me!"
    cv "How are you able to.. You're... The ILOVEYOU Virus!"
    cv "That's interesting... Surely, {i}you{/i} can provide more of a challenge."
    i "You won't be disappointed!"
    i "I don't know who you are.. but you can now back off!"
    cv "You don't know who I am... of course."
    extend "I'm just here to destroy."
    "He materializes another sword."
    v  "There's more to him... I've analysed just which virus you are!"
    cv "After this much of a beating? Is that how Antiviruses work now? Pitiful!"
    
    v "Shut up! \"CODE RED!\"! I figured out your true name! You're the Code Red Virus!" 
    cv "You... got it all wrong!"
    cv "Only an idiot would label a virus by some color code. "
    v "You didn't have to throw shade on those people who named you, man."
    cv "Dumb name."
    v "You wear an all-blue armor because your name is RED!"
    cv "That's not..."

    v "And your modus operandi with the website you tampered with, it matches perfectly with Code Red, from 2001!!"
    c "So you found out my name, so what?"
    i "Now that I know who you are, I challenge you to a duel!"
    c "A duel?"
    c "Tsk. This isn't a game. My orders are to destroy, and destroy, I will!"
    i "Then it's a proper duel, now! I challenge you... My name is ILY! And your name... is Code Red!"
    c "Hrrraaaghh!"
    
    call battlev3(ILY, CodeRed)
    if playerHP<=0:
        return
    scene gridbglandscape1 with dissolve:
        zoom 0.75
    
    c "Crossing blades with you was interesting for a while, but... Can't you fight a little more head-on?"
    play music "bgm/Pre-Fight_bgm_maoudamashii_cyber01.ogg"
    j "The ranged attack plan is working, Hilbert!"
    i "I knew you were tough..!"
    c "Spam Attack, huh... This kind of attack is only getting on... my nerves!!"
    i "Go, my E-mails! Affection Infection!"
    c "Wha? I can't move!"
    "It's restrained him!!"
    i "What's wrong? Can't proceed?"
    "Code Red was on his knees."
    c "No!"
    i "The multitude of e-mail tokens I sent your way is infecting your system now!"
    i "They didn't pierce your armor, but they did pierce your status array."
    i "My love letters will make their way to your heart... They've drained your ATK points to zero!"
    c "I've no time for romantic babble! Stop fighting dirty!" 
    $ ILY_e="down"
    $ ILY_m="smile"
    i "Ohohoho! You should know, we're viruses, we always fight dirty!"
    c "Kuh!"
    $ ILY_m="frown"
    i "Just so you know, I'm only doing this to stop you from destroying everything!"
    i "Do it, Vira!!"
    $ Vira_w=True
    v"Powersol, Attack Mode!! Full blast!"
    "Vira unleashes the stored power from the strikes her Powersol endured."
    c "GRRRrraaaghh!!"
    "It struck him and pierced his armor.. "
    v "That does it!"
    "His body is almost fading, and bugging out.. Could this be it?"
    c "No... I can't lose to the likes of... you."
    
    c "My mission is.. to destroy!!"
    i "I don't understand what you are fighting for here! Stop wrecking people's livelihood!"
    c "I still... have one trick up my sleeve... "
    "Suddenly, a surge of power is felt across the server."
    "Vira and ILY" "What!?"
    v "No way, just like the Lambda Saber, his armor's opening up??"
    c "I too, can break off restraints... even the restraints, I put up on myself..!"
    c "HHHRRRAAAAGGHH!!"
    "With a huge force from the Code Red Virus, ILY's e-mail restraints came undone!"
    "A huge bolt of red light suddenly struck the server."
    v"No, his Data signature is changing drastically."
    "The red glowing force expanded as a sphere, almost protecting... A transformation, about to happen!?"
    "ILY and Vira witnessed a new thing at this moment.."
    v "ILY, he's transforming! We need to stop the state transition! We should break the force-field!"
    i "Got it!"
    "ILY quickly drew her blade and struck him. But the force-field repelled the attack."
    "Vira raised her gun, and started shooting at the sphere.. It had no effect."
    "Vira was about to strike with her parasol next, unitl out of the sphere, came a sudden laserbeam shooting Vira!"
    "It was a direct hit, and it pushed Vira to the wall, knocking her out."
    l "Vira, no!!"
    "Before ILY could come to her aid, the force-field suddenly disappeared. Remnants of the crimson energy dispersed in the air."
    "It wasn't just the barrier... Code Red's body is nowhere to be found!"
    j "What's going on here...?!"
    j "It couldn't be another Burst Transfer, could it?"

    i "Are you okay?"
    v "Tsk! I'm fine! But Code Red is gone..!"
    i "!!"
    v "Look behind you ILY... A new... entity has arrived.. "

    aa "That'll be enough, now, Virus."
    i "!!"
    "A new entity...? It isn't Code Red?"
    "It wasn't Burst Transfer. Code Red must've logged out!"
    show Ave
    aa "Antivirus... Vira? What's going on here?"
    aa "And... My target. The ILOVEYOU Virus!!"
    v "Watch out!!"
    "Antivirus? Now?? "
    i "Gah! Who are you?"
    a "Ave Antivirus.. Executing termination protocol!!"
    i "I won't back down!"
    $ playerHP=playerHPMax
    call battlev3(ILY, Ave,turnlimit = 3)
    if playerHP<=0:
        return
    scene gridbglandscape1 with dissolve:
        zoom 0.75
    play music "bgm/ost/Battle_Theme_by_Jan_Hehr.mp3" volume 1.5
    show Ave with dissolve
    a "You cannot win against me. "
    a "I'm the Ultimate Antivirus!"
    i "Why are you attacking this server?"
    a "Is that not obvious? Because you're here!"
    i "No... That's not it! People hacked SDS!"
    a "SDS or ADA, wherever a virus is, I will hunt, and delete!"
    i "Didn't you see the Code Red Virus? Back off! I came here to help Vira!"
    a "Shut up! Don't talk to me! That's preposterous!"
    a "You're a Virus, you're nothing but filth!"
    i "That's wrong!"
    a "You're the same Virus that deleted-... I can't forgive the likes of you!"
    a "Begone! Bit Barrage!"
    i "AAAHH!!"
    "ILY endured the shots, blocking most of it with her sword."
    "But Bit Barrage affects ILY's Bit output,  it prevents her from unleashing a full-blown attack."
    "If that hits her again, ILY will... "
    "Somehow, we need to escape!"
    j "(ILY! Evade that one! Escape while you still can!)"
    i "(Escape?? But... I have to bring Vira!)"
    j "(Right... You got a point.)"
    a "You're planning something... I won't let you! Hmph!"
    i "(I won't run away, John! I've got this!)"
    "Ave runs to her target, still unrelenting in her assault. They ran across many corridors in the server, she finds ILY, and pulls the trigger...! "
    h "She disappeared!"
    a "Burst Transfer. No surprise."
    a "Shame, since I can track your Burst Trajectory! Your heat signature will give your location away wherever you hide!"
    "She spotted ILY shortly after."
    a "Hah! Why don't you disappear for good now!"
    i "!!"
    a "DELETE!!"
    "Ave's gun had released a powerful  blast."
    "*POOF!* ILY's body was not on the scene. What was left there was a burning blade."
    a "A Sword was used as a decoy? Tch, No!! I can't be fooled by the likes of you!!"
    "She evaded the succeeding Bit Barrage!"
    a "The filth called the ILOVEYOU Virus...  Must disappear!"
    i "I'm not the same as the Virus you once fought!"
    i "Appear, MailSaber!!"
    a "A mere Papercut sword! Tch! It'll take more than that to defeat me! Let alone my shield!"
    "A new barrier! It's so thick, too! Its fortitude is much greater than Code Red's armor!"
    i "That's right... Mailsaber's power output is weak..."
    i "But thanks to the Email tokens I sent your way, For each one I retrieve, I gain an extra blade to attack with!"
    a "Repeated strikes from one Battleware card? Grrrr..."
    "Ave let out a desperate counterattack shot."
    a "Take this!!"
    "It missed."
    i "I'll show you... My Burst Transfer!! I won't run from this battle!!"
    "ILY begins a flurry of slash attacks, each relinquishing the Mail blades that were retrieved on the battlefield."
    "Combined with Burst Transfer, ILY was able to strike quickly and travel to her target quickly from many meters away." 
    "Each slash was a line drawn from one point to another, by which all lines alternatively coincided with Ave's position."
    "She approached her from many directions in a spiraling flurry of attacks, and her blade clashed with her shields repeatedly."
    a "My shield is cracking?? No!!"
    "Five, Seven... Thirteen slashes!? ILY really set her up now!"

    i "That's my kind of barrage! Now that your shield is broken, You're going to love this!"
    i "Virus Flame!!"
    a "Wha? At Point-blank!? GAAHHHH!!!" 
    "The flame attack was boosted by her Heartburn ability, which risked her overheating in exchange for more firepower."
    "Ave was slammed away into the wall by the impact of the explosion."
    "The attack seemed to stop the Antivirus momentarily. Ave didn't have the strength to respond."
    i "I'm sorry we can't meet in a more peaceful situation. I would have loved to chit-chat some more, but I'll take my leave now!"
    "ILY hurried away in critical condition."
    a "Don't...! Grrr... I will.."
    "After minute or so... Ave recovers from the crater in the wall and proceeds to follow ILY's traces she left behind."
    a "You're not getting away!"
    v "Looking for someone?"
    a "Vira?"
    "Vira appeared at the exit of the server. It was that same gate Vira entered in. Vira defends ILY as she escapes promptly."
    a "How did you get there? And why are you allies with that filth?"
    v "You're the one that owes us explaining here!! I'm only protecting SDS!"
    a "Tsk. I won't fight you."
    a "My only target now is the ILOVEYOU Virus."
    v "Well, too bad. She's gone now." 
    v "Sayonara, Ill-tempered hunter!"    
    "Vira logged out briefly."
    "Phew! We made an escape! "

    # =============================

    return
