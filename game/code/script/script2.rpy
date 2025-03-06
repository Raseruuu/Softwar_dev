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

    i "John, it's done now."
    j "Here it is.."
    show Vira
    $ Lisa_w=True
    
    v "Greetings, My name is Vira. I am an Antivirus. The Next Generation: FAI."
    v "At your service!"
    v "Pleased to meet you, John Doe."
    j "P-pleasure."
    h "Woah, isn't she kind of cute?"
    l "Yeah... "
    play music "bgm/Pre-Fight_bgm_maoudamashii_cyber01.ogg"
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
    "ILY's holding her ground...!"
    l "No, You shouldn't fight!"
    v "My Powersol Shield has been... bypassed?"
    v "How.. I can't win.. the Virus Signature, is different from the ILOVEYOU Virus in my Database...?"
    i "I'm.. different! I've been altered!"
    v "No! altered or not, a Virus is Virus... I should be able to.. override your control!"
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
    j "Vira, show me what you can do! We have to try to detect for traces of FAI Viruses in SDS."
    v "Show me where this SDS area is..!"


    return


label SDS_Encounter:
    
    # Part 2
    j "So let's get to it now then."
    l "Right."
    "Final few keystrokes to the command line and we are in."
    # [Connecting…]
    # [Systems booting up]
    h "Alright looks like everything is going nicely. This is perfect."
    "Lisa shoots him a concerned look."
    h "What? It's going pretty good so far right?"
    # j "Too early to say it right now."
    # l "Anything could still happen in a remote access, we don't know what happened back then either."
    l "All the diagnostic runs turned back alright, but something could still go wrong."
    i "It's okay, I'm here if anything happens."
    j "Thank you ILY"
    i "Hehe--"
    v "Hey I'm the one scouting here, cut me some credits will you?"
    i "I'm cheering for you Vira. Show us how it's done by an Anti-virus."
    v "O-okay! Definitely! This is what I'm good at."
    h "Yeah we got nothing to worry about. Those should be the top of the class AI right? Nothing I know can affect them."
    "Maybe I should brief him about Bitwulf later, but now's probably not a good time."
    i "?"
    # ["Port Access:granted"]
    h "Let's gooooooo!!!"
    v "Is this blonde human always this noisy?"
    j "Hilbert can get a bit excessive sometimes."
    l "I'd say most of the time in fact."
    h "I'll just pretend I didn't hear those hurtful words."
    i "Gooooooooo!!"
    h "Yeah that's what I'm talking about!"
    v "Can't believe I'm with idiots."

    # =============================

    j "So Vira, can you see anything suspicious?"
    v "The GRID here is a bit more barren, given we just had a shutdown earlier."
    v "Everything looks pretty fine so far though. Kind of expected a professional outfit to have a more streamlined approach than your typical digital world."
    v "I'll run a diagnostic myself here to see if there's anything I need to address here. It could take a while so you guys can relax for now."
    i "I know I can count on you Vira! You're the best!"
    v "S-shut up. You're distracting me!"
    # [CG?]
    v "ahem. Let's see…"
    "A small hum starts to escape from her lips. A simple short tune that loops as she folds up her parasol."
    i "Ooooh? What's this?"
    l "Ssshhhh, let's watch her quietly shall we?"

    "Waving the folded up parasol like magic wand, the anti-viral avatar stretches out to the sound of her hum."
    "Like a ballet dancer, she swings her staff across her body. Her torso and limb elegantly bend as she spins her body around."
    "It's a slow dance at the exact same spot, but the way she controls her \"physical\" self to communicate music completely brightens the surrounding."
    "The typical blue hue of GRID world reflects back from her predominantly red coloured outfit, dazzling the world around her."
    "Gradually she picks up the speed, with the parasol in her hand acts as an extension of her body."
    "It's rapidly chaotic yet systematic at the same time."
    "I begin to wonder, is it really how programs scan things, or is it her character that brings such personality to this procedure."
    "The alluring sequence continues, with us on the other side of the monitor acting as her sole audience."
    "She doesn't care however, as her closed eyes tightens further, and the hum picks up the volume."
    "This is both a survey of the area, and also an extravagant taunt to anyone who happens to be nearby. And what a display it is."
    "With one foot kicked up she slowly drops it down again. The enchanting dance is almost over, and finishes up with the parasol covering her body once more."
    "The song finishes, and she takes a deep breath to regather her composure."

    v "Phew…Reporting, there's--"
    i "WHAT WAS THAT THAT WAS AMAZING VIRA!"
    v "Eh??"
    i "I DIDN'T KNOW YOU CAN DO THAT!"
    v "W-what do you mean??"
    i "DO IT AGAIN, I WANT TO SEE IT AGAIN!!!"
    h "YEAH, WE DEMAND AN ENCORE"
    v "But I don't need to--"
    i "I WANT TO SEE YOU DANCE AGAIN!"
    i "MORE! MORE! MORE! MORE!"
    v "Ehhhh????"
    "Vira nervously looks towards the monitor, searching for a response from me."
    "Lisa has dragged Hilbert away from the screen, with one hand firmly pressed on his mouth to stop him from chanting further." 
    j "Ignore them for now. What did you find?"
    i "Awwww, I want to see it again."
    j "There's time for that later."
    v "Ahem….Alright. There's no signs of major damage sustained in the server. There have been a few minor viruses leaked by but they don't pose a threat as far as I can see."
    v "Put it simply, this server is rather intact."
    h "rrrururururururu!!!"
    h "Haaa. So what did I tell you? Those girls are top at their work. Nothing to worry about here. This team is going great."
    l "I mean, my dad's company is the ones who made Vira, it's gotta be the best industry invention no matter how you see it."
    h "Indeed, and we are lucky to have her on the team. Now SDS should be even more secure for now."
    j "Vira, is that all you'd like to do while over there?"
    v "It should be all that's necessary for now. I think everything is fine over here."
    i "Hmm Heeehhhh. Told you guys my block is effective."
    v "Yeah, by the look of things this place is quarantined rather nicely from the attack."
    v "T-tha---"
    i "Hmmm?"
    v "That you can be rather useful I guess."
    i "Awwwwww"
    "Hmmmm"
    "Wasn't there a change before though?"
    "I guess it was also reverted or that Vira considered it to be minor."
    "Either way, it should be nothing else to do here now."
    i "Never mind that, could you do the dance again? PLEASE>???"
    v "N-no! I'm not dancing for your sake are you out of your mind?"
    j "ILY, we got to regroup again. Vira, can you find your way back fine?"
    v "Hmm? Sure it shouldn't be too much of an issue. The paths are rather spacious."
    h "Okay then, let's think of what do we do next for now."
    v "Yeah I'll see y--"
    # [ "WARNING! UNKNOWN ENTITY DETECTED!" ]

    v "Hold on I'm detecting something."
    j "What is it Vira?"
    v "How did I not see that before, wait."
    v "The gateway is open!"
    v "It's fastly approaching. Who is this entity??"
    h "What's happening!?"
    j "Seems like that previous peace was just a ruse."
    l "Can you handle it Vira?"
    v "Who do you think I am? I'm made for this stuff."
    "She points her parasol towards the direction of the charging enemy reminiscent of how she greeted ILY earlier."
    "Its shield was giving ILY some early troubles, so it should withstand any initial impacts."
    "After that it's just the matter of coordinating her moves."
    "While she lost to ILY earlier, she's still a very strong anti-virus."
    "So why is it that I still feel nervous about it?"
    v "Target approaching in 10 seconds, 9, 8--"

    "It was just way too fast."

    "No trickery, no elaborate ruses."
    "It's just a simple show of strength and speed."
    "Nothing more, nothing less."

    v "AAAAAAAAHHHHHHHHH!!!!"
    "Vira struggles to stand herself up, several screens from where she was standing just a moment ago."
    "The parasol opens up in her hands, still reeling from that initial impact."
    i "VIRA!"
    h "Oh shit oh shit what's happening to her? Why is she like this now???"
    l "Vira can you hear me?"
    "Lisa pushes herself between me and the mic, yelling desperately to it."
    "I've never seen her like this before."
    v "--Yeah I've heard you."
    v "Sorry Lisa. Guess I still am not good enough yet."
    j "Vira, can you see who attacked you?"
    j "Can you identify the assailant?"
    v "Yeah, hold on, i'll bring him up on your monitor."
    #CR sprite
        # ([I'll do the description later])
    v "I don't have him on my database. This could get tough."

    u "Who are you talking to?"
    v "???"
    j "?!"
    u "I SAID. WHO. ARE. YOU. TALKING. TO?"
    v "None of your business."
    u "Oh?"
    u "Guess I'll need to cut off your limbs before you'll tell me then?"
    u "Challenge accepted."
    "The entity draws his big oversized sword and points at Vira again."

    "Vira pulled up her parasol in between them."
    u "heh"
    # *clunk*
    "Another strike"
    "But this time, it's the blue one whose weapon flings behind. His arm arches all the way behind him after the impact."
    u "What is this!?"
    l "(to john) Vira is our company's top creation. We've put in a lot of effort into boosting her defensive capabilities."
    l "That one might've caught us by surprise before, but now there's no way he can get through Vira's parasol."
    l "Let's trust her on this."
    v "I thought you were better than that."
    u "Huh. This is unexpected."
    u "I wasn't expecting to fight you here, but this should be a good warmup before I find her."
    "Another energy wave flies out from his sword, which gets deflected by the parasol in the final moment."
    "The structure behind Vira fractures into fragments by the impact, the debris glitches around her."
    u "Hoh?"
    v "Come at me you overcompensating idiot!"
    "He pulls up another stance, the sword now high up above his head."
    u "Well then."
    u "If I can't get you in one strike, then it just means I just need to hit it more times."

    # [add more stuff here]

    # ====[Softwar]====

    # Part 3
    l "Vira, retreat right now. You are in no shape to fight against this one."
    v "You didn't think I thought about it?"
    v "This one is smart. He cornered me throughout the fight by his positioning."
    v "I'll need to get past him first if I'm to be able to have any chance of running away, in this body no less."
    v "But alas."
    "Vira lifts up the parasol again."
    v "My arms are really sore."
    v "Sorry ILY, don't think I can give you an encore today."

    # [Room background]
    j "..."
    i "John I'm going in."
    h "No you won't. We are not losing both of you to this insane monster."
    i "But…"
    "I turn to Lisa, who's showing even more fear than before."
    "It was just a program, right?"
    "Seeing our eyes meet, she struggles to get words out of her mouth."
    "We can always get a copy of this one right?"
    "So why…?"
    h "I'm going to call the guy to shut down the server again. It's clearly being compromised right now."
    i "But Vira is still in there, we can't leave her in there!"
    h "I don't care. She's an anti-virus, she knows this could happen."

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
