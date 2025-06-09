transform playerattack:
    zoom 1.0 xanchor 0.5 yanchor 0.5
    linear 0.2 zoom 1.2 xpos (tarx+origx)/2 ypos (tary+origy)/2
    linear 0.2 zoom 1.0 xpos (tarx+origx)/2 ypos tary+((origy-tary)/2)
    linear 0.2 zoom 1.0 xpos origx ypos origy

# transform cardpos1:

transform sway:
    transform_anchor True
    linear 0.25 rotate 5
    linear 0.5 rotate -5
    linear 0.20 rotate 1
    linear 0.05 rotate 0
transform alpha05:
    alpha 0.5
transform alpha08:
    alpha 0.8
transform dright: # Smooth dissolve with motion at the extreme right, from near side
    alpha 0.0 xpos 0.9 yalign 1.0 xanchor 0.5 xzoom 1.0
    linear 0.4 alpha 1.0 xanchor 0.5 xpos 0.85
transform dright2: # Smooth dissolve with motion at the mid right, from near side
    alpha 0.0 xpos 0.7 yalign 1.0 xanchor 0.5 xzoom 1.0
    linear 0.4 alpha 1.0 xanchor 0.5 xpos 0.65


transform dleft: # Smooth dissolve with motion at the extreme left, from near side
    alpha 0.0 xpos 0.1 yalign 1.0 xanchor 0.5 xzoom -1.0
    linear 0.4 alpha 1.0 xanchor 0.5 xpos 0.15
transform dleft2: # Smooth dissolve with motion at the mid left, from near side
    alpha 0.0 xpos 0.3 yalign 1.0 xanchor 0.5 xzoom -1.0
    linear 0.4 alpha 1.0 xanchor 0.5 xpos 0.35

transform rsurprise: #surprised and moved backward while facing Right
    alpha 1.0 rotate 0 yanchor 1.0 transform_anchor True
    linear 0.05 rotate 0 transform_anchor True yzoom 1.05 yanchor 0.95 xoffset 70
    linear 0.05 rotate 5 transform_anchor True yzoom 1.1 yanchor 0.95 xoffset 75
    linear 0.2 rotate -10 transform_anchor True yzoom 1.0 yanchor .90 xoffset 100
    linear 0.5 rotate 0 transform_anchor True yanchor 1.0 xoffset .10

transform lsurprise: #surprised and moved backward while facing Left
    alpha 1.0 rotate 0 yanchor 1.0 transform_anchor True
    linear 0.03 rotate -20 transform_anchor True yzoom 1.1 yanchor 0.95 xoffset -50
    linear 0.2 rotate 10 transform_anchor True yzoom 1.0 yanchor .90 xoffset -100
    linear 0.5 rotate 0 transform_anchor True yanchor 1.0 xoffset .10


transform raffirm: #upper body nodding at right
    alpha 1.0 rotate 0 yanchor 1.0 transform_anchor True
    linear 0.25 rotate -10 yanchor 0.9 transform_anchor True yanchor .90 xoffset 50
    linear 0.3 rotate 0 yanchor 1.0 transform_anchor True yanchor 1.0 xoffset 0
    linear 0.25 rotate -10 yanchor 0.9 transform_anchor True yanchor .90 xoffset 50
    linear 0.3 rotate 0 yanchor 1.0 transform_anchor True yanchor 1.0 xoffset 0
transform laffirm: #upper body nodding at left
    alpha 1.0 rotate 0 yanchor 1.0 transform_anchor True
    linear 0.25 rotate 15 yanchor 0.9 transform_anchor True yanchor .95 xoffset -20
    linear 0.3 rotate 0 yanchor 1.0 transform_anchor True yanchor 1.0 xoffset 0
    linear 0.25 rotate 15 yanchor 0.9 transform_anchor True yanchor .95 xoffset -20
    linear 0.3 rotate 0 yanchor 1.0 transform_anchor True yanchor 1.0 xoffset 0


transform rdown: #brief lowering of body while at right
    alpha 1.0 rotate 0 yanchor 1.0 transform_anchor True
    linear 0.2 rotate -5 yanchor .95 yzoom 0.9 transform_anchor True
    linear 0.4 rotate 0 yanchor .96 yzoom 0.90  transform_anchor True
    linear 0.5 rotate 0 yanchor 1.0 yzoom 1.0  transform_anchor True
transform ldown: #brief lowering of body while at left
    alpha 1.0 rotate 0 yanchor 1.0 transform_anchor True
    linear 0.2 rotate 5 yanchor .95 yzoom 0.9 transform_anchor True
    linear 0.4 rotate 0 yanchor .96 yzoom 0.90  transform_anchor True
    linear 0.5 rotate 0 yanchor 1.0 yzoom 1.0  transform_anchor True


transform dance: #Dancing, flipping left and right
    xanchor 0.5 alpha 1.0
    xzoom 0.95 yzoom 1.02 transform_anchor True
    linear 0.2 xzoom 1.0 yzoom 1.0 transform_anchor True
    linear 0.2 xzoom 0.95 yzoom 1.02 transform_anchor True
    xzoom -0.95 yzoom 1.02 transform_anchor True
    linear 0.2 xzoom -1.0 yzoom 1.0 transform_anchor True
    linear 0.2 xzoom -0.95 yzoom 1.02 transform_anchor True
    repeat





transform boing: #here I am
    yanchor 0.0
    ypos 1.0
    xzoom 1.5
    yzoom 0.5
    linear 0.2 yanchor 1.0 yzoom 0.5 xzoom 1.5
    linear 0.2 yzoom 1.5 xzoom 0.5 yzoom 1.5
    linear 0.2 yzoom 1.0 xzoom 1.0

transform kickedaway: #whaaaaaa
    rotate 0
    zoom 0.6
    ypos 1.0
    yanchor 0.7
    parallel:
        rotate 0
        linear 0.2 rotate 360
        repeat
    parallel:
        linear 0.5 zoom 0.0
    parallel:
        linear 0.5 yalign 0.2 xpos 1.0
transform excitement: #oh my gawd, it's coming!!
    parallel:
        xzoom -1.0
        pause 0.6
        xzoom 1.0
        pause 0.6
        repeat
    parallel:
        linear 0.6 xpos 0.4
        linear 0.6 xpos 0.3
        repeat
    parallel:
        ypos 1.0
        linear 0.3 ypos 1.1
        linear 0.3 ypos 1.0
        repeat
# transform sidesteps_effect(image_path, start_pos, end_pos, duration):
#     subpixel True
#     yalign 1.0
#     contains:
#         Image(image_path)
#         xalign start_pos alpha 0.2
#         easein duration + 0.4 xalign end_pos
#     contains:
#         Image(image_path)
#         xalign start_pos alpha 0.4
#         easein duration + 0.3 xalign end_pos
#     contains:
#         Image(image_path)
#         xalign start_pos alpha 0.6
#         easein duration + 0.2 xalign end_pos
#     contains:
#         Image(image_path)
#         xalign start_pos alpha 0.8
#         easein duration + 0.1 xalign end_pos
#     contains:
#         Image(image_path)
#         xalign start_pos alpha 1
#         easein duration xalign end_pos




transform sidesteps_effect(image_path, start_pos, end_pos, duration):
    subpixel True

    contains:
        image_path
        xalign start_pos alpha 0.1 
        easein duration + 0.4 xalign end_pos
        block:
            image_path
            xalign end_pos alpha 0.1
            easein duration xalign start_pos
            image_path
            xalign start_pos alpha 0.1
            easein duration  xalign end_pos
            repeat
    contains:
        image_path
        xalign start_pos alpha 0.2 
        easein duration + 0.3 xalign end_pos
        block:
            image_path
            xalign end_pos alpha 0.2 
            easein duration xalign start_pos
            image_path
            xalign start_pos alpha 0.2 
            easein duration  xalign end_pos
            repeat
    contains:
        image_path
        xalign start_pos alpha 0.3  
        easein duration + 0.2 xalign end_pos
        block:
            image_path
            xalign end_pos alpha 0.3 
            easein duration xalign start_pos
            image_path
            xalign start_pos alpha 0.3 
            easein duration  xalign end_pos
            repeat

    contains:
        image_path
        xalign start_pos alpha 0.5 
        easein duration + 0.1 xalign end_pos
        block:
            image_path
            xalign end_pos alpha 0.5 
            easein duration  xalign start_pos
            image_path
            xalign start_pos alpha 0.5 
            easein duration  xalign end_pos

            repeat

    contains:
        image_path
        xalign start_pos alpha 0.9 
        easein duration xalign end_pos
        image_path
        xalign end_pos alpha 0.9 
        easein duration xalign start_pos

        repeat
transform sidesteps_effect_dodge(image_path, start_pos, end_pos,duration,y_anch=0.32,y_pos=0.3, ):
    subpixel True
    
    contains:
        image_path
        yanchor y_anch ypos y_pos
        xalign start_pos alpha 0.1 
        easein duration + 0.4 xalign end_pos 
        block:
            image_path
            yanchor y_anch ypos y_pos
            xalign end_pos alpha 0.1
            easein duration xalign start_pos  
            image_path
            yanchor y_anch ypos y_pos
            xalign start_pos alpha 0.1
            easein duration  xalign end_pos  
            repeat 3
    contains:
        image_path
        yanchor y_anch ypos y_pos
        xalign start_pos alpha 0.2 
        easein duration + 0.3 xalign end_pos  
        block:
            image_path
            yanchor y_anch ypos y_pos
            xalign end_pos alpha 0.2 
            easein duration xalign start_pos  
            image_path
            yanchor y_anch ypos y_pos
            xalign start_pos alpha 0.2 
            easein duration  xalign end_pos  
            repeat 3
    contains:
        image_path
        yanchor y_anch ypos y_pos
        xalign start_pos alpha 0.3  
        easein duration + 0.2 xalign end_pos  
        block:
            image_path
            yanchor y_anch ypos y_pos
            xalign end_pos alpha 0.3 
            easein duration xalign start_pos 
            image_path
            yanchor y_anch ypos y_pos
            xalign start_pos alpha 0.3 
            easein duration  xalign end_pos 
            repeat 3

    contains:
        image_path
        yanchor y_anch ypos y_pos
        xalign start_pos alpha 0.5 
        easein duration + 0.1 xalign end_pos 
        block:
            image_path
            yanchor y_anch ypos y_pos
            xalign end_pos alpha 0.5 
            easein duration  xalign start_pos
            image_path
            yanchor y_anch ypos y_pos
            xalign start_pos alpha 0.5 
            easein duration  xalign end_pos

            repeat 3

    contains:
        image_path
        yanchor y_anch ypos y_pos
        xalign start_pos alpha 0.9 
        easein duration xalign end_pos
        image_path
        yanchor y_anch ypos y_pos
        xalign end_pos alpha 0.9 
        easein duration xalign start_pos
        
        repeat 3
    


init python:
    import math
    class Shaker(object):
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child
        def __call__(self, t, sizes):
            # Float to integer... turns floating point numbers to
            # integers.
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x
            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]
            xpos = xpos - xanchor
            ypos = ypos - yanchor
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            return (int(nx), int(ny), 0, 0)
    def _Shake(start, time, child=None, dist=100.0, **properties):
        move = Shaker(start, child, dist=dist)
        return renpy.display.layout.Motion(move,
            time,
            child,
            add_sizes=True,
            **properties)
    Shake = renpy.curry(_Shake)
    shake = Shaker((0, 0, 0, 0), 0.5, dist=8)
