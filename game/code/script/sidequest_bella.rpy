define sv = Character("Stray Virus")
define t = Character("Tetra",callback=speaker("Tetra"), color ='#f00',image ="Vira_side", ctc="ctc", ctc_position="fixed")
image Tetra:
    "images/Characters/Tetra/Tetra_v.png"
image side Tetra_side:

    ConditionSwitch(
        "Tetra_w==True","Tetra",
        "Tetra_w==False","Null_side"
    )
    zoom 0.38
label LunarLux_Sidequest:
    $ ILY_outfit ="Uniform"
    $ILY_e="normal"
    $ILY_m="smile3"
    show scrollingBG at scroll
    show battleroad:
        yalign 1.0 xalign 0.5
    show Tetra:
        xalign 0.7 zoom 0.4
    show ILY
    t "Hey! You there! Have you seen a pink-haired girl around here?"
    i "Ah! I found you! You must be Bella's robot partner, Tetra!"
    t "You've... You've seen Bella!"
    
    i "That's right, She had a really cool red space suit, and swirly hair, like Ice Cream!!"
    t "That is her!"
    i "Let's go!"
    t "Wait, who are you?"
    i "You can call me ILY!"
    t "You seem kind."
    i "That's what my name is all about!"
    "Tetra and ILY arrive at Bella's location."

    scene black
    pause 0.5
    show scrollingBG at scroll
    show battleroad:
        yalign 1.0 xalign 0.5
    $ togglechar("Bella",right)
    show ILY:
        xalign 0.2
    show Tetra:
        xalign 0.6 zoom 0.6 yalign 0.5
    with dissolve
    i"We're here!"
    t "Bella!"
    $ Bella_m="smileopen"
    $ Bella_e="normal"
    $ Bella_eyes="open"
    be "Tetra! I've been looking everywhere for you!"
    $ Bella_m="O"
    be "Oh, it's you!"
    t "Tetra found a new buddy, her name is ILY!"
    i "I'm glad you're together now again."
    be "Thank you!"
    $ Bella_m="frown"
    $ Bella_e="normal"
    $ Bella_eyes="open"
    be "ILY, huh.. Could you tell me more about you?"
    i "I'm... a virus! I'm ILY the ILOVEYOU Virus!"
    $ Bella_m="frown"
    $ Bella_e="1up"
    $ Bella_eyes="1up"
    be "You're a virus?? What kind of world is this? "
    be "Those critters attacking me earlier, they were viruses too?"
    $ Bella_e="down"
    $ Bella_eyes="midclose"
    be "So... We're actually still lost."
    i "Huh!? What do you mean?"
    t "We're not from here... Even though the atmosphere is similar to the cyberworld at my place."
    be "This world seems to be a special cyberspace. A Digital Realm."
    i "That's right, you gathered correctly."
    be "And... We seem to be in danger, now that a Virus is right here."
    i "Don't worry!! I won't bite!"
    be "How can we be sure we can trust you?"
    t "Um!!"
    t "ILY helped me find you! So I think that's cause enough to trust her!"
    
    return




























label milk_adventure:
    $ ILY_outfit ="Uniform"
    $ILY_e="normal"
    $ILY_m="smile3"
    scene battlebg
    show scrollingBG at scroll
    show battleroad:
        yalign 1.0 xalign 0.5
    show ILY
    i"According to Melissa, this item can boost my stats."
    i"How considerate of her!!"
    i"I might be able to face some antivirus that decides to chase me if I could get even stronger!"
    i"Time to open it!"
    $ILY_e="up"
    i"... It's a drink?"
    i"I use Energy cans often, but this one looks a bit different."
    i"It looks like milk?"
    "ILY gulps the drink down and quickly finishes every drop of it."
    
    $ILY_e="up2"
    i"u...uguu.."
    
    $ILY_m="frown"
    i"I'm feeling a bit strange."
    scene black with dissolve
    pause
    scene battlebg
    show scrollingBG at scroll
    show battleroad:
        yalign 1.0 xalign 0.5
    
    i"Huh? Where am I?"
    i"What's going on... My chest feels.. heavy."
    $ILY_e="up2"
    $ILY_m="O"
    $ EquipDress("outfit","UniformBig")
    show ILY with dissolve
    "My.. breasts... aaahhh!!! Was it the drink?"
    $ILY_m="frown"
    "My  breasts are so big now.."
    "Oh no..."
    "A stray Virus? No different than me, huh."
    "Now.. Have I been tricked?"
    "But... Melissa said..."
    sv"Would you like to have a part-time job?"
    i"Wha?? Wait, you can talk?"
    sv"Of course I can!"
    i"A part time job?"
    i"I'm not supposed to be here! I have a mission!"
    sv"No! Wait, this job pays well! You can even keep some of your own produce."
    i"What do you mean? My own produce?"
    sv"Yeah, it'll be great, a win-win situation, just spend some time at the farm."
    i"The farm?? There is a farm here at the Connecht GRID?"
    sv"How else do we make products to sell?"
    sv"Many people like to enjoy food and drink without knowing where they come from, tsk, tsk."
    sv"The shops around Connecht source their raw materials from our farm!"
    i"You mean, like.. Stella's items come from this place? How curious!"
    sv"Hurry up, you're missing out on an adventure!"
    i"For a stray virus, you're pretty pushy!"
    sv"You heard me talk all that and yet you call me a stray?"
    i"Sorry!"
    i"Ah! This must be it?"
    sv"Yup, here we are."
    i"Suddenly I'm a bit exhausted, I'm not used to my chest being this heavy.. What happened?"
    sv"You asking me? No clue, but that circumstance is just perfect for your job here today!"
    i"What do you mean?"
    sv"Let's get to work! will you put this on, it'll be perfect for you!"
    i"gah! Why that's a bit.."
    label uniformcow:
    sv"It's a uniform in here, someone just like you is rocking it in there, too."
    sv"You two could probably get along well! Your coworker!"
    i".. Fine! So I can have a coworker friend huh!" 
    
    $ILY_e="up2"
    $ILY_m="smile3"
    $ EquipDress("outfit","Cowgirl")
    
    show ILY with dissolve
    i"Coworker... cow.. orker.."
    i"!!!"
    sv"Great! Looks like you can get started already."
    ""
    ""
    ""
    return