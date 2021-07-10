
default plugincurrent =sorted( mydeck["plugins"],key=lambda x: x.NAME, reverse=False)
default plugin_library=deckdefault["content"]
default plugin_inventory=[DataDrill,DataDrill,Cursorclaw,DataBuster,Vshot,Vshot,Vslash,Vslash]

init python:
    notransform=False
    def RemoveFromPlugins(index):
        plugins_inventory.append(deckcurrent[index])
        return (deckcurrent.pop(index))
    def AddToPlugins(index):
        if (len(deckcurrent)<24):
            deckcurrent.append(card_inventory[index])
            return (card_inventory.pop(index))

    standardrates={
        "Blazebuster":100,
        "VFlame":100
        }
    # class Shop:
    #     def __init__(self,name,inventory,rate,location):
    #         self.name=name
    #         self.inventory=inventory
    #         self.rate=rate
    #         self.location=location
    #     class ShopItem:
    #         def __init__(self,name,object,type,price):
    #             self.name=name
    #             self.object=object
    #             self.type=type
    #             self.price=price
    # shop_Blazebuster=ShopItem("Blazebuster",Blazebuster,"card",200)
    # shop_Softdrink=ShopItem("Softdrink",Softdrink,"item",200)

screen Plugins:
    use pauselayout("PLUGINS")
    # add "cardflasher" xalign 0.34 yalign 0.58 at pausecardsize, pausetrans1
    use Card(currentcard,(420,205),1.0)
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
                textbutton "Edit" action Return("Battleware_Edit")
            null height 10
            frame:
                textbutton "Back" action Call("pauseshow")

screen Plugins_Edit:
    use pauselayout("DECK EDIT",False,True)
    use Card(currentcard,(50,205),1.0)
    frame:
        xpadding 20
        ypadding 20
        xalign 0.40 yalign 0.36
        # at pausetrans2
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
                            action Call("RemoveFromDeck",index)
                            hovered SetVariable("currentcard",item)
                            at inventorysize

                    for itemfiller in range(0,24-len(deckcurrent)):
                        image "images/Cards/Empty.png":
                            at inventorysize
                null width 10
    frame:
        left_margin 880
        right_margin 15
        top_margin 110
        bottom_margin 180
        # at pausetrans2
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
                            action Call("AddToDeck",index)
                            hovered SetVariable("currentcard",item)
                            at inventorysize

                    for itemfiller in range(0,4*25-len(card_inventory)):
                        image "images/Cards/Empty.png":
                            at inventorysize

    frame:
        # at pausetrans1
        style_prefix "stats"
        xalign 0.95 yalign 0.88
        # xsize 400
        hbox:
            frame:
                textbutton "Save" action Jump("Plugins_screen")
            null height 10
            frame:
                textbutton "Back" action Jump("Plugins_screen")
