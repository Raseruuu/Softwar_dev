transform gravity(groundpos):
    ease 0.9 ypos (groundpos)
init python:    
    field=[
        ["0000000000000000000000000000000000000000000000000"],
        ["0000000000000000000000000000000000011110000000000"],
        ["0000000000000000000000000001111000000000000000001"],
        ["00000p0000011110000000000000000000000000000111111"],
        ["1111111111111111000000111000000000111111111111111"],
        ["1111111111111111111111111111111111111111111111111"],    
    ]

# screen platformfield():



init python:

    class PlatformerDisplayable(renpy.Displayable):

        def __init__(self):

            renpy.Displayable.__init__(self)
