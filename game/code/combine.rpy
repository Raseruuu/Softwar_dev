
init python:
    class CraftItem:
        def __init__(self,name,object,components):
            self.name = name
            self.object = object
            self.components = components
    battleware_master_dict={
        "SparkBuster":SparkBuster,
        "Katana":Katana,
        "LambdaSaber":LambdaSaber,
        "RadioShield":RadioShield,
        "DrainShield":DrainShield,
        "FieryArc":FieryArc,
        "CosmicArc":CosmicArc,
        "SpiderAmulet":SpiderAmulet,
        "SnipeSensor":SnipeSensor,
        "LunexGunSaber":LunexGunSaber,
        "CupidArc":CupidArc,
        "DataArc":DataArc,
        "DataForce":DataForce,
        "DataSaber":DataSaber,
        "VirusFlame":VirusFlame,
        "DataBomb":DataBomb,
        "Flashbang":Flashbang,
        "Gigamorph":Gigamorph,
        "DataBuster":DataBuster,
        "Bitbuster":Bitbuster,
        "MachineBuster":MachineBuster,
        "Excalibrium":Excalibrium,
        "ILYFlash":ILYFlash,
        "RecursiveSlash":RecursiveSlash,
        "MailSaber":MailSaber,
        "ChocolateBar":ChocolateBar,
        "BruiseBash":BruiseBash,
        "ZSlash":ZSlash,
        "FreezeWave":FreezeWave,
        "FreezingBlade":FreezingBlade,
        "Salamandra":Salamandra,
        "BusterSword":BusterSword,
        "FlameFists":FlameFists,
        # "Gigacore":Gigacore,
        "UltraHead":UltraHead,
        "NitroArms":NitroArms,
        "VoltLegs":VoltLegs,
        "GUNVAR":GUNVAR,
        # "ArmorReactor":ArmorReactor,
        "Shotgun":Shotgun,
        "Laserbeam":Laserbeam,
        "SwordOfTruth":SwordOfTruth,
        "SwordOfLies":SwordOfLies,
        "VBlaze":VBlaze
    }
    def read_combination_tsv(filename):
            file = renpy.file(filename)
            # file = open(filename, "r")
            craft_dictionary = {}
            for i, line in enumerate(file):

                if i > 1:
                    line = str(line).replace("\n", '').replace('\r', '')
                    linearray = line.split('\t')
                    print(linearray)
                    # craftcomponents=[linearray[1],linearray[2],linearray[3]]
                    craftcomponents=[linearray]
                    craft_dictionary[linearray[0]] = CraftItem(linearray[0],battleware_master_dict[linearray[0]],craftcomponents)
                    # lines.append(line.split('\t'))
                # num_lines=[]
                # for line in lines:
                #     num_lines.append(list(map(int, line)))
                # print(num_lines)
            return craft_dictionary
    combinationlibrary=[]
    # combinationsraw=read_combination_tsv("code/tsv/Combination.tsv")

    # comb_library = combinationsraw.values()
    last_craftitem = 0

screen CombineMenu():
    use pauselayout("COMBINE")
    on "show":

        action Play("music","bgm/Shop_bgm_maoudamashii_acoustic41.mp3")
    on "hide":
        action Play("music","bgm/ost/Grid_noyemi_K.mp3")
    key "x" action SetVariable("shop_active",False), Return()

        # for create_index, item in enumerate(comb_library):
    # frame:
    #     background Null()
    #     hbox:
    #         text ""
    #         for comps in craftitem.components:
    #             frame:
    #                 add "images/Cards/items/[comps].png"
    frame:
        style "nvl_window"

        text "{b}BUILD BATTLEWARE{/b}"
        top_padding 2

        if not noscreentransformsfornow:
            at pausetrans2
        vbox:
            null height 32
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                hbox:
                    grid 1 40:
                        xspacing 20
                        for create_index, craftitem in enumerate(comb_library):
                            frame:
                                xsize 740
                                ysize 175
                                xpadding 10
                                ypadding 10
                                background Frame("gui/framefxn.png",10,10)
                                vbox:
                                    # elif craftitem.type=="Battleware":
                                    hbox:
                                        xalign 0.0 yalign 0.5
                                        image "images/Cards/"+craftitem.object.NAME+".png" at shopcardsize
                                        null width 10
                                        frame:
                                            background Null()
                                            xsize 170
                                            hbox:
                                                vbox:
                                                    text craftitem.object.NAME yalign 0.0
                                                    text "{size=12}MAG = "+str(craftitem.object.MAG)+"\nBITS = "+str(craftitem.object.COST)+"{/size}" yalign 0.0
                                                    add FunctionList(craftitem.object.FXN)
                                                null width 58
                                                vbox:
                                                    yalign 0.0
                                                    # vbox:

                                                    text "Components:"
                                                        # background Null()
                                                    hbox:
                                                        for component in craftitem.components:
                                                            if component!="":
                                                                frame:
                                                                    style "battlestats_frame"
                                                                    text "{size=12}  [component]{/size}"
                                                    button:
                                                        id "shop_button"+str(create_index)
                                                        xalign 0.0
                                                        frame:
                                                            xsize 150
                                                            idle_background Frame("gui/framefxn.png",10,10)
                                                            hover_background Frame("gui/framefxn2.png",10,10)
                                                            hbox:
                                                                yalign 0.5 xalign 0.5
                                                                text "COMBINE" yalign 0.5
                                                                null width 10
                                                                # add craftitemPriceDisplay(craftitem)
                                                        # sensitive (craftitem.price<=money)
                                                        action SetVariable("last_craftitem",create_index),Call("build_ware",craftitem)


label build_ware:

screen Combineinventory():
    # use Battleware("COMBINE"):
        frame:
            ysize 40 yalign 0.5
            textbutton "{size=14}Combine{/size}" action NullAction() yalign 0.5

style game_grid_button:
    background Frame("gui/framefxn.png", 4, 4, tile=gui.frame_tile)
    hover_background Frame("gui/framefxn2.png", 4, 4, tile=gui.frame_tile)
    xsize 360
    ysize 94

    right_padding 14
    left_padding 14
    bottom_padding 14
    top_padding 14
style game_grid_text:
    size 40
    xalign 0.5 yalign 0.5
screen FAI_menu:
    use pauselayout("FAI")
    frame:
        style "game_menu_content_frame"
        at pausetrans2
        xanchor 0.0 xpos 0.5 yanchor 0.0 ypos 0.24
        vbox:
            style_prefix "game_grid"
            button:

                text "Active FAI"
                action Return("ActiveFAI")
                # xanchor 0.5 xpos 0.50 yanchor 0.5 ypos 0.34
            button:

                text "Customize"
                action Return("Customize")
                # xanchor 0.5 xpos 0.50 yanchor 0.5 ypos 0.34
    frame:
        if not noscreentransformsfornow:
            at pausetrans1
        style_prefix "stats"
        xalign 0.95 yalign 0.88
        hbox:
            # frame:
            #     # textbutton "Save" action SetVariable("noscreentransformsfornow",True), Return("SaveDeck")
            #     imagebutton idle Text("{size=35}Save{/size}") hover Text("{size=35}{color=f00}Save{/size}") action SetVariable("noscreentransformsfornow",True), Return("SaveDeck")

            # null height 10
            frame:
                imagebutton idle Text("{size=35}Back{/size}") hover Text("{size=35}{color=f00}Back{/size}"):
                    action SetVariable("noscreentransformsfornow",True), Return()

screen ware_menu:
    use pauselayout("BATTLEWARE")
    frame:
        style "game_menu_content_frame"
        at pausetrans2
        xanchor 0.0 xpos 0.5 yanchor 0.0 ypos 0.24
        vbox:
            style_prefix "game_grid"
            button:

                text "Equipped"
                action Return("Equipped")
                # xanchor 0.5 xpos 0.50 yanchor 0.5 ypos 0.34
            button:
                text "Decks"
                action Return("Decks")
                # xanchor 0.5 xpos 0.50 yanchor 0.5 ypos 0.56
            button:
                text "Create"
                action Return("Create")
                # xanchor 0.5 xpos 0.50 yanchor 0.5 ypos 0.56
            button:
                text "Collection"
                action Return("Collection")
                # xanchor 0.5 xpos 0.50 yanchor 0.5 ypos 0.56
    frame:
        if not noscreentransformsfornow:
            at pausetrans1
        style_prefix "stats"
        xalign 0.95 yalign 0.88
        hbox:
            # frame:
            #     # textbutton "Save" action SetVariable("noscreentransformsfornow",True), Return("SaveDeck")
            #     imagebutton idle Text("{size=35}Save{/size}") hover Text("{size=35}{color=f00}Save{/size}") action SetVariable("noscreentransformsfornow",True), Return("SaveDeck")

            # null height 10
            frame:
                imagebutton idle Text("{size=35}Back{/size}") hover Text("{size=35}{color=f00}Back{/size}"):
                    action SetVariable("noscreentransformsfornow",True), Return()
