label Plugins_Run:
    $ deckplugin=playerPlugins
    $ playerplugin=deckplugin
    $ enemyplugin=enemyPlugins
    
    if enemyfirst: 
        
        call PluginExecution(enemyplugin,"enemy")
        call PluginExecution(playerplugin,"player")
    else:
        call PluginExecution(playerplugin,"player")
        call PluginExecution(enemyplugin,"enemy")
    return
label PluginExecution(plugin_set,plugin_user):
    $ runnumber = 0
    $ attacknumber = 0
    $ plugincurrent=""
    if plugin_set:
        $ plugincurrent=plugin_set[0].NAME
    "Plugin [plugin_user], [plugincurrent]"
    #Index of looper
    $iterations =len(plugin_set)
    if iterations>0:
        show screen phasemsg("INITIALIZE!")
    if iterations>0:
        
        
        $renpy.pause(0.5,hard=True)
        hide screen phasemsg
        label exec_loop_plugins:
            if plugin_user=="player":
                $ currentcard = playerplugin[runnumber]
            elif plugin_user=="enemy":
                $ currentcard = enemyplugin[runnumber]
            $ plugin_set.pop(0)
            # $ currentcard = (plugin_set[runnumber])
            $ currentcardFXN = currentcard.FXN
            $ currentcardMAG = currentcard.MAG
            $ currentcardTYPE = ""
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
            hide screen cardflashscreenenemy
            label runfunctions_plugins:
                $ runfxnstring = currentcardFXN[fxnindex].name
                if plugin_user=="player":
                    hide screen cardflashscreen2
                    show screen cardflashscreen2
                else:
                    hide screen cardflashscreenenemy2
                    show screen cardflashscreenenemy2
                label hitloop_plugins:
                    if plugin_user=="player":
                        call functioneffects(runfxnstring)
                    elif plugin_user=="enemy":
                        call enemyfunctioneffects(runfxnstring)
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
                jump exec_loop_plugins
            else:
                return
            
    return