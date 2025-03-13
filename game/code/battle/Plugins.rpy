label Plugins_Run:
    if enemyfirst:
        $ enemyplugin=enemyDeck["plugins"]
    $ playerplugin=playerDeck["plugins"]
    call PluginExecution
    return
label PluginExecution:
    $ runnumber = 0
    $ attacknumber = 0
    
    #Index of looper
    $iterations =len(playerplugin)
    show screen phasemsg("INITIALIZE!")
    $renpy.pause(0.5,hard=True)
    hide screen phasemsg

    label exec_loop:

        $ currentcard = playerplugin[0]
        $ playerplugin.pop(0)
        # $ currentcard = (playerplugin[runnumber])
        $ currentcardFXN = currentcard.FXN
        $ currentcardMAG = currentcard.MAG
        $ currentcardTYPE = currentcard.TYPE
        $ Magnitude = (currentcardMAG)
        $ damagetoenemy=int(playerATK_m*Magnitude)
        $ currentcardfunctions=[a.name for a in currentcardFXN]
        $ damagecard = ("attack" in currentcardfunctions) 
        
        hide screen battlestats
        show screen battlestats
        call battlecry from _call_battlecry
        play sound "sound/swing.wav"
        call screen cardflashscreen
        show screen cardflashscreen2
        
        ##
        $fxnindex=0
        $loopingcard=False
        $execution_active=True
        label runfunctions:
            $ runfxnstring = currentcardFXN[fxnindex].name
            hide screen cardflashscreen2
            show screen cardflashscreen2
            label hitloop:
                call functioneffects(runfxnstring)
            $fxnindex+=1
            if fxnindex<len(currentcardFXN):
                jump runfunctions

        hide screen cardflashscreen2
        hide ring
        $execution_active=False
        $fxnindex=0
        $runnumber+=1
        if (runnumber<iterations) and (battle_done==False):
            jump exec_loop
        else:

            call PlayerEndPhase from _call_PlayerEndPhase
            # info"[playerName]'s turn has ended."
            if not battle_done:
                call enemyattack from _call_enemyattack_1
    return