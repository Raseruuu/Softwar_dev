default norandomencounters= 0



init python:
    def UseItem(item):
        if len(item.FXN)!=0:
            if item.FXN[0] == "Recover":
                global playerHP
                global playerHPMax
                if playerHP<playerHPMax:
                    renpy.play("sfx/healx.ogg","sound")
                    healexcess=(playerHP+item.FXN[1]-playerHPMax)
                    healvalue=(item.FXN[1])
                    if healexcess>0:
                        healvalue-=healexcess
                    playerHP+=healvalue
                    if playerHP>playerHPMax:
                        playerHP=playerHPMax

                    renpy.notify("Healed "+str(healvalue)+" HP.")
                    for index,inv_item in enumerate(inventory):
                        if "SoftDrink" == inv_item.NAME:
                            inventory.pop(index)
                            break
                else:
                    renpy.play("sfx/sfx_damage_hit8.wav","sound")
                    renpy.notify("Your HP is full.")
            #       NAME            TYPE        DESC                                            FXN
    SoftDrink=Item("SoftDrink", "Consumable",   "For thirsty Software! \nRecovers 200 HP.",     ["Recover",200])
    SmallEnergy=Item("SmallEnergy", "Consumable",   "Small HP Energy! \nRecovers 250 HP.",     ["Recover",250])
    MediumEnergy=Item("MediumEnergy", "Consumable",   "Medium HP Energy! \nRecovers 500 HP.",     ["Recover",500])
    LargeEnergy=Item("LargeEnergy", "Consumable",   "Large HP Energy! \nRecovers 1000 HP.",     ["Recover",1000])
    Unlocker=Item("Unlocker",   "Key",        "Unlock locked Mystery Data. \nSingle use only.",   ["Unlock"])
    Antibody=Item("Antibody", "Consumable",   "Activates a temporary Safe Mode!\nRepels Viruses.",["Repel"])

    Datanium=Item("Datanium", "Material", "Data metal alloy.\nConducts electricity.",[])
    Informium=Item("Informium", "Material", "Processed Datanium.",[])
    W00D = Item("W00D", "Material","Wave-00-Data. Versatile material from Trojans.",[])
    Zereum = Item("Zereum", "Material","The element of Nothingness.",[])
    Oneum = Item("Oneum", "Material","The element of Somethingness.",[])
    Binon = Item("Binon", "Material","The Binary element.",[])
    Lambdium = Item("Lambdium", "Material","Essential wave component.",[])#WIND ELEMENT
    Photoceptor =  Item("Photoceptor", "Material","Spyware's eye component.",[])
    Iteratium =  Item("Iteratium", "Material","Gathered energy from loop iterations.",[])
    Strinnium = Item("Strinnium", "Material","Essence of string data.\n Connects things together.",[])
    Duplirium = Item("Duplirium", "Material","Gives Viruses the ability to duplicate.",[])
    Conflagrium = Item("Conflagrium", "Material","Material that stores Data Fire.",[]) #FIRE ELEMENT
    Combustium = Item("Combustium", "Material","Digital gunpowder.",[]) #Gunpowder
    Streamine = Item("Streamine", "Material","Azure fluid data.",[]) #WATER ELEMENT
    Neuron = Item("Neuron", "Material","Cybernetic brain cell.",[]) #Brain
    Hematocyte = Item("Hematocyte", "Material","Cybernetic blood cell.",[]) #Blood

    # Turbulene = Item("Turbulene", "Material","Turbulent data.",[])
    # Laminum = Item("Laminium", "Material","Laminar data.",[])

    battledrops={
        "Trojan Horse":[Datanium,W00D],
        "Keylogger":[Datanium,Iteratium],
        "Ransomware":[Conflagrium,Iteratium],
        "Rootkit":[Datanium,Strinnium],
        "Worm":[Duplirium,Lambdium],
        "Spyware":[Photoceptor,Streamine],
        "Vira":[Hematocyte,Informium],
        "Code Red":[Lambdium,Lambdium],
        "ILY":[Datanium,Hematocyte],

    }
