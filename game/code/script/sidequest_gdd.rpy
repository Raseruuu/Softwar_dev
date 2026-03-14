

label GDD_Sidequest:
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
    be "This world seems to be a special cyberspace. A digital realm."
    i "That's right, you gathered correctly."
    be "And... We seem to be in danger, now that a Virus is right here."
    i "Don't worry!! I won't bite!"
    be "How can we be sure we can trust you?"
    t "Um!!"
    t "ILY helped me find you! So I think that's cause enough to trust her!"
    
    return




