
screen VERSUS2(playerName,enemyName):

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
screen playersprite(yvalue):
    zorder yvalue
    imagebutton idle "images/Characters/ILY/ILY[direction].png" action Return("Pause") xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 1.0 at playerjump(jumphght), blockSizetrans(blockSize) #zorder maplayering(playerypos)
init python:
    [
    #    0 1 2 3 4 5
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
    ]
    
    playerbattlepos=(1,1)
screen battlegrid:
    timer 0.05 action check_inputs
    grid 6 3:
        for tiles in range(): 
            add "gui/bn/tile.png" 
            add image (Null(height=154,width=114) if evasion_active else "Icon_[playerName]") at zoomtrans(0.8)
screen battlestatsbn():
    
    $ playerbitsfirsthalf= (int(playerbitsmax/2) if (playerbits-int(playerbitsmax/2))>0 else playerbits)
    $ playerbitssecondhalf=(0 if playerbits<=int(playerbitsmax/2) else playerbits-playerbitsfirsthalf)
    $ enemybitsfirsthalf=  (int(enemybitsmax/2) if (enemybits-int(enemybitsmax/2))>0 else enemybits)
    $ enemybitssecondhalf= (0 if enemybits<=int(enemybitsmax/2) else enemybits-enemybitsfirsthalf)
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
                        
    frame:
        style_prefix "statsb"
        xsize 380 ysize 120
        ypos 0.60 yanchor 0.5
        at battlecode_trans(focused=battlecodestatus)
        
        vbox:
            vbox:
                text "{size=14}{b}CODE{/size}{/b}" xalign 0.0
                hbox:

                    xalign 0.0

                    for cards in playerbattlecode:
                        add "images/Cards/[cards.NAME].png" at codesize
                    for fillers in range(0,5-len(playerbattlecode)):

                        add "images/Cards/Empty.png" at codesize
            null height 5
            

#         }

label battlev4(PFAI=ILY,EFAI=Ave,pbitsMax=8,ebitsMax=8):
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
        call screen VERSUS2(playerName,enemyName)

    scene battlebg
    show battlebg2
    with pixellate
    call playbattlemusic(enemyName)
    # show Enemy:
    #     xalign 0.5 yanchor 0.32 ypos 0.3
        
    call start_battlecry(playerName)
    call start_battlecry(enemyName)
    


    show screen battlestatsbn
    call showphasemsg("SOFTWAR BEGIN!") 
    #Start Dialogue
    $ phasenum=0
    python:
        import copy 
        playerPlugins = copy.deepcopy(PFAI.deck["plugins"])
    call Plugins_Run
    label battleloop2:
        show screen battlegrid
        hide screen battlestatsbn
        show screen battlestatsbn

        if not battle_done:
            pass

        if enemyfirst and (not first_turn_done):
            # call enemyattack
            
            $ first_turn_done =True

            if not battle_done:
                jump battleloop2
            elif battle_done:

                show screen phasemsg("BATTLE_END")
                $ renpy.pause(0.9,hard=True)
                hide screen phasemsg
                hide screen battlestatsbn
                if playerHP<=0:
                    stop music
                    call lose 
                    return
                else:
                    play music "bgm/bgm_maoudamashii_cyber16.mp3"
                    # show Enemy:
                    #     linear 0.15 zoom 0.94
                    #     xoffset 0.12 yoffset 0.2 alpha 0.5
                    #     pause .05
                    #     xoffset 0.-17 yoffset 0.-17 alpha 0.8
                    #     pause .05
                    #     xoffset 0.13 yoffset 0.2 alpha 1.0
                    #     pause 0.1
                    #     xoffset 0.-19 yoffset 0.11
                    #     pause 0.1
                    #     xoffset 0.12 yoffset 0.2 alpha 0.5
                    #     pause .05
                    #     xoffset 0 yoffset 0
                    #     linear 0.1 zoom 0.8 alpha 0.0
                    $ renpy.pause(0.4,hard=True)
                    call win

        label playerturn2:

            call showphasemsg(playerName+"'S TURN")
            $renpy.pause(0.9,hard=True)
            hide screen phasemsg
            
            call screen Activate_Battleware
            call remaininghand
            show screen handcardsscreen

            call drawcards
            
            play sound "sound/Phase.wav" channel 1
            pause 0.5
            python:

                clickedcard=[False,False,False,False,False]
            label Codephase2:

                hide screen handcardsscreen
                call screen choosecardv4
                
                call BattleReturns
                $ card1usable = (playercard1COST<=playerbits) and (clickedcard[0]==False)
                $ card2usable = (playercard2COST<=playerbits) and (clickedcard[1]==False)
                $ card3usable = (playercard3COST<=playerbits) and (clickedcard[2]==False)
                $ card4usable = (playercard4COST<=playerbits) and (clickedcard[3]==False)
                $ card5usable = (playercard5COST<=playerbits) and (clickedcard[4]==False)
                $ cardusable = (((card1usable) or (card2usable)) or ((card3usable) or (card4usable))) or (card5usable)
                if (playerbits > 0) and cardusable:
                    jump Codephase2
                else:
                    show screen handcardsscreen
                    $ battlecodestatus=True
                    call screen Execute2
                    $ battlecodestatus=False
                    call BattleReturns
            if not battle_done:
                jump battleloop2
            elif battle_done:
                hide screen handcardsscreen
                $ playerDeck = sorted( actual_playerDeck,key=lambda x: x.NAME, reverse=False)
                show screen phasemsg("BATTLE_END")
                $ renpy.pause(0.9,hard=True)
                hide screen phasemsg
                hide screen battlestatsbn
                if playerHP<=0:
                    stop music
                    call lose
                else:
                    play music "bgm/bgm_maoudamashii_cyber16.mp3"
                    # show Enemy:
                    #     linear 0.15 zoom 0.94
                    #     xoffset 0.12 yoffset 0.2 alpha 0.5
                    #     pause .05
                    #     xoffset 0.-17 yoffset 0.-17 alpha 0.8
                    #     pause .05
                    #     xoffset 0.13 yoffset 0.2 alpha 1.0
                    #     pause 0.1
                    #     xoffset 0.-19 yoffset 0.11
                    #     pause 0.1
                    #     xoffset 0.12 yoffset 0.2 alpha 0.5
                    #     pause .05
                    #     xoffset 0 yoffset 0
                    #     linear 0.1 zoom 0.8 alpha 0.0
                    $ renpy.pause(0.4,hard=True)
                    call win
    return

label BattleReturns2:

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
        call Execution
    if (playerHP<=0):
        return
    $ battle_active=False
    return

screen Execute2:
    
    on "show":
        action Function(renpy.set_focus,"Execute", "Executebutton")
        
    imagebutton idle "gui/Execute.png" hover "gui/Execute_hover.png" action  Play("sound","sound/Execute.wav"), Return("Execute") xalign 0.5 yalign 0.95:
        id "Executebutton"
    key "K_BACKSPACE" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback()
    key "x" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback()
    key 'K_RETURN' action  Play("sound","sound/Execute.wav"), Hide("card6hover"),Return("Execute")
    key 'K_KP_ENTER' action  Play("sound","sound/Execute.wav"), Hide("card6hover"),Return("Execute")
    imagebutton idle "images/Cards/cardreturn.png" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback() hovered Show("card6hover"), Play("sound","sfx/select.wav") unhovered Hide("card6hover") xpos 0.86 xanchor 0.5 yalign 0.945

screen choosecardv4:
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
                    unhovered SetVariable("hoverFXN",[])
                    at enlargehover_choosecard
                    ypos 0.98 yanchor 1.0
            elif (playerhand[cardindex].COST>playerbits) and (clickedcard[cardindex]==False):
                imagebutton idle CardDisplayDimmed(playercardobj):
                    action NullAction()
                    hovered Play("sound","sfx/select.wav"), SetVariable("hoverFXN",playercardobj.FXN)

                    unhovered SetVariable("hoverFXN",[])
                    at enlargehover_choosecard
                    ypos 0.98 yanchor 1.0
                    

    if playerbattlecode!=[]:
        imagebutton idle "images/Cards/cardreturn.png" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback() hovered Show("card6hover"), Play("sound","sfx/select.wav") unhovered Hide("card6hover") xpos 0.86 xanchor 0.5 yalign 0.945
        key "K_BACKSPACE" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback()
        key "x" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback()
    else:
        add "images/Cards/cardblank2.png" xpos 0.86 xanchor 0.5 yalign 0.945
    # if hoverFXN!=[]:
    #     use card_tooltip_battle
return
