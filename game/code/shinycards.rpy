# Shiny Cards 0.2 by Maurimo
# Place this .rpy file anywhere in your project, to get access to the respective functions.

#region FUNCTIONS
init python:
    def rotating_object(trans, st, at):
        x, y = renpy.display.draw.get_mouse_pos()
        trans.matrixtransform = RotateMatrix((y - config.screen_height / 2) * -.02, (x - config.screen_width / 2) * .02, 0)
        return 0 

    def shift_hue(trans, st, at):
        x, y = renpy.display.draw.get_mouse_pos()
        trans.matrixcolor = HueMatrix(((y - config.screen_height / 2) * -.2 + (x - config.screen_width / 2) * .2) / 2) * ContrastMatrix(1.5)
        return 0

    def shift_diagonally(trans, st, at):
        x, y = renpy.display.draw.get_mouse_pos()
        val = (x - config.screen_width / 2) * .5 + (y - config.screen_height / 2) * .5
        val = val / 2
        trans.matrixtransform = OffsetMatrix(val - 100, val - 100, 0)
        return 0
    def shift_diagonally2(trans, st, at):
        x, y = (0,0)
        val = (x - config.screen_width / 2) * .5 + (y - config.screen_height / 2) * .5
        val = val / 2
        trans.matrixtransform = OffsetMatrix(val - 100, val - 100, 0)
        return 0
    
#endregion

#region TRANSFORMS
transform card_gradient_rep:
    alignaround (.5, .5)
    mesh True
    rotate -45
    xpos 0.0
    ypos 0.0
    alpha 0.5
    subpixel True
    function shift_diagonally
transform card_gradient_t:
    # alignaround (.5, .5)
    # mesh True
    align(0.5, 0.5)
    rotate -45
    alpha 0.4
    # subpixel True
    
    
    ypos 0.0 xpos 0.0 xanchor 1.0 
    matrixtransform OffsetMatrix(-800, -800,0)
    pause 2.0
    linear 0.3 matrixtransform OffsetMatrix(0, 0,0)
    alpha 0.6
    
    repeat
transform card_highlights_t:
    function shift_hue

transform rotate_object_t:
    perspective True
    subpixel True
    function rotating_object
#endregion

#region IMAGES
# card_base should be your card
image card_base = "images/card_2.png"
# card_gradient is the overlaid shiny gradient, I provided a base, but you can edit it to make your own.
image card_gradient = "images/Cards/card_gradient.webp"
# card_highlights is the shiny/holographic parts of your card
image card_highlights = "images/card_highlights.png"

# Here's where the magic happens! All those layers will be composited into one, into card_composite.
# The size is 325, 531, which is the size of the card_base.png I made. You can change this, but just make sure that it's the size of your card's base image.
image card_composite = Composite((325, 531),
    (0,0), "card_base",
    (0,0), At("card_highlights", card_highlights_t),
    (0,0), AlphaMask(At("card_gradient", card_gradient_t), "card_base"))
#endregion
init python:
    def CardDisplay(cardobj):
        return At(Composite(
            (225,325),
            (0,0),At("images/Cards/Cardblank.png"),
            
            
            # (170,169),
            # (11,184),At(Text( "{color=#FFFF00}{font=font/adventpro-bold.ttf}{size=20}"+cardobj.NAME+"{/color}{/font}{/size}",style="cardshadows", layout="nobreak"),cardnametrans(cardobj.NAME)),
            # (11,204),At(Text( "{color=#FFFF00}{font=font/adventpro-bold.ttf}{size=20}"+cardobj.NAME+"{/color}{/font}{/size}",style="cardshadows", layout="nobreak"),cardnametrans(cardobj.NAME)),
            
            (9,10),"images/Cards/"+("plugins" if cardobj.TYPE=="Plugin" else "")+"/"+cardobj.NAME+".png",
            (0,0), AlphaMask(At("card_gradient",card_gradient_t),"images/Cards/Cardblank.png"),
            
            (14,258),
                FunctionList(cardobj.FXN),
            (10,196),
                At("images/Cards/cardbit/bit.png",zoomtrans(0.5),card_highlights_t),
            (56,204),At(Text( "{color=#FFFF00}{b}{k=0}{font=font/consolas.ttf}{size=18}"+cardobj.NAME+"{/color}{/b}{/k}{/font}{/size}",style="cardshadows", layout="nobreak"),cardnametrans(cardobj.NAME),card_highlights_t),
            (60,224),At(Text( "{size=14}{b}TYPE: {/size}{color=#ffcc00}{font=font/consolas.ttf}{size=14}{k=-1}\""+cardobj.TYPE+"\"{/k}{/color}{/font}{/size}{/b}",style="cardshadows", layout="nobreak"),card_highlights_t),
            (60,238),At(Text( "{size=14}{b}POWR: {/size}{color=#ae81f2}{font=font/consolas.ttf}{size=14}{k=-1}"+str(cardobj.MAG)+"{/k}{/color}{/font}{/size}{/b}",style="cardshadows", layout="nobreak"),card_highlights_t),
            (14,228),At(Text("{color=#0751b6}{font=font/consolas.ttf}{b}{size=26}"+str(cardobj.COST)+"{/font}{/b}{/size}{size=13}{b}BIT{/b}{/size}{/color}",style="cardoutlines"),card_highlights_t),
            ),rotate_object_t)
    def CardDisplayDimmed(cardobj):
        return At(Composite(
            (225,325),
            (0,0),At("images/Cards/Cardblank.png"),
            
            
            # (170,169),
            # (11,184),At(Text( "{color=#FFFF00}{font=font/adventpro-bold.ttf}{size=20}"+cardobj.NAME+"{/color}{/font}{/size}",style="cardshadows", layout="nobreak"),cardnametrans(cardobj.NAME)),
            # (11,204),At(Text( "{color=#FFFF00}{font=font/adventpro-bold.ttf}{size=20}"+cardobj.NAME+"{/color}{/font}{/size}",style="cardshadows", layout="nobreak"),cardnametrans(cardobj.NAME)),
            
            (9,10),"images/Cards/"+("plugins" if cardobj.TYPE=="Plugin" else "")+"/"+cardobj.NAME+".png",
            (0,0), AlphaMask(At("card_gradient",card_gradient_t),"images/Cards/Cardblank.png"),
            
            (14,258),
                FunctionList(cardobj.FXN),
            (10,196),
                At("images/Cards/cardbit/bit.png",zoomtrans(0.5),card_highlights_t),
            (56,204),At(Text( "{color=#FFFF00}{b}{k=0}{font=font/consolas.ttf}{size=18}"+cardobj.NAME+"{/color}{/b}{/k}{/font}{/size}",style="cardshadows", layout="nobreak"),cardnametrans(cardobj.NAME),card_highlights_t),
            (60,224),At(Text( "{size=14}{b}TYPE: {/size}{color=#ffcc00}{font=font/consolas.ttf}{size=14}{k=-1}\""+cardobj.TYPE+"\"{/k}{/color}{/font}{/size}{/b}",style="cardshadows", layout="nobreak"),card_highlights_t),
            (60,238),At(Text( "{size=14}{b}POWR: {/size}{color=#ae81f2}{font=font/consolas.ttf}{size=14}{k=-1}"+str(cardobj.MAG)+"{/k}{/color}{/font}{/size}{/b}",style="cardshadows", layout="nobreak"),card_highlights_t),
            (14,228),At(Text("{color=#0751b6}{font=font/consolas.ttf}{b}{size=26}"+str(cardobj.COST)+"{/font}{/b}{/size}{size=13}{b}BIT{/b}{/size}{/color}",style="cardoutlines"),card_highlights_t),
            (0,0),At(Solid("#090c18"),alpha08)
            ),rotate_object_t)
            
            



label show_card_test:
    show expression Solid("#4d4a4a")
    show card_composite at rotate_object_t:
        align (0.5, 0.5)
        zoom 1.2
    "And there you go!"
    hide card_composite
    return


