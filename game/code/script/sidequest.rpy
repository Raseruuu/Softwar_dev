define sv = Character("Stray Virus")

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