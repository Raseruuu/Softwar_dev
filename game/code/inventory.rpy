screen Items(itemsmode="ITEMS"):
    python:
        if itemsmode=="ITEMS":
            inventory_counts= {z: ([y.NAME for y in inventory].count(z)) for z in  [z.NAME for z in inventory]}
            inventory_objects=[]
            for x in inventory:
                if (x.NAME not in [y.NAME for y in inventory_objects]):
                    inventory_objects.append(x)
        
    use pauselayout(itemsmode)
    frame:
        style "nvl_window"
        top_padding 32
        if not noscreentransformsfornow:
            at pausetrans2
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            hbox:

                grid 1 40:
                    xspacing 16
                    for item in inventory_objects:
                        button:
                            xsize 600
                            ymaximum 86
                            frame:
                                xpadding 12
                                ypadding 12
                                idle_background Frame("gui/framefxn.png",10,10)
                                hover_background Frame("gui/framefxn2.png",10,10)

                                hbox:
                                    xalign 0.0 yalign 0.5
                                    frame:
                                        xsize 120
                                        ysize 120
                                        if item.TYPE=="Material":
                                            background "images/Cards/items/Material.png" at zoom05
                                        else:
                                            background "images/Cards/items/"+item.NAME+".png" at zoom05
                                        if (inventory_counts[item.NAME])!=1:
                                            foreground At(Text("{size=38}{b}x"+str(inventory_counts[item.NAME])+"{/size}{/b}"),bottomright)

                                    null width 10
                                    frame:
                                        background Null()
                                        xsize 480
                                        ysize 50
                                        vbox:
                                            text "{size=16}{b}"+item.NAME+"{/size}{/b}{size=12}\n"+item.DESC+"{/size}" yalign 0.5
                                    transclude
                            if itemsmode=="ITEMS":
                                action Function(UseItem,item)
                            else:
                                action NullAction()


                                # text item.NAME
                    # for itemfiller in range(0,40-len(inventory)):
                    for itemfiller in range(0,40-len(inventory_objects)):

                        button:
                            xsize 600
                            ymaximum 86
                            frame:
                                xpadding 12
                                ypadding 12
                                idle_background Frame("gui/framefxn.png",10,10)
                                hover_background Frame("gui/framefxn2.png",10,10)
                                hbox:
                                    xalign 0.0 yalign 0.5
                                    xsize 480+70
                                    ysize 50
                                    image  "images/Cards/items/empty.png" at zoom05

                                    null width 230

                                    # text item.NAME yalign 0.5
                            action NullAction()

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
                    textbutton "Back" action Return()
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
