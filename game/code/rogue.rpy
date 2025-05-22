#################
##################
# default game_over=False
# default battle_active=False
define FAI_playables=[ILY, Ave, CodeRed, Vira, Bitwulf]



default r_Bosses=[]

# playerDeck = PlayerStatsnow["Deck"]
#     actual_playerDeck = playerDeck
label roguemode:
   
    "Rogue mode Start"
    "SoftWar"
    "Choose Your F.A.I. Fighter!"
    #create a character select screen like Bleach 4th flamebringer
    menu:
        "Choose Your F.A.I. Fighter!"
        "ILY":
            $ playerobject=ILY
            
        "Ave":
            $ playerobject=Ave
        "Code Red":
            $ playerobject=CodeRed
    python:
        PFAI=playerobject
        r_Bosses=FAI_playables

        mydeck=PFAI.deck
        deckplugin =mydeck["plugins"]
        plugincurrent =sorted( mydeck["plugins"],key=lambda x: x.NAME, reverse=False)
        deckcurrent =sorted( mydeck["content"],key=lambda x: x.NAME, reverse=False)
        
        PlayerStatsnow = {
            "name":PFAI.name,
            "HP":PFAI.HP,
            "HPMax":PFAI.HP,
            "SP":0,
            "SPMax":PFAI.SP,
            "ATK":PFAI.ATK,
            "DEF":PFAI.DEF,
            "Deck":PFAI.deck
        }
        statuslist=["BoostATK","BoostDEF","Email"]
        playerbits = 8
        playerstats = PlayerStatsnow
        playerName = PlayerStatsnow["name"]
        playerHP = PlayerStatsnow["HP"]
        playerHPMax = PlayerStatsnow["HPMax"]
        playerSP = 0
        playerSPMax = PlayerStatsnow["SPMax"]
        playerATK = PlayerStatsnow["ATK"]
        playerDEF = PlayerStatsnow["DEF"]

        actual_playerDeck = playerDeck
        playerPlugins =PlayerStatsnow["Deck"]["plugins"]
        fxnindex=0
        execution_active=False
        enemy_evasion_active=False
        evasion_active=False
        battle_done = False
        enemyfirst =False
        map_active=False
        playerbattlecode=[]
    
    # $ r_Bosses=FAI_playables
   
    ""
    
    
    label newbattle:
    $ enemyvirus = renpy.random.choice([Keylogger,Ransomware,Rootkit,Worm,Spyware])
    $ enemyobject= enemyvirus
    call battlev3(playerobject,enemyobject)
    if playerHP==0:
        $ game_over=True
    if not game_over:
        jump newbattle
    
label r_battlestart:
    
    return



