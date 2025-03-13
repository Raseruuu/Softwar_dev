label Plugins_Run:

    $ playerplugin=playerDeck["plugins"]
    $ enemyplugin=enemyDeck["plugins"]
    
    if enemyfirst: 
        call PluginExecution(playerplugin,"enemy")
        call PluginExecution(playerplugin,"player")
    else:
        call PluginExecution(playerplugin,"player")
        call PluginExecution(playerplugin,"enemy")
    return
label PluginExecution(plugin_set,plugin_user):
    $ runnumber = 0
    $ attacknumber = 0
    
    #Index of looper
    $iterations =len(plugin_set)
    show screen phasemsg("INITIALIZE!")
    $renpy.pause(0.5,hard=True)
    hide screen phasemsg
    
    label exec_loop_plugins:

        $ currentcard = playerplugin[0]
        $ plugin_set.pop(0)
        # $ currentcard = (plugin_set[runnumber])
        $ currentcardFXN = currentcard.FXN
        $ currentcardMAG = currentcard.MAG
        $ currentcardTYPE = currentcard.TYPE
        $ Magnitude = (currentcardMAG)

        $ damagetoenemy=int(playerATK_m*Magnitude)
        $ currentcardfunctions=[a.name for a in currentcardFXN]
        $ damagecard = ("attack" in currentcardfunctions) 
        
        hide screen battlestats
        show screen battlestats
        # call battlecry
        play sound "sound/swing.wav"
        if plugin_user=="player":
            call screen cardflashscreen
            show screen cardflashscreen2
        elif plugin_user=="enemy":
            call screen cardflashscreenenemy
            show screen cardflashscreenenemy
            
        ##
        $fxnindex=0
        $loopingcard=False
        $execution_active=True
        label runfunctions_plugins:
            $ runfxnstring = currentcardFXN[fxnindex].name
            if plugin_user=="player":
                hide screen cardflashscreen2
                show screen cardflashscreen2
            else:
                hide screen cardflashscreenenemy2
                show screen cardflashscreenenemy2
            label hitloop_plugins:
                call functioneffects(runfxnstring)
            $fxnindex+=1
            if fxnindex<len(currentcardFXN):
                jump runfunctions

        hide screen cardflashscreen2
        hide screen cardflashscreenenemy2

        hide ring
        $execution_active=False
        $fxnindex=0
        $runnumber+=1
        if (runnumber<iterations) and (battle_done==False):
            jump exec_loop
        else:

            call PlayerEndPhase
            # info"[playerName]'s turn has ended."
            if not battle_done:
                call enemyattack
    return