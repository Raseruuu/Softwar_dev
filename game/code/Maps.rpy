

init -2 python:
    def digital_root(a):
        while a>=10:
            b = int(a/10) #the rest of the other digits
            c = a-(b*10) #the rightmost digit
            a = b+c
        return a
    # import numpy
    def nextlocation(destinationstage,Door):
        newX=0
        newY=0
        founddoor=False
        if Door=="a":
            #d
            # search and get indexes of letter d
            gridmap = destinationstage
            for maprows in gridmap:
                if "d" in maprows:
                    newX=maprows.index("d")
                    founddoor=True
                if not founddoor:
                    newY+=1
            newY-=1
        elif Door=="b":
            #c
            # search and get indexes of letter c
            gridmap = destinationstage
            for maprows in gridmap:
                if "c" in maprows:
                    newX=maprows.index("c")
                    founddoor=True
                if not founddoor:
                    newY+=1
            newX+=1
        elif Door=="c":
            #b
            # search and get indexes of letter b
            gridmap = destinationstage
            for maprows in gridmap:
                if "b" in maprows:
                    newX=maprows.index("b")
                    founddoor=True
                if not founddoor:
                    newY+=1
            newX-=1
        elif Door=="d":
            #a
            # search and get indexes of letter a
            gridmap = destinationstage
            for maprows in gridmap:
                if "a" in maprows:
                    newX=maprows.index("a")
                    founddoor=True
                if not founddoor:
                    newY+=1
            newY+=1

        return (newX,newY)
    def map_token(mapsheet):
      newmap = []
      for rows in mapsheet:
        newmap.append([ch for ch in rows])

      return (newmap)
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
    stage0 = [
     #0  0     1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17
        '1111111',
        '1000001',
        '1000001',
        '1002001',
        '1000001',
        '1000001',
        '1000001',
        '1000001',
        '1000001',
        '1000001',
        '1000001',
        '1000001',
        '1000001',
        '1000001',
        '1110111',
        'nn111nn'
        ]
    stage0=map_token(stage0)
    stagea = [
     #0  0     1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17
        '111111111111111111',
        '100000100020000001',
        '10d000102000000001',
        '1110111010d0000001',
        'nn1010001010000001',
        'nn1010111010000001',
        'nn1000000010000001',
        '111001111010000001',
        '100001nn1011110101',
        '100001nn1000000101',
        '111111nn1111111111'
        ]
    stagea=map_token(stagea)
    stagehome = [
     #0  0     1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17
        '111111111111111',
        '1000000a0000001',
        '100000000000001',
        '100011111110001',
        '100010000010001',
        '1c00000000000b1',
        '100010000010001',
        '100011101110001',
        '100000000000001',
        '1000000d0000001',
        '111111111111111'
        ]
    stagehome=map_token(stagehome)
    stage1 = [

        'nnn11111111111',
        'n1110000000001',
        'n1000000000001',
        '11000000000001',
        '1c000000000001',
        '11000000000001',
        'n1000000000001',
        'n1110000000001',
        'nnn11111111111',
        ]
    stage1=map_token(stage1)
    stageemptyroom = [
        'nnn111nnn',
        'n111a111n',
        'n1000001n',
        '110000011',
        '1c00000b1',
        '110000011',
        'n1000001n',
        'n111d111n',
        'nnn111nnn',
        ]
    stageemptyroom=map_token(stageemptyroom)
    stage3 = [
        'nnn111nnn',
        'n111a111n',
        'n1000001n',
        '110000011',
        '1c00000b1',
        '110000011',
        'n1000001n',
        'n111d111n',
        'nnn111nnn'
        ]
    stage3=map_token(stage3)
    stagek=[
        'nnnnnnnnn111nnnnnnnnn',
        'nnnnnnnnn1a1nnnnnnnnn',
        'nnnnnnnnn101nnnnnnnnn',
        'nnnnnnnnn101nnnnnnnnn',
        'nnnn1111110111111nnnn',
        'nnnn1000000000001nnnn',
        '111110000000000011111',
        '1c00000000100000000b1',
        '111110000000000011111',
        'nnnn1000000000001nnnn',
        'nnnn1111110111111nnnn',
        'nnnnnnnnn101nnnnnnnnn',
        'nnnnnnnnn101nnnnnnnnn',
        'nnnnnnnnn1d1nnnnnnnnn',
        'nnnnnnnnn111nnnnnnnnn'
        ]
    stagek=map_token(stagek)
    stageABCD=[
        'nnnnnn111nnnnnn',
        'nnnnnn1a1nnnnnn',
        'nnnnnn101nnnnnn',
        'nnn111101111nnn',
        'nnn100000001nnn',
        'nnn100000001nnn',
        '111100000001111',
        '1c00000000000b1',
        '111100000001111',
        'nnn100000001nnn',
        'nnn100000001nnn',
        'nnn111101111nnn',
        'nnnnnn101nnnnnn',
        'nnnnnn1d1nnnnnn',
        'nnnnnn111nnnnnn'
        ]
    stageABCD=map_token(stageABCD)
    stage124578=[
        'nnnnnn111nnnnnn',
        'nnnnnn1a1nnnnnn',
        'nnnnnn101nnnnnn',
        'nnn111101111nnn',
        'nnn100000001nnn',
        'nnn100000001nnn',
        '111100000001111',
        '1c00000000000b1',
        '111100000001111',
        'nnn100000001nnn',
        'nnn100000001nnn',
        'nnn111101111nnn',
        'nnnnnn101nnnnnn',
        'nnnnnn1d1nnnnnn',
        'nnnnnn111nnnnnn'
        ]
    stage124578=map_token(stage124578)
    stage369=[
        'nnnnnnnnnn1nnnnnnnnnn',
        'nnnnnnnnn1a1nnnnnnnnn',
        'nnnnnnnn10001nnnnnnnn',
        'nnnnnnn1000001nnnnnnn',
        'nnnnnn100000001nnnnnn',
        'nnnnn10000000001nnnnn',
        'nnnn1000000000001nnnn',
        'nnn100000000000001nnn',
        'nn10000000000000001nn',
        'n1000000000000000001n',
        '1c00000000000000000b1',
        'n1000000000000000001n',
        'nn10000000000000001nn',
        'nnn100000000000001nnn',
        'nnnn1000000000001nnnn',
        'nnnnn10000000001nnnnn',
        'nnnnnn100000001nnnnnn',
        'nnnnnnn1000001nnnnnnn',
        'nnnnnnnn10001nnnnnnnn',
        'nnnnnnnnn1d1nnnnnnnnn',
        'nnnnnnnnnn1nnnnnnnnnn'
        ]
    stage369=map_token(stage369)
    stageTemplate=[
        'nnnnnnnnnnnnnnnnnnnn',
        'n111111111111111111n',
        'n111111111111111111n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n111111111111111111n',
        'n111111111111111111n',
        'nnnnnnnnnnnnnnnnnnnn'
        ]
    stageTemplate=map_token(stageTemplate)
    stage_SDS=[
        'nnnnnnnnnnnnnnnn',
        'n11111111111111n',
        'n11111111111111n',
        'n11000000000011n',
        'n11000000000011n',
        'n11000000000011n',
        'n11000000000011n',
        'n11000000000011n',
        'n11000000000011n',
        'n11000000000011n',
        'n11000000000011n',
        'n11000000000011n',
        'n11000000000011n',
        'n11000000000011n',
        'n11000000000011n',
        'n11111dddd11111n',
        'n11111111111111n',
        'nnnnnnnnnnnnnnnn'
        ]
    stage_SDS=map_token(stage_SDS)
    stage_Undernet=[
    ##The Entrance to the UNDERNET: where Z= -1
        'nnnnnnnnnnnnnnnnnnn',
        'nnnnnnn11111nnnnnnn',
        'nnnnnnn11111nnnnnnn',
        'nnnnnnn11u11nnnnnnn',
        'nnn100111011nnnn1nn',
        'nnnn01n11011nnnnnnn',
        'nnnnnn111011nnnnnnn',
        'nnnnn1n11011nn1001n',
        'nnnn1n111011nnn01nn',
        'n1nnnnn11011nnnnnnn',
        'nnnnnnn11011nnnn1nn',
        'nnnnnnn11011nn1nnnn',
        'nnnnnnn11011nnnnn1n',
        'nnnn1nn110111nnnnnn',
        'nnn1n1n11011nn1nnnn',
        'nnnnnnn110111nnnnnn',
        'nnnnnnn11011nnnnnnn',
        'nn1nnnn11011nnnnnnn',
        'n1n1nnn11011nnnnnnn',
        'nnnnnnn11011n1nn1nn',
        'nnnnnn1110111n1nnnn',
        'nnnnn1n11011nnnnnnn',
        'nnnnnn111011nnnnnnn',
        'nnnnnnn11011nnnnnnn',
        'nnnnnnn11d11nnnnnnn',
        'nnnnnnn11111nnn1nnn',
        'nnnnnnnnnnnn1nnnnnn'
        ]
    stage_Undernet=map_token(stage_Undernet)
    stage_Cafella=[
        'nnnnnnnnnnnnnnnnnnnn',
        'n111111111111111111n',
        'n111111111111111111n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n1c00000000000000b1n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n111111111111111111n',
        'n111111111111111111n',
        'nnnnnnnnnnnnnnnnnnnn'
        ]
    stage_Cafella=map_token(stage_Cafella)
    stage_AdaU=[
        'nnnnnnnnnnnnnnnnnnnn',
        'n111111111111111111n',
        'n111111111111111111n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n1c00000000000000b1n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n111111111111111111n',
        'n111111111111111111n',
        'nnnnnnnnnnnnnnnnnnnn'
        ]
    stage_AdaU=map_token(stage_AdaU)
    stage_Bytes=[
        'nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn',
        'n1111111111111111111111111111n',
        'n1111111111111111111111111111n',
        'n1100000000000000000000000011n',
        'n1100000000000000000000000011n',
        'n1100000000000000000000000011n',
        'n1100000000000000000000000011n',
        'n1100000000000000000000000011n',
        'n1100000000000000000000000011n',
        'n1100000000000000000000000011n',
        'n1c00000000000000000000000011n',
        'n1100000000000000000000000011n',
        'n1111111111111111111111111111n',
        'n1111111111111111111111111111n',
        'nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn'
        ]
    stage_Bytes=map_token(stage_Bytes)
    stage_Library=[
        'nnnnnnnnnnnnnnnnnnnn',
        'n111111111111111111n',
        'n111111111111111111n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n111111111d11111111n',
        'n111111111111111111n',
        'nnnnnnnnnnnnnnnnnnnn'
        ]
    stage_Library=map_token(stage_Library)
    stage_Battlewareshop=[
        'nnnnnnnnnnnnnnnnnnnn',
        'n111111111111111111n',
        'n11111111a111111111n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n1c00000000000000b1n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n111111111d11111111n',
        'n111111111111111111n',
        'nnnnnnnnnnnnnnnnnnnn'
        ]
    stage_Battlewareshop=map_token(stage_Battlewareshop)
    stage_Square=[
        'nnnnnnnnnnnnnnnnnnnn',
        'n111111111111111111n',
        'n11111111a111111111n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n1c00000000000000b1n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n110000000000000011n',
        'n111111111d11111111n',
        'n111111111111111111n',
        'nnnnnnnnnnnnnnnnnnnn'
        ]
    stage_Square=map_token(stage_Square)
    # stagek=[
    #     '1111101111111111111111111nnnnn',
    #     '1000001000000000000000001nnnnn',
    #     '1000001000000000000000001nnnnn',
    #     '1c0001000011111110000000111111',
    #     '100000000100000000000000000001',
    #     '111110d01000000000000000000001',
    #     '100001111000010000100000000001',
    #     '100000000000010000111111111111',
    #     '100000000000010000000000000001',
    #     '100000000000010000000000000001',
    #     '100000000000011111111111111111',
    #     '100000000000000000000000000001',
    #     '100000000000000000000001111001',
    #     '10b001111111111111111111000001',
    #     '111110000000000000000001000001',
    #     '100000000000000000000000000001',
    #     '100000000000000000000001000001',
    #     '100000000000000000000001000001',
    #     '111111111111111111111111111111'
    # ]
    # stagek=map_token(stagek)
    # stagek=[
    #     'nnnnnnnnnnn0n0n',
    #     'nnnnnnnnn1000nn',
    #     '111111110n0n0nn',
    #     '10000000n0n0n01',
    #     '10000000010n0n1',
    #     '100000000000001',
    #     '10000000000010n',
    #     '100000000000n1n',
    #     '10000000000001n',
    #     '10000000000001n',
    #     '11111111111111n'
    # ]
    # stagek=map_token(stagek)
    stage_WestGateway=[
        'n1111111111111111n',
        'n111111111111a111n',
        'n1000000000000001n',
        'n1000000000000001n',
        'n1000000000000001n',
        '11000000000000001n',
        '11000000000000001n',
        '1c000000000000001n',
        '11000000000000001n',
        '11000000000000001n',
        '11000000000000001n',
        'n1000000000000001n',
        'n1000000000000001n',
        'n111111111111d111n',
        'n1111111111111111n'
    ]
    stage_WestGateway=map_token(stage_WestGateway)
    stage_ShadyAlley=[
        'n1111111n',
        'n1000001n',
        'n1000001n',
        'n1000001n',
        'n1110001n',
        'nnn10001n',
        'nnn10001n',
        'nnn10001n',
        'nnn1d111n',
        'nnnnnnnnn'
    ]
    stage_ShadyAlley=map_token(stage_ShadyAlley)
    stagebroken=[
        'nnnnnnnnnnn0n0n',
        'nnnnnnn1n1000nn',
        '1111111a0n0n0nn',
        '10000000n0n0n01',
        '10000000010n0n1',
        '100000000000001',
        '1c00000000000bn',
        '100000000000nn1',
        '100000000000001',
        '1000000d0000001',
        '111111111111111'
    ]
    stagebroken=map_token(stagebroken)
    stageAD=[
        'n111111111n',
        'n1111a1111n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n1111d1111n',
        'n111111111n'
    ]
    stageAD=map_token(stageAD)
    stageABD=[
        'n111111111n',
        'n1111a1111n',
        'n100000001n',
        'n100000001n',
        'n1000000011',
        'n10000000b1',
        'n1000000011',
        'n100000001n',
        'n100000001n',
        'n1111d1111n',
        'n111111111n'
    ]
    stageABD=map_token(stageABD)
    stageABC=[
        'n111111111n',
        'n1111a1111n',
        'n100000001n',
        'n100000001n',
        '11000000011',
        '1c0000000b1',
        '11000000011',
        'n100000001n',
        'n100000001n',
        'n111111111n',
        'n111111111n'
    ]
    stageABC=map_token(stageABC)
    stageAB=[
        'n111111111n',
        'n1111a1111n',
        'n100000001n',
        'n100000001n',
        'n1000000011',
        'n10000000b1',
        'n1000000011',
        'n100000001n',
        'n100000001n',
        'n111111111n',
        'n111111111n'
    ]
    stageAB=map_token(stageAB)
    stageAC=[
        'n111111111n',
        'n1111a1111n',
        'n100000001n',
        'n100000001n',
        '1100000001n',
        '1c00000001n',
        '1100000001n',
        'n100000001n',
        'n100000001n',
        'n111111111n',
        'n111111111n'
    ]
    stageAC=map_token(stageAC)
    stageBC=[
        'n111111111n',
        'n111111111n',
        'n100000001n',
        'n100000001n',
        '11000000011',
        '1c0000000b1',
        '11000000011',
        'n100000001n',
        'n100000001n',
        'n111111111n',
        'n111111111n'
    ]
    stageBC=map_token(stageBC)
    stageBD=[
        'n111111111n',
        'n111111111n',
        'n100000001n',
        'n100000001n',
        'n1000000011',
        'n10000000b1',
        'n1000000011',
        'n100000001n',
        'n100000001n',
        'n1111d1111n',
        'n111111111n'
    ]

    stageBD=map_token(stageBD)
    stageCD=[
        'n111111111n',
        'n111111111n',
        'n100000001n',
        'n100000001n',
        '1100000001n',
        '1c00000001n',
        '1100000001n',
        'n100000001n',
        'n100000001n',
        'n1111d1111n',
        'n111111111n'
    ]
    stageCD=map_token(stageCD)
    stageACD=[
        'n111111111n',
        'n1111a1111n',
        'n100000001n',
        'n100000001n',
        '1100000001n',
        '1c00000001n',
        '1100000001n',
        'n100000001n',
        'n100000001n',
        'n1111d1111n',
        'n111111111n'
    ]
    stageACD=map_token(stageACD)
    stageBCD=[
        'n111111111n',
        'n111111111n',
        'n100000001n',
        'n100000001n',
        '11000000011',
        '1c0000000b1',
        '11000000011',
        'n100000001n',
        'n100000001n',
        'n1111d1111n',
        'n111111111n'
    ]
    stageBCD=map_token(stageBCD)
    stageA=[
        'n111111111n',
        'n1111a1111n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n111111111n',
        'n111111111n'
    ]
    stageA=map_token(stageA)
    stageB=[
        'n111111111n',
        'n111111111n',
        'n100000001n',
        'n100000001n',
        'n1000000011',
        'n10000000b1',
        'n1000000011',
        'n100000001n',
        'n100000001n',
        'n111111111n',
        'n111111111n'
    ]
    stageB=map_token(stageB)
    stageC=[
        'n111111111n',
        'n111111111n',
        'n100000001n',
        'n100000001n',
        '1100000001n',
        '1c00000001n',
        '1100000001n',
        'n100000001n',
        'n100000001n',
        'n111111111n',
        'n111111111n'
    ]
    stageC=map_token(stageC)
    stageD=[
        'n111111111n',
        'n111111111n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n1111d1111n',
        'n111111111n'
    ]
    stageD=map_token(stageD)

    #MAP OF CONNECHT

    Connecht_square=[
        'nnnnnn1111111111nnnnnnnn',
        'nnnn1100000000000010000nn',
        'nnn10000000000000000000nn',
        'nn100000000000000000000nn',
        'n100000nnnn000nnnn0000001',
        'n100000nnnn000nnnn000001n',
        'n100000nnnn000nnnn000001n',
        'n100000nnnn000nnnn000001n',
        'n10000000000000000000001n',
        'n10000000000000000000001n',
        'n100000nnnn000nnnn000001n',
        'n100000nnnn000nnnn000001n',
        'n100000nnnn000nnnn000001n',
        'n100000nnnn000nnnn000001n',
        'n100000nnnn000nnnn000001n',
        'nn111100000000011100000nn',
        'n10000000000000000000001n',
        'n10000000000000000000001n',
        'n10000000000000000000001n',
        'n11111111111111111111111n'
    ]
    Connecht_square=map_token(Connecht_square)



    globals()["GRID"] ={
        #x y
        (188,160):stageABC,
        (191,160):stageABC,
        (192,160):stageABC,
        (193,160):stageABC,
        (194,160):stageABC,

        (185,161):stageABC,
        (186,161):stageABC,
        (187,161):stageAC,
        (188,161):stage_SDS,
        (189,161):stageAB,
        (190,161):stageACD,
        (191,161):stageBD,
        (192,161):stageBC,
        (193,161):stageBC,
        (194,161):stageBCD,
        (195,161):stageABCD,

        (184,162):stageACD,
        (185,162):stageD,
        (186,162):stageBD,
        (187,162):stageBCD,
        (188,162):stageABC,
        (189,162):stageCD,
        (190,162):stageA,
        (191,162):stageAD,
        (192,162):stageD,
        (193,162):stageD,
        (194,162):stageAD,
        (195,162):stageAB,

        (184,163):stageACD,
        (185,163):stageABD,
        (186,163):stageAC,
        (187,163):stageAD,
        (188,163):stageB,
        (189,163):stageABC,
        (190,163):stageBC,
        (191,163):stageABCD,
        (192,163):stageABC,
        (193,163):stageACD,
        (194,163):stageABD,
        (195,163):stageC,
        (196,163):stageABD,

        (184,164):stageAC,
        (185,164):stageABD,
        (186,164):stageBC,
        (187,164):stageABCD,
        (188,164):stageBC,
        (189,164):stageBCD,
        (190,164):stageBC,
        (191,164):stageAC,
        (192,164):stage_ShadyAlley,#MELISSA AREA
        (193,164):stageAB,
        (194,164):stageACD,
        (195,164):stageBD,


        (183,165):stageACD,
        (184,165):stageBD,
        (185,165):stageABC,
        (186,165):stageCD,
        (187,165):stageABD,
        (188,165):stageCD,
        (189,165):stageAB,
        (190,165):stageCD,
        (191,165):stageBD,
        (192,165):stageABCD,
        (193,165):stageCD,
        (194,165):stageAD,
        (195,165):stageAB,

        (183,166):stageACD,
        (184,166):stageAD,
        (185,166):stageBD,
        (186,166):stageAC,
        (187,166):stageABD,
        (188,166):stageACD,
        (189,166):stage_Undernet,
        (190,166):stageAD,
        (191,166):stageAD,
        (192,166):stageAD,
        (193,166):stageAD,
        (194,166):stageABD,
        (195,166):stageC,
        (196,166):stageABD,

        (183,167):stageABCD,
        (184,167):stageABCD,
        (185,167):stageABC,
        (186,167):stage_Cafella,
        (187,167):stageACD,
        (188,167):stageAB,
        (189,167):stageAC,
        (190,167):stageABD,
        (191,167):stage_WestGateway,#BITWULF AREA Chapter2
        (192,167):stageAD,
        (193,167):stageABD,
        (194,167):stageACD,
        (195,167):stageBD,

        (183,168):stageACD,
        (184,168):stageABD,
        (185,168):stageBC,
        (186,168):stage_AdaU,
        (187,168):stageABCD,
        (188,168):stageBCD,
        (189,168):stage_Bytes,
        (190,168):stageAD,
        (191,168):stageABD,
        (192,168):stagehome,
        (193,168):stageACD,
        (194,168):stageAD,
        (195,168):stageAB,

        (183,169):stageACD,
        (184,169):stageAB,
        (185,169):stageBC,
        (186,169):stageBCD,
        (187,169):stageABC,
        (188,169):stage_Square,
        (189,169):stageBCD,
        (190,169):stageAC,
        (191,169):stageAB,
        (192,169):stageABC,
        (193,169):stageAC,
        (194,169):stageABD,
        (195,169):stageC,
        (196,169):stageABD,

        (183,170):stageABCD,
        (184,170):stageBCD,
        (185,170):stageCD,
        (186,170):stageAD,
        (187,170):stage_Library,
        (188,170):stageABD,
        (189,170):stage_Battlewareshop,
        (190,170):stageBC,
        (191,170):stageBC,
        (192,170):stageBCD,
        (193,170):stageBC,
        (194,170):stageACD,
        (195,170):stageBD,

        (183,171):stageACD,
        (184,171):stageAD,
        (185,171):stageAD,
        (186,171):stageAD,
        (187,171):stageABD,
        (188,171):stageACD,
        (189,171):stageAB,
        (190,171):stageBCD,
        (191,171):stageBC,
        (192,171):stageABC,
        (193,171):stageCD,
        (194,171):stageAD,
        (195,171):stageAB,

        (183,172):stageACD,
        (184,172):stageABD,
        (185,172):stageAC,
        (186,172):stageAB,
        (187,172):stageABCD,
        (188,172):stageAC,
        (189,172):stageD,
        (190,172):stageAB,
        (191,172):stageC,
        (192,172):stageD,
        (193,172):stageAB,
        (194,172):stageABC,
        (195,172):stageC,
        (196,172):stageABD,

        (183,173):stageACD,
        (184,173):stageAB,
        (185,173):stageCD,
        (186,173):stageBD,
        (187,173):stageAC,
        (188,173):stageBD,

        (190,173):stageBCD,
        (191,173):stageBCD,

        (193,173):stageBCD,
        (194,173):stageBCD,
        (195,173):stageBCD,

        (184,174):stageCD,
        (185,174):stageAB,
        (186,174):stageAC,
        (187,174):stageBD,

        (185,175):stageBCD,
        (186,175):stageBCD,
        }
    mapeventsdict={
        # (192,168):[homeevents],
        (191,167):[Chapter2events]
        }
    mapspritesdict={
        (192,168):[Heartsprite],
        # (192,164):[Avesprite,CodeRedsprite,Virasprite]
        (192,164):[Stellasprite],
        (192,165):[Bellasprite],

        (191,167):[Bitwulf_C2],
        (193,167):[Programkunsprite]
        }
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


    return
