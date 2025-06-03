#################
##################
# default game_over=False
# default battle_active=False
define FAI_playables=[ILY, Ave, CodeRed]



default r_Bosses=[ILY, Ave, CodeRed]

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
        playerPlugins =PFAI.deck["plugins"]
        fxnindex=0
        execution_active=False
        enemy_evasion_active=False
        evasion_active=False
        battle_done = False
        enemyfirst =False
        map_active=False
        playerbattlecode=[]
    
    # $ r_Bosses=FAI_playables
   
    "NODE"
    call r_battlestart
    scene gray
    call screen roguenodeselect
    label newbattle:
    $ enemyvirus = renpy.random.choice([Keylogger,Ransomware,Rootkit,Worm,Spyware])
    $ enemyobject= enemyvirus
    call battlev3(playerobject,enemyobject)
    if playerHP==0:
        $ game_over=True
    if not game_over:
        jump newbattle
    
default nodes_path=[]

init python:
    def mobvirus_random():
        enemyvirus = renpy.random.choice([Keylogger,Ransomware,Rootkit,Worm,Spyware])
        return enemyvirus
    class Node:
        def __init__(self,NAME,TYPE,LABEL):
            self.NAME = NAME
            self.TYPE = TYPE
            # enemy, 
            self.LABEL = LABEL
    Enemy=Node("Mob Virus", "Enemy","R_Enemy")
    StrongEnemy=Node("Rogue Virus", "StrongEnemy","R_StrongEnemy")
    Treasure=Node("Treasure", "Treasure","R_TreasureNode")
    Recovery=Node("Recovery", "Recovery","R_RecoveryNode")
    StellaShop=Node("Stella's Shop", "Shop","R_StellaShop")
    def random_node():
        newnode = renpy.random.choice([Enemy,Treasure,Recovery,StellaShop])
        return newnode
label r_battlestart:
    python:
        for nodes in range(0,5):
            nodes_path.append([random_node(),random_node()])
    return
screen roguenodeselect():
    vbox:
        xalign 0.5 yalign 0.5
        for nodes in nodes_path:
            hbox:
                text ""+nodes[0].NAME
                text ""+nodes[1].NAME
    key "dismiss" action Return()
