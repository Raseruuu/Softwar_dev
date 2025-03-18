################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    # outlines [(2, "#000000aa", 1, 1)]
    line_overlap_split 1
    line_spacing 1
    properties gui.text_properties()
    language gui.language


style text_nooutline:
    outlines [(0, "#000", 0, 0)]

style input:
    properties gui.text_properties("input", accent=True)

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style gui_label_text:
   outlines [(0, "#000", 0, 0)]

style button:
    properties gui.button_properties("button") hover_sound "sound/hover.wav" activate_sound "sound/click.wav"

style button_text is gui_text:
    properties gui.text_properties("button") hover_sound "sound/hover.wav" activate_sound "sound/click.wav"
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)





################################################################################
## Custom Screens
################################################################################



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say
transform blinky:
    linear 0.1 alpha 0.0
    linear 0.1 alpha 1.0
    repeat
init python:
    def NullSideImage():

        global showsideimage
        showsideimage=False
        return Null()
screen say(who, what):
    style_prefix "say"
    if say_shop_mode:
        key "dismiss" action Return()
    window:
        if say_shop_mode:
            pos(541,525) anchor (0,0)
            xsize 526
        else:
            xsize gui.textbox_width
        id "window"

        if who is not None:
            window:


                style "namebox"
                text who id "who"

        text what id "what":
            if say_shop_mode:
                xmaximum 400
    # if say_shop_mode:
    #     timer 3.25 action Hide('say')
    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    # if not renpy.variant("small"):
    if renpy.get_say_image_tag() is not None :
        if showsideimage:
            frame:
                xalign 0.02 yalign 0.987

                style "sideimage_frame"
                add SideImage()
            # text ""+str(SideImage())

style sideimage_frame:
    background Frame("gui/frame.png", 72, 32)
image ctc:
    xalign 0.82
    yalign 0.98
    alpha 1.0
    subpixel True

    "gui/ctc.png"
    block:
        easeout 0.5 alpha 0.8 yoffset 0
        easein 0.5 alpha 0.6 yoffset -10
        repeat


style window is default:
    xalign 0.5

    yalign 0.98
    ysize gui.textbox_height
    xsize gui.textbox_width

    # background Image("gui/textbox.png", xalign=0.5, yalign=1.0)
    background Frame("gui/frame3.png", 72, 32)
    # xalign 0.0
    # # xfill True
    # yalign 1.0#gui.textbox_yalign
    # # ysize 1.0#gui.textbox_height

    # top_padding 70
    # left_padding 250
    # background "gui/textbox.png"
    # # background Frame("gui/textbox.png", 64, 64)

style namebox is default:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    padding gui.namebox_borders.padding

style namebox_label is say_label

style say_label is text_nooutline:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
    bold True

style say_dialogue is default:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

style say_thought is say_dialogue

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xpos gui.dialogue_xpos
            xanchor gui.dialogue_xalign
            ypos gui.dialogue_ypos
            xsize gui.dialogue_width

            text prompt style "input_prompt"
            input id "input"

style input_prompt is say_dialogue:
    properties gui.text_properties("input_prompt")
    xmaximum gui.dialogue_width

style input:
    xmaximum gui.dialogue_width

## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## http://www.renpy.org/doc/html/screen_special.html#choice
init -1 python:
    # we use display.get_info() because it persists between reloads so we don't end up with an endless loop
    if getattr(renpy.display.get_info(), 'oldmenu', None) is None:
        renpy.display.get_info().oldmenu = renpy.exports.menu

    # append " (disabled)" to any choices that fail their conditions
    # while also pretending that they've all succeeded and calling the built-in menu
    def menu_override(items, set_expr,*args,**kwargs):
        items = [ (renpy.exports.substitute(label) + (" (disabled)" if not renpy.python.py_eval(condition) else ""), "True", value)
                  for label, condition, value in items ]

        return renpy.display.get_info().oldmenu(items, set_expr)

    # intercept the built-in menu
    renpy.exports.menu = menu_override
    def RenpysetFocusChoice():
        
        return renpy.set_focus("choice", "button1")

screen choice(items):
    style_prefix "choice"
    # $ renpy.set_focus("choice", "button1")
    $ currentchoiceindex=0
    on "show":
    
        # action MouseMove(x=613, y=655, duration=.3)
        action Function(RenpysetFocusChoice)
    #TODO: MAKE IT LOOK LIKE A PROMPT WINDOW
    hbox:
        for menu_choice in items:
            # $ hiddenchoice = "hidden" in choice.kwargs.keys()
            # $ print(choice.kwargs.keys())
            # if hiddenchoice:
           
            #     pass
            # else:
            $ currentchoiceindex+=1
            if menu_choice.action:
                if "(disabled)" in menu_choice.caption:
                    
                    textbutton menu_choice.caption.replace("(disabled)","") :
                        xmaximum 400
                        id "button"+str(currentchoiceindex)
                else:
                    textbutton menu_choice.caption :
                        xmaximum 400
                        action menu_choice.action  
                        hover_sound "sound/hover.wav" 
                        activate_sound "sound/click.wav"
                        id "button"+str(currentchoiceindex)
                        
            else:
                textbutton menu_choice.caption :
                        xmaximum 400
                        action menu_choice.action  
                        hover_sound "sound/hover.wav" 
                        activate_sound "sound/click.wav"
                        id "button"+str(currentchoiceindex)
            

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True
style choice_frame is frame:
    
    yalign 0.5
    top_padding 100
    xsize 500
    background Frame("gui/frame3.png", 72, 32)
style choice_hbox is hbox:
    
    ypos 0.9
    xpos 0.5
    xanchor 0.5
    # spacing gui.choice_spacing

style choice_button is button:
    top_padding 20
    bottom_padding 20
    left_padding 20
    right_padding 20
    
    background Frame("gui/framebtn.png", 32, 32)
    hover_background Frame("gui/framebtn_hover.png", 32, 32)
    # properties gui.button_properties("button")

# style choice_button_text is text_nooutline:#button_text:
#     properties gui.button_text_properties("button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():
  # if okdesktop:
    ## Ensure this appears on top of other screens.
    zorder 200

    # # scroll up for history
    # key "mousedown_4" action ShowMenu("history")
    # key "K_PAGEUP" action ShowMenu("history")
    # key "repeat_K_PAGEUP" action ShowMenu("history")
    # key "K_AC_BACK" action ShowMenu("history")

    if quick_menu:
        if (map_active==False):
            if battle_active==False:

                image "images/computer/top_menu_ground.png" xalign 0.0 yalign 0.0
                hbox:
                    style_prefix "quick"

                    xalign 0.05
                    yalign 0.0
                    # hotspot (  0,  66,  69, 354) action Hide("Console") hovered Show("Console"), Play("sound", "SFX/consshow.wav")  unhovered Hide("Console")
                    textbutton _("{color=000}{b}SOFTWAR{/b}{/color}") keyboard_focus False
                    # textbutton _("Back") action Rollback() keyboard_focus False
                
                    # textbutton _("History") action ShowMenu('history')
                    textbutton _("Save") action ShowMenu('save') keyboard_focus False
                    textbutton _("Load") action ShowMenu('load') keyboard_focus False
                    textbutton _("Settings") action ShowMenu('preferences') keyboard_focus False
                    textbutton _("Skip") action Skip(fast=True) alternate Skip(fast=True, confirm=True) keyboard_focus False
                    textbutton _("Auto") action Preference("auto-forward", "toggle") keyboard_focus False
                    #textbutton _("Back") action Rollback()
                    # textbutton _("Help") action ShowMenu("help")


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")
default quick_menu = True

style quick_button is default:
    properties gui.button_properties("quick_button")

style quick_button_text is text_nooutline:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():
    # if map_active:
    #     use pausemenu
    # else:
        window:
            at slideindown3
            style_prefix "navigation"

            vbox:
                xpos gui.navigation_xpos
                xanchor 1.0
                yalign 0.5

                spacing gui.navigation_spacing

                if _in_replay:
                    textbutton _("End Replay") action EndReplay(confirm=True)

                if main_menu:
                    textbutton _("Start();") action Start()

                else:
                    textbutton _("MainMenu();") action MainMenu()
                    null height gui.button_text_size
                    textbutton _("History();") action ShowMenu("history")
                    textbutton _("Save();") action ShowMenu("save")

                textbutton _("Load();") action ShowMenu("load")

                null height gui.button_text_size

                textbutton _("Options();") action ShowMenu("preferences")
                textbutton _("About();") action ShowMenu("about")

                if renpy.variant("pc"):
                    ## Help isn't necessary or relevant to mobile devices.
                    # textbutton _("Help();") action ShowMenu("help")

                    ## The quit button is banned on iOS and unnecessary on Android.
                    textbutton _("Quit();") action Quit(confirm=not main_menu)

                null height gui.button_text_size*1.5

                textbutton _("Return();"):
                    action Return()


style navigation_button is gui_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")


style navigation_button_text is gui_button_text:
    properties gui.button_text_properties("navigation_button")

style navigation_window is window:

    xalign 0.985
    xsize 250

    yanchor 0.0
    ypos 112
    ysize None

    left_padding -8
    right_padding -8
    top_padding 60
    bottom_padding 20

    background Frame("gui/frame3.png", 72, 32)

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
transform envanim:
    yzoom 0.0 xoffset 0
    on show:
        linear 0.2 yzoom 1.0
    on hide:
        linear 0.2 xoffset 0.3 alpha 0.0


screen EnvRun:
    add "gui/main_menu/Envelope.png" xpos 0.75 ypos 0.65 xanchor 0.5 yanchor 0.5 at envanim
screen EnvLoad:
    add "gui/main_menu/Envelope.png" xpos 0.75 ypos 0.70 xanchor 0.5 yanchor 0.5 at envanim
screen EnvOpt:
    add "gui/main_menu/Envelope.png" xpos 0.75 ypos 0.75 xanchor 0.5 yanchor 0.5 at envanim
screen EnvQuit:
    add "gui/main_menu/Envelope.png" xpos 0.75 ypos 0.80 xanchor 0.5 yanchor 0.5 at envanim


transform gamesize:
    zoom 0.33
transform flashbang:
    alpha 0.0
    pause 1.5
    alpha 1.0
    linear 0.1 alpha 0.0
transform flashbang2:
    alpha 0.0
    pause 0.5
    alpha 1.0
    pause 0.2
    linear 0.1 yzoom 0.0 yalign 0.5
transform slideinright:
    alpha 0.0 xoffset 20
    pause 0.5
    ease 0.2 alpha 1.0 xoffset 0
transform slideinright2:
    alpha 0.0 xoffset 20
    pause 0.7
    ease 0.2 alpha 1.0 xoffset 0
transform navigationtransform:
    # alpha 0.0
    xoffset 20
    on show:

        # pause 1.5
        ease 0.1 xoffset 0
    # alpha 1.0
transform slideinleft:
    alpha 0.0 xoffset -50
    pause 1.5
    ease 0.2 alpha 1.0 xoffset 0
transform phantomtrans:
    alpha 0.0 xoffset -20
    pause 1.7
    ease 0.8 alpha 1.0 xoffset 0
    block:
        choice:
            alpha 0.5 xoffset -20 yoffset 10
            pause 0.1
        choice:
            alpha 0.6 xoffset 20 yoffset -10
            pause 0.1
        choice:
            alpha 1.0 xoffset 0 yoffset -0
            pause 1.0
        repeat
transform navigationtransformL:
    alpha 0.0 xoffset -20
    pause 1.5
    ease 0.1 alpha 1.0 xoffset 0
screen main_menu():

    tag menu
    timer 1.5:
        action Play("music","bgm/Credits_bgm_maoudamashii_8bit08.mp3")
    add "gui/main_menu/main menu bglayer1.png"
    if persistent.has_met_ILY:
        add "gui/main_menu/main menu ILYphantom.png" at phantomtrans
        add "gui/main_menu/main menu ILY text.png" at  phantomtrans
    add "gui/main_menu/main menu bglayer2.png" at slideinright
    add "gui/main_menu/main menu Softwar Logo.png" at slideinright2
    if persistent.has_met_ILY:
        add "gui/main_menu/main menu ILY.png" at slideinleft
    add "gui/main_menu/main menu TeamKizuna.png" xalign 0.0 yalign 0.0 at navigationtransformL

    # add "gui/logo.png" xalign 0.5 yalign 0.2
    add "white" at flashbang
    timer 1.5 action Show("mainmenu_buttons")
screen mainmenu_buttons:
    vbox:
        xalign 0.9 yalign 0.785
        at navigationtransform
        textbutton "{color=000}Start( );{/color}" action Start(), Hide("EnvRun"), Hide("mainmenu_buttons") hovered Show("EnvRun") unhovered Hide("EnvRun")
        textbutton "{color=000}Load( );{/color}" action ShowMenu("load"), Hide("EnvLoad"), Hide("mainmenu_buttons") hovered Show("EnvLoad") unhovered Hide("EnvLoad")
        textbutton "{color=000}Options( );{/color}"  action ShowMenu("preferences"), Hide("EnvOpt"), Hide("mainmenu_buttons") hovered Show("EnvOpt") unhovered Hide("EnvOpt")
        textbutton "{color=000}Quit( );{/color}" action Quit(confirm=not main_menu), Hide("EnvQuit"), Hide("mainmenu_buttons") hovered Show("EnvQuit") unhovered Hide("EnvQuit")





    # ## This ensures that any other menu screen is replaced.
    # tag menu

    # style_prefix "main_menu"

    # add gui.main_menu_background

    # ## This empty frame darkens the main menu.
    # frame:
    #     pass

    # ## The use statement includes another screen inside this one. The actual
    # ## contents of the main menu are in the navigation screen.
    # use navigation

    # if gui.show_name:

    #     vbox:
    #         text "[config.name!t]":
    #             style "main_menu_title"

    #         text "[config.version]":
    #             style "main_menu_version"


style main_menu_frame is empty:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox is vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text is gui_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title is main_menu_text:
    properties gui.text_properties("title")

style main_menu_version is main_menu_text:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.
transform slideindown:
    yoffset -20 alpha 0.0
    pause 0.1
    ease 0.15 yoffset 0 alpha 1.0
transform slideindown2:
    yoffset -20 alpha 0.0
    pause 0.26
    ease 0.15 yoffset 0 alpha 1.0
transform slideindown3:
    yoffset -20 alpha 0.0
    pause 0.18
    ease 0.15 yoffset 0 alpha 1.0

screen game_menu(title, scroll=None, scroll_y=None):
    on "show" action Stop("sound"),Stop("blipsound")
    style_prefix "game_menu"

    add gui.game_menu_background xalign 0.0 yalign 0.0
    add "gui/game_menu/options whiteframe.png" at slideindown xalign 0.0 ypos 0.0 yanchor 0.02
    add "gui/game_menu/[title].png" at gamesize, slideindown
    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.

            frame:
                style "game_menu_content_frame"
                at slideindown2
                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        if scroll_y != None:
                            yinitial scroll_y
                        else:
                            yinitial 1.0

                        side_yfill False
                        xfill False

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1

                        if scroll_y != None:
                            yinitial scroll_y
                        else:
                            yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude
            frame:
                style "game_menu_navigation_frame"



    #label title
    # label 'Menu'
    # label title:
    #     xpos 320
    use navigation
    if main_menu:
        key "game_menu" action ShowMenu("main_menu")






style game_menu_outer_frame is empty:
    bottom_padding 20
    top_padding 112

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame is empty:
    xsize 280
    yfill True


style game_menu_content_frame is empty:
    left_margin 20
    right_margin 280
    left_padding 28
    right_padding 28
    top_padding 42
    bottom_padding 16
    background Frame("gui/frame3.png",72, 32, tile=gui.frame_tile)

style game_menu_viewport is gui_viewport:
    xsize 900


style game_menu_scrollbar is gui_vscrollbar
style game_menu_vscrollbar:
    unscrollable gui.unscrollable


style game_menu_side is gui_side:
    spacing 10

style game_menu_label is gui_label:
    xpos 40
    yanchor 0.5
    ypos 130
    ysize 120

#style game_menu_label_text is gui_label_text:
#    size gui.title_text_size
#    color gui.accent_color
#    yalign 0.5

style game_menu_label_text is text_nooutline:
    #size gui.title_text_size
    color '#fff'
    xpos -5
    ypos 38

style return_button is navigation_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30

style return_button_text is navigation_button_text

## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label

style about_label_text is gui_label_text:
    size gui.label_text_size

style about_text is gui_text


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.4

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5
                        null height 3
                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("Empty Slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page) #ypos 

                textbutton _(">") action FilePageNext()


style page_label is gui_label:
    xpadding 50
    ypadding 3

style page_label_text is gui_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button is gui_button:
    properties gui.button_properties("page_button")

style page_button_text is gui_button_text:
    properties gui.button_text_properties("page_button")

style slot_button is gui_button:
    properties gui.button_properties("slot_button")

style slot_button_text is gui_button_text:
    properties gui.button_text_properties("slot_button")

style slot_time_text is slot_button_text

style slot_name_text is slot_button_text


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Settings"), scroll="viewport"):
        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text is gui_label_text:
    yalign 1.0

style pref_vbox is vbox:
    xsize 225

style pref_window is navigation_window





style radio_vbox  is pref_vbox:
    spacing gui.pref_button_spacing

style radio_button is gui_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text is gui_button_text:
    xoffset 8
    properties gui.button_text_properties("radio_button")

style radio_label is pref_label
style radio_label_text is pref_label_text




style check_vbox:
    spacing gui.pref_button_spacing

style check_label is pref_label
style check_label_text is pref_label_text

style check_button is gui_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text is gui_button_text:
    xoffset 8
    properties gui.button_text_properties("check_button")




style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_pref_vbox is pref_vbox

style slider_slider is gui_slider:
    xsize 350

style slider_button is gui_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text is gui_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450



style mute_all_button is check_button
style mute_all_button_text is check_button_text

## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html
init -5 python:
    class RollbackConfirm(Action, DictEquality):
        """
         :doc: menu_action
         Causes Ren'Py to return to the main menu.
         `confirm`
              If true, causes Ren'Py to ask the user if he wishes to
              return to the main menu, rather than returning
              directly.
         """

        def __init__(self, history_entry, confirm=True):
            self.history_entry = history_entry
            self.confirm = confirm

        def __call__(self):
            if self.confirm:
                layout.yesno_screen("Do you want to rewind to this point?", RollbackConfirm(self.history_entry, confirm=False))

            else:
                checkpoints = renpy.get_identifier_checkpoints(self.history_entry.rollback_identifier)
                renpy.rollback(force=True, checkpoints=checkpoints)
                renpy.restart_interaction()
                ui.close()



screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    ## @TODO: Problem with crolling if you use the arrow keys

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), scroll_y=1.0):
        style_prefix "history"

        for h in _history_list:
            button:
                ysize None
                action RollbackConfirm(h)
                hover_background Frame("gui/framew_hover.png", 10, 10)
                background Frame("gui/framew.png", 10, 10)


                window:
                    ## This lays things out properly if history_height is None.
                    has fixed:
                        yfit True


                    if h.who:

                        label h.who:
                            style "history_name"

                            ## Take the color of the who text from the Character, if
                            ## set.
                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                    text h.what
            

        if not _history_list:
            label _("The dialogue history is empty.")


style history_window is empty:
    xfill True
    ysize gui.history_height
    top_margin gui.history_entry_top_margin

style history_name is gui_label:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text is gui_label_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text is gui_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label is gui_label:
    xfill True

style history_label_text is gui_label_text:
    xalign 0.5

## Disable the hover and click sounds
style history_button is empty
style history_button_text is empty

## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text is gui_button_text:
    properties gui.button_text_properties("help_button")

style help_label is gui_label:
    xsize 250
    right_padding 20

style help_label_text is gui_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0

style help_text is gui_text

################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100
                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action


    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame:
    background Frame("gui/frameopaque.png", 72, 32, tile=gui.frame_tile)
    #padding gui.confirm_frame_borders.padding
    top_padding 52
    bottom_padding 20
    right_padding 16
    left_padding 16

    xalign .5
    yalign .5

style confirm_prompt is gui_prompt

style confirm_prompt_text is gui_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button is gui_medium_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text is gui_medium_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text is gui_text:
    size gui.notify_text_size

style skip_triangle is skip_text:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "font/DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style notify_frame is empty:
    ypos gui.notify_ypos

    # background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    background Solid("000")
    padding gui.notify_frame_borders.padding

style notify_text is gui_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing 0

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

style nvl_window is default:
    xfill True
    yfill True
    background Frame("gui/frame3.png",72, 32, tile=gui.frame_tile)
    # padding gui.nvl_borders.padding
    xpadding 20
    ypadding 20
    top_padding 0
    left_margin 540
    right_margin 16
    top_margin 112
    bottom_margin 202

style nvl_entry is default:
    xfill True
    ysize gui.nvl_height

style nvl_label is say_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue is say_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button is button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text is button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"
    zorder 200

    # hbox:
    #     style_prefix "quick"

        # xalign 0.5
        # yalign 1.0
        #
        # textbutton _("Back") action Rollback()
        # textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        # textbutton _("Auto") action Preference("auto-forward", "toggle")
        # textbutton _("Menu") action ShowMenu()
    image "images/computer/top_menu_ground.png" xalign 0.0 yalign 0.0
    hbox:
        # style_prefix "quick"

        xalign 0.05
        yalign 0.0
        # hotspot (  0,  66,  69, 354) action Hide("Console") hovered Show("Console"), Play("sound", "SFX/consshow.wav")  unhovered Hide("Console")
        textbutton _("{b}SOFTWAR{/b}")
        textbutton _("History") action ShowMenu('history')
        textbutton _("Back") action Rollback()

        textbutton _("Save") action ShowMenu('save')
        textbutton _("Load") action ShowMenu('load')
        textbutton _("Settings") action ShowMenu('preferences')
        textbutton _("Skip") action Skip(fast=True) alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")

style window:
    variant "small"
    background Frame("gui/frame3.png", 72, 32)

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600
