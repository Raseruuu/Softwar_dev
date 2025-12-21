# """    Outline
#      Feb 18th (Tuesday)
# School Section.
# Insert John’s thoughts on Hacker X incident.
# Submit their internship 
# After Code Red incident John alone decides to take on the initiative, trying to get info about their mystery attacker.
# Free Roam to investigate about Code Red.
# reveal that ILY was able to take location data from her fight with Code Red.
# Location data only supplies limited information of Red’s steps in the GRID.
# Break Time
# John calls Alicia 
# Feb 19th
# The team chills at school and thinks about what to do next.
# Funny slice of life moments with Hilbert, John and Lisa.
# John is continuously curious about Hacker X
# Free Roam:
# Possibly using Vira’s help, ILY discovers and approaches Hacker X’s network
# Ave is intercepting ILY’s attack with Sniping
# ILY looks to the direction where bullets come from and pushes through
# John’s party is dumbfounded at meeting Ave. This was supposed to be Hacker X’s and Code Red’s territory, but an Antivirus is here.
# John pieces together that the owner of Ave, and the owner of Code Red are the same person.
# Battle Ave
# ILY draws her blade. This makes Ave extremely angry.
# Emotional battle with an evident grudge from Ave. 
# ILY is able to escape deletion
# """    
# ###
label script3:
    call hideMapview
    
    "After defeating Ave, she agreed to report to Nick and ask him to meet us."
    "However, we've been waiting for nearly thirty minutes now and he still hasn't arrived."
    l "Maybe he's not coming." 
    j "You might be right."
    l "How long have you known Nick?"
    j "Ages but we lost contact after Alicia took me in."
    l "Were you good friends in the orphanage?"
    j "More than that, we were like brothers."
    l "I wonder why your supposed brother would hide something like this from you."
    j "Yeah, me too."
    "Suddenly the doors to the cafe fly open."
    "I offer him a smile but all I receive in return are a pair of daggers."
    "He slowly makes his way over and takes a seat opposite Lisa and me."
    j "Nick! It's good to-"
    n "Let's make this quick. I have places to be."
    "Lisa looks at me with concern in her eyes."
    j "Nick...I just need to know..."
    j "Why did you hide your identity as Hacker X from me?"
    n "Like you don't know already…"
    n "I've spent my entire life trying to surpass you."
    j "Nick...I thought we were friends."
    n "Maybe we were."
    n "Maybe all those days we spent programming together as kids were real."
    n "Or maybe it was all just a lie!"
    "Nick slams a fist down onto the table."
    "We recoil in surprise." 
    n "After you were adopted, it's like you forgot all about me."
    j "That's not true! I-"
    n "Liar!"
    n "I would always beat you at sports and video games…"
    n "Even programming; we started out as equals…"
    n "But after a few short months you had already surpassed me."
    n "I had no problem playing second fiddle to your lead guitar."
    n "That's what friends are for, after all."
    n "Truthfully, I was amazed by your skill. I wanted nothing more than to program with you."
    n "But when you left...I had no one to play backup for anymore."
    "Nick goes silent."

    # Menu: 
    menu:
        "What should I do?"

        "Apologize.": 
            j "I had no idea you felt that way."
            j "I admit, after I was adopted, it felt like I hit restart on everything that had happened before."
            j "I still don't remember my life before the orphanage."
            j "But I do remember the warm feeling I get when I'm with you."
            j "You and Alicia filled that empty space in my heart."
            j "But I didn't think how distancing myself from you would make you feel."
            j "I was selfish and I apologize."

        "Explain myself":

            j "I felt lost for so long in that orphanage."
            j "Being told my parents had died but not remembering a thing about them…"
            j "There was a void in my heart that couldn't be filled."
            j "After I was adopted, it rebooted my entire life."
            j "You were there for me in the orphanage and our experiences were as real as the glasses on my face!" 
            j "I admit, we don't talk as much anymore and I apologize for that."
            j "But I never forgot about you!"

    n "Nothing you say can change things."
    n "I always walked in your shadow."
    n "Before, it was cool, like the shade from a tree on a summer afternoon."
    n "Now, I can see that it was nothing more than a well of darkness used to mask your true intentions."
    j "True intentions?"
    n "You're working with the ILOVEYOU virus."
    n "Or if not you...someone from SDS is." 
    n "I have spyware located all over GRID."
    n "Code Red and I can find you wherever you run."
    l "Nick, you misunderstand us. ILY is-"
    n "A deadly virus that needs to be terminated."
    n "Not content to spend my life walking behind you, John, I decided to take matters into my own hands."
    n "I honed my programming skills, landed a job at a leading antivirus company, and began my first assignment."
    j "That is?"
    "Nick leans back in his seat and glares at us."
    n "The ILOVEYOU virus that you control is nothing but a copy."
    n "The real virus is still out there somewhere—fragmented into thousands of individual pieces."
    n "Something is using these fragments to infect programs and mass-produce mini FAIs."
    "Lisa leans into my ear."
    l "Like the ones we fought before!"
    n "I will track down those ILOVEYOU fragments, destroy them, and surpass you, John!"
    "Nick stands and throws a finger in my general direction."
    n "I will become the greatest hacker to ever live and finally release my grip on your coattails!"
    "Lisa and I look at each other." 
    "We start chuckling and recline in our seats."
    l "What a relief!"
    j "You can say that again!"
    "Nick's finger goes flaccid."
    n "Wh-wh-"
    n "WHY AREN'T YOU GUYS MORE INTIMIDATED?!"
    j "You've got it all wrong!"
    l "Yeah, ILY's a good virus."
    n "Please, there's no such thing."
    j "What about Code Red? He's a virus under your control, right?"
    n "That's because I spent weeks training him!"
    j "Weeks?"
    l "Didn't it only take you a few hours to tame ILY, John?"
    "Nick sits down, his head falling into his palms."
    n "So, after everything, I'm still in second place, huh?"
    "Although he came across a little abrasive, this is still the same Nick I know."
    "I can feel the faint sparks of a long-lost kinship reigniting inside me."
    "I look at Lisa and she shoots me a large toothy grin."
    "Placing a hand onto Nick's shoulder, he looks up teary-eyed."
    j "We're investigating what's happening to the infected programs as of late."
    l "ILY thinks the internet might be in danger."
    n "And what do you want me to do about it?"
    j "Code Red and Ave are strong but they're even stronger with you at the helm."
    "I hold out my palm."
    j "We could really use someone with as much skill as you to help us!"
    j "What do you say? Let bygones be bygones?"
    "Nick looks at my hand before sighing."
    n "Looks like I don't have much of a choice."
    "Nick firmly shakes my hand and we share a smile."
    n "I see you're even beating me in the girlfriend department."
    "He gestures to Lisa."
    n "How did a guy like you get a girl like her?!"
    j "G-g-g-g-g-girlfriend?! She's not...I mean...we're not…"
    l "Right! I like John...a lot...but…"
    l "Ah! What am I saying?!"
    "Nick smiles and bursts out laughing."
    n "You always did know how to put a smile on my face."
    n "Looks like we're in for one wild ride now, doesn't it?"
    "Nick puts his fist into the center of the table."
    "Lisa and I place our own fists on top."
    "We smile at him but he looks away."
    n "I...look forward to working with you..."

    
    return
