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
    Melissasprite2 = SpriteinMap("Melissa",[5,3],'down',"Melissa")
    Stellasprite = SpriteinMap("Stella",[3,1],'down',"Stella")
    Programkunsprite = SpriteinMap("ProgramKun",[8,5],'down',"Program-kun")
    Bellasprite = SpriteinMap("Bella",[9,5],'down',"Bella")

    Chapter2events=EventInMap("storyevent",[
       [2,4], [3,4], [4,4], [5,4], [6,4], [7,4], [8,4],
       [2,10],[3,10],[4,10],[5,10],[6,10],[7,10],[8,10],
       [8,9],[8,8],[8,7],[8,6],[8,5]
       ],"prescript2")
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
        if gridplace in mapspritesdict:
            for key in mapspritesdict:
                if gridplace == key:
                    for sprite in mapspritesdict[gridplace]:
                        spritelist.append(sprite)
        if gridplace in mapeventsdict:
            for key in mapeventsdict:
                if gridplace == key:
                    for event in mapeventsdict[gridplace]:
                        eventlist.append(event)
        # else:
            #     spritelist = []
                #





    return
