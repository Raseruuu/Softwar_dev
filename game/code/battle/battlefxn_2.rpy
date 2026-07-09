label Attack(params={}):
    #  {
    #    "multiplier":multiplier,
    #    "rangevalue":rangevalue,
    #    "absolute",absolute,
    #    "onhit":onhit
    #     }
    $ Attackparams=params
    if currentcardFXN[fxnindex].name=="Attack" and params["onhit"]:
        $ block_functions_ATK=params["onhit"]
    else:
        $ block_functions_ATK=[]
    # if currentcard_fxn_params[0]!="POWR" and currentcard_fxn_params[0]: 
    $ damagemultiplier = params["multiplier"]
    $ absolutedamage = params["absolute"]
    # "ATTACK BLOCK [block_functions]"
    $ Power = (currentcardPOW)
    if absolutedamage:
        $ damagetoenemy=int(damagemultiplier)
    else: 
        if damagemultiplier=="POWR":
            $ damagetoenemy=int(playerATK_m*Power)
        elif damagemultiplier!="POWR": 
            $ damagetoenemy=int(playerATK_m*damagemultiplier)
    $ attackrange = params["rangevalue"]
    $ attackhit=True
    $ battle_distance_old=battle_distance
    ## EVADE
    
    # elif attackhit:
    if battle_distance>attackrange:
            
        $ attackhit=False
        # show Enemy:
        #     xalign 0.5 yanchor 0.32 ypos 0.3
        $ enemy_evasion_active=True
        
        play sound "sfx/miss.wav" channel 1
        show Enemy at sidesteps_effect_dodge("Enemy", 0.5, renpy.random.choice([0.6,0.4]), 0.12)
            # yanchor 1.0 ypos 0.5
            # yanchor 0.32 ypos 0.3
            # yoffset 1.0
        pause 0.24
        $ enemy_evasion_active=False
        show Enemy:
            alpha 1.0
            xalign 0.5 yanchor 0.32 ypos 0.3 
        call battlemessage("MISSED!")
        call Advance(params={"quantity":1})
        if battle_distance==0 and battle_distance_old>0:
            call battlemessage("DISTANCE:ZERO")
        $ renpy.pause(0.2,hard=True)
        return
        
    if "Evade" in EnmySts:
    #     $ attackhit=False
    # if not attackhit:
        $ EnmySts.remove('Evade') 
        $ enemy_evasion_active=True
        pause 0.1
        play sound "sfx/miss.wav" channel 1
        show Enemy at sidesteps_effect_dodge("Enemy", 0.5, renpy.random.choice([0.6,0.4]), 0.12)
        pause 0.24
        $ enemy_evasion_active=False
        show Enemy:
            xalign 0.5 yanchor 0.32 ypos 0.3 
        call battlemessage("EVADED")
    # NO EVADE    
    else:
        $ enemy_being_damaged=True
        $ enemyHP_stay = enemyHP
        call TYPE_sfx
        call hurtnoise_enemy
        python:
            if enemySP>0:
                enemySP-=damagetoenemy
                if enemySP<0:
                    enemyHP+=enemySP
                    enemySP = 0
            else:
                enemyHP-=damagetoenemy

            if enemyHP <=0:
                enemyHP = 0
                
                battle_done=True
            dmgdist = ((currentcard.POW*100)/20)
            dmgdist = int(dmgdist*2.5)
        hide damageeffect
        show damageeffect
        show dmgpoint onlayer overlay
        show Enemy:
            linear 0.05 zoom 0.94
            xoffset (dmgdist) yoffset (dmgdist) alpha 0.7
            pause .05
            xoffset (dmgdist*-1) yoffset (dmgdist*-1) alpha 0.8
            pause .05
            xoffset (dmgdist) yoffset (dmgdist) alpha 1.0
            pause 0.05
            xoffset ((dmgdist*-1)-2) yoffset ((dmgdist)-2)
            pause 0.05
            xoffset 0 yoffset 0
            linear 0.05 zoom 1.0

        $ renpy.pause(0.6,hard=True)
        call TYPE_delay
        show Enemy:
            alpha 1.0
            xalign 0.5 yanchor 0.32 ypos 0.3
            
        hide damageeffect
        $ enemy_being_damaged=False
        if block_functions_ATK !=[]:
            $ block_count_ATK = 0
            label block_loop_atk:
                $ runfxnstringatk = block_functions_ATK[block_count_ATK].name
                $ newfunctionparam=block_functions_ATK[block_count_ATK].params
                call functioneffects(runfxnstringatk,newfunctionparam)
                $ block_count_ATK+=1
                if block_count_ATK<len(block_functions_ATK):
                    jump block_loop_atk
    return

label RemoveTokenPlayer(params={}):
    
    $ token_name = params["tokenname"]
    $ remove_target = params["target"]
    if remove_target=="Self":
        $ PlayerSts.remove(token_name)
        show screen tokenremove_anim(token_name,"player")
        $ renpy.pause(0.4,hard=True)
        hide screen tokenremove_anim
    elif remove_target=="Enemy":
        $ EnmySts.remove(token_name)
        
        show screen tokenremove_anim(token_name,"enemy")

        $ renpy.pause(0.4,hard=True)
        hide screen tokenremove_anim
    return
label RemoveTokenEnemy(params={}):
    $ token_name = params["tokenname"]
    $ remove_target = params["target"]
    if remove_target=="Self":
        $ EnmySts.remove(token_name)
        show screen tokenremove_anim(token_name,"enemy")
        $ renpy.pause(0.4,hard=True)
        hide screen tokenremove_anim
    elif remove_target=="Enemy":
        $ PlayerSts.remove(token_name)
        show screen tokenremove_anim(token_name,"player")
        $ renpy.pause(0.4,hard=True)
        hide screen tokenremove_anim
    return


label Retreat(params={},distanceamount=0):
    $ paramsvar = params
    $ distance_quantity = params["quantity"]
    python:
        for dist in range(0,distance_quantity):
            # if battle_distance!=0:
            battle_distance=battle_distance+1
            renpy.show("Enemy")
            renpy.play("sound/stepfar.wav","sound")
            
            renpy.pause(0.3,hard=True)
    call updatestats_enemy
    return
label Advance(params={},distanceamount=0):
    $ distance_quantity = params["quantity"]
    python:
        for dist in range(0,distance_quantity):
            if battle_distance!=0:
                battle_distance=battle_distance-1
                renpy.show("Enemy")
                renpy.play("sound/stepnear.wav","sound")
                # dist+=1
                renpy.pause(0.3,hard=True)
    call updatestats_enemy
    return
# label Advanceplayer(params={},distanceamount=0,):
#     $ distance_quantity = params["quantity"]
#     python:
#         for dist in range(0,distance_quantity):
#             if battle_distance!=0:
#                 battle_distance=battle_distance-1
#                 renpy.show("Enemy")
#                 renpy.play("sound/stepnear.wav","sound")
#                 renpy.pause(0.3,hard=True)
#     call updatestats_player
#     return
label GiveToken(params={}):
    $ token_name = params["tokenname"]
    $ quantity = params["quantity"]
    # $ EnmySts.append("Burn")
    $ counter=0
    label tokenquant_loop:
        play sound "sfx/tokengain.mp3"
        $ EnmySts=statusAppend(EnmySts,token_name)
        show screen tokenappend_anim(token_name)
        $ renpy.pause(0.4,hard=True)
        hide screen tokenappend_anim
        $ counter+=1
        if counter<quantity:
            jump tokenquant_loop
    call updatestats_enemy
    return
label GainTokenPlayer(params={}):
    $ token_name = params["tokenname"]
    $ quantity = params["quantity"]
    # $ EnmySts.append("Burn")
    $ counter=0
    label tokenquant_loop2:
        play sound "sfx/tokengain.mp3"
        $ PlayerSts=statusAppend(PlayerSts,token_name)
        show text "{size=20}"+token_name+"{/size}" onlayer overlay:
            
            zoom 1.3 xpos 0.1 xanchor 0.5 yanchor 1.0 ypos 0.20 alpha 1.0
            pause 0.2
            linear 0.1 zoom 0.98
            linear 0.2 zoom 1.0 alpha 0.0
        $ renpy.pause(0.6,hard=True)
        hide text
        $ counter+=1
        if counter<quantity:
            jump tokenquant_loop2
    return