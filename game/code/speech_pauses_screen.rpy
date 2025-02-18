###############################################################################################################
### AUTOMATIC SPEECH PAUSES - Preference sample code ##########################################################
###############################################################################################################
#
# Thanks to your kind donations, I whipped up this sample code for use in your [preferences] screen.
# Feel free to modify it however you like!
#
# How to use:
#   1. Uncomment the vbox code below and copy it wherever it would fit your preferences screen best!
#   2. It also comes with a simple "expander" transform that shows and hides the sliders whenever the main preference is toggled
#
# Thanks again for your support, and let me know if you'd like to see any other features: https://kigyo.itch.io/speech-pauses-for-renpy
# - KigyoDev
#
###############################################################################################################

# vbox:
#     style_prefix "radio"
#     textbutton _("Speech Pauses") action ToggleField(persistent,"speech_pauses")
#     
#     showif persistent.speech_pauses:
#         vbox at expander:
#             style_prefix "slider"
#             label _("Commas")
#             bar value FieldValue(persistent, "speech_pause_comma", step=.05, style=u'slider', min=0.05, max=1.0)
#             label _("Sentences")
#             bar value FieldValue(persistent, "speech_pause_period", step=.05, style=u'slider', min=0.1, max=2.0)

transform expander(y=90):
    on show:
        alpha 0 yoffset -y
        easein 0.3 alpha 1 yoffset 0
    on hide:
        alpha 1 yoffset 0
        easein 0.3 alpha 0 yoffset -y