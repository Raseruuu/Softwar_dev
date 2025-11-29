transform newdissolve:
    # mesh True
    alpha 0.0
    linear 1.0 alpha 1.0 
label download_complete:
    scene blue with Dissolve(0.2)
    show Folders with dissolve

    show whitewindow:
        zoom 0.0  xpos 0.5 xanchor 0.5 yalign 0.5
        linear 0.2 zoom 1.0

    pause 0.5
    show dlcomp:
        alpha 0.0 xalign 0.5 yalign 0.5
        linear 0.3 alpha 1.0 xalign 0.5 yalign 0.45
    pause 0.5
    show dlheart with Dissolve(0.1):
        xalign 0.5 yalign 0.52
        alpha 0.0
        linear 0.3 alpha 1.0
    return
label script1:
    # jump test
    $ okdesktop = False
    scene black
    pause 1.0
    show text "{size=30}{color=#fff}February 14{/color}{/size}\n\n" with dissolve
    pause 1.0
    show text "{size=30}{color=#fff}February 14{/color}{/size}\n\n {color=#ddd}Valentine's Day{/color}" with dissolve
    pause 2.0

    scene Email with dissolve_heart

    "What's this? Someone sent me a love letter?"
    "I wonder who it's from... Wait, Lisa?"
    "This attachment.. She's... confessing, using a script? That's something only a shut-in programmer would do."
    "I didn't know she was that kind of person... sending such a thing to me."
    show Mouse:
        xalign 1.0 yalign 0
        linear 0.5 yalign 0.4 xalign 0.3
    pause 0.6
    play sound "sfx/sfx_sounds_interaction24.wav"
    pause 0.4


    scene white_noise with dissolve
    pause 1.0

    scene black with dissolve
    play music "bgm/downtime_bgm_maoudamashii_8bit17.mp3"
    show ILOVEYOU

    pause 0.5
    "Huh? What the...?"
    "Oh crap, don't tell me..."

    play sound "sfx/sfx_damage_hit8.wav"

    "*Spacebar* " with Shake((0, 0, 0, 0), 0.5, dist=5)
    play sound "sfx/sfx_damage_hit4.wav"
    extend "*Esc* " with Shake((0, 0, 0, 0), 0.5, dist=10)
    play sound "sfx/sfx_damage_hit8.wav"
    extend "*Enter* " with Shake((0, 0, 0, 0), 0.5, dist=15)
    play sound "sfx/sfx_damage_hit8.wav"
    "*CTRL+ALT+Del* " with Shake((0, 0, 0, 0), 0.5, dist=15)
    play sound "sfx/sfx_damage_hit8.wav"
    extend "*qwertyuiop* " with Shake((0, 0, 0, 0), 0.5, dist=20)
    play sound "sfx/sfx_damage_hit4.wav"
    extend "*asdfghjkl* " with Shake((0, 0, 0, 0), 0.5, dist=20)
    play sound "sfx/sfx_damage_hit8.wav"
    extend "*zxcvbnm,./*" with Shake((0, 0, 0, 0), 0.5, dist=20)
    "Keyboard commands aren't working. I can't close this thing."

    $ JohnSprite("frown")
    "A... {i}Virus{/i}?"
    "That means.. Lisa was... no way."
    j "Great, I didn't get a chance to save."
    j "Well, there goes 2 hours worth of work."
    $ JohnSprite("mad")
    j "Actually, that was probably worth more than just 2 hours. "
    "Damn, I guess I don't have a choice but to restart."

    play sound "sfx/sfx_sounds_interaction24.wav"
    hide ILOVEYOU with dissolve
    pause 1.0

    "Alright, and back on..."
    play sound "sfx/sfx_sounds_interaction24.wav"
    pause 1.0

    show ILOVEYOU with dissolve

    "No way, this can't be happening!"
    play sound "sfx/sfx_damage_hit4.wav"
    extend "*Esc* " with Shake((0, 0, 0, 0), 0.5, dist=10)
    play sound "sfx/sfx_damage_hit8.wav"
    extend "*Esc* " with Shake((0, 0, 0, 0), 0.5, dist=10)
    play sound "sfx/sfx_damage_hit4.wav"
    extend "*Esc* " with Shake((0, 0, 0, 0), 0.5, dist=10)

    "I can't believe it! How did I fall for an email virus?!"
    "I program software all day. I should have known better!"
    "I blame my lack of sleep. I've been up for 30 hours working on this project.. and others... and I'm still not done."

    "This looks like the end of my computer. "
    extend "And my career. "
    extend "And any hopes of me finishing college."

    "My computer was destroyed by an e-mail virus."
    "Next Tuesday is when we launch the big stuff. But it looks like I'm getting fired!"
    j "Why didn't I make a backup?!"
    "Forget a few hours, that's weeks worth of work!"

    play sound "sfx/sfx_damage_hit4.wav"
    "*Esc* " with Shake((0, 0, 0, 0), 0.5, dist=10)
    play sound "sfx/sfx_damage_hit4.wav"
    extend "*spacebar* " with Shake((0, 0, 0, 0), 0.5, dist=10)
    play sound "sfx/sfx_damage_hit4.wav"
    extend "*Enter* " with Shake((0, 0, 0, 0), 0.5, dist=10)
    j "{i}sigh{/i}"

    hide ILOVEYOU with Dissolve(2.0)
    scene JD_Space2_night with dissolve
    "I go to the window to get some fresh air."
    "Hhmmmmmm... Ughhhhh.."

    play sound "sfx/sfx_coin_cluster6.wav"
    "I look at my phone and notice a new text."
    "It's Hilbert Salcedo, my pal from school."
    h "Real funny, dude. For a second, I thought I got a love letter from a hottie."
    h "Had fun yanking my chain?"
    j "What are you talking about?"
    h "You sent me an email called \"My confession...<3\"."
    h "Haven't read it yet, just give me a sec."

    "What, a love letter? That's stupid, I didn't send--"
    "Wait...  Damn. It's that virus! It's sending itself to my contacts!"
    "\"Bro, don't open the attachment! It's a virus!\""
    "I hit the send button, but..."

    play sound "sfx/sfx_coin_cluster6.wav"
    h "What the heck man, my PC's not working! I'm getting this stupid message on my screen that won't go away."
    "Too late. He's suffering just like me now. I bet every one of my contacts is experiencing the same crap."
    "Hilbert restarted his PC. But I already knew that was pointless."
    scene JD_PCN with dissolve
    $renpy.pause(0.8,hard=True)
    scene black with dissolve
    show ILOVEYOU with Dissolve(2.0)
    "I head back to the desktop. That awful message is still controlling my screen."
    "\"ILOVEYOU\" is a name of an old virus that infects by tricking the users that they received a love letter."
    extend "\nI must admit it only worked because it was from Lisa. I thought she was... noticing me..."
    "..."
    j "{i}yawn{/i}"
    "Oh man, I've gotta get some sleep. I was hoping to finish today, but there's no point anymore."
    "I'll get back to it in the morning once I have a clearer head. When I'm not panicking about getting fired."
    "I rest my head on the table in front of the monitor and decide to let the night pass..."

    hide ILOVEYOU with Dissolve(2.0)
    pause 2.0

    scene white
    "I wake up, remembering last night."
    "Another dreamless night. If only the virus was just part of a dream."
    "I glance at the screen. Strangely, the screen had gone black."
    "I hadn't pulled the plug. And I live alone. I guess the computer went to sleep."
    "I clumsily stretch my arms forward to the desktop and press a random button on the keyboard."

    $ okdesktop = True
    call download_complete
    pause 0.5
    $ JohnSprite("frown")
    j "Woah!"
    "The screen lights up and reveals a new app."
    $ JohnSprite("normal")
    play sound "sfx/Damage.wav"
    j "Hell yeah! My PC still works!" with Shake((0, 0, 0, 0), 0.5, dist=5)

    "Download complete? What does that mean?"

    call download_hide
    "Oh crap, is this thing monitoring me now?"
    hide screen checks

    show text "{color=000}ALL SYSTEMS READY{/color}" at notifanim
    "..."
    hide text
    show dlheart with Dissolve(0.1):
        xalign 0.5 yalign 0.52
    show text "{color=#b51b1b}INITIATING FUTURE A.I.:\nILOVEYOU VIRUS v2.0{/color}" at notifanim
    "This is still part of the ILOVEYOU virus? Well, damn."
    hide text
    pause 0.5
    hide whitewindow
    hide dlheart
    play sound "sound/loadcard.wav"
    show ILY with dissolve_pixels
    play music "bgm/ost/ILY's_Theme_game_by_Jan_Hehr.mp3"  fadeout 1 loop
    $ persistent.has_met_ILY=True
    i "HELLO, USER! I am the ILOVEYOU virus!"
    i "Call me ILY! "
    extend "I'm signing up to be your personal assistant!\nI'd like to confirm your name!"
    "Am I really awake? A virus is signing up to be my assistant. That's kinda sweet."
    i"Should I just call you master then?"
    "ILY, huh. The envelope on her head reminds me of last night's e-mail. I'm supposed to be mad now, but this is quite interesting."



    $ ILYSprite("frown",0)
    i "Are you listening to me?"
    i "The speakers are on, aren't they? Please confirm your full name."

    "This thing is suspicious, but it looks like it has a lot to offer."
    $plrname = 'John Doe'
    #$plrname = renpy.input(_("Input your name(Default = John Doe):")) or _("John Doe")

    # @TODO  : make sure john's sprite appears

    $ JohnSprite("frown")
    j "[plrname]. That's my name."

    $ ILYSprite("smile3")
    i "Identity confirmed."

    $ ILYSprite("smile")
    i "[plrname], do you accept my offer to be your assistant? I've worked so hard just to get to your PC!"

    menu:
        "ILY wants to be my assistant. Do I accept?"
        "Yes":
            "This is exciting. I want to see just how good this AI is."
            j "I accept. But I have to know the conditions."
        "No":
            "No way, this is way too suspicious."
            "Still, she IS a virus... I have to be careful with how I respond."

    j "What is this all about? You hacked my PC, and suddenly offer some service. Nothing in this world's free."

    i "[plrname]. I am the ILOVEYOU virus."
    $ ILYSprite("smile")
    extend" True love is...{w=0.5}{nw}"
    play sound "sfx/Damage2.wav"
    extend" Unconditional!" with Shake((0, 0, 0, 0), 0.5, dist=5)

    "Inconcievable. If anything, conditions are the meat of every program."
    "I have little trust in what this virus can do for me, or if any of my data is safe at all after this. After all, this IS hacking."

    $ JohnSprite("mad")
    # show John eyeszoom with Dissolve(0.3):
    #    yzoom 0.0
    #    linear 0.1 yzoom 1.0

    "I'm curious about... This \"Future Artificial Intelligence\"!"
    # show John eyeszoom:
    #    linear 0.1 yzoom 0.0
    # pause 0.1
    # hide John eyeszoom

    j "I've got many questions about you and your purpose as a... virus assistant."

    $ ILYSprite("smile3", 0)
    i "I understand. Please ask them one at a time."

    "I have two main concerns for now: My PC, and her. Here goes."
    $ q1_else=""
    $ q1_read_ily  = False
    $ q1_read_pc   = False
    $ q1_read_grid = False
    
    $ q_TheGrid = "???"
    $ q_Softwar = "???"
    
    label question1_demo:
      
        $ q_TheGrid = "The GRID" if q1_read_pc and not q1_read_grid else "???" 
        if q1_read_grid:
            $ q_TheGrid = "The GRID"
        $ q_Softwar = "Softwar" if q1_read_ily and q1_read_grid else "???" 
        if q1_read_ily and q1_read_grid:
            play music "bgm/Enemy_bgm_maoudamashii_cyber19.ogg" fadeout 1 loop
        else:
            play music "bgm/Relax_bgm_maoudamashii_healing15.ogg"  fadeout 1 loop
        menu:
            "What [q1_else]do I want to ask about?"
            "ILY" if q1_read_ily == False:
                $ q1_else="else "
                $ ILYSprite("smile3")
                $ JohnSprite("normal")

                j "You're a pretty well done program."
                i "Isn't it a little too early for you to be evaluating my performance?"
                j "In the eyes of a programmer, you're already amazing."
                voice "voice/ILY22C - Giggle.mp3"
                i "Do you love me?"

                $ ILYSprite("frown")
                $ JohnSprite("mad")
                j "No."
                i "..."
                j "Say.."
                voice "voice/ILY01 - It's ILY~.mp3"
                i"It's ILY~!"
                j"What happens if I disconnect my computer from the internet now?"

                $ ILYSprite("smile3")
                i "That's fine by me. Go on, try it."
                "If all the processing is done online, this could possibly shut down her bot brain..."
                show screen notifwindow("{color=#000}Disconnected from the Internet.{/color}")
                "*Disconnects internet connection*"
                hide screen notifwindow
                i "Awww, now I can't go surfing."
                "Huh, she works fine even without an internet connection."
                i "Hey, this is fine, too. Being disconnected from the world means that only the two of us are in this room."
                "Two of us? I'm alone in this room. There's no \"two of us\"."
                "Moving on..."
                j "How exactly are you going to be my assistant?"

                $ ILYSprite("smile")
                i "I have full control over your PC! Any time you wanna command me to do stuff, just speak over the mic, I'll get it done!"

                i "I'm a product of the Future Artificial Intelligence, or FAI Project!"
                i "FAI programs are powerful like this, but only a few are like me."

                $ ILYSprite("smile3", 0)
                j "This \"FAI project\" stuff. Who made it? Who is your creator?"

                $ ILYSprite("frown")
                i "I can't disclose any more information about the FAI project or my creator."
                j "How come?"
                i "Classified information."
                "I pause for a moment to think. I say it out loud;"
                j "Hackers."

                $ ILYSprite("smile")
                i "That's a good word to sum up your situation right now."
                j "Tell me about it."
                i "I'm a hacking tool. Used by hackers. And that's what I'm here for!"
                j "Say what?"
                i "I'm going to make you a hacker!"

                $ ILYSprite("smile3")
                j "You're kidding."
                voice "voice/ILY22C - Giggle.mp3"
                i "I can joke around, but that isn't my thought sequence right now."

                $ ILYSprite("frown")
                j "So you're suggesting that I become a hacker?"
                play music "bgm/Enemy_bgm_maoudamashii_cyber19.ogg"  fadeout 1 loop
                i "I'm not suggesting. It is your destiny."
                $ ILYSprite("smile3")
                "Serious words coming from someone with a deeply unserious character design."
                i "[plrname], I will assist you with any digital matters as your assistant... And as a hacking tool."
                i "With me, you can hack another system, for whatever reason."
                i "It isn't that simple, though."
                i "Some PCs may be able to protect from hacking. That's when we go to war."

                j "This is getting really shady."
                j "I'm... not really all that interested in hacking anybody now..."
                $ILY_e='down'
                i "[plrname], I was made also to participate in this war."
                extend" A Softwar."

                if not q1_read_grid:
                    "Softwar, huh. I'll have to ask her about that later."
                else:
                    "I think It's finally time to ask about this Softwar."

                play music "bgm/Conversation_bgm_maoudamashii_cyber13.ogg"  fadeout 1 loop
                $q1_read_ily = True
                jump question1_demo

            "My PC" if not q1_read_pc:
                $ ILYSprite("smile3")

                j "What did you do to my PC?"
                i "I made some changes before downloading myself here!"
                i "First of all, despite infecting your computer and all, your computer is safe and usable."
                "I still need to make the site modifications, and my deadline is next Tuesday. That's a huge relief, but why though?"
                j "Why would you spare my computer?"
                i "Because ILOVEYOU."
                j "So what about Hilbert's computer? Is that fine as well?"
                i "Nope, it's still down."
                j "So why is it just my computer that's okay?"
                i "I already said it's because ILOVEYOU."

                "This thing has a habit of dodging questions..."
                j "What other changes did you make?"
                i "Since I take up 14.3 gigabytes, I deleted some stuff."
                "I let that sink in a little bit."
                "Hold on a sec..."
                play sound "sfx/Damage.wav"
                "My disk is almost full. Did she just say she deleted 14.3 gigabytes!?" with Shake((0, 0, 0, 0), 0.5, dist=5)
                i "You look terrible. Well I deleted 10.56709 GB from your drive to be exact."
                "Keep... Calm..."
                j "What did you delete?"

                $ ILYSprite("smile")
                i "A folder called \"G\" and another one called \"H\"."

                $ ILYSprite("o")
                play sound "sfx/Damage.wav"
                "G AND H!?" with Shake((0, 0, 0, 0), 0.5, dist=5)

                $ ILYSprite("frown")
                j "Why those?"

                $ ILYSprite("smile3")
                voice "voice/ILY22C - Giggle.mp3"
                i "They were on the top of the list of folders with most useless files with the biggest size!"
                "So she checked out my files. How does she even classify what's useless and not?"
                i "You look upset."
                i "I believe \"G\" stands for \"Games\", and \"H\" stands for \"He--"
                j "Wait. Don't say it."
                play sound "sfx/Damage2.wav"
                "My precious collection!! " with Shake((0, 0, 0, 0), 0.5, dist=5)
                extend"But now it's gone. I had a few time-killing games and... well, that \"H\" folder..."
                j "I'm fine with it. It's okay to delete those files, as long as that's all."
                i "I didn't delete anything work-related."
                j "That's perfect. Let's move on."

                $ ILYSprite("smile")
                i "Oh yeah, the third thing! You should know about the GRID!"
                i "Every FAI program is a package to set up the computer for the GRID!"
                "The GRID...? I'll have to ask about that."
                $q1_read_pc = True
                jump question1_demo

            "[q_TheGrid]" if q1_read_pc and not q1_read_grid:
                $ ILYSprite("smile3")
                j "What's this GRID all about?"
                i "The GRID is the name for the place we cyberpeople step into!"
                i "As I've said earlier, this PC can now access the GRID. FAI programs installed can automatically access the GRID."
                i "I'm a FAI virus, so naturally, here I am. This desktop now is the GRID version of what you've been using."
                i "Not every program can enter the GRID."
                i "Think of it as another dimension aside from the usual interface you see on the computer."

                "How come I've never heard of any of this before? It almost sounds like a conspiracy."
                i "If you ever get attacked by a regular virus, it's easy to get infected if you don't have an antivirus."
                i "However, if you get attacked by FAI virus such as myself, you're definitely getting infected."
                "That's exactly what happened."

                j "So an antivirus is useless against FAI viruses?"
                i "It really depends. You can survive an attack if you meet these two conditions:"
                i "First, the antivirus must exist in the grid, or be a FAI antivirus."
                i "Second, the antivirus must be stronger than I am, or be able to beat me in a cyber battle, called a Softwar."
                j "I see."
                if q1_read_ily:
                    "It all falls back to this Softwar battle."
                i "Since I have control of your computer, I won't allow you to install an antivirus."
                "Damn. She saw through me."
                j "If I understand correctly... The GRID is a place only FAI programs can get into, so it's isolated space from the one regular programs reside in."
                j "So the Softwar is a GRID-exclusive battle of programs... Right?"
                i "Correct! You're easy to pick up on things."
                if q1_read_ily:
                    i "I should definitely start telling you about this Softwar."
                $q1_read_grid = True
                jump question1_demo

            "[q_Softwar]" if q1_read_ily and q1_read_grid:
                j "Alright. Tell me about Softwar. You sounded serious when you mentioned it earlier."

                i "Only FAIs can take part in Softwars. They are battles between programs."
                i "Technically, it's really a game,"
                $ ILYSprite("frown")

                extend " but the stakes are quite serious!"
                "A battle game, huh."
                $ ILYSprite("mad")
                i "A Softwar goes like this. A virus, with or without a user, may be transported to a target computer system."
                i "The antivirus, living inside the target computer system, will intercept the arrival of that virus, and hope to delete it!"
                i "If the virus gets deleted, then the target computer is safe! Otherwise, the target will be subject to the terror of that virus."
                j "So it's like storming a castle."
                i "Yes, the Attackers are viruses, and the castle is the target computer system, the Defenders."
                i "So there are 2 sides to this battle. Attackers and Defenders."
                "I don't like the idea of being an Attacker, even though I have an intelligent virus with me..."

                j "Why would such a game exist?"
                $ ILYSprite("smile3")
                i "Softwar gives everybody a chance to protect themselves from hackers!"
                j "But if hackers created the whole Softwar system in the first place..."
                $ ILYSprite("frown")
                j "It makes no sense to give your supposed victims a chance to fight back."
                play music "bgm/Relax_bgm_maoudamashii_healing15.ogg"  fadeout 1 loop

                $ ILYSprite("o")
                i "That's true."

                $ ILYSprite("smile")
                extend" I'm not sure, myself! "
                i"Maybe the system is meant to keep the bad viruses from causing too much trouble!"

                j"You speak as if viruses can be any good."
                i"I'm a good virus!"
                "Hmph. Viruses are pure evil."

                $ ILYSprite("frown")
                j "Not convinced."

                $ ILYSprite("smile")
                i "Personally, I think the Softwar system was made for a new generation of fun! Perhaps it was made for the Future AIs to gain a spotlight or two."
                j "But we're talking about people who break rules all the time. Who's to say that hackers won't find a flaw in the Softwar system?"

                $ ILYSprite("smile3")
                i "They might try, but we don't know if they'll succeed. The GRID is running on a deeper level than the regular interfaces."

                j "Really..."
                i "The GRID, FAIs, and the Softwar system were also built without the knowledge or permission of the government, so it's best not to tell others for now."
                j "An elaborate system of AIs and Cyber battles like this will definitely be popular soon."
                i "A Softwar might happen soon in this PC, if we reconnect our Internet, so we better be careful."
                j "How exactly do I prepare for a Softwar though? Just in case?"

                $ ILYSprite("frown")
                i "Usually you'd install antiviruses to protect from viruses..."

                $ ILYSprite("o")
                i "But you've already been bit by the lovebug! I'm the only FAI you need!"

                $ ILYSprite("smile")
                play sound "sfx/Damage.wav"
                extend" I can delete viruses too, you know!" with Shake((0, 0, 0, 0), 0.5, dist=5)
                "So viruses can battle viruses too, huh. That's like having an antivirus and virus in 1 program. Interesting."

                $ ILYSprite("o")
                j "That's good to know, ILY."
                i "Have you accepted your fate?"
                j "I still can't trust you yet."

                $ ILYSprite("smile3")
                i "Of course you can trust me! Trust is an essential part of love!"

        

label date1:
    j"There are some things you have to do for me to trust you."
    "Damn, I never thought I'd see the day when I say such words... to a program. "
    "I'm actually being a huge idiot for buying into what this virus says."
    "Back in the year 2000,{w=.3}{nw}"
    extend" the ILOVEYOU Virus destroyed a heck load of PCs."
    extend" To think this program would call herself by that name...{w=.3}{nw}"
    extend" It's driving me crazy."
    "This PC is all I have,"
    extend" so I'll have to make do with all this."
    "More importantly, I have an appointment today."
    $ ILYSprite("O")
    j"ILY, I have someone to meet today."
    i"May I ask who?"
    "It's Lisa Fairfield."
    $ JohnSprite('mad')
    j"Lisa.. is a friend from uni."
    $ ILYSprite("O")
    i"Is it a date?"
    j"She's not into me."
    i"Oh, It's a girl!"
    $ ILYSprite("smile")
    play sound "sfx/Damage.wav"
    extend" I knew it!" with Shake((0, 0, 0, 0), 0.5, dist=5)
    # $ILY_p = '2'
    play sound "sfx/Damage.wav"
    extend" Virus intuition!" with Shake((0, 0, 0, 0), 0.5, dist=5)
    extend" I knew it, John's going to a date!" with Shake((0, 0, 0, 0), 0.5, dist=5)
    # $ ILY_p = '0'
    $ ILYSprite('frown')
    j"We're meeting for business' sake only,{w=.3}{nw}"
    extend" okay?"
    j"I'm shutting down this PC..."
    "..."
    $ ILYSprite('smile3')
    j"Wait a minute."
    extend" How do I exit you?"
    i"You don't. FAIs are always active!"
    # $ ILY_p='2'
    extend" But don't worry about your RAM, I've integrated myself to your OS to reserve processing power!"
    "My mental image of that \"integration\" was not so pleasant."
    # $ ILY_p='0'
    j"Okay."
    extend" I'm still shutting down."
    $ ILYSprite("O")
    play sound "sfx/Damage.wav"
    i"Wait!!" with Shake((0, 0, 0, 0), 0.5, dist=5)
    $ILY_m='smile3'
    extend" I wanna go surf the net."
    j"I don't trust you enough to let you roam while I'm not around, you virus girl."
    $ILY_m='O'
    i"So you're really shutting down?"
    $ILY_m='frown'
    j"Shutting down."
    $ILY_m='smile3'
    i"Well, have a lovely day, John! Good luck with Lisa."
    hide ILY with dissolve_pixels
    $ okdesktop = False
    pause .5
    scene black with dissolve
    j"Wait a sec, did you just say--{w=.5}{nw}"
    j"Got shut down already, huh."
    extend" Did she say \"Lisa\"?"
    "She said her name."
    extend" Lisa."

    show Lisa with dissolve:
        xalign 0.5
    "Lisa Fairfield."
    extend" A genius programmer girl. We're batchmates currently taking internship at Hilbert's family company."
    "We've been working on this website for a client for quite a while now."
    "I'm seeing her today for our job at the Salcedo Dev studio."
    "She also said that she'll tell me something important."
    extend" I wonder what that is..."
    "I hope it's something exciting, like a new programming contest."
    extend" I'd love to join a Hackathon soon."
    hide Lisa with dissolve
    scene JD_PC1
    play music "bgm/downtime_bgm_maoudamashii_8bit17.mp3"


label date2:
        "Lisa had been away, since last December."
        "She'd been scheduling for us to see each other for over a month now, actually."
        "Lisa... Inviting me to meet at a cafe..."
        "Now that I think about it, this does sound like a date,{w=.3} given the month,"
        play sound "sfx/Damage.wav"
        extend " we could be mistaken for a couple!" with Shake((0, 0, 0, 0), 0.5, dist=5)
        "What am I thinking?"
        extend" This is ILY's fault for putting that idea into my head!"
        scene JD_Door with dissolve
        "It's a meeting, not a date. {w=.5}{nw}"
        play sound "sfx/Damage.wav"
        extend"Totally not a date!" with Shake((0, 0, 0, 0), 0.5, dist=5)
        scene black with dissolve
        "As I head toward our meeting place.. {w=.3}{nw}"
        extend"My thoughts are filled with Lisa, {w=.3}{nw}"
        extend"and whatever she wanted to tell me."
        scene cafeoutside
        play music "bgm/Cafella_bgm_maoudamashii_acoustic51.mp3"
        "I walk towards the cafe. There she is, waiting for me by the entrance."
        "It's been 30 minutes since our designated meeting time. If it hadn't been for that virus on my PC!"
        extend" I wonder if she's frustrated that I'm late?"
        show Lisa with dissolve
        $ Lisa_w=False
        l"John!"
        $JohnSprite('normal')
        j"Lisa, you're here!"
        j"Sorry I'm late! Have you been here long?"
        l"No, not at all! I got here a few minutes ago myself."
        "That's a relief."
        l"Anyway, um.. I'm glad you came, John!"
        j"Right. What was it you wanted to talk about?"
        l"Ah yes.. I'll tell you inside."
        scene cafedoor with dissolve
        $ renpy.pause(0.8,hard=True)
        scene cafeinside with dissolve
        $Lisa_w=True
        l"Actually, I've already got a table for us."
        $JohnSprite('frown')
        j"Wait, so I really am late?"

        l"Yeah, by a few minutes."
        scene cafetable with dissolve
        "Something tells me the \"few minutes\" she mentioned earlier lasted longer than she's telling me."
        "Here's some concrete evidence... 2 ice-cold frappes are already on the table she's pointing at."
        "She's so thoughtful and responsible.. "
        $ Lisa_e = 'mad'
        $ Lisa_m = 'frown'
        play sound "sfx/Damage.wav"
        l"J-just so we're clear!!" with Shake((0, 0, 0, 0), 0.5, dist=5)
        play sound "sfx/Damage2.wav"
        extend" Those two cups are all for me, ok?" with Shake((0, 0, 0, 0), 0.5, dist=5)
        "Eh? That's too sweet!"
        $Lisa_w=False
        show Lisa with dissolve
        l"You can order for yourself if you want."
        "It's tempting, but I'm trying to save my money..."
        "Hold on... What am I thinking? This isn't very manly of me."
        j"..."
        $ Lisa_e = 'normal'
        l"You're not getting any?"
        j"..."
        l"Hey, just tell me if you want my other cup."
        j"I didn't mean that at all!"
        l"Go on, you can have it."
        "Did Lisa just read my mind?"
        "Wow, what just happened? Does this mean she actually did buy this for me?"
        $JohnSprite('mad')
        j"Uh, Thank you very much!!"
        "Dammit. I'm such an awkward guy to be with. This is quite embarassing."
        "Mocha... Does she know what I like or was it a lucky guess?"
        $JohnSprite('normal')
        j"This is... I like this very much, Lisa."
        "I'm genuinely glad, and it puts a smile on my face."
        "Looking straight to her eyes makes me think of a lot of my shortcomings."
        $ Lisa_m="smile"
        l"Th-that's good!"
        
        l"Umm... In exchange you have to code a lot tonight!"
        "Ah. So it's about work now."
        l"I'm giving you this as your subordinate, ok?"
        $JohnSprite('mad')
        j"Yes ma'am!"
        "Take that ILY, this is a meeting, not  a date! It's all about work from here."
        l"We've got work to do, John. I know I can explain online, but it's easier in person."
        j"Go on."
        $ Lisa_m="frown"
        l"We're adding 3 more features to the website we've been working on to be submitted before next Tuesday."
        l"They're a little different from the ones we've already done,"
        $ Lisa_m="smile"
        $ Lisa_e="normal"
        extend" but I'm sure you can handle it."
        j"I see."
        "Lisa lifts her tablet on me to show her notes."
        j"Wait a minute... This isn't very exciting news. I was hoping for a hackathon."
        $ Lisa_e="mad"
        $ Lisa_m="frown"
        l"The hackathon can wait!"
        scene cafeoutside2 with dissolve
        "After that, we discussed a lot."
        "Time passed quickly as I stared at her, jotting down notes regarding our assignment."
        "We've sipped our last drops of coffee."
        $ Lisa_e="normal"
        $ Lisa_m="smile"
        $Lisa_w = True
        l"John, If anything comes up, you're free to call me, OK?"
        "I should probably tell her."
        j"..."
        j"Lisa. I have to confess.."
        $ Lisa_m="open"
        l"Confess? What is it John?"
        $ Lisa_m="smile"
        show black:
            alpha 0.5
        show ILOVEYOU:
            alpha 0.5
        with dissolve
        j"Erhm. My computer got infected by a virus last night."
        $ Lisa_m="open"
        $ Lisa_e="up"
        $ Lisa_eyes="raised"
        l"A Virus! You too?"
        j"The ILOVEYOU Virus. Have you heard of it?"
        $ Lisa_m="frown"
        $ Lisa_e="mad"
        l"Of course. The ILOVEYOU Virus is a legendary program!"
        j"My computer is... alright, and functional. For some reason."
        $ Lisa_e="normal"
        l"Ehhh? That's good then!"
        j"Actually, if I remember correctly, It was an e-mail from you yesterday."
        l"My e-mail? I didn't send--"
        j"No doubt.. It's the virus that did it."
        l"Ah, that's it. My PC got infected too."
        j"I see. Hilbert's PC as well. His PC didn't recover though, unlike mine."
        $ Lisa_eyes="open"
        l"Did you notice anything odd?"
        "Something definitely was super odd."
        j"An AI person appeared on my screen and introduced itself as the virus."
        j"The AI virus signed herself up to be my assistant, and told me to call her \"ILY\""
        $ Lisa_m="open"
        $ Lisa_eyes="raised"
        l"No way! "
        extend "You're kidding!"
        scene black with dissolve
        play music "bgm/Sunset_bgm_maoudamashii_acoustic42.mp3" fadeout 1 loop
        "How serious can it get? The whole AI virus fiasco is unbelievable."
        "I explained the whole story to Lisa."
        "I told her about ILY, how she's a FAI Virus, living in the GRID and made to fight Softwars."
        "She gets more curious after every bit about ILY."
        $ Lisa_m="frown"
        $ Lisa_e="mad"
        $ Lisa_w = False
        $ Lisa_eyes="open"
        scene cafetable
        show Lisa
        with dissolve

        l"John! You have to let me see the AI virus you got last night!"
        j"How am I supposed to do that?"
        l"Invite me to your house!"
        $JohnSprite('frown')
        j"Huh? That'd pose a few problems."
        l"I wanna see it!"
        j"I'll take a screenshot when I get back."
        l"That won't do! "
        extend"Put it this way, John."
        l"If the AI you got is the brain of the virus attacks from last night,"
        extend" maybe we can beg it to surrender its attacks and repair the damages."
        $ Lisa_m="smile"
        $ Lisa_e="normal"
        l"You told me she looked harmless! Maybe she's a kind virus, you know?"
        "A kind virus. Like that'll ever exist."
        j"So you'll beg to her personally?"
        $ Lisa_eyes="closeup" 
        l"I'm gonna talk with her, woman to woman."
        "More like, woman to program."
        $ Lisa_eyes="open" 
        $ Lisa_m="frown"
        $ Lisa_e="mad"
        l"She destroyed my PC. We should grab any chance we see to reset the damages."
        $ JohnSprite('mad')
        j"I wonder how that'd work though."
        j"I mean... I'm not sure how the virus busts the OS now, but based on history.."
        j"The script of the ILOVEYOU virus overwrites files. All of the files, including the meat and potatoes for your OS."
        j"I mean... Her file size was 14.3 gigabytes. Maybe the files are gone forever?"
        $ Lisa_m="smile"
        $ Lisa_e="normal"
        l"We won't know unless we try!"
        $ Lisa_m="frown"
        $ Lisa_e="mad"
        l"You know about Botnet right?"
        "Wow, this conversation brings me back. First year college."
        $ JohnSprite('normal')
        $ Lisa_m="smile"
        $ Lisa_e="normal"
        j"Like, the network of communication for multiple duplicates of the same virus?"
        l"Yes. Maybe if they'd used some kind of system like that, ILY would've been able to keep all the files we've lost."
        "All the files we've lost..."
        play sound "sfx/Damage2.wav"
        extend"including \"G\" and \"H\"?" with Shake((0, 0, 0, 0), 0.5, dist=5)
        $JohnSprite('mad')
        j"Despite being a Virus and all, that'd be really hard to do."
        j"Internet connection and speed aren't guaranteed, especially when the screen's all black with just ILOVEYOU on it."
        $ John_e='normal'
        j"But it might work. The probability in my opinion is just really slim."
        l"Count on her to be a kind virus and hope for the best, John!"
        "She's awfully optimistic about this AI virus girl."
        l"Oh, one more thing... Nick told me something..."
        show black with dissolve:
            alpha 0.5
        "Nicholas. "
        extend"Nicholas Cann. He made most of the work for our previous clients on the same company. We go way back."
        "Nick is the closest guy I have to a brother. "
        "Nick is also a really good programmer, and one of the people I found to teach me a lot of what I know and practice today."
        "Unfortunately though, he quit working with us for some reason."
        hide black with dissolve
        j"What did he say?"
        $ Lisa_m="frown"
        $ Lisa_e="mad"
        l"He has a warning about Salcedo Dev Studio."
        j"What about SDS? Mr. Salcedo is doing an honest job."
        l"Apparently some people from SDS have been hacking against their competitors."
        $JohnSprite('mad')
        j"That's really childish. Are they looking for a fight?"
        l"I'm not sure if it's related to how we received viruses recently, but..."
        j"I don't think I want to get involved in that kind of trouble."
        scene cafeinside with dissolve
        j"If it's at all connected to the virus attack last night, I'd like to know why."
        j"If it comes to something dire between SDS and some other organizatiion.. I don't want to be involved."
        j"Though I can't deny my curiosity on this matter..."
        $Lisa_w = True
        l"Right? Could this trouble be what Nick is talking about?"
        j"Could be. But it's not like we're really \"in charge\" here. Since we're still just interns."
        j"I'll talk to Hilbert about it later, perhaps. So they could deal with it."
        l"I do hope we could get to the bottom of this!"
        $JohnSprite('happy')
        j"... You're so responsible."
        
        j"Alright. Let's get going, I guess."
        scene cafeoutside2 with dissolve
        $ Lisa_m="smile"
        $ Lisa_e="normal"
        l"John!"
        $JohnSprite('normal')
        j"Yeah?"
        $ Lisa_m="frown"
        $ Lisa_e="mad"
        l"I'm really excited to see that AI Virus you got!"
        j"Trust me, she's a total mess."
        l"Don't say that about {i}people you've just met!{/i}"
        "I can say what I want about {i}programs I just downloaded{/i}."
        l"What does your house look like?"
        j"It's an apartment, I live alone."
        l"When we get there, I'll pass over the project files."
        l"You'll just have to continue from where the former project coders left off with last year's bugs in the database side."
        j"Then, after that I'll go implement the new changes from our last meeting, right?"
        l"I placed a really long to do list there so you gotta work on it!"
        play music "bgm/downtime_bgm_maoudamashii_8bit17.mp3" fadeout 1 loop
        scene black with dissolve
        "After our little chat, we headed home... My apartment. Like never before."
        "Here's to hoping it's presentable enough for a girl to see."
        $ okdesktop = True
        scene blue with dissolve
        show Folders
        show ILY with dissolve
        i"Welcome back, John!"
        $ ILY_m='O'
        i"My, I see you have a guest!"
        $ Lisa_w = True
        $ Lisa_m="smile"
        $ Lisa_e="normal"
        l"Ah, Hello there! I'm Lisa!"
        $ ILY_m='smile'

        i"Hi!"
        
        extend" Nice to meet you Lisa! I'm ILY!"
        i"I am now taking the role of \"Virtual Assistant\" for John!"
        i"John's quite something else, bringing a girl back home after a date!"
        $ JohnSprite('mad')
        j"It's not a date! Lisa just came over so we could continue working on our website thing."
        "It'd be much better with a desktop computer around."
        j"Mhh... here she is, Lisa. Meet ILY."
        $ Lisa_m="smile"
        l"ILY! "
        $ Lisa_m="open"
        l"She kinda looks like a virtual streamer don't you think?"
        $ JohnSprite('normal')
        "!!!"

        j"That is true. "
        $ JohnSprite('mad')
        extend"And quite odd."
        j"Ok, uhh..."
        $ JohnSprite('mad')
        extend"We're doing work, so you better behave."
        $ Lisa_m="smile"
        
        l"We're gonna work on our website here, ILY."

        i"Speak over the mic if you need any help, then!"
        l"Yup. Appreciate it, virtual assistant ILY!"
        scene JD_Space2 with dissolve
        "Lisa is in my room. "
        "All she's gonna do here is work on our website database with me."
        "How do I feel about this?"
        "I feel happy."
        extend" It's not that I like her or anything, I just think I'm lucky to have a nice programmer girl as a friend."
        "She's also very reliable and smart."
        extend" The type you don't see just anywhere."
        "She does remind me of an old internet friend I haven't seen in a while.."
        "I have now introduced her to this, one hell of a program."
        "The sudden twist of events urged me to utter these words to Lisa:\n"
        extend "\"I love you\"."
        "Of course, we were talking about the ILOVEYOU Virus, but still."
        "It makes me feel embarassed. I can't even look straight at Lisa now."
        scene JD_Bed3
        show Lisa
        with dissolve
        $ Lisa_w=False
        l"John! I'm plugging in my USB drive."
        $JohnSprite("frown")
        j"Huh?"
        scene blue
        show Folders
        show ILY
        with dissolve
        $ Lisa_w = True

        voice "voice/ILY22C - Giggle.mp3"
        i"You look a little red, John."
        $JohnSprite("mad")
        j"No, I don't!"
        $JohnSprite("normal")
        j"You can place the drive now, Lisa."
        l"There."
        show explorer:
            zoom 0.0 xalign 0.0 yalign 0.0
            linear 0.25 zoom 1.0 xalign 0.2 yalign 0.5
        "Lisa is trying to access her files from her drive while i sit on a corner of my room, trying to fix and hide the messed up stuff."
        $ Lisa_m = 'open'
        l"J-John.. I can't see my files."
        $ JohnSprite('mad')
        j"Wait a sec.. this should solve that.."
        show blackwindow:
            zoom 0.0 xalign 0.0 yalign 0.0
            linear 0.25 zoom 1.0 xalign 0.8 yalign 0.5

        j"How's this?"
        "It's not working.."
        show blackwindow:
            linear 0.25 zoom 0.0 xalign 0.0 yalign 0.0
        show explorer:
            linear 0.25 zoom 0.0 xalign 0.0 yalign 0.0
        $ILYSprite('mad')
        voice "voice/ILY17D - Gasp.mp3"

        i"John! I think I know what's going on!"
        play music "bgm/Pre-Fight_bgm_maoudamashii_cyber01.ogg"
        play sound "sfx/Damage2.wav"
        i"It's a virus from the USB!" with Shake((0, 0, 0, 0), 0.5, dist=5)
        j"You serious?"
        $ Lisa_m = 'open'
        l"What do we do now, ILY?"
        # $ ILY_p = '2'
        i"We'll engage it in a Softwar!"
        play sound "sfx/Damage.wav"
        j"A Softwar? That's crazy! I wasn't ready for this!" with Shake((0, 0, 0, 0), 0.5, dist=5)
        i"Let's go!! I feel that there's a program in danger!"

        $ usb = '2'

        scene battlebg with pixellate
        show battlering:
            xalign 0.5 ypos 0.15 yanchor 0.5
            block:
                rotate 0
                linear 15.0 rotate 360
                repeat
        show curve:
            xpos 0.5 xanchor 0.0 ypos 0.15 yanchor 0.5
        show curve as curve2:
            xpos 0.5 xanchor 1.0 ypos 0.15 yanchor 0.5
            zoom -1.0

        show battleroad:
            yalign 1.0 xalign 0.5
        with dissolve

        show USBchan:
            xalign 0.88 yalign 0.5

        show Trojan:
            xalign 0.8 yalign 0.5  zoom 0.82
        show USBkun:
            xalign 0.12 yalign 0.5 xzoom -1.0
        # $ ILY_p = '0'

        show ILY:
            xpos 0.0 xanchor 1.0
        with dissolve
        uc"Help!!"
        show ILY with move:
            xalign 0.2
        i"Here we are. This is USB GATE AREA 1!"
        play sound "sfx/Damage.wav"
        j"What is this, a hostage taking?" with Shake((0, 0, 0, 0), 0.5, dist=10)
        uk"PLEASE HELP US. The Trojan Virus is gonna overwrite all of the files in the USB!"
        play sound "sfx/Damage2.wav"
        j"What do we do now? Do you shoot it?" with Shake((0, 0, 0, 0), 0.5, dist=5)
        play sound "sfx/Damage.wav"
        j"If you miss, you might hit the program!" with Shake((0, 0, 0, 0), 0.5, dist=10)
        show Trojan with ease:
            xalign 0.6 yalign 0.5 zoom 0.82
        "The Trojan approaches ILY anyway, and here I was getting worried over the threat that the Trojan would harm the poor program."
        "Maybe this Future AI... isn't very intelligent?"
        $ ILY_w = True
        $ okdesktop = False
        $ enemyName = "Trojan Horse"
        scene battlebg
        show battlering:
            xalign 0.5 ypos 0.15 yanchor 0.5
            block:
                rotate 0
                linear 15.0 rotate 360
                repeat
        show curve:
            xpos 0.5 xanchor 0.0 ypos 0.15 yanchor 0.5
        show curve as curve2:
            xpos 0.5 xanchor 1.0 ypos 0.15 yanchor 0.5
            zoom -1.0
        show battleroad:
            yalign 1.0 xalign 0.5
        show Enemy:
            xalign 0.5 yanchor 0.32 ypos 0.25

        with pixellate
        i"John! I need your help! Let's destroy the Virus Together!"
        $ currentcard=(DataSaber)
        show cardflasher:
            xalign 0.5 yalign 0.46
        i"In a Softwar, we use Battleware!!"
        j"A sword?"
        $ ILY_m = 'smile'
        i"The sword is the weapon of the romantic hero!"
        j"How are we going about this?"
        i"I gain 8 bits and 5 cards every turn, each card in my hand will cost Bits."
        i"You choose from those 5 cards which cards to use in a turn."
        i"Once you've expended enough bits, you can Execute the queue of cards!"
        j"I have to call the shots?"
        i"Of course! You're my operator!"
        hide screen Card
        i"After our turn, It'll be the enemy's chance to attack, so let's strike with all the data we have!"
        j"Got it!"
        $ Lisa_m = 'frown'
        $ Lisa_e = 'mad'
        l"Do your best, ILY!"
        # call demo_battle_vs_trojanhorse

        call battlev3(ILY,Trojan) from _call_battlev3
        if playerHP<=0:
            return
        scene blue
        show Folders
        $ okdesktop = True
        $ ILYSprite('smile')
        show ILY with pixellate
        #Finishing Move!
        #ILY Slash!
        $ ILY_w = False
        play music "bgm/Aaa_maoudamashii_8bit29.mp3"
        show USBkun:
            xalign 0.12 yalign 0.5 xzoom -1.0
        show USBchan:
            xalign 0.88 yalign 0.5
        with dissolve
        $ usb = '1'
        i"We did it, John!"
        $ Lisa_e = 'normal'
        $Lisa_m = 'smile'
        l"The little programs are safe!"

        i"Look, it's love at first sight!"
        voice "voice/ILY22 - Giggle.mp3"
        extend " *giggles*"
        $ Lisa_m = 'smile'
        l"It's like they're meant for each other."
        show USBkun:
            linear 0.7 xalign 0.7
            pause .3
            xzoom 1.0
        show USBchan:
            linear 1.0 xalign 0.88 yalign 0.5
        l"The USB driver programs are connected now."
        uc"Thank you for saving us!"
        uk"I have a new partner!"
        uc"Let's get to work."
        uk"We owe you our lives. We'll see you again!"
        hide USBchan
        hide USBkun
        with Dissolve(2.0)
        l"How cute! What do you think, John?"
        $ JohnSprite('mad')
        j"We just fought a file-threatening virus! What are you two so cheery about?"
        play sound "sfx/Damage.wav"
        j"You could've been deleted, ILY!" with Shake((0, 0, 0, 0), 0.5, dist=10)
        i"Nah, that was easy!"
        if playerHP<800:
            j"You did have a hard time! You barely survived with just [playerHP] HP left!"
            play sound "sfx/Damage.wav"
            extend" You were on the brink of erasure!" with Shake((0, 0, 0, 0), 0.5, dist=10)
        else:
            j"Anything can happen in a battle..."
        l"It looks like John cares for you, ILY!"
        i"Care is an important aspect of love!"
        j"I'm only concerned about our assignment, Lisa."
        l"Though... was a bit of fun to watch her fight."
        i"You should be more cheery now that I solved the problem."
        j"Hmph.. You Viruses are troublesome creatures."
        $ JohnSprite('normal')
        j"I'm just glad our files are okay, Lisa."
        l"Let's work on it now!"
        "Alright, "
        extend"finally something more important is happening here,"
        extend" and I assure you, it isn't about Lisa and me."
        play sound "sfx/Damage.wav"
        extend "\nI can finally get back to work!" with Shake((0, 0, 0, 0), 0.5, dist=10)
        extend"\nOr so I thought."
        "Just after I open the folder containing Lisa's files, my phone rings."
        play sound "sfx/sfx_coin_cluster6.wav"
        # $ ILY_p = '0'
        $ ILYSprite('smile3')
        h"John, bro. My second PC just got hacked through my website."
        $ JohnSprite('frown')
        j"Again? This is getting too often."
        h"I also have like, the best antivirus in that PC, too."
        j"You sure all the security programs were active?"
        h"Yeah, they were, and we still got hacked."
        i"Sounds like a FAI attack."
        $ JohnSprite('mad')
        j"We can't rule out the possibility."
        j"Why are you contacting me, then?"
        h"Can you uh... help me out so I won't get hacked again? You're the better computer guy here."
        l"John, I think this calls for another..."
        i"Softwar!"
        i"We'll find those hackers and fight them ourselves!"
        stop music fadeout 1
        j"No!"
        play music "bgm/Relieve_bgm_maoudamashii_acoustic52.mp3"
        j"ILY, I don't want to be a hacker."
        j"If there's a way to avoid Softwars... I'll take it."
        $ILYSprite('frown')
        i"Why, John?"
        j"You don't understand."
        j"This isn't some kind of game."
        extend" And even if we had to, you're a virus."
        j"The only thing you're good at is destroying computers."
        j"Nothing good can come out of us destroying other people's livelihood."
        j"What's gonna happen next is that they'll come after us for revenge."
        extend" And it'll never end."
        voice "voice/ILY18 - No.mp3"
        i"No..."
        $ Lisa_e='normal'
        $ Lisa_m='frown'
        l"John..."
        "This must be it. This is what Nick warned Lisa about."
        j"I can't afford to lose this computer."
        j"I've already lost a lot in my life. The last thing I want to get in is a fight."
        l"John, we were gonna tell ILY about our proposal, right?"
        j"..."
        $ Lisa_m='smile'
        l"ILY, is there anything you can do about the computers you've destroyed?"
        $ Lisa_m='frown'
        l"Would you, by any chance have a backup storage for all the files you took from us?"
        j"Lisa..."
        i"That's a request, isn't it?"
        "How could Lisa be so nice to the virus that destroyed her PC?"
        j"There's no way. The equivalent is too high in gigabytes."
        j"You couldn't have uploaded THAT much to your botnet in just one night."
        stop music fadeout 1
        $ILY_e='normal'
        i"Hmph..."
        # $ILY_p='2'
        $ILY_m='smile3'
        $ILY_e='down'
        play music "bgm/ost/ILY's_Theme_game_by_Jan_Hehr.mp3"
        i"\"Just who the hell do you think I am?\""
        l"That's an unusual line.."
        j"Did you look into my anime collection?"
        i"FAIs are really quick, so yes."
        # $ILY_p='1'
        i"As for your request, Lisa... The answer is yes! I did save the files from my vicitm's computers."
        # $ILY_p='0'
        j"Wait, does this mean you can really return the files you stole?"
        $ILY_m='frown'
        play sound "sfx/Damage.wav"
        i"I didn't steal them!" with Shake((0, 0, 0, 0), 0.5, dist=10)
        i"I kept them safe in my online database! What's the word... backup! I made a backup!"
        j"That's... kind of the same thing."
        $ Lisa_m='open'
        l"Kept them safe from what?"
        $ILY_m='smile3'
        i"Well, you see, among viruses, I am special."
        i"I heard there would be an attack around the people from \"SDS\"."
        i"So I sent myself to their e-mails, and attempted to get to all the members."
        i"I'll have to say, I didn't conquer the world this time."
        j"What are you saying... You mean, you were expecting Hilbert's PC to be attacked today?"
        i"Yes. I kept the PC's inactive so they can stay safe from the incoming attack."
        i"It's such a shame that I didn't get to that one PC of Hilbert though."
        j"Hold on, I don't understand."
        "What the heck. This virus..."
        j"It's like, ILY burnt down a part of the forest so the prevailing wildfire won't spread..."
        $Lisa_m = 'smile'
        l"That's one way to put it, John."
        j"Hold on.. Can you show the files... now?"
        i"Your files?"
        $JohnSprite("frown")
        j"No no no!!"
        $JohnSprite("mad")
        extend" Lisa's."
        "I'll be in huge trouble if she shows {i}my{/i} files...!"
        i"Sure thing, but we have to connect to the internet first."
        j"Hmph. Don't do anything suspicious."
        # $ILY_p='1'
        i"Don't worry John, I won't."
        show screen notifwindow("{color=000}Connected to the Internet.{/color}")
        j"You're connected now. Show us!"
        hide screen notifwindow
        # $ILY_p='2'
        i"Well then, let's begin!"
        i"HEART DRIVE ACTIVATE!"
        $okdesktop = False
        scene white with dissolve
        $ILY_w = True
        i"Initiating access to ILY database..."
        i"Access{w=.3} Granted."
        i"Retrieving data{w=.5}.{w=.5}.{w=.5}."
        l"My files!"
        "Well what do you know.. She was right."
        scene JD_PC1 with dissolve
        l"Hey what's this, I think we got Hilbert's files too!"
        $Lisa_m = 'frown'
        l"Oh my, this is a movie I haven't seen!"
        $ Lisa_m='smile'
        l"John, I'll be copying this to my hard drive, okay?"
        j"Go on..."
        $JohnSprite('normal')
        j"ILY... I don't believe it..."
        i"Well, what I really did there was disable their use of their computers, so it wasn't that hard!"
        i"Do the impossible, see the invisible, right?"
        j"Stop quoting from my favorite anime."
        i"I'm more than just a PC destroying virus now, aren't I?"
        # $ILY_p = '1'
        "Why would a virus do this? This is beyond crazy."
        "Moreover...  Who made her to be this way?"
        # $ILY_p = '0'

        j"With this, do you propose to stop further attacks to Hilbert and SDS?"
        i"Now that you're convinced that we have the files safe with me..."
        $ILY_m = 'smile3'
        extend"Allow me to explain."
        scene JD_Bed3 with dissolve
        $ ILY_m="frown"
        i"Right now, if we reconnect Hilbert's computer to the internet, as well as the other members of SDS..."
        $ILY_m = 'smile'
        i"I will be able to recover their data and give back their computers' lives."
        j"We'll have to tell them to fix their hardware up and try connecting, now don't we?"
        l"I'll call Hilbert now!"
        scene black with dissolve
        stop music fadeout 1
        "Lisa walks next to the window to make a call."
        "Hilbert Salcedo."
        extend" The next leader of SDS, our classmate, and the man who lives right next to our server."
        "If anyone had the ability to mess up the whole SDS company, It'd be anyone that has access to Hilbert's data."
        "It totally makes sense how he's the one being hacked right now."
        "Lisa had now prompted Hilbert to reconnect their computers..."
        scene JD_Space2 with dissolve
        play music "bgm/Enemy_bgm_maoudamashii_cyber19.ogg" fadein 1 loop
        $ILY_m = 'frown'
        i"I've received traces of data left from the attacking virus."
        i"This virus has destroyed a total of 7 websites and servers from SDS now."
        j"Do you have data on what virus it is?"
        i"Based on the way it moves, I'd say it's a worm."
        i"You should see the website you guys made with Hilbert."
        j"What's up with it?"
        $ okdesktop = True
        scene blue with dissolve
        show Folders
        # $ILY_p = '0'
        $ILY_w = False
        show ILY with dissolve:
            xalign 0.78
        show redwebsite:
            xalign 0.0 yalign 0.0 zoom 0.0
            linear 0.2 xalign 0.4 ypos 0.07 yanchor 0.0 zoom 0.9
        "There it is..."
        extend" It says our website is... \"Hacked By ...\" -What?"
        "Where have I heard or seen this from before?"
        show redwebsite:
            linear 0.2 xalign 0.0 yalign 0.0 zoom 0.0
        "I take a moment to think about what we can do to keep SDS websites active without sacrificing Hilbert's computer usability..."
        hide redwebsite
        "If the virus attacks are made by a FAI Virus now, then we'll need... that!"
        play music "bgm/downtime_bgm_maoudamashii_8bit17.mp3" fadein 1 loop
        $ILY_m = 'smile3'
        show ILY with move:
            xalign 0.5
        j"ILY, didn't you say that there were FAI antiviruses?"
        #$ILY_p = '1'
        i"Yes, I did say."
        j"Where do we get one?"
        $ILY_m = 'frown'
        #$ILY_p = '0'
        i"No, John."
        $ILY_m = 'smile'
        #$ILY_p = '2'
        extend" The proper question is \"Where do we {i}befriend{/i} one?\"."
        $ILY_m = 'smile3'
        j"... Okay, whatever."
        i"Remember, John. FAIs are people too!"
        #$ILY_p = '0'
        j"Sure. So where do I, er.. {i}befriend{/i} one?"
        $ILY_m = 'frown'
        $ILY_e = 'up'
        i"You're gonna install an antivirus here?"
        j"No. This is for Hilbert and SDS."
        "Alright. If this world has come to an age where antiviruses have to fight Softwars just for security..."
        "Then I'll have to roll with it. "
        extend"Best to keep protected."
        "We don't have to be the attackers here. Installing FAI antiviruses will be perfect."
        l"John, Hilbert told me he's on to recovering all the office computers."

        j"Do as you promised, ILY. We need SDS to be active."
        $ILY_m = 'smile3'
        $ILY_e = 'normal'
        i"Gotcha. As soon as they reconnect, they should be able to run their computers fine."
        i"I've turned off the switch that disables any inputs from the user."
        j"So that's all it was all this time?"
        $ILY_m = 'smile'
        $ILY_e = 'up'
        i"Yep."
        l"So, what do we do about the incoming attack, John?"
        $ILY_m = 'smile3'
        j"Here's the plan. FAIs are the next generation Artificial Intelligence programs for hacking now."
        j"If it's true that the impending attack is by a FAI virus..."
        j"Then the only way to counter it properly is by using a FAI antivirus."
        l"Do you have any idea where we can download one?"
        $ILY_m = 'frown'
        $ILY_e = 'normal'
        i"The correct term is \"befriend\", OK?"
        j"I was just asking the same thing to ILY, Lisa."
        $ILY_m = 'smile3'
        $ILY_e = 'up'
        l"Ah. so ILY... where do we {i}befriend{/i} one?"
        i"That's..."
        $ILY_m = 'frown'
        $ILY_e = 'normal'
        extend" I really don't know."
        i"FAIs are really hard to come by, being hidden and all, they return mismatches from searches."
        "FAIs are THAT rare? no matches in Googz?"
        j"..."
        j"Damn."
        "This is a dead end. I don't want to lose my job, dammit. We gotta find one somehow."
        $Lisa_m = 'open'
        l"Ah... John!"
        $Lisa_w = False
        $Lisa_m = 'smile'
        $ okdesktop = False
        scene JD_Bed3
        show Lisa
        with dissolve
        j"Lisa, got any clue?"
        l"I just might know where to get one..."
        $Lisa_m = 'smile'
        l"Recently..."
        $Lisa_m = 'frown'
        $Lisa_e = 'mad'
        extend" ummm.."
        l"M-my dad has been speaking with this AI! "
        $Lisa_m = 'smile'
        $Lisa_e = 'normal'
        extend"She sounded like a FAI, just like ILY!"
        j"Really?"
        "Right, Lisa's dad would know such a thing. He does lead their own Cyber-security business."
        $Lisa_e = 'mad'
        $Lisa_m = 'frown'
        l"Um, I'll go ask my father if I can grab a copy!"
        $ILY_w = True
        $ILY_m = "smile3"
        j"Hmmmm... Could it be?"
        j"If it really is a FAI Antivirus, that'd be a jackpot."
        i"Lucky!"
        $Lisa_m = 'smile'
        $Lisa_e = 'normal'
        l"Yeah, I guess I am lucky!"
        "Alright. I guess I can count Hilbert's problem as solved now.."
        "It's finally time to work on the assignment now, right?"
        j"So, now that SDS and Hilbert's problems have been dealt with for now, can we finally work on our assignment?"

        l"Sure, John! The side quests are over."
        j"Alright then."
        $Lisa_w = True
        scene JD_Space1 with dissolve
        "This is the main event. We can finally get something done now!"

        "I can feel it. No more interruptions this time."
        "To assure this, I must require ILY to shut up, so I can focus."
        i"You look like you're in deep thought. "
        extend"Is there anything I can do to help?"
        "What great timing."
        j"I need you to refrain from bothering me, ILY."
        $ILY_m = 'smile3'
        i"Oh, okay."
        "That was quick."
        $John_m = 'smile'
        j"Let's get to work."
        l"Here's my work so far."
        "Lisa shows me her handiwork from her USB."
        l"The server-side fetching of data hasn't been implemented yet, so I was hoping you could help on that."
        j"I see."
        "I've worked on web applications like this before, so this should be a piece of cake."
        j"Give me a few minutes, I'll add in the GET and POST request scripts for this part."
        l"I'll help out on the front-end side while you're working."
        "Lisa and I have become indulged in coding for the website."
        #
        scene black with dissolve
        play music "bgm/Sunset_bgm_maoudamashii_acoustic42.mp3"
        show John with dissolve:
            xalign 0.5
        "As I thoroughly edit through my messed up code, I think carefully about the recent, and upcoming events."
        "Today, I've been dragged into a mess involving the company I work in."
        "This assistant virus, while very interesting, has increased my concerns in life, and stress."
        "She's willing to help us out with the hacking problem against SDS, so I guess she's not too bad."
        "Tomorrow will be when we assess if we can keep the website active without risking server shutdown."
        "I'm still curious whether Lisa's father really holds a FAI."
        "If we manage to acquire a FAI antivirus, let's hope it's strong enough to protect SDS."
        "Now, I think the server side is good to go. {w}The website server is ready."
        "Time to show Lisa."
        scene JD_Bed3 with dissolve
        $ILY_w = True
        $Lisa_w = True
        j"I'm done here, Lisa!"
        l"Oh, Let's see!"
        i"I helped out well, didn't I, John?"
        j"Thank you for not bothering me."
        l"Let's see... Hmmm~ Hm~!"
        "I spent about an hour on that one."
        scene JD_Kitchen with dissolve
        "While Lisa checks the functionality of my database code, I stand up from the computer chair and get a drink."
        "Lisa's gonna need a gulp too."
        scene JD_Bed3 with dissolve
        pause 1.0
        scene JD_PC2 with dissolve
        l"What's this? Why is it in a bowl?"
        j"It's water. "
        extend "I... don't have cups."
        i"That's weird, John!"
        l"Hmmm. I think it's smart! Thanks, John."
        "Lisa gulps it down quickly and then replies."
        l"Bowls can double as plates for food, and cups to drink from."
        l"It's a way to reserve energy having to wash plates and cups."
        l"Living alone, you won't have to deal with a lot of extra chores this way."
        "I am so glad I didn't have to explain it!"
        j"Waugh.."
        $ Lisa_m = 'frown'
        l"Did I get it wrong?"
        j"You're right, Lisa, glad you understand."
        "In my head, I want to hug her."
        l"If you... Didn't want to be bothered with many plates..."
        $Lisa_e = 'mad'
        l"That kind of makes me think that... You aren't ever expecting guests to come here."
        $John_m="frown"
        j"!!"
        "She just sees through me, reading me like an open book."
        $ Lisa_e = "normal"
        $ Lisa_blush=True
        l"M-maybe that should change!"
        $Lisa_e = 'mad'
        $ Lisa_m = 'frown'
        l"Being a loner isn't a good thing!"
        "..."
        extend "She's right."
        $JohnSprite('mad')
        j"You're right... I'll... think about it!"
        $ Lisa_m = 'smile'
        $ Lisa_blush=False
        scene black with dissolve
        pause
        scene JD_PC2 with dissolve
        l"About your code..."
        l"It's pretty well done. I didn't encounter any bugs."
        $JohnSprite('normal')
        j"That's relieving to hear."
        $Lisa_e = 'normal'
        l"It's your work, after all!"
        l"Well, here are my improvements to the website design."
        j"This looks so much better than before, Lisa."
        j"Well done."
        l"We did great today."
        "Agreed. She's really a genius."
        l"That was really fun."
        l"I guess that's one of our assignments down!"
        j"You're gonna have to go home for now."
        $Lisa_e = 'normal'
        l"For now?"
        j"Ah.. I meant.. We'll have to meet again tomorrow, right?"
        $Lisa_m = 'smile'
        $Lisa_e = 'normal'
        l"O-of course!"
        $Lisa_m = 'frown'
        $Lisa_e = 'mad'
        l"John! You have to finish it! Finish our assignment!"
        l"Remember the to do list I put up from the files in the USB?"
        j"Got it. 1 feature down, 2 more to go."
        $Lisa_m = 'smile'
        $Lisa_e = 'normal'
        l"See ya again."
        $ILY_e = 'up'
        $ILY_m = 'smile'
        $ILY_w = False
        $Lisa_w = True
        $ okdesktop = True
        scene blue
        show Folders
        show ILY
        with dissolve
        play music "bgm/downtime_bgm_maoudamashii_8bit17.mp3" fadeout 1 loop
        i"John, did you say you wanted your files back earlier?"
        "What is it now, ILY?"
        l"Oh right, You lost files too!"
        $ILY_m = 'smile3'
        i"I made a backup of them just in case!"
        $JohnSprite('mad')
        j"ILY, stop! Don't show Lisa!"
        "At an instant, I turned the PC monitor off through the switch."
        $ILY_w = True
        $Lisa_w = False
        $Lisa_m = 'smile'
        $ okdesktop = False
        scene JD_PC2 with dissolve
        i"Hngu- What's going on, the screen's all black!"
        j"Bugger off."
        scene JD_Door
        show Lisa
        with dissolve
        $Lisa_m = 'frown'
        $Lisa_e = 'normal'
        l"Eh?"
        $JohnSprite('normal')
        j"That was nothing."
        $JohnSprite('mad')
        extend" Don't mind her."
        $JohnSprite('normal')
        j"You should go home before it's late, Lisa."
        $ILY_m = 'frown'
        $ILY_e = 'down'
        i"Turn it back on, John! I wanna wave goodbye!"
        $Lisa_m = 'smile'
        l"Hahaha! Bye ILY!"
        extend" Thanks, John."
        j"We still have more to do."
        j"Thank me another time."
        l"See ya!"
        play music "bgm/Cafella_bgm_maoudamashii_acoustic51.mp3" fadeout 1 loop
        i"I think you should send her back, John!"
        "ILY... stop it!"
        $Lisa_m = 'frown'
        $Lisa_e = 'normal'
        l"Will you come back with me outside?"
        $JohnSprite('mad')
        j"Fine,"
        $JohnSprite('normal')
        $Lisa_m = 'smile'
        extend" just until the street where you can commute home."
        l"Around Cafella! Good."
        scene black with dissolve

        "Thus we took a walk... we reached Cafella."
        "This kind of thing is gonna happen again tomorrow, it seems."
        scene cafeoutsideaftern with dissolve
        show Lisa with dissolve
        l"Thanks again, John. I had quite a bit of fun today."
        j"Anything for work."
        hide Lisa with dissolve
        "She waves and crosses the street."
        extend" She smiles at me as she hails a ride."
        "We're gonna meet again tomorrow."
        "And perhaps, next week again, if work allows."
        "Am I looking forward to it?"
        extend" Maybe so."
        "Hold on..."
        "Did I...?"
        "I didn't."

        play music "bgm/Enemy_bgm_maoudamashii_cyber19.ogg"

        $ okdesktop = True
        scene blue with dissolve
        show Folders
        #$ILY_p = '0'
        $ILY_m = 'smile'
        $ILY_e = 'normal'

        $ILY_w = False
        show ILY at sidesteps_effect("ILY", 0.5, 0.1, 0.25):
            xalign 0.5 
        i"Waaaahh! I'm free!!"
        hide ILY
        $ okdesktop = False
        scene black with dissolve
        "That's right. I didn't turn off the PC!!"
        $ILY_w = True
        scene JD_Door with dissolve
        i"Who's there? Is that you, John?"
        scene JD_Bed3 with dissolve
        pause 0.5
        scene JD_PC2 with dissolve
        $JohnSprite('mad')
        j"Oh it's me, alright!"
        i"Welcome back John! How's it going?"
        j"Don't \"How's it going\" me! "
        extend"What have you been doing on, and online?"
        i"I was um... Exploring the GRID!"
        "No... I'm sure she's started sending my coordinates so a secret organization can recruit me for evil things."
        "Dammit. How could I let this slip by?!"
        i"I'll show you! Switch the monitor on!"
        j"What is it?"
        $ILY_m = 'frown'
        play music "bgm/ost/ILY's_Theme_game_by_Jan_Hehr.mp3"
        i"If you're thinking that I contacted my evil hacker creators, I'll destroy this PC!"
        "..."
        j"Fine."
        #$ILY_p = '0'
        $ILY_m = 'smile'
        $ILY_e = 'normal'
        label map_phase_chapter1:
            python:
                gridpos = [192,168]
                maptalks = 0
                maptalks2 = 0
                enemy_encounter = False
                boxsheet = stagehome
                playerpos = [7,6]
                playerxpos = playerpos[0]
                playerypos = playerpos[1]
                objxanchor = ((playerpos[0]+1)*blockSize)-(blockSize/2)
                objyanchor = ((playerpos[1]+1)*blockSize)-(blockSize/2)
                direction = 'down'
                for sprite in spritelist:
                    boxsheet[sprite.position[1]][sprite.position[0]]=sprite.dialogue
        call addsprites(gridpos) from _call_addsprites
        # call mapcall([7,6],stagehome)
        # scene blue with dissolve
        scene battlebg
        show scrollingBG at scroll
        show screen mapB
        i"This is the GRID!"
        i"Listen John, and listen carefully!"
        j"Gotcha."
        i"Basically here is where we are in the grid. Our home location, (192,168)!"
        "The GRID cyberspace huh.. So it follows a cartesian plane system."
        j"It's so empty.. what do we even do in here?"
        i"Lots of things. But I'm not going to spoil!"
        j"What?"
        i"You're gonna have to come with me!"
        j"O-kay.."
        i"So let me give you a tutorial."
        j"I get it. Arrow keys for movement, 'Z' for action, probably triggers stuff like, talking to NPCs and getting items, right?"
        $ ILY_m = 'O'
        i"How did you know?!"
        j"Humans are an intelligent species."
        $ ILY_m = 'smile3'
        i"Well, in addition to that, You can talk to me anytime by pressing 'X'."
        j"Okay."
        
        j"There's one thing I am curious about since this crossroad area resembles the one we have IRL."
        i"IRL?"
        j"Could it be that we can find a path to SDS using this GRID?"
        i"You mean using its geological location?"
        j"Yes. to the west of here, approaching Connecht Square, we can get to my internship office."
        i"There's one way to find out!"
        j"Alright, let's explore the area then."

        ## TODO: Make Mission/Quest Screen
        "Mission: Direct ILY to the West Area until you reach the \"Connecht Square\""


        jump script1_2
