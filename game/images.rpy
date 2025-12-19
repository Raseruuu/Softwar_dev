#################
#################

##################
default game_over=False
default battle_active=False
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
    dissolve_pixels = ImageDissolve("images/computer/transition_pixels.png", 0.8)
image Mouse = "images/computer/mouse.png"
#image white_noise  = "images/computer/white_noise.png"
#image white_noise2 = im.Flip("images/computer/white_noise.png", horizontal=True)
image cafeoutside:
    "images/BGs/Cafella/CoffeeShop_SATURATED_23-1.jpg"
    zoom 0.7
image cafedoor:
    "images/BGs/Cafella/CoffeeShop_SATURATED_22.jpg"
    zoom 0.7
image cafeinside2:
    "images/BGs/Cafella/CoffeeShop_SATURATED_24.jpg"
    zoom 0.7
image cafeoutsideaftern:
    "images/BGs/Cafella/CoffeeShop_AFTERN_30.jpg"
    zoom 0.7
image cafeinside:
    "images/BGs/Cafella/CoffeeShop_SATURATED_25.jpg"
    zoom 0.7
image cafetable:
    "images/BGs/Cafella/CoffeeShop_SATURATED_29.jpg"
    zoom 0.7
image cafeoutside2:
    "images/BGs/Cafella/CoffeeShop_SATURATED_30-1.jpg"
    zoom 0.7
image JD_Bed:
    "images/BGs/John's Room/Bed.jpg"
    zoom 0.7
image JD_Bed2:
    "images/BGs/John's Room/Bed2.jpg"
    zoom 0.7
image JD_Bed3:
    "images/BGs/John's Room/Bed3.jpg"
    zoom 0.7
image JD_Door:
    "images/BGs/John's Room/Door.jpg"
    zoom 0.7
image JD_Kitchen:
    "images/BGs/John's Room/Kitchen.jpg"
    zoom 0.7
image JD_PC1:
    "images/BGs/John's Room/PC1.jpg"
    zoom 0.7
image JD_PC2:
    "images/BGs/John's Room/PC2.jpg"
    zoom 0.7
image JD_PCN:
    "images/BGs/John's Room/Bedroom_NIGHT_09.jpg"
    zoom 0.7
    
    
image JD_Space1:
    "images/BGs/John's Room/Space1.jpg"
    zoom 0.7
image JD_Space2:
    "images/BGs/John's Room/Space2.jpg"
    zoom 0.7
image JD_Space2_night:
    "images/BGs/John's Room/Space2_night.jpg"
    zoom 0.7
image JD_Space3:
    "images/BGs/John's Room/Space3.jpg"
    zoom 0.7
image JD_Space3_night:
    "images/BGs/John's Room/Space3_night.jpg"
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



image Email="images/computer/E-mail.png"
image whitewindow = "images/computer/whitewindow.png"
image dlcomp = "images/computer/Download Complete.png"
image dlheart = "images/computer/Download-heart.png"
image iconalert = "images/computer/iconalert.png"
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
image lightningbolt:
    "images/battle/effects/bolt1.png"
    pause 0.05
    "images/battle/effects/bolt2.png"
    pause 0.1
    "images/battle/effects/bolt3.png"
    pause 0.05
    "images/battle/effects/bolt4.png"
    pause 0.05
image lightningbolt2:
    "lightningbolt"
    zoom 0.5

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
        # block:
        #     linear 1.0 yoffset 2
        #     linear 1.0 yoffset -2
        #     repeat

label desktopscene:
    scene blue with Dissolve(0.2)
    show Folders with dissolve
    return

label battlescene:
    scene black with dissolve
    pause 0.5
    show scrollingBG at scroll
    show battleroad:
        yalign 1.0 xalign 0.5
    with pixellate
    return



image powerflow:
    zoom 0.3 ypos 1.0 xalign 0.5
    "images/Characters/Code Red/powerflow_1.png"
    pause 0.03
    "images/Characters/Code Red/powerflow_2.png"
    pause 0.03
    "images/Characters/Code Red/powerflow_3.png"
    pause 0.03
    "images/Characters/Code Red/powerflow_4.png"
    pause 0.11
    
label powerflow_animation:
    $ CodeRed_m="open"
    $ CodeRed_e="down"
    show battleroad at tremors
    show powerflow at surgeofpower("powerflow"):
        zoom 1.4 xalign 0.5 yoffset 100
    show CodeRed at reddening:
        xalign 0.5


    show powerflow as powerflow2 at surgeofpower("powerflow"):
        zoom 1.3 xalign 0.5 yoffset 120
        # ypos 1.0 xalign 0.5
    
    return
label hidepowerflow:
    hide powerflow 
    hide powerflow2
    hide CodeRed
    with dissolve_pixels
    call battlescene 
    return 