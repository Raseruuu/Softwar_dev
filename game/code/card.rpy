style cardframe:
    margin (0,0)
transform cardzoom(zoomvalue):
    zoom zoomvalue
transform widthresize(zoomvalue):
    xzoom zoomvalue
style cardoutlines:
    outlines [(2, "#000", -1, 2),(2, "#fff", 0, 0)]
style cardshadows:
    outlines [(1, "#000", -1, 2),(2, "#111", 0, 0)]
style cardshadows2:

    outlines [(1, "#181818", -1, 1),(1, "#141414", 0, 0)]
style marqueeshadows:
    outlines [(5, "#051231", -0, 8),(2, "#07638e", 2, 2)]

init python:
    def cardnamewidth(fontsize,text,maxwidth,maxchar):
        if len(text)!=0:
            namewidth=fontsize*len(text)
            excess=namewidth-maxwidth
            remmax=namewidth-excess
            rem=remmax/namewidth
            excesspercentage=excess/maxwidth
            zoompercentage=rem
            return zoompercentage
        else:
            return 1.0

label cardflash_story(cardobj):
    $ currentcard=(cardobj)
    
    # show white:
    #     alpha 1.0
    #     pause 0.1
    #     linear 0.2 alpha 0.0
    play sound "sfx/sfx-fwasshing.wav"
    
    show cardflasher_temporary onlayer overlay at cardflash_bright("cardflasher_temporary"):
        xalign 0.5 yalign 0.46 
    # show cardflasher onlayer overlay:
    #     zoom 2.0 xalign 0.5 yalign 0.46 alpha 0.6
    #     # matrixcolor BrightnessMatrix(0.7) * OpacityMatrix(0.6)
    #     pause 1.1
    #     zoom 2.7

    #     pause 6.1
    #     ease 1.0 alpha 0.0
    pause 6.0
    hide cardflasher_temporary
    hide whitecard
    return

init python:
    
    def FunctionList(FXN):
        fxns=[]
        long_fxn_name=False
        for function_index_local,cardfunction in enumerate(FXN):
            currentcodetext = cardfunction.code
            if "\n" in currentcodetext:
                
                code_lines = currentcodetext.split('\n')
                for fxncodepart in code_lines:

                    if fxnindex==function_index_local and execution_active:
                        
                        fxns.append(
                            At(
                                Text(
                                    "{size=11}{u}{b}"+fxncodepart+
                                    "{/size}{/u}{/b}", layout="nobreak",style="cardshadows2"),
                                    widthresize(1.0 if (len(fxncodepart)<(48)) else (cardnamewidth(11,fxncodepart,360,48)))))
                    else:
                        fxns.append(
                            At(
                                Text(
                                    "{size=11}"+fxncodepart+
                                    "{/size}", layout="nobreak",style="cardshadows2"),
                                    widthresize(1.0 if (len(fxncodepart)<(48)) else (cardnamewidth(11,fxncodepart,360,48))  )))

            else:
                if fxnindex==function_index_local and execution_active:
                    
                    fxns.append(
                        At(
                            Text(
                                "{size=11}{u}{b}"+cardfunction.code+
                                "{/size}{/u}{/b}", layout="nobreak",style="cardshadows2"),
                                widthresize(1.0 if (len(cardfunction.code)<(48)) else 1.0 if ("for" in cardfunction.code) else 0.9 if ("while" in cardfunction.code or "if" in cardfunction.code) else (cardnamewidth(11,cardfunction.code,360,48)))))
                else:
                    fxns.append(
                        At(
                            Text(
                                "{size=11}"+cardfunction.code+
                                "{/size}", layout="nobreak",style="cardshadows2"),
                                widthresize(1.0 if (len(cardfunction.code)<(48)) else 1.0 if ("for" in cardfunction.code and len(cardfunction.code)<70 ) else 0.9 if ("while" in cardfunction.code or "if" in cardfunction.code) else (cardnamewidth(11,cardfunction.code,360,48)))))

        return VBox(*fxns,spacing=-2)
    def FunctionListNormal(FXN):
        fxns=[]
        long_fxn_name=False
        
        for function_index_local,cardfunction in enumerate(FXN):
            currentcodetext = cardfunction.code
            if "\n" in currentcodetext:
                
                code_lines = currentcodetext.split('\n')
                for fxncodepart in code_lines:

                
                    fxns.append(
                        At(
                            Text(
                                "{size=11}"+fxncodepart+
                                "{/size}", layout="nobreak",style="cardshadows2"),
                                widthresize(1.0 if (len(fxncodepart)<(48)) else (cardnamewidth(11,fxncodepart,360,48))  )))

            else:
                
                fxns.append(
                    At(
                        Text(
                            "{size=11}"+cardfunction.code+
                            "{/size}", layout="nobreak",style="cardshadows2"),
                            widthresize(1.0 if (len(cardfunction.code)<(48)) else 1.0 if ("for" in cardfunction.code and len(cardfunction.code)<70 ) else 0.9 if ("while" in cardfunction.code or "if" in cardfunction.code) else (cardnamewidth(11,cardfunction.code,284,48)))))

        return VBox(*fxns,spacing=-2)
    def FunctionListDescript(FXN):
        fxns=[]
        
        for function_index_local, cardfunction in enumerate(FXN):
            fxns.append(Text("{size=12}{b}{u}"+cardfunction.name+"{/b}{/u}{/size}\n {size=11}"+cardfunction.text+"{/size}"))
                
        return VBox(*fxns,spacing=4)
    def CardDisplayNew(cardobj):
        return Composite(
            (225,325),
            (0,0),"images/Cards/CARDblank.png",
            
            (9,10),"images/Cards/"+("Plugins" if cardobj.TYPE=="Plugin" else "")+"/"+cardobj.NAME+".png",
            (14,260),
                FunctionList(cardobj.FXN),
            # (170,169),
            (10,196),
                At("images/Cards/cardbit/bit.png",zoomtrans(0.5)),
            # (11,184),At(Text( "{color=#FFFF00}{font=font/adventpro-bold.ttf}{size=20}"+cardobj.NAME+"{/color}{/font}{/size}",cardshadows", layout="nobreak"),cardnametrans(cardobj.NAME)),
            (56,204),At(Text( "{color=#FFFF00}{b}{k=0}{font=font/consolas.ttf}{size=18}"+cardobj.NAME+"{/color}{/b}{/k}{/font}{/size}",style="cardshadows", layout="nobreak"),cardnametrans(cardobj.NAME)),
            # (11,204),At(Text( "{color=#FFFF00}{font=font/adventpro-bold.ttf}{size=20}"+cardobj.NAME+"{/color}{/font}{/size}",style="cardshadows", layout="nobreak"),cardnametrans(cardobj.NAME)),
            (60,224),Text( "{size=14}{b}TYPE: {/size}{color=#ffcc00}{font=font/consolas.ttf}{size=14}{k=-1}\""+cardobj.TYPE+"\"{/k}{/color}{/font}{/size}{/b}",style="cardshadows", layout="nobreak"),
            (60,238),Text( "{size=14}{b}POWR: {/size}{color=#ae81f2}{font=font/consolas.ttf}{size=14}{k=-1}"+str(cardobj.MAG)+"{/k}{/color}{/font}{/size}{/b}",style="cardshadows", layout="nobreak"),
            # (168,196),Text("{color=#0751b6}{font=font/consolas.ttf}{b}{size=26}"+str(cardobj.COST)+"{/font}{/b}{/size}{size=13}{b}BIT{/b}{/size}{/color}",style="cardoutlines"),
            (14,228),Text("{color=#0751b6}{font=font/consolas.ttf}{b}{size=26}"+str(cardobj.COST)+"{/font}{/b}{/size}{size=13}{b}BIT{/b}{/size}{/color}",style="cardoutlines"),
            # (164,231),Text("{color=#ffffff}{font=font/consolas.ttf}{size=10}{b}TYPE{/color}{/font}{/size}{/b}"),
            # (164,242),Text("{color=#ffcc00}{font=font/consolas.ttf}{size=10}{k=-1}\""+cardobj.TYPE+"\"{/k}{/color}{/font}{/size}"),
            # (164,255),Text("{color=#ffffff}{font=font/consolas.ttf}{size=10}{b}POW{/color}{/font}{/size}{/b}"),
            # (165,267),Text("{color=#ae81f2}{size=24}"+str(cardobj.MAG)+"{/color}{/size}"),
            )
    # def CardDisplayDimmed(cardobj):
    #     return Composite(
    #         (225,325),
    #         (0,0),"images/Cards/CARDblank.png",
            
    #         (9,10),"images/Cards/"+("plugins" if cardobj.TYPE=="Plugin" else "")+"/"+cardobj.NAME+".png",
    #         (14,260),
    #             FunctionList(cardobj.FXN),
    #         # (170,169),
    #         (10,196),
    #             At("images/Cards/cardbit/bit.png",zoomtrans(0.5)),
    #         # (11,184),At(Text( "{color=#FFFF00}{font=font/adventpro-bold.ttf}{size=20}"+cardobj.NAME+"{/color}{/font}{/size}",style="cardshadows", layout="nobreak"),cardnametrans(cardobj.NAME)),
    #         (56,204),At(Text( "{color=#FFFF00}{b}{k=0}{font=font/consolas.ttf}{size=18}"+cardobj.NAME+"{/color}{/b}{/k}{/font}{/size}",style="cardshadows", layout="nobreak"),cardnametrans(cardobj.NAME)),
    #         # (11,204),At(Text( "{color=#FFFF00}{font=font/adventpro-bold.ttf}{size=20}"+cardobj.NAME+"{/color}{/font}{/size}",style="cardshadows", layout="nobreak"),cardnametrans(cardobj.NAME)),
    #         (60,224),Text( "{size=14}{b}TYPE: {/size}{color=#ffcc00}{font=font/consolas.ttf}{size=14}{k=-1}\""+cardobj.TYPE+"\"{/k}{/color}{/font}{/size}{/b}",style="cardshadows", layout="nobreak"),
    #         (60,238),Text( "{size=14}{b}POWR: {/size}{color=#ae81f2}{font=font/consolas.ttf}{size=14}{k=-1}"+str(cardobj.MAG)+"{/k}{/color}{/font}{/size}{/b}",style="cardshadows", layout="nobreak"),
    #         # (168,196),Text("{color=#0751b6}{font=font/consolas.ttf}{b}{size=26}"+str(cardobj.COST)+"{/font}{/b}{/size}{size=13}{b}BIT{/b}{/size}{/color}",style="cardoutlines"),
    #         (14,228),Text("{color=#0751b6}{font=font/consolas.ttf}{b}{size=26}"+str(cardobj.COST)+"{/font}{/b}{/size}{size=13}{b}BIT{/b}{/size}{/color}",style="cardoutlines"),
    #         (0,0),At(Solid("#090c18"),alpha08)
    #         # (164,231),Text("{color=#ffffff}{font=font/consolas.ttf}{size=10}{b}TYPE{/color}{/font}{/size}{/b}"),
    #         # (164,242),Text("{color=#ffcc00}{font=font/consolas.ttf}{size=10}{k=-1}\""+cardobj.TYPE+"\"{/k}{/color}{/font}{/size}"),
    #         # (164,255),Text("{color=#ffffff}{font=font/consolas.ttf}{size=10}{b}POW{/color}{/font}{/size}{/b}"),
    #         # (165,267),Text("{color=#ae81f2}{size=24}"+str(cardobj.MAG)+"{/color}{/size}"),
    #         )
            
    def CardDisplayNormal(cardobj):
        return Composite(
            (225,325),
            (0,0),"images/Cards/CARDblank.png",
            
            (9,10),"images/Cards/"+("Plugins" if cardobj.TYPE=="Plugin" else "")+"/"+cardobj.NAME+".png",
            (14,258),
                FunctionListNormal(cardobj.FXN),
            # (170,169),
            (10,196),
                At("images/Cards/cardbit/bit.png",zoomtrans(0.5)),
            # (11,184),At(Text( "{color=#FFFF00}{font=font/adventpro-bold.ttf}{size=20}"+cardobj.NAME+"{/color}{/font}{/size}",cardshadows", layout="nobreak"),cardnametrans(cardobj.NAME)),
            (56,204),At(Text( "{color=#FFFF00}{b}{k=0}{font=font/consolas.ttf}{size=18}"+cardobj.NAME+"{/color}{/b}{/k}{/font}{/size}",style="cardshadows", layout="nobreak"),cardnametrans(cardobj.NAME)),
            # (11,204),At(Text( "{color=#FFFF00}{font=font/adventpro-bold.ttf}{size=20}"+cardobj.NAME+"{/color}{/font}{/size}",style="cardshadows", layout="nobreak"),cardnametrans(cardobj.NAME)),
            (60,224),Text( "{size=14}{b}TYPE: {/size}{color=#ffcc00}{font=font/consolas.ttf}{size=14}{k=-1}\""+cardobj.TYPE+"\"{/k}{/color}{/font}{/size}{/b}",style="cardshadows", layout="nobreak"),
            (60,238),Text( "{size=14}{b}POWR: {/size}{color=#ae81f2}{font=font/consolas.ttf}{size=14}{k=-1}"+str(cardobj.MAG)+"{/k}{/color}{/font}{/size}{/b}",style="cardshadows", layout="nobreak"),
            # (168,196),Text("{color=#0751b6}{font=font/consolas.ttf}{b}{size=26}"+str(cardobj.COST)+"{/font}{/b}{/size}{size=13}{b}BIT{/b}{/size}{/color}",style="cardoutlines"),
            (14,228),Text("{color=#0751b6}{font=font/consolas.ttf}{b}{size=26}"+str(cardobj.COST)+"{/font}{/b}{/size}{size=13}{b}BIT{/b}{/size}{/color}",style="cardoutlines"),
            # (164,231),Text("{color=#ffffff}{font=font/consolas.ttf}{size=10}{b}TYPE{/color}{/font}{/size}{/b}"),
            # (164,242),Text("{color=#ffcc00}{font=font/consolas.ttf}{size=10}{k=-1}\""+cardobj.TYPE+"\"{/k}{/color}{/font}{/size}"),
            # (164,255),Text("{color=#ffffff}{font=font/consolas.ttf}{size=10}{b}POW{/color}{/font}{/size}{/b}"),
            # (165,267),Text("{color=#ae81f2}{size=24}"+str(cardobj.MAG)+"{/color}{/size}"),
            )
transform cardnametrans(text):
    xzoom (1.0 if (len(text)<(150/10))  else (cardnamewidth(10,text,150,16)))
screen Card(cardobj,position=(0.5,0.5),zoomvalue=1.0):
    zorder 50
    frame:
        xsize 225
        ysize 300
        pos (position)
        # anchor (anchor)
        at cardzoom(zoomvalue)
        if not noscreentransformsfornow:
            at pausetrans2

        style "cardframe"
        image Composite(
            (225,300),
            (0,0),"images/Cards/CARDblank.png",
            (10,10),"images/Cards/"+cardobj.NAME+".png",
            # (160,169),"images/Cards/cardbit/"+str(cardobj.COST)+".png"
            (170,169),At("images/Cards/cardbit/bit.png",zoomtrans(0.5))
            )
        vbox:
            pos (14,231)
            add FunctionList(cardobj.FXN)
        text "{color=#FFFF00}{font=font/adventpro-bold.ttf}{size=20}"+cardobj.NAME+"{/color}{/font}{/size}" style "cardshadows":
            pos (11,204)
            
        text "{color=#0751b6}{font=font/consolas.ttf}{b}{size=26}"+str(cardobj.COST)+"{/font}{/b}{/size}{size=13}{b}BIT{/b}{/size}{/color}" style "cardoutlines" :
            pos (168,196)
        text "{color=#ffffff}{font=font/consolas.ttf}{size=10}{b}TYPE{/color}{/font}{/size}{/b}":
            pos (164,231)
        text "{color=#ffcc00}{font=font/consolas.ttf}{size=10}\""+cardobj.TYPE+"\"{/color}{/font}{/size}":
            pos (164,242)
        text "{color=#ffffff}{font=font/consolas.ttf}{size=10}{b}POW{/color}{/font}{/size}{/b}":
            pos (164,255)
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
                        add "images/Cards/CARDblank2.png" pos ((indexx*138 )+300,520)
                else:
                    add "images/Cards/CARDblank2.png" pos ((indexx*138 )+300,520)
                $indexx+=1
            if playerbattlecode!=[]:
                imagebutton idle "images/Cards/cardreturn.png" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback() hovered Show("card6hover"), Play("sound","sfx/select.wav") unhovered Hide("card6hover") xpos 0.86 xanchor 0.5 yalign 0.95
                key "K_BACKSPACE" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback()
                key "x" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback()

