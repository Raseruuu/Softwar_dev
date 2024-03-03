

init -2 python:


    # def map_token(mapsheet):
    #   newmap = []
    #   for rows in mapsheet:
    #     newmap.append([ch for ch in rows])

    #   return (newmap)

    # stage


    # class Place:
    #     def __init__(self,name,mapbox,safe)
    #         self.name = name
    #         self.mapbox = mapbox
    #         self.safe = safe
    # stageproto = [
    #     "1111111111111111",
    #     "1000000000000001",
    #     "1000000000000001",
    #     "1000000000000001",
    #     "1000000000000001",
    #     "1000000000000001",
    #     "1000000000000001",
    #     "1000000000000001",
    #     "1000000000000001",
    #     "1111111111111111"
    #     ]
    # stageproto = map_token(stage)


    from copy import deepcopy
    globals()["GRID"] ={
        #x y
        (188,160):deepcopy(stageABC),
        (191,160):deepcopy(stageABC),
        (192,160):deepcopy(stageABC),
        (193,160):deepcopy(stageABC),
        (194,160):deepcopy(stageABC),

        (185,161):deepcopy(stageABC),
        (186,161):deepcopy(stageABC),
        (187,161):deepcopy(stageAC),
        (188,161):deepcopy(stage_SDS),
        (189,161):deepcopy(stageAB),
        (190,161):deepcopy(stageACD),
        (191,161):deepcopy(stageBD),
        (192,161):deepcopy(stageBC),
        (193,161):deepcopy(stageBC),
        (194,161):deepcopy(stageBCD),
        (195,161):deepcopy(stageABCD),

        (184,162):deepcopy(stageACD),
        (185,162):deepcopy(stageD),
        (186,162):deepcopy(stageBD),
        (187,162):deepcopy(stageBCD),
        (188,162):deepcopy(stageABC),
        (189,162):deepcopy(stageCD),
        (190,162):deepcopy(stageA),
        (191,162):deepcopy(stageAD),
        (192,162):deepcopy(stageD),
        (193,162):deepcopy(stageD),
        (194,162):deepcopy(stageAD),
        (195,162):deepcopy(stageAB),

        (184,163):deepcopy(stageACD),
        (185,163):deepcopy(stageABD),
        (186,163):deepcopy(stageAC),
        (187,163):deepcopy(stageAD),
        (188,163):deepcopy(stageB),
        (189,163):deepcopy(stageABC),
        (190,163):deepcopy(stageBC),
        (191,163):deepcopy(stageABC),
        (192,163):deepcopy(stageABC),
        (193,163):deepcopy(stageACD),
        (194,163):deepcopy(stageABD),
        (195,163):deepcopy(stageC),
        (196,163):deepcopy(stageABD),

        (184,164):deepcopy(stageAC),
        (185,164):deepcopy(stageABD),
        (186,164):deepcopy(stageBC),
        (187,164):deepcopy(stageABC),
        (188,164):deepcopy(stageBC),
        (189,164):deepcopy(stageBCD),
        (190,164):deepcopy(stageBC),
        (191,164):deepcopy(stageAC),
        (192,164):deepcopy(stage_ShadyAlley),#MELISSA AREA
        (193,164):deepcopy(stageAB),
        (194,164):deepcopy(stageACD),
        (195,164):deepcopy(stageBD),


        (183,165):deepcopy(stageACD),
        (184,165):deepcopy(stageBD),
        (185,165):deepcopy(stageABC),
        (186,165):deepcopy(stageCD),
        (187,165):deepcopy(stageABD),
        (188,165):deepcopy(stageCD),
        (189,165):deepcopy(stageAB),
        (190,165):deepcopy(stageCD),
        (191,165):deepcopy(stageBD),
        (192,165):deepcopy(stageBCD),
        (193,165):deepcopy(stageCD),
        (194,165):deepcopy(stageAD),
        (195,165):deepcopy(stageAB),

        (183,166):deepcopy(stageACD),
        (184,166):deepcopy(stageAD),
        (185,166):deepcopy(stageBD),
        (186,166):deepcopy(stageAC),
        (187,166):deepcopy(stageABD),
        (188,166):deepcopy(stageACD),
        (189,166):deepcopy(stage_Undernet),
        (190,166):deepcopy(stageAD),
        (191,166):deepcopy(stageAD),
        (192,166):deepcopy(stageAD),
        (193,166):deepcopy(stageAD),
        (194,166):deepcopy(stageABD),
        (195,166):deepcopy(stageC),
        (196,166):deepcopy(stageABD),

        (183,167):deepcopy(stageABC),
        (184,167):deepcopy(stageABC),
        (185,167):deepcopy(stageABC),
        (186,167):deepcopy(stage_Cafella),
        (187,167):deepcopy(stageACD),
        (188,167):deepcopy(stageAB),
        (189,167):deepcopy(stageAC),
        (190,167):deepcopy(stageABD),
        (191,167):deepcopy(stage_WestGateway),#BITWULF AREA Chapter2
        (192,167):deepcopy(stageAD),
        (193,167):deepcopy(stageABD),
        (194,167):deepcopy(stageACD),
        (195,167):deepcopy(stageBD),

        (183,168):deepcopy(stageACD),
        (184,168):deepcopy(stageABD),
        (185,168):deepcopy(stageBC),
        (186,168):deepcopy(stage_AdaU),
        (187,168):deepcopy(stageABC),
        (188,168):deepcopy(stageBCD),
        (189,168):deepcopy(stage_Bytes),
        (190,168):deepcopy(stageAD),
        (191,168):deepcopy(stageABD),
        (192,168):deepcopy(stagehome),
        (193,168):deepcopy(stageACD),
        (194,168):deepcopy(stageAD),
        (195,168):deepcopy(stageAB),

        (183,169):deepcopy(stageACD),
        (184,169):deepcopy(stageAB),
        (185,169):deepcopy(stageBC),
        (186,169):deepcopy(stageBCD),
        (187,169):deepcopy(stageABC),
        (188,169):deepcopy(stage_Square),
        (189,169):deepcopy(stageBCD),
        (190,169):deepcopy(stageAC),
        (191,169):deepcopy(stageAB),
        (192,169):deepcopy(stageABC),
        (193,169):deepcopy(stageAC),
        (194,169):deepcopy(stageABD),
        (195,169):deepcopy(stageC),
        (196,169):deepcopy(stageABD),

        (183,170):deepcopy(stageABCD),
        (184,170):deepcopy(stageBCD),
        (185,170):deepcopy(stageCD),
        (186,170):deepcopy(stageAD),
        (187,170):deepcopy(stage_Library),
        (188,170):deepcopy(stageABD),
        (189,170):deepcopy(stage_Battlewareshop),
        (190,170):deepcopy(stageBC),
        (191,170):deepcopy(stageBC),
        (192,170):deepcopy(stageBCD),
        (193,170):deepcopy(stageBC),
        (194,170):deepcopy(stageACD),
        (195,170):deepcopy(stageBD),

        (183,171):deepcopy(stageACD),
        (184,171):deepcopy(stageAD),
        (185,171):deepcopy(stageAD),
        (186,171):deepcopy(stageAD),
        (187,171):deepcopy(stageABD),
        (188,171):deepcopy(stageACD),
        (189,171):deepcopy(stageAB),
        (190,171):deepcopy(stageBCD),
        (191,171):deepcopy(stageBC),
        (192,171):deepcopy(stageABC),
        (193,171):deepcopy(stageCD),
        (194,171):deepcopy(stageAD),
        (195,171):deepcopy(stageAB),

        (183,172):deepcopy(stageACD),
        (184,172):deepcopy(stageABD),
        (185,172):deepcopy(stageAC),
        (186,172):deepcopy(stageAB),
        (187,172):deepcopy(stageABC),
        (188,172):deepcopy(stageAC),
        (189,172):deepcopy(stageD),
        (190,172):deepcopy(stageAB),
        (191,172):deepcopy(stageC),
        (192,172):deepcopy(stageD),
        (193,172):deepcopy(stageAB),
        (194,172):deepcopy(stageABC),
        (195,172):deepcopy(stageC),
        (196,172):deepcopy(stageABD),

        (183,173):deepcopy(stageACD),
        (184,173):deepcopy(stageAB),
        (185,173):deepcopy(stageCD),
        (186,173):deepcopy(stageBD),
        (187,173):deepcopy(stageAC),
        (188,173):deepcopy(stageBD),

        (190,173):deepcopy(stageBCD),
        (191,173):deepcopy(stageBCD),

        (193,173):deepcopy(stageBCD),
        (194,173):deepcopy(stageBCD),
        (195,173):deepcopy(stageBCD),

        (184,174):deepcopy(stageCD),
        (185,174):deepcopy(stageAB),
        (186,174):deepcopy(stageAC),
        (187,174):deepcopy(stageBD),

        (185,175):deepcopy(stageBCD),
        (186,175):deepcopy(stageBCD),
        }
    mapeventsdictdefault={

    }
    mapeventsdict={
        # (192,168):[homeevents],
        
        }
    mapeventschapter0={
        
    }
    mapeventschapter1={
        (191,167):[Chapter2events]
    }
    mapeventschapter2={
    }
    mapeventschapter3={
    }
    mapeventschapter4={
    }
    mapeventschapter5={
    }
    mapeventschapter6={
    }
    mapeventschapter7={
    }
    mapeventschapter8={
    }

    mapeventsdicts=[
            mapeventschapter0,
            mapeventschapter1,
            mapeventschapter2,
            mapeventschapter3,
            mapeventschapter4,
            mapeventschapter5,
            mapeventschapter6,
            mapeventschapter7,
            mapeventschapter8
        ]
    mapspritesdictdefault={
        (192,168):[Heartsprite],
        # (192,164):[Melissasprite],
        (192,164):[Melissasprite],
        (192,165):[Bellasprite],

        (191,167):[Bitwulf_C2],
        (193,167):[Programkunsprite]
        }
    mapspriteschapter0 = {
        
    }
    mapspriteschapter1 = {
        (192,164):[Stellasprite,Melissasprite],
    }
    mapspriteschapter2 = {
        
    }
    mapspriteschapter3 = {
        
    }
    mapspriteschapter4 = {
        
    }
    mapspriteschapter5 = {
        
    }
    mapspriteschapter6 = {
        
    }
    mapspriteschapter7 = {
        
    }
    mapspriteschapter8 = {
        
    }
    mapspritesdicts=[mapspriteschapter0,mapspriteschapter1,mapspriteschapter2,mapspriteschapter3,mapspriteschapter4,mapspriteschapter5,mapspriteschapter6,mapspriteschapter7,mapspriteschapter8]
    mapwheredict={
        (192,168):"Home_Page",
        (192,164):"Shady_Alley",

        (191,167):"West_Gateway",
        (193,167):"East_Gateway",

        (188,169):"Connecht_Square"
        }
# label eventdoor:
#     ""
#     return




label doorjump:
    $ linearmaptransform=False
    $ doordirection = Here #abcd
    # a =North
    # b =East
    # c =West
    # d =South
    if doordirection == "a":
        $gridpos[1] = gridpos[1] - 1
    elif doordirection == "b":
        $gridpos[0] = gridpos[0] + 1
    elif doordirection == "c":
        $gridpos[0] = gridpos[0] - 1
    elif doordirection == "d":
        $gridpos[1] = gridpos[1] + 1

    $ GRIDX= gridpos[0]
    $ GRIDY= gridpos[1]

    $ Grid_D_root=digital_root(GRIDX+GRIDY)

    # globals()["GRID"][GRIDX,GRIDY] in
    # if thereisaroom on this position

    if (GRIDX,GRIDY) in globals()["GRID"]:
        $ griddestination = globals()["GRID"][(GRIDX,GRIDY)]
        $ transfercoordinates = nextlocation(griddestination,doordirection)
        call maptransfer(transfercoordinates,griddestination) from _call_maptransfer

    elif (((((Grid_D_root==1) or (Grid_D_root==2)) or (Grid_D_root==4)) or (Grid_D_root==5)) or (Grid_D_root==7)) or (Grid_D_root==8):
        $griddestination = stage124578
        $transfercoordinates = nextlocation(griddestination,doordirection)
        call maptransfer(transfercoordinates,griddestination) from _call_maptransfer_1

    elif ((Grid_D_root==3) or (Grid_D_root==6)) or (Grid_D_root==9):
        $griddestination = stage369
        $transfercoordinates = nextlocation(griddestination,doordirection)
        call maptransfer(transfercoordinates,griddestination) from _call_maptransfer_2
    else:
        $griddestination = stageemptyroom
        $transfercoordinates = nextlocation(griddestination,doordirection)
        call maptransfer(transfercoordinates,stageemptyroom) from _call_maptransfer_3

    $ linearmaptransform=True
    return
