style uguu:
    xpos 0.6
    xanchor 0.0
    ypos 0.4
    yanchor 0.5
    background Frame("gui/frame.png", 64, 64)
style uguu2:
    xpos 0.6 top_padding 4 right_padding 4 left_padding 4
    background Frame("gui/frame.png", 64, 64)

define narrator = Character(ctc="ctc", ctc_position="fixed", callback=speaker("N"))
define name_only = Character( color = '#fff',ctc="ctc", ctc_position="fixed", callback=speaker("N"))
define j = Character("John", color = '#0b99f4', image = "John_side", callback = speaker("John"), ctc="ctc", ctc_position="fixed")
define emailnvl = Character("", color = '#0b99f4',kind=nvl, callback = speaker("John"))

define h = Character("Hilbert",color = '#f7941d', image = "Hilbert_side", callback=speaker("Hilbert"), ctc="ctc", ctc_position="fixed")
define l = Character("Lisa",color = '#992e2c', image = "Lisa_side", callback=speaker("Lisa"), ctc="ctc", ctc_position="fixed")
define al = Character("Alicia",color = '#992e2c', image = "Alicia_side", callback=speaker("Alicia"), ctc="ctc", ctc_position="fixed")
define info = Character("INFO",callback=speaker("INFO"), color='#fff', ctc="ctc", ctc_position="fixed")

define i = Character("ILY",callback=speaker("ILY"), color='#f00', image = "ILY_side", ctc="ctc", ctc_position="fixed")
define v = Character("Vira",callback=speaker("Vira"), color ='#f00',image ="Vira_side", ctc="ctc", ctc_position="fixed")
# define v = Character("Vira",callback=speaker("Vira"), color ='#f00',image ="Vira_side", ctc="ctc", ctc_position="fixed")
define b = Character("Bitwulf",callback=speaker("Bitwulf"),what_slow_cps=40, image = "Bitwulf_side", ctc="ctc", ctc_position="fixed")

define s = Character("Stella",callback=speaker("Stoned"),what_slow_cps=40, image = "Stoned_side", ctc="ctc", ctc_position="fixed")
define c = Character("Code Red",callback=speaker("CodeRed"), color='#f00',image ="CodeRed_side", ctc="ctc", ctc_position="fixed")
define a = Character("Ave",callback=speaker("Ave"), color='#ff8a00', image ="Ave_side", ctc="ctc", ctc_position="fixed")
define m = Character("Melissa",callback=speaker("Melissa"), color='#ff8a00', image ="Melissa_side", ctc="ctc", ctc_position="fixed")
define n = Character("Nick",callback=speaker("Nick"), color='#4e813b', image ="Nick_side", ctc="ctc", ctc_position="fixed")
define cv = Character("Virus Boy",callback=speaker("CodeRed"), color='#f00', ctc="ctc", ctc_position="fixed")
define aa = Character("Antivirus Girl",callback=speaker("Ave"), color='#ff8a00', ctc="ctc", ctc_position="fixed")

define hx = Character("Hacker X",color = '#088', image = "HackerX_side", ctc="ctc", ctc_position="fixed",callback=speaker("HackerX"))


define uc = Character("USB-chan",callback=speaker("USB-chan"),color='#f9b9f9', ctc="ctc", ctc_position="fixed")
define uk = Character("USB-kun",callback=speaker("USB-kun"),color='#7ce7ed', ctc="ctc", ctc_position="fixed")
########
## Functions
########
init -1 python:
    ## Initialize variables
    # globals()["stopblips"] = False
    globals()["direction"] = "down"
    globals()["pdirection"] = "down"
    globals()["bg"] = "1"
    globals()["anim_done"] = True
    globals()["jumping"] = False


    globals()["ILY_m"] = "smile"
    globals()["ILY_p"] = "1"
    globals()["ILY_e"] = "1"
    globals()["ILY_underwear"] = "red" # "red", "small", "" 

    globals()["ILY_outfit"] = "uniform" #bunny, garden, ""

    globals()["ILY_stockings"] = "stockings" # "" if none
    globals()["ILY_w"] = False

    globals()["John_e"] = "normal"
    globals()["John_m"] = "smile"
    globals()["John_w"] = True

    globals()["Hilbert_e"] = "down"
    globals()["Hilbert_m"] = "frown"
    globals()["Hilbert_w"] = True

    globals()["Nick_e"] = "down"
    globals()["Nick_m"] = "frown"
    globals()["Nick_w"] = True
    globals()["HackerX_w"] = True
    # Nick_m

    # globals()["HackerX_w"] = True

    globals()["Lisa_e"] = "normal"
    globals()["Lisa_m"] = "smile"
    globals()["Lisa_w"] = True

    globals()["Vira_m"] = "smile"
    globals()["Vira_e"] = "mad"
    globals()["Vira_w"] = False

    globals()["Ave_e"] = "mad"
    globals()["Ave_m"] = "frown"
    globals()["Ave_w"] = True

    globals()["Melissa_e"] = "up"
    globals()["Melissa_m"] = "smile"
    globals()["Melissa_w"] = True
    globals()["Stoned_e"] = "normal"
    globals()["Stoned_m"] = "happy"
    globals()["Stoned_w"] = True

    globals()["CodeRed_e"] = "normal"
    globals()["CodeRed_m"] = "frown"
    globals()["CodeRed_w"] = True

    globals()["showsideimage"] = False


    # import numpy as np
    # import scipy

    speaking = None
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None

    curried_while_speaking = renpy.curry(while_speaking)

    def WhileSpeaking(name, speaking_d, done_d=Null()):

        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))

    def WhileSpeakingHeld(name, speaking_d, done_d=Null()):

        return DynamicDisplayable(speakbuttonheld(name, speaking_d, done_d))

    renpy.music.register_channel("blipsound", mixer="sfx", stop_on_mute=True, tight=False, buffer_queue=True, movie=False)




    def speaker_callback(name, event, **kwargs):

        global speaking

        if (name == "John"):
            globals()["showsideimage"]=John_w
        elif (name == "Hilbert"):
            globals()["showsideimage"]=Hilbert_w
        elif (name == "ILY"):
            globals()["showsideimage"]=ILY_w
        elif (name == "Lisa"):
            globals()["showsideimage"]=Lisa_w
        elif (name == "Ave"):
            globals()["showsideimage"]=Ave_w
        elif (name == "Vira"):
            globals()["showsideimage"]=Vira_w
        elif (name == "CodeRed"):
            globals()["showsideimage"]=CodeRed_w
        elif (name == "HackerX"):
            globals()["showsideimage"]=HackerX_w

        blipvoices = {
            "John":"low",
            "ILY":"high",
            "Lisa":"mid",
            "N":"low",
            "Hilbert":"low",
            "CodeRed":"low",
            "Vira":"high",
            "Melissa":"high",
            "Ave":"mid",
            "USB-kun":"high",
            "USB-chan":"high",
            "HackerX":"low",
            "Nick":"low",
            "Stoned":"mid",
            "":"mid"
        }
        if event == "begin" or event == "show":
            speaking = name

            # globals()["stopblips"]=False
            if name in blipvoices.keys():
                renpy.sound.play("sound/character/"+blipvoices[name]+".ogg", channel="blipsound", loop=True)
            else:
                renpy.sound.play("sound/character/"+blipvoices[""]+".ogg", channel="blipsound", loop=True)
           #  if (name == "John"):
           #     renpy.sound.play("sound/character/low.ogg", channel="blipsound", loop=True)
           #
           #  elif (name == "ILY"):
           #     renpy.sound.play("sound/character/high.ogg", channel="blipsound", loop=True)
           #  elif (name == "Lisa"):
           #     renpy.sound.play("sound/character/mid.ogg", channel="blipsound", loop=True)
           #  elif (name == 'N'):
           #     renpy.sound.play("sound/character/sfx-blipmale.wav", channel="blipsound", loop=True)
           #  elif (name == 'Hilbert'):
           #     renpy.sound.play("sound/character/low.ogg", channel="blipsound", loop=True)
           #  elif (name == 'CodeRed'):
           #     renpy.sound.play("sound/character/low.ogg", channel="blipsound", loop=True)
           #  elif (name == 'Vira'):
           #     renpy.sound.play("sound/character/high.ogg", channel="blipsound", loop=True)
           #  elif (name == 'Melissa'):
           #     renpy.sound.play("sound/character/high.ogg", channel="blipsound", loop=True)
           #  elif (name == 'Ave'):
           #     renpy.sound.play("sound/character/mid.wav", channel="blipsound", loop=True)
           #  elif (name == 'USB-kun'):
           #     renpy.sound.play("sound/character/low.ogg", channel="blipsound", loop=True)
           #  elif (name == 'USB-chan'):
           #     renpy.sound.play("sound/character/high.ogg", channel="blipsound", loop=True)
           #  elif (name == 'Hilbert'):
           #     renpy.sound.play("sound/character/low.ogg", channel="blipsound", loop=True)
           #  elif (name == 'HackerX'):
           #     renpy.sound.play("sound/character/low.ogg", channel="blipsound", loop=True)
           # elif (name == 'HackerX'):
           #    renpy.sound.play("sound/character/low.ogg", channel="blipsound", loop=True)
           #  elif (name == 'Stoned'):
           #     renpy.sound.play("sound/character/low.ogg", channel="blipsound", loop=True)
           #  elif name=="":
           #     renpy.sound.play("sound/character/low.ogg", channel="blipsound", loop=True)
        elif (event == "slow_done" or event == "end"):
            speaking = None
            renpy.sound.stop(channel="blipsound")


    speaker = renpy.curry(speaker_callback)






    def ILYSprite(emotion="smile", pose=None):
        ## Only change pose if user input something
        if (pose != None):
            globals()["ILY_p"] = str(pose)

        ## Make everything lowercase
        emotion = emotion.lower()

        if (emotion == "smile"):
            globals()["ILY_m"] = "smile"
            globals()["ILY_e"] = '1'

        elif (emotion == "smile2"):
            globals()["ILY_m"] = "smile2"
            globals()["ILY_e"] = '1'

        elif (emotion == "smile3"):
            globals()["ILY_m"] = "smile3"
            globals()["ILY_e"] = '2'

        elif(emotion == "frown"):
            globals()["ILY_m"] = "frown"
            globals()["ILY_e"] = '1'
        elif(emotion == "mad"):
            globals()["ILY_m"] = "frown"
            globals()["ILY_e"] = '2'
        elif(emotion == "o"):
            globals()["ILY_m"] = "o"
            globals()["ILY_e"] = '1'

        else:
            raise ValueError("Unknown emotion entered: " + emotion)




    def JohnSprite(emotion="smile"):
        ## Make everything lowercase
        emotion = emotion.lower()

        if (emotion == "normal"):
            globals()["John_m"] = "smile"
            globals()["John_e"] = "normal"

        elif (emotion == "frown"):
            globals()["John_m"] = "frown"
            globals()["John_e"] = "up"

        elif (emotion == "mad"):
            globals()["John_m"] = "frown"
            globals()["John_e"] = "mad"

        else:
            raise ValueError("Unknown emotion entered: " + emotion)




    def LisaSprite(emotion="smile"):
        ## Make everything lowercase
        emotion = emotion.lower()

        if (emotion == "smile"):
            globals()["Lisa_m"] = "smile"
            globals()["Lisa_e"] = "normal"

        else:
            raise ValueError("Unknown emotion entered: " + emotion)



    def ViraSprite(emotion="smile"):
        ## Make everything lowercase
        emotion = emotion.lower()

        if (emotion == "smile"):
            globals()["Vira_m"] = "smile"
            globals()["Vira_e"] = "normal"

        elif (emotion == "frown"):
            globals()["Vira_m"] = "frown"
            globals()["Vira_e"] = "normal"

        elif (emotion == "mad"):
            globals()["Vira_m"] = "frown"
            globals()["Vira_e"] = "mad"

        else:
            raise ValueError("Unknown emotion entered: " + emotion)




#########
## ILY
#########
image ILYRpg="images/Characters/ILY/ILY[direction].png"

image ILYjumpRpg:
    "images/Characters/ILY/ILY[olddirection].png"
    xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.7
    linear 0.1 yoffset -80
    linear 0.05 yoffset 0


image side ILY_side:

    ConditionSwitch(
        "ILY_w==True","ILYside2",
        "ILY_w==False","Null_side"
    )
    zoom 0.38
image ILYside2:
    LiveCrop((200,60, 440,565), "ILYside3")

image ILYside3:
    "ILYFull"
    zoom 0.9

image Icon_ILY:
    LiveCrop((230,100, 440,565), "ILYFull")
    zoom 0.22


image ILY:
    "ILYFull"
    zoom 0.5
    yalign 0.1
    linear 1.0 yoffset -10
    linear 1.0 yoffset 10
    repeat

image ILYnew:
    "ILYFullBody"
    zoom 0.5
    yalign 0.1

image ILY big:
    "ILYFullBody"
    zoom 0.75
    yalign 0.1
    linear 1.0 yoffset -10
    linear 1.0 yoffset 10
    repeat

image ILY small:
    "ILYFullBody"
    zoom 0.3
    yalign 0.3
    linear 1.0 yoffset -10
    linear 1.0 yoffset 10
    repeat
# image ILYLayered:
image ILYFull:
    LiveComposite(
    (0.75, 0.75), #(544,600),
    (0, 0), "images/Characters/ILY/ILY_p[ILY_p].png", #pose
    #(0, 0), "ILY_p[ILY_p].png",
    (0, 0), "images/Characters/ILY/ILY_e[ILY_p][ILY_e].png", #eyebrows
    (0, 0), "ILYEyes[ILY_p]",#eyes
    (0, 0), "images/Characters/ILY/ILY_heart[ILY_p].png",
    (0, 0), ConditionSwitch(
        "((ILY_p=='1') or (ILY_p=='0'))", WhileSpeaking(
            "ILY",
            ConditionSwitch(
                "('smile' in ILY_m)","ILYMouthsmile",
                "('smile' not in ILY_m)","ILYMouthfrown"
                ),
            "images/Characters/ILY/ILY_m[ILY_m].png"
            ),
        "(ILY_p=='2')", WhileSpeaking(
                            "ILY",
                            ConditionSwitch(
                                "('smile' in ILY_m)","ILYMouthsmile2",
                                "('smile' not in ILY_m)","ILYMouthfrown2"
                                ),
                            "images/Characters/ILY/ILY_m2[ILY_m].png"
                            )
        )
    )
transform ilyfix(deg):
    zoom deg
    xoffset 60
    xpos 0
    ypos 0
image ILYFullBody:
    LiveComposite(
    (0.75, 0.75), #(544,600),
    (0, 0), At("images/Characters/ILY/Full/ILY_Full_base_[ILY_stockings].png",ilyfix(0.5)), #pose
    (0, 0), ConditionSwitch("ILY_underwear!=''",At("images/Characters/ILY/Full/ILY_v2_underwear_[ILY_underwear].png",ilyfix(0.5)),"ILY_underwear==''",Null()), #underwear
    (0, 0), ConditionSwitch("ILY_outfit!=''",At("images/Characters/ILY/Full/ILY_v2_[ILY_outfit].png",ilyfix(0.5)),"ILY_outfit==''",Null()), #outfit
    #(0, 0), "ILY_p[ILY_p].png",
    (0, 0), "images/Characters/ILY/ILY_e1[ILY_e].png", #eyebrows
    (0, 0), "ILYEyes[ILY_p]",#eyes
    (0, 0), "images/Characters/ILY/ILY_heart0.png",
    (0, 0), ConditionSwitch(
        "((ILY_p=='1') or (ILY_p=='0'))", WhileSpeaking(
            "ILY",
            ConditionSwitch(
                "('smile' in ILY_m)","ILYMouthsmile",
                "('smile' not in ILY_m)","ILYMouthfrown"
                ),
            "images/Characters/ILY/ILY_m[ILY_m].png"
            ),
        "(ILY_p=='2')", WhileSpeaking(
                            "ILY",
                            ConditionSwitch(
                                "('smile' in ILY_m)","ILYMouthsmile2",
                                "('smile' not in ILY_m)","ILYMouthfrown2"
                                ),
                            "images/Characters/ILY/ILY_m2[ILY_m].png"
                            )
        )
    )
    
image ILYVtuber:
    LiveComposite(
    (0.75, 0.75), #(544,600),
    (0, 0), "images/Characters/ILY/ILY_Full_base[ILY_p].png", #nude base
    
    #(0, 0), "ILY_p[ILY_p].png",
    (0, 0), "images/Characters/ILY/ILY_e[ILY_p][ILY_e].png", #eyebrows
    (0, 0), "ILYEyes[ILY_p]",#eyes
    (0, 0), "images/Characters/ILY/ILY_heart[ILY_p].png",
    (0, 0), ConditionSwitch(
        "((ILY_p=='1') or (ILY_p=='0'))", WhileSpeakingHeld(
            "ILY",
            ConditionSwitch(
                "('smile' in ILY_m)","ILYMouthsmile",
                "('smile' not in ILY_m)","ILYMouthfrown"
                ),
            "images/Characters/ILY/ILY_m[ILY_m].png"
            ),
        "(ILY_p=='2')", WhileSpeakingHeld(
                            "ILY",
                            ConditionSwitch(
                                "('smile' in ILY_m)","ILYMouthsmile2",
                                "('smile' not in ILY_m)","ILYMouthfrown2"
                                ),
                            "images/Characters/ILY/ILY_m2[ILY_m].png"
                            )
        )
    )


image ILYEyes0:
    choice:
        "images/Characters/ILY/ILY_eyes.png"
        pause 1.0
        "images/Characters/ILY/ILY_eyesmclosed.png"
        pause 0.07
        "images/Characters/ILY/ILY_eyesclosed.png"
        pause 0.1
        "images/Characters/ILY/ILY_eyesmclosed.png"
        pause 0.07
    choice:
        "images/Characters/ILY/ILY_eyes.png"
        pause 8.0
    choice:
        "images/Characters/ILY/ILY_eyes.png"
        pause 4.0
    choice:
        "images/Characters/ILY/ILY_eyes.png"
        pause 1.5
        "images/Characters/ILY/ILY_eyesmclosed.png"
        pause 0.07
        "images/Characters/ILY/ILY_eyesclosed.png"
        pause 0.1
        "images/Characters/ILY/ILY_eyesmclosed.png"
        pause 0.07
        "images/Characters/ILY/ILY_eyesclosed.png"
        pause 0.1
        "images/Characters/ILY/ILY_eyes.png"
        pause 1.5
    repeat

image ILYEyes1:
    choice:
        "images/Characters/ILY/ILY_eyes.png"
        pause 1.0
        "images/Characters/ILY/ILY_eyesmclosed.png"
        pause 0.07
        "images/Characters/ILY/ILY_eyesclosed.png"
        pause 0.1
        "images/Characters/ILY/ILY_eyesmclosed.png"
        pause 0.07
    choice:
        "images/Characters/ILY/ILY_eyes.png"
        pause 8.0
    choice:
        "images/Characters/ILY/ILY_eyes.png"
        pause 4.0
    choice:
        "images/Characters/ILY/ILY_eyes.png"
        pause 1.5
        "images/Characters/ILY/ILY_eyesmclosed.png"
        pause 0.07
        "images/Characters/ILY/ILY_eyesclosed.png"
        pause 0.1
        "images/Characters/ILY/ILY_eyesmclosed.png"
        pause 0.07
        "images/Characters/ILY/ILY_eyesclosed.png"
        pause 0.1
        "images/Characters/ILY/ILY_eyes.png"
        pause 1.5
    repeat

image ILYEyes2:
    choice:
        "images/Characters/ILY/ILY_2eyes.png"
        pause 1.0
        "images/Characters/ILY/ILY_2eyesmclosed.png"
        pause 0.07
        "images/Characters/ILY/ILY_2eyesclosed.png"
        pause 0.1
        "images/Characters/ILY/ILY_2eyesmclosed.png"
        pause 0.07
    choice:
        "images/Characters/ILY/ILY_2eyes.png"
        pause 8.0
    choice:
        "images/Characters/ILY/ILY_2eyes.png"
        pause 4.0
    choice:
        "images/Characters/ILY/ILY_2eyes.png"
        pause 1.5
        "images/Characters/ILY/ILY_2eyesmclosed.png"
        pause 0.07
        "images/Characters/ILY/ILY_2eyesclosed.png"
        pause 0.1
        "images/Characters/ILY/ILY_2eyesmclosed.png"
        pause 0.07
        "images/Characters/ILY/ILY_2eyesclosed.png"
        pause 0.1
        "images/Characters/ILY/ILY_2eyes.png"
        pause 1.5
    repeat

image ILYMouthsmile:
    "images/Characters/ILY/ILY_mmidopen.png"
    pause .08
    "images/Characters/ILY/ILY_msmile2.png"
    pause .05
    "images/Characters/ILY/ILY_msmile.png"
    pause .08
    "images/Characters/ILY/ILY_msmile2.png"
    pause .05
    "images/Characters/ILY/ILY_mmidopen.png"
    pause .08
    "images/Characters/ILY/ILY_msmile3.png"
    pause .08
    "images/Characters/ILY/ILY_mmidopen.png"
    pause .05
    "images/Characters/ILY/ILY_mO2.png"
    pause .08
    "images/Characters/ILY/ILY_mO.png"
    pause .1
    "images/Characters/ILY/ILY_mO2.png"
    pause .08
    "images/Characters/ILY/ILY_mmidopen.png"
    pause .05
    "images/Characters/ILY/ILY_msmile3.png"
    pause .08
    repeat

image ILYMouthsmile2:
    "images/Characters/ILY/ILY_m2smile2.png"
    pause .08
    "images/Characters/ILY/ILY_m2smile2.png"
    pause .05
    "images/Characters/ILY/ILY_m2smile.png"
    pause .08
    "images/Characters/ILY/ILY_m2smile2.png"
    pause .05
    "images/Characters/ILY/ILY_m2smile2.png"
    pause .08
    "images/Characters/ILY/ILY_m2smile3.png"
    pause .08
    "images/Characters/ILY/ILY_m2smile2.png"
    pause .05
    "images/Characters/ILY/ILY_m2O2.png"
    pause .08
    "images/Characters/ILY/ILY_m2O.png"
    pause .1
    "images/Characters/ILY/ILY_m2O2.png"
    pause .08
    "images/Characters/ILY/ILY_m2smile2.png"
    pause .05
    "images/Characters/ILY/ILY_m2smile3.png"
    pause .08
    repeat

image ILYMouthfrown:
    "images/Characters/ILY/ILY_mO2.png"
    pause .08
    "images/Characters/ILY/ILY_mO.png"
    pause .1
    "images/Characters/ILY/ILY_mO2.png"
    pause .08
    "images/Characters/ILY/ILY_mfrown.png"
    pause .08
    repeat

image ILYMouthfrown2:
    "images/Characters/ILY/ILY_m2O2.png"
    pause .08
    "images/Characters/ILY/ILY_m2O.png"
    pause .1
    "images/Characters/ILY/ILY_m2O2.png"
    pause .08
    "images/Characters/ILY/ILY_m2frown.png"
    pause .08
    repeat

#########
## John
#########
# image side John_Side:
#     "JohnFull"
#     zoom 0.38

#image John:
#    "JohnFull"

# image John eyeszoom:
#     LiveCrop((0,200,440,100),"JohnFull")
#     zoom 2.0 yalign 0.5 xalign 0.5
#
# image JohnFull:
#     LiveComposite(
#         (440,565),
#         (0, 0), "images/Characters/John/Johnb.png",
#         (0, 0), WhileSpeaking(
#             "John",ConditionSwitch(
#                 "('smile' in John_m)","JohnMouthsmile",
#                 "('smile' not in John_m)","JohnMouthfrown"
#                 ),
#             "images/Characters/John/John_m[John_m].png"
#             ),
#         (0, 0), "images/Characters/John/John_e[John_e].png",
#         (0, 0), "JohnEyes",#eyes
#         (0, 0), "images/Characters/John/John_glasses.png")
#
# # image JohnMouthsmile:
# #     "images/Characters/John/John_mspeak1.png"
# #     pause .05
# #     "images/Characters/John/John_mspeak2.png"
# #     pause .05
# #     "images/Characters/John/John_mspeak4.png"
# #     pause .08
# #     "images/Characters/John/John_mspeak2.png"
# #     pause .05
# #     "images/Characters/John/John_mspeak1.png"
# #     pause .05
# #     "images/Characters/John/John_msmile.png"
# #     pause .05
# #     repeat
# #
# # image JohnMouthfrown:
# #     "images/Characters/John/John_mspeak1.png"
# #     pause .08
# #     "images/Characters/John/John_mspeak2.png"
# #     pause .05
# #     "images/Characters/John/John_mspeak3.png"
# #     pause .05
# #     "images/Characters/John/John_mspeak2.png"
# #     pause .05
# #     "images/Characters/John/John_mspeak1.png"
# #     pause .08
# #     "images/Characters/John/John_mfrown.png"
# #     pause .05
# #     repeat
# #
# # image JohnEyes:
# #     choice:
# #         "images/Characters/John/John_eyes.png"
# #         pause 1.0
# #         "images/Characters/John/John_eyesmclosed.png"
# #         pause 0.07
# #         "images/Characters/John/John_eyesclosed.png"
# #         pause 0.1
# #         "images/Characters/John/John_eyesmclosed.png"
# #         pause 0.07
# #     choice:
# #         "images/Characters/John/John_eyes.png"
# #         pause 8.0
# #     choice:
# #         "images/Characters/John/John_eyes.png"
# #         pause 4.0
# #     choice:
# #         "images/Characters/John/John_eyes.png"
# #         pause 1.5
# #         "images/Characters/John/John_eyesmclosed.png"
# #         pause 0.07
# #         "images/Characters/John/John_eyesclosed.png"
# #         pause 0.1
# #         "images/Characters/John/John_eyesmclosed.png"
# #         pause 0.07
# #         "images/Characters/John/John_eyesclosed.png"
# #         pause 0.1
# #         "images/Characters/John/John_eyes.png"
# #         pause 1.5
# #     repeat



image JohnEyes:
    choice:
        "images/Characters/John/John_eyes.png"
        pause 1.0
        "images/Characters/John/John_eyes_midclose.png"
        pause 0.07
        "images/Characters/John/John_eyes_closed.png"
        pause 0.1
        "images/Characters/John/John_eyes_midclose.png"
        pause 0.07
    choice:
        "images/Characters/John/John_eyes.png"
        pause 5.0
    choice:
        "images/Characters/John/John_eyes.png"
        pause 4.0
    choice:
        "images/Characters/John/John_eyes.png"
        pause 1.5
        "images/Characters/John/John_eyes_midclose.png"
        pause 0.07
        "images/Characters/John/John_eyes_closed.png"
        pause 0.1
        "images/Characters/John/John_eyes_midclose.png"
        pause 0.07
        "images/Characters/John/John_eyes_closed.png"
        pause 0.1
        "images/Characters/John/John_eyes.png"
        pause 1.5
    repeat

image JohnMouthsmile:
    "images/Characters/John/John_mouth_smile_midopen.png"
    pause .1
    "images/Characters/John/John_mouth_smile_open.png"
    pause .08
    "images/Characters/John/John_mouth_smile_midopen.png"
    pause .1
    "images/Characters/John/John_mouth_smile.png"
    pause .1
    "images/Characters/John/John_mouth_O2.png"
    pause .08
    "images/Characters/John/John_mouth_O.png"
    pause .1
    "images/Characters/John/John_mouth_O2.png"
    pause .08
    repeat

image JohnMouthfrown:
    "images/Characters/John/John_mouth_frown.png"
    pause .05
    # "images/Characters/John/John_mouth_O2.png"
    # pause .05
    "images/Characters/John/John_mouth_O.png"
    pause .08
    # "images/Characters/John/John_mouth_O2.png"
    # pause .05
    "images/Characters/John/John_mouth_frown.png"
    pause .08
    "images/Characters/John/John_mouth_frown_midopen.png"
    pause .05
    "images/Characters/John/John_mouth_frown_open.png"
    pause .08
    "images/Characters/John/John_mouth_frown_midopen.png"
    pause .05
    "images/Characters/John/John_mouth_frown.png"
    pause .05
    repeat
image JohnFull:
    # "images/Characters/John/John_full.png"
    LiveComposite(
        (1076,2368),
        (0, 0), "images/Characters/John/John_base.png",
        (0, 0), WhileSpeaking(
            "John",
            ConditionSwitch(
                "('smile' in John_m)","JohnMouthsmile",
                "('smile' not in John_m)","JohnMouthfrown"
            ),
            "images/Characters/John/John_mouth_[John_m].png"


            ),
        (0, 0), "images/Characters/John/John_eyebrows_[John_e].png",
        (0, 0), "JohnEyes",
        (0, 0), "images/Characters/John/John_glasses.png"
        # (0, 0), "images/Characters/John/Johnshades.png",
        )
    zoom 0.7
image John sidew:
    LiveCrop((246,52, 300,385), "JohnFull")
    zoom 0.56

image John:
    "JohnFull"
   # yalign 0.1 xalign 1.0


image side John_side:
    "John sidew"
    ConditionSwitch(
        "John_w==True","John sidew",
        "John_w==False","Null_side")

#########
## Lisa
#########
# image Lisa:
#     "Lisafull"
#     zoom 0.5

image Lisafull:

        LiveComposite(
        (507,730),
        (0, 0), "images/Characters/Lisa/Lisabase.png",
        (0, 0), WhileSpeaking(
            "Lisa",
            # ConditionSwitch(
            ConditionSwitch(
                "('smile' in Lisa_m)","LisaMouthsmile",
                "('smile' not in Lisa_m)","LisaMouthfrown"
                ),
            "images/Characters/Lisa/Lisa_m[Lisa_m].png"
            ),
        (0, 0), "images/Characters/Lisa/Lisa_e[Lisa_e].png",
        (0, 0), "LisaEyes",#eyes
        )
image Lisa:
    "Lisafull"
    # yanchor 0.0 ypos 0.01
    # linear 1.0 yoffset 0
    # pause .5
    # linear 1.0 yoffset 5
    # pause .5
    # repeat

image Lisa sidew:
    LiveCrop((150,20, 300,385), "Lisafull")
    zoom 0.56
image side Lisa_side:
    ConditionSwitch(
        "Lisa_w==True","Lisa sidew",
        "Lisa_w==False","Null_side")

image Null_side:
    Null(width=440,height=565)

image LisaEyes:
    choice:
        "images/Characters/Lisa/Lisa_eyes.png"
        pause 1.0
        "images/Characters/Lisa/Lisa_eclose1.png"
        pause 0.07
        "images/Characters/Lisa/Lisa_eclose2.png"
        pause 0.1
        "images/Characters/Lisa/Lisa_eclose1.png"
        pause 0.07
    choice:
        "images/Characters/Lisa/Lisa_eyes.png"
        pause 5.0
    choice:
        "images/Characters/Lisa/Lisa_eyes.png"
        pause 4.0
    choice:
        "images/Characters/Lisa/Lisa_eyes.png"
        pause 1.5
        "images/Characters/Lisa/Lisa_eclose1.png"
        pause 0.07
        "images/Characters/Lisa/Lisa_eclose2.png"
        pause 0.1
        "images/Characters/Lisa/Lisa_eclose1.png"
        pause 0.07
        "images/Characters/Lisa/Lisa_eclose2.png"
        pause 0.1
        "images/Characters/Lisa/Lisa_eyes.png"
        pause 1.5
    repeat

image LisaMouthsmile:
    "images/Characters/Lisa/Lisa_mopen1.png"
    pause .05
    "images/Characters/Lisa/Lisa_mopen2.png"
    pause .05
    "images/Characters/Lisa/Lisa_mopen3.png"
    pause .08
    "images/Characters/Lisa/Lisa_mopen2.png"
    pause .05
    "images/Characters/Lisa/Lisa_mopen1.png"
    pause .05
    "images/Characters/Lisa/Lisa_msmile.png"
    pause .05
    "images/Characters/Lisa/Lisa_msmile2.png"
    pause .08
    "images/Characters/Lisa/Lisa_msmile3.png"
    pause .1
    "images/Characters/Lisa/Lisa_msmile2.png"
    pause .05
    "images/Characters/Lisa/Lisa_msmile.png"
    pause .08
    repeat

image LisaMouthfrown:
    "images/Characters/Lisa/Lisa_msmile2.png"
    pause .05
    "images/Characters/Lisa/Lisa_mopen2.png"
    pause .05
    "images/Characters/Lisa/Lisa_mopen3.png"
    pause .08
    "images/Characters/Lisa/Lisa_mopen2.png"
    pause .05
    "images/Characters/Lisa/Lisa_msmile2.png"
    pause .05
    "images/Characters/Lisa/Lisa_mfrown.png"
    pause .05
    repeat
#########
## Vira
#########

image Vira large:
    "ViraFull"
    yalign 0.05
    linear 1.0 yoffset -5
    pause .5
    linear 1.0 yoffset 5
    pause .5
    repeat

image Vira:
    "Vira large"
    # zoom 0.25

image ViraFull:
    LiveComposite(
        (680,961),
        (0, 0), "images/Characters/Vira/Vira_p.png",
        (0, 0), "images/Characters/Vira/Vira_e[Vira_e].png", #eyebrows
        (0, 0), "images/Characters/Vira/Vira_eopen.png",#eyes
        (0, 0), WhileSpeaking(
            "Vira",
            ConditionSwitch(
                "('smile' in Vira_m)","ViraMouthsmile",
                "('smile' not in Vira_m)","ViraMouthfrown"
            ),
            "images/Characters/Vira/Vira_m[Vira_m].png"
        )
    )

image Vira sidew:
    LiveCrop((140,40, 300,385), "ViraFull")
    zoom 0.56
image side Vira_side:
    ConditionSwitch(
        "Vira_w==True","Vira sidew",
        "Vira_w==False",Null(width=100))

image Icon_Vira:
    LiveCrop((280,100, 440,565), "ViraFull")
    zoom 0.22

image ViraMouthsmile:
    "images/Characters/Vira/Vira_msmile2.png"
    pause .08
    "images/Characters/Vira/Vira_msmile.png"
    pause .05
    "images/Characters/Vira/Vira_msmile2.png"
    pause .1
    "images/Characters/Vira/Vira_msmile.png"
    pause .05

    repeat

image ViraMouthfrown:
    "images/Characters/Vira/Vira_mO2.png"
    pause .08
    "images/Characters/Vira/Vira_mO.png"
    pause .1
    "images/Characters/Vira/Vira_mO2.png"
    pause .08
    "images/Characters/Vira/Vira_mfrown.png"
    pause .08
    repeat



#########
## Code Red
#########

image CodeRed:
    "CodeRedFull"
    yanchor 0.0 ypos 0.01
    linear 1.0 yoffset 0
    pause .5
    linear 1.0 yoffset 5
    pause .5
    repeat

image CodeRedFull:
    LiveComposite(
        (714,1025),
        (0, 0), "images/Characters/Code Red/CODE RED_base.png",
        (0, 0), WhileSpeaking(
            "CodeRed",
            "CodeRed mouth",
            "images/Characters/Code Red/CODE RED_mclosed.png"
        )
    )
image CodeRed sidew:
    LiveCrop((140,40, 300,385), "CodeRedFull")
    zoom 0.56
image side CodeRed_side:
    ConditionSwitch(
        "CodeRed_w==True","CodeRed sidew",
        "CodeRed_w==False",Null(width=100))
image Icon_CodeRedFull:
    LiveCrop((280,100, 440,565), "CodeRedFull")
    zoom 0.22
image CodeRed mouth:
    "images/Characters/Code Red/CODE RED_mopen1.png"
    pause .08
    "images/Characters/Code Red/CODE RED_mopen2.png"
    pause .1
    "images/Characters/Code Red/CODE RED_mopen1.png"
    pause .08
    "images/Characters/Code Red/CODE RED_mclosed.png"
    pause .08
    repeat
#CODE RED Icon

image ModeRed:
    "ModeRedFull"
    linear 0.25 alpha 0.8 yoffset 20
    linear 0.25 alpha 1.0 xoffset -20
    repeat

image ModeRedFull:
    "images/Characters/Code Red/MODE RED3.png"
    pause .05
    "images/Characters/Code Red/MODE RED4.png"
    pause .05
    "images/Characters/Code Red/MODE RED5.png"
    pause .05
    "images/Characters/Code Red/MODE RED6.png"
    pause .05
    repeat

#########
## Melissa
#########
image Melissa:
    "MelissaFull"
    yanchor 0.6 ypos 1.0 zoom 0.9
    linear 1.0 yoffset 0
    pause .5
    linear 1.0 yoffset 5
    pause .5
    repeat
image MelissaEyes:
    choice:
        "images/Characters/Melissa/Melissa_eyes.png"
        pause 1.0
        "images/Characters/Melissa/Melissa_eyesclose1.png"
        pause 0.07
        "images/Characters/Melissa/Melissa_eyesclose2.png"
        pause 0.1
        "images/Characters/Melissa/Melissa_eyesclose1.png"
        pause 0.07
    choice:
        "images/Characters/Melissa/Melissa_eyes.png"
        pause 5.0
    choice:
        "images/Characters/Melissa/Melissa_eyes.png"
        pause 4.0
    choice:
        "images/Characters/Melissa/Melissa_eyes.png"
        pause 1.5
        "images/Characters/Melissa/Melissa_eyesclose1.png"
        pause 0.07
        "images/Characters/Melissa/Melissa_eyesclose2.png"
        pause 0.1
        "images/Characters/Melissa/Melissa_eyesclose1.png"
        pause 0.07
        "images/Characters/Melissa/Melissa_eyesclose2.png"
        pause 0.1
        "images/Characters/Melissa/Melissa_eyes.png"
        pause 1.5
    repeat

image MelissaMouthsmile:
    "images/Characters/Melissa/Melissa_mopen1.png"
    pause .1
    "images/Characters/Melissa/Melissa_mopen.png"
    pause .08
    "images/Characters/Melissa/Melissa_mopen1.png"
    pause .1
    "images/Characters/Melissa/Melissa_msmile.png"
    pause .1
    "images/Characters/Melissa/Melissa_mopensmile.png"
    pause .08
    "images/Characters/Melissa/Melissa_msmile.png"
    pause .1
    "images/Characters/Melissa/Melissa_msmile.png"
    pause .08
    repeat

image MelissaMouthfrown:
    "images/Characters/Melissa/Melissa_msmile2.png"
    pause .05
    "images/Characters/Melissa/Melissa_mopen2.png"
    pause .05
    "images/Characters/Melissa/Melissa_mopen3.png"
    pause .08
    "images/Characters/Melissa/Melissa_mopen2.png"
    pause .05
    "images/Characters/Melissa/Melissa_msmile2.png"
    pause .05
    "images/Characters/Melissa/Melissa_mfrown.png"
    pause .05
    repeat
image MelissaFull:
    # "images/Characters/Melissa/Melissa_full.png"
    LiveComposite(
        (1956,5716),
        (0, 0), "images/Characters/Melissa/Melissa_base.png",
        (0, 0), WhileSpeaking(
            "Melissa",
            ConditionSwitch(
                "('smile' in Melissa_m)","MelissaMouthsmile",
                "('smile' not in Melissa_m)","MelissaMouthfrown"
            ),
            "images/Characters/Melissa/Melissa_m[Melissa_m].png"


            ),
        (0, 0), "images/Characters/Melissa/Melissa_e[Melissa_e].png",
        (0, 0), "MelissaEyes"#eyes
        # (0, 0), "images/Characters/Melissa/Melissashades.png",
        )
    zoom 0.22
image Melissa sidew:
    LiveCrop((75,60, 300,385), "MelissaFull")
    zoom 0.56




image side Melissa_side:
    ConditionSwitch(
        "Melissa_w==True","Melissa sidew",
        "Melissa_w==False",Null(width=100))
#########
## Ave
#########
image Ave:
    "AveFull"
    yanchor 0.9 ypos 1.0 zoom 0.9
    linear 1.0 yoffset 0
    pause .5
    linear 1.0 yoffset 5
    pause .5
    repeat


image AveFull:
    LiveComposite(
        (486,861),
        (0, 0), "images/Characters/Ave/Avebase.png",
        (0, 0), WhileSpeaking(
            "Ave",
            "Ave mouth",
            "images/Characters/Ave/Ave_m[Ave_m].png"
            ),
        (0, 0), "images/Characters/Ave/Ave_e[Ave_e].png",
        (0, 0), "AveEyes",#eyes
        (0, 0), "images/Characters/Ave/Aveshades.png",
        )
image AveEyes:
    "images/Characters/Ave/Ave_eyes.png"

image Ave mouth:
    "images/Characters/Ave/Ave_mspeak1.png"
    pause .08
    "images/Characters/Ave/Ave_mspeak2.png"
    pause .1
    "images/Characters/Ave/Ave_mspeak1.png"
    pause .08
    "images/Characters/Ave/Ave_mfrown.png"
    pause .08
    repeat
image Ave sidew:
    LiveCrop((140,40, 300,385), "AveFull")
    zoom 0.56
image side Ave_side:
    ConditionSwitch(
        "Ave_w==True","Ave sidew",
        "Ave_w==False",Null(width=100))

image Icon_Ave:
    LiveCrop((240,100, 440,565), "AveFull")
    zoom 0.22


#########
## Hilbert
#########

# image side Hilbert_side:
#     "images/Characters/Hilbert/Hilbertb.png"
#     zoom 0.38
    # ConditionSwitch(
    #     "Lisa_w==True","Lisa sidew",
    #     "Lisa_w==False",Null(width=100))

image Hilbert:
    "HilbertFull"
    ypos 1.0 yanchor 0.52 #zoom 0.9
    # linear 1.0 yoffset 0
    # pause .5
    # linear 1.0 yoffset 5
    # pause .5
    # repeat
image HilbertEyes:
    choice:
        "images/Characters/Hilbert/Hilbert_eyes.png"
        pause 1.0
        "images/Characters/Hilbert/Hilbert_eyes_midclose.png"
        pause 0.07
        "images/Characters/Hilbert/Hilbert_eyes_closed.png"
        pause 0.1
        "images/Characters/Hilbert/Hilbert_eyes_midclose.png"
        pause 0.07
    choice:
        "images/Characters/Hilbert/Hilbert_eyes.png"
        pause 5.0
    choice:
        "images/Characters/Hilbert/Hilbert_eyes.png"
        pause 4.0
    choice:
        "images/Characters/Hilbert/Hilbert_eyes.png"
        pause 1.5
        "images/Characters/Hilbert/Hilbert_eyes_midclose.png"
        pause 0.07
        "images/Characters/Hilbert/Hilbert_eyes_closed.png"
        pause 0.1
        "images/Characters/Hilbert/Hilbert_eyes_midclose.png"
        pause 0.07
        "images/Characters/Hilbert/Hilbert_eyes_closed.png"
        pause 0.1
        "images/Characters/Hilbert/Hilbert_eyes.png"
        pause 1.5
    repeat
image HilbertEyesLookaway:
    choice:
        "images/Characters/Hilbert/Hilbert_eyes.png"
        pause 1.0
        "images/Characters/Hilbert/Hilbert_eyes_midclose.png"
        pause 0.07
        "images/Characters/Hilbert/Hilbert_eyes_closed.png"
        pause 0.1
        "images/Characters/Hilbert/Hilbert_eyes_midclose.png"
        pause 0.07
    choice:
        "images/Characters/Hilbert/Hilbert_eyes.png"
        pause 5.0
    choice:
        "images/Characters/Hilbert/Hilbert_eyes.png"
        pause 4.0
    choice:
        "images/Characters/Hilbert/Hilbert_eyes.png"
        pause 1.5
        "images/Characters/Hilbert/Hilbert_eyes_midclose.png"
        pause 0.07
        "images/Characters/Hilbert/Hilbert_eyes_closed.png"
        pause 0.1
        "images/Characters/Hilbert/Hilbert_eyes_midclose.png"
        pause 0.07
        "images/Characters/Hilbert/Hilbert_eyes_closed.png"
        pause 0.1
        "images/Characters/Hilbert/Hilbert_eyes.png"
        pause 1.5
    repeat
image HilbertMouthsmile:
    "images/Characters/Hilbert/Hilbert_mouth_smile_midopen.png"
    pause .1
    "images/Characters/Hilbert/Hilbert_mouth_smile_open.png"
    pause .08
    "images/Characters/Hilbert/Hilbert_mouth_smile_midopen.png"
    pause .1
    "images/Characters/Hilbert/Hilbert_mouth_smile.png"
    pause .1
    "images/Characters/Hilbert/Hilbert_mouth_O2.png"
    pause .08
    "images/Characters/Hilbert/Hilbert_mouth_O.png"
    pause .1
    "images/Characters/Hilbert/Hilbert_mouth_O2.png"
    pause .08
    repeat

image HilbertMouthfrown:
    "images/Characters/Hilbert/Hilbert_mouth_frown.png"
    pause .05
    # "images/Characters/Hilbert/Hilbert_mouth_O2.png"
    # pause .05
    "images/Characters/Hilbert/Hilbert_mouth_O.png"
    pause .08
    # "images/Characters/Hilbert/Hilbert_mouth_O2.png"
    # pause .05
    "images/Characters/Hilbert/Hilbert_mouth_frown.png"
    pause .08
    "images/Characters/Hilbert/Hilbert_mouth_frown_midopen.png"
    pause .05
    "images/Characters/Hilbert/Hilbert_mouth_frown_open.png"
    pause .08
    "images/Characters/Hilbert/Hilbert_mouth_frown_midopen.png"
    pause .05
    "images/Characters/Hilbert/Hilbert_mouth_frown.png"
    pause .05
    repeat
image HilbertFull:
    # "images/Characters/Hilbert/Hilbert_full.png"
    LiveComposite(
        (704,2016),
        (0, 0), "images/Characters/Hilbert/Hilbert_base.png",
        (0, 0), WhileSpeaking(
            "Hilbert",
            ConditionSwitch(
                "('smile' in Hilbert_m)","HilbertMouthsmile",
                "('smile' not in Hilbert_m)","HilbertMouthfrown"
            ),
            "images/Characters/Hilbert/Hilbert_mouth_[Hilbert_m].png"


            ),
        (0, 0), "images/Characters/Hilbert/Hilbert_eyebrows_[Hilbert_e].png",
        (0, 0), "HilbertEyes"#eyes
        # (0, 0), "images/Characters/Hilbert/Hilbertshades.png",
        )
    zoom 0.7
image Hilbert sidew:
    LiveCrop((93,24, 300,385), "HilbertFull")
    zoom 0.56




image side Hilbert_side:
    ConditionSwitch(
        "Hilbert_w==True","Hilbert sidew",
        "Hilbert_w==False",Null(width=100))
#########
## Hacker X
#########
image side HackerX_side:
    "images/Characters/HackerX/HackerX.png"
    zoom 0.38
    # ConditionSwitch(
    #     "Lisa_w==True","Lisa sidew",
    #     "Lisa_w==False",Null(width=100))

image Nick:
    "NickFull"
    ypos 1.0 yanchor 0.52 #zoom 0.9
    # linear 1.0 yoffset 0
    # pause .5
    # linear 1.0 yoffset 5
    # pause .5
    # repeat
image NickEyes:
    choice:
        "images/Characters/Nick/Nick_eyes.png"
        pause 1.0
        "images/Characters/Nick/Nick_eyes_midclose.png"
        pause 0.07
        "images/Characters/Nick/Nick_eyes_closed.png"
        pause 0.1
        "images/Characters/Nick/Nick_eyes_midclose.png"
        pause 0.07
    choice:
        "images/Characters/Nick/Nick_eyes.png"
        pause 5.0
    choice:
        "images/Characters/Nick/Nick_eyes.png"
        pause 4.0
    choice:
        "images/Characters/Nick/Nick_eyes.png"
        pause 1.5
        "images/Characters/Nick/Nick_eyes_midclose.png"
        pause 0.07
        "images/Characters/Nick/Nick_eyes_closed.png"
        pause 0.1
        "images/Characters/Nick/Nick_eyes_midclose.png"
        pause 0.07
        "images/Characters/Nick/Nick_eyes_closed.png"
        pause 0.1
        "images/Characters/Nick/Nick_eyes.png"
        pause 1.5
    repeat
image NickEyesLookaway:
    choice:
        "images/Characters/Nick/Nick_eyes.png"
        pause 1.0
        "images/Characters/Nick/Nick_eyes_midclose.png"
        pause 0.07
        "images/Characters/Nick/Nick_eyes_closed.png"
        pause 0.1
        "images/Characters/Nick/Nick_eyes_midclose.png"
        pause 0.07
    choice:
        "images/Characters/Nick/Nick_eyes.png"
        pause 5.0
    choice:
        "images/Characters/Nick/Nick_eyes.png"
        pause 4.0
    choice:
        "images/Characters/Nick/Nick_eyes.png"
        pause 1.5
        "images/Characters/Nick/Nick_eyes_midclose.png"
        pause 0.07
        "images/Characters/Nick/Nick_eyes_closed.png"
        pause 0.1
        "images/Characters/Nick/Nick_eyes_midclose.png"
        pause 0.07
        "images/Characters/Nick/Nick_eyes_closed.png"
        pause 0.1
        "images/Characters/Nick/Nick_eyes.png"
        pause 1.5
    repeat
image NickMouthsmile:
    "images/Characters/Nick/Nick_mouth_smile_midopen.png"
    pause .1
    "images/Characters/Nick/Nick_mouth_smile_open.png"
    pause .08
    "images/Characters/Nick/Nick_mouth_smile_midopen.png"
    pause .1
    "images/Characters/Nick/Nick_mouth_smile.png"
    pause .1
    "images/Characters/Nick/Nick_mouth_frown_midopen.png"
    pause .08
    "images/Characters/Nick/Nick_mouth_frown_open.png"
    pause .1
    "images/Characters/Nick/Nick_mouth_frown_midopen.png"
    pause .08
    repeat

image NickMouthfrown:
    # "images/Characters/Nick/Nick_mouth_frown.png"
    # pause .05
    # # "images/Characters/Nick/Nick_mouth_O2.png"
    # # pause .05
    # "images/Characters/Nick/Nick_mouth_O.png"
    # pause .08
    # # "images/Characters/Nick/Nick_mouth_O2.png"
    # # pause .05
    # "images/Characters/Nick/Nick_mouth_frown.png"
    # pause .08
    "images/Characters/Nick/Nick_mouth_frown_midopen.png"
    pause .05
    "images/Characters/Nick/Nick_mouth_frown_open.png"
    pause .08
    "images/Characters/Nick/Nick_mouth_frown_midopen.png"
    pause .05
    "images/Characters/Nick/Nick_mouth_frown.png"
    pause .05
    repeat
image NickFull:
    # "images/Characters/Nick/Nick_full.png"
    LiveComposite(
        (714,2076),
        (0, 0), "images/Characters/Nick/Nick_base.png",
        (0, 0), WhileSpeaking(
            "Nick",
            ConditionSwitch(
                "('smile' in Nick_m)","NickMouthsmile",
                "('smile' not in Nick_m)","NickMouthfrown"
            ),
            "images/Characters/Nick/Nick_mouth_[Nick_m].png"


            ),
        (0, 0), "images/Characters/Nick/Nick_eyebrows_[Nick_e].png",
        (0, 0), "NickEyes",#eyes
        (0, 0), "images/Characters/Nick/Nick_hair.png"
        )
    zoom 0.7
image Nick sidew:
    LiveCrop((93,24, 300,385), "NickFull")
    zoom 0.56




image side Nick_side:
    ConditionSwitch(
        "Nick_w==True","Nick sidew",
        "Nick_w==False",Null(width=100))


#########
## Stella
#########

image Stoned_eyes:
    "images/Characters/Stoned/Stoned_eyes.png"
    pause 1.0
    choice:
        "images/Characters/Stoned/Stoned_eyes.png"
        pause 2.0
    choice:
        "images/Characters/Stoned/Stoned_eyes.png"
        pause 3.0
    choice:

        "images/Characters/Stoned/Stoned_eyes2.png"
        pause 0.1
        "images/Characters/Stoned/Stoned_eyes3.png"
        pause 0.1
        "images/Characters/Stoned/Stoned_eyes2.png"
        pause 0.1

    choice:
        "images/Characters/Stoned/Stoned_eyes2.png"
        pause 0.05
        "images/Characters/Stoned/Stoned_eyes3.png"
        pause 0.1
        "images/Characters/Stoned/Stoned_eyes2.png"
        pause 0.05
        "images/Characters/Stoned/Stoned_eyes.png"
        pause 0.1

        repeat 2
    repeat
image Stoned_Guns:
    "images/Characters/Stoned/Stoned_Guns.png"
    linear 1.0 yoffset 40
    linear 1.0 yoffset 0
    repeat
image Stoned:
    LiveComposite(
    (761,1695),
    (0,0),"images/Characters/Stoned/Stoned_base.png",
    (0,0),"images/Characters/Stoned/Stoned_e[Stoned_e].png",
    (0,0),"Stoned_eyes",
    (0,0),WhileSpeaking("Stoned",("Stoned_m[Stoned_m]"),"images/Characters/Stoned/Stoned_m[Stoned_m].png"),
    (0,0),"images/Characters/Stoned/Stoned_glass.png"
    # (0,0),"Stoned_Guns"
    )
    zoom 0.95 xalign 0.5 yanchor 0.05 ypos 0.0
image Stonedsmall:
    "Stoned"
    zoom 0.80
image side Stoned_side:
    ConditionSwitch(
            "Stoned_w==True",(LiveCrop((327,150,300,385),"Stonedsmall")),
            "Stoned_w==False",Null()
        )
    zoom 0.56
image Stoned_icon:
    (LiveCrop((327,150,280,280),"Stonedsmall"))
    zoom 0.4
image Stoned_mhappy:

    "images/Characters/Stoned/Stoned_mopenU.png"
    pause .16
    "images/Characters/Stoned/Stoned_mhappy.png"
    pause .08
    "images/Characters/Stoned/Stoned_mopenO.png"
    pause .16
    "images/Characters/Stoned/Stoned_mhappy.png"
    pause .08
    repeat
image Stoned_msad:
    "images/Characters/Stoned/Stoned_mopen2.png"
    pause .08
    "images/Characters/Stoned/Stoned_mopenO.png"
    pause .08
    "images/Characters/Stoned/Stoned_mopenO.png"
    pause .08
    "images/Characters/Stoned/Stoned_msad.png"
    pause .08
    repeat

#########
## Bitwulf
#########

# image Stoned_eyes:
#     "images/Characters/Stoned/Stoned_eyes.png"
#     pause 1.0
#     choice:
#         "images/Characters/Stoned/Stoned_eyes.png"
#         pause 2.0
#     choice:
#         "images/Characters/Stoned/Stoned_eyes.png"
#         pause 3.0
#     choice:

#         "images/Characters/Stoned/Stoned_eyes2.png"
#         pause 0.1
#         "images/Characters/Stoned/Stoned_eyes3.png"
#         pause 0.1
#         "images/Characters/Stoned/Stoned_eyes2.png"
#         pause 0.1

#     choice:
#         "images/Characters/Stoned/Stoned_eyes2.png"
#         pause 0.05
#         "images/Characters/Stoned/Stoned_eyes3.png"
#         pause 0.1
#         "images/Characters/Stoned/Stoned_eyes2.png"
#         pause 0.05
#         "images/Characters/Stoned/Stoned_eyes.png"
#         pause 0.1

#         repeat 2
#     repeat

# image Stoned_Guns:
#     "images/Characters/Stoned/Stoned_Guns.png"
#     linear 1.0 yoffset 40
#     linear 1.0 yoffset 0
#     repeat
image Bitwulf:
    LiveComposite(
    (761,1695),
    (0,0),"images/Characters/Bitwulf/Bitwulf_base.png",
    (0,0),"images/Characters/Bitwulf/Bitwulf_e[Bitwulf_e].png",
    (0,0),"Bitwulf_eyes",
    (0,0),WhileSpeaking("Bitwulf",("Bitwulf_m[Bitwulf_m]"),"images/Characters/Bitwulf/Bitwulf_m[Bitwulf_m].png"),
    (0,0),"images/Characters/Bitwulf/Bitwulf_glass.png"
    # (0,0),"Bitwulf_Guns"
    )
    zoom 0.95 xalign 0.5 yanchor 0.05 ypos 0.0
image Bitwulfsmall:
    "Bitwulf"
    zoom 0.80
image side Bitwulf_side:
    ConditionSwitch(
            "Bitwulf_w==True",(LiveCrop((327,150,300,385),"Bitwulfsmall")),
            "Bitwulf_w==False",Null()
        )
    zoom 0.56
image Bitwulf_icon:
    (LiveCrop((327,150,280,280),"Bitwulfsmall"))
    zoom 0.4
image Bitwulf_mhappy:

    "images/Characters/Bitwulf/Bitwulf_mopenU.png"
    pause .16
    "images/Characters/Bitwulf/Bitwulf_mhappy.png"
    pause .08
    "images/Characters/Bitwulf/Bitwulf_mopenO.png"
    pause .16
    "images/Characters/Bitwulf/Bitwulf_mhappy.png"
    pause .08
    repeat
image Bitwulf_msad:
    "images/Characters/Bitwulf/Bitwulf_mopen2.png"
    pause .08
    "images/Characters/Bitwulf/Bitwulf_mopenO.png"
    pause .08
    "images/Characters/Bitwulf/Bitwulf_mopenO.png"
    pause .08
    "images/Characters/Bitwulf/Bitwulf_msad.png"
    pause .08
    repeat
