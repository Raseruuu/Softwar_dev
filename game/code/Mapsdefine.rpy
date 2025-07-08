init -3 python:
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
    stage0 = [
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
        'n1c00000000000000b1n',
        'n110000000000000011n',
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
        'nnnnnnnnnnnnnnnnnn',
        'n111111111111a111n',
        'n1000000000000001n',
        'n1000000000000001n',
        'n1000000000000001n',
        'nc000000000000001n',
        'nc000000000000001n',
        'nc000000000000001n',
        'nc000000000000001n',
        'nc000000000000001n',
        'n1000000000000001n',
        'n1000000000000001n',
        'n1000000000000001n',
        'n111111111111d111n',
        'nnnnnnnnnnnnnnnnnn'
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
        
        'nnnnnnnnnnn',
        'n1111a1111n',
        'n100rrr001n',
        'n100rrr001n',
        'n100rrr001n',
        'n100rrr001n',
        'n100rrr001n',
        'n100rrr001n',
        'n100rrr001n',
        'n1111d1111n',
        'nnnnnnnnnnn'
    ]
    stageAD=map_token(stageAD)
    stageABD=[
        
        'nnnnnnnnnnn',
        'n1111a1111n',
        'n100rrr001n',
        'n100rrr001n',
        'n100rrrrr1n',
        'n100rrrrrbn',
        'n100rrrrr1n',
        'n100rrr001n',
        'n100rrr001n',
        'n1111d1111n',
        'nnnnnnnnnnn'
    ]
    stageABD=map_token(stageABD)
    stageABC=[
        'nnnnnnnnnnn',
        'n1111a1111n',
        'n100rrr001n',
        'n100rrr001n',
        'n1rrrrrrr1n',
        'ncrrrrrrrbn',
        'n1rrrrrrr1n',
        'n100000001n',
        'n100000001n',
        'n111111111n',
        'nnnnnnnnnnn'
    ]
    stageABC=map_token(stageABC)
    stageAB=[
        'nnnnnnnnnnn',
        'n1111a1111n',
        'n100rrr001n',
        'n100rrr001n',
        'n100rrrrr1n',
        'n100rrrrrbn',
        'n100rrrrr1n',
        'n100000001n',
        'n100000001n',
        'n111111111n',
        'nnnnnnnnnnn'
    ]
    stageAB=map_token(stageAB)
    stageAC=[
        'nnnnnnnnnnn',
        'n1111a1111n',
        'n100rrr001n',
        'n100rrr001n',
        'n1rrrrr001n',
        'ncrrrrr001n',
        'n1rrrrr001n',
        'n100000001n',
        'n100000001n',
        'n111111111n',
        'nnnnnnnnnnn'
    ]
    stageAC=map_token(stageAC)
    stageBC=[
        'nnnnnnnnnnn',
        'n111111111n',
        'n100000001n',
        'n100000001n',
        'n1rrrrrrr1n',
        'ncrrrrrrrbn',
        'n1rrrrrrr1n',
        'n100000001n',
        'n100000001n',
        'n111111111n',
        'nnnnnnnnnnn'
    ]
    stageBC=map_token(stageBC)
    stageBD=[
        'nnnnnnnnnnn',
        'n111111111n',
        'n100000001n',
        'n100000001n',
        'n100rrrrr1n',
        'n100rrrrrbn',
        'n100rrrrr1n',
        'n100rrr001n',
        'n100rrr001n',
        'n1111d1111n',
        'nnnnnnnnnnn'
    ]

    stageBD=map_token(stageBD)
    stageCD=[
        'nnnnnnnnnnn',
        'n111111111n',
        'n100000001n',
        'n100000001n',
        'n1rrrrr001n',
        'ncrrrrr001n',
        'n1rrrrr001n',
        'n100rrr001n',
        'n100rrr001n',
        'n1111d1111n',
        'nnnnnnnnnnn'
    ]
    stageCD=map_token(stageCD)
    stageACD=[
        'nnnnnnnnnnn',
        'n1111a1111n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'nc00000001n',
        'n100000001n',
        'n100000001n',
        'n100000001n',
        'n1111d1111n',
        'nnnnnnnnnnn'
    ]
    stageACD=map_token(stageACD)
    stageBCD=[
        'nnnnnnnnnnn',
        'n111111111n',
        'n100000001n',
        'n100000001n',
        'n1rrrrrrr1n',
        'ncrrrrrrrbn',
        'n1rrrrrrr1n',
        'n100rrr001n',
        'n100rrr001n',
        'n1111d1111n',
        'nnnnnnnnnnn'
    ]
    stageBCD=map_token(stageBCD)
    stageBCD2=[
        'nnnnnnnnnnn',
        'n1111111a1n',
        'n100000001n',
        'n100000001n',
        'n1rrrrrrr1n',
        'ncrrrrrrrbn',
        'n100rrr001n',
        'n100rrr001n',
        'n100rrr001n',
        'n1111d1111n',
        'nnnnnnnnnnn'
    ]
    stageBCD2=map_token(stageBCD2)
    stageA=[
        'n111111111n',
        'n1111a1111n',
        'n100rrr001n',
        'n100rrr001n',
        'n100rrr001n',
        'n100rrr001n',
        'n100rrr001n',
        'n100000001n',
        'n100000001n',
        'n111111111n',
        'nnnnnnnnnnn'
    ]
    stageA=map_token(stageA)
    stageB=[
        'nnnnnnnnnnn',
        'n111111111n',
        'n100000001n',
        'n100000001n',
        'n100rrrrr1n',
        'n100rrrrrbn',
        'n100rrrrr1n',
        'n100000001n',
        'n100000001n',
        'n111111111n',
        'nnnnnnnnnnn'
    ]
    stageB=map_token(stageB)
    stageC=[
        'n111111111n',
        'n111111111n',
        'n100000001n',
        'n100000001n',
        '11rrrrr001n',
        '1crrrrr001n',
        '11rrrrr001n',
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
        'n100rrr001n',
        'n100rrr001n',
        'n100rrr001n',
        'n100rrr001n',
        'n100rrr001n',
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
        'nn000000000000000000000nn',
        'n10000000000000000000001n',
        'n10000000000000000000001n',
        'n10000000000000000000001n',
        'n11111111111111111111111n'
    ]
    Connecht_square=map_token(Connecht_square)

    #MAP OF CONNECHT

    Connecht_square=[
        'nnnnnn1111111111nnnnnnnn',
        'nn000000000000000000000nn',
        'nn000000000000000000000nn',
        'nn000000000000000000000nn',
        'n100000000000000000000001',
        'n10000000000000000000001n',
        'n10000000000000000000001n',
        'n10000000000000000000001n',
        'n10000000000000000000001n',
        'n10000000000000000000001n',
        'n10000000000000000000001n',
        'n10000000000000000000001n',
        'n10000000000000000000001n',
        'nnwwwwwwwwwwwwwwwwwwwwwnn',
        'nnwwwwwwwwwwwwwwwwwwwwwnn',
        'nnwwwwwwwwwwwwwwwwwwwwwnn',
        'nnwwwwwwwwwwwwwwwwwwwwwnn',
        'nnwwwwwwwwwwwwwwwwwwwwwnn',
        'nnwwwwwwwwwwwwwwwwwwwwwnn',
        'nnwwwwwwwwwwwwwwwwwwwwwnn'
    ]
    Connecht_square=map_token(Connecht_square)
