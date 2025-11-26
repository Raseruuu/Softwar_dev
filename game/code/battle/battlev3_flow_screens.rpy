init python:
    PFAI = ILY
    ILYStatsnow = {
        "name":PFAI.name,
        "HP":PFAI.HP,
        "HPMax":PFAI.HP,
        "SP":0,
        "SPMax":PFAI.SP,
        "ATK":PFAI.ATK,
        "DEF":PFAI.DEF,
        "Deck":PFAI.deck
    }
    statuslist=["BoostATK","BoostDEF","Email"]
    playerbits = 8
    playerstats = ILYStatsnow
    playerName = ILYStatsnow["name"]
    playerHP = ILYStatsnow["HP"]
    playerHPMax = ILYStatsnow["HPMax"]
    playerSP = 0
    playerSPMax = ILYStatsnow["SPMax"]
    playerATK = ILYStatsnow["ATK"]
    playerDEF = ILYStatsnow["DEF"]

    playerDeck = ILYStatsnow["Deck"]
    actual_playerDeck = playerDeck
    fxnindex=0
    execution_active=False
    enemy_evasion_active=False
    evasion_active=False
    battle_done = False
    enemyfirst =False
    map_active=False
    playerbattlecode=[]
    

default playerPlugins =[]
default battle_distance = 0
transform flip_image:
    xzoom -1.0
transform xZoom(value):
    xzoom (value)



define boss_list=["Code Red", "Ave","ILY", "Vira", "Bitwulf", "Brain","Melissa","ILY_Alpha"]

# camera:
#     perspective True
#     gl_depth True
# transform xrotate:
#     yrotate 0.1 
transform vstrans:
    choice:
        xoffset 0 yoffset 0 zoom 1.0
        linear 0.1 xoffset 10 yoffset 10 zoom 1.1
        pause 0.1
    choice:
        xoffset 0 yoffset 0
        linear 0.1 xoffset -10 yoffset 10 zoom 1.1
        pause 0.1
    choice:
        xoffset 0 yoffset 0 zoom 1.0
        linear 0.1 xoffset 10 yoffset -10 zoom 1.1
        pause 0.1
        xoffset 0 yoffset 0 zoom 1.0
    choice:
        xoffset 0 yoffset 0 zoom 1.0
        linear 0.1 xoffset -10 yoffset -10 zoom 1.1
        pause 0.1
    repeat
transform vstrans2:
    choice:
        xoffset 0 yoffset 0 zoom 1.0
        xoffset 10 yoffset 10 zoom 1.4
        pause 0.1
    choice:
        xoffset -10 yoffset 10 zoom 1.4
        pause 0.1
    choice:
        xoffset 0 yoffset 0 zoom 1.0
        xoffset 10 yoffset -10 zoom 1.4
        pause 0.1
    choice:
        xoffset 0 yoffset 0 zoom 1.0
        xoffset -10 yoffset -10 zoom 1.4
        pause 0.1
    repeat
    repeat
screen VICTORY():

    add ("images/Special Images/BattleCutscene_"+playerName+".png")  xpos 0.5 xanchor 0.5 yalign 0.25 at zoomtrans(0.12), pausetrans0
    

screen VERSUS(playerName,enemyName):

    add ("images/Special Images/BattleCutscene_"+enemyName+".png")  xpos 0.5 xanchor 0.0 yalign 0.25 at zoomtrans(0.15)
    add ("images/Special Images/BattleCutscene_"+playerName+".png") xpos 0.5 xanchor 1.0 yalign 0.25 at zoomtrans(0.15)
    key "dismiss" action Return()

    text "{size=100}{b}[playerName]{/size}{/b}" xalign 0.1 yalign 0.75  style 'statusoutlines_red'
    text "{size=85}{b}{color=f00}VS{/size}{/b}{/color}" xalign 0.5 yalign 0.75 at vstrans2
    text "{size=80}{b}VS{/size}{/b}" xalign 0.5 yalign 0.75 style 'statusoutlines_red'
    text "{size=100}{b}"+ ("ILY" if (enemyName =="ILY_Alpha") else enemyName )+"{/size}{/b}" xalign 0.9 yalign 0.75  style 'statusoutlines_red'  

transform battlecode_trans(focused=False):
    xoffset 12
    linear 0.2 xpos (0.49 if focused else 0.0) xanchor (0.5 if focused else 0.0) zoom (1.4 if focused else 1.0)

    
screen battlestats():
    
    $ playerbitsfirsthalf=(int(playerbitsmax/2) if (playerbits-int(playerbitsmax/2))>0 else playerbits)
    $ playerbitssecondhalf=(0 if playerbits<=int(playerbitsmax/2) else playerbits-playerbitsfirsthalf)
    $ enemybitsfirsthalf=(int(enemybitsmax/2) if (enemybits-int(enemybitsmax/2))>0 else enemybits)
    $ enemybitssecondhalf=(0 if enemybits<=int(enemybitsmax/2) else enemybits-enemybitsfirsthalf)
    frame:
        yalign 0.01
        xalign 0.5
        xsize 520
        ysize 80
        
        vbox:
            
            xalign 0.5
            text "{font=font/lucon.ttf}{size=18}{b}VS{/font}{/size}{/b}" xalign 0.5
            frame:
                style_prefix "bit"
                xfill True
                
                vbox:
                    xalign 0.5 
                    hbox:
                        xalign 0.5 
                        add "gui/distperson.png" yalign 0.5 at zoomtrans(0.6)
                        null width 2
                        add "gui/distarrow.png" yalign 0.5 at zoomtrans(0.4),flip_image
                        null width 1
                        for dist in range(0,battle_distance):
                            null width 2
                            add "gui/dist.png" yalign 0.5 at xZoom(2.0)
                            null width 2    
                        null width 1
                        add "gui/distarrow.png" yalign 0.5 at zoomtrans(0.4)
                        null width 2
                        add "gui/distperson.png" yalign 0.5 at zoomtrans(0.6)
                    text "{font=font/lucon.ttf}{size=14}{b}DISTANCE=[battle_distance]{/font}{/size}{/b}" xalign 0.5
                    # text "{font=font/lucon.ttf}{size=11}{b}{/font}{/size}{/b}" xalign 0.5

                
    
            
            

    frame:
        style_prefix "statsb"
        xpos 0.01 xanchor 0.0 yalign 0.01 xsize 380
        # at alpha08
        # at xrotate
        vbox:
            hbox:
                style_prefix "battlestats"
                image (Null(height=154,width=114) if evasion_active else "Icon_[playerName]") at zoomtrans(0.8)
                spacing 10
                vbox:
                    
                    text "{b}{size=24}[playerName]{/b}{/size}"
                    vbox:
                        fixed:
                            ysize 24
                            frame:
                                    style_prefix "healthbar_bg"
                                    xsize 235
                                    ysize 24
                            frame:
                                yalign 0.5
                                style_prefix "healthbar"
                                xsize bar_size(playerHP,playerHPMax,235)
                                ysize 22
                            hbox:
                                yalign 0.5 xalign 0.05
                                add "gui/HP_Heart.png" yalign 0.5 
                                text "{b}[playerHP]/[playerHPMax]{/b}" style "HPbaroutlines" yalign 0.5 xpos 0.05
                        null height 10
                        fixed:
                            ysize 24
                            frame:
                                style_prefix "healthbar2_bg"
                                xsize 235
                                ysize 24
                            frame:
                                yalign 0.5
                                style_prefix "healthbar2"
                                xsize bar_size(playerSP,playerSPMax,235)
                                ysize 22
                            
                            hbox:
                                yalign 0.5 xalign 0.05
                                add "gui/SP_Shield.png" yalign 0.5 
                                text "{b}[playerSP]/[playerSPMax]{/b}" style "SPbaroutlines" yalign 0.5 xpos 0.05
                                
                        null height 10
                        # text "ATK: [playerATK]  DEF: [playerDEF]"
                        hbox:
                            if (playerATK<playerATK_m):
                                text "ATK: {color=#0ff} [playerATK_m]{/color}"
                            elif (playerATK>playerATK_m):
                                text "ATK: {color=#f00} [playerATK_m]{/color}"
                            else:
                                text "ATK: [playerATK_m]"
                            null width 20
                            if (playerDEF<playerDEF_m):
                                text "DEF: {color=#0ff}[playerDEF_m]{/color}"
                            elif (playerDEF>playerDEF_m):
                                text "DEF: {color=#f00}[playerDEF_m]{/color}"
                            else:
                                text "DEF: [playerDEF_m]"
                        
                        null height 5
                    
                        
            vbox:
                null height 8
                text "{size=14}{b}Self_Status{/size}{/b}" xalign 0.0
                grid 8 2:
                    for fxns in PlayerSts:
                        # image "gui/battlests/[fxns].png"

                        if type(fxns)== list:

                            # else:
                            image "gui/battlests/[fxns[0]].png" at zoomtrans(0.9)
                        elif type(fxns) == str:
                                # frame:
                                #     background Null()
                                #     image "gui/battlests/token.png"
                                #     text "{size=3}{font=font/adventpro-bold.ttf}[fxns]{/size}{/font}" xalign 0.5 yalign 0.82
                            image "gui/battlests/[fxns].png" at zoomtrans(0.9)
                    for fillerz in range(0,16-len(PlayerSts)):
                        # null width 50 height 50
                        image "gui/battlests/Empty.png" at zoomtrans(0.9)
                text "{size=14}{b}BITS{/size}{/b}" xalign 0.0
                frame:
                    style_prefix "bit"
                    ysize 80
                    hbox:
                        
                        for bit in range(0,playerbitsfirsthalf):
                            add "gui/Bit.png"
                        for fillers in range(0,int(playerbitsmax/2)-playerbitsfirsthalf):
                                add "gui/Bit_empty.png"
                                    
                    hbox:
                        xoffset 20 yoffset 22
                        for bit in range(0,playerbitssecondhalf):
                            add "gui/Bit.png"
                        for fillers in range(0,int(playerbitsmax/2)-playerbitssecondhalf):
                                add "gui/Bit_empty.png"
            
    frame:
        style_prefix "statsb"
        xpos 0.99 xanchor 1.0 yalign 0.01 xsize 380
        # at alpha08
        vbox:
            hbox:
                xalign 1.0
                style_prefix "battlestats"
                box_reverse True
                if enemyName in boss_list: 
                    image (Null(height=154,width=114) if enemy_evasion_active else "Icon_[enemyName]") xalign 1.0  at zoomtrans(0.8)
                else:
                    null width 115 height 154
                spacing 10
                vbox:
                    xalign 1.0
                    
                    text ("{b}{size=24}" + ("ILY" if (enemyName =="ILY_Alpha") else enemyName )+"{/b}{/size}") xalign 1.0
                    vbox:
                        fixed:
                            ysize 24
                            frame:
                                
                                style_prefix "healthbar_bg"
                                xsize 235
                                xalign 1.0 
                                ysize 24
                            frame:
                                yalign 0.5
                                xalign 1.0
                                style_prefix "healthbar"
                                
                                xsize bar_size(enemyHP,enemyHPMax,235)
                                ysize 22
                            
                            hbox:
                                yalign 0.5 xalign 0.95
                                text "{b}[enemyHP]/[enemyHPMax]{/b}" style "HPbaroutlines" yalign 0.5 
                                add "gui/HP_Heart.png" yalign 0.5 
                        null height 10
                        fixed:
                            ysize 24
                            frame:
                                xalign 1.0
                                style_prefix "healthbar2_bg"
                                xsize 235
                                ysize 24
                            frame:
                                yalign 0.5
                                xalign 1.0
                                style_prefix "healthbar2"
                                xsize bar_size(enemySP,enemySPMax,235)
                                ysize 22
                            hbox:
                                yalign 0.5 xalign 0.95
                                text "{b}[enemySP]/[enemySPMax]{/b}" style "SPbaroutlines" yalign 0.5 xalign 0.95
                                add "gui/SP_Shield.png" yalign 0.5 
                        null height 10
                        hbox:
                            xalign 1.0
                            if (enemyATK<enemyATK_m):
                                text "ATK: {color=#0ff} [enemyATK_m]{/color}"
                            elif (enemyATK>enemyATK_m):
                                text "ATK: {color=#f00} [enemyATK_m]{/color}"
                            else:
                                text "ATK: [enemyATK_m]"
                            null width 20
                            if (enemyDEF<enemyDEF_m):
                                text "DEF: {color=#0ff}[enemyDEF_m]{/color}"
                            elif (enemyDEF>enemyDEF_m):
                                text "DEF: {color=#f00}[enemyDEF_m]{/color}"
                            else:
                                text "DEF: [enemyDEF_m]"
                        null height 5
                        
                        null height 5
                        
                        
            vbox:    
                null height 8
                        # null height 57
                text "{size=14}{b}Target_Status{/size}{/b}" xalign 1.0
                grid 8 2:
                    xalign 1.0
                    for fxns in EnmySts:
                        # image "gui/battlests/[fxns].png"
                        if type(fxns)== list:
                            image "gui/battlests/[fxns[0]].png" at zoomtrans(0.9)
                        elif type(fxns) == str:
                            image "gui/battlests/[fxns].png" at zoomtrans(0.9)

                    for fillerz in range(0,16-len(EnmySts)):
                        # null width 50 height 50
                        image "gui/battlests/Empty.png" at zoomtrans(0.9)
                text "{size=14}{b}BITS{/size}{/b}" xalign 1.0
                frame:
                    style_prefix "bit"
                    ysize 80
                    xalign 1.0
                    hbox:
                        box_reverse True
                        xalign 1.0
                        for bit in range(0,enemybitsfirsthalf):
                            add "gui/Bit.png"
                        for fillers in range(0,int(enemybitsmax/2)-enemybitsfirsthalf):
                                add "gui/Bit_empty.png"              
                    hbox:
                        box_reverse True
                        xalign 1.0
                        xoffset -20 yoffset 22
                        for bit in range(0,enemybitssecondhalf):
                            add "gui/Bit.png"
                        for fillers in range(0,int(enemybitsmax/2)-enemybitssecondhalf):
                                add "gui/Bit_empty.png"
                        null width 0       
                        
                            # grid 4 2:
                            #     for bit in range(0,playerbits):
                            #         add "gui/Bit.png":
                            #             zoom 0.75
                            #     for fillers in range(0,8-playerbits):
                            #         add "gui/Bit_empty.png":
                            #             zoom 0.75
                    #     text "{b}ATK: [enemyATK]{/b}"
                    #     null width 10
                    #     text "{b}DEF: [enemyDEF]{/b}"
    frame:
        style_prefix "statsb"
        xsize 380 ysize 120
        # xpos 0.01 xanchor 0.0 ypos 0.60 yanchor 0.5
        # xpos 0.5 xanchor 0.5 ypos 0.60 yanchor 0.5
        # at alpha08
        ypos 0.60 yanchor 0.5
        at battlecode_trans(focused=battlecodestatus)
        
        vbox:
            vbox:
                text "{size=14}{b}CODE{/size}{/b}" xalign 0.0
                hbox:

                    xalign 0.0

                    for cards in playerbattlecode:
                        add "images/Cards/[cards.NAME].png" at codesize
                    # for cards in playerbattlecode:
                    #     add "images/Cards/[cards.NAME].png" at codesize
                    for fillers in range(0,5-len(playerbattlecode)):

                        add "images/Cards/Empty.png" at codesize
            null height 5
            
style battlestats_text is text:
    color "#fff"
    font "font/lucon.ttf"
    size 14

style statsb_frame is gui_frame:
    background Frame("gui/framew.png", 4, 4, tile=gui.frame_tile)

    right_padding 14
    left_padding 14
    bottom_padding 14
    top_padding 14
style stats2_frame is gui_frame:
    background Frame("gui/framefxn.png", 4, 4, tile=gui.frame_tile)

    right_padding 14
    left_padding 14
    bottom_padding 14
    top_padding 14
style stats_frame:
    background Frame("gui/frame.png", 4, 4, tile=gui.frame_tile)

    right_padding 14
    left_padding 14
    bottom_padding 14
    top_padding 14
style healthbar_frame is gui_frame:
    background Frame("gui/bar.png", 4, 4, tile=gui.frame_tile)
    ysize 25

    right_padding 0
    left_padding 0
    bottom_padding 0
    top_padding 0
style healthbar_bg_frame is gui_frame:
    background Frame("gui/bar_bg.png", 4, 4, tile=gui.frame_tile)
    ysize 25

    right_padding 0
    left_padding 0
    bottom_padding 0
    top_padding 0
style healthbar2_frame is gui_frame:
    background Frame("gui/barblue.png", 4, 4, tile=gui.frame_tile)
    ysize 25

    right_padding 0
    left_padding 0
    bottom_padding 0
    top_padding 0
style healthbar2_bg_frame is gui_frame:
    background Frame("gui/barblue_bg.png", 4, 4, tile=gui.frame_tile)
    ysize 25

    right_padding 0
    left_padding 0
    bottom_padding 0
    top_padding 0

transform codesize:
    zoom 0.35

label remaininghand:
    
    python:
        playerhandminususedcards = []
        if usedcards!=[]:
            for (handindex, hand_cards) in enumerate(playerhand):
                if handindex in usedcards:
                    pass
                else:
                    playerhandminususedcards.append(hand_cards)   
            
        else:
            playerhandminususedcards=playerhand
    return
default playerhand = []
default usedcards = []
default playerhandminususedcards = []
default battlecodestatus = False
screen playerviewdraw:
    # image "black" at pausedim2
    image At("[playerName]",zoomtrans(0.8 )) :
        xpos 0.75 xanchor 0.5

label drawcards:
    # $ battlecodestatus=True
    show screen playerviewdraw
    call remaininghand
    show card_deck:
        zoom 0.1
        xalign 0.5 yalign 0.5
    show screen handcardsscreen(phase="drawphase")
    
        
    pause 0.4    
    python:
        # playerhandcombined=[x for x in playerhand: playerhandcombined+=x]
        # renpy.say("",""+str(playerhand[0].NAME)) 
        
        # playerhand = []
        
        playerbattlecode = []
        usedcards = []
        handdrawindex=0
        playerhand=playerhandminususedcards
        for hand_draw in range(0,5-len(playerhand)):
            renpy.hide_screen('handcardsscreen')
            renpy.show_screen('handcardsscreen',phase="drawphase")
            renpy.show("card_deck_draw")
            playerhand.append(playerDeck[0])
            playerDeck.pop(0)
            # renpy.play("sfx/draw.wav")
            renpy.play("sfx/draw.mp3","sound")
            renpy.pause(0.2)
            
            renpy.hide("card_deck_draw")
            handdrawindex+=1
        renpy.hide_screen('handcardsscreen')
        renpy.show_screen('handcardsscreen',phase="drawphase")
        # playerhand.append(playerDeck[0])
        # playerhand.append(playerDeck[1])
        # playerhand.append(playerDeck[2])
        # playerhand.append(playerDeck[3])
        # playerhand.append(playerDeck[4])
        # for deckcard in range (0,5):
        #     playerDeck.pop(0)
        # for handcard in range (0,5):
        #     playerDeck.append(playerhand[handcard])

        playercard1obj =playerhand[0]
        playercard1name = playerhand[0].NAME
        playercard1ATK = playerhand[0].TYPE
        playercard1DEF = playerhand[0].MAG
        playercard1FXN = playerhand[0].FXN
        playercard1COST = playerhand[0].COST

        playercard2obj =playerhand[1]
        playercard2name = playerhand[1].NAME
        playercard2ATK = playerhand[1].TYPE
        playercard2DEF = playerhand[1].MAG
        playercard2FXN = playerhand[1].FXN
        playercard2COST = playerhand[1].COST

        playercard3obj =playerhand[2]
        playercard3name = playerhand[2].NAME
        playercard3ATK = playerhand[2].TYPE
        playercard3DEF = playerhand[2].MAG
        playercard3FXN = playerhand[2].FXN
        playercard3COST = playerhand[2].COST

        playercard4obj =playerhand[3]
        playercard4name = playerhand[3].NAME
        playercard4ATK = playerhand[3].TYPE
        playercard4DEF = playerhand[3].MAG
        playercard4FXN = playerhand[3].FXN
        playercard4COST = playerhand[3].COST

        playercard5obj =playerhand[4]
        playercard5name =playerhand[4].NAME
        playercard5TYPE = playerhand[4].TYPE
        playercard5MAG = playerhand[4].MAG
        playercard5FXN = playerhand[4].FXN
        playercard5COST = playerhand[4].COST

        playerhandcosts = []
        playerhand2 = playerhand
    hide screen playerviewdraw
    hide card_deck with dissolve
    # call check_cost
    return
# label check_cost:
    # $ playerhandcosts = []
    # python:
    #     for cards in playerhand2:
    #         playerhandcosts.append(cards)
    # $ playerhandminimumcost = min(playerhandcosts)
    # return

    # call Damageplayer(1.0)
    # return
image cardflash:
    "cardflasher"
    xalign 0.5 ypos 0.70 yanchor 0.5 zoom 0.9
    linear 0.05 zoom 1.2
    linear 0.05 zoom 1.1
image cardflash2:
    "cardflasher"
    xalign 0.5 ypos 0.70 yanchor 0.5
    zoom 1.1
    # linear 0.05 zoom 1.3
    # linear 0.05 zoom 1.2
image cardflashenemy:
    "cardflasher"
    xalign 0.5 ypos 0.38 yanchor 0.5 zoom 0.9
    linear 0.05 zoom 1.2
    linear 0.05 zoom 1.1
image cardflashenemy2:
    "cardflasher"
    xalign 0.5 ypos 0.38 yanchor 0.5 
    zoom 1.1

# define battlemusic_dict=
#     {
#         "Ave":"bgm/ost/BOSSBATTLE-A_by-Noyemi_K.ogg"
#         "Vira":"bgm/ost/BOSSBATTLE-A_by-Noyemi_K.ogg"
        
#         }
label playbattlemusic(e_name):
    
    if e_name=="Ave":
        play music "bgm/ost/BOSSBATTLE-A_by-Noyemi_K.ogg"
    elif e_name=="Vira":
        play music "<from 0 to 16.9>bgm/ost/BOSSBATTLE-V_by-StarryMarshmell_0.ogg"
        queue music "bgm/ost/BOSSBATTLE-V-Loop_by-StarryMarshmell_0.ogg"
        # queue music "bgm/ost/BOSSBATTLE-V-Loop_by-StarryMarshmell_0.ogg"
    elif e_name=="Code Red":
        play music "bgm/ost/BOSSBATTLE-C_by_StarryMarshmell_0.ogg"
    elif e_name=="Melissa":
        play music "bgm/ost/BOSSBATTLE-M_by_Walter_Chamod.wav"
    
    else:
        
        play music ""+renpy.random.choice(["bgm/Fight_bgm_maoudamashii_cyber14.ogg","bgm/ost/BATTLE_Common_by_Walter_Chamod.wav"])
        # play music "bgm/ost/BATTLE_Common.wav"
    return
label returncardfrombattlecode(cardobject,handindex):
    $ clickedcard[handindex] = False
    $ playerbits+=cardobject.COST
    $ playerbattlecode.remove(cardobject)
    $ usedcards.remove(handindex)
    return

label battlev3(PFAI=ILY,EFAI=Ave,pbitsMax=8,ebitsMax=8,turnlimit=100):
    if playerHP==0:
        return
    $ quick_menu=False
    $ evasion_active=False
    $ execution_active=False
    $ playerhand=[]
    $ ILY_w=True
    $ ILY_m="frown"
    $ ILY_e="down"
    $ ILY_p="0"
    $ battle_active=True
    $ battle_done=False
    $ playerName = PFAI.name
    # $ playerSP = PFAI.SP
    $ playerSP = 0
    $ playerATK = PFAI.ATK
    $ playerDEF = PFAI.DEF
    # if playerName == "ILY":
    if playerobject.name==PFAI.name:
        $ playerDeck = copy.deepcopy(deckcurrent)
    else:
        $ playerDeck = PFAI.deck["content"]
    $ actual_playerDeck = deckcurrent
    
    $ playerPlugins = playerPlugins =PFAI.deck["plugins"]
    $ first_turn_done =False

    python:
        hcount=0
        vcount=0
        ahcount=0
        avcount=0

        playerbits = pbitsMax
        enemybits= ebitsMax
        
        playerbitsmax=pbitsMax
        enemybitsmax=pbitsMax
        random.shuffle(playerDeck)
        battle_distance = 0
        battle_done = False
        enemyfirst =renpy.random.choice([True,False])
        map_active=False
        playerbattlecode=[]
        playerATK_m = playerATK
        playerDEF_m = playerDEF
        EnmySts = []
        PlayerSts = []
        # PlayerFAIstats = ILYStatsnow
        EnemyFAIstats = {
            "name":EFAI.name,
            "HP":EFAI.HP,
            "HPMAX":EFAI.SP,
            "SP":EFAI.SP,
            "SPMAX":EFAI.SP,
            "Deck":EFAI.deck,
            "ATK":EFAI.ATK,
            "DEF":EFAI.DEF

        }
        enemyName = EnemyFAIstats["name"]
        enemyHP = EnemyFAIstats["HP"]
        enemyHPMax = EnemyFAIstats["HP"]
        # enemySP = EnemyFAIstats["SP"]
        enemySP = 0
        enemySPMax = EnemyFAIstats["SPMAX"]
        enemyDeck = EnemyFAIstats["Deck"]["content"]
        enemyPlugins =EFAI.deck["plugins"]
        enemyATK = EnemyFAIstats["ATK"]
        enemyDEF = EnemyFAIstats["DEF"]
        enemyATK_m = enemyATK
        enemyDEF_m = enemyDEF
        random.shuffle(enemyDeck)
    # call battlebg_animation
    if enemyName in boss_list:
        call speedspikebg
        call screen VERSUS(playerName,enemyName)

    scene battlebg 
    show battlebg2 
    # with pixellate
    with dissolve_pixels
    call playbattlemusic(enemyName)
    
    show battlering:
        xalign 0.5 ypos 0.20 yanchor 0.5
        block:
            rotate 0
            linear 15.0 rotate 360
            repeat
    show curve:
        xpos 0.5 xanchor 0.0 ypos 0.15 yanchor 0.5
    show curve as curve2:
        xpos 0.5 xanchor 1.0 ypos 0.17 yanchor 0.5
        zoom -1.0

    show battleroad:
        yalign 1.0 xalign 0.5
    show Enemy:
        xalign 0.5 yanchor 0.32 ypos 0.3
        
    call start_battlecry(playerName)
    call start_battlecry(enemyName)
    
    # show screen decknum
    # with pixellate
    # show screen stats
    # show cardback at poscarddeck
    # label battleinit:


    show screen battlestats
    call showphasemsg("SOFTWAR BEGIN!") 
    #Start Dialogue
    $ phasenum=0
    python:
        import copy 
        playerPlugins = copy.deepcopy(PFAI.deck["plugins"])
    show screen phasemsg("PLUGIN PHASE")
    $ renpy.pause(0.9,hard=True)
    hide screen phasemsg
    call Plugins_Run
    $ turncount = 0
    $ turnlimit_over=False
    label battleloop:
        
        hide screen battlestats
        show screen battlestats
        $ turncount += 1
        show screen phasemsg("CYCLE #" + str(turncount))
        $ renpy.pause(0.9,hard=True)
        hide screen phasemsg
        if turncount>=turnlimit:
            $ turnlimit_over=True
            $ battle_done = True
        if not battle_done:
            pass

        if enemyfirst and (not first_turn_done):
            call enemyattack
            
            $ first_turn_done =True

            if not battle_done:
                jump battleloop
            elif battle_done:

                show screen phasemsg("BATTLE_END")
                $ renpy.pause(0.9,hard=True)
                hide screen phasemsg
                hide screen battlestats
                if playerHP<=0:
                    stop music
                    call lose 
                    return
                elif turnlimit_over:
                    show screen phasemsg("BATTLE_INTERRUPTED")
                    $ renpy.pause(0.9,hard=True)
                    hide screen phasemsg
                    hide screen battlestats
                    return
                else:
                    play music "bgm/bgm_maoudamashii_cyber16.mp3"
                    show Enemy:
                        linear 0.15 zoom 0.94
                        xoffset 0.12 yoffset 0.2 alpha 0.5
                        pause .05
                        xoffset 0.-17 yoffset 0.-17 alpha 0.8
                        pause .05
                        xoffset 0.13 yoffset 0.2 alpha 1.0
                        pause 0.1
                        xoffset 0.-19 yoffset 0.11
                        pause 0.1
                        xoffset 0.12 yoffset 0.2 alpha 0.5
                        pause .05
                        xoffset 0 yoffset 0
                        linear 0.1 zoom 0.8 alpha 0.0
                    $ renpy.pause(0.4,hard=True)
                    call win

        label playerturn:

        # elif battle_done:
        #     call showphasemsg("BATTLE_END")
            call showphasemsg(playerName+"'S TURN")
            $renpy.pause(0.9,hard=True)
            hide screen phasemsg
            
            call screen Activate_Battleware
            call remaininghand
            show screen handcardsscreen

            call drawcards from _call_drawcards
            
            play sound "sound/Phase.wav" channel 1
            pause 0.5
            python:

                clickedcard=[False,False,False,False,False]
            label Codephase:

                # call screen choosecardv3(playerhand)
                hide screen handcardsscreen
                $ battlecodestatus=True
                call screen choosecardv2
                
                call BattleReturns
                $ card1usable = (playercard1COST<=playerbits) and (clickedcard[0]==False)
                $ card2usable = (playercard2COST<=playerbits) and (clickedcard[1]==False)
                $ card3usable = (playercard3COST<=playerbits) and (clickedcard[2]==False)
                $ card4usable = (playercard4COST<=playerbits) and (clickedcard[3]==False)
                $ card5usable = (playercard5COST<=playerbits) and (clickedcard[4]==False)
                $ cardusable = (((card1usable) or (card2usable)) or ((card3usable) or (card4usable))) or (card5usable)
                if (playerbits > 0) and cardusable:
                    jump Codephase
                else:
                    show screen handcardsscreen
                    
                    call screen Execute
                    $ battlecodestatus=False
                    call BattleReturns
                    # if not enemyfirst:
                    #     call enemyattack
                #Execute button runs "Execution" label
            if not battle_done:
                jump battleloop
            elif turnlimit_over:
                show screen phasemsg("BATTLE_INTERRUPTED")
                $ renpy.pause(0.9,hard=True)
                hide screen phasemsg
                hide screen battlestats
                
                return
            elif battle_done:
                hide screen handcardsscreen
                $ playerDeck = sorted( actual_playerDeck,key=lambda x: x.NAME, reverse=False)
                show screen phasemsg("BATTLE_END")
                $ renpy.pause(0.9,hard=True)
                hide screen phasemsg
                hide screen battlestats
                if playerHP<=0:
                    stop music
                    call lose from _call_lose_1
                else:
                    play music "bgm/bgm_maoudamashii_cyber16.mp3"
                    show Enemy:
                        linear 0.15 zoom 0.94
                        xoffset 0.12 yoffset 0.2 alpha 0.5
                        pause .05
                        xoffset 0.-17 yoffset 0.-17 alpha 0.8
                        pause .05
                        xoffset 0.13 yoffset 0.2 alpha 1.0
                        pause 0.1
                        xoffset 0.-19 yoffset 0.11
                        pause 0.1
                        xoffset 0.12 yoffset 0.2 alpha 0.5
                        pause .05
                        xoffset 0 yoffset 0
                        linear 0.1 zoom 0.8 alpha 0.0
                    $ renpy.pause(0.4,hard=True)
                    call win from _call_win_1
    return

label BattleReturns:

    if _return=="card1":
        play sound "sound/Phase.wav" channel 2
        $ clickedcard[0] = True
        $ playerbits-=playercard1COST
        $ playerbattlecode.append(playercard1obj)
        $ usedcards.append(0)
    elif _return=="card2":
        play sound "sound/Phase.wav" channel 2
        $ clickedcard[1] = True
        $ playerbits-=playercard2COST
        $ playerbattlecode.append(playercard2obj)
        $ usedcards.append(1)
    elif _return=="card3":
        play sound "sound/Phase.wav" channel 2
        $ clickedcard[2] = True
        $ playerbits-=playercard3COST
        $ playerbattlecode.append(playercard3obj)
        $ usedcards.append(2)
    elif _return=="card4":
        play sound "sound/Phase.wav" channel 2
        $ clickedcard[3] = True
        $ playerbits-=playercard4COST
        $ playerbattlecode.append(playercard4obj)
        $ usedcards.append(3)
    elif _return=="card5":
        play sound "sound/Phase.wav" channel 2
        $ clickedcard[4] = True
        $ playerbits-=playercard5COST
        $ playerbattlecode.append(playercard5obj)
        $ usedcards.append(4)
    elif _return=="Return_card":
        if playerbattlecode != []:
            $ playerbattlecode.pop(-1)
    elif _return=="Execute":
        python:
            playerhandminus_usedcards = []
            for usedcardindex,cards_used in enumerate(usedcards):
                if not usedcardindex==cards_used:
                    playerhandminus_usedcards.append(playerhand[cards_used])
                    
                playerDeck.append(playerhand[cards_used])
        # $ usedcardsnum=len(usedcards)
        # $ decklength=len(playerDeck)
        # "returned [usedcardsnum] cards to the deck."
        # "deck length = [decklength]"
        call Execution
        # $ playerDeck=playerDeck+playerhandminus_usedcards
            # for cards_used in usedcards[::-1]:
            #     playerhand.pop(cards_used)
            #     playerDeck.append(playerhand[cards_used])
    if (playerHP<=0):
        return
    $ battle_active=False
    return

screen Execute:
    
    on "show":
        action Function(renpy.set_focus,"Execute", "Executebutton")
        
    imagebutton idle "gui/Execute.png" hover "gui/Execute_hover.png" action  Play("sound","sound/Execute.wav"), Return("Execute") xalign 0.5 yalign 0.95:
        id "Executebutton"
    key "K_BACKSPACE" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback()
    key "x" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback()
    key 'K_RETURN' action  Play("sound","sound/Execute.wav"), Hide("card6hover"),Return("Execute")
    key 'K_KP_ENTER' action  Play("sound","sound/Execute.wav"), Hide("card6hover"),Return("Execute")
    imagebutton idle "images/Cards/cardreturn.png" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback() hovered Show("card6hover"), Play("sound","sfx/select.wav") unhovered Hide("card6hover") xpos 0.86 xanchor 0.5 yalign 0.945
    # key 'z' action  Play("sound","sound/Execute.wav"), Hide("card6hover"),Return("Execute")
    # key 'Z' action  Play("sound","sound/Execute.wav"), Hide("card6hover"),Return("Execute")
screen phasemsg(Message):
    frame:

        xalign 0.5 yalign 0.5 xsize 1280 at phasetrans
        text "{b}{size=100}[Message]{/b}{/size}":
            style "statusoutlines_thick"
            xalign 0.5 yalign 0.5
            at phasetrans
screen battlemessagescreen(Message):
    # frame:

    frame:

        xalign 0.5 yalign 0.5 xsize 1280 at phasetrans3
        text "{b}{size=100}[Message]{/b}{/size}" :
            style "statusoutlines_thick"
            xalign 0.5 yalign 0.5
            at phasetrans3

    
transform phasetrans:
    on show:
        yzoom 0.0
        linear 0.08 yzoom 1.1
        linear 0.02 yzoom 1.0
    on hide:
        linear 0.1 yzoom 0.0
transform phasetrans2:
    on show:
        yzoom 0.0
        pause 0.2
        linear 0.06 yzoom 1.1
        linear 0.02 yzoom 1.0
    on hide:
        linear 0.1 yzoom 2.0 alpha 0.0
transform phasetrans3:
    on show:
        yzoom 0.0
        pause 0.2
        linear 0.06 yzoom 1.1
        linear 0.02 yzoom 1.0
    on hide:
        linear 0.1 xzoom 2.0 alpha 0.0

label showphasemsg(msg):
    show screen phasemsg(msg)
    $ renpy.pause(0.9,hard=True)
    hide screen phasemsg
    return
label battlemessage(msg):
    show screen battlemessagescreen(msg)
    $ renpy.pause(0.8,hard=True)
    hide screen battlemessagescreen
    return

transform zoomBattlecards:
    zoom 0.6
screen choosecardv2:
    if playerbattlecode!=[]:
        # if rollbackchanged:
        $ config.rollback_enabled = True
    else:
        $ config.rollback_enabled = False
        
    hbox:
        # xalign 0.5 yalign 0.92
        xpos 0.5 xanchor 0.5 ypos 0.98 yanchor 1.0
        spacing 4
        for cardindex in range(0,5):
            $ playercardobj = playerhand[cardindex]
            $ card_distance = 0.12
            $ cardxpos=0.26+(cardindex*card_distance)

            if (playerhand[cardindex].COST<=playerbits) and (clickedcard[cardindex]==False):
                ###TODO:: ADD HOVER DESCRIPTION Layered Images
                imagebutton idle CardDisplay(playercardobj):
                    action Play("sound","sound/Phase.wav"), Hide("cardhover"), Return("card"+str(cardindex+1))
                    hovered Play("sound","sfx/select.wav"), SetVariable("hoverFXN",playercardobj.FXN)
                    # Show("cardhover",cardobject=playercardobj,cardhoverxpos=cardxpos),
                    
                    unhovered SetVariable("hoverFXN",[])
                    # Hide("cardhover"),
                    at enlargehover_choosecard
                    # xpos cardxpos 
                    # xanchor 0.5 ypos 0.90 yanchor 0.5
                    ypos 0.98 yanchor 1.0
            elif (playerhand[cardindex].COST>playerbits) and (clickedcard[cardindex]==False):
                imagebutton idle CardDisplayDimmed(playercardobj):
                    action NullAction()
                    hovered Play("sound","sfx/select.wav"), SetVariable("hoverFXN",playercardobj.FXN)
                    # Show("cardhover",cardobject=playercardobj,cardhoverxpos=cardxpos),
                    
                    unhovered SetVariable("hoverFXN",[])
                    # Hide("cardhover"),
                    at enlargehover_choosecard
                    # xpos cardxpos 
                    # xanchor 0.5 ypos 0.90 yanchor 0.5
                    ypos 0.98 yanchor 1.0
                    
            # elif clickedcard[cardindex]:
            #     add "images/Cards/cardblank2.png" xpos cardxpos xanchor 0.5 yalign 0.945
            # else:
            #     add CardDisplay(playercardobj) xpos cardxpos xanchor 0.5 ypos 0.90 yanchor 0.5 at enlargehover_choosecard
                # add "images/Cards/cardblank2.png" at alpha08 xpos cardxpos xanchor 0.5 yalign 0.945
        

    if playerbattlecode!=[]:
        imagebutton idle "images/Cards/cardreturn.png" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback() hovered Show("card6hover"), Play("sound","sfx/select.wav") unhovered Hide("card6hover") xpos 0.86 xanchor 0.5 yalign 0.945
        key "K_BACKSPACE" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback()
        key "x" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback()
    else:
        add "images/Cards/cardblank2.png" xpos 0.86 xanchor 0.5 yalign 0.945
    # if hoverFXN!=[]:
    #     use card_tooltip_battle
image card_deck = "images/Cards/card_deck.png"
image card_deck_draw :
    "images/Cards/card_deck_draw.png"
    zoom 0.1 xoffset 0 yoffset 0 xalign 0.5 yalign 0.5
    linear 0.1 xoffset 30 yoffset 80 zoom 0.12
transform linger:
    pause 0.5
transform draw_out:
    on hide:
        linear 0.4 xoffset 70 yoffset 100
screen Activate_Battleware:
        use playerviewdraw
        
        
        use handcardsscreen("drawphase")
        # add "images/Cards/cardblank2.png" xpos 0.26 xanchor 0.5 yalign 0.945
        # add "images/Cards/cardblank2.png" xpos 0.38 xanchor 0.5 yalign 0.945
        # add "images/Cards/cardblank2.png" xpos 0.5 xanchor 0.5  yalign 0.945
        # add "images/Cards/cardblank2.png" xpos 0.62 xanchor 0.5 yalign 0.945
        # add "images/Cards/cardblank2.png" xpos 0.74 xanchor 0.5 yalign 0.945
        add "card_deck" at zoomtrans(0.1),linger xalign 0.5 yalign 0.5
        
        text "{size=70}{b}DRAW!{/size}{/b}" xpos 0.5 xanchor 0.5 yalign 0.5 at alphablinking:
            style "statusoutlines"
        key 'mouseup_1' action Return()
        key 'K_RETURN' action Return()
        key 'K_SPACE' action Return()
        key 'K_KP_ENTER' action Return()
        key 'K_SELECT' action Return()
        key 'K_LEFT' action Return()
        key 'K_RIGHT' action Return()
        key 'K_UP' action Return()
        key 'K_DOWN' action Return()
        key 'Z' action Return()
        key 'z' action Return()
        key 'dismiss' action Return()
transform alphablinking:
    ease 0.25 alpha 0.0
    ease 0.25 alpha 1.0
    repeat
image selectring:
    "images/Cards/selectring.png"
    rotate 0 zoom 1.4
    linear 4.0 rotate 360
    repeat


screen cardhover(cardobject,cardhoverxpos):
    image CardDisplay(cardobject) xanchor 0.5 xpos cardhoverxpos yalign 0.92 at cardtrans
screen card6hover:
    # image "selectring" xanchor 0.5 xpos 0.86 yanchor 0.5 ypos 0.75
    image "images/Cards/cardreturn.png" xanchor 0.5 xpos 0.86 yalign 0.945 at cardtrans2


image zenny:
    "gui/zenny_big.png"
    xalign 0.5 yalign 0.5
label Battledrops:
    python:
        gainitems=[]
        # scene mainbg 
        for item in battledrops[enemyName]:
            shopitem = shop_item(item.NAME,item,"Material",0)
            for gain_num in range(0,renpy.random.choice([0,0,0,0,1,1,1,2,2,3])):
                gainitems.append(shopitem)
        Moneygain = renpy.random.choice([40,50,100,100,400,500,250,250])
        Money+=Moneygain
    play sound "sound/loadcard.wav"
    show zenny with dissolve_pixels
    $ renpy.say(info,"Gained "+str(Moneygain)+" Zenny! \nTotal Zenny: [Money]")
    hide zenny
    call GainItem(gainitems)

    return

label win:
    #MAKE VICTORY ANIMATION
    # show ILY_byTorakun14:
    #   xalign 0.0
    $ battle_done = True
    $ quick_menu=True
    show screen phasemsg("VICTORY!")
    pause 0.8
    hide screen phasemsg
    show screen VICTORY
    info"[playerName] Wins!" 
    hide screen VICTORY
    call Battledrops
    # "VICTORY!"
    #BATTLE DROPS
    return
label lose:
    $ okdesktop = False
    $ quick_menu=False

    hide screen mapA
    hide screen mapB
    scene ILYgameover with pixellate
    pause
    scene black with pixellate
    "Thank you for playing SoftWar!"

return
