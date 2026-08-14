label maptalk_Herby:
    "Herby""Did you know that in a SoftWar, you can combine battleware cards with certain Types?"
    i "Combine? What's this about?"
    "Herby" "It's called Concatenation!"
    "Herby" "If the Type attributes of your cards in the battle code form a special word, they combine into a new Battleware card!"
    i "Ah!"
    "Herby" "Have you tried it? My go-to combo has been FIRESWORD, a combination of \"FIRE\" and \"SWORD\"! It's simple but powerful!"
    "Herby" "It calls upon the mighty FlameSaber battleware!"
    i "Neato!"
    "Herby" "I'm quite psyched just to try what other combinations are out there!"
    i "I'll see what I can find!"
    "Herby" "Great!"

    return
label maptalk_Tau:
    "Tau" "Wow! What do you think of this new cyber place? I'm pretty overwhelmed!"
    i "I'm looking forward to adventuring around, yes!"
    "Tau" "I'm Tau!"
    i "And I am ILY! Nice To meet you! Tell me whatchu think!"
    "Tau" "I'm a fan of games and a developer of games, too. It really tickles me to enter a new game world. It's funny that the threat in this world are viruses!"
    i "You think this place is a game? Hmmm... You're not wrong.. "
    j "(Wait, she's a human interacting from the real world with her own avatar, huh?)"
    i "(Yeah it's not common, but it's possible to access the GRID without a FAI.)"
    j "(What a curious case.)"

    return

label maptalk_Taka:
    "Taka" "I'm curious about this new cyberworld battle system."
    "Taka" "I've not encountered much battle with Viruses, but I'm told the battleware card library has a wide range of choices to construct the deck with."
    "Taka" "If you know your card games, that means making the deck is half the battle! Or it can decide the entire gameplan!"
    "Taka" "The cards of this world's battle system have text boxes written in code. Do you understand it?"
    "Taka" "I'm only starting to grasp what each card does!"
    "Taka" "It's quite exciting isn't it? Gah! Sorry for yapping."
    
    i "It's alright!"
    return
label maptalk_Ai:
    $ ILY_m = "smile3"
    $ ILY_e = "normal"
    
    "Ai" "Welcome to the GRID! I'm called Ai! Nice to meet you!"
    i "Ah! Hello Ai! My name is ILY! Nice To meet you too!!"
    i "Hey! The name Ai means \"Love\" in Japanese!"
    "Ai" "That's right! Your name is ILY? That means \"I Love You\" doesn't it?"
    i "Yep!!! Waah! We have to be friends!"
    "Ai" "There are some viruses roaming around, keep safe! "
    i "Oh! Yes. Of course! Yeah!! The Viruses!"
    $ ILY_m = "smile4"
    $ ILY_e = "up2"
    
    i "Ha ha ha!"
    "Ai" "I'm classified as an FAI with basic combat ability.. I can protect myself, luckily!"
    j "(Looks like there are FAIs that are neither Antiviruses nor Viruses..)"
    $ ILY_m = "smile3"
    $ ILY_e = "normal"
    i "(Yeah. We might see more of them soon.)"
    return
    