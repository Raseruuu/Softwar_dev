init -3 python:
    class SpriteinMap:
        def __init__(self,name,position,direction,dialogue):
            self.name=name
            self.position = position
            self.direction = direction
            self.dialogue = dialogue
    class EventInMap:
        def __init__(self,type,positionlist,label):
            self.type=type
            self.positionlist = positionlist
            self.label = label
    Avesprite = SpriteinMap("Ave",[5,3],'down',"Ave")
    Heartsprite = SpriteinMap("Heart",[7,5],'down',"Heart")
    CodeRedsprite = SpriteinMap("CodeRed",[7,3],'down',"CodeRed")
    Virasprite = SpriteinMap("Vira",[3,3],'down',"Vira")
    Melissasprite = SpriteinMap("Melissa",[5,3],'down',"Melissa")
    Bitwulf_C2 = SpriteinMap("Bitwulf",[2,7],'right',"Bitwulf")
    Melissasprite2 = SpriteinMap("Melissa",[5,3],'down',"Melissa2")
    Stellasprite = SpriteinMap("Stella",[3,1],'down',"Stella")
    Programkunsprite = SpriteinMap("ProgramKun",[8,5],'down',"Program-kun")
    Bellasprite = SpriteinMap("Bella",[8,4],'down',"Bella")
    Chapter2unlockdoor = EventInMap("storyevent",[[4,2]],"a")

    Chapter1events=EventInMap("storyevent",[
       [2,4], [3,4], [4,4], [5,4], [6,4], [7,4], [8,4],
       [2,10],[3,10],[4,10],[5,10],[6,10],[7,10],[8,10],
       [8,9],[8,8],[8,7],[8,6],[8,5]
       ],"script2")
    Chapter2events=EventInMap("storyevent",[
       [2,4], [3,4], [4,4], [5,4], [6,4], [7,4], [8,4],
       [2,10],[3,10],[4,10],[5,10],[6,10],[7,10],[8,10],
       [8,9],[8,8],[8,7],[8,6],[8,5]
       ],"script3")
default spritelist = []
default eventlist = []


label chapter_map_events:
    if chapternum==2:
        "stuff"
    return
label addsprites(gridplace):
    python:
        gridplace = (gridplace[0],gridplace[1])
        if gridplace in mapwheredict:
            Where = mapwheredict[gridplace]
        else:
            Where = "Road"
        # renpy.say("",str(gridplace))
        spritelist=[]
        eventlist = []
        if gridplace in mapspritesdictdefault:
            for key in mapspritesdictdefault:
                if gridplace == key:
                    for sprite in mapspritesdictdefault[gridplace]:
                        spritelist.append(sprite)
        if gridplace in mapspritesdicts[chapternum]:
            map_dict=mapspritesdicts[chapternum]
            for key in map_dict:
                if gridplace == key:
                    for sprite in map_dict[gridplace]:
                        spritelist.append(sprite)
        if gridplace in mapeventsdicts[chapternum]:
            for key in mapeventsdicts[chapternum]:
                if gridplace == key:
                    for event in mapeventsdicts[chapternum][gridplace]:
                        eventlist.append(event)
        # else:
            #     spritelist = []
                #
        Chapter2unlockdoor
    return
label mapcallquest():

    $ gridpos = [192,164]
    call addsprites(gridpos)
    call mapcall([6,5],stage_ShadyAlley)
    if playerHP<=0:
        return
    $ILY_w = False
    hide screen mapB
    hide screen mapA

    return