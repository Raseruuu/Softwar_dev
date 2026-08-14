
define bn_tiles=[
    "b","b","b","r","r","r",
    "b","b","b","r","r","r",
    "b","b","b","r","r","r",
]
define bn_tile_objects=[
    ["","","","","",""],
    ["","","","","",""],
    ["","","","","",""],
]

label BN_grid:
    "Start BN Style Battle!"
    $ start_position=(1,1)
    $ start_position2=(4,1)
    $ sprites_in_bnarena=[("megaman",start_position)]
    # python:
    #     for y in bn_tile_objects:
    #         for x in y:
    #             if in sprites_in_bnarena:


    call screen bn_battle(ILY,ILY)

    return
init python:
    def arena_changeposition(playername="megaman"):
        global sprites_in_bnarena
        for sp_index,sp in enumerate(sprites_in_bnarena):
            sprites_in_bnarena[sp_index]
default key_inputs=[]
default movedirection = ""
screen bn_battle(Player_FAI=ILY,Enemy_FAI=Ave):
    
    grid 6 3:
        xalign 0.5 yalign 0.5 
        for bntile in bn_tiles:
            add "gui/bn/tile_[bntile].png" zoom 0.3
    
            # if 
    frame:  
        background Null() 
        xalign 0.5 yalign 0.5    
        for index_bn_y,bn_object_y in enumerate(bn_tile_objects):
            # hbox:
                for index_bn_x,bn_object_x in enumerate(bn_object_y):
                    for bn_object in sprites_in_bnarena:
                        $ spritename=bn_object[0]
                        $ position_in_arena=bn_object[1]
                        if position_in_arena==(index_bn_x,index_bn_y):

                            add "gui/bn/[spritename].png" zoom 4.0 xpos (index_bn_x*160) ypos (index_bn_y*119)
                        else:
                            frame:
                                background Null(width=160,height=119)
                                # width 160
                                # height 119
                                # text str(bn_object_x)+" "+str((index_bn_x,index_bn_y))
                       
                           


            
    key "K_UP" action SetVariable("movedirection","up") 
    key "K_DOWN" action SetVariable("movedirection","down")
    key "K_LEFT" action SetVariable("movedirection","left")
    key "K_RIGHT" action SetVariable("movedirection","right")
