style uguu:
    xpos 0.6
    xanchor 0.0
    ypos 0.4
    yanchor 0.5
    background Frame("gui/frame.png", 64, 64)
style uguu2:
    xpos 0.6 top_padding 4 right_padding 4 left_padding 4
    background Frame("gui/frame.png", 64, 64)
transform left:
    xalign 0.02
transform right:
    xalign 0.98
transform center:
    xalign 0.5
init python:

    def togglechar(character_name, where=center):
        if globals()[character_name+"_w"]==False:
            renpy.hide(character_name)
        else:
            character_xpos=(0.1 if where=="left" else 0.9 if "right" else 0.5)
            renpy.show(character_name,at_list=[where])
        globals()[character_name+"_w"] = not globals()[character_name+"_w"]
        return
    # usage:
    #     showchar("ILY","left")


define narrator = Character(ctc="ctc", ctc_position="fixed", callback=speaker("N"))
define name_only = Character( color = '#fff',ctc="ctc", ctc_position="fixed", callback=speaker("N"))
define emailnvl = Character("", color = '#0b99f4',kind=nvl, callback = speaker("John"))
define u = Character("???",color = '#fff', callback=speaker("N"), ctc="ctc", ctc_position="fixed")
define info = Character("INFO",callback=speaker("INFO"), color='#fff', ctc="ctc", ctc_position="fixed")

## Humans
define j = Character("John", color = '#0b99f4', image = "John_side", callback = speaker("John"), ctc="ctc", ctc_position="fixed")
define h = Character("Hilbert",color = '#f7941d', image = "Hilbert_side", callback=speaker("Hilbert"), ctc="ctc", ctc_position="fixed")
define l = Character("Lisa",color = '#992e2c', image = "Lisa_side", callback=speaker("Lisa"), ctc="ctc", ctc_position="fixed")
define al = Character("Alicia",color = '#992e2c', image = "Alicia_side", callback=speaker("Alicia"), ctc="ctc", ctc_position="fixed")
define lc = Character("Lucida",color = '#405f82', image = "Lucida_side", callback=speaker("Lucida"), ctc="ctc", ctc_position="fixed")
define n = Character("Nick",callback=speaker("Nick"), color='#4e813b', image ="Nick_side", ctc="ctc", ctc_position="fixed")

define be = Character("Bella",callback=speaker("Bella"), color='#ff6992', image = "Bella_side", ctc="ctc", ctc_position="fixed")
define te = Character("Tetra",callback=speaker("Tetra"), color='#ff6992', image = "Bella_side", ctc="ctc", ctc_position="fixed")

#Viruses
define i = Character("ILY",callback=speaker("ILY"), color='#f00', image = "ILY_side", ctc="ctc", ctc_position="fixed")
define br= Character("Brain",callback=speaker("Brain"), color ='#f842d6',image ="Brain_side", ctc="ctc", ctc_position="fixed")
define m = Character("Melissa",callback=speaker("Melissa"), color='#ff8a00', image ="Melissa_side", ctc="ctc", ctc_position="fixed")
define s = Character("Stella",callback=speaker("Stoned"),what_slow_cps=40, image = "Stoned_side", ctc="ctc", ctc_position="fixed")
define c = Character("Code Red",callback=speaker("CodeRed"), color='#f00',image ="CodeRed_side", ctc="ctc", ctc_position="fixed")

# AntiViruses
define a = Character("Ave",callback=speaker("Ave"), color='#ff8a00', image ="Ave_side", ctc="ctc", ctc_position="fixed")
define b = Character("Bitwulf",callback=speaker("Bitwulf"),what_slow_cps=40, image = "Bitwulf_side", ctc="ctc", ctc_position="fixed")
define v = Character("Vira",callback=speaker("Vira"), color ='#f00',image ="Vira_side", ctc="ctc", ctc_position="fixed")
define t = Character("Tabby",callback=speaker("Tabby"), color ='#fff',image ="Tabby_side", ctc="ctc", ctc_position="fixed")


# define v = Character("Vira",callback=speaker("Vira"), color ='#f00',image ="Vira_side", ctc="ctc", ctc_position="fixed")


define mu = Character("???",callback=speaker("Melissa"), color='#ff8a00', image ="Melissa_side", ctc="ctc", ctc_position="fixed")

define hx = Character("Hacker X",color = '#088', image = "HackerX_side", ctc="ctc", ctc_position="fixed",callback=speaker("HackerX"))
define cv = Character("Virus Boy",callback=speaker("CodeRed"), color='#f00', ctc="ctc", ctc_position="fixed")
define aa = Character("Antivirus Girl",callback=speaker("Ave"), color='#ff8a00', ctc="ctc", ctc_position="fixed")



define uc = Character("USB-chan",callback=speaker("USB-chan"),color='#f9b9f9', ctc="ctc", ctc_position="fixed")
define uk = Character("USB-kun",callback=speaker("USB-kun"),color='#7ce7ed', ctc="ctc", ctc_position="fixed")

define config.side_image_only_not_showing = True
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
    globals()["ILY_e"] = "normal"
    
    globals()["ILY_eyes"] = "open"
    globals()["ILY_underwear"] = "red" # "red", "small", "" 
    globals()["ILY_outfit"] = "uniform" #bunny, garden, ""
    
    globals()["ILY_hair"] = "default" #""", "down", ""
    # def ILY_damaged():
    #     return 
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
    globals()["Lisa_eyes"] = "open"
    globals()["Lisa_m"] = "smile"
    globals()["Lisa_blush"]= False
    globals()["Lisa_w"] = True
    globals()["Lisa_underwear"] = "red"
    globals()["Lisa_outfit"] = "uniform"
    globals()["Lisa_glasses"] = False

    globals()["Vira_m"] = "smile"
    globals()["Vira_e"] = "mad"
    globals()["Vira_eyes"] = "open"
    globals()["Vira_w"] = False
    
    globals()["Lucida_m"] = "frown"
    globals()["Lucida_e"] = "down"
    globals()["Lucida_eyes"] = "open"
    globals()["Lucida_w"] = False

    globals()["Ave_e"] = "down"
    globals()["Ave_eyes"] = "open"
    globals()["Ave_m"] = "frown"
    globals()["Ave_w"] = True

    globals()["Melissa_e"] = "up"
    globals()["Melissa_m"] = "smile"
    globals()["Melissa_w"] = True
    
    globals()["Bitwulf_e"] = "normal"
    globals()["Bitwulf_m"] = "1"
    globals()["Bitwulf_w"] = True

    globals()["Stoned_e"] = "normal"
    globals()["Stoned_eyes"] = "open"
    globals()["Stoned_m"] = "happy"
    globals()["Stoned_w"] = True

    globals()["Bella_e"] = "normal"
    globals()["Bella_eyes"] = "open"
    globals()["Bella_m"] = "smile"
    globals()["Bella_w"] = True

    globals()["CodeRed_e"] = "normal"
    globals()["CodeRed_m"] = "frown"
    globals()["CodeRed_w"] = True

    globals()["Brain_m"] = "smile"
    globals()["Brain_p"] = "1"
    globals()["Brain_e"] = "down"
    globals()["Brain_eyes"] = "open"
    globals()["Brain_w"] = True
    
    

    globals()["showsideimage"] = False


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

    def ILY_outfit_function():
        global ILY_outfit
        
        # el
        if playerHP<=playerHPMax/8:
            return "images/Characters/ILY/Full/ILY_v2_"+ILY_outfit+("_damaged" if playerHP<=playerHPMax/8 else "")+".png"
        # elif playerHP>playerHPMax/8:
        #     ILY_outfit =""
        #     return "Null"
        else:
            return "images/Characters/ILY/Full/ILY_v2_"+ILY_outfit+".png"
    


    def speaker_callback(name, event, **kwargs):

        global speaking

        if (name == "John"):
            globals()["showsideimage"]=John_w
        elif (name == "Hilbert"):
            globals()["showsideimage"]=Hilbert_w
        elif (name == "Melissa"):
            globals()["showsideimage"]=Melissa_w
        elif (name == "Stoned"):
            globals()["showsideimage"]=Stoned_w
        elif (name == "Bitwulf"):
            globals()["showsideimage"]=Bitwulf_w
        elif (name == "Brain"):
            globals()["showsideimage"]=Brain_w
        elif (name == "ILY"):
            globals()["showsideimage"]=ILY_w
        elif (name == "Lisa"):
            globals()["showsideimage"]=Lisa_w
        elif (name == "Lucida"):
            globals()["showsideimage"]=Lucida_w
        elif (name == "Ave"):
            globals()["showsideimage"]=Ave_w
        elif (name == "Vira"):
            globals()["showsideimage"]=Vira_w
        elif (name == "CodeRed"):
            globals()["showsideimage"]=CodeRed_w
        elif (name == "Bella"):
            globals()["showsideimage"]=Bella_w
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
            globals()["ILY_e"] = 'up'

        elif (emotion == "smile2"):
            globals()["ILY_m"] = "smile2"
            globals()["ILY_e"] = 'up'

        elif (emotion == "smile3"):
            globals()["ILY_m"] = "smile3"
            globals()["ILY_e"] = 'up'

        elif(emotion == "frown"):
            globals()["ILY_m"] = "frown"
            globals()["ILY_e"] = 'normal'
        elif(emotion == "mad"):
            globals()["ILY_m"] = "frown"
            globals()["ILY_e"] = 'down'
        elif(emotion == "o"):
            globals()["ILY_m"] = "o"
            globals()["ILY_e"] = 'up'

        else:
            raise ValueError("Unknown emotion entered: " + emotion)




    def JohnSprite(emotion="smile"):
        ## Make everything lowercase
        emotion = emotion.lower()

        if (emotion == "normal"):
            globals()["John_m"] = "smile"
            globals()["John_e"] = "normal"
        elif (emotion == "happy"):
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
            globals()["Vira_eyes"] = "open"

        elif (emotion == "frown"):
            globals()["Vira_m"] = "frown"
            globals()["Vira_e"] = "normal"
            globals()["Vira_eyes"] = "open"

        elif (emotion == "mad"):
            globals()["Vira_m"] = "frown"
            globals()["Vira_e"] = "mad"
            globals()["Vira_eyes"] = "open"

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
        "ILY_w==True",LiveCrop((200,60, 440,565), (At("ILYFullBody", zoomtrans(0.9)))),
        "ILY_w==False","Null_side"
    )
    zoom 0.38
image ILYside2:
    LiveCrop((200,60, 440,565), "ILYside3")

image ILYside3:
    "ILYFullBody"
    zoom 0.9

image Icon_ILY:
    mesh True
    LiveCrop((230,80, 520,700), "ILYFullBody")
    zoom 0.22


image ILY:
    mesh True

    "ILYFullBody"
    zoom 0.5
    yanchor 0.50
    ypos 1.0
    linear 1.0 yoffset 0
    linear 1.0 yoffset 5
    repeat

image ILYold:
    "ILYFull"
    zoom 0.5
    yalign 0.1 xalign 0.0
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
    linear 1.0 yoffset 0
    linear 1.0 yoffset 5
    repeat
transform ilyfix(deg):
    zoom deg
    xoffset 60
    xpos 0
    ypos 0

image ILY_outfit:
    ""+ILY_outfit_function()
    # "images/Characters/ILY/Full/ILY_v2_"+ILY_outfit+("_damaged" if playerHP<=playerHPMax/4 else "")+".png"
layeredimage ILYFullBody:
    always:
        ConditionSwitch("ILY_hair!='default'",At("images/Characters/ILY/Full/ILY_Full_hairback.png",ilyfix(0.5)),"ILY_hair=='default'",Null())
    always:
        At("images/Characters/ILY/Full/ILY_Full_base.png",ilyfix(0.5)) #pose
    always:
        ConditionSwitch("ILY_stockings!=''",At("images/Characters/ILY/Full/ILY_[ILY_stockings].png",ilyfix(0.5)),"ILY_stockings==''",Null()) #stockings
    always:
            ConditionSwitch("ILY_underwear!=''",At(("images/Characters/ILY/Full/ILY_v2_underwear_[ILY_underwear].png"),ilyfix(0.5)),"ILY_underwear==''",Null()) #underwear
    always:
            ConditionSwitch("ILY_outfit!=''",At("ILY_outfit",ilyfix(0.5)),"ILY_outfit==''",Null()) #outfit
    always:
        At("images/Characters/ILY/Full/ILY_Full_face.png",ilyfix(0.5))
    always:
        At("images/Characters/ILY/Full/ILY_Full_hair_[ILY_hair].png",ilyfix(0.5))
    always:
        ConditionSwitch(
            "ILY_eyes=='open'",
            At("ILYEyes[ILY_p]",ilyfix(0.5)),
            "ILY_eyes!='open'",
            At("images/Characters/ILY/ILY_eyes[ILY_eyes].png",ilyfix(0.5)),
            )
    always:
        At("images/Characters/ILY/ILY_e[ILY_e].png",ilyfix(0.5))
    always:
        At("images/Characters/ILY/ILY_heart0.png",ilyfix(0.5))
    always:
        At(WhileSpeaking(
            "ILY",
            ConditionSwitch(
                "('smile' in ILY_m)","ILYMouthsmile",
                "('smile' not in ILY_m)","ILYMouthfrown"
                ),
            "images/Characters/ILY/ILY_m[ILY_m].png"
            ),ilyfix(0.5))
image ILYVtuber:
    LiveComposite(
    (0.75, 0.75), #(544,600),
    (0, 0), "images/Characters/ILY/ILY_Full_base[ILY_p].png", #nude base
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


#########
## John
#########


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
    pause .1
    "images/Characters/John/John_mouth_O2.png"
    pause .1
    "images/Characters/John/John_mouth_O.png"
    pause .1
    "images/Characters/John/John_mouth_O2.png"
    pause .1
    "images/Characters/John/John_mouth_frown.png"
    pause .1
    "images/Characters/John/John_mouth_frown_midopen.png"
    pause .1
    "images/Characters/John/John_mouth_frown_open.png"
    pause .1
    "images/Characters/John/John_mouth_frown_midopen.png"
    pause .1
    "images/Characters/John/John_mouth_frown.png"
    pause .1
    repeat
image JohnFull:
    # "images/Characters/John/John_full.png"
    LiveComposite(
        (999,2353),
        (0, 0), At("images/Characters/John/John_base.png",zoomtrans(0.5)),
        (0, 0), WhileSpeaking(
            "John",
            ConditionSwitch(
                "('smile' in John_m)",At("JohnMouthsmile",zoomtrans(0.5)),
                "('smile' not in John_m)",At("JohnMouthfrown",zoomtrans(0.5))
            ),
            At("images/Characters/John/John_mouth_[John_m].png",zoomtrans(0.5))


            ),
        (0, 0), At("images/Characters/John/John_eyebrows_[John_e].png",zoomtrans(0.5)),
        (0, 0), At("JohnEyes",zoomtrans(0.5)),
        (0, 0), At("images/Characters/John/John_glasses.png",zoomtrans(0.5))
        # (0, 0), "images/Characters/John/Johnshades.png",
        )
    zoom 0.7
image JohnFullside:
    "JohnFull"
    zoom 0.97
image John sidew:
    LiveCrop((242,38, 300,385), "JohnFullside")
    zoom 0.56

image John:
    "JohnFull"
    zoom 0.85
    yanchor 0.53 ypos 1.0 xalign 1.0


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
layeredimage Lisafull:
    always:
        "images/Characters/Lisa/Lisa_base.png"
    always:
        "images/Characters/Lisa/Lisa_underwear_[Lisa_underwear].png"
    always:
        "images/Characters/Lisa/Lisa_dress_[Lisa_outfit].png"
    always:
        WhileSpeaking(
            "Lisa",
            # ConditionSwitch(
            ConditionSwitch(
                "('smile' in Lisa_m)","LisaMouthsmile",
                "('smile' not in Lisa_m)","LisaMouthfrown",
                ),
            "images/Characters/Lisa/Lisa_m[Lisa_m].png"
            )
    always:
        "images/Characters/Lisa/Lisa_e[Lisa_e].png"
    always:
        ConditionSwitch(
            "Lisa_blush==True","images/Characters/Lisa/Lisa_blush.png",
            "Lisa_blush==False",Null(),
            )
    always:
        
        ConditionSwitch(
            "('close' in Lisa_eyes)","images/Characters/Lisa/Lisa_e[Lisa_eyes].png",
            "('close' not in Lisa_eyes)","LisaEyes",
            )
    always:
        # "images/Characters/Lisa/LisaGlasses.png"
        ConditionSwitch(
            "Lisa_glasses==True","images/Characters/Lisa/LisaGlasses.png",
            "Lisa_glasses==False",Null(),
            )
    zoom 0.31
image Lisa:
    "Lisafull"
    yanchor 0.0 ypos 0.01
    # linear 1.0 yoffset 0
    # pause .5
    # linear 1.0 yoffset 5
    # pause .5
    # repeat
image Lisafullside:
    "Lisafull"
    zoom 1.13
image Lisa sidew:
    LiveCrop((130,20, 300,385), "Lisafullside")
    zoom 0.56
image side Lisa_side:
    ConditionSwitch(
        "Lisa_w==True","Lisa sidew",
        "Lisa_w==False","Null_side")

image Null_side:
    Null()

image LisaEyes:
    choice:
        "images/Characters/Lisa/Lisa_eyes_[Lisa_eyes].png"
        pause 1.0
        "images/Characters/Lisa/Lisa_eclose1.png"
        pause 0.07
        "images/Characters/Lisa/Lisa_eclosedown.png"
        pause 0.1
        "images/Characters/Lisa/Lisa_eclose1.png"
        pause 0.07
    choice:
        "images/Characters/Lisa/Lisa_eyes_[Lisa_eyes].png"
        pause 5.0
    choice:
        "images/Characters/Lisa/Lisa_eyes_[Lisa_eyes].png"
        pause 4.0
    choice:
        "images/Characters/Lisa/Lisa_eyes_[Lisa_eyes].png"
        pause 1.5
        "images/Characters/Lisa/Lisa_eclose1.png"
        pause 0.07
        "images/Characters/Lisa/Lisa_eclosedown.png"
        pause 0.1
        "images/Characters/Lisa/Lisa_eclose1.png"
        pause 0.07
        "images/Characters/Lisa/Lisa_eclosedown.png"
        pause 0.1
        "images/Characters/Lisa/Lisa_eyes_[Lisa_eyes].png"
        pause 1.5
    repeat

image LisaMouthsmile:
    "images/Characters/Lisa/Lisa_mopen1.png"
    pause .1
    "images/Characters/Lisa/Lisa_mopen2.png"
    pause .1
    "images/Characters/Lisa/Lisa_mopen1.png"
    pause .1
    "images/Characters/Lisa/Lisa_msmile.png"
    pause .1
    "images/Characters/Lisa/Lisa_msmile2.png"
    pause .1
    "images/Characters/Lisa/Lisa_msmile3.png"
    pause .1
    "images/Characters/Lisa/Lisa_msmile2.png"
    pause .1
    "images/Characters/Lisa/Lisa_msmile.png"
    pause .1
    repeat

image LisaMouthfrown:
    "images/Characters/Lisa/Lisa_mopen1.png"
    pause .1
    "images/Characters/Lisa/Lisa_mopen2.png"
    pause .1
    "images/Characters/Lisa/Lisa_mopen1.png"
    pause .1
    "images/Characters/Lisa/Lisa_mfrown.png"
    pause .1
    
    "images/Characters/Lisa/Lisa_mopen1.png"
    pause .1
    "images/Characters/Lisa/Lisa_mfrown3.png"
    pause .1
    "images/Characters/Lisa/Lisa_mopen1.png"
    pause .1
    "images/Characters/Lisa/Lisa_mfrown.png"
    pause .1
    
    repeat

###########
## Lucida
###########


layeredimage Lucidafull:
    always:
        "images/Characters/Lucida/Lucida_base.png"
    always:
        WhileSpeaking(
            "Lucida",
            # ConditionSwitch(
            ConditionSwitch(
                "('smile' in Lucida_m)","LucidaMouthsmile",
                "('smile' not in Lucida_m)","LucidaMouthfrown",
                ),
            "images/Characters/Lucida/Lucida_m[Lucida_m].png"
            )
    always:
        "images/Characters/Lucida/Lucida_eyebrows_[Lucida_e].png"
    # always:
    #     ConditionSwitch(
    #         "Lucida_blush==True","images/Characters/Lucida/Lucida_blush.png",
    #         "Lucida_blush==False",Null(),
    #         )
    always:
        
        ConditionSwitch(
            "('close' in Lucida_eyes)","images/Characters/Lucida/Lucida_eyes_[Lucida_eyes].png",
            "('close' not in Lucida_eyes)","LucidaEyes",
            )
    
    zoom 0.22
image Lucida:
    "Lucidafull"
    yanchor 0.0 ypos 0.01
    # linear 1.0 yoffset 0
    # pause .5
    # linear 1.0 yoffset 5
    # pause .5
    # repeat
image Lucidafullside:
    "Lucidafull"
    zoom 1.13
image Lucida sidew:
    LiveCrop((130,20, 300,385), "Lucidafullside")
    zoom 0.56
image side Lucida_side:
    ConditionSwitch(
        "Lucida_w==True","Lucida sidew",
        "Lucida_w==False","Null_side")

image Null_side:
    Null(width=440,height=565)

image LucidaEyes:
    choice:
        "images/Characters/Lucida/Lucida_eyes_[Lucida_eyes].png"
        pause 1.0
        "images/Characters/Lucida/Lucida_eyes_midopen.png"
        pause 0.07
        "images/Characters/Lucida/Lucida_eyes_closed.png"
        pause 0.1
        "images/Characters/Lucida/Lucida_eyes_midopen.png"
        pause 0.07
    choice:
        "images/Characters/Lucida/Lucida_eyes_[Lucida_eyes].png"
        pause 5.0
    choice:
        "images/Characters/Lucida/Lucida_eyes_[Lucida_eyes].png"
        pause 4.0
    choice:
        "images/Characters/Lucida/Lucida_eyes_[Lucida_eyes].png"
        pause 1.5
        "images/Characters/Lucida/Lucida_eyes_midopen.png"
        pause 0.07
        "images/Characters/Lucida/Lucida_eyes_closed.png"
        pause 0.1
        "images/Characters/Lucida/Lucida_eyes_midopen.png"
        pause 0.07
        "images/Characters/Lucida/Lucida_eyes_closed.png"
        pause 0.1
        "images/Characters/Lucida/Lucida_eyes_[Lucida_eyes].png"
        pause 1.5
    repeat

image LucidaMouthsmile:
    "images/Characters/Lucida/Lucida_mmidopenfrown.png"
    pause .1
    "images/Characters/Lucida/Lucida_mopenfrown.png"
    pause .1
    "images/Characters/Lucida/Lucida_mmidopenfrown.png"
    pause .1
    "images/Characters/Lucida/Lucida_msmile.png"
    pause .1
    "images/Characters/Lucida/Lucida_mmidopensmile.png"
    pause .1
    "images/Characters/Lucida/Lucida_mopensmile.png"
    pause .1
    "images/Characters/Lucida/Lucida_mmidopensmile.png"
    pause .1
    "images/Characters/Lucida/Lucida_msmile.png"
    pause .1
    repeat

image LucidaMouthfrown:
    "images/Characters/Lucida/Lucida_mmidopenfrown.png"
    pause .1
    "images/Characters/Lucida/Lucida_mopenfrown.png"
    pause .1
    "images/Characters/Lucida/Lucida_mmidopenfrown.png"
    pause .1
    "images/Characters/Lucida/Lucida_mfrown.png"
    pause .1
    
    # "images/Characters/Lucida/Lucida_mmidopenfrown.png"
    # pause .1
    # "images/Characters/Lucida/Lucida_mopenfrown.png"
    # pause .1
    # "images/Characters/Lucida/Lucida_mmidopenfrown.png"
    # pause .1
    # "images/Characters/Lucida/Lucida_mfrown.png"
    # pause .1
    
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
        (0, 0), At("images/Characters/Vira/Vira_p.png",zoomtrans(0.36697247706)),
        (0, 0), At("images/Characters/Vira/Vira_e[Vira_e].png",zoomtrans(0.36697247706)), #eyebrows
        (0, 0), At("ViraEyes",zoomtrans(0.36697247706)),#eyes
        (0, 0), At(WhileSpeaking(
            "Vira",
            ConditionSwitch(
                "('smile' in Vira_m)","ViraMouthsmile",
                "('smile' not in Vira_m)","ViraMouthfrown"
            ),
            "images/Characters/Vira/Vira_m[Vira_m].png"
        ),zoomtrans(0.36697247706))
    )
image Virasmall:
    "ViraFull"
    zoom 2.0
image Vira sidew:
    LiveCrop((140,40, 300,385), "ViraFull")
    zoom 0.56
    
image side Vira_side:
    ConditionSwitch(
        "Vira_w==True","Vira sidew",
        "Vira_w==False","Null_side")

image Icon_Vira:
    LiveCrop((280,100, 520,700), "Virasmall")
    
    zoom 0.22
image ViraMouthsmile:
    "images/Characters/Vira/Vira_msmile2.png"
    pause .08
    "images/Characters/Vira/Vira_msmile3.png"
    pause .08
    "images/Characters/Vira/Vira_msmile2.png"
    pause .08
    "images/Characters/Vira/Vira_msmile.png"
    pause .08
    "images/Characters/Vira/Vira_mO2.png"
    pause .08
    "images/Characters/Vira/Vira_mO.png"
    pause .1
    "images/Characters/Vira/Vira_mO2.png"
    pause .08
    repeat
image ViraEyes:
    choice:
        "images/Characters/Vira/Vira_eyes_[Vira_eyes].png"
        pause 1.0
        "images/Characters/Vira/Vira_eyes_midclose.png"
        pause 0.07
        "images/Characters/Vira/Vira_eyes_closed.png"
        pause 0.1
        "images/Characters/Vira/Vira_eyes_midclose.png"
        pause 0.07
    choice:
        "images/Characters/Vira/Vira_eyes_[Vira_eyes].png"
        pause 5.0
    choice:
        "images/Characters/Vira/Vira_eyes_[Vira_eyes].png"
        pause 4.0
    choice:
        "images/Characters/Vira/Vira_eyes_[Vira_eyes].png"
        pause 1.5
        "images/Characters/Vira/Vira_eyes_midclose.png"
        pause 0.07
        "images/Characters/Vira/Vira_eyes_closed.png"
        pause 0.1
        "images/Characters/Vira/Vira_eyes_midclose.png"
        pause 0.07
        "images/Characters/Vira/Vira_eyes_closed.png"
        pause 0.1
        "images/Characters/Vira/Vira_eyes_[Vira_eyes].png"
        pause 1.5
    repeat
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




image Icon_TrojanHorse:

    mesh True
    LiveCrop((0,0, 520,700), "Trojan")
    zoom 0.25
#########
## Code Red
#########

image CodeRed:
    "CodeRedFull"
    yanchor 0.76 ypos 1.0
    linear 1.0 yoffset 0
    pause .5
    linear 1.0 yoffset 5
    pause .5
    repeat

image CodeRedFull:
    LiveComposite(
        (714,1025),
        (0, 0), At("images/Characters/Code Red/CODE RED_base.png",zoomtrans(0.36)),
        (0, 0),At("images/Characters/Code Red/CODE RED_eyes.png",zoomtrans(0.36)),
        (0, 0),At("images/Characters/Code Red/CODE RED_e[CodeRed_e].png",zoomtrans(0.36)),
        (0, 0), WhileSpeaking(
            "CodeRed",
            At("CodeRed mouth",zoomtrans(0.36)),
            At("images/Characters/Code Red/CODE RED_mclosed.png",zoomtrans(0.36))
        )
    )
    
image CodeRed sidew:
    LiveCrop((140,40, 300,385), "CodeRedFull")
    zoom 0.56
image side CodeRed_side:
    ConditionSwitch(
        "CodeRed_w==True","CodeRed sidew",
        "CodeRed_w==False","Null_side")
image CodeRedFullzoomed:
    "CodeRedFull"
    zoom 1.6
image Icon_Code Red:
    LiveCrop((280,100, 440,565), "CodeRedFullzoomed")
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
    mesh True
    "MelissaFull"
    yanchor 0.5 ypos 1.0 zoom 0.9
    linear 1.0 yoffset 0
    pause .5
    linear 1.0 yoffset 5
    pause .5
    repeat
image Melissajump:
    mesh True
    "MelissaFull base_jump"
    yanchor 0.50 ypos 1.0 zoom 0.9
    ease 0.35 yoffset -30
    pause 0.1
    ease 0.1 yoffset 5
    ease 0.2 yoffset 0
    # linear 1.0 yoffset 0
    # pause .5
    # linear 1.0 yoffset 5
    # pause .5
    
image Melissajumping:
    
    "MelissaFull base_jump"
    yanchor 0.50 ypos 1.0 zoom 0.9
    mesh True
    ease 0.3 yoffset -30
    pause 0.1
    ease 0.3 yoffset 5
    ease 0.15 yoffset 0
    # linear 1.0 yoffset 0
    # pause .5
    # linear 1.0 yoffset 5
    # pause .5
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
    "images/Characters/Melissa/Melissa_mopen1.png"
    pause .1
    "images/Characters/Melissa/Melissa_mopen.png"
    pause .08
    "images/Characters/Melissa/Melissa_mopen1.png"
    pause .1
    "images/Characters/Melissa/Melissa_mfrown.png"
    pause .1
    "images/Characters/Melissa/Melissa_mopen1.png"
    pause .1
    "images/Characters/Melissa/Melissa_mopen2.png"
    pause .12
    "images/Characters/Melissa/Melissa_mopen1.png"
    pause .1
    repeat
image Melissa_base_jump:
    "images/Characters/Melissa/Melissa_base_down1.png"
    pause 0.05
    "images/Characters/Melissa/Melissa_base_down2.png"
    pause 0.05
    "images/Characters/Melissa/Melissa_base_down3.png"
    pause 0.05
    "images/Characters/Melissa/Melissa_base_down2.png"
    pause 0.05
    "images/Characters/Melissa/Melissa_base.png"
    pause 0.05
    "images/Characters/Melissa/Melissa_base_up1.png"
    pause 0.05
    "images/Characters/Melissa/Melissa_base_up2.png"
    pause 0.05
    "images/Characters/Melissa/Melissa_base_up3.png"
    pause 0.2
    "images/Characters/Melissa/Melissa_base_up2.png"
    pause 0.05
    "images/Characters/Melissa/Melissa_base_up1.png"
    pause 0.05
    "images/Characters/Melissa/Melissa_base.png"
    pause 0.05
    "images/Characters/Melissa/Melissa_base_down1.png"
    pause 0.05
    "images/Characters/Melissa/Melissa_base_down2.png"
    pause 0.05
    "images/Characters/Melissa/Melissa_base_down3.png"
    pause 0.05
    "images/Characters/Melissa/Melissa_base_down2.png"
    pause 0.05
    "images/Characters/Melissa/Melissa_base_down1.png"
    pause 0.05
    "images/Characters/Melissa/Melissa_base.png"
    pause 0.05
    
layeredimage MelissaFull:
    # always:
    #     "images/Characters/Melissa/Melissa_base.png"
    group base:
        attribute base_normal default:
            "images/Characters/Melissa/Melissa_base.png"
        attribute base_jump:   
            "Melissa_base_jump"
    always:
        WhileSpeaking(
            "Melissa",
            ConditionSwitch(
                "('smile' in Melissa_m)","MelissaMouthsmile",
                "('smile' not in Melissa_m)","MelissaMouthfrown"
            ),
            "images/Characters/Melissa/Melissa_m[Melissa_m].png"
            )
    always:
        "images/Characters/Melissa/Melissa_e[Melissa_e].png"
    always:
        "MelissaEyes"
    zoom 0.22
    
image MelissaFullBody:
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
    LiveCrop((75,30, 300,385), "MelissaFull")
    zoom 0.56




image side Melissa_side:
    ConditionSwitch(
        "Melissa_w==True","Melissa sidew",
        "Melissa_w==False","Null_side")
#########
## Ave
#########
image Ave:
    "AveFull"
    yanchor 0.46 ypos 1.0 zoom 0.9 xalign 0.5

    linear 1.0 yoffset 0
    pause .5
    linear 1.0 yoffset 5
    pause .5
    repeat


image AveFull:
    LiveComposite(
        (4189,7278),
        (0, 0), "images/Characters/Ave/Avebase.png",
        (0, 0), WhileSpeaking(
            "Ave",
            ConditionSwitch(
                "('smile' in Ave_m)","AveMouthsmile",
                "('smile' not in Ave_m)","AveMouthfrown",
                ),
            "images/Characters/Ave/Ave_m[Ave_m].png"
            ),
        (0, 0), "images/Characters/Ave/Ave_e[Ave_e].png",

        (0, 0), "AveEyes",#eyes
        (0, 0), "images/Characters/Ave/Aveshades.png",
        )
    
    zoom 0.24
image AveEyes:
    choice:
        "images/Characters/Ave/Ave_eyes.png"
        pause 1.0
        "images/Characters/Ave/Ave_eyes_midclose.png"
        pause 0.07
        "images/Characters/Ave/Ave_eyes_closed.png"
        pause 0.1
        "images/Characters/Ave/Ave_eyes_midclose.png"
        pause 0.07
    choice:
        "images/Characters/Ave/Ave_eyes.png"
        pause 5.0
    choice:
        "images/Characters/Ave/Ave_eyes.png"
        pause 4.0
    choice:
        "images/Characters/Ave/Ave_eyes.png"
        pause 1.5
        "images/Characters/Ave/Ave_eyes_midclose.png"
        pause 0.07
        "images/Characters/Ave/Ave_eyes_closed.png"
        pause 0.1
        "images/Characters/Ave/Ave_eyes_midclose.png"
        pause 0.07
        "images/Characters/Ave/Ave_eyes_closed.png"
        pause 0.1
        "images/Characters/Ave/Ave_eyes.png"
        pause 1.5
    repeat
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

image AveMouthsmile:
    "images/Characters/Ave/Ave_msmile2.png"
    pause .1
    "images/Characters/Ave/Ave_msmile3.png"
    pause .1
    "images/Characters/Ave/Ave_msmile2.png"
    pause .1
    "images/Characters/Ave/Ave_msmile.png"
    pause .1
    "images/Characters/Ave/Ave_mopen1.png"
    pause .1
    "images/Characters/Ave/Ave_mopen2.png"
    pause .1
    "images/Characters/Ave/Ave_mopen1.png"
    pause .1
    "images/Characters/Ave/Ave_msmile.png"
    pause .1
    repeat

image AveMouthfrown:
    "images/Characters/Ave/Ave_mopen1.png"
    pause .1
    "images/Characters/Ave/Ave_mopen2.png"
    pause .1
    "images/Characters/Ave/Ave_mopen1.png"
    pause .1
    "images/Characters/Ave/Ave_mfrown.png"
    pause .1
    
    "images/Characters/Ave/Ave_mopen1.png"
    pause .1
    "images/Characters/Ave/Ave_mO.png"
    pause .1
    "images/Characters/Ave/Ave_mopen1.png"
    pause .1
    "images/Characters/Ave/Ave_mfrown.png"
    pause .1
    
    repeat
image Ave sidew:
    LiveCrop((150,40, 300,385), "AveFull")
    zoom 0.56
image side Ave_side:
    ConditionSwitch(
        "Ave_w==True","Ave sidew",
        "Ave_w==False","Null_side")

image AveFullzoom:
    "AveFull"
    zoom 1.58
image Icon_Ave:
    mesh True
    LiveCrop((220,80, 520,700), "AveFullzoom")
    zoom 0.25


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
    ypos 1.0 yanchor 0.56 zoom 0.92
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
        (0, 0), At("images/Characters/Hilbert/Hilbert_base.png",ilyfix(0.5)),
        (0, 0), WhileSpeaking(
            "Hilbert",
            ConditionSwitch(
                "('smile' in Hilbert_m)",At("HilbertMouthsmile",ilyfix(0.5)),
                "('smile' not in Hilbert_m)",At("HilbertMouthfrown",ilyfix(0.5))
            ),
            At("images/Characters/Hilbert/Hilbert_mouth_[Hilbert_m].png",ilyfix(0.5))


            ),
        (0, 0), At("images/Characters/Hilbert/Hilbert_eyebrows_[Hilbert_e].png",ilyfix(0.5)),
        (0, 0), At("HilbertEyes",ilyfix(0.5))#eyes
        # (0, 0), "images/Characters/Hilbert/Hilbertshades.png",
        )
    zoom 0.7
image Hilbert sidew:
    LiveCrop((120,24, 300,385), "HilbertFull")
    zoom 0.56




image side Hilbert_side:
    ConditionSwitch(
        "Hilbert_w==True","Hilbert sidew",
        "Hilbert_w==False","Null_side")
#########
## Hacker X
#########
image side HackerX_side:
    "images/Characters/HackerX/HackerX.png"
    zoom 0.38

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
        "Nick_w==False","Null_side")


#########
## Stella
#########

image Stoned_eyes_open:
    "images/Characters/Stoned/Stoned_eyes_[Stoned_eyes].png"
    pause 1.0
    choice:
        "images/Characters/Stoned/Stoned_eyes_[Stoned_eyes].png"
        pause 2.0
    choice:
        "images/Characters/Stoned/Stoned_eyes_[Stoned_eyes].png"
        pause 3.0
    choice:

        "images/Characters/Stoned/Stoned_eyes_midclose.png"
        pause 0.1
        "images/Characters/Stoned/Stoned_eyes_closed.png"
        pause 0.1
        "images/Characters/Stoned/Stoned_eyes_midclose.png"
        pause 0.1

    choice:
        "images/Characters/Stoned/Stoned_eyes_midclose.png"
        pause 0.05
        "images/Characters/Stoned/Stoned_eyes_closed.png"
        pause 0.1
        "images/Characters/Stoned/Stoned_eyes_midclose.png"
        pause 0.05
        "images/Characters/Stoned/Stoned_eyes_[Stoned_eyes].png"
        pause 0.1

        repeat 2
    repeat
image Stoned_eyes_midclose:
    "images/Characters/Stoned/Stoned_eyes_midclose.png"
    pause 1.0
    choice:
        "images/Characters/Stoned/Stoned_eyes_midclose.png"
        pause 2.0
    choice:
        "images/Characters/Stoned/Stoned_eyes_midclose.png"
        pause 3.0
    choice:

        "images/Characters/Stoned/Stoned_eyes_midclose.png"
        pause 0.1
        "images/Characters/Stoned/Stoned_eyes_closed.png"
        pause 0.1
        "images/Characters/Stoned/Stoned_eyes_midclose.png"
        pause 0.1

    choice:
        "images/Characters/Stoned/Stoned_eyes_midclose.png"
        pause 0.05
        "images/Characters/Stoned/Stoned_eyes_closed.png"
        pause 0.1
        "images/Characters/Stoned/Stoned_eyes_midclose.png"
        pause 0.15

        repeat 2
    repeat
image Stoned_Guns:
    "images/Characters/Stoned/Stoned_Cannons.png"
    
    linear 1.0 yoffset 40
    linear 1.0 yoffset 0
    repeat
layeredimage StonedFull:
    always:
        "images/Characters/Stoned/Stoned_base.png"
    group eyebrows:
        attribute normal default:
            "images/Characters/Stoned/Stoned_e[Stoned_e].png"
    group eyebrows:
        attribute open default:
            "Stoned_eyes_[Stoned_eyes]"
        attribute midclose:
            "Stoned_eyes_midclose"
        attribute closed:
            "images/Characters/Stoned/Stoned_eyes_closed.png"
    always:
        WhileSpeaking("Stoned",("Stoned_m[Stoned_m]"),"images/Characters/Stoned/Stoned_m[Stoned_m].png")
    always:
        "images/Characters/Stoned/Stoned_glass.png"
    # always:
    #     "Stoned_Guns"
    xalign 0.5
    
# zoom 0.60

    # LiveComposite(
    # (761,1695),
    # (0,0),"images/Characters/Stoned/Stoned_base.png",
    # (0,0),"images/Characters/Stoned/Stoned_e[Stoned_e].png",
    # (0,0),"Stoned_eyes_[Stoned_eyes]",
    # (0,0),WhileSpeaking("Stoned",("Stoned_m[Stoned_m]"),"images/Characters/Stoned/Stoned_m[Stoned_m].png"),
    # (0,0),"images/Characters/Stoned/Stoned_glass.png"
    # (0,0),"Stoned_Guns"
    # )
    # zoom 0.93 xalign 0.5 

image Stoned:
    # (LiveCrop((479,0,611,2413),"StonedFull"))
    "StonedFull"
    # xoffset -200
    yanchor 0.58 ypos 1.0  zoom 0.56
    # zoom 0.56 
    # linear 1.0 yoffset 0
    # pause .5
    # linear 1.0 yoffset 5
    # pause .5
    # repeat
image Stonedshop:
    "Stoned"
    xoffset -200
image Stonedsmall:
    "StonedFull"
    zoom 0.60
image side Stoned_side:
    ConditionSwitch(
            "Stoned_w==True",(LiveCrop((320,150,300,385),"Stonedsmall")),
            "Stoned_w==False","Null_side"
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
    pause .16
    # "images/Characters/Stoned/Stoned_mopen2.png"
    # pause .08
    "images/Characters/Stoned/Stoned_msad.png"
    pause .08
    repeat
image Stoned_mopen2:

    "images/Characters/Stoned/Stoned_mopen2.png"
    pause .08
    "images/Characters/Stoned/Stoned_mopenO.png"
    pause .16
    "images/Characters/Stoned/Stoned_mopen2.png"
    pause .08
    "images/Characters/Stoned/Stoned_msad.png"
    pause .08
    repeat
#########
## Bitwulf
#########

image Bitwulf_eyes:
    "images/Characters/Bitwulf/Bitwulf_eyes.png"
    pause 1.0
    choice:
        "images/Characters/Bitwulf/Bitwulf_eyes.png"
        pause 2.0
    choice:
        "images/Characters/Bitwulf/Bitwulf_eyes.png"
        pause 3.0
    choice:

        "images/Characters/Bitwulf/Bitwulf_eyes_midclose.png"
        pause 0.1
        "images/Characters/Bitwulf/Bitwulf_eyes_closed.png"
        pause 0.1
        "images/Characters/Bitwulf/Bitwulf_eyes_midclose.png"
        pause 0.1

    choice:
        "images/Characters/Bitwulf/Bitwulf_eyes_midclose.png"
        pause 0.05
        "images/Characters/Bitwulf/Bitwulf_eyes_closed.png"
        pause 0.1
        "images/Characters/Bitwulf/Bitwulf_eyes_midclose.png"
        pause 0.05
        "images/Characters/Bitwulf/Bitwulf_eyes.png"
        pause 0.1

        repeat 2
    repeat


image Bitwulf:
    LiveComposite(
    (5951,6324),
    (0,0),"images/Characters/Bitwulf/Bitwulf_eyes.png",
    (0,0),"images/Characters/Bitwulf/Bitwulf_base.png",
    # (0,0),"images/Characters/Bitwulf/Bitwulf_e[Bitwulf_e].png",
    (0,0),"Bitwulf_eyes",
    (0,0),WhileSpeaking("Bitwulf",("Bitwulf_jaw[Bitwulf_m]"),"images/Characters/Bitwulf/Bitwulf_jaw[Bitwulf_m].png"),
    (0,0),"images/Characters/Bitwulf/Bitwulf_fang.png",
    # (0,0),"images/Characters/Bitwulf/Bitwulf_glass.png"
    # (0,0),"Bitwulf_Guns"
    )
    zoom 0.25 xalign 0.5 yanchor 0.05 ypos 0.0
image Bitwulfsmall:
    (LiveCrop((260,90,300,385),At("Bitwulf",zoomtrans(0.8))))
image side Bitwulf_side:
    ConditionSwitch(
            "Bitwulf_w==True","Bitwulfsmall",
            "Bitwulf_w==False","Null_side"
        )
    zoom 0.56
image Bitwulf_icon:
    (LiveCrop((260,90,280,280),"Bitwulfsmall"))
    zoom 0.4
image Bitwulf_jaw1:

    "images/Characters/Bitwulf/Bitwulf_jaw1.png"
    pause .16
    "images/Characters/Bitwulf/Bitwulf_jaw2.png"
    pause .08
    "images/Characters/Bitwulf/Bitwulf_jaw3.png"
    pause .16
    "images/Characters/Bitwulf/Bitwulf_jaw2.png"
    pause .08
    repeat
image Bitwulf_msad:
    "images/Characters/Bitwulf/Bitwulf_jaw1.png"
    pause .08
    "images/Characters/Bitwulf/Bitwulf_jaw2.png"
    pause .08
    "images/Characters/Bitwulf/Bitwulf_jaw3.png"
    pause .08
    "images/Characters/Bitwulf/Bitwulf_jaw2.png"
    pause .08
    repeat

### BRAIN

image Brain:
    mesh True

    "BrainFullBody"
    zoom 0.5
    yanchor 0.50
    ypos 1.0
    linear 1.0 yoffset 0
    linear 1.0 yoffset 5
    repeat



image BrainEyes:
    choice:
        "images/Characters/Brain/Brain_eyes.png"
        pause 1.0
        "images/Characters/Brain/Brain_eyes_midclose.png"
        pause 0.07
        "images/Characters/Brain/Brain_eyes_closed.png"
        pause 0.1
        "images/Characters/Brain/Brain_eyes_midclose.png"
        pause 0.07
    choice:
        "images/Characters/Brain/Brain_eyes.png"
        pause 8.0
    choice:
        "images/Characters/Brain/Brain_eyes.png"
        pause 4.0
    choice:
        "images/Characters/Brain/Brain_eyes.png"
        pause 1.5
        "images/Characters/Brain/Brain_eyes_midclose.png"
        pause 0.07
        "images/Characters/Brain/Brain_eyes_closed.png"
        pause 0.1
        "images/Characters/Brain/Brain_eyes_midclose.png"
        pause 0.07
        "images/Characters/Brain/Brain_eyes_closed.png"
        pause 0.1
        "images/Characters/Brain/Brain_eyes.png"
        pause 1.5
    repeat




image BrainMouthsmile:
    "images/Characters/Brain/Brain_mouthsmileopen2.png"
    pause .08
    "images/Characters/Brain/Brain_mouthsmileopen.png"
    pause .05
    "images/Characters/Brain/Brain_mouthsmileopen2.png"
    pause .05
    "images/Characters/Brain/Brain_mouthsmile.png"
    pause .08
    "images/Characters/Brain/Brain_mouthopen2.png"
    pause .05
    "images/Characters/Brain/Brain_mouthopen.png"
    pause .1
    "images/Characters/Brain/Brain_mouthopen2.png"
    pause .08
    "images/Characters/Brain/Brain_mouthsmile.png"
    pause .08
    repeat




image BrainMouthfrown:
    "images/Characters/Brain/Brain_mouthopen2.png"
    pause .08
    "images/Characters/Brain/Brain_mouthopen.png"
    pause .1
    "images/Characters/Brain/Brain_mouthopen2.png"
    pause .08
    "images/Characters/Brain/Brain_mouthfrown.png"
    pause .08
    repeat




image side Brain_side:

    ConditionSwitch(
        "Brain_w==True",LiveCrop((964,440, 440,565), At("BrainFullBody",zoomtrans(0.88))),
        "Brain_w==False","Null_side"
    )
    zoom 0.38


layeredimage BrainFullBody:
    always:
        "images/Characters/Brain/Brain_backring.png"
    always:
        "images/Characters/Brain/Brain_backhair.png"
    always:
        "images/Characters/Brain/Brain_backcloth.png"
    always:
        "images/Characters/Brain/Brain_body.png"
   
    always:
        "images/Characters/Brain/Brain_face.png"
    
    always:
        ConditionSwitch(
            "Brain_eyes=='open'",
            "BrainEyes",
            "Brain_eyes!='open'",
            "images/Characters/Brain/Brain_eyes_[Brain_eyes].png",
            )
    always:
        "images/Characters/Brain/Brain_eyebrows_[Brain_e].png"
    always:
        "images/Characters/Brain/Brain_helmet.png"
    always:
       WhileSpeaking(
            "Brain",
            ConditionSwitch(
                "('smile' in Brain_m)","BrainMouthsmile",
                "('smile' not in Brain_m)","BrainMouthfrown"
                ),
            "images/Characters/Brain/Brain_mouth[Brain_m].png"
            )
image BellaEyes:
    choice:
        "images/Characters/Bella/Bella_eyes_open.png"
        pause 1.0
        "images/Characters/Bella/Bella_eyes_midclose.png"
        pause 0.07
        "images/Characters/Bella/Bella_eyes_closed.png"
        pause 0.1
        "images/Characters/Bella/Bella_eyes_midclose.png"
        pause 0.07
    choice:
        "images/Characters/Bella/Bella_eyes_open.png"
        pause 5.0
    choice:
        "images/Characters/Bella/Bella_eyes_open.png"
        pause 4.0
    choice:
        "images/Characters/Bella/Bella_eyes_open.png"
        pause 1.5
        "images/Characters/Bella/Bella_eyes_midclose.png"
        pause 0.07
        "images/Characters/Bella/Bella_eyes_closed.png"
        pause 0.1
        "images/Characters/Bella/Bella_eyes_midclose.png"
        pause 0.07
        "images/Characters/Bella/Bella_eyes_closed.png"
        pause 0.1
        "images/Characters/Bella/Bella_eyes_open.png"
        pause 1.5
    repeat

image Bella_eyes_open:
    "images/Characters/Bella/Bella_eyes_[Bella_eyes].png"
    pause 1.0
    choice:
        "images/Characters/Bella/Bella_eyes_[Bella_eyes].png"
        pause 2.0
    choice:
        "images/Characters/Bella/Bella_eyes_[Bella_eyes].png"
        pause 3.0
    choice:

        "images/Characters/Bella/Bella_eyes_midclose.png"
        pause 0.1
        "images/Characters/Bella/Bella_eyes_closed.png"
        pause 0.1
        "images/Characters/Bella/Bella_eyes_midclose.png"
        pause 0.1

    choice:
        "images/Characters/Bella/Bella_eyes_midclose.png"
        pause 0.05
        "images/Characters/Bella/Bella_eyes_closed.png"
        pause 0.1
        "images/Characters/Bella/Bella_eyes_midclose.png"
        pause 0.05
        "images/Characters/Bella/Bella_eyes_[Bella_eyes].png"
        pause 0.1

        repeat 2
    repeat
image Bella_eyes_midclose:
    "images/Characters/Bella/Bella_eyes_midclose.png"
    pause 1.0
    choice:
        "images/Characters/Bella/Bella_eyes_midclose.png"
        pause 2.0
    choice:
        "images/Characters/Bella/Bella_eyes_midclose.png"
        pause 3.0
    choice:

        "images/Characters/Bella/Bella_eyes_midclose.png"
        pause 0.1
        "images/Characters/Bella/Bella_eyes_closed.png"
        pause 0.1
        "images/Characters/Bella/Bella_eyes_midclose.png"
        pause 0.1

    choice:
        "images/Characters/Bella/Bella_eyes_midclose.png"
        pause 0.05
        "images/Characters/Bella/Bella_eyes_closed.png"
        pause 0.1
        "images/Characters/Bella/Bella_eyes_midclose.png"
        pause 0.15

        repeat 2
    repeat

image BellaMouthsmile:
    "images/Characters/Bella/Bella_mmidopen.png"
    pause .08
    "images/Characters/Bella/Bella_msmileopen.png"
    pause .05
    "images/Characters/Bella/Bella_mmidopen.png"
    pause .08
    "images/Characters/Bella/Bella_msmile.png"
    pause .08
    "images/Characters/Bella/Bella_mO2.png"
    pause .05
    "images/Characters/Bella/Bella_mO.png"
    pause .1
    "images/Characters/Bella/Bella_mO2.png"
    pause .08
    "images/Characters/Bella/Bella_msmile.png"
    pause .08
    repeat


image BellaMouthfrown:
    "images/Characters/Bella/Bella_mO2.png"
    pause .08
    "images/Characters/Bella/Bella_mO.png"
    pause .1
    "images/Characters/Bella/Bella_mO2.png"
    pause .08
    "images/Characters/Bella/Bella_mfrown.png"
    pause .08
    "images/Characters/Bella/Bella_mO2.png"
    pause .08
    "images/Characters/Bella/Bella_mO3.png"
    pause .1
    "images/Characters/Bella/Bella_mO2.png"
    pause .08
    "images/Characters/Bella/Bella_mfrown.png"
    pause .08
    repeat
layeredimage BellaFullBody:
    always:
        At("images/Characters/Bella/Bella_base.png",ilyfix(0.5)) #pose
    always:
        ConditionSwitch(
            "Bella_eyes=='open'",
            At("BellaEyes",ilyfix(0.5)),
            "Bella_eyes!='open'",
            At("images/Characters/Bella/Bella_eyes_[Bella_eyes].png",ilyfix(0.5)),
            )
    always:
        At("images/Characters/Bella/Bella_e[Bella_e].png",ilyfix(0.5))

    always:
        At(WhileSpeaking(
            "Bella",
            ConditionSwitch(
                "('smile' in Bella_m)","BellaMouthsmile",
                "('smile' not in Bella_m)","BellaMouthfrown"
                ),
            "images/Characters/Bella/Bella_m[Bella_m].png"
            ),ilyfix(0.5))
# image Bella:
image Bella:
    mesh True

    "BellaFullBody"
    zoom 0.5
    yanchor 0.50
    ypos 1.0
    linear 1.0 yoffset 0
    linear 1.0 yoffset 5
    repeat
image side Bella_side:

    ConditionSwitch(
        "Bella_w==True",LiveCrop((230,60, 440,565), (At("BellaFullBody", zoomtrans(0.9)))),
        "Bella_w==False","Null_side"
    )
    zoom 0.38