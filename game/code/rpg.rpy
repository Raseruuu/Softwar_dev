
# screen partylist:

#     frame:
#         xpadding 10 ypadding 10 xalign 0.5 yalign 0.5
#         vbox:

#             text "{b}TEAM{/b}"
#             for i in party:
#                 frame:
#                     hbox:
#                         frame:
#                             yalign 0.5
#                             imagebutton auto "images/rpg/Edit_%s.png" action SetVariable("profile",i[0]), SetVariable("profilearray",i),  ShowMenu("Profile")
#                         add "Icon [i[0]]"
#                         null width 10
#                         vbox:
#                             text "{b}[i[0]]{/b}"
#                             hbox:
#                                 text "{size=18}HP:{/size}"
#                                 null width 120
#                             add "images/rpg/bar.png" at barwidth(i[1],i[2])

#                             text"{color=#999}{size=15}[i[1]]{/color}{/size}"
#                             text "{size=18}Defense:{/size}"
#                             add "images/rpg/bar2.png" at barwidth(i[3],i[2])

#                             text"{color=#999}{size=15}[i[3]]{/color}{/size}"
#                         vbox:
#                             at planzoom
#                             if i[4] =="A":
#                                 imagebutton auto "images/rpg/planA_%s.png" action SetVariable("clk",party.index(i)), Play("sound","sound/click.wav"), Jump("planchange") unhovered SetVariable("btnhovered",1.0)
#                                 null width 100
#                                 for j in i[5]:
#                                     add "images/rpg/[j].png"
#                             elif i[4] =="B":
#                                 imagebutton auto "images/rpg/planB_%s.png" action SetVariable("clk",party.index(i)), Play("sound","sound/click.wav"), Jump("planchange") unhovered SetVariable("btnhovered",1.0)
#                                 null width 100
#                                 for j in i[6]:
#                                     add "images/rpg/[j].png"
#             textbutton "Return" action Return()
#             key 'x'             action Return()
# transform rot90:
#     rotate -90
# transform planzoom:
#     zoom 1.1
# transform hoveredonbutton(btnhovered):

#     linear 0.1 zoom btnhovered

# screen Profile:
#     frame:
#         xpadding 10 ypadding 10 xalign 0.03 yalign 0.04
#         vbox:
#             text "[profile]"
#             frame:
#                 hbox:       #i[0] = name i[1] = HP  i[2] = plan
#                     add "Icon [profilearray[0]]"
#                     null width 10
#                     vbox:
#                         text "{b}[profilearray[0]]{/b}"
#                         hbox:
#                             text "HP:"
#                             null width 120

#                         add "images/rpg/bar.png" at barwidth(profilearray[1],profilearray[2])

#                         text"{color=#999}{size=20}[profilearray[1]]{/color}{/size}"

#                         text "{size=18}Defense:{/size}"
#                         add "images/rpg/bar2.png" at barwidth(profilearray[3],profilearray[2])
#                         text"{color=#999}{size=15}[profilearray[3]]{/color}{/size}"

#                     vbox:
#                         at planzoom
#                         if profilearray[4] =="A":
#                             imagebutton auto "images/rpg/planA_%s.png" action SetVariable("clk",party.index(profilearray)), Play("sound","sound/click.wav"), Jump("planchange") hovered SetVariable("btnhovered",1.2), Play("sound","sound/hover.wav") unhovered SetVariable("btnhovered",1.0) at hoveredonbutton(btnhovered)
#                             null width 120
#                             for j in profilearray[5]:
#                                 add "images/rpg/[j].png"
#                         elif profilearray[4] =="B":
#                             imagebutton auto "images/rpg/planB_%s.png" action SetVariable("clk",party.index(profilearray)), Play("sound","sound/click.wav"), Jump("planchange") hovered SetVariable("btnhovered",1.2), Play("sound","sound/hover.wav") unhovered SetVariable("btnhovered",1.0) at hoveredonbutton(btnhovered)
#                             null width 120
#                             for j in profilearray[6]:
#                                 add "images/rpg/[j].png"



# screen battle_m:
#     vbox:
#         xalign 0.5
#         frame:
#             xalign 0.5
#             text "  SOFTWAR  " xalign 0.5
#         hbox:

#             frame:
#                 xalign 0.5 yalign 0.5

#                 vbox:

#                     xalign 0.5
#                     text "Action"
#                     style_prefix "quick_button"
#                     textbutton "ENGAGE" action Return()
#                     textbutton "DEFEND" action Return()
#                     textbutton "CHANGE PLAN" action Return()

            # frame:
            #     vbox:
            #         text "TEAM"
            #         for i in party:
            #             frame:
            #                 hbox:

            #                     add "Icon [i[0]]"
            #                     null width 10
            #                     vbox:
            #                         text "{b}[i[0]]{/b}"
            #                         hbox:
            #                             text "{size=18}HP:{/size}"
            #                             null width 120
            #                         add "images/rpg/bar.png" at barwidth(i[1],i[2])

            #                         text"{color=#999}{size=15}[i[1]]{/color}{/size}"
            #                         text "{size=18}Defense:{/size}"
            #                         add "images/rpg/bar2.png" at barwidth(i[3],i[2])

            #                         text"{color=#999}{size=15}[i[3]]{/color}{/size}"
            #     xalign 1.0
            #     vbox:
            #             text "ENEMIES"
            #             for enemy in enemies:

            #                     vbox:
            #                       frame:
            #                         vbox:
            #                             text "{b}[enemy[0]]{/b}"
            #                             hbox:
            #                                 text "{size=18}HP:{/size}"
            #                                 null width 150
            #                             add "images/rpg/bar.png" at barwidth(500,500.0)

            #                             text"{color=#999}{size=15}500{/color}{/size}"
            #                             text "{size=18}Defense:{/size}"
            #                             add "images/rpg/bar2.png" at barwidth(100,500.0)

            #                             text"{color=888t1099}{size=15}10{/color}{/size}"

            #                         null width 10
            #                       vbox:
            #                             add "images/rpg/Enemies/[enemy[0]].png" at rpgsize
                                #    at planzoom
                                #    if i[4] =="A":
                                #        imagebutton auto "images/rpg/planA_%s.png" action SetVariable("clk",party.index(i)), Play("sound","sound/click.wav"), Jump("planchange") unhovered SetVariable("btnhovered",1.0)
                                #        null width 100
                                #        for j in i[5]:
                                #            add "images/rpg/[j].png"
                                #    elif i[4] =="B":
                                #        imagebutton auto "images/rpg/planB_%s.png" action SetVariable("clk",party.index(i)), Play("sound","sound/click.wav"), Jump("planchange") unhovered SetVariable("btnhovered",1.0)
                                #        null width 100
                                #        for j in i[6]:
                                #            add "images/rpg/[j].png"


# label startbattle:
#         $ enemies = []
#         $ enemyq = renpy.random.randint(1,4)
#         python:
#          for emy in range(0,enemyq):
#             enemies.append(renpy.random.choice([Keylogger,Ransomware,Rootkit,Worm1]))


#         $ Ily_m = "sad"
#         $ Ily_p = "2"
#         $ Ily_e = "2"
#         call screen battle_m
#         call Execute from _call_Execute
#         return
# label Execute:

#     return

# transform barwidth(value,maxvalue):
#     xzoom float(value)/float(maxvalue)
