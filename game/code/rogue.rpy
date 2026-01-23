#################
##################
# default game_over=False
# default battle_active=False
define FAI_playables=[ILY, Ave, CodeRed]
default game_win=False


default r_Bosses=[ILYAlpha, Ave, CodeRed, Melissa, Vira]

# playerDeck = PlayerStatsnow["Deck"]
#     actual_playerDeck = playerDeck
init python:
    def FAI_card(FAI_object):
        return Composite((1394, 2031),
            (0,0), "images/Special Images/Card_"+FAI_object.name+".png",
            # (0,0), At("card_highlights", card_highlights_t),
            (0,0), AlphaMask(At(("card_gradient"), card_gradient_t,zoomtrans(2.0)), "images/Special Images/Card_"+FAI_object.name+".png"))
# image FAI_card_ILY:

#     "images/Special Images/Card_ILY.png"
#     FAI_card(ILY)
# image FAI_card_Ave:
#     "images/Special Images/Card_Ave.png"
# image FAI_card_Code Red:
#     "images/Special Images/Card_CodeRed.png"
# image FAI_card_Vira:
#     "images/Special Images/Card_Vira.png"
transform enlargehover:
    zoom 1.0 
    on hover:
        ease 0.2 zoom 1.5
    on selected_hover:
        ease 0.2 zoom 1.5
    on idle:
        ease 0.2 zoom 1.0
    on selected_idle:
        ease 0.2 zoom 1.5
transform enlargehover_choosecard:
    zoom 0.6 ypos 0.94 yanchor 1.0
    on show:
        zoom 0.6 
    on hover:
        ease 0.2 zoom 1.0
    on selected_hover:
        ease 0.2 zoom 1.0
    on idle:
        zoom 0.6
    on selected_idle:
        ease 0.2 zoom 1.0
transform enlargehover_choosecard_treasure:
    zoom 0.8 ypos 0.5 yanchor 0.5
    on show:
        zoom 0.8 
    on hover:
        ease 0.2 zoom 1.2
    on selected_hover:
        ease 0.2 zoom 1.2
    on idle:
        zoom 0.8
    on selected_idle:
        ease 0.2 zoom 1.2

screen CharacterCardSelect(character_choices=[ILY,Ave]):
    frame:
        xalign 0.5 yalign 0.02
        text "CHOOSE YOUR FIGHTER!" style "statusoutlines"
    hbox:
    
        xalign 0.5 yalign 0.5
        spacing 80
        for characters in character_choices:
            $ charactername = characters.name
            button:
                at enlargehover
                xsize 279
                ysize 406
                xalign 0.5 yalign 0.5
                background At((FAI_card(characters)), zoomtrans(0.4))
                # hover_background At(("FAI_card_"+charactername),rotate_object_t, zoomtrans(0.2),enlargehover)
                action SetVariable("playerobjectset",characters),Return()
default playerobject=ILY
default playerobjectset=""
default rogue_stage=1
label roguemode:
    play music "bgm/Roam_game_maoudamashii_5_town18.mp3"
    scene mainbg with pixellate
    call screen CharacterCardSelect([ILY,Ave,CodeRed])
    $ playerobject=playerobjectset
    python:
        PFAI = playerobject
        if playerobject in r_Bosses:
            r_Bosses.remove(playerobject)
            playerobject
        mydeck=PFAI.deck
        deckplugin =mydeck["plugins"]
        plugincurrent =sorted( mydeck["plugins"],key=lambda x: x.NAME, reverse=False)
        deckcurrent =sorted( mydeck["content"],key=lambda x: x.NAME, reverse=False)
        mydeckname =  mydeck["name"]
       
        statuslist=["BoostATK","BoostDEF","Email"]
        playerbits = 8
        playerName = PFAI.name
        playerHP = PFAI.HP
        playerHPMax = PFAI.HP
        playerSP = 0
        playerSPMax = PFAI.SP
        playerATK = PFAI.ATK
        playerDEF = PFAI.DEF

        actual_playerDeck = playerDeck
        playerPlugins =PFAI.deck["plugins"]
        fxnindex=0
        execution_active=False
        enemy_evasion_active=False
        evasion_active=False
        battle_done = False
        enemyfirst =False
        map_active=False
        playerbattlecode=[]
        game_win==False
    # $ r_Bosses=FAI_playables
        node_current=(0,0)
    if playerName=="ILY":
        show ILY
        $ John_m="frown"
        $ John_e="mad"
        i "John! The Undernet Labyrinth at the depths of Connecht City... A gate to it has emerged from the ground!"
        j "This is the Mother Virus at work! It's time to fight, ILY!"
        i "Right on!"
        j "Be careful in there! We could be in serious trouble.."
        i "I'll be fine, I know you're there to watch out for me!"
        j "That's right."


    elif playerName=="Ave":
        $ inventory_dress=[]
        show Ave
        $ Lucida_m="frown"
        $ Lucida_w=True
        
        a "I'm detecting severe virus activity right at this point. "
        a "A gate to The Undernet? This must be it." 
        a "A maze, a castle, a dungeon.. Nothing will be able to stop me!"
        a "I will have my revenge!"
        lc "Calm down, let's focus on the task at hand, Ave."
        lc "I don't doubt your abilities, but I urge you to take care."
        a "Affirmative, Ms. Lucida."
    elif playerName=="Code Red":
        $ inventory_dress=[]
        show CodeRed
        c "An Undernet Labyrinth at the depths of Connecht City..."
        c "I know I usually fight for bounty and all, but this actually seems like a challenge I'd enjoy."
        c "Let's get this over with."

    scene gridbglandscape1 with pixellate:
        zoom 0.75
    $ Brain_w=False
    show Brain
    br "Welcome.."
    br "I am the mother of all FAI Viruses."
    br "Connecht's entire network is now under my control."
    br "Challengers... Face me!"
    br "This Undernet Labyrinth is my magnum opus!"
    $ boss_index=1
    label rogue_game_loop:
        
        call roguestage
        if boss_index==len(r_Bosses) and Boss_defeated:
            $ game_win=True
    if not game_over:
        jump rogue_game_loop
    if game_win and  game_over:

        call showphasemsg("YOU WIN!!")
        pause
        call showphasemsg("CONGRATS")
        pause
        call showphasemsg("ON BEATING")
        pause
        call showphasemsg("SOFTWAR")
        pause
        
    
    return
image mainbg = "gui/main_menu/main menu bglayer1.png"
label roguestage:
    scene mainbg with pixellate
    $ node_current=(-1,0)
    if r_Bosses==[]:
        "CAMPAIGN CLEARED"
        $ game_win=True
        $ Boss_defeated=True
        $ game_over=True
        return
    else:
        call showphasemsg("Stage "+str(boss_index)+"")
        $ stageboss=renpy.random.choice(r_Bosses)
        $ r_Bosses.remove(stageboss)
        if boss_index==1:
            call r_battlestart
    label newnodes:
        play music "bgm/ost/Serious_Noyemi_K.ogg"
        scene mainbg 
        
        if Boss_defeated:
            
            "Stage [boss_index] complete."
            $ Boss_defeated=False
            $ boss_index+=1
            return
        else:
            call screen roguenodeselect
        if _return=="R_player_talks":
            call R_player_talks
            jump newnodes
        elif _return=="pausemenu":
            call pauseshow
        elif _return=="items":
            $ inventory= sorted( inventory,key=lambda x: x.NAME, reverse=False)
            label Itemscreen_r:
                $ noscreentransformsfornow=False
                call screen Items
                # if _return=="Return":
                #     $ pausemenu =False
                    
                #     return
                # elif _return!="Return":
                #     # jump pauseshow
                #     jump Itemscreen_r
                
                # if _return=="Open":
                #     call OpenItem(messageview["sender"],messageview["subject"],messageview["body"]) from _call_OpenItem
                #     jump Itemscreen_r
                # elif _return!="Open":
                #     jump Itemscreen_r
        elif _return=="deck_edit":
            python:
                deck_unedited=copy.deepcopy(sorted( deckcurrent,key=lambda x: x.NAME, reverse=False))
                card_inventory_unedited=copy.deepcopy(sorted( card_inventory,key=lambda x: x.NAME, reverse=False))
            label Battleware_edit_screen2:
                call screen Battleware_Edit
                if _return=="SaveDeck":
                    call SaveDeck
                elif _return=="UnsaveDeck":
                    call UnsaveDeck

                else:
                    jump Battleware_edit_screen2
        elif _return=="Return":
            $ pausemenu =False
        if not game_over: 
            jump newnodes
    return
default nodes_path=[]

init python:
    
    class Node:
        def __init__(self,NAME,TYPE,LABEL):
            self.NAME = NAME
            self.TYPE = TYPE
            self.LABEL = LABEL
    Enemy=Node("Mob Virus", "Enemy","R_Enemy")
    StrongEnemy=Node("Rogue Virus", "StrongEnemy","R_StrongEnemy")
    Treasure=Node("Treasure", "Treasure","R_TreasureNode")
    
    Unknown=Node("Unknown", "Unknown","R_UnknownNode")
    Recovery=Node("Recovery", "Recovery","R_RecoveryNode")
    StellaShop=Node("Stella's Shop", "Shop","R_StellaShop")
    Boss=Node("Boss", "Boss","R_Boss")
    
    def random_node(used_nodes):
        global nodes_tpf
        choicenodes=nodes_tpf
        newnode = renpy.random.choice(choicenodes)
        nodes_tpf.remove(newnode)
        return newnode

    def generate_treasures():
        global treasure_tpf
        newtreasurelist=[]
        for tx in range(0,3):
            # newtreasure = renpy.random.choice(treasure_tpf)
            add_treasure=False
            newtreasure=0
            while not add_treasure:
                newtreasure = renpy.random.choice(treasure_tpf)
                
                if newtreasure in newtreasurelist:
                    add_treasure=False
                else:
                    newtreasurelist.append(newtreasure)
                    add_treasure=True
        # treasure_battleware_list = {item.NAME:shop_item(item.NAME,item,"Battleware",pricelist[item.NAME]) for item in battleware_list}

        # treasure_tpf.remove(newnode)

        return newtreasurelist

label R_Enemy:
    call showphasemsg("ENCOUNTER: Virus!")
    $ enemyvirus = renpy.random.choice([Keylogger,Worm,Spyware])
    $ enemyobject= enemyvirus
    call battlev3(playerobject,enemyobject)
    
    if playerHP==0:
        $ game_over=True
    call R_TreasureNode
    return
label R_StrongEnemy:
    call showphasemsg("ENCOUNTER: Rare Virus")
    $ enemyvirus = renpy.random.choice([Ransomware,Rootkit,Trojan])
    $ enemyobject= enemyvirus
    
    call battlev3(playerobject,enemyobject)
    if playerHP==0:
        $ game_over=True
    call R_TreasureNode
    return
init python:
    def choosetreasurecard(cardtreasure):
        global selected_treasure
        itemquantity=1
        selected_treasure =cardtreasure
        renpy.call("GainItem",[cardtreasure]*itemquantity)
        
        return 
screen SelectNewTreasure(treasurelist):
    # choosetreasurecard 
    text "Select a card to Download!":
        xalign 0.5 yalign 0.1
        style "statusoutlines"
    hbox:
        # xalign 0.5 yalign 0.92
        xpos 0.5 xanchor 0.5 ypos 0.5 yanchor 0.5
        spacing 40
        for cardtreasure in treasurelist:
            $ playercardobj = treasurelist[cardtreasure].object
            $ shopobj = treasurelist[cardtreasure]
            
            $ card_distance = 0.12
            # $ cardxpos=0.26+(cardindex*card_distance)

            # if (playercardobj.COST<=playerbits) and (clickedcard[cardindex]==False):
            #     ###TODO:: ADD HOVER DESCRIPTION Layered Images
            imagebutton idle CardDisplay(playercardobj):
                action Play("sound","sound/Phase.wav"), Hide("cardhover"), Function(choosetreasurecard,shopobj),SetVariable("selected_treasure",playercardobj),Return()
                hovered Play("sound","sfx/select.wav"), SetVariable("hoverFXN",playercardobj.FXN)
                # Show("cardhover",cardobject=playercardobj,cardhoverxpos=cardxpos),
                
                unhovered SetVariable("hoverFXN",[])
                # Hide("cardhover"),
                at enlargehover_choosecard_treasure
                # xpos cardxpos 
                # xanchor 0.5 ypos 0.90 yanchor 0.5
                ypos 0.5 yanchor 0.5
            # elif (playercardobj.COST>playerbits) and (clickedcard[cardindex]==False):
            #     imagebutton idle CardDisplayDimmed(playercardobj):
            #         action NullAction()
            #         hovered Play("sound","sfx/select.wav"), SetVariable("hoverFXN",playercardobj.FXN)

            #         unhovered SetVariable("hoverFXN",[])
            #         at enlargehover_choosecard_treasure

            #         ypos 0.5 yanchor 0.5

default selected_treasure=GUNVAR

label R_TreasureNode:
    scene mainbg with dissolve_pixels
    call showphasemsg("DATA TREASURE")
    $ new_treasure=generate_treasures()
    $ new_treasure_battleware_list = {item.NAME:shop_item(item.NAME,item,"Battleware",pricelist[item.NAME]) for item in new_treasure}
    
    call screen SelectNewTreasure(new_treasure_battleware_list)
    
    $ newcard=selected_treasure.name
    $ currentcard=(selected_treasure.object)
    play sound "sound/loadcard.wav"
    show cardflasher with dissolve_pixels:
        xalign 0.5 yalign 0.46
    "You got: [newcard]!"
    return

label R_UnknownNode:
    scene mainbg with dissolve_pixels
    call showphasemsg("DATA TREASURE")
    $ new_treasure=generate_treasures()
    $ new_treasure_battleware_list = {item.NAME:shop_item(item.NAME,item,"Battleware",pricelist[item.NAME]) for item in new_treasure}
    
    call screen SelectNewTreasure(new_treasure_battleware_list)
    
    $ newcard=selected_treasure.name
    $ currentcard=(selected_treasure.object)
    play sound "sound/loadcard.wav"
    show cardflasher with dissolve_pixels:
        xalign 0.5 yalign 0.46
    "You got: [newcard]!"
    return
screen playerwidget:
    button:
        xsize 400
        background ("[playerName]")
        yanchor 0.7 ypos 1.0 xalign 0.5
        at pausetrans1, zoomtrans(0.8)
        action Return("R_player_talks")
    frame:
        xalign 0.5 yalign 0.5
        if not notransform:
            at pausetrans1
        style "pausestats_r"
        
        hbox:
            null width 4
            vbox:
                text "{b}[playerName]{/b}"
                null height 7
                fixed:
                    frame:
                        style_prefix "healthbar"
                        xsize bar_size(playerHP,playerHPMax, 420)
                    hbox:
                        null width 40
                        text "HP: [playerHP]/[playerHPMax]"
                    vbox:
                        null height 32
                        hbox:

                            frame:
                                style "deckframe"
                                text "{size=14}Deck: [mydeckname]{/size}"
                            
                            frame:
                                style "deckframe"
                                text "{size=14}ATK: [playerATK] DEF: [playerDEF] {/size}"
                            
                        frame:
                            xminimum 460
                            style "deckframe"
                            text "{size=16}Money: [Money] {image=gui/zenny.png} Zennys{/size}"

                null height 10
label R_RecoveryNode:
    show screen playerwidget
    menu:
        "Would you like to recover 1000 HP?"
        "Yes":
            python:
                renpy.play("sfx/healx.ogg","sound")
                healexcess=(playerHP+1000-playerHPMax)
                healvalue=(1000)
                if healexcess>0:
                    healvalue-=healexcess
                playerHP+=healvalue
                if playerHP>playerHPMax:
                    playerHP=playerHPMax

                renpy.notify("Healed "+str(healvalue)+" HP.")
            "You are healed. Goodbye!"
        "No":
            "Alright."
    hide screen playerwidget
    return
label R_StellaShop:
    $ Stoned_m="open2"
    $ Stoned_e="up"
    $ Stoned_eyes="open"
    
    $ shop_page=0
    s"What do you want?"
    $ Stoned_m="happy"
    $ Stoned_e="normal"
        
    $ shop_active=True
    $ Stoned_w = False

    show screen item_shop()
    $ renpy.set_focus("item_shop", "shop_button0")

    while shop_active:
        window hide
        # show screen shop_image()


        pause
        hide screen shop_prompt
        # hide screen item_shop
        # if _return =="ItemModal":
        #     # show screen shop_image
        #     $ notransform=True
        #     $ noscreentransformsfornow=True
        #     call screen ItemModal

    hide screen shop_image
    hide screen item_shop
    $ say_shop_mode=False
    $ Stoned_w = True

    return
default Boss_defeated=False
label R_Boss:
    $ enemyobject= enemyvirus

    call battlev3(playerobject, stageboss)
    if playerHP==0:
        $ game_over=True
    else:
        $ Boss_defeated=True
    
    
    return
label r_battlestart:
    python:
        nodes_path=[]
        ILY_m="smile3"
        used_nodes=[]
        nodes_tpf=[Enemy]*8+[StrongEnemy]*2+[Unknown,Unknown,Treasure,Recovery,StellaShop]
        treasurebattleware =[
            GearframeUnitron,
            NucleusVernier,
            AccelRiser,
            VirusFlame,
            SaberAura,
            Katana,
            Laserbeam,
            LambdaSaber,
            DataForce,
            Shieldbit,
            RecursiveSlash,
            DataSaber,
            SaberDeflect,
            BlockSaber,
            DataBuster,
            DataBomb,
            WindBlast,
            Tackle,
            ]
        treasure_tpf=treasurebattleware
        nodes_path.append([Enemy])
        used_nodes.append(Enemy)
        for nodes in range(1,5):
            # nodes_path.append([random_node(),random_node()])
            newnoderow=[]
            for nodeitems in range(nodes+1):
                newrandomnode=random_node(used_nodes)
                if newrandomnode not in used_nodes:
                    used_nodes.append(newrandomnode)
                newnoderow.append(newrandomnode)
            nodes_path.append(newnoderow)
        nodes_path.append([Boss])
        # r_Bosses.remove(playerobject)
        


    return
init python:
    def nodechoices(pos_tuple):
        node_x=pos_tuple[1]
        node_y=pos_tuple[0]
        node_choice1=(node_x,node_y+1,)
        node_choice2=(node_x+1,node_y+1)
        list_node_choice=[]
        if node_y==4:
            list_node_choice=[(0,5)]
        else:
            list_node_choice=[node_choice1,node_choice2]
        #   nodechoices(1,1)

        return list_node_choice
    def change_node(nodechoice,node_item):
        global node_current
        node_current=nodechoice
        nodelabel=node_item.LABEL
        renpy.call(""+nodelabel)
        return node_current
    def open_node(nodechoice,node_item):
        global node_current
        # node_current=nodechoice
        nodelabel=node_item.LABEL
        renpy.call(""+nodelabel)
        return node_current
    def check_choice(n_index_1,n_index_2):
        # nodechoices((n_index_2,n_index_1))[0]==n_index_2 and nodechoices((n_index_2,n_index_1))[1]
        if (n_index_2,n_index_1) in nodechoices((node_current[0],node_current[1])):

            return True
        else:
            return False
default r_talks=0
label R_player_talks:
    $ renpy.call("r_talks_"+(playerName if playerName!="Code Red" else "CodeRed")+"_"+str(r_talks))
    # if playerName=="ILY":
        
        
    # if playerName=="Ave":
    #     a"Let's get going."
    # if playerName=="Code Red":
    #     c"Let's get going."
    $ r_talks+=1
    if r_talks==3:
        $ r_talks=0
    return
label r_talks_ILY_0:
    show ILY with dissolve
    i "Have you optimized the battleware deck yet?"
    i "Try some new cards out by using the Deck Construction menu!"
    return
label r_talks_ILY_1:
    show ILY with dissolve
    $ John_m="frown"
    j "Why do you wear a heart-shaped monocle?"
    i "Oh this? It's a tool to help me to understand more about others!"
    $ John_e="up"
    j "So... battle analysis?"
    i "Not just for battle! It's rose-colored, you know. It's poetic."
    $ John_m="O"
    j "... Oh, I kind of get it now."

    return
label r_talks_ILY_2:
    show ILY with dissolve
    $ ILY_m = "frown"
    $ ILY_e = "down"
    i "The original version of me is roaming in this labyrinth."
    $ John_m="frown"
    $ John_e="mad"
    
    j "Yikes. You think we can take her on?"
    i "She's a ruthless one. "
    $ ILY_m = "smile3"
    $ ILY_e = "down"
    extend "But she lacks the resolve of the romantic hero!"
    i "She is the old me. I'm not about to back out against my past!"
    j "Something tells me you're eager to prove her wrong."
    $ John_m="smile"
    j "That's good. But you have to stay focused."

    return

label r_talks_Ave_0:
    show Ave with dissolve
    a "Have you optimized the battleware deck yet?"
    a "Try some new cards out by using the Deck Construction menu!"
    return
label r_talks_Ave_1:
    show Ave with dissolve
    $ Lucida_m="frown"
    $ Lucida_e="down"
    l "We're up against a horde of viruses now."
    a "I can handle all of them no problem..."
    l "Good."    
    return
label r_talks_Ave_2:
    show Ave with dissolve
    a "Miss Lucida, I never got the chance to ask."
    $ Lucida_m="frown"
    $ Lucida_e="down"
    l "We're up against a horde of viruses now."
    a ""
    
    return
screen roguenodeselect():
    # text str(node_current) xalign 0.75 yalign 0.75
    hbox:
        xpos 0.52 ypos 0.87
        button:
            action Return("pausemenu")
            hover_background Frame("gui/framew_hover.png", 10, 10)
            background Frame("gui/framew.png", 10, 10)
            # top_padding 52
            bottom_padding 20
            right_padding 26
            left_padding 26
            text "Menu"
        button:
            action Return("items")
            hover_background Frame("gui/framew_hover.png", 10, 10)
            background Frame("gui/framew.png", 10, 10)
            # top_padding 52
            bottom_padding 20
            right_padding 26
            left_padding 26
            text "Items"
        
        button:
            action Return("deck_edit")
            hover_background Frame("gui/framew_hover.png", 10, 10)
            background Frame("gui/framew.png", 10, 10)
            # top_padding 52
            bottom_padding 20
            right_padding 26
            left_padding 26
            text "Deck Construction"

    button:
        xsize 400
        ysize 700
        background ("[playerName]")
        yanchor 1.0 ypos 1.0 
        at pausetrans1, zoomtrans(0.8)
        action Return("R_player_talks")
    text "Stage "+str(boss_index)+" Boss: "+str(stageboss.name) xalign 0.5 yalign 0.1

    hbox:
        # spacing 80
        xalign 0.9 yalign 0.5
        for n_index_1,nodes in enumerate(nodes_path):
            vbox:
                spacing 10
                xalign 0.5 yalign 0.5
                if n_index_1==5:
                    # null width (422*0.2)
                    add "gui/connector2.png" xalign 0.5 yalign 0.5
                else:
                    for node_item in range(0,len(nodes)-1):
                        add "gui/connector.png" xalign 0.5 yalign 0.5
            vbox:
                spacing 10
                xalign 0.5 yalign 0.5
                for n_index_2,node_item in enumerate(nodes):
                    vbox:
                        
                        xalign 0.5 yalign 0.5
                        if (check_choice(n_index_1,n_index_2)):
                            imagebutton:
                                idle Composite(
                                    (84,84),
                                    (0,0),("gui/"+node_item.TYPE+".png"),
                                    (0,0),(("gui/selector2.png")))  
                                hover Composite(
                                    (84,84),
                                    (0,0),("gui/"+node_item.TYPE+".png"),
                                    (0,0),(("gui/selector2.png")),
                                    (0,0),("blinky"))
                                # at zoomtrans(0.2)
                                action Function(change_node,(n_index_1,n_index_2),node_item),Return()
                        elif node_current==(n_index_1,n_index_2) and node_item.TYPE!="Shop":
                            imagebutton:
                                idle Composite(
                                    (84,84),
                                    (0,0),("gui/"+node_item.TYPE+".png"),
                                    (0,0),(("gui/selector.png")))
                                # at zoomtrans(0.2)
                                action NullAction()
                        elif node_current==(n_index_1,n_index_2) and node_item.TYPE=="Shop":
                            imagebutton:
                                idle Composite(
                                    (84,84),
                                    (0,0),("gui/"+node_item.TYPE+".png"),
                                    (0,0),(("gui/selector.png")))
                                hover Composite(
                                    (84,84),
                                    (0,0),("gui/"+node_item.TYPE+".png"),
                                    (0,0),(("gui/selector2.png")),
                                    (0,0),("blinky"))
                                # at zoomtrans(0.2)
                                # action NullAction()
                                action Function(open_node,(n_index_1,n_index_2),node_item)
                          
                        else:
                            # add ("gui/"+node_item.TYPE+".png") at zoomtrans(0.2)
                            imagebutton:
                                idle Composite(
                                    (84,84),
                                    (0,0),("gui/"+node_item.TYPE+".png"),
                                    (0,0),At(Frame(Solid("#000000"),10,10),alphatrans(0.8)))
                                # at zoomtrans(0.2)
                                action NullAction()
                        # vbox:
                        #     text (node_item.TYPE+" ")
                        #     # text ("("+str(n_index_1)+","+str(n_index_2)+")")  
                        #     at zoomtrans(0.5)
    frame:
        if not notransform:
            at pausetrans1
        style "pausestats"
        hbox:
            null width 4
            vbox:
                text "{b}[playerName]{/b}"
                null height 7
                fixed:
                    frame:
                        style_prefix "healthbar"
                        xsize bar_size(playerHP,playerHPMax, 420)
                    hbox:
                        null width 40
                        text "HP: [playerHP]/[playerHPMax]"
                    vbox:
                        null height 32
                        hbox:

                            frame:
                                style "deckframe"
                                text "{size=14}Deck: [mydeckname]{/size}"
                            
                            frame:
                                style "deckframe"
                                text "{size=14}ATK: [playerATK] DEF: [playerDEF] {/size}"
                            
                        frame:
                            xminimum 460
                            style "deckframe"
                            text "{size=16}Money: [Money] {image=gui/zenny.png} Zennys{/size}"

                null height 10
    
    # key "dismiss" action Return()

