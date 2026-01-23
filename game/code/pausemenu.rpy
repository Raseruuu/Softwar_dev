label pauseshow:
    $ pausemenu =True
    $ILY_p = '0'
    $ILY_m = 'smile3'
    $ILY_e = 'normal'
    python:
        pause_button_offset1 = 0
        pause_button_offset2 = 0
        pause_button_offset3 = 0
        pause_button_offset4 = 0
        pause_button_offset5 = 0
        pause_button_offset6 = 0
    $stay_on_pause=False
    hide screen pauselayout
    call screen pausemenu
    if _return=="FAI":
        
        
        # jump pauseshow
        label FAI_menu:
        call screen FAI_menu
        if _return=="Customize":
            label FAICustomizescreen:
                $ noscreentransformsfornow=False
                call screen Items_dress
                # if _return=="Battleware_Edit":
                   
                #     label Battleware_edit_screen:
                #         call screen Battleware_Edit
                #         if _return=="SaveDeck":
                #             call SaveDeck
                #         elif _return=="UnsaveDeck":
                #             call UnsaveDeck

                #         else:
                #             jump Battleware_edit_screen
                        # return
        elif _return=="ActiveFAI":
            "Switch FAI: Select a FAI other than ILY"
            
    

    elif _return=="Mail":
        # call screen Items

        label Mailscreen:
            show screen pauselayout("INBOX",True,True)
            call screen Mailbox
            if _return=="Read":
                call ReadMessage(messageview["sender"],messageview["subject"],messageview["body"]) from _call_ReadMessage
                jump Mailscreen
            elif _return!="Read":
                jump Mailscreen

            # return
    elif _return=="Items":
        $ inventory= sorted( inventory,key=lambda x: x.NAME, reverse=False)
        # label Items_manage:
            # call screen Itemsmanage
            # if _return=="Items":
        label Itemscreen:
            $ noscreentransformsfornow=False
            call screen Items

            # if _return=="Open":
            #     call OpenItem(messageview["sender"],messageview["subject"],messageview["body"]) from _call_OpenItem
            #     jump Itemscreen
            # elif _return!="Open":
            #     jump Itemscreen
            # return

            # return
    
    elif _return=="Battleware":
        $ deckcurrent= sorted( deckcurrent,key=lambda x: x.NAME, reverse=False)
        # label ware_menu:
        # call screen ware_menu
        # if _return=="Equipped":
        label Battlewarescreen:
            $ noscreentransformsfornow=False
            call screen Battleware
            if _return=="Battleware_Edit":
                python:
                    deck_unedited=copy.deepcopy(sorted( deckcurrent,key=lambda x: x.NAME, reverse=False))
                    card_inventory_unedited=copy.deepcopy(sorted( card_inventory,key=lambda x: x.NAME, reverse=False))
                label Battleware_edit_screen:
                    call screen Battleware_Edit
                    if _return=="SaveDeck":
                        call SaveDeck
                    elif _return=="UnsaveDeck":
                        call UnsaveDeck

                    else:
                        jump Battleware_edit_screen
                    return
        # elif _return=="Decks":
        #     label Deckmenu:
        #         $ noscreentransformsfornow=False
        #         "Sorry, Click \"Equipped\" for now, to check and edit your deck."
        # elif _return=="Create":
        #     "Battleware Creation is Not Yet Implemented"
        #     # label MaterialCombination:
        #     #     call screen CombineMenu
        # elif _return=="Collection":
        #     label CardCollection:
        #         "Collection cannot be accessed atm"

        # return
    elif _return=="Plugins":
        "This Feature Has Not Yet Been Implemented."
        # jump pauseshow
        # label Plugins_screen:
        #     call screen Plugins
        #     if _return=="Plugins_Edit":
        #         label Plugins_edit_screen:
        #             call screen Plugins_Edit
        #             if _return!="Return":
        #                 jump Plugins_edit_screen
        #             return
    if _return=="Save":
        hide screen pausemenu
        call screen save()
        # ShowMenu()
    elif _return=="Load":
        hide screen pausemenu
        call screen load()
    elif _return=="Pref":
        hide screen pausemenu
        call screen preferences()
    if _return=="Return":
        $ pausemenu =False
        
        return
    elif _return!="Return":
        jump pauseshow
    $ pausemenu =False

    return
init python:
    hoverFXN=[]

    def tool_position():
        import pygame
        position = pygame.mouse.get_pos()
        print(position)
        tooltip_anchors = [0.0,0.0]
        if (position[0]>=0.5*config.screen_width):
            tooltip_anchors[0]=1.0
        if (position[1]>=0.5*config.screen_height):
            tooltip_anchors[1]=1.0
        return (position[0],position[1]-40,tooltip_anchors[0],tooltip_anchors[1])

transform fxn_frame_pos(tooltip_position):
    xpos tooltip_position[0]
    ypos tooltip_position[1]
    xanchor tooltip_position[2]
    yanchor tooltip_position[3]
screen card_tooltip_battle:

    frame:
        at fxn_frame_pos(tool_position())
        # xpos 0.44 xanchor 0.0 ypos 0.94 yanchor 1.0
        xsize 420
        ysize 180
        add FunctionListDescript(hoverFXN) 

screen card_tooltip:

    frame:
        # at fxn_frame_pos(tool_position())
        xpos 0.42 xanchor 0.0 ypos 0.95 yanchor 1.0
        xsize 450
        ysize 160
        add FunctionListDescript(hoverFXN) 
label ObtainItem(item):

    if len(inventory)== 100:
        python:
            inventory.append(item)
    else:
        menu:
            "Your inventory is full. Would you like to discard am item to receive [item.name]?"
            "Yes":
                call screen inventorydiscard
            "No":
                "You will be discarding [item.name], are you sure?"

default deckname=mydeck["name"]
default deckcurrent =sorted( mydeck["content"],key=lambda x: x.NAME, reverse=False)
default deckplugin =mydeck["plugins"]
default deck_unedited=[]



default card_inventory_unedited=[]
default inventory =[SoftDrink]
default inventory_key = [] #(KEY ITEMS)

default card_library=deckdefault["content"]
default card_inventory=[DataDrill,WindBlast,Shieldbit,Shieldbit,DataBuster,Tackle,Tackle]



default inbox =  [
        {
            "sender":"ILY",
            "subject":"Locate SDS!",
            "body":"John, the SDS server is located northwest of here. Let's go!"
            },
        {
            "sender":"Lisa lsfrfld@vmail.com",
            "subject":"Love Letter For You!",
            "body":" Happy Valentines Day! Attached: A very special message <3 "
            }
            ]




init python:
    messageview= {"sender":"","subject":"","body":""}
label ReceiveMessage(sender,subject,body):
    $ renpy.notify("New Message from "+sender+"!")
    $ inbox.append({"sender":sender,"subject":subject,"body":body})
    return

label ReadMessage(sender,subject,message):
    # show screen pauselayout("EMAIL",True,True)
    nvl clear
    emailnvl"{b}[subject]{/b}\n\n{i}From:{/i} [sender]\n\n[message]"

    return
screen Mailbox:
    # use pauselayout("INBOX",True,True)
    frame:
        style "nvl_window"
        top_padding 32
        # left_margin 540
        # right_margin 16
        # top_margin 112
        # bottom_margin 202
        if not noscreentransformsfornow:
            at pausetrans2

        viewport:
            scrollbars "vertical"
            mousewheel True
            arrowkeys True
            draggable True

            hbox:
                vbox:
                    for message in inbox:
                        imagebutton:
                            idle Composite(
                                (743,76),
                                (0,0),"gui/messagebox.png",
                                (100,10),Text(""+message["sender"]+"\n  "+message["subject"]))
                            hover Composite(
                                (743,76),
                                (0,0),"gui/messagehover.png",
                                (100,10),Text(""+message["sender"]+"\n  "+message["subject"]))
                            action SetVariable("messageview",message), Return("Read"),  SetVariable("noscreentransformsfornow",True)
                        null height 20
                null width 10
    frame:
        if not noscreentransformsfornow:
            at pausetrans1
        style_prefix "stats"
        xalign 0.95 yalign 0.88
        ysize 100
        hbox:
            # frame:
            #     textbutton "Save" action SetVariable("noscreentransformsfornow",True), Return("SaveDeck")

            null height 10
            frame:
                textbutton "Back":
                    action SetVariable("noscreentransformsfornow",True), Jump("pauseshow")


init python:
    import copy
    noscreentransformsfornow=False
    notransform=False
    def SaveDeck(deckcurrent,deck_unedited):
        if (len(deckcurrent)==24):
            # deckcurrent = deck_unedited
            deckcurrent= sorted( deckcurrent,key=lambda x: x.NAME, reverse=False)
            renpy.notify("Deck Saved.")
            renpy.jump("Battlewarescreen")
        else:
            renpy.notify("Deck must contain 24 cards.")

    def RemoveFromDeck(index):
        card_inventory.append(deckcurrent[index])

        return deckcurrent.pop(index)
    def ReadMessage(sender,body):
        renpy.say(sender,body)
        return

    def AddToDeck(index):
        if (len(deckcurrent)<24):
            name_of_card_to_add=card_inventory[index].NAME
            samecards_in_deck = sum(cards.NAME == name_of_card_to_add for cards in deckcurrent)
            if samecards_in_deck<5:
                deckcurrent.append(card_inventory[index])
                return (card_inventory.pop(index))
            else:
                renpy.notify("You cannot add more than 5 cards of the same name.")
        else:
            renpy.notify("You cannot add more than 24 cards.")
label SaveDeck:
    python:
        if (len(deckcurrent)==24):
            deckcurrent= sorted( deckcurrent,key=lambda x: x.NAME, reverse=False)
            renpy.notify("Deck sorted and saved.")
            renpy.jump("Battlewarescreen")
        else:
            renpy.notify("Deck must contain 24 cards.")
            renpy.jump("Battleware_edit_screen")
    return
label UnsaveDeck:
    python:
        if deckcurrent!=deck_unedited:
            renpy.notify("Deck Changes Not Saved.")
        deckcurrent= sorted(deck_unedited,key=lambda x: x.NAME, reverse=False)
        card_inventory=sorted(card_inventory_unedited,key=lambda x: x.NAME, reverse=False)
        renpy.jump("Battlewarescreen")

    return
transform inventorysize:
    zoom 0.4
transform selectedItem:
    ease 0.1 zoom 0.1
transform alphablinky:
    alpha 0.9
    linear 0.1 alpha 0.0
    linear 0.1 alpha 0.9
    linear 0.1 alpha 0.0
    repeat
image blinky:
    Solid("#fff")
    alpha 0.2
    linear 0.3 alpha 0.9
    linear 0.3 alpha 0.0
    repeat
transform zoom05():
    zoom 0.5

transform pausecardsize:
    zoom 0.8

# elif itemsmode=="COMBINE":
label getCardLibrary:
    python:
    # comb_list=combinationlibrary.values()
        comb_obj_list=[comb.object for comb in combinationlibrary.values()]
        inventory_counts= {z: ([y.NAME for y in [comb.object for comb in combinationlibrary.values()]].count(z)) for z in  [z.NAME for z in [comb.object for comb in combinationlibrary.values()]]}
        inventory_objects=[]
        for x in [comb.object for comb in combinationlibrary.values()]:
            if (x.NAME not in [y.NAME for y in inventory_objects]):
                inventory_objects.append(x)
screen Battleware:
    $ mydeckname = mydeck["name"]
    use pauselayout("BATTLEWARE",True,True)
    # add "cardflasher" xalign 0.34 yalign 0.58 at pausecardsize, pausetrans1
    # use Card(currentcard,(420,217),1.0)
    add CardDisplay(currentcard):
        xpos 420 ypos 192 xanchor 0.0 yanchor 0.0

    frame:
        xpadding 20
        ypadding 20
        xalign 0.90 yalign 0.36
        at pausetrans2
        vbox:
            hbox:
                vbox:
                    text "{b}DECK NAME: [mydeckname]{/b}"
                    # text "{size=16}TYPE : Virus{/size}"
                # null width 80

            null height 10
            hbox:

                grid 6 4:
                    for item in deckcurrent:
                        imagebutton:
                            idle "images/Cards/"+item.NAME+".png"
                            hover Composite(
                                (205,205),
                                (0,0),"images/Cards/"+item.NAME+".png",
                                (0,0),"blinky")
                            action NullAction()
                            hovered SetVariable("currentcard",item),SetVariable("hoverFXN",item.FXN)
                            at inventorysize

                    for itemfiller in range(0,24-len(deckcurrent)):
                        image "images/Cards/Empty.png":
                            at inventorysize
                null width 10
    frame:
        at pausetrans1
        style_prefix "stats"
        xalign 0.95 yalign 0.88
        # xsize 400
        hbox:
            frame:
                imagebutton idle Text("{size=35}Edit{/size}") hover Text("{size=35}{color=f00}Edit{/size}"):
                    action Return("Battleware_Edit"), SetVariable("noscreentransformsfornow",False)
            null height 10
            frame:
                imagebutton idle Text("{size=35}Back{/size}") hover Text("{size=35}{color=f00}Back{/size}"):
                    action Return(), SetVariable("noscreentransformsfornow",False)
    if hoverFXN!=[]:
        use card_tooltip
screen Battleware_Edit():
    $ mydeckname = mydeck["name"]
    use pauselayout("DECK EDIT",False,True)

    # use Card(currentcard,(50,217),1.0)
    add CardDisplay(currentcard):
        xpos 50 ypos 192 xanchor 0.0 yanchor 0.0
    frame:
        xpadding 20
        ypadding 20
        xalign 0.40 yalign 0.36
        if not noscreentransformsfornow:
            at pausetrans2
        vbox:
            hbox:
                vbox:
                    text "{b}DECK NAME: [mydeckname]{/b}"
                    # text "{size=16}TYPE : Virus{/size}"
                # null width 80

            null height 10
            hbox:

                grid 6 4:
                    for index,item in enumerate(deckcurrent):
                        imagebutton:
                            idle "images/Cards/"+item.NAME+".png"
                            hover Composite(
                                (205,205),
                                (0,0),"images/Cards/"+item.NAME+".png",
                                (0,0),"blinky")
                            action Function(RemoveFromDeck,index), SetVariable("noscreentransformsfornow",True)
                            hovered SetVariable("currentcard",item),SetVariable("hoverFXN",item.FXN)
                            at inventorysize

                    for itemfiller in range(0,24-len(deckcurrent)):
                        image "images/Cards/Empty.png":
                            at inventorysize
                null width 10
    frame:
        left_margin 880
        right_margin 16
        top_margin 112
        bottom_margin 202
        if not noscreentransformsfornow:
            at pausetrans2
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True


            hbox:

                grid 4 25:
                    for index,item in enumerate(card_inventory):
                        imagebutton:
                            idle "images/Cards/"+item.NAME+".png"
                            hover Composite(
                                (205,205),
                                (0,0),"images/Cards/"+item.NAME+".png",
                                (0,0),"blinky")
                            action Function(AddToDeck,index), SetVariable("noscreentransformsfornow",True)
                            hovered SetVariable("currentcard",item),SetVariable("hoverFXN",item.FXN)
                            at inventorysize

                    for itemfiller in range(0,4*25-len(card_inventory)):
                        image "images/Cards/Empty.png":
                            at inventorysize

    frame:
        if not noscreentransformsfornow:
            at pausetrans1
        style_prefix "stats"
        xalign 0.95 yalign 0.88
        hbox:
            frame:
                # textbutton "Save" action SetVariable("noscreentransformsfornow",True), Return("SaveDeck")
                imagebutton idle Text("{size=35}Save{/size}") hover Text("{size=35}{color=f00}Save{/size}") action SetVariable("noscreentransformsfornow",True), Return("SaveDeck")

            null height 10
            frame:
                imagebutton idle Text("{size=35}Back{/size}") hover Text("{size=35}{color=f00}Back{/size}"):
                    action SetVariable("noscreentransformsfornow",True), Return("UnsaveDeck")
    if hoverFXN!=[]:
        use card_tooltip

transform marquee(image_path):
    #on show:
    contains:
        image_path
        # rotate 90 xalign 0.8
        xpos 1.0 xanchor 0.0
        linear 3.0 xpos 0.5 xanchor 0.5
        repeat
    contains:
        image_path
        # rotate 90 xalign 0.8
        xpos 0.5 xanchor 0.5
        linear 3.0 xpos 0.0 xanchor 1.0
        repeat
transform marquee2:
    #on show:
        pause 0.7
        xpos 1.0 xanchor 0.0
        linear 6.0 xpos 0.0 xanchor 1.0

        repeat
transform vmarquee(image_path):
    #on show:
    contains:
        image_path
        rotate 90 xalign 0.8
        ypos 1.0 yanchor 0.0
        linear 3.0 ypos 0.5 yanchor 0.5
        repeat
    contains:
        image_path
        rotate 90 xalign 0.8
        ypos 0.5 yanchor 0.5
        linear 3.0 ypos 0.0 yanchor 1.0
        repeat
transform zoomtrans(zoomvalue):
    zoom zoomvalue
screen pauselayout(scrname,spritevisible=True,notransform=False):
    $ mydeckname = mydeck["name"]
    # key 's'       action Return()
    # key 'S'       action Return()
    if notransform:
        image "black" at pausedim2
        text "{size=100}{b}"+scrname+"{/b}{/size}" ypos 0.03 xalign 0.6
        image "gui/rpgmenu/frame1.png" xalign 0.0 yalign 0.0
        image "gui/rpgmenu/frame2.png" xalign 1.0 yalign 1.0

    else:
        image "black" at pausedim
        text "{size=100}{b}"+scrname+"{/b}{/size}"  ypos 0.03 xalign 0.6
        image "gui/rpgmenu/frame1.png" at pausetrans3 xalign 0.0 yalign 0.0
        image "gui/rpgmenu/frame2.png" at pausetrans4 xalign 1.0 yalign 1.0


    if spritevisible:
        # image At("[playerName]",zoomtrans(0.5 if scrname=="CUSTOMIZE" else 1.0 )) :
        #     xpos 0.25 xanchor 0.5
        #     ypos (0.0 if scrname=="CUSTOMIZE" else 0.4 ) 
        #     yanchor 0.3
        #     if not notransform:
        #         at pausetrans1

        button:
            xsize 400
            background ("[playerName]")
            yanchor 0.7 ypos (0.54 if scrname=="CUSTOMIZE" else 1.0 )  xpos 0.20 xanchor 0.5 
            at pausetrans1, zoomtrans(0.5 if scrname=="CUSTOMIZE" else 1.0 )
            action Return("R_player_talks")

    if scrname!="CUSTOMIZE":
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
                                    style "deckframe"
                                    text "{size=14}Chapter [chapternum]{/size}"
                            frame:
                                xminimum 460
                                style "deckframe"
                                text "{size=16}Money: [Money] {image=gui/zenny.png} Zennys{/size}"

                    null height 10
style deckframe:
    background Frame("gui/framefxn.png", 32, 32)
    xpadding 8
    ypadding 8
style pausestats:
    xfill True
    yfill True
    background Frame("gui/frame3.png",72, 32, tile=gui.frame_tile)

    xpadding 20
    ypadding 20
    top_padding 2
    left_margin 16
    right_margin 752
    top_margin 524
    bottom_margin 48
style pausestats_r:
    xfill True
    yfill True
    background Frame("gui/frame3.png",72, 32, tile=gui.frame_tile)

    xpadding 20
    ypadding 20
    top_padding 2
    left_margin 16
    right_margin 752
    top_margin 324
    bottom_margin 248
init python:
    pause_button_offset0 = 0
    pause_button_offset1 = 0
    pause_button_offset2 = 0
    pause_button_offset3 = 0
    pause_button_offset4 = 0
    pause_button_offset5 = 0
    pause_button_offset6 = 0
    pause_button_offset7 = 0
    pause_button_offset8 = 0
    def set_focus(screen_name,id):
        renpy.set_focus(screen_name,id)
default pausemenu =False
screen pausemenu:
    
    tag menu
    timer 0.01:
        action Function(set_focus,"pausemenu", "pausebattleware")
    key "K_SPACE" action Return("Return")
    use pauselayout("SOFTWAR")

    imagebutton idle "gui/rpgmenu/mail.png" hover "gui/rpgmenu/mail_h.png":
        hovered SetVariable('pause_button_offset0',-15) unhovered SetVariable('pause_button_offset0',0)
        xanchor 0.5 xpos 0.50 yanchor 0.5 ypos 0.34
        at pausetrans2,pausetranshover(pause_button_offset0)
        action Return("Mail")
    imagebutton idle "gui/rpgmenu/fai.png" hover "gui/rpgmenu/fai_h.png":
        hovered SetVariable('pause_button_offset1',-15) unhovered SetVariable('pause_button_offset1',0)
        xanchor 0.5 xpos 0.675 yanchor 0.5 ypos 0.34
        at pausetrans2,pausetranshover(pause_button_offset1)
        action Return("FAI")
    imagebutton idle "gui/rpgmenu/items.png" hover "gui/rpgmenu/items_h.png":
        hovered SetVariable('pause_button_offset2',-15) unhovered SetVariable('pause_button_offset2',0)
        xanchor 0.5 xpos 0.85 yanchor 0.5 ypos 0.34
        at pausetrans2,pausetranshover(pause_button_offset2)
        action Return("Items")

    imagebutton idle "gui/rpgmenu/options.png" hover "gui/rpgmenu/options_h.png":
        hovered SetVariable('pause_button_offset3',-15) unhovered SetVariable('pause_button_offset3',0)
        xanchor 0.5 xpos 0.50 yanchor 0.5 ypos 0.56
        at pausetrans2,pausetranshover(pause_button_offset3)
        action ShowMenu('preferences'), Return()
        # action Return("Pref")
    imagebutton idle "gui/rpgmenu/battleware.png" hover "gui/rpgmenu/battleware_h.png":
        # default_focus True
        id "pausebattleware"
        hovered SetVariable('pause_button_offset4',-15) unhovered SetVariable('pause_button_offset4',0)
        xanchor 0.5 xpos 0.675 yanchor 0.5 ypos 0.56
        at pausetrans2,pausetranshover(pause_button_offset4)
        action Return("Battleware")


    imagebutton idle "gui/rpgmenu/plugins.png" hover "gui/rpgmenu/plugins_h.png":
        hovered SetVariable('pause_button_offset5',-15) unhovered SetVariable('pause_button_offset5',0)
        xanchor 0.5 xpos 0.85 yanchor 0.5 ypos 0.56
        at pausetrans2,pausetranshover(pause_button_offset5)
        action Return("Plugins")

    imagebutton idle "gui/rpgmenu/saveload.png" hover "gui/rpgmenu/saveload_h.png":
        hovered SetVariable('pause_button_offset6',-15) unhovered SetVariable('pause_button_offset6',0)
        xanchor 0.5 xpos 0.5 yanchor 0.5 ypos 0.78
        at pausetrans2,pausetranshover(pause_button_offset6)
        action ShowMenu("save"), Return()
        # action Return("Save")
    imagebutton idle "gui/rpgmenu/load.png" hover "gui/rpgmenu/load_h.png":
        hovered SetVariable('pause_button_offset7',-15) unhovered SetVariable('pause_button_offset7',0)
        xanchor 0.5 xpos 0.675 yanchor 0.5 ypos 0.78
        at pausetrans2,pausetranshover(pause_button_offset7)
        action ShowMenu("load"), Return()
        # action Return("Load")
    imagebutton idle "gui/rpgmenu/return.png" hover "gui/rpgmenu/return_h.png":
        hovered SetVariable('pause_button_offset8',-15) unhovered SetVariable('pause_button_offset8',0)
        xanchor 0.5 xpos 0.85 yanchor 0.5 ypos 0.78
        at pausetrans2,pausetranshover(pause_button_offset8)
        action Return("Return")

transform pausetranshover(pauseoffset=0):
    # linear 0.1 yoffset pauseoffset
    linear 0.1 yoffset 0
transform pausetrans0:
    alpha 0.0
    xoffset -20
    ease 0.3 alpha 1.0 xoffset 0
    alpha 1.0
# transform pausetrans1:
#     alpha 0.0
#     xoffset -20
#     on show:
#         ease 0.3 alpha 1.0 xoffset 0
#     alpha 1.0
transform pausetrans1:
    alpha 0.0 xoffset -20
    ease 0.3 alpha 1.0 xoffset 0
    alpha 1.0
transform pausetrans2:
    alpha 0.0 xoffset 20
    ease 0.3 alpha 1.0 xoffset 0
    alpha 1.0
    on hide:
        ease 0.3 alpha 0.0 xoffset -20
transform pausetrans3:
    xanchor 1.0
    ease 0.1 alpha 1.0 xanchor 0.0
transform pausetrans4:
    xanchor 0.0
    ease 0.1 alpha 1.0 xanchor 1.0
transform pausedim:
    alpha 0.0
    ease 0.3 alpha 0.77
    alpha 0.77
transform pausedim2:
    alpha 0.77
transform pauseshow:
    alpha 0.0
    ease 0.3 alpha 1.0
    alpha 1.0
