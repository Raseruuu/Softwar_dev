
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
        def __init__(self,NAME,DESC,MAG,FXN,COST,TYPE="Plugin"):
            self.NAME = NAME
            self.DESC = DESC
            self.MAG = MAG
            self.FXN = FXN
            self.COST = COST
            self.TYPE = TYPE
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
    #     def __init__(self,name,POWR,SPD,fxn,rank):
    #         self.name=name
    #         # self.type =
    #         self.POWR = POWR
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
    def Evade(quantity=1):
        tokenname="Evade"
        return Fxn(
            "Evade",
            "evade("+str(quantity)+")",
            "Gain "+str(quantity)+" \"Evade\" token(s). This will allow you to evade Attack() functions.",
            [tokenname,quantity])
    def GainToken(tokenname,quantity=1):
        return Fxn(
            "GainToken",
            "gainToken(\""+str(tokenname)+"\","+str(quantity)+")",
            "Gain "+str(quantity)+" \""+str(tokenname)+"\" token(s).",
            [tokenname,quantity])
    def GiveToken(tokenname,quantity=1):
        return Fxn(
            "GiveToken",
            "giveToken(\""+str(tokenname)+"\","+str(quantity)+")",
            "Give a \""+str(tokenname)+"\" token(s).",
            [tokenname,quantity])
    def Advance(quantity=1):
        return Fxn(
            "Advance",
            "advance("+str(quantity)+")",
            "Decrease distance by "+str(quantity)+".",
            [quantity])
    def Retreat(quantity=1):
        return Fxn(
            "Retreat",
            "retreat("+str(quantity)+")",
            "Increase distance by "+str(quantity)+".",
            [quantity])
    def Push(quantity=1):
        return Fxn(
            "Push",
            "push("+str(quantity)+")",
            "Push the enemy away!\nIncrease distance by "+str(quantity)+".",
            [quantity])

    def ReduceBit(quantity=1):
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
            "For",
            "for("+str(condition)+"):\n  "+str(function1)+codepart2,
            "Execute enclosed functions for each item in list",
            (iterations,fxns)
            )

    def IfFunction(condition,token_name,target,fxns):
        function1=fxns[0].code
        codepart2=""
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
            "Apply Freeze status to target, \nFreeze token negates the execution of a card function.")
    # def Attack():
    #     return Fxn(
    #         "Attack",
    #         "attack(ATK*POWR)",
    #         "Deal Damage to target.")
    def Attack(multiplier="POWR",rangevalue=1,absolute=False):
        return Fxn(
            "Attack",
            ("attack(ATK*"+str(multiplier)+",range="+str(rangevalue)+")" if not absolute else "attack("+str(multiplier)+",range="+str(rangevalue)+")"),
            "Deal damage to the target. Hits within the range of "+str(rangevalue)+".",
            [multiplier,rangevalue,absolute]
            )
    
    def AttackSP(multiplier="POWR",rangevalue=1,absolute=False):
        return Fxn(
            "AttackSP",
            ("attackSP(ATK*"+str(multiplier)+",range="+str(rangevalue)+")" if not absolute else "attackSP("+str(multiplier)+",range="+str(rangevalue)+")"),
            "Deal Damage to target's Shield Points only.Hits within the range of "+str(rangevalue)+"",
            [multiplier,rangevalue,absolute]
            )
    def Defend(multiplier="POWR",absolute=False):
        return Fxn(
            "Defend",
            "defend(DEF*"+str(multiplier)+")",
            "Gain Shield Points.",
            [multiplier,absolute]
            )
    
    def ReduceSPself(multiplier="POWR",absolute=False):
        return Fxn(
            "ReduceSPself",
            ("reduceSPself(DEF*"+str(multiplier)+")"),
            "Reduce Shield Points.",
            [multiplier,absolute]
            )
    def DeckChange(deckName):
        return Fxn(
            "DeckChange",
            "deckChange(\""+deckName+"\")",
            "Changes the current battleware deck.",
            deckName
            )
    def Recover(MAG):
        return Fxn(
            "Recover",
            "recover(MAXHP*POWR)",
            "Recover (MAXHP*POWR) HP.",
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
    ##name              name                     TYPE               POWR        FXN List                      COST
    FlameSaber=    Card("FlameSaber",           "FireSword",        1.75,    [Attack(),GiveToken("Burn",3),GainToken("Saber",1) ],                   0)
    MailSaberPlus=    Card("MailSaberPlus",     "MailSword",  0.5,    [While("\"Email\" in Target_status","Email","Enemy",[RemoveToken("Email","Enemy"),Attack()]),GainToken("Saber",1)],                   0)
    FlameDrill=    Card("FlameDrill",           "FireDrill",        0.25,    [ForInRange("x in range(0,8)",8,[Attack()]),Burn(20)],                   0)
    FrostBuster=   Card("FrostBuster",          "IceGun",           1.75,    [Attack(),Freeze()],                   0)
    Waveslash=     Card("Waveslash",            "SwordWave",        1.75,    [Attack(),NullFxn()],                  0)
    WindSaber=     Card("WindSaber",            "WindSword",        1.0,    [Attack(),ForInRange("x in range(0,3)",3,[Push(),Attack(0.15,rangevalue=4)]),],                  0)
    GUNVAR=        Card("Virtual Mobile Armor GUNVAR",   "GUNVAR",  3.0,     [Defend(),Attack()],   0)
    # GUNVAR=        Card("Virtual Mobile Armor GUNVAR",   "GUNVAR",  3.0,     [ForInRange("x in range(0,7)",enemyHP,[Boost("ATK",0.25),Boost("DEF",0.25)]),Attack(),],   0)

    # GUNVAR=        Card("Mobile Suit GUNVAR",   "GUNVAR",           1.0,     [Attack(),NullFxn()],   0)
    Concatenations=[FlameSaber,FlameDrill,FrostBuster,Waveslash,WindSaber,GUNVAR]
    Concat_strings=[concat.TYPE for concat in Concatenations]

#ILY's cards
    # FourAtk=      Card("DataSaber",         "Mail",           0.1,   [Attack(),Attack(),Attack(),Attack()],    2)
    Eraser=        Card("Eraser",           "Eraser",          1.0,     [ForInRange("x in range(0,target.HP)",7,[Attack(1,absolute=True),])],   8)
    SpamAtk=       Card("SpamAtk",          "Mail",           0.1,      [Attack(rangevalue=7),GiveToken("Email",3)],    2 )
    MailSaber=     Card("MailSaber",        "Sword",          0.25,     [While("\"Email\" in Target_status","Email","Enemy",[RemoveToken("Email","Enemy"),Attack()]),NullFxn()],   4)
    RecursiveSlash=Card("RecursiveSlash",   "Sword",          0.5,      [While("\"Saber\" in Self_Status","Saber","Self",[RemoveToken("Saber","Self"),Attack()]),NullFxn()],   4)
    SaberAura=     Card("SaberAura",        "Sword",          0.5,   [While("\"Saber\" in Self_Status","Saber","Self",[RemoveToken("Saber","Self"),Boost("ATK",0.25)]),NullFxn()],   8)
    HeartBurn=     Card("HeartBurn",        "PowerUp",        0.2,    [Boost("ATK",0.25),GainToken("Burn",1)],       2)
    ChocolateBar=  Card("ChocolateBar",     "Chocolate",      0.25,    [Recover(0.25),NullFxn()],          2)

#Ave's cards    
    FiberBuster=   Card("FiberBuster",      "Gun",            0.75,     [Attack(rangevalue=7,)],              4)
    DataBuster=    Card("DataBuster",       "Gun",            0.75,     [Attack(rangevalue=7)],              3)
    SparkBuster=   Card("SparkBuster",      "Gun",            0.25,      [Attack(rangevalue=7)],           2)
    Snipe=         Card("Snipe",            "Gun",            0.0,      [Boost("ATK",0.25),Retreat(2)],       6)
#Swords and Blades  
    FiberSword=    Card("FiberSword",      "Sword",           0.5,     [GainToken("Saber",1),Advance(4),Attack()], 3)
    DataSaber=     Card("DataSaber",        "Sword",           1.0,      [Attack(),Defend(0.25),GainToken("Saber",1),],   4)
    
    Katana=        Card("Katana",           "Sword",           0.7,      [Attack(),GainToken("Saber",3)],   4)
    BreakSaber=    Card("BreakSaber",       "Sword",           0.5,      [AttackSP(),Attack(),GainToken("Saber",1)],  3)
    BlockSaber=    Card("BlockSaber",       "Sword",           0.25,     [Attack(),Defend(0.75),GainToken("Saber",1)],    4)
    LambdaSaber=   Card("LambdaSaber",      "Sword",           0.2,     [ForInRange("x in range(0,3)",3,[Attack(),Attack(0.1,rangevalue=7)]),GainToken("Saber",1)], 4)
    StepSaber=     Card("StepSaber",        "Sword",           0.5,     [Advance(2),Attack()], 5)
    
    XAxess=        Card("X-Axess",          "X",               0.75,     [AttackSP(),Attack()],            4)
    YAxess=        Card("Y-Axess",          "Y",               0.50,     [AttackSP(),Attack()],            3)
    DataMining=    Card("DataMining",       "Mining",          0.50,     [Attack(),GainToken("Data",1)],            3)

    DataPiercer=   Card("DataPiercer",      "Spear",           1.0,      [Attack(),Defend(0.25)],   5)
    WindBlast=     Card("WindBlast",        "Wind",            0.4,      [Attack(rangevalue=2),Push(2)],   3)
    
    #ZAxess=       Card("Z-Axess",        "Z",      0.25,     [DamageSP,Damage],        1)
# Evasion cards
    BurstTransfer=      Card("BurstTransfer",         "Maneuver",      0.0,   [Evade(1), IfFunction("\"Data\" in Self_Status","Data","Self",[RemoveToken("Data","Self"),Evade(1)])],          2)
    BurstTransferTurbo= Card("BurstTransferTurbo",    "Maneuver",      0.0,   [Evade(1), IfFunction("\"Data\" in Self_Status","Data","Self",[RemoveToken("Data","Self"),Evade(1)])],          2)
    
#SaberSkills 
    SaberDeflect=  Card("SaberDeflect",     "SaberSkill",        0.75,     [IfFunction("\"Saber\" in Self_Status","Saber","Self",[RemoveToken("Saber","Self"),Defend()]),NullFxn()],   1)
    MomentumSlash= Card("MomentumSlash",    "SaberSkill",        0.75,     [IfFunction("\"Saber\" in Self_Status","Saber","Self",[RemoveToken("Saber","Self"),AttackSP()]),NullFxn()],   1)
    SkullCrush=  Card("SkullCrush",       "SaberSkill",        0.75,     [IfFunction("\"Saber\" in Self_Status","Saber","Self",[RemoveToken("Saber","Self"),Defend()]),NullFxn()],   1)
    MomentumSlash= Card("MomentumSlash",    "SaberSkill",        0.75,     [IfFunction("\"Saber\" in Self_Status","Saber","Self",[RemoveToken("Saber","Self"),AttackSP()]),NullFxn()],   1)
#Hammer 
    ImpactHammer = Card("ImpactHammer",     "Hammer",       0.50,     [Attack(rangevalue=1),Push(3)],            3)
# Virus Exclusive
    Vshot=         Card("V-Shot",           "Gun",          0.6,         [Attack(rangevalue=7),NullFxn()],           3)
    VirusFlame=    Card("V-Flame",          "Fire",         0.5,         [Attack(rangevalue=4),Burn(20)],               3)
    Vslash=        Card("V-Slash",          "Slash",        0.5,         [Attack(),NullFxn()],              2)
    VBlaze=        Card("VBlaze",           "Fire",           1.0,     [Attack(),Burn(40)],   4)
    WormHole=      Card("WormHole",         "Hole",           1.0,     [ReduceSPself(0.15),GainToken("Hole",1),Evade(1)],   1)
    WormBite=      Card("WormBite",         "Hole",           1.0,   [IfFunction("\"Hole\" in Self_Status","Hole","Self",[RemoveToken("Hole","Self"),Advance(2)]),Attack()],   4)
    WormRetreat=    Card("WormRetreat",      "Hole",         0.0,     [IfFunction("\"Hole\" in Self_Status","Hole","Self",[RemoveToken("Hole","Self"),Retreat(3)])],   3)
    WormAdvance=    Card("WormAdvance",      "Hole",         0.0,     [IfFunction("\"Hole\" in Self_Status","Hole","Self",[RemoveToken("Hole","Self"),Advance(3)]),Advance()],   1)

#Antivirus Exclusive
    Firewall=     Card("Firewall",       "Wall",    0.75,    [Defend(),Boost("DEF",0.25)],      4)
    FixerBeam=    Card("FixerBeam",       "Beam",    0.75,    [Recover(0.5),IfFunction("\"Data\" in Self_Status","Data","Self",[RemoveToken("Data","Self"),Recover(0.5)])],      4)
    Scan=           Card("Scan",       "Scan",    0.5,         [Defend(),Boost("DEF",0.25)],      4)
    
#Bombs
    DataBomb=     Card("DataBomb",       "Bomb",     1.0,     [Retreat(),Attack(rangevalue=5)],          4)
    Flashbang=    Card("Flashbang",      "Bomb",     0.0,     [Retreat(),Attack(rangevalue=5)],          3)
#Force
    BruteForce=   Card("BruteForce",     "Force",    0.20,     [While("\"BoostATK\" in Self_Status","BoostATK","Self",[Attack()]),Boost("ATK",0.25)],      6)
    DataForce=    Card("DataForce",      "Force",    0.25,      [Boost("ATK",0.25),Boost("DEF",0.25),IfFunction("\"Data\" in Self_Status","Data","Self",[Recover(0.5)])],       4)
   
    Tackle=       Card("Tackle",      "Maneuver",        0.3,     [Advance(2),Attack()], 2)
    
    DataDrill=    Card("DataDrill",       "Drill",   0.5,     [ForInRange("x in range(0,3)",3,[Attack()]) ,GainToken("Data",1)],       5)
    Powersol=     Card("Powersol",        "Wall",    1.0,     [Defend(),Boost("ATK",0.25)],        4)
    Shieldbit=    Card("Shieldbit",       "Shield",    0.25,     [Defend(),NullFxn()],          1)
    RadioShield=  Card("RadioShield",       "Shield",    0.25,     [Defend(),NullFxn()],          1)
    Assault=      Card("Assault",       "Tech",    0.25,       [Advance(),Boost("ATK",0.25)],  2)
    Snipe=        Card("Snipe",           "Gun",    0.0,     [Retreat(2),Boost("ATK",0.25)],       6)
    Laserbeam=    Card("Laserbeam",       "Gun",    2.0,      [Attack(rangevalue=20),NullFxn()],          8)
    Cursorclaw=   Card("Cursorclaw",      "Claw",    0.5,   [Attack(),NullFxn()],           2)
    #newcards
    DrainShield=   Card("DrainShield",    "Shield",      1.0,     [Defend(),GainToken("Negate",1)],   4)
    FieryArc=      Card("FieryArc",       "Bow",         1.0,     [Attack(),GiveToken("Burn",1)],   4)
    CosmicArc=     Card("CosmicArc",      "Bow",         1.0,     [Attack(),GainToken("Saber",1)],   4)
    # SnipeSensor=   Card("SnipeSensor",    "Sword",           1.0,     [Attack(),GainToken("Saber",1)],   4)
    LunexGunSaber= Card("LunexGunSaber",  "Gun",       1.0,     [Attack(rangevalue=7),GiveToken("Saber",1)],   4)
    BusterSword=   Card("BusterSword",  "Sword",         1.0,     [Attack(),GiveToken("Saber",1)],   4)
    CupidArc=      Card("CupidArc",       "Bow",         1.0,     [Attack(),GainToken("Saber",1)],   4)
    DataArc=       Card("DataArc",       "Bow",          1.0,     [Attack(),GainToken("Saber",1)],   4)
    Flashbang=     Card("Flashbang",      "Bomb",        1.0,     [Attack(),GainToken("Saber",1)],   4)
    Gigamorph=     Card("Gigamorph",      "Power",       1.0,     [Attack(),GainToken("Saber",1)],   4)
    # DataBuster=    Card("DataBuster",      "Gun",        1.0,     [Attack(),GainToken("Saber",1)],   4)
    Bitbuster=     Card("Bitbuster",      "Gun",         0.5,     [Attack(rangevalue=7),ReduceBit(1)],   4)
    MachineBuster= Card("MachineBuster",      "Gun",     1.0,     [Attack(),GainToken("Saber",1)],   4)
    Excalibrium=   Card("Excalibrium",      "Sword",     1.0,     [Attack(),GainToken("Saber",1)],   4)
    ILYFlash=      Card("ILYFlash",      "Power",        1.0,     [Attack(),GainToken("Saber",1)],   4)
    BruiseBash=    Card("BruiseBash",      "Skill",      1.0,     [Attack(),GiveToken("DEFdown",1)],   4)
    ZSlash=        Card("ZSlash",          "Slash",      1.0,     [Attack(),GainToken("Saber",1)],   4)
    FreezeWave=    Card("FreezeWave",      "Wave",       1.0,     [Attack(),Freeze()],   4)
    FreezingBlade= Card("FreezingBlade",   "Sword",      1.0,     [Attack(),Freeze()],   4)
    Salamandra=    Card("Salamandra",      "Sword",      1.0,     [Attack(),GainToken("Saber",1)],   4)
    FlameFists=    Card("FlameFists",      "Fist",       1.0,     [Attack(),GainToken("Saber",1)],   4) 
    GearframeUnitron= Card("GU-Gearframe Unitron","GU",  1.0,     [Advance(3),NullFxn()],   2)
    NucleusVernier=  Card("NV-Nucleus Vernier", "NV",    1.0,     [Advance(1),Boost("ATK",0.25)],   2)
    AccelRiser=      Card("AR-Accel Riser","AR",         1.0,     [Retreat(2),Evade()],   4)
    GUNVARSaber=     Card("GUNVARSaber","GUNVAR",  2.3,         [Attack(rangevalue=2)],   8)
    GUNVARFist=      Card("GUNVARFist","GUNVAR",  2.1,         [Attack(rangevalue=2)],   8)
    GUNVARKick=      Card("GUNVARKick","GUNVAR",  2.2,         [Attack(rangevalue=2)],   8)
    GUNVARBeam=      Card("GUNVARBeam","GUNVAR",  2.5,     [Attack(rangevalue=6)],   8)
    GUNVARShield=    Card("GUNVARShield","GUNVAR",  2.0,         [Defend()],   4)
    Shotgun=         ("Shotgun",      "Gun",           1.0,     [Attack(),GainToken("Saber",1)],   4)
    SwordOfTruth =   Card("SwordOfTruth",      "Sword",           1.0,     [Attack(),GainToken("Saber",1)],   4)
    SwordOfLies=     Card("SwordOfLies",      "Sword",           1.0,     [Attack(),GainToken("Saber",1)],   4)
    

    # Library
    CardLibrary = [
        DataArc,
        DataSaber,
        Shotgun

    ]

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
######################
#####Plugins:#########
######################
    FirstBarrier=Plugin("First Barrier", "Initial Defense!",0.5, [Defend()],4)
    RubyRevolver=Plugin("Ruby Revolver", "ILY's magical spinning bracelet!",0.25, [GainToken("Saber",1),GiveToken("Email",1)],4)
    Analysis=Plugin("Analysis", "Examine the target.",0.25, [GainToken("Data",1),Evade()],4)
    SpiderAmulet=Plugin("Spider Amulet", "Why a spider? Because it looks cute!",0.25, [Boost("ATK",0.1)],4)
    MoonlitAmulet=Plugin("Moonlit Amulet", "Yami's fancy moon-shaped necklace!",0.25, [Boost("ATK",0.1)],4)
    DigitalPressure=Plugin("Digital Pressure","Let your power overflow!!",0.2,[Attack(rangevalue=10)], 4)
    SnipeSensor=Plugin("SnipeSensor","!",1.0,[Attack()], 8)
    SuperArmor=Plugin("SuperArmor", "Initial Defense!",0.25, [Boost("DEF",0.25),Defend()],4)
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
            ChocolateBar,ChocolateBar,
            DataSaber,DataSaber,
            DataSaber,MailSaber,
            VirusFlame,RecursiveSlash,
            BlockSaber,SaberDeflect,
            DataSaber,BlockSaber,
            HeartBurn,HeartBurn,
            # GearframeUnitron,GearframeUnitron,
            # GearframeUnitron,GearframeUnitron,
            # NucleusVernier,NucleusVernier,
            # NucleusVernier,NucleusVernier,
            # AccelRiser,AccelRiser,
            # AccelRiser,AccelRiser

            ],
        "plugins":[RubyRevolver,FirstBarrier]
        }
   
    deckalpha = {
        "name":"Deceitful Love",
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
        "name":"Avaricious Anomaly",
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
        "name":"Gift of Invasion",
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
            Vshot,Vshot,
            Tackle,Tackle,
            Tackle,Tackle
            ],
        "plugins":[]
        }

    deckkeylogger ={
        "name":"Password Uncovered",
        "content":[
            VirusFlame,VirusFlame,
            VirusFlame,DataBuster,
            DataBuster,DataBuster,
            DataForce,Vslash,
            DataBomb,Cursorclaw,
            Cursorclaw,Cursorclaw,
            Vslash,Vslash,
            Vslash,Vslash,
            Vshot,Vshot,
            Vshot,Vshot,
            DataMining,DataMining,
            DataMining,DataDrill
        
            ],
        "plugins":[]
        }
    deckransomware = {
        "name":"Give Zenny",
        "content":[
            VirusFlame,VirusFlame,
            VirusFlame,DataBuster,
            DataBuster,DataBuster,
            Vslash,Vslash,
            Vslash,Vslash,
            Vshot,Vshot,
            Vshot,Vshot,
            Cursorclaw,Cursorclaw,
            DataMining,DataMining,
            Tackle,Tackle,
            DataMining,DataDrill,
            Tackle,Tackle
            ],
        "plugins":[]
        }
    deckrootkit = {
        "name":"Digging Deep",
        "content":[
            Vshot,Vshot,
            DataMining,DataMining,
            Vslash,Vslash,
            DataDrill,DataDrill,
            Tackle,Tackle,
            Tackle,Tackle,
            BurstTransfer,BurstTransfer,
            Assault,Assault,
            BruteForce,BruteForce,
            BruteForce,BruteForce,
            DataDrill,DataDrill,
            DataMining,DataMining
            ],
        "plugins":[]
        }
    deckworm = {
        "name":"A Hole lot of Trouble",
        "content":[
            WormBite,Vshot,
            Vslash,VirusFlame,
            VirusFlame,VirusFlame,
            WormRetreat,WormAdvance,
            WormBite,WormBite,
            WormAdvance,WormAdvance,
            WormHole,WormHole,
            WormHole,WormHole,
            WormRetreat,WormRetreat,
            WormRetreat,WormBite],
        "plugins":[]
        }
    deckspyware = {
        "name":"With My Little Eye",
        "content":[
            Laserbeam,BurstTransfer,
            BurstTransfer,BurstTransfer,
            BurstTransfer,Vslash,
            Vslash,Vslash,
            Tackle,Tackle,
            Tackle,Tackle,
            DataBomb,WindBlast,
            Vslash,WindBlast,
            Vshot,Vshot,
            Vshot,Vshot],
        "plugins":[]
        }
    decknibbler = {
        "name":"What's Up",
        "content":[
            Vshot,Vshot,
            Vshot,Vshot,
            Vslash,Vslash,
            Vslash,Vslash,
            Vslash,Vslash,
            Vshot,Vshot,
            Vslash,WindBlast,
            Vslash,WindBlast,
            Vshot,Vshot,
            Vshot,Vshot],
        "plugins":[]
        }
    deckvira = {
        "name":"I'll Save You!",
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
        "name":"The Ultimate Antivirus",
        "content":[
            DataBuster,BurstTransfer,
            DataBuster,DataBuster,
            DataBuster,Firewall,
            Firewall,DataForce,
            Firewall,Firewall,
            DataBomb,DataBomb,
            Laserbeam,DataForce,
            Shieldbit,Shieldbit,
            FixerBeam,Bitbuster,
            Bitbuster,DataMining,
            DataMining,FixerBeam,
            Assault,Assault],
        "plugins":[FirstBarrier,Analysis]
        }
    deckred = {
        "name":"Wave Sword Arts",
        "content":[
            DataSaber,DataSaber,
            DataSaber,DataSaber,
            LambdaSaber,LambdaSaber,
            BlockSaber,BlockSaber,
            BlockSaber,VirusFlame,
            BreakSaber,BreakSaber,
            SaberAura,SaberAura,
            WormRetreat,WormHole,
            BurstTransfer,DataBomb,
            DataDrill,WindBlast,
            DataDrill,WindBlast,
            DataForce,DataForce
            ],
        "plugins":[DigitalPressure,SuperArmor]
        }
    # decksephiroth = {
    #     "name":"",
    #     "content":[
    #         DataSaber,DataSaber,
    #         DataSaber,DataSaber,
    #         DataSaber,VirusFlame,
    #         BlockSaber,BlockSaber,
    #         Katana,Katana,
    #         Katana,Katana,
    #         BlockSaber,BlockSaber,
    #         BlockSaber,DataForce,
    #         DataForce,DataForce],
    #     "plugins":[]
    #     }
    deckGUNVAR = {
        "name":"Mechanical Hero",
        "content":[
            GUNVARBeam,GUNVARBeam,
            GUNVARFist,GUNVARFist,
            GUNVARFist,GUNVARFist,
            GUNVARKick,GUNVARKick,
            GUNVARKick,GUNVARKick,
            GUNVARSaber,GUNVARSaber,
            GUNVARSaber,GUNVARSaber,
            GUNVARShield,GUNVARShield,
            GUNVARShield,GUNVARShield],
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

    # BASE STATS
    #DEFINE CHARACTERS BY
            # NAME,TYPE,HP,SP,ATK,DEF,DECK,STATUS
    ILY=FAI("ILY","Virus",2500,2500,500,500,deckdefault,[])
    ILYAlpha=FAI("ILY_Alpha","Virus",2500,2500,500,500,deckalpha,[])
    
    Trojan=     FAI("TrojanHorse",  "Virus",2000,   2000,   400,    250,    decktrojan,[])
    Keylogger=  FAI("Keylogger",    "Virus",600,    600,    300,    250,    deckkeylogger,[])
    Ransomware= FAI("Ransomware",   "Virus",1600,    600,    300,    250,    deckransomware,[])
    Rootkit=    FAI("Rootkit",      "Virus",1500,    700,    300,    250,    deckrootkit,[])
    Worm=       FAI("Worm",         "Virus",1000,    800,    300,    250,    deckworm,[])
    Spyware=    FAI("Spyware",      "Virus",800,    800,    300,    250,    deckspyware,[])
    Nibbler=    FAI("Nibbler",      "Virus",800,    800,    300,    250,    decknibbler,[])
    
    
    
    Vira=FAI("Vira","Antivirus",3500,3500,450,550,deckvira,[])
    CodeRed=FAI("Code Red","Virus",4000,4000,450,550,deckred,[])
    Bitwulf=FAI("Bitwulf","Antivirus",4000,4000,500,500,deckred,[])
    # Sephiroth=FAI("Sephiroth","Virus",4000,4000,500,500,decksephiroth,[])
    Melissa=FAI("Melissa","Virus",3200,3200,400,400,deckmelissa,[])
    Ave=FAI("Ave","Antivirus",3000,3000,550,450,deckave,[])


    # Vira=FAI("Vira","Antivirus",4000,deckvira)
default EnmySts = []
default PlayerSts = []
default Enmyname = "TrojanHorse"

#  Concatenations
#     Concat_strings 
#     Eraser
#     SpamAtk
#     MailSaberPlus 
#      Number: 00001
#      Rarity: N, R, SR, and UR 
#      Color:
#             Red=Offensive
#             Blue=Defensive
#             Green= Support
define card_library={
    "Vshot"           : {"card":Vshot           ,"ID":'001',"rarity": "N","color":"red","compatibility":"virus"},
    "Vslash"          : {"card":Vslash          ,"ID":'001',"rarity": "N","color":"red","compatibility":"virus"},
    "VirusFlame"      : {"card":VirusFlame      ,"ID":'001',"rarity": "N","color":"red","compatibility":"virus"},
    "VBlaze"          : {"card":VBlaze          ,"ID":'001',"rarity": "N","color":"red","compatibility":"virus"},
    "DataSaber"       : {"card":DataSaber       ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "DataBuster"      : {"card":DataBuster      ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "BreakSaber"      : {"card":BreakSaber      ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "DataDrill"       : {"card":DataDrill       ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "DataBomb"        : {"card":DataBomb        ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "DataForce"       : {"card":DataForce       ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "DataArc"         : {"card":DataArc         ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "BlockSaber"      : {"card":BlockSaber      ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "LambdaSaber"     : {"card":LambdaSaber     ,"ID":'001',"rarity":"SR","color":"red","compatibility":"basic"},
    "RecursiveSlash"  : {"card":RecursiveSlash  ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "SaberAura"       : {"card":SaberAura       ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "BruteForce"      : {"card":BruteForce      ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "FiberBuster"     : {"card":FiberBuster     ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "SparkBuster"     : {"card":SparkBuster     ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "HeartBurn"       : {"card":HeartBurn       ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "ChocolateBar"    : {"card":ChocolateBar    ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "Snipe"           : {"card":Snipe           ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "Katana"          : {"card":Katana          ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "XAxess"          : {"card":XAxess          ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "YAxess"          : {"card":YAxess          ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "BurstTransfer"   : {"card":BurstTransfer   ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "SaberDeflect"    : {"card":SaberDeflect    ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "MomentumSlash"   : {"card":MomentumSlash   ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "SkullCrush"      : {"card":SkullCrush      ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "ImpactHammer"    : {"card":ImpactHammer    ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "Firewall"        : {"card":Firewall        ,"ID":'001',"rarity": "R","color":"red","compatibility":"antivirus"},
    "FixerBeam"       : {"card":FixerBeam       ,"ID":'001',"rarity": "R","color":"red","compatibility":"antivirus"},
    "Flashbang"       : {"card":Flashbang       ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "Powersol"        : {"card":Powersol        ,"ID":'001',"rarity":"UR","color":"red","compatibility":"antivirus"},
    "Shieldbit"       : {"card":Shieldbit       ,"ID":'001',"rarity": "N","color":"red","compatibility":"basic"},
    "RadioShield"     : {"card":RadioShield     ,"ID":'001',"rarity": "N","color":"red","compatibility":"basic"},
    "Assault"         : {"card":Assault         ,"ID":'001',"rarity": "N","color":"red","compatibility":"basic"},
    "Laserbeam"       : {"card":Laserbeam       ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "Cursorclaw"      : {"card":Cursorclaw      ,"ID":'001',"rarity": "N","color":"red","compatibility":"basic"},
    "DrainShield"     : {"card":DrainShield     ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "FieryArc"        : {"card":FieryArc        ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "CosmicArc"       : {"card":CosmicArc       ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "LunexGunSaber"   : {"card":LunexGunSaber   ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "BusterSword"     : {"card":BusterSword     ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "CupidArc"        : {"card":CupidArc        ,"ID":'001',"rarity":"SR","color":"red","compatibility":"basic"},
    "Gigamorph"       : {"card":Gigamorph       ,"ID":'001',"rarity":"UR","color":"red","compatibility":"basic"},
    "Bitbuster"       : {"card":Bitbuster       ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "MachineBuster"   : {"card":MachineBuster   ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "Excalibrium"     : {"card":Excalibrium     ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "ILYFlash"        : {"card":ILYFlash        ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "BruiseBash"      : {"card":BruiseBash      ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "ZSlash"          : {"card":ZSlash          ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "FreezeWave"      : {"card":FreezeWave      ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "FreezingBlade"   : {"card":FreezingBlade   ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "Salamandra"      : {"card":Salamandra      ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "FlameFists"      : {"card":FlameFists      ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "GearframeUnitron": {"card":GearframeUnitron,"ID":'001',"rarity":"UR","color":"red","compatibility":"basic"},
    "NucleusVernier"  : {"card":NucleusVernier  ,"ID":'001',"rarity":"UR","color":"red","compatibility":"basic"},
    "AccelRiser"      : {"card":AccelRiser      ,"ID":'001',"rarity":"UR","color":"red","compatibility":"basic"},
    "GUNVARSaber"     : {"card":GUNVARSaber     ,"ID":'001',"rarity":"UR","color":"red","compatibility":"basic"},
    "GUNVARFist"      : {"card":GUNVARFist      ,"ID":'001',"rarity":"UR","color":"red","compatibility":"basic"},
    "GUNVARKick"      : {"card":GUNVARKick      ,"ID":'001',"rarity":"UR","color":"red","compatibility":"basic"},
    "GUNVARBeam"      : {"card":GUNVARBeam      ,"ID":'001',"rarity":"UR","color":"red","compatibility":"basic"},
    "GUNVARShield"    : {"card":GUNVARShield    ,"ID":'001',"rarity":"UR","color":"red","compatibility":"basic"},
    "Shotgun"         : {"card":Shotgun         ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "SwordOfTruth"    : {"card":SwordOfTruth    ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"},
    "SwordOfLies"     : {"card":SwordOfLies     ,"ID":'001',"rarity": "R","color":"red","compatibility":"basic"}
}
