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
    SoulReaper = Item_dress("SoulReaper","Outfit","Uniform worn by spiritual warriors that maintain order!")
    BlackBelts = Item_dress("BlackBelts","Outfit","Uniform worn by spiritual warriors that maintain order!")
    
    
    ArmorBikini = Item_dress("ArmorBikini","Underwear","The charming and beautiful knightess charges on!")
    Red_underwear=Item_dress("Red","Underwear","ILY's Default underwear.")
    White_underwear = Item_dress("White","Underwear","Classic underwear.")
    Red_underwear=Item_dress("Red","Underwear","Default.")
    
    Bunny_underwear=Item_dress("Bunny","Underwear","A popular Bunny suit! This one is a gift from Melissa.")
    


    inventory_dress=[
        Unequip,
        Uniform,
        PinkDress,
        Red_underwear,
        White_underwear,
        UniformBig,
        CowGirl,
        BikiniArmor,
        ArmorBikini,
        BlackBelts
        ]
    
    def EquipDress(dresstype,dressname):
        currentoutfit= globals()["ILY_outfit"]
        currentunderwear= globals()["ILY_underwear"]
        if dressname=="Unequip":
            globals()["ILY_outfit"]=""
            if currentunderwear=="":
                globals()["ILY_underwear"]="Red"
        elif dresstype.lower()=="outfit" and dressname!="Unequip":
            if dressname.lower()=="cowgirl" or dressname.lower()=="maid" :
                globals()["ILY_underwear"]=""
            if dressname.lower()=="bikiniarmor":
                globals()["ILY_underwear"]="ArmorBikini"
            globals()["ILY_outfit"]=dressname.lower()

        elif dresstype.lower()=="underwear":
            if currentoutfit=="cowgirl":
                globals()["ILY_outfit"]=""
            
            globals()["ILY_underwear"]=dressname.lower()
        # elif dressname=="Unequip":
        # renpy.notify(dressname+" is now equipped.")
        return    
screen Items_dress(itemsmode="CUSTOMIZE"):
    python:
        if itemsmode=="CUSTOMIZE":
            inventory_counts= {z: ([y.NAME for y in inventory_dress].count(z)) for z in  [z.NAME for z in inventory_dress]}
            inventory_objects=[]
            for x in inventory_dress:
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

                grid 1 20:
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
                                        xsize 60
                                        ysize 60
                                        background "images/rpg/"+item.TYPE+".png"
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
                    for itemfiller in range(0,20-len(inventory_objects)):
                        null width 600
                        

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
