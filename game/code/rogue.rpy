#################
##################
# default game_over=False
# default battle_active=False
define FAI_playables=[ILY, Ave, CodeRed]



default r_Bosses=[ILY, Ave, CodeRed, Melissa, Vira]

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
        node_current=(0,0)
    "NODE"
    scene gray
    call r_battlestart
    label newnodes:
        play music "bgm/ost/Serious_Noyemi_K.ogg"
        scene black
        call screen roguenodeselect
        if not game_over: 
            jump newnodes
        
    return
    # label newbattle:
    # $ enemyvirus = renpy.random.choice([Keylogger,Ransomware,Rootkit,Worm,Spyware])
    # $ enemyobject= enemyvirus
    # call battlev3(playerobject,enemyobject)
    # if playerHP==0:
    #     $ game_over=True
    # if not game_over:
    #     jump newbattle
    
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
    Boss=Node("Boss", "Boss","R_Boss")
    
    def random_node(used_nodes):
        global nodes_tpf
        choicenodes=nodes_tpf
        newnode = renpy.random.choice(choicenodes)
        nodes_tpf.remove(newnode)
        return newnode
label R_Enemy:
    $ enemyvirus = renpy.random.choice([Keylogger,Ransomware,Rootkit,Worm,Spyware])
    $ enemyobject= enemyvirus
    call battlev3(playerobject,enemyobject)
    
    if playerHP==0:
        $ game_over=True
    
    return
label R_StrongEnemy:
    $ enemyvirus = renpy.random.choice([Keylogger,Ransomware,Rootkit,Worm,Spyware])
    $ enemyobject= enemyvirus
    call battlev3(playerobject,enemyobject)
    if playerHP==0:
        $ game_over=True
    
    return
label R_TreasureNode:
    "Get A new Treasure!!"
    
    return
label R_RecoveryNode:
    "Heal Up!!!"
    
    return
label R_StellaShop:
    "Welcome to Stella's Shop!!"
    
    return
label R_Boss:
    $ enemyobject= enemyvirus

    call battlev3(playerobject, stageboss)
    if playerHP==0:
        $ game_over=True
    
    
    return
label r_battlestart:
    python:
        used_nodes=[]
        nodes_tpf=[Enemy]*10+[StrongEnemy]*2+[Treasure,Recovery,StellaShop]
        for nodes in range(0,5):
            # nodes_path.append([random_node(),random_node()])
            newnoderow=[]
            for nodeitems in range(nodes+1):
                newrandomnode=random_node(used_nodes)
                if newrandomnode not in used_nodes:
                    used_nodes.append(newrandomnode)
                newnoderow.append(newrandomnode)
            nodes_path.append(newnoderow)
        nodes_path.append([Boss])
        # r_Bosses.remove(playerobject)
        stageboss=renpy.random.choice(r_Bosses)
        r_Bosses.remove(stageboss)

    return
init python:
    def nodechoices(pos_tuple):
        node_x=pos_tuple[1]
        node_y=pos_tuple[0]
        node_choice1=(node_x,node_y+1,)
        node_choice2=(node_x+1,node_y+1)
        list_node_choice=[]
        if node_y==4:
            list_node_choice=[(0,5)]
        else:
            list_node_choice=[node_choice1,node_choice2]
        #   nodechoices(1,1)

        return list_node_choice
    def change_node(nodechoice,node_item):
        global node_current
        node_current=nodechoice
        nodelabel=node_item.LABEL
        renpy.call(""+nodelabel)
        return node_current
    def check_choice(n_index_1,n_index_2):
        # nodechoices((n_index_2,n_index_1))[0]==n_index_2 and nodechoices((n_index_2,n_index_1))[1]
        if (n_index_2,n_index_1) in nodechoices((node_current[0],node_current[1])):

            return True
        else:
            return False
screen roguenodeselect():
    # text str(node_current) xalign 0.75 yalign 0.75
    text str(stageboss.name) xalign 0.5 yalign 0.1
    hbox:
        spacing 80
        xalign 0.5 yalign 0.5
        for n_index_1,nodes in enumerate(nodes_path):
            vbox:
                spacing 10
                xalign 0.5 yalign 0.5
                for n_index_2,node_item in enumerate(nodes):
                    vbox:
                        
                        xalign 0.5 yalign 0.5
                        if (check_choice(n_index_1,n_index_2)):
                            imagebutton:
                                idle Composite(
                                    (422,422),
                                    (0,0),("gui/"+node_item.TYPE+".png"),
                                    (0,0),(("gui/selector2.png")))  
                                hover Composite(
                                    (422,422),
                                    (0,0),("gui/"+node_item.TYPE+".png"),
                                    (0,0),("blinky"))
                                at zoomtrans(0.2)
                                action Function(change_node,(n_index_1,n_index_2),node_item),Return()
                        elif node_current==(n_index_1,n_index_2):
                            imagebutton:
                                idle Composite(
                                    (422,422),
                                    (0,0),("gui/"+node_item.TYPE+".png"),
                                    (0,0),(("gui/selector.png")))
                                at zoomtrans(0.2)
                                action NullAction()
                          
                        else:
                            add ("gui/"+node_item.TYPE+".png") at zoomtrans(0.2)
                        vbox:
                            text (node_item.TYPE+" ")  
                            # text ("("+str(n_index_1)+","+str(n_index_2)+")")  
                            at zoomtrans(0.5)
                        

    # key "dismiss" action Return()
