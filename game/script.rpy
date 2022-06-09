 #################
#################

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
#   SPD point declares card's order of execution in the battle phase

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
##################

init python:
    # config.nearest_neighbor = True
    """
    def replace_text(s):
        ## Automatically add a small stop after punctuation to mimic the natural flow of words
        ## This is done by adding zero-width spaces
        ## This scales with CPS so it doesn't introduce annoying delays at high reading speads

        filler = "\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b"
        s = s.replace(",", "," + filler)
        s = s.replace(". ", ". " + filler)
        s = s.replace("... ", "." + filler + "." + filler + ". " + filler + filler)
        s = s.replace("! ", "! " + filler)
        s = s.replace("? ", "? " + filler)
        s = s.replace("?! ", "?! " + filler)
        s = s.replace("!? ", "?! " + filler)
        s = s.replace("-- ", "-- " + filler)
        return s

    config.replace_text = replace_text
    """

    dissolve_heart = ImageDissolve("images/computer/transition_heart_wide.png", 0.5)

image Mouse = "images/computer/mouse.png"
#image white_noise  = "images/computer/white_noise.png"
#image white_noise2 = im.Flip("images/computer/white_noise.png", horizontal=True)
image cafeoutside:
    "images/Cafella/CoffeeShop_SATURATED_23-1.jpg"
    zoom 0.7
image cafedoor:
    "images/Cafella/CoffeeShop_SATURATED_22.jpg"
    zoom 0.7
image cafeinside2:
    "images/Cafella/CoffeeShop_SATURATED_24.jpg"
    zoom 0.7
image cafeoutsideaftern:
    "images/Cafella/CoffeeShop_AFTERN_30.jpg"
    zoom 0.7
image cafeinside:
    "images/Cafella/CoffeeShop_SATURATED_25.jpg"
    zoom 0.7
image cafetable:
    "images/Cafella/CoffeeShop_SATURATED_29.jpg"
    zoom 0.7
image cafeoutside2:
    "images/Cafella/CoffeeShop_SATURATED_30-1.jpg"
    zoom 0.7
image JD_Bed:
    "images/John's Room/Bed.jpg"
    zoom 0.7
image JD_Bed2:
    "images/John's Room/Bed2.jpg"
    zoom 0.7
image JD_Bed3:
    "images/John's Room/Bed3.jpg"
    zoom 0.7
image JD_Door:
    "images/John's Room/Door.jpg"
    zoom 0.7
image JD_Kitchen:
    "images/John's Room/Kitchen.jpg"
    zoom 0.7
image JD_PC1:
    "images/John's Room/PC1.jpg"
    zoom 0.7
image JD_PC2:
    "images/John's Room/PC2.jpg"
    zoom 0.7
image JD_Space1:
    "images/John's Room/Space1.jpg"
    zoom 0.7
image JD_Space2:
    "images/John's Room/Space2.jpg"
    zoom 0.7
image JD_Space2_night:
    "images/John's Room/Space2_night.jpg"
    zoom 0.7
image JD_Space3:
    "images/John's Room/Space3.jpg"
    zoom 0.7
image JD_Space3_night:
    "images/John's Room/Space3_night.jpg"
    zoom 0.7
image redwebsite:
    "images/computer/Webpage.png"
image blackwindow:
    "images/computer/blackwindow.png"
    pause 1.2
    "images/computer/blackwindow2.png"
image ILYgameover="gui/ILYgameover.png"
image USBchan:
    "images/Characters/Softwares/USB-chan[usb].png"
    linear 1.0 yoffset 10
    linear 1.0 yoffset -10
    repeat
image USBkun:
    "images/Characters/Softwares/USB-kun[usb].png"
    linear 1.0 yoffset 10
    linear 1.0 yoffset -10
    repeat
image Mailsaber:
    "images/Cards/MailSaber.png"
image white_noise:
    block:
        "images/computer/white_noise.png"
        pause 0.1
        "images/computer/white_noise2.png"
        pause 0.1
        "images/computer/white_noise3.png"
        pause 0.1
        repeat
image cardpreviewcust:
    LiveComposite(
        (225,300),
        (0,0),"images/Cards/Cardblank.png",
        (11,14),"images/Cards/Datadrill.png",
        (11,219),Text("{color=#FFFF00}{font=font/Dejavusans.ttf}{size=20}DataDrill{/color}{/font}{/size}"),
        (17,244),Text("{color=#FFF}{font=font/Dejavusans.ttf}{size=20}Break();{/color}{/font}{/size}"),
        (57,272),Text("{color=#6600CC}{font=font/Dejavusans.ttf}{size=16}[DataDrill.POW]{/color}{/font}{/size}"),
        (132,272),Text("{color=#6600CC}{font=font/Dejavusans.ttf}{size=16}[DataDrill.SPD]{/color}{/font}{/size}"),
        (160,272),Text("{color=#FFF}{font=font/Dejavusans.ttf}{size=16}16-BIT{/color}{/font}{/size}")
        )
init python:
    okdesktop = False
    # Time = "Feb 15 2018, Thurs 7:00 AM"
    config.keymap['dismiss'].append('Z')
    config.keymap['dismiss'].append('z')
    config.keymap['button_select'].append('z')
    config.keymap['button_select'].append('Z')
transform bounce:
    linear 0.2 yoffset -20
    linear 0.2 yoffset 0

## Flashback
##  Kids Lisa Talks with John: Refer to each respectively: Girl, and Boy.
    # Year 2000, before ILOVEYOU Virus spread
    # Girl and Boy are 7 years old
    # Boy asks girl about her parents' jobs
    # Girl mentions her father's programming career.
    # Girl explains programming
    # Boy suggests to make programs that provide free Internet
    # Boy explains his love for internet and games "It should be free for everyone!"
    # Girl agrees.
    # Boy declares future job to be a programmer.
    # Girl declares the same.

image Email="images/computer/E-mail.png"
image whitewindow = "images/computer/whitewindow.png"
image dlcomp = "images/computer/Download Complete.png"
image dlheart = "images/computer/Download-heart.png"
image iconalert = "images/computer/iconalert.png"
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

label download_hide:
    hide dlcomp
    hide dlheart
    with Dissolve(0.2)
    show screen checks
    return
transform windowanim:
    on show:
        zoom 0.0 xpos 0.5 xanchor 0.5 yalign 0.5
        linear 0.2 zoom 1.0
    on hide:
        linear 0.1 zoom 0.0
screen notifwindow(notification):
    add "whitewindow" at windowanim
    vbox:
        xalign 0.5
        at notifanim
        add "iconalert"
        text "{size=18}[notification]{/size}"

screen checks:
    vbox:
        at notifanim
        text "{color=#000}CAMERA: {/color}{color=#0f0}CHECK{/color}"
        text "{color=#000}SOUND: {/color}{color=#0f0}CHECK{/color}"
        text "{color=#000}MIC: {/color}{color=#0f0}CHECK{/color}"
        text "{color=#000}WEB STATUS: {/color}{color=#0f0}ONLINE{/color}"

transform notifanim:
    xalign 0.45 yalign 0.5 alpha 0.0
    on show:
        linear 0.2 xpos 0.5 alpha 1.0
    on hide:
        linear 0.2 xalign 0.55 alpha 0.0


image black = Solid("#000")
image blue  = Solid("#069")
image bg    = Solid("#035")
image Virusx= "images/rpg/Viruses/[virus].png"

image ILOVEYOU:
    "images/computer/ILOVEYOU.png"
    xalign 0.5 yalign 0.5
    block:
        linear 2.0 xzoom -1.0
        linear 2.0 xzoom 1.0
        repeat

image Folders:
        "images/computer/Folders.png"
        xalign 0.1 yalign 0.1
        block:
            linear 1.0 yoffset 2
            linear 1.0 yoffset -2
            repeat

label test:
    python:
        ILY_w=True
        maptalks = 0
        maptalks2 = 0
        enemy_encounter = False
        spritelist = []
        boxsheet = Connecht_square
        gridpos = [192,168]
        playerpos = [7,5]
        playerxpos = playerpos[0]
        playerypos = playerpos[1]
        objxanchor = ((playerpos[0]+1)*blockSize)-(blockSize/2)
        objyanchor = ((playerpos[1]+1)*blockSize)-(blockSize/2)
        direction = 'down'
        for sprite in spritelist:
            boxsheet[sprite.position[1]][sprite.position[0]]=sprite.dialogue
    scene blue with dissolve
    # $where="Home"
    # call mapcall([4,6],Connecht_square)
    hide screen mapB
    hide screen mapA
    if playerHP<=0:
        return
    scene cafeoutside:
        zoom 1.1
    # call var_init
    # call iptest\
    $hands=[VirusFlame,XAxess,DataDrill,MailSaber,BreakSaber]

    call screen choosecardv3(hands)
    $ index=0

    # call screen Card(DataForce,(0,0),Return())

    show Vira with dissolve:
        xanchor 0.5 xpos 0.85
    v"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    v"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    v"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    # hide Vira
    show CodeRed with dissolve
    c"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    c"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    c"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    c"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    # hide CodeRed
    show Ave with dissolve:
        xalign 0.03
    a"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    a"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    a"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    a"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    # hide Ave
    return
label Vtuber:

    $ game_over = False
    while not game_over:
        show John:
            yalign 0.0
        call screen speakbuttons

    return
screen speakbuttons:

    key "K_DOWN" action SetVariable("John_e","normal")
    key "K_UP" action SetVariable("John_e","up")
    key "K_LEFT" action SetVariable("John_m","frown")
    key "K_RIGHT" action SetVariable("John_m","smile")
    key "K_SPACE" action SetVariable("speaking","John")
    key "repeat_K_SPACE" action SetVariable("speaking","John")
    key "keyup_K_SPACE" action SetVariable("speaking",None)
    key "K_ESCAPE" action SetVariable("game_over",True),Return()
