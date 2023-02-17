
init python:
  def placeobject(boxsheet,xpos,ypos,objectnum):
       boxsheet[ypos][xpos]= objectnum
       return boxsheet
  bg = 1
  bgyanchor = 720
  bgxanchor = 1280
  bgypos = 0.5*720
  bgxpos = 0.5*1280
  blockSize = 50
  jumphght = 0
  Running = True
  direction = 'down'
  linearmaptransform=True


  boxsheet = stagehome
  Where = "Home"
  startplayerpos = [1,1] #(x,y)
  #ILY'S FIRST POSITION

  playerpos = startplayerpos
  playerxpos = playerpos[0]
  playerypos = playerpos[1]

  Here = boxsheet[playerypos][playerxpos]
  Hereisempty = (boxsheet[playerypos][playerxpos]=='0')

  playerxpos = playerpos[0]
  playerypos = playerpos[1]
  objxanchor = ((playerpos[0]+1)*blockSize)-(blockSize/2)
  objyanchor = ((playerpos[1]+1)*blockSize)-(blockSize/2)

  Upisempty = (boxsheet[playerypos-1][playerxpos]=='0')
  Downisempty = (boxsheet[playerypos+1][playerxpos]=='0')
  Leftisempty = (boxsheet[playerypos][playerxpos-1]=='0')
  Rightisempty = (boxsheet[playerypos][playerxpos+1]=='0')

  objectabove = boxsheet[playerypos-1][playerxpos]
  objectbelow = boxsheet[playerypos+1][playerxpos]
  objectleft = boxsheet[playerypos][playerxpos-1]
  objectright = boxsheet[playerypos][playerxpos+1]

  UpisActor = (objectabove!='0') and (direction == 'up')
  DownisActor = (objectbelow!='0') and (direction == 'down')
  LeftisActor = (objectleft!='0') and (direction == 'left')
  RightisActor = (objectright!='0') and (direction == 'right')
  FacingActor = (UpisActor or DownisActor) or (LeftisActor or RightisActor)
default gridpos = [192,168]
label initializemapvariables:
    python:
       gridpos = [192,168]

    return
label checkwalls:
   python:
      playerxpos = playerpos[0]
      playerypos = playerpos[1]
      Hereisempty = (boxsheet[playerypos][playerxpos]=='0')
      Here = boxsheet[playerypos][playerxpos]
      HereisDoor = ((Here=='a') or (Here=='b')) or ((Here=='c') or (Here=='d'))
      HereisEventDoor = ('script' in Here)

   python:
      objectabove = boxsheet[playerypos-1][playerxpos]
      objectbelow = boxsheet[playerypos+1][playerxpos]
      objectleft = boxsheet[playerypos][playerxpos-1]
      objectright = boxsheet[playerypos][playerxpos+1]

      Upisempty = (objectabove=='0') or (objectabove=='d') or (objectabove=='c') or (objectabove=='b') or (objectabove=='a') or ('script'in objectabove)
      Downisempty = (objectbelow=='0') or (objectbelow=='d') or (objectbelow=='c') or (objectbelow=='b') or (objectbelow=='a') or ('script'in objectbelow)
      Leftisempty = (objectleft=='0') or (objectleft=='d') or (objectleft=='c') or (objectleft=='b') or (objectleft=='a') or ('script'in objectleft)
      Rightisempty = (objectright=='0') or (objectright=='d') or (objectright=='c') or (objectright=='b') or (objectright=='a') or ('script'in objectright)


      UpisActor = (objectabove!='0') and (direction == 'up')
      DownisActor = (objectbelow!='0') and (direction == 'down')
      LeftisActor = (objectleft!='0') and (direction == 'left')
      RightisActor = (objectright!='0') and (direction == 'right')
      FacingActor = (UpisActor or DownisActor) or (LeftisActor or RightisActor)

      if direction=='up':
        actornum = objectabove
      elif direction == 'down':
        actornum = objectbelow
      elif direction == 'left':
        actornum = objectleft
      elif direction == 'right':
        actornum = objectright

      # return
   if HereisDoor:
      play sound"sfx/door-fr_0009.wav"
      call doorjump from _call_doorjump
   if HereisEventDoor:
      play sound"sfx/door-fr_0009.wav"
      call eventdoor from _call_eventdoor
   return

label eventdoor:
    $renpy.jump(str(Here))
    return
# label poschange:
#     ""
#     return
label mapcall(position,stage):
    # scene bg
    #position is an (x,y) tuple declaring place in map.
    #stage is declared by stage number: stage = stage1
    #call mapcall((5,5),stage1)
    play music "bgm/ost/Grid_noyemi_K.mp3"
    call addsprites(gridpos)
    python:
        boxsheet = stage
        playerpos = position
        playerxpos = playerpos[0]
        playerypos = playerpos[1]
        objxanchor = ((playerpos[0]+1)*blockSize)-(blockSize/2)
        objyanchor = ((playerpos[1]+1)*blockSize)-(blockSize/2)
        for sprite in spritelist:
            spritename=str(sprite.name)
            boxsheet[sprite.position[1]][sprite.position[0]]=str(spritename)
        for event in eventlist:
            eventlabel=str(event.label)
            for eventposition in event.positionlist:
                boxsheet[eventposition[1]][eventposition[0]]=eventlabel
    $ map_active=True
    label maploop:

      show screen mapB
      call screen mapA
      call Returns

      if map_active==True:
        jump maploop

      else:
        return
    return
image bgmap:

    "images/rpg/overworld/bg.png"
    pause .2
    "images/rpg/overworld/bgsparkle2.png"
    pause .2
    "images/rpg/overworld/bgsparkle.png"
    pause .2
    "images/rpg/overworld/bgsparkle2.png"
    pause .2
    repeat
image scrollingBG:
    Tile("bgmap")
    # rotate 22.5
    xalign 0.0 yalign 0.0
transform scroll:
    xpan 0 ypan 0
    linear 20.0 xpan 360 ypan 360
    repeat

label mapresume:

    play music "bgm/ost/Grid_noyemi_K.mp3"
    scene scrollingBG at scroll
    # $ boxsheet = globals()["GRID"][(gridpos[0],gridpos[1])]
    call addsprites(gridpos) from _call_addsprites_2
    show screen mapB
    call screen mapA
    call Returns
    return

label maptransfer(position,stage):
    # scene bg
    #position is an (x,y) tuple declaring place in map.
    #stage is declared by stage number: stage = stage1
    #call mapcall((5,5),stage1)
    call addsprites(gridpos)
    python:
        linearmaptransform=False
        boxsheet = stage
        playerpos = position
        playerxpos = playerpos[0]
        playerypos = playerpos[1]
        # Here = boxsheet[playerxpos][playerypos]
        objxanchor = ((playerpos[0]+1)*blockSize)-(blockSize/2)
        objyanchor = ((playerpos[1]+1)*blockSize)-(blockSize/2)
        for sprite in spritelist:
            spritename=str(sprite.name)
            boxsheet[sprite.position[1]][sprite.position[0]]=spritename
        for event in eventlist:
            eventlabel=str(event.label)
            for eventposition in event.positionlist:
                boxsheet[eventposition[1]][eventposition[0]]=eventlabel
    call checkwalls from _call_checkwalls
    $ linearmaptransform=True


    return
image shock:
    "images/rpg/overworld/shock1.png"
    pause .05
    "images/rpg/overworld/shock12.png"
    pause .05
    "images/rpg/overworld/shock2.png"
    pause .05
    "images/rpg/overworld/shock22.png"
    pause .05
    "images/rpg/overworld/shock3.png"
    pause .05
    "images/rpg/overworld/shock32.png"
    pause .05
    choice:
      xzoom -1.0
    choice:
      yzoom -1.0
    choice:
      xzoom 1.0
    choice:
      yzoom 1.0
    repeat


screen mapB:

    vbox:
      if linearmaptransform:
          at mover(objxanchor,objyanchor)
      else:
          at mover_nolinear(objxanchor,objyanchor)
      for i in boxsheet:
         hbox:
           xalign 0.5 yalign 1.0
           for j in i:
             if j !='n':
               image "images/rpg/tile/Tilebg.png"
             elif j == 'n':
               null height blockSize width blockSize
    vbox:
      if linearmaptransform:
          at mover(objxanchor,objyanchor)
      else:
          at mover_nolinear(objxanchor,objyanchor)
      for i in boxsheet:
         hbox:
           xalign 0.5 yalign 1.0
           for j in i:
             if j =='1':
               image "images/rpg/overworld/object.png"
             elif j =='2':
               image "shock"
             elif j =='3':
               image "images/rpg/overworld/object3.png"
             elif j =='4':
               image "images/rpg/overworld/object4.png"
             elif j =='5':
               image "images/rpg/overworld/object5.png"
             elif j =='a':
               image "images/rpg/overworld/objectd.png"
             elif j =='b':
               image "images/rpg/overworld/objectd.png"
             elif j =='c':
               image "images/rpg/overworld/objectd.png"
             elif j =='d':
               image "images/rpg/overworld/objectd.png"
             elif 'script' in j:
               image "images/rpg/overworld/storyevent.png"
             elif j=='0':
               null height blockSize width blockSize
             elif j == 'n':
               null height blockSize width blockSize
             elif len(j)>1:
               null height blockSize width blockSize

##NPC SPRITES


    ##PLAYER CHARACTER
    if len(objectbelow)>1:
      use playersprite(playerypos)
    for sprites in spritelist:
          use npcsprite(sprites)
    if len(objectbelow)<=1:
      # for sprites in spritelist:
      #   use npcsprite(sprites)
      use playersprite(playerypos)
    frame:
      style_prefix "overworld"
      xpadding 15
      ypadding 15
      yalign 0.11 xalign 0.01
      vbox:


        null width 260
        text "GRID ([gridpos[0]],[gridpos[1]])"
        text "{color=#fff}Position = ([playerxpos],[playerypos]){/color}"
        text "{color=#fff}Running = [Running]{/color}"
        # text "{color=#fff}Here = [Here]{/color    }"
        # text "{color=#fff}Where = [Where]{/color}"
        text "{color=#fff}Where = [Where]{/color}"
        # text "{color=#fff}direction = [direction]{/color}"
        # text "{color=#fff}moving = [moving]{/color}"
        # direction
        frame:
            style_prefix "healthbar"
            xsize bar_size(playerHP,playerHPMax,200)
            # xsize
        null height 7
        text "HP: [playerHP]/[playerHPMax]"
        null height 10
## MOBILE BUTTONS
    # if not anim_done:
    #
    #     image "gui/phone/buttonA.png":
    #         pos (0.96,0.8) align (0.5,0.5) at zoombutton
    #     image "gui/phone/buttonB.png":
    #         pos (0.9,0.9) align (0.5,0.5) at zoombutton
    #     image "gui/phone/buttonX.png":
    #         pos (0.9,0.7) align (0.5,0.5) at zoombutton
    #     image "gui/phone/buttonY.png":
    #         pos (0.84,0.8) align (0.5,0.5) at zoombutton
###UNCOMMENT FOR MOBILE
    # imagebutton idle "gui/phone/direction.png":
    #     hovered SetVariable("direction","up"),SetVariable("direction2","up")#,Return("up")
    #     unhovered SetVariable("direction2",None)
    #     action SetVariable("direction","up")#,Return("up")
    #     at rotate(0) pos (0.1,0.7) align (0.5,0.5)
    # imagebutton idle "gui/phone/direction.png":
    #     hovered SetVariable("direction","down"),SetVariable("direction2","down")#,Return("down")
    #     unhovered SetVariable("direction2",None)
    #     action SetVariable("direction","down")#,Return("down")
    #     at rotate(180) pos (0.1,0.9) align (0.5,0.5)
    # imagebutton idle "gui/phone/direction.png":
    #     hovered SetVariable("direction","left"),SetVariable("direction2","left")#,Return("left")
    #     unhovered SetVariable("direction2",None)
    #     action SetVariable("direction","left")#,Return("left")
    #     at rotate(270) pos (0.04,0.8) align (0.5,0.5)
    # imagebutton idle "gui/phone/direction.png":
    #     hovered SetVariable("direction","right"),SetVariable("direction2","right")#,Return("right")
    #     unhovered SetVariable("direction2",None)
    #     action SetVariable("direction","right")#,Return("right")
    #     at rotate(90) pos (0.16,0.8) align (0.5,0.5)

    # frame:
    #     align (0.9,0.0)
    #     vbox:
    #         add Indicator():
    #             align (0.5,0.5)
    #         label "hold mouse":
    #             align (0.5,0.5)
transform zoombutton:
    zoom 0.1
style overworld_text:
    size 14
    # zorder yvalue
screen npcsprite(sprites):
    zorder sprites.position[1]

    image "images/rpg/overworld/[sprites.name][sprites.direction].png" xpos 0.5 ypos 0.508:
        if linearmaptransform:
            at mover2((objxanchor-(sprites.position[0])*50),objyanchor-(sprites.position[1])*50), halftrans# zorder maplayering(sprites.position[1])
        elif not linearmaptransform:
            at mover2_nolinear((objxanchor-(sprites.position[0])*50),objyanchor-(sprites.position[1])*50), halftrans
screen playersprite(yvalue):
    zorder yvalue
    imagebutton idle "images/Characters/ILY/ILY[direction].png" action Return("Pause") xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 1.0 at playerjump(jumphght), blockSizetrans(blockSize) #zorder maplayering(playerypos)


transform blockSizetrans(blockSize):
  zoom blockSize*.01 transform_anchor True
transform halftrans:
  zoom 0.5

transform zoombig:
    xalign 0.5 yalign 1.0
# init python:
#     btnhovered = 1.0
#     profilearray = []
transform transp:
        alpha 0.6
transform rpgsize:
        zoom 0.35 alpha 1.0


# transform maptrans:
#   on show:
#    zoom 1.0
#    xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5
#   rotate 90
#   linear 0.1 xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5

transform mover(objxanchor,objyanchor):
  xpos 0.5 ypos 0.5
  linear 0.1 xanchor int(objxanchor) yanchor int(objyanchor) transform_anchor True
transform mover2(objxanchor,objyanchor):
  # xpos 1.0 ypos 1.0
  xanchor 0.5 yanchor 0.5
  linear 0.1 xpos int(-1*(objxanchor)+(690)) ypos int(-1*(objyanchor)+(405)) transform_anchor True
transform mover_nolinear(objxanchor,objyanchor):
  xpos 0.5 ypos 0.5
  xanchor int(objxanchor) yanchor int(objyanchor) transform_anchor True
transform mover2_nolinear(objxanchor,objyanchor):
  # xpos 1.0 ypos 1.0
  xanchor 0.5 yanchor 0.5
  xpos int(-1*(objxanchor)+(690)) ypos int(-1*(objyanchor)+(405)) transform_anchor True

# transform maplayering(yvalue):
#   zorder yvalue
transform playerjump(jumphght):
  xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.7
  linear 0.05 yoffset - jumphght
  linear 0.05 yoffset 0
  pause .1
  repeat
transform rotate(degree):
    rotate degree
    zoom 0.1
init python:
    directionpress={x:False for x in ["up","down","left","right"]}
    direction2=None
screen mapA:
    # $ moving=False
    #CONTROLS
    key 'K_UP'          action SetVariable("direction","up"),     Return("up")
    key 'K_DOWN'        action SetVariable("direction","down"),   Return("down")
    key 'K_LEFT'        action SetVariable("direction","left"),   Return("left")
    key 'K_RIGHT'       action SetVariable("direction","right"),  Return("right")
# for mobile stuff
    # if direction2 is not None:
    #     if moving and direction=="up":
    #         timer 0.01 action Return("up") repeat True
    #     if moving and direction=="down":
    #         timer 0.01 action Return("down") repeat True
    #     if moving and direction=="left":
    #         timer 0.01 action Return("left") repeat True
    #     if moving and direction=="right":
    #         timer 0.01 action Return("right") repeat True
    #
    # key ["mousedown_1"] action Function(setmoving,(True))
    # key ["mouseup_1"] action Function(setmoving,(False))

    if anim_done:

        key 'repeat_K_UP'     action SetVariable("direction","up"),     Return("up")
        key 'repeat_K_DOWN'   action SetVariable("direction","down"),   Return("down")
        key 'repeat_K_RIGHT'  action SetVariable("direction","right"),  Return("right")
        key 'repeat_K_LEFT'   action SetVariable("direction","left"),   Return("left")
    # key 'K_ESCAPE'      action Return("End")
    # key 'K_RETURN'         action Return("Pause")
    key 'z'             action Return("OK")
    key 'Z'             action Return("OK")
    key 'x'             action Return("MapTalk")
    key 'X'             action Return("MapTalk")
    # key 'x'             action ShowMenu("partylist")
    key 'r'             action Return("running")
    key 'R'             action Return("running")

    key 'K_SPACE'       action Return("Pause")
    key 's'       action Return("Pause")
    key 'S'       action Return("Pause")
    key 'a'       action Return("running")
    key 'A'       action Return("running")

    key 'c' action Return("jump")
    key 'c' action Return("jump")
    key 'repeat_c'action Return("jump")
    key 'repeat_C'action Return("jump")
    # key 'repeat_K_SPACE'action Return("jump")
    # key 'E'             action Return("End")
    # key 'e'             action Return("End")
    # add KeyCatcher()
## MOBILE BUTTONS
    # imagebutton idle "gui/phone/buttonA.png" action Return("OK"):
    #     pos (0.96,0.8) align (0.5,0.5) at zoombutton
    # imagebutton idle "gui/phone/buttonB.png" action Return("MapTalk"):
    #     pos (0.9,0.9) align (0.5,0.5) at zoombutton
    # imagebutton idle "gui/phone/buttonX.png" action Return("Pause"):
    #     pos (0.9,0.7) align (0.5,0.5) at zoombutton
    # imagebutton idle "gui/phone/buttonY.png" action Return("running"):
    #     pos (0.84,0.8) align (0.5,0.5) at zoombutton

init python:
    def setmoving(mov):
        global moving
        moving=mov

##################
# label main_menu:
#     return
#
# define _confirm_quit = False
#
init python:
    moving=False

############################
transform floatmov:
    linear 0.5 yoffset -2
    linear 0.5 yoffset 2
    repeat
transform ilymov2:
    linear 1.0 yoffset -10

    linear 1.0 yoffset 10
    repeat
define safezones = ["Home_Page","Shady_Alley"]
label randomencounter:
     $ randomenemy = renpy.random.randint(0,100)
     $ safezone=(Where in safezones)
     # $safezone=True #for debugging
     $ enemy_encounter = ((randomenemy >99) and (not safezone)) and (Here=="0")
     if enemy_encounter == True:
          $ enemyvirus = renpy.random.choice([Keylogger,Ransomware,Rootkit,Worm,Spyware])
          # $ enemyvirus = renpy.random.choice([Vira])
          hide screen mapB
          hide screen mapA
          call battlev3(ILY,enemyvirus)
          if playerHP<=0:
              return
          $ enemy_encounter=False
          $ map_active=True
          call mapresume
          return

     return
label Returns:
#   if not running:

  if map_active:
   if (_return=="running"):
    if not Running:
     $ Running = True
    elif Running:
     $ Running = False
   if (pdirection ==_return) or Running:
    #if Hereisempty:

      $ playerxpos = playerpos[0]
      $ playerypos = playerpos[1]
      $ anim_done = False
      $ linearmaptransform=False
      if Upisempty:
       if (_return=="up"):
        
        $ objyanchor = objyanchor-blockSize
        $ playerpos = [playerxpos,playerypos-1]
      else:
        if _return=="up":
            play sound "sfx/bumpintowall_X5CNQPB.mp3"
      if Downisempty:
       if (_return=="down"):
        $ objyanchor = objyanchor+blockSize
        $ playerpos = [playerxpos,playerypos+1]
      else:
        if _return=="down":
            play sound "sfx/bumpintowall_X5CNQPB.mp3"
      if Leftisempty:
       if (_return=="left"):
        $ objxanchor = objxanchor-blockSize
        $ playerpos = [playerxpos-1,playerypos]
      else:
        if _return=="left":
            play sound "sfx/bumpintowall_X5CNQPB.mp3"
      if Rightisempty:
       if (_return=="right"):
        $ objxanchor = objxanchor+blockSize
        $ playerpos = [playerxpos+1,playerypos]
      else:
        if _return=="right":
          play sound "sfx/bumpintowall_X5CNQPB.mp3"
      
      pause 0.02
      $ anim_done = True
      #call wildenemy

   if (_return=="zoomin"):
     $ blockSize = blockSize + 10
     hide screen mapA
   if (_return=="zoomout"):
     $ blockSize = blockSize - 10
     hide screen mapA
   if (_return=="jump"):
        $ jumphght=blockSize*1.0
        pause 0.1
        $ jumphght=0

   if FacingActor:
     if (_return=="OK"):
       call whatactor from _call_whatactor
       return
   if (_return=="MapTalk"):
       call MapTalk from _call_MapTalk
       return
   if (_return=="Pause"):
       # "Pause"
       call pauseshow from _call_pauseshow
       return
   elif (_return=="End"):
        $map_active=False
        return
   else:
       $ pdirection = direction
   call checkwalls
   # $safezone=True
   call randomencounter
   if (playerHP<=0) or (map_active==False):
      return
   call screen mapA
   call Returns
   return
  return

# label Damage:
#         # DAMAGING ENEMY USING OWN CARD
#
#         hide ring
#         hide card1
#         hide card2
#         hide card3
#         hide card4
#         #Calculate dmg here
#         call fxnCaller(PlayerFxn) from _call_fxnCaller
#         if EnmyHP <=0:
#           $EnemyHP=0
#           show Enemy:
#             linear 0.15 zoom 0.94
#             xoffset 0.12 yoffset 0.2 alpha 0.5
#             pause .05
#             xoffset 0.-17 yoffset 0.-17 alpha 0.8
#             pause .05
#             xoffset 0.13 yoffset 0.2 alpha 1.0
#             pause 0.1
#             xoffset 0.-19 yoffset 0.11
#             pause 0.4
#             linear 0.1 zoom 0.8 alpha 0.0
#           $ renpy.pause(0.4,hard=True)
#           $Battle_End = True
#           hide Enemy
#           hide screen stats
#           hide screen choosecard
#           stop music
#
#           # jump cardcycle
#         return


label EnmyDamage:
    #ILY LOSING HP
    #Calculate dmg here
    call fxnCallerp(EnmyFxn) from _call_fxnCallerp
    if playerHP <=0:
      $playerHP=0
      #Losing Animation
      "ILY Deleted!"
      $Battle_End = True
      hide Enemy
      hide screen stats
      hide screen choosecard
      stop music

      # jump cardcycle
    return


screen notif(notiftext):
    frame:
      null height 100 width 1280
      text "[notiftext]" at notifanim
      null height 100 width 1280

transform notifanim:
  on show:
    yzoom 0.0
    linear 0.2 yzoom 1.0

image ILY_byTorakun14:
  "images/characters/ILY/ILY nobg_by_Torakun.png"
  zoom 0.3
