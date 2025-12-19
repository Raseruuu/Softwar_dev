  # init python:

image cardback:
    "images/cards/cardback.png"
image ring = "images/Cards/ring.png"
image ring2 = "images/Cards/ring2.png"
# image card1 = "images/Cards/[card1].png"
# image card2 = "images/Cards/[card2].png"
image fxnDMG = "images/cards/fxn-Damage.png"
image fxnBRK = "images/cards/fxn-Break.png"
image fxnTGT = "images/cards/fxn-Target.png"
image fxnFRZ = "images/cards/fxn-Freeze.png"
image fxnFW = "images/cards/fxn-Firewall.png"
image fxnREC = "images/cards/fxn-Recover.png"

image Frzsts = "images/battle/Frozen.png"
image Brksts = "images/battle/Broken.png"
image Brnsts = "images/battle/Burned.png"
image Emailsts = "images/battle/Emailed.png"
image IncreaseATKsts = "images/battle/IncreaseATK.png"
image IncreaseDEFsts = "images/battle/IncreaseDEF.png"

image Redframe:
    "white"
    pause .1
    block:
        "images/computer/n1.png"
        pause .05
        "images/computer/n2.png"
        pause .05
        "images/computer/n3.png"
        pause .05
        repeat
image Blueframe:
    "white"
    pause .1
    block:
        "images/computer/m3.png"
        pause .05
        "images/computer/m1.png"
        pause .05
        "images/computer/m2.png"
        pause .05
        repeat

image playerdmgpoint:
    Text("{b}[damagetoplayer]{/b}", style= "statusoutlines_red")
    choice:
        xalign 0.57 yanchor 0.5 ypos 0.1+0.55
        zoom 1.0
        xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
        pause 0.05
        xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
        pause 0.1
        xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.5 zoom 0.8
        pause .05
        xoffset (dmgdist) yoffset (dmgdist) alpha 0.4
        pause .05
        xoffset 0 yoffset 0
        linear 0.1 zoom 1.5 alpha 0.0
    choice:
        xalign 0.43 yanchor 0.5 ypos 0.25+0.55
        zoom 1.0
        xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
        pause 0.05
        xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
        pause 0.1
        xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.5 zoom 0.8
        pause .05
        xoffset (dmgdist) yoffset (dmgdist) alpha 0.4
        pause .05
        xoffset 0 yoffset 0
        linear 0.1 zoom 1.5 alpha 0.0
    choice:
        xalign 0.5 yanchor 0.5 ypos 0.1+0.55
        zoom 1.0
        xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
        pause 0.05
        xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
        pause 0.1
        xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.5 zoom 0.8
        pause .05
        xoffset (dmgdist) yoffset (dmgdist) alpha 0.4
        pause .05
        xoffset 0 yoffset 0
        linear 0.1 zoom 1.5 alpha 0.0
    choice:
        xalign 0.43 yanchor 0.5 ypos 0.1+0.55
        zoom 1.0
        xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
        pause 0.05
        xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
        pause 0.1
        xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.5 zoom 0.8
        pause .05
        xoffset (dmgdist) yoffset (dmgdist) alpha 0.4
        pause .05
        xoffset 0 yoffset 0
        linear 0.1 zoom 1.5 alpha 0.0
    choice:
        xalign 0.43 yanchor 0.5 ypos 0.3+0.55
        zoom 1.0
        xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
        pause 0.05
        xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
        pause 0.1
        xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.5 zoom 0.8
        pause .05
        xoffset (dmgdist) yoffset (dmgdist) alpha 0.4
        pause .05
        xoffset 0 yoffset 0
        linear 0.1 zoom 1.5 alpha 0.0
    choice:
        xalign 0.57 yanchor 0.5 ypos 0.3+0.5
        zoom 1.0
        xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
        pause 0.05
        xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
        pause 0.1
        xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.5 zoom 0.8
        pause .05
        xoffset (dmgdist) yoffset (dmgdist) alpha 0.4
        pause .05
        xoffset 0 yoffset 0
        linear 0.1 zoom 1.5 alpha 0.0
image dmgpoint:
    Text("{size=60}[damagetoenemy]{/size}", style= "statusoutlines_red")
    choice:
        xalign 0.57 yanchor 0.5 ypos 0.1
        zoom 1.5
        xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
        pause 0.05
        xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
        pause 0.1
        xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.5 zoom 0.8
        pause .05
        xoffset (dmgdist) yoffset (dmgdist) alpha 0.4
        pause .05
        xoffset 0 yoffset 0
        linear 0.1 zoom 1.0 alpha 0.0
    choice:
        xalign 0.43 yanchor 0.5 ypos 0.25
        zoom 1.5
        xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
        pause 0.05
        xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
        pause 0.1
        xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.5 zoom 0.8
        pause .05
        xoffset (dmgdist) yoffset (dmgdist) alpha 0.4
        pause .05
        xoffset 0 yoffset 0
        linear 0.1 zoom 1.0 alpha 0.0
    choice:
        xalign 0.5 yanchor 0.5 ypos 0.1
        zoom 1.5
        xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
        pause 0.05
        xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
        pause 0.1
        xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.5 zoom 0.8
        pause .05
        xoffset (dmgdist) yoffset (dmgdist) alpha 0.4
        pause .05
        xoffset 0 yoffset 0
        linear 0.1 zoom 1.0 alpha 0.0
    choice:
        xalign 0.43 yanchor 0.5 ypos 0.1
        zoom 1.5
        xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
        pause 0.05
        xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
        pause 0.1
        xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.5 zoom 0.8
        pause .05
        xoffset (dmgdist) yoffset (dmgdist) alpha 0.4
        pause .05
        xoffset 0 yoffset 0
        linear 0.1 zoom 1.0 alpha 0.0
    choice:
        xalign 0.43 yanchor 0.5 ypos 0.3
        zoom 1.5
        xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
        pause 0.05
        xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
        pause 0.1
        xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.5 zoom 0.8
        pause .05
        xoffset (dmgdist) yoffset (dmgdist) alpha 0.4
        pause .05
        xoffset 0 yoffset 0
        linear 0.1 zoom 1.0 alpha 0.0
    choice:
        xalign 0.57 yanchor 0.5 ypos 0.3
        zoom 1.5
        xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
        pause 0.05
        xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
        pause 0.1
        xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.5 zoom 0.8
        pause .05
        xoffset (dmgdist) yoffset (dmgdist) alpha 0.4
        pause .05
        xoffset 0 yoffset 0
        linear 0.1 zoom 1.0 alpha 0.0
image dmgpointb:
    Text("{size=60}[burndmg]{/size}", style= "statusoutlines_red")
    choice:
        xalign 0.57 yanchor 0.5 ypos 0.1
        zoom 1.5
        xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
        pause 0.05
        xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
        pause 0.1
        xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.5 zoom 0.8
        pause .05
        xoffset (dmgdist) yoffset (dmgdist) alpha 0.4
        pause .05
        xoffset 0 yoffset 0
        linear 0.1 zoom 1.0 alpha 0.0
    choice:
        xalign 0.43 yanchor 0.5 ypos 0.25
        zoom 1.5
        xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
        pause 0.05
        xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
        pause 0.1
        xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.5 zoom 0.8
        pause .05
        xoffset (dmgdist) yoffset (dmgdist) alpha 0.4
        pause .05
        xoffset 0 yoffset 0
        linear 0.1 zoom 1.0 alpha 0.0
    choice:
        xalign 0.5 yanchor 0.5 ypos 0.1
        zoom 1.5
        xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
        pause 0.05
        xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
        pause 0.1
        xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.5 zoom 0.8
        pause .05
        xoffset (dmgdist) yoffset (dmgdist) alpha 0.4
        pause .05
        xoffset 0 yoffset 0
        linear 0.1 zoom 1.0 alpha 0.0
    choice:
        xalign 0.43 yanchor 0.5 ypos 0.1
        zoom 1.5
        xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
        pause 0.05
        xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
        pause 0.1
        xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.5 zoom 0.8
        pause .05
        xoffset (dmgdist) yoffset (dmgdist) alpha 0.4
        pause .05
        xoffset 0 yoffset 0
        linear 0.1 zoom 1.0 alpha 0.0
    choice:
        xalign 0.43 yanchor 0.5 ypos 0.3
        zoom 1.5
        xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
        pause 0.05
        xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
        pause 0.1
        xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.5 zoom 0.8
        pause .05
        xoffset (dmgdist) yoffset (dmgdist) alpha 0.4
        pause .05
        xoffset 0 yoffset 0
        linear 0.1 zoom 1.0 alpha 0.0
    choice:
        xalign 0.57 yanchor 0.5 ypos 0.3
        zoom 1.5
        xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
        pause 0.05
        xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
        pause 0.1
        xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.5 zoom 0.8
        pause .05
        xoffset (dmgdist) yoffset (dmgdist) alpha 0.4
        pause .05
        xoffset 0 yoffset 0
        linear 0.1 zoom 1.0 alpha 0.0
image battlebg = Solid("#1a1a1a")
image battlering = "images/battle/battlering.webp"
image battleroad = "images/battle/battleroad.png"
# image TrojanH = "TrojanHsmall.png"

transform BurstTransfer_trans:
    alpha 1.0
    parallel:
        linear 0.4 xoffset 500 
    parallel:
        linear 0.1 alpha 0.0 xzoom 1.1
        easein 0.1 xzoom 1.0
    pause 2.0
    alpha 0.0 xoffset -500
    # linear 0.2 alpha 1.0 xoffset 0
    parallel:
        linear 0.4 xoffset 0 
    parallel:
        pause 0.2
        linear 0.1 alpha 0.8 xzoom 1.1
        easein 0.1 xzoom 1.0 alpha 1.0

transform BurstTransfer_trans2:
    alpha 1.0
    parallel:
        linear 0.4 xoffset 500 
    parallel:
        linear 0.1 alpha 0.0 xzoom 1.1
        easein 0.1 xzoom 1.0
        xoffset 0 



image cardflasher:
    CardDisplay(currentcard)
image cardflasher_temporary:
    CardDisplay(currentcard) 
    # zoom 1.5
    alpha 1.0
    pause 5.0
    linear 0.5 alpha 0.0
    


image card1:
    Composite(
        (225,300),
        (0,0),"images/Cards/Cardblank.png",
        (11,12),"images/Cards/[playercard1name].png",
        (11,214),Text("{color=#FFFF00}{font=font/adventpro-bold.ttf}{size=20}[playercard1name]{/color}{/font}{/size}"),
        (13,240),FunctionList(playercard1FXN),
        (165,175),"images/Cards/cardbit/[playercard1COST].png",
        (165,237),Text("{color=#ffcc00}{font=font/adventpro-bold.ttf}{size=12}[playerhand[0].TYPE]{/color}{/font}{/size}"),
        (165,267),Text("{color=#ae81f2}{size=24}[playerhand[0].MAG]{/color}{/size}"),
        # (185,273),Text("{color=#ae81f2}{font=font/adventpro-bold.ttf}{size=12}[playerhand[0].HIT]{/color}{/font}{/size}"),
        )
image card2:
    LiveComposite(
        (225,300),
        (0,0),"images/Cards/Cardblank.png",
        (11,12),"images/Cards/[playercard2name].png",
        (11,214),Text("{color=#FFFF00}{font=font/adventpro-bold.ttf}{size=20}[playercard2name]{/color}{/font}{/size}"),
        (13,240),FunctionList(playercard2FXN),
        (165,175),"images/Cards/cardbit/[playercard2COST].png",
        (165,237),Text("{color=#ffcc00}{font=font/adventpro-bold.ttf}{size=12}[playerhand[1].TYPE]{/color}{/font}{/size}"),
        (165,267),Text("{color=#ae81f2}{size=24}[playerhand[1].MAG]{/color}{/size}"),
        # (185,273),Text("{color=#ae81f2}{font=font/adventpro-bold.ttf}{size=12}[playerhand[1].HIT]{/color}{/font}{/size}"),
        )
image card3:
    Composite(
        (225,300),
        (0,0),"images/Cards/Cardblank.png",
        (11,12),"images/Cards/[playercard3name].png",
        (11,214),Text("{color=#FFFF00}{font=font/adventpro-bold.ttf}{size=20}[playercard3name]{/color}{/font}{/size}"),
        # (13,240),FunctionList(playercard3FXN),
        (13,240),FunctionList(playercard3FXN),
        (165,175),"images/Cards/cardbit/[playercard3COST].png",
        (165,237),Text("{color=#ffcc00}{font=font/adventpro-bold.ttf}{size=12}[playerhand[2].TYPE]{/color}{/font}{/size}"),
        (165,267),Text("{color=#ae81f2}{size=24}[playerhand[2].MAG]{/color}{/size}"),
        # (185,273),Text("{color=#ae81f2}{font=font/adventpro-bold.ttf}{size=12}[playerhand[2].HIT]{/color}{/font}{/size}"),
        )
image card4:
    LiveComposite(
        (225,300),
        (0,0),"images/Cards/Cardblank.png",
        (11,12),"images/Cards/[playercard4name].png",
        (11,214),Text("{color=#FFFF00}{font=font/adventpro-bold.ttf}{size=20}[playercard4name]{/color}{/font}{/size}"),
        (13,240),FunctionList(playercard4FXN),
        (165,175),"images/Cards/cardbit/[playercard4COST].png",
        (165,237),Text("{color=#ffcc00}{font=font/adventpro-bold.ttf}{size=12}[playerhand[3].TYPE]{/color}{/font}{/size}"),
        (165,267),Text("{color=#ae81f2}{size=24}[playerhand[3].MAG]{/color}{/size}"),
        # (185,273),Text("{color=#ae81f2}{font=font/adventpro-bold.ttf}{size=12}[playerhand[3].HIT]{/color}{/font}{/size}"),
        )
image card5:
    LiveComposite(
        (225,300),
        (0,0),"images/Cards/Cardblank.png",
        (11,12 ),"images/Cards/[playercard5name].png",
        (11,214),Text("{color=#FFFF00}{font=font/adventpro-bold.ttf}{size=20}[playercard5name]{/color}{/font}{/size}"),
        (13,240),FunctionList(playercard5FXN),
        (165,175),"images/Cards/cardbit/[playercard5COST].png",
        (165,237),Text("{color=#ffcc00}{font=font/adventpro-bold.ttf}{size=12}[playerhand[4].TYPE]{/color}{/font}{/size}"),
        (165,267),Text("{color=#ae81f2}{size=24}[playerhand[4].MAG]{/color}{/size}"),
        # (185,273),Text("{color=#ae81f2}{font=font/adventpro-bold.ttf}{size=12}[playerhand[4].HIT]{/color}{/font}{/size}"),
        )
init python:
    def battle_distance_function(bd):
        return 0.8-(bd/30)
    def battle_distance_function2(bd):
        return (bd*3.5)
image Enemy:
    "images/battle/Enemies/[enemyName].png"
    zoom battle_distance_function(battle_distance)
    linear 0.2 zoom battle_distance_function(battle_distance)
    # ypos -battle_distance_function2(battle_distance)
    # linear 1.0 yoffset 10
    # linear 1.0 yoffset -10
    # repeat
image Trojan:
    "images/battle/Enemies/TrojanHorse.png"
    zoom 2.0
image cardflip1:
    "images/cards/cardback.png"
    xzoom 1.0
    linear 0.2 xzoom 0.0
    "card1"
    xzoom 0.0
    linear 0.2 xzoom 1.0
image cardflip2:
    "images/cards/cardback.png"
    xzoom 1.0
    linear 0.2 xzoom 0.0
    "card2"
    xzoom 0.0
    linear 0.2 xzoom 1.0
image cardflip3:
    "images/cards/cardback.png"
    xzoom 1.0
    linear 0.2 xzoom 0.0
    "card3"
    xzoom 0.0
    linear 0.2 xzoom 1.0
image cardflip4:
    "images/cards/cardback.png"
    xzoom 1.0
    linear 0.2 xzoom 0.0
    "card4"
    xzoom 0.0
    linear 0.2 xzoom 1.0

transform poscarddeck:
    xpos 1110
    ypos 620
    xanchor 0.5
    yanchor 0.5
    zoom 0.5
transform card1pos:
    xalign 0.30
    yalign 0.95


transform card2pos:
    xalign 0.43
    yalign 0.95

transform card3pos:
    xalign 0.57
    yalign 0.95

transform card4pos:
    xalign 0.70
    yalign 0.95

transform choosecardsize:
    zoom 0.4




label Enemydisappear:
    show Enemy:
        linear 0.15 zoom 0.94
        xoffset 0.12 yoffset 0.2 alpha 0.5
        pause .05
        xoffset 0.-17 yoffset 0.-17 alpha 0.8
        pause .05
        xoffset 0.13 yoffset 0.2 alpha 1.0
        pause 0.1
        xoffset 0.-19 yoffset 0.11
        pause 0.4
        linear 0.1 zoom 0.7 alpha 0.0
    hide Enemy
    return

# label TurnEnd:


#     ##RETURN CARDS FROM HAND TO DECK
#     # if selectedcard=="card1":
#     if len(myhand) >=1:
#         $ mydeck.append(myhand[0])
#     if len(myhand) >=2:
#         $ mydeck.append(myhand[1])
#     if len(myhand) >=3:
#         $ mydeck.append(myhand[2])
#     if len(myhand) >=4:
#         $ mydeck.append(myhand[3])
#     $ decknum = len(mydeck)
#     if len(Enmyhand) >=1:
#         $ Enmydeck.append(Enmyhand[0])
#     if len(Enmyhand) >=2:
#         $ Enmydeck.append(Enmyhand[1])
#     if len(Enmyhand) >=3:
#         $ Enmydeck.append(Enmyhand[2])
#     if len(Enmyhand) >=4:
#         $ Enmydeck.append(Enmyhand[3])
#     # "deck = [mydeck]\nhand = [myhand]"
#     return

# show cardbacks at deck as cardbacks2
# show cardbacks at deck as cardbacks1
init -2 python:
    def bar_size(value,maxvalue, barwidth):
        barsize = int(barwidth*float(value)/float(maxvalue))
        if value > maxvalue:
            barsize=int(barwidth*float(maxvalue)/float(maxvalue))
        return barsize

transform fxnicon:
    zoom 0.07
        #hbox:
        #    null height 30 width 20
        #    add "Icon_Ily"
        #    null height 30 width 20
        #    vbox:
        #        text "Ily"
        #        hbox:
        #            text "{size=18}HP:{/size}"
        #            null width 150
        #        add "images/battle/bar.png" at barwidth(Ily_HP,Ily_HPmax)
        #        text "[Ily_HP]/[ILY_HPmax]"
style battlestats_frame is gui_frame:
    background Frame("gui/frame.png", 64, 64, tile=gui.frame_tile)
    right_padding 16
    left_padding 16
    bottom_padding 16
    top_padding 8

style battlestats_text is text_nooutline:
    color '#000'

style fxn_frame is gui_frame:
    background Frame("gui/framefxn.png", 4, 4, tile=gui.frame_tile)
    right_padding 16
    left_padding 16
    bottom_padding 16
    top_padding 8
    ysize 350
    xsize 250
style bit_frame is gui_frame:
    background Frame("gui/framefxn.png", 4, 4, tile=gui.frame_tile)
    right_padding 8
    left_padding 8
    bottom_padding 8
    top_padding 8
style fxn_text is text_nooutline:
    color '#fff'


style healthbar_frame is gui_frame:
    background Frame("images/battle/bar.png", 4, 4, tile=gui.frame_tile)
    ysize 35

    right_padding 0
    left_padding 0
    bottom_padding 0
    top_padding 0

image curve:
    "images/battle/curve1.webp"
    pause .15
    "images/battle/curve2.webp"
    pause .15
    "images/battle/curve3.webp"
    pause .15
    "images/battle/curve4.webp"
    pause .15
    repeat
screen decknum:
    text "{color=#FFF}Deck: [decknum]{/color}" xpos 1162 xalign 0.5 ypos 400 yanchor 1.0


#
#
image fxndescription:
    ConditionSwitch(
        "'Freeze' in fxnpreview",Text("Add Freeze to Attack (x1)."),
        "'Burn' in fxnpreview",Text("Add Burn to Attack (x4). Effect fades each turn."),
        "'Break' in fxnpreview",Text("Break weaker Battleware. if Break succeeds: Negate attack ."),
        "'TripleHit' in fxnpreview",Text("Decrease Target HP 3 times."),
        "'DoubleHit' in fxnpreview",Text("Decrease Target HP 2 times."),
        "'Recover' in fxnpreview",Text("Increase Self HP."),
        "'POWR_Up' in fxnpreview",Text("Increase Self POWR for 3 turns."),
        # "'SPD_Up' in fxnpreview",Text("Increase Self SPD for 3 turns."),
        "'Saber_Up' in fxnpreview",Text("Increase Self \"Saber\" named Battleware POW for 3 turns. Effect fades each turn."),
        "'Damage' in fxnpreview",Text("Decrease Target HP.")
        )

    # frame:
    #     hbox:
    #         xalign 0.5 yalign 0.9
    #         for i in range(0,1):
    #             imagebutton idle "images/cards/[myhand[i][1]]" action Return("card1") hovered Show("card1"),Play("sound","sfx/select.wav")
            # imagebutton idle "images/cards/[i].png" action Hide("card2"), Return("card2") hovered Show("card2"),Play("sound","sfx/select.wav") unhovered Hide("card2") at card2pos


transform cardtrans:

    on show:
        zoom 0.6
        linear 0.05 zoom 1.1

transform cardtrans2:

    on show:
        zoom 1.0
        linear 0.05 zoom 1.6
