style cardframe:
    margin (0,0)
transform cardzoom(zoomvalue):
    zoom zoomvalue
transform widthresize(zoomvalue):
    xzoom zoomvalue
screen Card(cardobj,position,zoomvalue):
    frame:
        pos (position)
        at cardzoom(zoomvalue)
        if not noscreentransformsfornow:
            at pausetrans2

        style "cardframe"
        image LiveComposite(
            (225,300),
            (0,0),"images/Cards/Cardblank.png",
            (10,10),"images/Cards/"+cardobj.NAME+".png",
            (160,172),"images/Cards/cardbit/"+str(cardobj.COST)+".png"
            )
        vbox:
            pos (13,240)
            add FunctionList(cardobj.FXN)
        text "{color=#FFFF00}{font=font/adventpro-bold.ttf}{size=20}"+cardobj.NAME+"{/color}{/font}{/size}":
            pos (11,214)
        text "{color=#ffcc00}{font=font/adventpro-bold.ttf}{size=12}"+cardobj.TYPE+"{/color}{/font}{/size}":
            pos (165,237)
        text "{color=#ae81f2}{size=24}"+str(cardobj.MAG)+"{/color}{/size}":
            pos (165,267)

screen choosecardv3(handcards):
    $indexx=0
    frame:
        style "cardframe"
        xalign 0.5
        frame:
            style "cardframe"
            for cardobj in handcards:
                if (handcards[indexx].COST<=playerbits):
                    if (not clickedcard[indexx]):
                        use Card(cardobj,((indexx*138 )+300,520),Return("card"+str(indexx+1)),0.6)
                    else:
                        add "images/Cards/cardblank2.png" pos ((indexx*138 )+300,520)
                else:
                    add "images/Cards/cardblank2.png" pos ((indexx*138 )+300,520)
                $indexx+=1
            if playerbattlecode!=[]:
                imagebutton idle "images/Cards/cardreturn.png" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback() hovered Show("card6hover"), Play("sound","sfx/select.wav") unhovered Hide("card6hover") xpos 0.86 xanchor 0.5 yalign 0.95
                key "K_BACKSPACE" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback()
                key "x" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback()


# screen Card(cardobj,position,cardAction):
#     frame:
#         style "cardframe"
#         imagebutton idle LiveComposite(
#             (225,300),
#             (0,0),"images/Cards/Cardblank.png",
#             (10,10),"images/Cards/"+cardobj.NAME+".png"
#             ):
#                 pos (position)
#                 action cardAction
#         textbutton "{color=#FFFF00}{font=font/adventpro-bold.ttf}{size=20}[cardobj.NAME]{/color}{/font}{/size}":
#             pos (position[0]+11,position[1]+208)
#         vbox:
#             pos (position[0]+16,position[1]+244)
#             for fxn in cardobj.FXN:
#                 text "{size=12}[fxn.name]{/size}"
#         imagebutton idle "images/Cards/cardbit/"+str(cardobj.COST)+".png":
#             action cardAction
#             pos (position[0]+162,position[1]+170)
#         textbutton "{color=#ffcc00}{font=font/adventpro-bold.ttf}{size=12}[cardobj.TYPE]{/color}{/font}{/size}":
#             pos (position[0]+152,position[1]+225)
#         textbutton "{color=#ae81f2}{size=24}[cardobj.MAG]{/color}{/size}":
#             pos (position[0]+165,position[1]+261)


        # use Card(handcards[1],(10+(1*225),400),Return())
        # use Card(handcards[2],(10+(2*225),400),Return())
        # use Card(handcards[3],(10+(3*225),400),Return())
        # use Card(handcards[4],(10+(4*225),400),Return())
            # button action cardAction:
            #     style "cardframe"
            #     pos (20,400)
            #     image Composite(
            #         (225,300),
            #         (0,0),"images/Cards/Cardblank.png",
            #         (10,10),"images/Cards/"+cardobj[0].NAME+".png",
            #         (160,172),"images/Cards/cardbit/"+str(cardobj[0].COST)+".png"
            #
            #         )
            #
            # button action cardAction:
            #     style "cardframe"
            #     pos (250,400)
            #     image Composite(
            #         (225,300),
            #         (0,0),"images/Cards/Cardblank.png",
            #         (10,10),"images/Cards/"+cardobj[1].NAME+".png",
            #         (160,172),"images/Cards/cardbit/"+str(cardobj[1].COST)+".png"
            #
            #         )
            #     vbox:
            #         pos (16,244)
            #         for fxn in cardobj[1].FXN:
            #             text "{size=12}[fxn.name]{/size}"
            #     text "{color=#FFFF00}{font=font/adventpro-bold.ttf}{size=20}"+cardobj[1].NAME+"{/color}{/font}{/size}":
            #         pos (11,214)
            #     text "{color=#ffcc00}{font=font/adventpro-bold.ttf}{size=12}"+cardobj[1].TYPE+"{/color}{/font}{/size}":
            #         pos (155,237)
            #     text "{color=#ae81f2}{size=24}"+str(cardobj[1].MAG)+"{/color}{/size}":
            #         pos (165,267)
            # button action cardAction:
            #     style "cardframe"
            #     pos (480,400)
            #     image Composite(
            #         (225,300),
            #         (0,0),"images/Cards/Cardblank.png",
            #         (10,10),"images/Cards/"+cardobj[2].NAME+".png",
            #         (160,172),"images/Cards/cardbit/"+str(cardobj[2].COST)+".png"
            #
            #         )
            #     vbox:
            #         pos (16,244)
            #         for fxn in cardobj[2].FXN:
            #             text "{size=12}[fxn.name]{/size}"
            #     text "{color=#FFFF00}{font=font/adventpro-bold.ttf}{size=20}"+cardobj[2].NAME+"{/color}{/font}{/size}":
            #         pos (11,214)
            #     text "{color=#ffcc00}{font=font/adventpro-bold.ttf}{size=12}"+cardobj[2].TYPE+"/color}{/font}{/size}":
            #         pos (155,237)
            #     text "{color=#ae81f2}{size=24}"+str(cardobj[2].MAG)+"{/color}{/size}":
            #         pos (165,267)
            # button action cardAction:
            #     style "cardframe"
            #     pos (610,400)
            #     image Composite(
            #         (225,300),
            #         (0,0),"images/Cards/Cardblank.png",
            #         (10,10),"images/Cards/"+cardobj[3].NAME+".png",
            #         (160,172),"images/Cards/cardbit/"+str(cardobj[3].COST)+".png"
            #
            #         )
            #     vbox:
            #         pos (16,244)
            #         for fxn in cardobj[3].FXN:
            #             text "{size=12}[fxn.name]{/size}"
            #     text "{color=#FFFF00}{font=font/adventpro-bold.ttf}{size=20}"+cardobj[3].NAME+"{/color}{/font}{/size}":
            #         pos (11,214)
            #     text "{color=#ffcc00}{font=font/adventpro-bold.ttf}{size=12}"+cardobj[3].TYPE+"{/color}{/font}{/size}":
            #         pos (155,237)
            #     text "{color=#ae81f2}{size=24}"+str(cardobj[3].MAG)+"{/color}{/size}":
            #         pos (165,267)
            # button action cardAction:
            #     style "cardframe"
            #     pos (840,400)
            #     image Composite(
            #         (225,300),
            #         (0,0),"images/Cards/Cardblank.png",
            #         (10,10),"images/Cards/"+cardobj[4].NAME+".png",
            #         (160,172),"images/Cards/cardbit/"+str(cardobj[4].COST)+".png"
            #
            #         )
            #     vbox:
            #         pos (16,244)
            #         for fxn in cardobj[4].FXN:
            #             text "{size=12}[fxn.name]{/size}"
            #     text "{color=#FFFF00}{font=font/adventpro-bold.ttf}{size=20}"+cardobj[4].NAME+"{/color}{/font}{/size}":
            #         pos (11,214)
            #     text "{color=#ffcc00}{font=font/adventpro-bold.ttf}{size=12}"+cardobj[4].TYPE+"{/color}{/font}{/size}":
            #         pos (155,237)
            #     text "{color=#ae81f2}{size=24}"+str(cardobj[4].MAG)+"{/color}{/size}":
            #         pos (165,267)
image cardflasher2:
    LiveComposite(
        (225,300),
        (0,0),"images/Cards/Cardblank.png",
        (11,12),"images/Cards/[cardobj.NAME].png",
        (11,214),Text("{color=#FFFF00}{font=font/adventpro-bold.ttf}{size=20}[cardobj.NAME]{/color}{/font}{/size}"),

        (17,240),
            ConditionSwitch(
                "cardobj.FXN[0].name!='N'",
                    (Text("{size=12}[cardobj.FXN[0].name]{/size}")),
                "True",
                    Null()
                    ),
        (17,258),
            ConditionSwitch(
                "cardobj.FXN[1].name!='N'",
                    (Text("{size=12}[cardobj.FXN[1].name]{/size}")),
                "True",


                    Null()
                    ),
        (165,175),"images/Cards/cardbit/[cardobj.COST].png",
        (155,237),Text("{color=#ffcc00}{font=font/adventpro-bold.ttf}{size=12}[cardobj.TYPE]{/color}{/font}{/size}"),
        (165,267),Text("{color=#ae81f2}{size=24}[cardobj.MAG]{/color}{/size}"),
        # (185,273),Text("{color=#ae81f2}{font=font/adventpro-bold.ttf}{size=12}[cardobj.HIT]{/color}{/font}{/size}"),
        )
