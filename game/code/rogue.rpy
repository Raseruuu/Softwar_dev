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
    label newnodes:
        call r_battlestart
        scene gray
        call screen roguenodeselect
        ""
        $ nodes_path=[]
        jump newnodes
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
            self.LABEL = LABEL
    Enemy=Node("Mob Virus", "Enemy","R_Enemy")
    StrongEnemy=Node("Rogue Virus", "StrongEnemy","R_StrongEnemy")
    Treasure=Node("Treasure", "Treasure","R_TreasureNode")
    Recovery=Node("Recovery", "Recovery","R_RecoveryNode")
    StellaShop=Node("Stella's Shop", "Shop","R_StellaShop")
    def random_node(used_nodes):
        global nodes_tpf
        choicenodes=nodes_tpf
        newnode = renpy.random.choice(choicenodes)
        nodes_tpf.remove(newnode)
        return newnode
label r_battlestart:
    python:
        used_nodes=[]
        nodes_tpf=[Enemy]*10+[StrongEnemy]*2+[Treasure,Recovery,StellaShop]
        for nodes in range(0,5):
            # nodes_path.append([random_node(),random_node()])
            newnoderow=[]
            for i in range(nodes+1):
                newrandomnode=random_node(used_nodes)
                if newrandomnode not in used_nodes:
                    used_nodes.append(newrandomnode)
                newnoderow.append(newrandomnode)
            print(newnoderow)
            nodes_path.append(newnoderow)
    return
screen roguenodeselect():
    vbox:
        xalign 0.5 yalign 0.5
        for nodes in nodes_path:
            hbox:
                xalign 0.5 yalign 0.5
                for nodex in nodes:
                    vbox:
                        xalign 0.5 yalign 0.5
                        text (nodex.TYPE+"")  at zoomtrans(0.4)
                        add ("gui/"+nodex.TYPE+".png") at zoomtrans(0.2)

                     
            
    key "dismiss" action Return()
