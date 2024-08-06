init python:
    class FAI:
        def __init__(self,name,kind,HP,SP,ATK,DEF,deck,status):
            self.name=name
            self.HPmax = HP
            self.HP= HP
            self.SP= SP
            self.ATK = ATK
            self.DEF = DEF
            self.kind = kind
            self.deck = deck
            self.status = status
    class Card:
        def __init__(self,NAME,TYPE,MAG,FXN,COST):
            self.NAME = NAME
            self.TYPE = TYPE
            self.MAG = MAG
            self.FXN = FXN
            self.COST = COST


    class Plugin:
        def __init__(self,NAME,DESC,MAG,FXN,COST):
            self.NAME = NAME
            self.DESC = DESC
            self.MAG = MAG
            self.FXN = FXN
            self.COST = COST
    class Item:
        def __init__(self,NAME,TYPE,DESC,FXN):
            self.NAME = NAME
            self.TYPE = TYPE
            self.DESC = DESC
            self.FXN = FXN
    class Item_dress:
        def __init__(self,NAME,TYPE,DESC):
            self.NAME = NAME
            self.TYPE = TYPE
            self.DESC = DESC
    # class Card:
    #     def __init__(self,name,POW,SPD,fxn,rank):
    #         self.name=name
    #         # self.type =
    #         self.POW = POW
    #         self.SPD = SPD
    #         self.fxn = fxn
    #         self.rank = rank
    class Fxn:
        def __init__(self,name,code,text,params=[]):
            self.name=name
            #code to display
            self.code=code
            self.text=text
            self.params=params
            # self.displayname=name+"()"
    class BattleStatus:
        def __init__(self,name,text,magnitude):
            self.name=name
            self.text=text
            self.magnitude=magnitude




#     Freeze =    Fxn("Freeze()","Negate 1 execution")
#     # Break = Fxn("Break","Break 1 execution")
#     Breach = Fxn("Breach()","Inflict SP-Ignoring Damage.")
#     ForEachEmail=Fxn("while E has Email:","Iterate enclosed function")
#
#
#     Damage = Fxn("Damage(MAG)","Inflict Damage to enemy.")
#     RemovEmailDamage = Fxn("  RemoveEmail()\n  Damage(MAG)","Remove Email. Inflict MAG * ATK Damage.")
#     DamageSP = Fxn("DamageSP(MAG)","Inflict Damage to SP.")
#     DamageSPself = Fxn("DamageSPself(MAG)","Inflict Damage to own SP.")
#     Recover = Fxn("Recover(MAG)","Increase HP.")
#     Shield = Fxn("Shield(MAG)","Increase SP.")
#     Reflect = Fxn("Reflect(MAG)","Apply Reflect Status:{Negate incoming Damage; BoostATK;}")
#     Burn_Self = Fxn("Burnself()","Append Burn status to self.")
#     BoostATK = Fxn("BoostATK()","Increase ATK")
#     BoostDEF = Fxn("BoostDEF()","Increase DEF")
#     AntiAntiDamage = Fxn("AntiAntiDamage()","Remove all AntiDamage from your opponent")
#     HalfHP_self = Fxn("HalfHP_self()","Half current HP of self.")
#     Evade = Fxn("NegateDmg()","Negate a Damage function once.")
#     ReduceBit = Fxn("reduceBit","ReduceBit()","Reduce opponent's bit value by 1.")
#     BoostGun = Fxn("BoostGun()","Increase  MAG of \"Gun\" type Battleware")
#     BoostSword = Fxn("BoostSword()","Increase  MAG of \"Sword\" type Battleware")
# #Tokens
#
#
#     Email=Fxn("Email()","Append Email token to opponent.")
#     Burn = Fxn("Burn()","Append Burn token to opponent.")
#     Saber = Fxn("Saber()","Gain a \"Saber\" token.")
#     Bullet = Fxn("Bullet()","Gain a \"Bullet\" token.")
    def Burn(burndmg):
        return Fxn(
            "Burn",
            "burn("+str(burndmg)+")",
            "Apply Burn status to target, Burn token deals "+str(burndmg)+" each turn.",
            burndmg
            )
    def BurnSelf(burndmg) :
        return Fxn("BurnSelf","burnself()","Append Burn status to self.")
    def Evade(quantity):
        return Fxn(
            "Evade",
            "evade("+str(quantity)+")",
            "Gain "+str(quantity)+" \"Evade\" token(s). This will allow you to evade Attack() functions.",
            [tokenname,quantity])
    def GainToken(tokenname,quantity):
        return Fxn(
            "GainToken",
            "gainToken(\""+str(tokenname)+"\","+str(quantity)+")",
            "Gain "+str(quantity)+" \""+str(tokenname)+"\" token(s).",
            [tokenname,quantity])
    def GiveToken(tokenname,quantity):
        return Fxn(
            "GiveToken",
            "giveToken(\""+str(tokenname)+"\","+str(quantity)+")",
            "Give a \""+str(tokenname)+"\" token(s).",
            [tokenname,quantity])
    def ReduceBit(quantity):
        return Fxn(
            "ReduceBit",
            "reduceBit("+str(quantity)+")",
            "Reduce opponent's bit value by "+str(quantity)+"."
            )
    def While(condition,token_name,target,fxns):
        function1=fxns[0].code
        codepart2=""
        if len(fxns)==2:
            function2=fxns[1]
            codepart2="\n  "+str(function2.code)
        return Fxn(
            "While",
            "while("+str(condition)+"):\n  "+str(function1)+codepart2,
            "Execute enclosed functions while condition is True",
            (token_name,fxns,target)
            )
    def ForInRange(condition,iterations,fxns):
        function1=fxns[0].code
        codepart2=""
        if len(fxns)==2:
            function2=fxns[1]
            codepart2="\n  "+str(function2.code)
        return Fxn(
            "ForInRange",
            "for("+str(condition)+"):\n  "+str(function1)+codepart2,
            "Execute enclosed functions for each item in list",
            (iterations,fxns)
            )

    def IfFunction(condition,token_name,target,fxns):
        function1=fxns[0].code
        if len(fxns)==2:
            function2=fxns[1]
            codepart2="\n  "+str(function2.code)
        return Fxn(
            "If",
            "if ("+str(condition)+"):\n  "+str(function1)+codepart2,
            "Execute enclosed functions if condition is True",
            (token_name,fxns,target)
            )
    def Boost(statname,MAG):
        return Fxn(
            "Boost"+statname,
            "boost(\""+str(statname)+"\","+str(MAG)+")",
            "Increase "+str(statname)+" by "+str(MAG)+".",
            [statname,MAG]
            )
    def Freeze():
        return Fxn(
            "Freeze",
            "Freeze()",
            "Apply Freeze status to target, Freeze token negates the execution of a card function.")
    def Attack():
        return Fxn(
            "Attack",
            "attack(ATK*MAG)",
            "Deal Damage to target.")
    def AttackSP():
        return Fxn(
            "AttackSP",
            "attackSP(ATK*MAG)",
            "Deal Damage to target's SP.")
    def Defend():
        return Fxn(
            "Defend",
            "defend(DEF*MAG)",
            "Gain Shield Points.")
    def Recover(MAG):
        return Fxn(
            "Recover",
            "recover(MAXHP*MAG)",
            "Recover (MAXHP * MAG) HP.",
            MAG
            )
    #
 
    def RemoveToken(token_name,target):
        return Fxn(
            "RemoveToken",
            "removeToken(\""+token_name+"\",\""+target+"\")",
            "Remove 1 \""+token_name+"\" token from target's status.",
            (token_name,target)
            )

    def NullFxn():
        return Fxn(
            "",
            "",
            ""
            )
    # GainToken("E-mail")

    # Recover_EX = Fxn("Recover","EX","Recover all HP",,0)
    # Recover_A = Fxn("Recover","A","Gain HP",1000,0)
    # Recover_B = Fxn("Recover","B","Gain some HP",700,0)

    # Empty = Fxn("","")

    # 0 2 4 8 16 32 64 128 256 512 1024
    """
    Average COST for functions

    BITS           1     2     3      4     5      6     7       8
    MAG(Damage)    0.25  0.5   0.75   1.0   1.25   1.5   1.75    2.0
    MAG(Shield)    0.5   0.75  1.0    1.25  1.5    1.75  2.0     2.25
    BoostATK                           *
    BoostDEF                           *
    FXN
    Freeze()       2
    """
#Concatenations
    ##name              name                     TYPE               MAG        FXN List                      COST
    FlameSaber=    Card("FlameSaber",           "FireSword",        1.75,    [Attack(),GiveToken("Burn",3),GainToken("Saber",1) ],                   0)
    FlameDrill=    Card("FlameDrill",           "FireDrill",        0.25,    [ForInRange("x in range(0,8)",8,[Attack()]),Burn(20)],                   0)
    FrostBuster=   Card("FrostBuster",          "IceGun",           1.75,    [Attack(),Freeze()],                   0)
    Waveslash=     Card("Waveslash",            "SwordWave",        1.75,    [Attack(),NullFxn()],                  0)
    # GUNVAR=        Card("Mobile Suit GUNVAR",   "GUNVAR",           1.0,     [Attack(),NullFxn()],   0)
    Concatenations=[FlameSaber,FlameDrill,FrostBuster,Waveslash]
    Concat_strings=[concat.TYPE for concat in Concatenations]

#ILY's cards
    SpamAtk=      Card("SpamAtk",         "Mail",           0.1,   [Attack(),GiveToken("Email",3)],    2)
    MailSaber=    Card("MailSaber",       "Sword",          0.25,  [While("\"Email\" in enmy_status","Email","Enemy",[RemoveToken("Email","Enemy"),Attack()]),NullFxn()],   4)

    RecursiveSlash=Card("RecursiveSlash", "Sword",          0.5,  [While("\"Saber\" in plyr_status","Saber","Self",[RemoveToken("Saber","Self"),Attack()]),NullFxn()],   4)
    SaberAura=Card("SaberAura", "Sword",          0.5,  [While("\"Saber\" in plyr_status","Saber","Self",[RemoveToken("Saber","Self"),Boost("ATK",0.25)]),NullFxn()],   8)

    HeartBurn=    Card("HeartBurn",       "PowerUp",        0.2,   [Boost("ATK",0.25),NullFxn()],       2)
    ChocolateBar= Card("ChocolateBar",    "Chocolate",      0.25,   [Recover(0.25),NullFxn()],          2)
#Ave's cards
    FiberBuster=  Card("FiberBuster",     "Gun",            0.75,    [Attack(),NullFxn()],              4)
    DataBuster=   Card("DataBuster",      "Gun",            0.75,    [Attack(),NullFxn()],              3)
    SparkBuster=  Card("SparkBuster",       "Gun",            0.25,     [Attack(),NullFxn()],           2)
    Snipe=        Card("Snipe",           "Gun",              0.0,     [BoostGun,Evade()],              6)
#Swords and Blades
    # FiberSword=   Card("FiberSword",     "Sword",    0.25,    [AntiAntiDamage,Damage,Empty], 4)
    DataSaber=    Card("DataSaber",      "Sword",           1.0,     [Attack(),GainToken("Saber",1)],   4)
    Katana=       Card("Katana",      "Sword",           0.7,     [Attack(),GainToken("Saber",3)],   4)
    BreakSaber=   Card("BreakSaber",     "Sword",           0.5,     [Attack(),AttackSP(),GainToken("Saber",1)],  3)
    BlockSaber=   Card("BlockSaber",     "Sword",           0.5,     [Attack(),Defend(),GainToken("Saber",1)],    4)
    LambdaSaber=   Card("LambdaSaber",     "Sword",           0.5,     [Attack(),AttackSP(),GainToken("Saber",1)], 3)
    XAxess=       Card("X-Axess",        "X",               0.75,     [AttackSP(),Attack()],            4)
    YAxess=       Card("Y-Axess",        "Y",               0.50,     [AttackSP(),Attack()],            3)
    
    #ZAxess=       Card("Z-Axess",        "Z",      0.25,     [DamageSP,Damage],        1)
#SaberSkills
    SaberDeflect= Card("SaberDeflect",      "Sword",           0.75,     [IfFunction("\"Saber\" in plyr_status","Saber","Self",[RemoveToken("Saber","Self"),Defend()]),NullFxn()],   1)
    MomentumSlash= Card("MomentumSlash",      "Sword",           0.75,     [IfFunction("\"Saber\" in plyr_status","Saber","Self",[RemoveToken("Saber","Self"),AttackSP()]),NullFxn()],   1)
    
# Virus Exclusive
    Vshot=        Card("V-Shot",         "Gun",      0.6,               [Attack(),NullFxn()],           3)
    VirusFlame=   Card("V-Flame",        "Fire",      0.5,            [Attack(),Burn(20)],               3)
    Vslash=       Card("V-Slash",        "Slash",    0.5,            [Attack(),NullFxn()],              2)

#Antivirus Exclusive
    Firewall=     Card("Firewall",       "Wall",    0.75,    [Defend(),Boost("DEF",0.25)],      4)

#Bombs
    DataBomb=     Card("DataBomb",       "Bomb",     1.0,     [Attack(),NullFxn()],          4)
    Flashbang=    Card("Flashbang",      "Bomb",     0.0,     [Attack(),NullFxn()],          2)

#Force
    BruteForce=   Card("BruteForce",     "Force",    1.0,     [Attack(),Boost("ATK",0.25)],      8)
    DataForce=    Card("DataForce",      "Force",    1.0,      [Boost("ATK",0.25),Boost("DEF",0.25)],       4)
   
    DataDrill=    Card("DataDrill",       "Drill",   0.5,     [Attack(),Attack(),Attack()],       5)
    Powersol=     Card("Powersol",        "Wall",    1.0,     [Defend(),Boost("ATK",0.25)],        4)
    Shieldbit=    Card("Shieldbit",       "Wall",    0.25,     [Defend(),NullFxn()],          1)
    RadioShield=  Card("RadioShield",       "Wall",    0.25,     [Defend(),NullFxn()],          1)
    Assault=      Card("Assault",       "Tech",    0.25,       [Boost("ATK",0.25),NullFxn()],  2)
    # Snipe=        Card("Snipe",           "Gun",    0.0,     [BoostGun,Evade],       6)
    Laserbeam=    Card("Laserbeam",       "Gun",    2.0,      [Attack(),NullFxn()],          8)
    Cursorclaw=   Card("Cursorclaw",      "Claw",    0.5,   [Attack(),NullFxn()],           2)
    #newcards

    DrainShield=   Card("DrainShield",    "Shield",      1.0,     [Defend(),GainToken("Negate",1)],   4)
    FieryArc=      Card("FieryArc",       "Bow",         1.0,     [Attack(),Burn(40)],   4)
    CosmicArc=     Card("CosmicArc",      "Bow",         1.0,     [Attack(),GainToken("Saber",1)],   4)
    # SnipeSensor=   Card("SnipeSensor",    "Sword",           1.0,     [Attack(),GainToken("Saber",1)],   4)
    LunexGunSaber= Card("LunexGunSaber",  "Sword",       1.0,     [Attack(),GiveToken("Saber",1)],   4)
    BusterSword=   Card("BusterSword",  "Sword",         1.0,     [Attack(),GiveToken("Saber",1)],   4)
    CupidArc=      Card("CupidArc",       "Bow",         1.0,     [Attack(),GainToken("Saber",1)],   4)
    DataArc=       Card("DataArc",       "Bow",          1.0,     [Attack(),GainToken("Saber",1)],   4)
    Flashbang=     Card("Flashbang",      "Bomb",        1.0,     [Attack(),GainToken("Saber",1)],   4)
    Gigamorph=     Card("Gigamorph",      "Power",       1.0,     [Attack(),GainToken("Saber",1)],   4)
    # DataBuster=    Card("DataBuster",      "Gun",        1.0,     [Attack(),GainToken("Saber",1)],   4)
    Bitbuster=     Card("Bitbuster",      "Gun",         0.5,     [Attack(),ReduceBit(1)],   4)
    MachineBuster= Card("MachineBuster",      "Gun",     1.0,     [Attack(),GainToken("Saber",1)],   4)
    Excalibrium=   Card("Excalibrium",      "Sword",     1.0,     [Attack(),GainToken("Saber",1)],   4)
    ILYFlash=      Card("ILYFlash",      "Power",        1.0,     [Attack(),GainToken("Saber",1)],   4)
    BruiseBash=    Card("BruiseBash",      "Skill",      1.0,     [Attack(),GiveToken("DEFdown",1)],   4)
    ZSlash=        Card("ZSlash",          "Slash",      1.0,     [Attack(),GainToken("Saber",1)],   4)
    FreezeWave=    Card("FreezeWave",      "Wave",       1.0,     [Attack(),Freeze()],   4)
    FreezingBlade= Card("FreezingBlade",   "Sword",      1.0,     [Attack(),Freeze()],   4)
    Salamandra=    Card("Salamandra",      "Sword",      1.0,     [Attack(),GainToken("Saber",1)],   4)
    FlameFists=    Card("FlameFists",      "Fist",       1.0,     [Attack(),GainToken("Saber",1)],   4)
    UltraHead=     Card("U-UltraHead",      "U",           1.0,     [Attack(),GainToken("Armor",1)],   2)
    NitroArms=     Card("N-NitroArms",      "N",           1.0,     [Attack(),GainToken("Armor",1)],   2)
    VoltLegs=      Card("V-VoltLegs",       "V",           1.0,     [Attack(),GainToken("Armor",1)],   2)
    GUNVAR=        Card("Mobile Suit GUNVAR",   "GUNVAR",           1.0,     [Attack(),NullFxn()],   0)

    Shotgun=       Card("Shotgun",      "Gun",           1.0,     [Attack(),GainToken("Saber",1)],   4)
    SwordOfTruth=  Card("SwordOfTruth",      "Sword",           1.0,     [Attack(),GainToken("Saber",1)],   4)
    SwordOfLies=   Card("SwordOfLies",      "Sword",           1.0,     [Attack(),GainToken("Saber",1)],   4)
    VBlaze=        Card("VBlaze",      "Fire",           1.0,     [Attack(),Burn(40)],   4)



    ##NO ART
    # Chainsaw=     Card("Chainsaw",     550,     32,     1, "Break",            'B')
    # SoftDrink=    Card("SoftDrink",    500,    256,     1, "Recover",          'D')
    # Noisewave=    Card("Noisewave",    200,    256,     1, "Firewall",         'C')
    # DataBarrier=  Card("DataBarrier",  300,    256,     1, "Firewall",         'C')

    # Laserbeam=    Card("Laserbeam",    600,    128,     1, "Damage",           'A')
    # WormSlayer=   Card("WormSlayer",   350,    128,     1, "Anti-Worm",        'A')
    # HyperCannon=  Card("HyperCannon",  700,    32,      1,  "Damage",           'A')


    # MegaBomb=    ("MegaBomb",    700,    70)
    # GigaBomb=    ("GigaBomb",    1500,   60)
    #ILY's Deck at the beginning of the game.
    #24 Cards Per deck

#    Plugins:
    RubyRevolver=Plugin("Ruby Revolver", "ILY's magical spinning bracelet!",0.25, GiveToken("Email",1),4)
    SpiderAmulet=Plugin("Spider Amulet", "Why a spider? Because it looks cute!",0.25, Boost("ATK",0.1),4)
    MoonlitAmulet=Plugin("Moonlit Amulet", "Yami's fancy moon-shaped necklace!",0.25, Boost("ATK",0.1),4)
    DigitalPressure=Plugin("Digital Pressure","Let your power overflow!!",1.0,Attack(), 8)
    SnipeSensor=Plugin("SnipeSensor","!",1.0,Attack(), 8)

    #BEFORE BUILD:
    ##CHANGE TO DEFAULT TO AVOID ERRORS
    # [default deckdefault]
    deckdefault = {
        "name":"The Love Machine",
        "content":[
            VirusFlame,VirusFlame,
            VirusFlame,Vslash,
            SpamAtk,SpamAtk,
            SpamAtk,SpamAtk,
            SpamAtk,DataSaber,
            DataSaber,DataSaber,
            ChocolateBar,ChocolateBar,
            DataSaber,MailSaber,
            VirusFlame,RecursiveSlash,
            BlockSaber,SaberDeflect,
            DataSaber,BlockSaber,
            HeartBurn,HeartBurn],
        "plugins":[]
        }
    deckalpha = {
        "name":"The Love Machine",
        "content":[
            VirusFlame,VirusFlame,
            VirusFlame,DataSaber,
            Laserbeam,Laserbeam,
            Laserbeam,Laserbeam,
            SaberDeflect,DataSaber,
            DataSaber,DataSaber,
            SaberDeflect,SaberDeflect,
            Katana,Katana,
            Katana,Katana,
            RecursiveSlash,SaberDeflect,
            Katana,RecursiveSlash,
            DataForce,DataForce],
        "plugins":[]
        }
    deckmelissa = {
        "name":"",
        "content":[
            VirusFlame,VirusFlame,
            VirusFlame,DataSaber,
            DataSaber,DataSaber,
            Vslash,Vslash,
            Vslash,DataBuster,
            DataBuster,DataBuster,
            SpamAtk,DataForce,
            Shieldbit,Shieldbit,
            Shieldbit,Shieldbit,
            XAxess,Vslash,
            Vslash,Bitbuster,
            Bitbuster,Bitbuster],
        "plugins":[]
        }

    # deckdefault = [
    #     VirusFlame,DataBomb,
    #     DataDrill,DataBuster,
    #     Vshot,Vslash,
    #     Vslash,DataDrill,
    #     XAxess,XAxess,
    #     XAxess,XAxess,
    #     DataDrill,DataDrill,
    #     BreakSaber,DataDrill,
    #     HeartBurn,BreakSaber,
    #     BreakSaber,BreakSaber]

    #The first deck you will fight.
    decktrojan = {
        "name":"",
        "content":[
            VirusFlame,VirusFlame,
            VirusFlame,DataBomb,
            DataBuster,DataBomb,
            DataBuster,DataBuster,
            DataBomb,Cursorclaw,
            Cursorclaw,Cursorclaw,
            Vslash,Vslash,
            Vslash,Vslash,
            Vshot,Vshot,
            Vshot,Vshot
            ],
        "plugins":[]
        }

    deckkeylogger ={
        "name":"",
        "content":[
            VirusFlame,VirusFlame,
            VirusFlame,DataBuster,
            DataBuster,DataBuster,
            DataBuster,Vslash,
            DataBomb,Cursorclaw,
            Cursorclaw,Cursorclaw,
            Vslash,Vslash,
            Vslash,Vslash,
            Vshot,Vshot,
            Vshot,Vshot],
        "plugins":[]
        }
    deckransomware = {
        "name":"",
        "content":[
            VirusFlame,VirusFlame,
            VirusFlame,DataBuster,
            DataBuster,DataBuster,
            DataBuster,DataBuster,
            Vslash,Vslash,
            Vslash,Vslash,
            Vshot,Vshot,
            Vshot,Vshot],
        "plugins":[]
        }
    deckrootkit = {
        "name":"",
        "content":[
            Vshot,Vshot,
            Vshot,Vshot,
            Vslash,Vslash,
            Vslash,Vslash,
            Vslash,Vslash,
            Vshot,Vshot,
            Vslash,Vslash,
            Vslash,Vslash,
            Vshot,Vshot,
            Vshot,Vshot],
        "plugins":[]
        }
    deckworm = {
        "name":"",
        "content":[
            Vshot,Vshot,
            Vshot,Vshot,
            Vslash,Vslash,
            Vslash,Vslash,
            Vslash,Vslash,
            Vshot,Vshot,
            Vslash,Vslash,
            Vslash,Vslash,
            Vshot,Vshot,
            Vshot,Vshot],
        "plugins":[]
        }
    deckspyware = {
        "name":"",
        "content":[
            Vshot,Vshot,
            Vshot,Vshot,
            Vslash,Vslash,
            Vslash,Vslash,
            Vslash,Vslash,
            Vshot,Vshot,
            Vslash,Vslash,
            Vslash,Vslash,
            Vshot,Vshot,
            Vshot,Vshot],
        "plugins":[]
        }
    deckvira = {
        "name":"",
        "content":[
            Firewall,
            Firewall,Firewall,
            Firewall,DataBuster,
            DataBuster,
            Shieldbit,Shieldbit,
            DataBuster,Shieldbit,
            Shieldbit,
            Powersol,Powersol,
            Firewall,Firewall,
            Shieldbit,
            Powersol,Powersol,
            DataForce,Firewall],
        "plugins":[]
        }
    deckave = {
        "name":"",
        "content":[
            DataBuster,
            DataBuster,DataBuster,
            DataBuster,Firewall,
            Firewall,
            Firewall,Shieldbit,
            DataBomb,DataBomb,
            Laserbeam,
            Shieldbit,Shieldbit,
            Shieldbit,Bitbuster,
            Bitbuster,
            Assault,Assault,
            Assault,Assault],
        "plugins":[]
        }
    deckred = {
        "name":"",
        "content":[
            DataSaber,DataSaber,
            DataSaber,DataSaber,
            DataSaber,VirusFlame,
            BlockSaber,BlockSaber,
            Katana,Katana,
            Katana,Katana,
            BlockSaber,BlockSaber,
            BlockSaber,DataForce,
            DataForce,DataForce],
        "plugins":[]
        }
    decksephiroth = {
        "name":"",
        "content":[
            DataSaber,DataSaber,
            DataSaber,DataSaber,
            DataSaber,VirusFlame,
            BlockSaber,BlockSaber,
            Katana,Katana,
            Katana,Katana,
            BlockSaber,BlockSaber,
            BlockSaber,DataForce,
            DataForce,DataForce],
        "plugins":[]
        }

    selectedcard = ""
    currentcard = DataSaber

    mydeck = deckdefault
    Enmydeck = decktrojan
    decknum = len(mydeck)
    import random
    random.shuffle(mydeck["content"])
    random.shuffle(Enmydeck["content"])
    movecard = MoveTransition(0.2)

    card1name = "DataSaber"
    card2name = "FiberSword"
    Enmycard1name = "DataSaber"
    Enmycard2name = "FiberSword"

    # BASE STATSO
    #DEFINE CHARACTERS BY
            # NAME,TYPE,HP,SP,ATK,DEF,DECK,STATUS
    ILY=FAI("ILY","Virus",2500,1250,500,500,deckdefault,[])
    ILYAlpha=FAI("ILY","Virus",2500,1250,500,500,deckalpha,[])
    Trojan=FAI("Trojan Horse","Virus",2000,600,400,250,decktrojan,[])
    Keylogger=FAI("Keylogger","Virus",500,250,300,250,deckkeylogger,[])
    Ransomware=FAI("Ransomware","Virus",600,300,300,250,deckransomware,[])
    Rootkit=FAI("Rootkit","Virus",700,350,300,250,deckrootkit,[])
    Worm=FAI("Worm","Virus",800,400,300,250,deckworm,[])
    Spyware=FAI("Spyware","Virus",800,400,300,250,deckspyware,[])
    Vira=FAI("Vira","Antivirus",3500,1750,450,550,deckvira,[])
    CodeRed=FAI("Code Red","Virus",4000,2000,500,500,deckred,[])
    Sephiroth=FAI("Sephiroth","Virus",4000,2000,500,500,decksephiroth,[])
    Melissa=FAI("Melissa","Virus",2000,1000,500,500,deckmelissa,[])
    Ave=FAI("Ave","Antivirus",3000,1500,550,440,deckave,[])


    # Vira=FAI("Vira","Antivirus",4000,deckvira)
default EnmySts = []
default PlayerSts = []
default Enmyname = "Trojan Horse"
