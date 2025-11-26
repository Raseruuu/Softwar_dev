init python:
    chapternum = 0
label game_loop:
    $ chapternum+=1
    # call showphasemsg("Chapter "+str(chapternum))

    #Chapter Novel_Mode
    if not game_over:
        if chapternum>=3:
            scene black
            "Demo Over."
            "Thank  You for playing SOFTWAR!"
            $ game_over=True
        else:
            $ renpy.call("script"+str(chapternum))
            
    # if chapternum==2:
    #     return
    if not playerHP<=0:
        if not game_over:
            jump game_loop
    if not game_over:
        call credits
    return
