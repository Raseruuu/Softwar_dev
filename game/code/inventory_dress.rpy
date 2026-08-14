init python:
    
    
    #   NAME,TYPE,DESC,FXN  
    Unequip = Item_dress("Unequip","Outfit","Remove ILY's current outfit")    
    Uniform = Item_dress("Uniform","Outfit","ILY's regular outfit! It's like a College student's uniform.")
    UniformBig = Item_dress("UniformBig","Outfit","ILY's regular outfit! It's like a College student's uniform.")
    Garden = Item_dress("Garden","Outfit","A Green Gardener's dress.")
    BladeArmor = Item_dress("BladeArmor","Outfit","ILY's Most powerful armor!")
    Bloomers = Item_dress("Bloomers","Outfit","Bloomers are good for Physical exercise!")
    PinkDress = Item_dress("PinkDress","Outfit","A cute casual outfit!")
    CowGirl = Item_dress("CowGirl","Outfit","Something strange happened to ILY's breasts...")
    BikiniArmor = Item_dress("BikiniArmor","Outfit","The charming and beautiful knightess charges on!")
    SoulReaper = Item_dress("SoulReaper","Outfit","Uniform worn by spirit warriors that maintain order!")
    BlackBelts = Item_dress("BlackBelts","Outfit","What is this style called? I like it!")
    CasualRed = Item_dress("CasualRed","Outfit","Casual outfit.")
    DarkQueen = Item_dress("DarkQueen","Outfit","The Darkness from within reveals itself...")
    MaidUniform = Item_dress("MaidUniform","Outfit","I'm your maid now! Goshujin-sama!")
    Transporter = Item_dress("Transporter","Outfit","I am a transporter from the wasteland ~!")
    Mummy = Item_dress("Mummy","Outfit","Mummies can revive after many years according to legend...")

    ArmorBikini = Item_dress("ArmorBikini","Underwear","The charming and beautiful knightess charges on!")
    Red_underwear=Item_dress("Red","Underwear","ILY's Default underwear.")
    Red2_underwear=Item_dress("Red2","Underwear","This one is red too.")
    White_underwear = Item_dress("White","Underwear","Classic underwear.")
    Sports_underwear=Item_dress("Sports","Underwear","Humans wear fitted clothes to move easily when doing physical activities!")
    Straps_underwear=Item_dress("Straps","Underwear","This one keeps things together quite nicely.")
    Coworker_underwear=Item_dress("Coworker","Underwear","This is a special cow-print bikini I got from that one farm job I had.")
    Bunny_underwear=Item_dress("Bunny","Underwear","A popular Bunny suit! I can wear this leotard under my clothes. This one is a gift from Melissa.")
    Mummy_underwear=Item_dress("Mummy","Underwear","Mummies can revive after many years according to legend...")
    Bodysuit_underwear=Item_dress("Bodysuit","Underwear","This one covers the entire body. It's really tight but also sturdy somehow! Almost like it replaces ILY's skin.")
    


    inventory_dress=[
        Unequip,
        Garden,
        Uniform,
        PinkDress,
        Red_underwear,
        White_underwear,
        Sports_underwear,
        MaidUniform,
        BlackBelts,CasualRed,
        Bloomers,
        BikiniArmor,
        ArmorBikini,
        Transporter,
        Bodysuit_underwear
        ]
    
    def EquipDress(dresstype,dressname):
        currentoutfit= globals()["ILY_outfit"]
        currentunderwear= globals()["ILY_underwear"]
        if dressname=="Unequip":
            globals()["ILY_outfit"]=""
            globals()["ILY_stockings"]=""
            if currentunderwear=="":
                globals()["ILY_underwear"]="Red"
        elif dresstype.lower()=="outfit" and dressname!="Unequip":
            if dressname.lower()=="cowgirl" or dressname.lower()=="maid" :
                globals()["ILY_underwear"]=""
            elif globals()["ILY_underwear"]=="":
                globals()["ILY_underwear"]="red"
            if dressname.lower()=="bikiniarmor":
                globals()["ILY_underwear"]="ArmorBikini"

            if dressname.lower()=="mummy":
                globals()["ILY_underwear"]="mummy"
            if dressname.lower()=="bladearmor":
                globals()["ILY_underwear"]=""
            if dressname.lower()=="bloomers":
                globals()["ILY_stockings"]="socks"
            if dressname.lower()=="maiduniform":
                globals()["ILY_stockings"]=""
            if dressname.lower()=="uniform":
                globals()["ILY_stockings"]="stockings"
            if dressname.lower()=="garden":
                globals()["ILY_stockings"]=""
            if dressname.lower()=="transporter":
                globals()["ILY_underwear"]="bodysuit"
            
            
            globals()["ILY_outfit"]=dressname.lower()

        elif dresstype.lower()=="underwear":
            if currentoutfit=="cowgirl":
                globals()["ILY_outfit"]=""
            
            globals()["ILY_underwear"]=dressname.lower()
        # elif dressname=="Unequip":
        # renpy.notify(dressname+" is now equipped.")
        return    
default dress_select="Outfit"
init python:
    def dress_sort(dress_list,d_selection="Outfit"):
        new_dress_list=[]
        for dress_item in dress_list:
            if dress_item.TYPE==d_selection:
                new_dress_list.append(dress_item)
        return new_dress_list
screen Items_dress(itemsmode="CUSTOMIZE"):
    python:
        if itemsmode=="CUSTOMIZE":
            inventory_counts= {z: ([y.NAME for y in inventory_dress].count(z)) for z in  [z.NAME for z in inventory_dress]}
            inventory_objects=[]
            for x in inventory_dress:
                if (x.NAME not in [y.NAME for y in inventory_objects]):
                    inventory_objects.append(x)
            filtered_inventory_dress=dress_sort(inventory_objects)
        
    use pauselayout(itemsmode)
    frame:
        style "nvl_window"
        top_padding 32
        if not noscreentransformsfornow:
            at pausetrans2
        vbox:
            spacing 14
            hbox:
                button:
                    frame:
                        if dress_select=="Outfit": 
                            style_prefix "bit"
                        text "Outfit"
                    action SetVariable("dress_select","Outfit")
                button:
                    frame:
                        if dress_select=="Underwear": 
                            style_prefix "bit"
                        text "Underwear"
                    action SetVariable("dress_select","Underwear")
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                if dress_select=="Outfit":
                    hbox:

                        grid 1 len(dress_sort(inventory_objects,"Outfit")):
                            xspacing 16

                            for item in dress_sort(inventory_objects,"Outfit"):
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
                                                xsize 60
                                                ysize 60
                                                background "images/rpg/armor/"+item.TYPE+".png"
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
                                    if itemsmode=="CUSTOMIZE":
                                        action Function(EquipDress,item.TYPE,item.NAME)
                                    else:
                                        action NullAction()


                                        # text item.NAME
                            # for itemfiller in range(0,40-len(inventory)):
                            
                        null width 10
                elif dress_select=="Underwear":
                    hbox:

                        grid 1 len(dress_sort(inventory_objects,"Underwear")):
                            xspacing 16

                            for item in dress_sort(inventory_objects,"Underwear"):
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
                                                xsize 60
                                                ysize 60
                                                background "images/rpg/armor/"+item.TYPE+".png"
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
                                    if itemsmode=="CUSTOMIZE":
                                        action Function(EquipDress,item.TYPE,item.NAME)
                                    else:
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
