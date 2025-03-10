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
init python:
    def cardnamewidth(fontsize,text,maxwidth,maxchar):
        if len(text)!=0:
            namewidth=fontsize*len(text)
            excess=namewidth-maxwidth
            remmax=namewidth-excess
            rem=remmax/namewidth
            excesspercentage=excess/maxwidth
            if maxwidth!=164:
                print(text)
                print(rem)
            zoompercentage=rem
            return zoompercentage
        else:
            return 1.0
init python:
    
    def FunctionList(FXN):
        fxns=[]
        long_fxn_name=False
        # execution_active= globals()["execution_active"]
        # fxnindex=globals()["fxnindex"]
        for function_index_local,cardfunction in enumerate(FXN):
            # if len(cardfunction.code)>20:
            #     long_fxn_name=True
            if fxnindex==function_index_local and execution_active:
                fxns.append(At(Text("{size=12}{u}{b}"+cardfunction.code+"{/size}{/u}{/b}", layout="nobreak"),widthresize(1.0 if (len(cardfunction.code)<(226/12)) else 0.9 if ("for" in cardfunction.code) else 0.68 if ("while" in cardfunction.code or "if" in cardfunction.code) else (cardnamewidth(12,cardfunction.code,226,16)))))
            else:
                fxns.append(At(Text("{size=12}"+cardfunction.code+"{/size}", layout="nobreak"),widthresize(1.0 if (len(cardfunction.code)<(226/12)) else 0.9 if ("for" in cardfunction.code) else 0.68 if ("while" in cardfunction.code or "if" in cardfunction.code) else (cardnamewidth(12,cardfunction.code,226,16)))))

        return VBox(*fxns)
    def FunctionListDescript(FXN):
        fxns=[]
        # long_fxn_name=False
        for function_index_local, cardfunction in FXN:
            # if len(cardfunction.code)>18:
            #     long_fxn_name=True
            
            fxns.append(Text("{size=12}{b}"+cardfunction.name+"{/b}{/size}\n  {size=12}"+cardfunction.text+"{/size}"))
                

        # if long_fxn_name:
        #     return At(VBox(*fxns))
        # else:
        return VBox(*fxns)
    def CardDisplay(cardobj):
        return LiveComposite(
            (225,300),
            (0,0),"images/Cards/Cardblank.png",
            (11,12),"images/Cards/"+cardobj.NAME+".png",
            (14,231),
                FunctionList(cardobj.FXN),
            (170,169),
                At("images/Cards/cardbit/bit.png",zoomtrans(0.5)),
            (11,204),At(Text( "{color=#FFFF00}{font=font/adventpro-bold.ttf}{size=20}"+cardobj.NAME+"{/color}{/font}{/size}",style="cardshadows", layout="nobreak"),cardnametrans(cardobj.NAME)),
            (168,196),Text("{color=#0751b6}{font=font/consolas.ttf}{b}{size=26}"+str(cardobj.COST)+"{/font}{/b}{/size}{size=13}{b}BIT{/b}{/size}{/color}",style="cardoutlines"),
            (164,231),Text("{color=#ffffff}{font=font/consolas.ttf}{size=10}{b}TYPE{/color}{/font}{/size}{/b}"),
            (164,242),Text("{color=#ffcc00}{font=font/consolas.ttf}{size=10}{k=-1}\""+cardobj.TYPE+"\"{/k}{/color}{/font}{/size}"),
            (164,255),Text("{color=#ffffff}{font=font/consolas.ttf}{size=10}{b}POW{/color}{/font}{/size}{/b}"),
            (165,267),Text("{color=#ae81f2}{size=24}"+str(cardobj.MAG)+"{/color}{/size}"),
            )

transform cardnametrans(text):
    xzoom (1.0 if (len(text)<(164/10))  else (cardnamewidth(10,text,164,16)))
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
        image LiveComposite(
            (225,300),
            (0,0),"images/Cards/Cardblank.png",
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
                        add "images/Cards/cardblank2.png" pos ((indexx*138 )+300,520)
                else:
                    add "images/Cards/cardblank2.png" pos ((indexx*138 )+300,520)
                $indexx+=1
            if playerbattlecode!=[]:
                imagebutton idle "images/Cards/cardreturn.png" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback() hovered Show("card6hover"), Play("sound","sfx/select.wav") unhovered Hide("card6hover") xpos 0.86 xanchor 0.5 yalign 0.95
                key "K_BACKSPACE" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback()
                key "x" action Play("sound","sound/Phase.wav"), Hide("card6hover"), Rollback()

