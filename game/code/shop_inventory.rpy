transform pricepos:
    xanchor 1.0 xpos 0.94 yalign 0.96
style pricetext:
    size 18
    padding (2,2,2,2)
    background Frame("gui/framefxn.png", 32, 32)
transform bottomright:
    xalign 1.0 yalign 1.0

init python:

    def  ItemPriceDisplay(item):
        price = item.price
        return At(Text(str(price)+" {image=gui/zenny.png}",style="pricetext"),pricepos)
    class shop_item:
        def __init__(self,name,object,type,price):
            self.name = name
            self.object = object
            self.type = type
            self.price = price
    pricelist = {
        "SoftDrink":100,
        "SmallEnergy":120,
        "MediumEnergy":240,
        "LargeEnergy":480,
        # "Unlocker":1000,
        "Antibody":350,

        "V-Flame":600,
        "Laserbeam":3000,
        "LambdaSaber":1000,
        "BlockSaber":1000,
        "DataBuster":2000

    }

    item_list = [SoftDrink,SmallEnergy,MediumEnergy] #Unlocker
    battleware_list =[VirusFlame,LambdaSaber,BlockSaber,DataBuster,Laserbeam]


    shop_item_list = {item.NAME:shop_item(item.NAME,item,"Item",pricelist[item.NAME]) for item in item_list}
    shop_battleware_list = {item.NAME:shop_item(item.NAME,item,"Battleware",pricelist[item.NAME]) for item in battleware_list}

    shop_inventory=[item for item in shop_item_list.values()]
    
    for bwares in [item for item in shop_battleware_list.values()]:
        shop_inventory.append(bwares)
    def moneyvalue():
        global Money
        return Money
default Money= 1000
default item_selected=None
# screen shop_image:
#     zorder 200
#     add "Stoned":
#         xpos 0.06 xanchor 0.5
#         if not notransform:
#             at pausetrans1
#     frame:
#         if not notransform:
#             at pausetrans1
#         style "pausestats"
#         hbox:
#             null width 4
#             vbox:
#                 text "{b}STELLA SHOP{/b}"
#                 null height 7
#                 fixed:
#                     vbox:
#                         null height 12
#                         frame:
#                             xminimum 460
#                             style "deckframe"
#                             text "{size=24}\"Yo.\"{/size}"
#                         frame:
#                             xminimum 460
#                             style "deckframe"
#                             text "{size=24}Current Money: "+moneyvalue()+" Zennys{/size}"
#                 null height 10
transform shopcardsize:
    zoom 0.5
default shop_view = False
default shop_page = 0
default lastshop_item =0
style itembuttontext:
    insensitive_color "#808182"

    # insensitive_color "#000"
# init python:
#     def page_change(dir):
#         # pagelimit = 
#         if dir=="Prev" and shop_page!=0:
#             return SetVariable("shop_page",shop_page-1)
#         elif dir=="Next" and shop_page <= int(len(shop_inventory)/4):
#             return SetVariable("shop_page",shop_page+1)
#         else:
#             pass
screen item_shop:

    on "show":

        action Play("music","bgm/Shop_bgm_maoudamashii_acoustic41.mp3")
    on "hide":
        action Play("music","bgm/ost/Grid_noyemi_K.mp3")

    # zorder 201
    key "x" action SetVariable("shop_active",False), Return()
    if notransform:
        image "black" at pausedim2
        # text "{size=100}{b}"+scrname+"{/b}{/size}" ypos 0.03 xalign 0.6
        image "gui/rpgmenu/frame1.png" xalign 0.0 yalign 0.0
        image "gui/rpgmenu/frame2.png" xalign 1.0 yalign 1.0

    else:
        image "black" at pausedim
        # text "{size=100}{b}"+scrname+"{/b}{/size}"  ypos 0.03 xalign 0.6
        image "gui/rpgmenu/frame1.png" at pausetrans3 xalign 0.0 yalign 0.0
        image "gui/rpgmenu/frame2.png" at pausetrans4 xalign 1.0 yalign 1.0

    add "Stonedshop":
        xpos 0.25 xanchor 0.5 yanchor 0.60 ypos 1.0 
        # xpos 0.06 xanchor 0.5
        if not notransform:
            at pausetrans1
    frame:
        if not notransform:
            at pausetrans1
        style "pausestats"
        hbox:
            null width 4
            vbox:
                text "{b}STELLA SHOP{/b}"
                
                null height 7
                fixed:
                    vbox:
                        null height 12
                        frame:
                            xminimum 460
                            style "deckframe"
                            text "{size=24}\"Yo.\"{/size}"
                        frame:
                            xminimum 460
                            style "deckframe"
                            text "{size=24}Money: [Money] Zennys{/size}"
                null height 10
   
    frame:
        style "nvl_window"

        text "{b}FOR SALE{/b}"
        top_padding 2
        ysize 720
        if not noscreentransformsfornow:
            at pausetrans2
        vbox:
            null height 32
            hbox:
                xalign 0.5
                yanchor 0.0 ypos 0.0
                button:
                    top_padding 0
                    top_margin 0
                    
                    frame:
                        style_prefix "stats"
                        text "Prev. Page"
                        xsize 200
                        idle_background Frame("gui/framebtn.png",10,10)
                        hover_background Frame("gui/framefxn2.png",10,10)
                        # hbox:
                        #     style "itembuttontext"
                        #     yalign 0.5 xalign 0.5
                        #     text "Buy" yalign 0.5
                        #     null width 10
                        #     add ItemPriceDisplay(item)
                    action If((shop_page>0) ,SetVariable("shop_page",shop_page-1))
                frame:
                    xsize 200
                    ysize 56
                    yalign 0.5
                    top_margin 4
                    text ("Page "+str(shop_page+1))
                button:
                    top_padding 0
                    top_margin 0
                    frame:
                        style_prefix "stats"
                        text "Next Page"
                        xsize 200
                        idle_background Frame("gui/framebtn.png",10,10)
                        hover_background Frame("gui/framefxn2.png",10,10)
                        # hbox:
                        #     style "itembuttontext"
                        #     yalign 0.5 xalign 0.5
                        #     text "Buy" yalign 0.5
                        #     null width 10
                        #     add ItemPriceDisplay(item)
                    action If((shop_page+1 < int(len(shop_inventory)/4+(1 if (len(shop_inventory)%4>0) else 0))) ,SetVariable("shop_page",shop_page+1))
            null height 7
            
            # viewport:
            #     # scrollbars "vertical"
            #     # mousewheel True
            #     # arrowkeys True
            #     pagekeys True
                # draggable True
            hbox:
                    grid 2 2:
                        xspacing 20
                        # page*page_size:page*page_size+page_size
                        for shop_index, item in enumerate(shop_inventory[shop_page*4:shop_page*4+4]):
                        # for shop_index, item in enumerate(shop_inventory[:4]):
                            frame:
                                xsize 320
                                ysize 150
                                xpadding 8
                                ypadding 8
                                background Frame("gui/framefxn.png",10,10)
                                vbox:
                                    
                                    if item.type=="Item":
                                        hbox:
                                            xalign 0.0 yalign 0.5
                                            image "images/Cards/items/"+item.object.NAME+".png"

                                            null width 10
                                            frame:
                                                background Null()
                                                top_padding 0
                                                xsize 170
                                                vbox:
                                                    yalign 0.0
                                                    text "{size=22}"+item.object.NAME+"{/size}{size=12}\n\n"+item.object.DESC+"{/size}" yalign 0.0
                                                    button:
                                                        id "shop_button"+str(shop_index)

                                                        xalign 1.0
                                                        yalign 1.0
                                                        frame:
                                                            xsize 150
                                                            idle_background Frame("gui/framebtn.png",10,10)
                                                            hover_background Frame("gui/framefxn2.png",10,10)
                                                            hbox:
                                                                style "itembuttontext"
                                                                yalign 0.5 xalign 0.5
                                                                text "{size=16} Buy {/size}" yalign 0.5
                                                                null width 10
                                                                add ItemPriceDisplay(item)
                                                        action SetVariable("lastshop_item",shop_index),Call("buyitem",item)
                                    elif item.type=="Battleware":
                                        hbox:
                                            xalign 0.0 yalign 0.5
                                            image "images/Cards/"+item.object.NAME+".png" at shopcardsize

                                            null width 10
                                            frame:
                                                background Null()
                                                top_padding 0
                                                xsize 170
                                                vbox:
                                                    text "{size=22}"+item.object.NAME+"{/size}" yalign 0.0
                                                    text "{size=12}MAG = "+str(item.object.MAG)+"\nBITS = "+str(item.object.COST)+"{/size}" yalign 0.0

                                                    add FunctionList(item.object.FXN)


                                                    button:
                                                        id "shop_button"+str(shop_index)

                                                        xalign 1.0
                                                        frame:
                                                            xsize 150
                                                            idle_background Frame("gui/framebtn.png",10,10)
                                                            hover_background Frame("gui/framefxn2.png",10,10)
                                                            # insensitive_background Frame("gui/framefxn2.png",10,10)

                                                            # style "buttoninsens"
                                                            hbox:
                                                                yalign 0.5 xalign 0.5
                                                                text "{size=16} Buy {/size}" yalign 0.5
                                                                null width 10
                                                                add ItemPriceDisplay(item)
                                                        # sensitive (item.price<=money)
                                                        action SetVariable("lastshop_item",shop_index),Call("buyitem",item)

                                    # text item.NAME
                        # for itemfiller in range(0,40-len(shop_inventory)):

                        #     # frame:
                        #     #     xsize 320
                        #     #     ysize 175
                        #         frame:
                        #             xsize 320
                        #             ysize 175
                        #             xpadding 20
                        #             ypadding 20
                        #             background Frame("gui/framefxn.png",10,10)
                        #             # hover_background Frame("gui/framefxn2.png",10,10)
                        #             hbox:
                        #                 xalign 0.0 yalign 0.5
                        #                 image  "images/Cards/items/empty.png"

                        #                 null width 180

                        #                 # text item.NAME yalign 0.5
                        #         # action NullAction()

                    null width 10
    frame:
        if not noscreentransformsfornow:
            at pausetrans1
        style_prefix "stats"
        xalign 0.95 yalign 0.88
        ysize 100
        hbox:
            null width 10
            vbox:

                frame:
                    textbutton "Back" action SetVariable("shop_active",False), Return()
    if shop_view:
        use ItemModal
    
screen ItemModal:
    zorder 201

    frame:
        xpos 0.5 xanchor 0.0 yalign 0.9
        xpadding 20
        ypadding 20
        idle_background Frame("gui/framebtn.png",10,10)
        hover_background Frame("gui/framefxn2.png",10,10)
        # foreground ItemPriceDisplay(item_selected)
        vbox:
            if item_selected.type=="Item":
                hbox:
                    xalign 0.0 yalign 0.5
                    image "images/Cards/items/"+item_selected.object.NAME+".png"

                    null width 10
                    frame:
                        background Null()
                        xsize 170
                        text item_selected.object.NAME+"{size=12}\n\n"+item_selected.object.DESC+"{/size}" yalign 0.0
            elif item_selected.type=="Battleware":
                hbox:
                    xalign 0.0 yalign 0.5

                    # use Card(item_selected.object,)
                    # image "images/Cards/"+item_selected.object.NAME+".png" at shopcardsize
                    use Card(item_selected.object,(0,0),1.0)
                    null width 10
                    frame:
                        background Null()
                        xsize 170
                        vbox:
                            text item_selected.object.NAME yalign 0.0
                            text "{size=12}MAG = "+str(item_selected.object.MAG)+"\nBITS = "+str(item_selected.object.COST)+"{/size}" yalign 0.0

                            add FunctionList(item_selected.object.FXN)

                            fixed:
                                xalign 1.0
                                button:
                                    id "button1"
                                    frame:
                                        xsize 150
                                        idle_background Frame("gui/framebtn.png",10,10)
                                        hover_background Frame("gui/framefxn2.png",10,10)
                                        hbox:
                                            yalign 0.5 xalign 0.5
                                            text "Buy" yalign 0.5
                                            null width 10
                                            add ItemPriceDisplay(item_selected)
                                    action Call("buyitem",item_selected)
                                null height 10
                                button:
                                    frame:
                                        xsize 150
                                        idle_background Frame("gui/framebtn.png",10,10)
                                        hover_background Frame("gui/framefxn2.png",10,10)
                                        text "Cancel" yalign 0.5 xalign 0.5
                                    action SetVariable("shop_view",False), Return("Cancel")
    # key "dismiss" action Return()
init python:
    def buyitem(item_to_buy):
        global Money
        itemprice = item_to_buy.price
        renpy.say("info","Itemconfirm")
        if itemprice > Money:

            renpy.say("info","You can't afford this item!")
        else:
            Money -= itemprice
            # renpy.say("info","Bought 1 [item_to_buy.name]!")
            inventory.append(item_to_buy.object)
    # quant =lambda : itemquantity
        # return
screen shop_quant():
    # $ quant =

    style_prefix "say"
    zorder 30
    # key "dismiss" action Hide("shop_quant"),Jump("shop_quant_confirm")
    key "x" action Hide("shop_quant"),Jump("shopNo")
    key "X" action Hide("shop_quant"),Jump("shopNo")
    key "K_UP" action (Play("sound","sound/click.wav"),SetVariable("itemquantity",itemquantity+1) if (itemquantity<100) else NullAction())
    key "repeat_K_UP" action (Play("sound","sound/click.wav"),SetVariable("itemquantity",itemquantity+1) if (itemquantity<100) else NullAction())
    key "K_DOWN" action (Play("sound","sound/click.wav"),SetVariable("itemquantity",itemquantity-1) if (itemquantity>1) else NullAction())
    key "repeat_K_DOWN" action (Play("sound","sound/click.wav"),SetVariable("itemquantity",itemquantity-1) if (itemquantity>1) else NullAction())

    # key "K_DOWN" action If((itemquantity>1),SetVariable("itemquantity",itemquantity-1))
    # key "repeat_K_UP" action If((itemquantity<100),SetVariable("itemquantity",itemquantity+1))
    # key "repeat_K_DOWN" action If((itemquantity>1),SetVariable("itemquantity",itemquantity-1))
    hbox:
        pos(604,618) anchor (0,0)
        frame:
            xsize 180
            ysize 36
            style "deckframe"
            text str(itemquantity) xpos 0.98 xanchor 1.0
        spacing 10
        textbutton "↑":
            id "shopincreasequant"
            action (SetVariable("itemquantity",itemquantity+1) if (itemquantity<100) else NullAction())
        textbutton "↓":
            id "shopdecreasequant"
            action (SetVariable("itemquantity",itemquantity-1) if (itemquantity>1) else NullAction())
        textbutton "OK":
            id "shopconfirmquant"
            action Hide("shop_quant"),Jump("shop_quant_confirm")
        textbutton "Cancel":
            id "shopcancelquant"
            action Hide("shop_quant"),Jump("shopNo")
        # textbutton "Yes" action Hide("shop_quant"), Jump("shopYes"):
        #     id "buttonyes"
        # null width 20
        # textbutton "No" action  Hide("shop_quant"),Jump("shopNo")

screen shop_prompt():
    on "show":
        action MouseMove(x=633, y=635, duration=.3)
        # Function(renpy.set_focus,"shop_prompt", "buttonyes")
    style_prefix "say"
    zorder 30
    # key "dismiss" action Hide("shop_prompt"),Jump("shop_prompt")
    key "x" action Hide("shop_prompt"),Jump("shopNo")
    key "X" action Hide("shop_prompt"),Jump("shopNo")

    hbox:
        pos(603,617) anchor (0,0)

        textbutton "Yes" action Hide("shop_prompt"), Jump("shopYes"):
            id "buttonyes"
        null width 20
        textbutton "No" action  Hide("shop_prompt"),Jump("shopNo")

default say_shop_mode = False
label shopquant:
    if (itemprice * int(itemquantity)) > Money:
        $ Stoned_m="sad"
        $ Stoned_e="up"

        s"You can't afford to buy [itemquantity] [item_to_buy.name]!"
        $ Stoned_m="happy"
        $ Stoned_e="normal"
        pause 0.8
        hide screen say
        $ can_buy = False
    return
label buyitem(item_to_buy):
    $ itemprice = item_to_buy.price
    $ say_shop_mode = True
    $ itemquantity=1
    $ can_buy = True
    call shopquant


    # if itemprice * itemquantity > Money:
    #     $ Stoned_m="sad"
    #     $ Stoned_e="up"
    #
    #     s"You can't afford to buy [item_to_buy.name]!"
    #     $ Stoned_m="happy"
    #     $ Stoned_e="normal"
    #     pause 0.8
    #     hide screen say

    if can_buy:
        show screen shop_prompt
        $ renpy.set_focus("shop_prompt", "buttonyes")
        s"Are you sure you want to buy [item_to_buy.name]?"
        label shopprompt:
            pass
        pause
        hide screen shop_prompt
    return
label shopYes:
    show screen shop_quant()
    $ renpy.set_focus("shop_quant", "shopconfirmquant")
    s"How many [item_to_buy.name] do you want to buy?"
    label shop_quant_confirm:
    # call shopquant
    #
    hide screen shop_quant
    if (itemprice * int(itemquantity)) > Money:
        $ Stoned_m="sad"
        $ Stoned_e="up"

        s"You can't afford to buy [itemquantity] [item_to_buy.name]!"
        $ Stoned_m="happy"
        $ Stoned_e="normal"
        pause 0.8
        hide screen say

    else:
        $ MoneyDamage=itemprice*itemquantity
        $ Money -= MoneyDamage

        $ renpy.call("GainItem",[item_to_buy]*itemquantity)
        s"Thanks."
        $ renpy.set_focus("item_shop", "shop_button"+str(lastshop_item))


        # $ inventory.append(item_to_buy.object)
        jump shopprompt
label shopNo:
    $ renpy.set_focus("item_shop", "shop_button"+str(lastshop_item))
    # s "Ok."

    pass
    jump shopprompt


label GainItem(items):
    $ gain_index=0

    if items!=[]:
        $ items_counts= {z: ([y.name for y in items].count(z)) for z in  [z.name for z in items]}
        $ gainitem_objects=[]
        python:
            for x in items:
                if (x.object.NAME not in [y.NAME for y in gainitem_objects]):
                    gainitem_objects.append(x.object)
        $ gainitemshown =[]
        label gainloop:

            $ newitem=items[gain_index]

            # $ gba_inventory.append(newitem)
            if newitem.type=="Battleware":
                $ currentcard = newitem.object
                $ card_inventory.append(newitem.object)
            elif newitem.type=="Item":
                $ inventory.append(newitem.object)
            elif newitem.type=="Material":
                $ inventory.append(newitem.object)
            hide screen gain_item
            if newitem.name not in gainitemshown:
                show screen gain_item(newitem,items_counts[newitem.name])
                $ renpy.pause(1.2,hard=True)
            $ gainitemshown.append(newitem.name)
            hide screen gain_item
            $ gain_index+=1
            if gain_index<len(items):
                jump gainloop
            return
screen gain_item(gainitem,itemcount=1):
    # frame:
    #     at gainitem_bounce
    #     background Null()
    #     xpos 461 ypos 179
    #     xminimum 718
    #     yminimum 708
        timer 0.4 action Play("sound","sfx/sfx_coin_cluster6.wav")
        # zorder 20
        frame:
            at gainitem_bounce
            xminimum 150
            yminimum 150
            xalign 0.5
            yalign 0.5
            background Frame("gui/frame.png", 72, 32)
            vbox:

                text "{b}DOWNLOAD!{/b}" xalign 0.5
                null height 10
                if gainitem.type=="Battleware":
                    image "cardflasher" at cardzoom(0.75)
                # else:
                    # add "images/Cards/items/"+item.name+".png"
                elif gainitem.type=="Material":
                    image "images/Cards/items/Material.png" xalign 0.5
                else:
                    image "images/Cards/items/"+gainitem.name+".png" xalign 0.5
                if itemcount >1:
                    text "{size=24}{b}x"+str(itemcount)+"{/size}{/b}" at bottomright
                null height 10
                text "{size=24}[gainitem.name]{/size}" xalign 0.5

transform gainitem_bounce:
    zoom 1.5 alpha 1.0
    yoffset -60
    pause 0.4
    ease 0.1 yoffset -20
    pause 0.4
    ease 0.4 alpha 0.0
###
