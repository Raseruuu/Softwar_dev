 #################
#################
## Flashback
##  Kids Lisa Talks with John: Refer to each respectively: Girl, and Boy.
    # Year 2000, before ILOVEYOU Virus spread
    # Girl and Boy are 7 years old
    # Boy asks girl about her parents' jobs
    # Girl mentions her father's programming career.
    # Girl explains programming
    # Boy suggests to make programs that provide free Internet
    # Boy explains his love for internet and games "It should be free for everyone!"
    # Girl agrees.
    # Boy declares future job to be a programmer.
    # Girl declares the same.
label test:
    "Test mode"
    menu:
        "Select mode"
        "Story":
            return
        "Rogue":
            call roguemode
        "Dialog":
            call testdialog
    return

label testdialog:
    "test"
    # call battlev3(ILY,CodeRed,pbitsMax=8,ebitsMax=8)
    # if playerHP==0:
    #     return
    ""
    stop music
    scene gridbglandscape1:
        zoom 0.75
    show CodeRed with dissolve
    c"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    c"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    c"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    c"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    # hide CodeRed
    # call var_init
    # call iptest\
    # $hands=[VirusFlame,XAxess,DataDrill,MailSaber,BreakSaber]

    # call screen choosecardv3(hands)
    # $ index=0

    # call screen Card(DataForce,(0,0),Return())
    show ILY_Alpha
    ia"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    ia"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    
    show Lucida
    lc"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    lc"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    
    $ Lucida_m="smile"
    lc"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    show Brain
    br "Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    br "Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    
    $ Brain_m="smile"
    br "Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    
    $ Vira_w= True
    show Vira with dissolve:
        xanchor 0.5 xpos 0.85
    v"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    v"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    v"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    # hide Vira
    
    show Ave with dissolve:
        xalign 0.03
    a"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    a"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    a"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    a"Lorem Ipsum dolor sit amet consectetur adipiscing elit."
    # hide Ave
    return

label Vtuber:

    $ game_over = False
    play music "bgm/ost/Discussion-RLD_05-by- NoyemiK_.mp3"
    while not game_over:


        scene cafeoutside2
        ""
        $ ILY_m='smile'
        show ILY:
            # yalign 0.0
            xalign 0.5
        call screen speakbuttons
        # i "Thank You For Watching!"
        # show ILY:
        #     linear 0.2 yoffset -30
        #     linear 0.2 yoffset 0
        # $ ILY_m='smile3'
    
        # i "Don't forget to Like, Share and Subscribe!!"

    return
screen speakbuttons:

    key "K_DOWN" action SetVariable("ILY_e","2")
    key "K_UP" action SetVariable("ILY_e","1")
    key "K_LEFT" action SetVariable("ILY_m","frown")
    key "K_RIGHT" action SetVariable("ILY_m","smile3")
    key "K_SPACE" action SetVariable("speaking","ILY")
    key "repeat_K_SPACE" action SetVariable("speaking","ILY")
    key "keyup_K_SPACE" action SetVariable("speaking",None)
    key "K_ESCAPE" action SetVariable("game_over",True),Return()