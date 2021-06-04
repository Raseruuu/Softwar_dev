label pauseshow:
    $ILY_p = '0'
    $ILY_m = 'smile3'
    $ILY_e = '1'
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
        "This feature has not yet been implemented."
        jump pauseshow
    elif _return=="Mail":
        # call screen Items

        label Mailscreen:
            show screen pauselayout("INBOX",True,True)
            call screen Mailbox
            if _return=="Read":
                call ReadMessage(messageview["sender"],messageview["subject"],messageview["body"])
                jump Mailscreen
            elif _return!="Read":
                jump Mailscreen

            return
    elif _return=="Items":
        $ inventory= sorted( inventory,key=lambda x: x.NAME, reverse=False)
        label Itemscreen:
            $ noscreentransformsfornow=False
            call screen Items
            if _return=="Open":
                call OpenItem(messageview["sender"],messageview["subject"],messageview["body"])
                jump Itemscreen
            elif _return!="Open":
                jump Itemscreen
            return
    elif _return=="Battleware":
        $ deckcurrent= sorted( deckcurrent,key=lambda x: x.NAME, reverse=False)
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
            return
    elif _return=="Plugins":
        "This Feature Has Not Yet Been Implemented."
        jump pauseshow
        # label Plugins_screen:
        #     call screen Plugins
        #     if _return=="Plugins_Edit":
        #         label Plugins_edit_screen:
        #             call screen Plugins_Edit
        #             if _return!="Return":
        #                 jump Plugins_edit_screen
        #             return
    return
init python:
    hoverFXN=[]

    def tooltip_position():
        import pygame
        position = pygame.mouse.get_pos()
        print(position)
        tooltip_anchors = [0.0,0.0]
        if (position[0]>=0.5*config.screen_width):
            tooltip_anchors[0]=1.0
        if (position[1]>=0.5*config.screen_height):
            tooltip_anchors[1]=1.0
        return (position[0],position[1],tooltip_anchors[0],tooltip_anchors[1])

transform fxn_frame_pos(tooltip_position):
    xpos tooltip_position[0]
    ypos tooltip_position[1]
    xanchor tooltip_position[2]
    yanchor tooltip_position[3]
screen card_tooltip:

    frame:
        at fxn_frame_pos(tooltip_position())
        xsize 300
        ysize 200
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
default deck_unedited=[]



default card_inventory_unedited=[]
default inventory =[SoftDrink]


default card_library=deckdefault["content"]
default card_inventory=[DataDrill,DataDrill,Cursorclaw,DataBuster,Vshot,Vshot,Vslash,Vslash]



default inbox =  [
        {
            "sender":"ILY",
            "subject":"Locate SDS!",
            "body":"John, the SDS server is located northwest of here. Let's go!"
            },
        {
            "sender":"Lisa",
            "subject":"Lorem Ipsum",
            "body":"Lorem Ipsum Dolor  Sit Amet"
            }
            ]
init python:
            #       NAME            TYPE        DESC                                            FXN         MAG     COST
    SoftDrink=Item("SoftDrink", "Consumable",   "For thirsty Software! \nRecovers 100 HP.",        "Recover",  100,    20)
    Unlocker=Item("Unlocker",   "Key",        "Unlock locked Mystery Data. \nSingle use only.",   "Unlock",   100,    20)







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
    on show:
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
screen Items:
    use pauselayout("ITEMS")
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
            draggable True

            hbox:
                grid 2 50:
                    xspacing 20
                    for index, item in enumerate(inventory):
                        button:
                            xsize 300
                            ysize 150
                            frame:

                                xpadding 20
                                ypadding 20
                                idle_background Frame("gui/framefxn.png",10,10)
                                hover_background Frame("gui/framefxn2.png",10,10)
                                hbox:
                                    xalign 0.0 yalign 0.5
                                    image "images/Cards/items/"+item.NAME+".png"

                                    null width 10
                                    frame:
                                        background Null()
                                        xsize 170
                                        text item.NAME+"{size=12}\n\n"+item.DESC+"{/size}" yalign 0.0
                            action Return()


                                # text item.NAME
                    for itemfiller in range(0,100-len(inventory)):

                        button:
                            xsize 300
                            ysize 150
                            frame:
                                xpadding 20
                                ypadding 20
                                idle_background Frame("gui/framefxn.png",10,10)
                                hover_background Frame("gui/framefxn2.png",10,10)
                                hbox:
                                    xalign 0.0 yalign 0.5
                                    image  "images/Cards/items/empty.png"

                                    null width 180

                                    # text item.NAME yalign 0.5
                            action Return()

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
            null width 10
            vbox:
                # frame:
                    # textbutton "Edit" action Return()
                # null height 10
                frame:
                    textbutton "Back" action Jump("pauseshow")




                    # grid 8 8:
                    #     spacing 5
                    #     for index, item in enumerate(inventory):
                    #         imagebutton:
                    #             idle "images/Cards/"+item.NAME+".png"
                    #             hover Composite(
                    #                 (100,100),
                    #                 (0,0),"images/Cards/"+item.NAME+".png",
                    #                 (0,0),"blinky",
                    #                 (0,0),Text(index))
                    #             action Return()
                    #             at inventorysize
                    #
                    #     for itemfiller in range(0,64-len(inventory)):
                    #         image "images/Cards/items/empty.png":
                #     #             at inventorysize
                # null width 10
                # vbox:
                #     # frame:
                #         # textbutton "Edit" action Return()
                #     # null height 10
                #     frame:
                #         textbutton "Back" action Jump("pauseshow")
transform pausecardsize:
    zoom 0.8
screen Battleware:

    use pauselayout("BATTLEWARE",True,True)
    # add "cardflasher" xalign 0.34 yalign 0.58 at pausecardsize, pausetrans1
    use Card(currentcard,(420,217),1.0)

    frame:
        xpadding 20
        ypadding 20
        xalign 0.90 yalign 0.36
        at pausetrans2
        vbox:
            hbox:
                vbox:
                    text "{b}DECK NAME: [deckname]{/b}"
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
                            hovered SetVariable("currentcard",item)
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
                    action Call("pauseshow"), SetVariable("noscreentransformsfornow",False)

screen Battleware_Edit():
    use pauselayout("DECK EDIT",False,True)

    use Card(currentcard,(50,217),1.0)

    frame:
        xpadding 20
        ypadding 20
        xalign 0.40 yalign 0.36
        if not noscreentransformsfornow:
            at pausetrans2
        vbox:
            hbox:
                vbox:
                    text "{b}DECK NAME: [deckname]{/b}"
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
                            hovered SetVariable("currentcard",item)
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

transform marquee:
   #on show:
     xpos 1.0 xanchor 0.0
     linear 6.0 xpos 0.0 xanchor 1.0

     repeat
transform vmarquee:
   #on show:
     rotate -90
     ypos 1.0 yanchor 0.0
     linear 6.0 ypos 0.0 yanchor 1.0
     repeat
screen pauselayout(scrname,spritevisible=True,notransform=False):
    key "K_SPACE" action Return()
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
        add "ILY":
            xalign 0.08
            if not notransform:
                at pausetrans1
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
                                text "{size=18}Deck: [deckname]{/size}"
                        frame:
                            style "deckframe"
                            text "{size=14}Chapter [chapternum]{/size}"
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
screen pausemenu:
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
        action ShowMenu('preferences')

    imagebutton idle "gui/rpgmenu/battleware.png" hover "gui/rpgmenu/battleware_h.png":
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
        action ShowMenu("save")

    imagebutton idle "gui/rpgmenu/load.png" hover "gui/rpgmenu/load_h.png":
        hovered SetVariable('pause_button_offset7',-15) unhovered SetVariable('pause_button_offset7',0)
        xanchor 0.5 xpos 0.675 yanchor 0.5 ypos 0.78
        at pausetrans2,pausetranshover(pause_button_offset7)
        action ShowMenu("load")

    imagebutton idle "gui/rpgmenu/return.png" hover "gui/rpgmenu/return_h.png":
        hovered SetVariable('pause_button_offset8',-15) unhovered SetVariable('pause_button_offset8',0)
        xanchor 0.5 xpos 0.85 yanchor 0.5 ypos 0.78
        at pausetrans2,pausetranshover(pause_button_offset8)
        action Return()
transform pausetranshover(pauseoffset=0):
    # linear 0.1 yoffset pauseoffset
    linear 0.1 yoffset 0
transform pausetrans0:
    alpha 0.0 xoffset -20
    on show:
        ease 0.3 alpha 1.0 xoffset 0
    alpha 1.0
transform pausetrans1:
    alpha 0.0 xoffset -20
    on show:
        ease 0.3 alpha 1.0 xoffset 0
    alpha 1.0
transform pausetrans2:
    alpha 0.0 xoffset 20
    on show:
        ease 0.3 alpha 1.0 xoffset 0
    alpha 1.0
    on hide:
        ease 0.3 alpha 0.0 xoffset -20
transform pausetrans3:
    xanchor 1.0
    on show:
        linear 0.1 alpha 1.0 xanchor 0.0
transform pausetrans4:
    xanchor 0.0
    on show:
        linear 0.1 alpha 1.0 xanchor 1.0
transform pausedim:
    alpha 0.0
    on show:
        ease 0.3 alpha 0.77
    alpha 0.77
transform pausedim2:
    alpha 0.77
transform pauseshow:
    alpha 0.0
    on show:
        ease 0.3 alpha 1.0
    alpha 1.0
