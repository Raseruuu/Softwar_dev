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
    "Chapter 2: A New Friend" #(Can change chapter name anytime)
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
    j "We'll keep watch on this side, ILY will know what's going on."
    h "Let's get em!"
    
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

    v "Spywares are built to gather as much info as it can to send to its master network..."
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
    l "It was the Cafella Coffe Shop's marketplace website. They handle orders for deliveries through that portal."
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
    l "You can call me Pizzalizza!"
    j "?"
    l "Oh!"
    j "Hahahaha!"
    l "HAHAHAHAHA!"

    h "Great, Cafella staff is ready with online transactions. Tell me what you guys like."
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
    "What's going on? I'm  awkward usually.. When did we become so... close?"
    
            # =============================

    # j "So Vira, can you see anything suspicious?"
    # v "The GRID here is a bit more barren, given we just had a shutdown earlier."
    # v "Everything looks pretty fine so far though. Kind of expected a professional outfit to have a more streamlined approach than your typical digital world."
    # v "I'll run a diagnostic myself here to see if there's anything I need to address here. It could take a while so you guys can relax for now."
    # i "I know I can count on you Vira! You're the best!"
    # v "S-shut up. You're distracting me!"
    # # [CG?]
    # v "ahem. Let's see…"
    # "A small hum starts to escape from her lips. A simple short tune that loops as she folds up her parasol."
    # i "Ooooh? What's this?"
    # l "Ssshhhh, let's watch her quietly shall we?"

    # "Waving the folded up parasol like magic wand, the anti-viral avatar stretches out to the sound of her hum."
    # "Like a ballet dancer, she swings her staff across her body. Her torso and limb elegantly bend as she spins her body around."
    # "It's a slow dance at the exact same spot, but the way she controls her \"physical\" self to communicate music completely brightens the surrounding."
    # "The typical blue hue of GRID world reflects back from her predominantly red coloured outfit, dazzling the world around her."
    # "Gradually she picks up the speed, with the parasol in her hand acts as an extension of her body."
    # "It's rapidly chaotic yet systematic at the same time."
    # "I begin to wonder, is it really how programs scan things, or is it her character that brings such personality to this procedure."
    # "The alluring sequence continues, with us on the other side of the monitor acting as her sole audience."
    # "She doesn't care however, as her closed eyes tightens further, and the hum picks up the volume."
    # "This is both a survey of the area, and also an extravagant taunt to anyone who happens to be nearby. And what a display it is."
    # "With one foot kicked up she slowly drops it down again. The enchanting dance is almost over, and finishes up with the parasol covering her body once more."
    # "The song finishes, and she takes a deep breath to regather her composure."

    # v "Phew…Reporting, there's--"
    # i "WHAT WAS THAT THAT WAS AMAZING VIRA!"
    # v "Eh??"
    # i "I DIDN'T KNOW YOU CAN DO THAT!"
    # v "W-what do you mean??"
    # i "DO IT AGAIN, I WANT TO SEE IT AGAIN!!!"
    # h "YEAH, WE DEMAND AN ENCORE"
    # v "But I don't need to--"
    # i "I WANT TO SEE YOU DANCE AGAIN!"
    # i "MORE! MORE! MORE! MORE!"
    # v "Ehhhh????"
    # "Vira nervously looks towards the monitor, searching for a response from me."
    # "Lisa has dragged Hilbert away from the screen, with one hand firmly pressed on his mouth to stop him from chanting further." 
    # j "Ignore them for now. What did you find?"
    # i "Awwww, I want to see it again."
    # j "There's time for that later."
    # v "Ahem….Alright. There's no signs of major damage sustained in the server. There have been a few minor viruses leaked by but they don't pose a threat as far as I can see."
    # v "Put it simply, this server is rather intact."
    # h "rrrururururururu!!!"
    # h "Haaa. So what did I tell you? Those girls are top at their work. Nothing to worry about here. This team is going great."
    # l "I mean, my dad's company is the ones who made Vira, it's gotta be the best industry invention no matter how you see it."
    # h "Indeed, and we are lucky to have her on the team. Now SDS should be even more secure for now."
    # j "Vira, is that all you'd like to do while over there?"
    # v "It should be all that's necessary for now. I think everything is fine over here."
    # i "Hmm Heeehhhh. Told you guys my block is effective."
    # v "Yeah, by the look of things this place is quarantined rather nicely from the attack."
    # v "T-tha---"
    # i "Hmmm?"
    # v "That you can be rather useful I guess."
    # i "Awwwwww"
    # "Hmmmm"
    # "Wasn't there a change before though?"
    # "I guess it was also reverted or that Vira considered it to be minor."
    # "Either way, it should be nothing else to do here now."
    # i "Never mind that, could you do the dance again? PLEASE>???"
    # v "N-no! I'm not dancing for your sake are you out of your mind?"
    # j "ILY, we got to regroup again. Vira, can you find your way back fine?"
    # v "Hmm? Sure it shouldn't be too much of an issue. The paths are rather spacious."
    # h "Okay then, let's think of what do we do next for now."
    # v "Yeah I'll see y--"
    # # [ "WARNING! UNKNOWN ENTITY DETECTED!" ]

    # v "Hold on I'm detecting something."
    # j "What is it Vira?"
    # v "How did I not see that before, wait."
    # v "The gateway is open!"
    # v "It's fastly approaching. Who is this entity??"
    # h "What's happening!?"
    # j "Seems like that previous peace was just a ruse."
    # l "Can you handle it Vira?"
    # v "Who do you think I am? I'm made for this stuff."
    # "She points her parasol towards the direction of the charging enemy reminiscent of how she greeted ILY earlier."
    # "Its shield was giving ILY some early troubles, so it should withstand any initial impacts."
    # "After that it's just the matter of coordinating her moves."
    # "While she lost to ILY earlier, she's still a very strong anti-virus."
    # "So why is it that I still feel nervous about it?"
    # v "Target approaching in 10 seconds, 9, 8--"

    # "It was just way too fast."

    # "No trickery, no elaborate ruses."
    # "It's just a simple show of strength and speed."
    # "Nothing more, nothing less."

    # v "AAAAAAAAHHHHHHHHH!!!!"
    # "Vira struggles to stand herself up, several screens from where she was standing just a moment ago."
    # "The parasol opens up in her hands, still reeling from that initial impact."
    # i "VIRA!"
    # h "Oh shit oh shit what's happening to her? Why is she like this now???"
    # l "Vira can you hear me?"
    # "Lisa pushes herself between me and the mic, yelling desperately to it."
    # "I've never seen her like this before."
    # v "--Yeah I've heard you."
    # v "Sorry Lisa. Guess I still am not good enough yet."
    # j "Vira, can you see who attacked you?"
    # j "Can you identify the assailant?"
    # v "Yeah, hold on, i'll bring him up on your monitor."
    # #CR sprite
    #     # ([I'll do the description later])
    # v "I don't have him on my database. This could get tough."

    # u "Who are you talking to?"
    # v "???"
    # j "?!"
    # u "I SAID. WHO. ARE. YOU. TALKING. TO?"
    # v "None of your business."
    # u "Oh?"
    # u "Guess I'll need to cut off your limbs before you'll tell me then?"
    # u "Challenge accepted."
    # "The entity draws his big oversized sword and points at Vira again."

    # "Vira pulled up her parasol in between them."
    # u "heh"
    # # *clunk*
    # "Another strike"
    # "But this time, it's the blue one whose weapon flings behind. His arm arches all the way behind him after the impact."
    # u "What is this!?"
    # l "(to john) Vira is our company's top creation. We've put in a lot of effort into boosting her defensive capabilities."
    # l "That one might've caught us by surprise before, but now there's no way he can get through Vira's parasol."
    # l "Let's trust her on this."
    # v "I thought you were better than that."
    # u "Huh. This is unexpected."
    # u "I wasn't expecting to fight you here, but this should be a good warmup before I find her."
    # "Another energy wave flies out from his sword, which gets deflected by the parasol in the final moment."
    # "The structure behind Vira fractures into fragments by the impact, the debris glitches around her."
    # u "Hoh?"
    # v "Come at me you overcompensating idiot!"
    # "He pulls up another stance, the sword now high up above his head."
    # u "Well then."
    # u "If I can't get you in one strike, then it just means I just need to hit it more times."

    # # [add more stuff here]

    # # ====[Softwar]====

    # # Part 3
    # l "Vira, retreat right now. You are in no shape to fight against this one."
    # v "You didn't think I thought about it?"
    # v "This one is smart. He cornered me throughout the fight by his positioning."
    # v "I'll need to get past him first if I'm to be able to have any chance of running away, in this body no less."
    # v "But alas."
    # "Vira lifts up the parasol again."
    # v "My arms are really sore."
    # v "Sorry ILY, don't think I can give you an encore today."

    # # [Room background]
    # j "..."
    # i "John I'm going in."
    # h "No you won't. We are not losing both of you to this insane monster."
    # i "But…"
    # "I turn to Lisa, who's showing even more fear than before."
    # "It was just a program, right?"
    # "Seeing our eyes meet, she struggles to get words out of her mouth."
    # "We can always get a copy of this one right?"
    # "So why…?"
    # h "I'm going to call the guy to shut down the server again. It's clearly being compromised right now."
    # i "But Vira is still in there, we can't leave her in there!"
    # h "I don't care. She's an anti-virus, she knows this could happen."

    "It's not right."
    "This isn't right."
    "My mind flashes back to when Melissa saved ILY earlier."
    "No one deserves to disappear alone."
    "It's just not right."
    j "Hilbert, hold on for a second there."
    j "ILY?"
    i "Yes John?"
    j "Smash. Go bring her home."
    i "ROGER THAT!"

    # ====[GRID]====

    # [segment of more Vira and CR]
    # [ILY triumphant entry]
    # [CR interrogates ILY]

    # [SW]

    # Part 4
    u "Gah!"
    "The blue enemy leans onto his massive weapon, one knee down to the ground."
    i "Now get away and never come back!"
    u "Heheh"


    return
