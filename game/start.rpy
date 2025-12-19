

#########

# -SOFTWAR TO DO:
# URVANG
#   Add:
#       Battleware Functions:

#           Slash()         Increase Slash cards for 3 turns
#           Bomb()          Increase Bomb cards for 3 turns
#           Blast()         Increase Blast cards for 3 turns
#           Break()         Ignore Shield
#
#           Damage()        Inflict (MAG*ATK) Damage to enemy
#           Shield()        Gain (MAG*DEF) SP

#           Boost(type)     Append Boost status to user for [type] cards
#           Burn()          Append Burn status to enemy
#           Burnself()      Burn status
#           Freeze()      Cancel 1 execution
#           Shock()       Reduce

#           Negate()      Negate 1 execution
#           Recover()
#           Boost()       Increase (target) Card point for (turn) turns
#           Resist()      Gain Resistance to (Fxn) Damage


#       New Battleware:
#           Ave's Guns
#           SoftDrink

# Draw Phase:

#   Draw cards until 4
# Battle Phase:
#   Drop card to attack with

# Return Phase:
#   Return Dropped card to hand

# RULES:
#   Player loses when HP hits 0
#   POW point declares card's damage to be reduced to opponent player
#   When attacked:
#       Player can discard Battleware with higher SPD to negate the attack.
#       Make Status Variable an Array
#       .append("Frozen")
#       "Frozen" in Sts

#       Browser image displaying "Hacked by ???"
# TODO:
# *Add more juice to the start
# *Fan collection
#   - Make it easy for them to "play" the game without downloading it (ie. trailer, screenshots)
#
# *Fan retention
#   - Ask for mailing list registration
#   - Link to website
#   - Ask for a review/rating
#
##################

    # jump debug_menu
image logo = "gui/logo.png"
image white = Solid("#fff")
image Credits = "gui/Credits.png"
image Maoudamashii = "Maoudamashii.png"
label start:
    # call cutscene_gunvar
    # call roguemode
    # call test
    call game_loop from _call_game_loop
    return
label credits:
    hide screen mapB
    hide screen mapA
    $ILY_m="smile"
    scene white with pixellate
    play music "bgm/Credits_bgm_maoudamashii_8bit08.mp3"

    show logo:
        zoom 0.0 xalign 0.5 yalign 0.5
        linear 0.3 zoom 1.5
        linear 0.3 zoom 1.4
    pause 1.0
    scene Credits with pixellate
    voice "voice/ILY10E - Thank you for playing demo.mp3"
    i"Thank you for playing the Softwar Demo!"
    scene blue with dissolve
    show Folders
    $ direction = 'down'
    # show ILY:
    #     xalign 0.5


    show text "We hope you had at least {size=32}a bit{/size} of fun!!":
        xalign 0.5 yalign 0.6
    pause 3.0
    show text "Softwar Demo - End" with dissolve
    pause 3.0
    show text "Say hello to the Softwar Team!" with dissolve
    pause 3.0
    show text "Raseruuu/Zan Kizuna\n\nStory, Programming and Character Art" with dissolve
    pause 3.0
    # show text "Arsym\n\nProject Manager, Programmer, GUI, Co-writer" with dissolve
    # pause 3.0
    # show text "Opa\n\nStory, Co-writer" with dissolve
    # pause 3.0
    show text "Jeroz\n\nStory, Co-writer" with dissolve
    pause 3.0
    show text "Kiora001/Julian\n\nCharacter Art, Logo, and Cover Art" with dissolve
    pause 3.0
    show text "patricio_hue2\n\nPromotional Art, CG Art" with dissolve
    pause 3.0
    show text "Gelopsychedelico\n\nPromotional Art, Virus designs" with dissolve
    pause 3.0
    show text "Sayaka Mashiro\n\nIly's Voice" with dissolve
    pause 3.0
    show text "Bunnyvoid\n\n3D Background Art" with dissolve
    pause 3.0
    show text "Maoudamashii.jokersounds.com\n\nBackground Music" with dissolve
    pause 3.0
    show text "The Essential Retro Video Game Sound - Juhani Junkala\n\nSound Effects" with dissolve
    pause 3.0
    show text "Ren'py Visual Novel Engine\n\nVersion "+renpy.version() with dissolve
    pause 3.0
    show text "Tom Rothamel aka Pytom\n\nRen'py Visual Novel Engine" with dissolve
    pause 3.0
    show text "Ren'py Discord Server\n\nSpecial Thanks" with dissolve
    pause 3.0
    show text "AMA Computer College Fairview, Philippines\n\nSpecial Thanks" with dissolve
    pause 3.0
    show text "The original ILOVEYOU VIRUS by Reonel Ramones, Onel De Guzman\n\nSpecial Thanks" with dissolve
    pause 3.0
    hide text
    hide IlyRpg
    # $ Ily_p='1'
    # $ Ily_m='smile'

    # show ILY:
    #     xalign 0.5
    # i"Have a Lovely Day, User!"

    return
