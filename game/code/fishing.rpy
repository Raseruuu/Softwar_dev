###Fishing
"""
    (N- Normal ):
        Zander
        Carp
        Salmon
        Goldfish    
    (R- Rare ):
        Catfish
        Eel
        Tuna    
    (SR - Super Rare ):
        Shark
        Sun fish 
        Flying Fish 
    (UR - Ultra Rare Raity) 
        Gold fish (actual gold)
        Blobfish :)
        Leviathan
"""
init python:
    class Water_body:
        def __init__(self,name,contents,where):
            self.name=name
            self.contents=contents
            self.where=where 
    class Fish:
        def __init__(self,name,rarity):
            self.name=name
            self.rarity=rarity

    
label fishingstart(fishinglocation="beach"):
    
    ""
