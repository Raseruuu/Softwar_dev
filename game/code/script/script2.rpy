
label prescript2:
    $map_active=False
    hide screen mapB
    ""
    "STUFF"
    #Call Scene after approaching tile on Connecht, North of Home area
    j"ILY, when you talk to an entity in there, they won't actually hear me right?"
    i"Yeah, they won't."
    j"That's a relief."
    i"I can also whisper to you when I'm in front of them, and they won't know."
    j"Sounds good."

    #John thinks to himself about the Grid
    "So this is what the GRID's like."
    "The shape of this map... it feels awfully familiar."
    "A highway next to a \"Cafe\"..."
    "residential area down south, a tall building just around a crossroad, a monument at the center of a rotunda road..."
    "It almost exactly resembles the area near my place, but the components are different."
    "There aren't any cars, not as much people, and no actual stores or restaurants. What would you expect from a cyber town?"

    ##Arrived at a checkpoint: meet Melissa

    i"John, Here's the new friend I told you about!"
    "A fellow humanoid avatar."
    "So far, there have been a few humanoids passing by, just like ILY. I wonder what's so special about this one?"
    j"Is she a FAI?"
    i"She is."
    j"I see. What kind of FAI is she?"
    i"(I'm actually not sure myself.)"
    i"(But she does know a lot about the area.)"
    i"(Her name's Melissa!)"

label script2:
    #ILY introduction to the Grid
    #ILY strolls around their own personal cyberspace area:
    # There are a few Mini FAIS hanging around, representing computer systems inside his own device.
    # Explanation of Mini FAI


    show Melissa:
        xalign 0.5
    m"Hi there, ILY. Welcome back to the GRID."
    i"Hey Melissa!"
    "I'll have to say.. this FAI is looking quite... fashionable."
    j"Can you ask her about for directions?"
    j"I'd like to confirm something."
    j"We need to find the SDS area."
    "the GRID world is directly basing their maps on real-life locations... I wonder why?"
    "If my guess is right, then I will be able to find the road to SDS."
    i"Can you show me around?"

    m"Sure thing, let's exchange info for info. What are you up to?"
    i"I'm just exploring."
    m"Exploring? Are you perhaps... looking for a {i}victim{/i}?"
    i"No! I'm not!"
    m"*Smiles*"
    j"She knows that you're a virus?"
    i"(Ehhehehe..)"
    i"(Actually, She's... also a Virus.)"
    "A FAI Virus just like ILY? How rare is it to meet one?"
    j"(ILY! that's dangerous!)"
    m"What are you seeking?"
    i"I'm doing my master's business. I'm his cyber assistant."
    j"(ILY, I really have a bad feeling about this! And about this friend of yours!)"
    m"Hahaha! That's interesting. You're a Virus, with a human master?"
    m"In this world you will find that most of the viruses are like me."
    m"I am free to roam, anywhere, any time. You could call me a Stray."
    j"(ILY, We should go back.. I... really don't wanna interact with another Virus.)"
    i"(But we need to find SDS!)"
    i"(She's the only person around I can relate to...)"


    #Approaching a road blocked by Antiviruses: Bitwulves
    m"Watch out, they're on patrol on these hours."
    m"I'll walk ahead of you and take a peek."
    i"??"
    # Melissa returns
    m"It's a dead end here.."
    m"It's Bitwulf. An Antivirus. They've made it their job to look for Viruses and fight them in Softwars."



    #After this, John decides to review the day in his head and go to sleep.

    #Morning

    #E-mail from Lisa appears
    i"John!! You have 1 new unread e-mail! It's Lisa!"
    "Huh... Right. We were together yesterday..."
    "I wonder if it's true that her dad has a FAI Antivirus?"
    j"Please open it, ILY!"
    i"OK!"
    #(change to lnvl) for e-mail view
    #Show NVL window
    l"Subject: Update on Antivirus!"
    l"John!! I got my dad's Antivirus!!"
    l"Her name is Vira! From Vira Internet Solutions!"

    l"As I suspected, she was really a FAI Antivirus!"
    l"I'm going to your place today."
    l"We have to install her as soon as possible!"
    #nvl hide


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
    h"Were you... gaming just now?"
    h"Sorry to bother you man."
    j"Yeah I lost a PVP match. Dang it."
    i"No, John didn't just lose a match."
    "..."
    h"Who was that?"
    j"Nobody."
    i"I'm ILY! Nice to meet you!"
    h"Woah what? Is that from your PC?"
    h"Are you in a voice chat? oh man I'm sorry to butt in bro."
    j"Yeah. voice chat."

    i"This is not a voice chat."
    i"I am John's personal assistant AI. ILY!"
    j"No no no.. stop that. Don't introduce yourself!"
    h"Assistant AI?"
    h"That's super cool man!"
    j"No, it's not super cool."
    h"But like, she can talk, right?"
    "Hilbert moves closer to my computer."

    #Transition to ILY screen
    h"Hello there, I'm Hilbert, John's best friend!"
    i"Confirmed. You are indeed Hilbert, from John's contacts."
    j"I don't know about \"Best friend\"."
    h"Hey! She recognized my face!"
    j"Yeah, she's pretty high tech."
    h"You've been hiding a program this advanced?"
    # j"Umm, Hilbert, could you be a good visitor and-"
    h"I knew you were a genius when it comes to this kinda stuff."
    j"No, this isn't my AI."
    h"You didn't develop this?"
    j"No. I stopped working on my AI some time ago."
    "I take a seat down and rest my chin on my right hand."
    h"I have so many questions..."
    j"Sit here."
    h"... Okay."
    j"Well..."
    i""
    h"John. it's been crazy lately, hasn't it?"
    h"The virus attack on SDS.."
    j"Is that what you came here for?"
    h"I need your help John."
    ""
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
