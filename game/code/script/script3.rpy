# """    Outline (SCRAPPED)
#      Feb 18th (Tuesday)
# School Section.
# Insert John’s thoughts on Hacker X incident.
# Submit their internship 
# After Code Red incident John alone decides to take on the initiative, trying to get info about their mystery attacker.
# Free Roam to investigate about Code Red.
# reveal that ILY was able to take location data from her fight with Code Red.
# Location data only supplies limited information of Red’s steps in the GRID.
# Break Time
# John calls Alicia 
# Feb 19th
# The team chills at school and thinks about what to do next.
# Funny slice of life moments with Hilbert, John and Lisa.
# John is continuously curious about Hacker X
# Free Roam:
# Possibly using Vira’s help, ILY discovers and approaches Hacker X’s network
# Ave is intercepting ILY’s attack with Sniping
# ILY looks to the direction where bullets come from and pushes through
# John’s party is dumbfounded at meeting Ave. This was supposed to be Hacker X’s and Code Red’s territory, but an Antivirus is here.
# John pieces together that the owner of Ave, and the owner of Code Red are the same person.
# Battle Ave
# ILY draws her blade. This makes Ave extremely angry.
# Emotional battle with an evident grudge from Ave. 
# ILY is able to escape deletion
# """    
# ###

#  Alicia debut part
# 1. Establish her relationship with John
# 2. Adoptive Mother
# 3. Teacher of John since childhood
# 4. Alicia checks the status of John's internship. In a little while they are gonna finish the paperwork and submit it completely.
# 5. Alicia finds out about ILY's inhabitance of John's PC. As a response she aids him to make ILY portable using a special device she volunteers to create.
# 6. Hilbert and Lisa feel easy about miss Alicia. John feels a little awkward when she tells him to call her "Mom".
# 7. It's a little late into their college social life, but Alicia thinks to introduce Claire, Kazuki, and Jugo to John and the others. (Engineers for Robot Cup Arc) - they had an encounter with FAI viruses already
# Past:
# 1. Alicia did regular visits to the orphanage as part of her school program she is a part of. Raising children for various industries. Alicia and others taught them computer studies. A chain of interests followed where John and Nick continued to study computer science.
# 2. Alicia adopted John only. But Nick was supposed to be adopted too. Nevertheless, John treats Nick as his brother. Nick was old enough to decide to leave the orphanage probably at 13(?) after leaving, he became distant, but he continued to train, even coinciding in SDS. 
# 3. Alicia has a connection with Professor Mirai, who started the FAI project
    
label script3:
    call hideMapview
    
    call showphasemsg("Chapter 3") #(Can change chapter name anytime)
    call showphasemsg("Hurry Up",2.0)
    
    play music "bgm/ost/ChinWilla/Assembly by ChinWilla.mp3"
    scene classroom with pixellate
    "Back at Uni."
    "Class hasn't started yet. I spot Hilbert in the room, suddenly, he leaps out of his seat. He's approaching me, who just got past the door."
    show Hilbert
    $ Hilbert_w = False
    $ Lisa_w = False
    $ Lisa_eyes="open"
    h "John!!! This is it, we gotta tell Miss Alicia about what happened at SDS! Since it's our internship!"
    $ Hilbert_m = "frown" 
    $ John_m = "frown"
    j "Okay, but not now, we still have a regular class to finish."
    $ Hilbert_eyes = "lookaway" 
    h "I'm half-excited and half-anxious about it. What if she scolds us?"
    
    j "Right..."
    h "We botched the security of the company by clumsily opening emails... and.. ahhh!!!"
    j "Do you think she'll understand since it was Valentines and such?"
    $ Hilbert_eyes = "open" 
    $ Hilbert_e = "up" 
    h "Valentines? The situation just makes us look like lovesick idiots."
    "Lisa... is a lovesick idiot?"
    j "I'm about to explain the ILY situation on my PC to one more person... I'm going to lose it.."
    $ Hilbert_eyes = "open"
    $ Hilbert_e = "down"
    $ Hilbert_m = "smile"   
    h "Since ILY isn't much danger at all, Miss Alicia might be more open about her. Whatchu think?"
    h"Do we have to tell her what happened with Code Red? Seems like that's where the more vital part comes along!"
    j "I guess we shoo'd that Virus away successfully. But.. Ave.. She said she was targeting ILY."

    h "The Hacker X threat is still looming.. Maybe she can advise something for us."
    j "I'm a little curious what kind of... advice."
    h "Hey! Lisa is here!"
    show Lisa with dissolve:
        ease 0.5 xalign 0.20
    show Hilbert:
        ease 0.5 xalign 0.80
    h "Lisa! We're going to... make our report! To Miss Alicia! After class!"
    l "Oh! Is that so? Hmmmm. I was... going to tell her in person too!"
    h "So you can join us?"
    l "Well, I e-mailed her my report already. I wrote it last night."
    $ Hilbert_e = "up" 
    $ Hilbert_m = "frown" 
    h "Whaa?"
    j "How much of the internship trouble was in there?"
    l "She knows most of what happened already. I think."
    j "I see..."
    j "She's here!"
    hide Hilbert
    hide Lisa 
    with dissolve
    "Miss Alicia arrived. Just like usual, she began the lecture.. It was an ordinary session."
    $ Alicia_w = False
    show Alicia with dissolve    
    #"Insert Technobabble here"
    "Miss Alicia manages to catch everyone's attention in class even in our final semester... She's always been my mentor ever since. And it's no mistake. I do like being in her class."
    scene black with dissolve
    scene classroom
    show Alicia with dissolve    
    "Soon after, the lecture was over."
    al"Hope y'all got that. This lesson will be included in your final exam! It's very soon. I'm going to see y'all in graduation, Okay? You can do it!"
    al "Any questions?"
    # "Somebody" "Miss Alicia, what about the upcoming festival?"

    al "Okay, if there aren't any more questions, class is dismissed!!"
    scene black with dissolve
    scene classroom with dissolve
    show Alicia with dissolve    
    $ Hilbert_w = True
    $ Lisa_w = True
    play music "bgm/ost/Serious_Noyemi_K.ogg"
    l "Hello Miss Alicia!"
    al "Hey! You three! So, how was SDS?"
    j "... It's fine now, I guess. Wait, Lisa sent you a report all about it!"
    al "Well, it'd be nice to hear from y'all in person."
    j "Where do we even start..."
    al "Hmmm... I think I got a good idea of what went on!"
    al "You got your PCs hacked... "
    al "By a love letter trap..."
    j "... Yeah."
    $ Hilbert_eyes = "midclose"
    $ Hilbert_e = "up2"
    $ Hilbert_m = "frown"   
    h "How embarassing..."
    al "Lisa filled me in on the events. No need to get embarassed. I'm also not in any position to scold you."
    j "..."

    al "Hey! It's fine, it's Valentines season so that kind of thing could work on me too!"
    $ Hilbert_e = "up"
    
    $ Hilbert_eyes = "open" 
    $ Hilbert_m = "frown_open" 
    h "Huh?"

    $ Hilbert_m = "frown" 
    h "Wait, Miss Alicia is still single?"
    al "Y-yes.."
    al "Now you're embarrassing me.."
    al "I'm only John's adoptive mother. I'm still young, I can still..."
    j "Y-yeah.."
    h "John's adoptive mother..? After all these years I only just found out about this?"
    $ Hilbert_e = "down"
    h "Wait, John! I'm letting it sink in just now. You're a top student, of course! You kept it a secret?"
    j "Well, not like there's any reason to bring it up."
    al "John would never address me as his mom though.. I'm a little hurt."
    j "Gah! Wh-what.."
    al "My son!!"
    #John : (-_-)
    l "..."
    al "Getting back on track.. You're with the ILOVEYOU Virus now, huh?"
    j "She calls herself ILY, and she decided to be my... assistant."
    j "She is also called an F.A.I.. If you know what this means."
    al "ILY... I see how it is. Believe it or not, I am knowledgeable with this stuff! I'm familiar about ILY, too."

    "She knows!"
    h "How much does Miss Alicia know?!"
    al "I'm sure you guys are curious.. Let's just say I dabble with FAI too, and I have used my own FAI Antivirus as well!"
    "!!!"
    # Alicia Serious
    al "ILY isn't that kind of virus. On top of being able to trick users with her Virus Algorithm, she is virtually unbeatable in Softwars. She doesn't stroll around looking for a master to serve."
    "Amazing.. She really is an expert. As expected of Miss Alicia..."
    al "That ILY you have is an anomaly."
    al "You're lucky that this is a special case. I would normally advise for y'all to re-format your PCs and change all of your passwords."
    # Alicia Eyes closed
    al "What's done is done..."
    # Alicia panicked
    al "Honestly, I'd check up on my son at his place ASAP because of this, to see his PC... But, I'm absolutely occupied for the rest of this week! Even now is borrowed time from my Professor duties!!!"
    j "Ah. Is that so..."
    al "But there's something I wanted to try! You see I've been working with the engineers on a little project for FAIs."
    j "!! For FAIs?"
    al "I'll be doing finishing touches on it still, so come back to me tomorrow!"
    h "Woah! What is it exactly?"
    "There are plenty of questions dancing in my head right now."
    "I better ask before she leaves!"
    j "Wait, "
    al "Well, I'll be seeing y'all next time!"

    scene black

## VIRA CHECK UP


## VIRA gets leads on Hacker X from the remains of the Spyware bug
# LEADS TO investigation toward Connecht Square.




    "NEXT PART : ELLIE MINI ARC"
##############
#####Goals of this arc:
#######
    # 1. Make a conflict with Ellie for John to overcome with his good character and intentions 
    # 2. Ellie realizes John isn't a bad person to get with Lisa
    # 3. Establish who likes who: John likes Lisa, and Ellie likes Hilbert

    # OUTLINE: 
    # 1. Because another Antivirus has dropped in SDS, Hilbert is looking into who could have ordered to install it. (They don't think Ave was from Hacker X) Vira remains on SDS at standby to guard for activity. 
    # 2. Ellie finds out about the Lisa, John and Hilbert team Photo and confronts John. After a semi-long chat, Ellie turns out to be chill and wants to join that team. 
    #     **<CG MOMENT: Ellie looking at John with suspicion at Cafella>**
    # 1. Ellie suggests that Lisa could be more suspicious than she looks. She could be the one behind ILY
    # 2. 



    play music "bgm/Cafella_bgm_maoudamashii_acoustic51.mp3"
    scene cafeoutside
    "Nice, I'm much earlier than I was before."
    "Last night, Lisa e-mailed Miss Alicia..."
    "Of course, there's one more person she e-mailed! It was me. She's so thoughtful."
    "What will it be this time?"
    "She told me to meet here. But..."
    "She's not here yet."
    scene cafeinside with dissolve
    "I might be able to repay her now for that last time I was late."
    "But... will it be okay if I ordered a drink before she came? Like she did for me?"
    "That time, she guessed correctly what flavor I like to buy from this place." 
    "I don't know if she would appreciate me doing that for her. I know the drink she got was... this one! Red Velvet?"

    "What would she think? Is that weird? Like I'm stalking her?"
    "When she did it for me, I just accepted it, because it was convenient and... huh? How did she know?"
    "That brain of hers might just be too smart for me. Yeah. She's the best after all."
    "And she wouldn't... stalk me."
    "Red Velvet.. I suppose I'll try that one out too."
    "I wonder if she would appreciate this.. Croissant. Yeah! A bit random, but who doesn't like croissants?"
    scene cafeinside2 with dissolve
    "..."
    "So I ended up getting 2 red velvet frappes and 2 croissants!"
    scene black with dissolve
    scene cafetable with dissolve
    "Yep... it's served already, but she's not here yet."
    "I got to try my red velvet frappe. It's really good. I hadn't tried this flavor before."
    "Aaand just like that, I drank all of it."
    "I took some time to myself.. Until..."
    "Someone entered the cafe! Is it her?"
    "It's not Lisa. She's... approaching here?"
    "It's Ellie. Lisa's roommate."
    "Hmmm... They're usually together, so where's Lisa?"
    show Ellie with dissolve
    $ Ellie_w=False
    e "So you're really here."
    j "..."
    e"You waiting for someone? I will sit here now."
    j "Ah! G-go ahead!"
    "She lands her elbows on the table, locks her fingers together, then rests her chin on them. Then she gives me a gaze like that of a detective skimming for any signs of criminal activity. At least that is what it feels like."
    "My upper body retreats back insinctively, in response to her leering eyes."
    "I can't help but notice her nice, partially exposed breasts. In front of me. I hope she doesn't notice me glancing at them."
    e "John."
    j "Uhh what can I do for you?"
    stop music
    e "Lisa isn't coming today."
    $ Ellie_e = "down"
    e "You can forget about your little date here."
    j "Wha- did something happen? Is she okay?"
    $ Ellie_eyes="midclose"
    $ Ellie_m="O3"
    e "You stay away from her that's what!"
    j "B-but the pastry! A-and this drink!"
    $ Ellie_m="midopen"
    $ Ellie_eyes="open"
    e "Guh!"
    j  "Where is she?"
    $ Ellie_m="O3"
    e "Why do you care!"
    $ Ellie_m="frown"
    e "I-I forbid you!"
    j "Forbid? But we were-"
    e "Why were you together? And that was... your house?!"
    
    j "Huh?! She's just! It's work! The internship!"
    
    j "Hilbert was with us! There was some trou-"
    $ Ellie_e="down"
    $ Ellie_m="midopen"
    e "You were....!!"
    $ Ellie_m="frown"
    j "I can explain!!"
    play music "bgm/Enemy_bgm_maoudamashii_cyber19.ogg"
    $ Ellie_eyes="midclose"
    "Her leering straight to my soul intensifies, Like she is judging me.. I think that's what her squinting eyes and lowering brows mean, at least."
    e "I don't trust men like you."
    e "I bet you're thinking something nasty right now!"
    j "What!!"
    "She got worked up.. Just what is her problem with me?"
    j "uhhh... will you calm down? "
    extend "Please?"
    "I push the plate closer to her."
    j "You can... take this. Though this was supposed to be for Lis-"
    $ Ellie_eyes="midclose"
    $ Ellie_e="1up"
    $ Ellie_m="O3"
    e "Huh?! You idiot, you bought this for her, don't just give it to-..."
    $ Ellie_m="frown"
    j "But you said she isn't coming here anymore."
    # e "She's busy with her swimming sessions now. The swim club needs her for the upcoming festival!"
    $ Ellie_e="normal"
    $ Ellie_eyes="open"

    e "She's busy with Miss Alicia. I dunno what it is, I suppose she's needed for the upcoming festival!"
    j "Ah. Of course... The festival... "
    j "So yeah I guess you can have the crois-"
    e "What's your deal? Don't think you can sway me with.."
    j "You can have the drink too.."
    $ Ellie_eyes="open"
    $ Ellie_e="normal"
    "She takes a bite."
    "I can sense she is enjoying the croissant."

    "After a while of munching she resumes her little speech."
    play music "bgm/Cafella_bgm_maoudamashii_acoustic51.mp3"
    $ Ellie_eyes="closed"
    
    $ Ellie_e="down"
    e "Tch. Listen!"
    $ Ellie_eyes="open"

    e "You didn't do anything with Lisa that's.. that's..."
    j "Like I said, it's work! The internship!"
    e "I saw your photo together! What the heck was that?"
    j "Hilbert posted it??"
    "That idiot.. Now I'm in trouble."
    $ Ellie_e="1up"

    e "In your house!!.... With... Hilbert??"
    $ Ellie_e="down"

    j "What are you implying?!"
    j "... Are you even listening to me?"
    j "We solved some problems together.. does that suffice? It was.. complicated!"
    j "And it was her that said we should work on the thing at my place."

    $ Ellie_eyes="midclose"

    "She gives me a glare. Again."
    j "I refused, of course! But she... insisted!"
    e"Wha?" 
    e "You refused? You don't have the hots for Lisa?"
    j "I do!"
    $ Ellie_eyes="midclose"
    $ Ellie_e="1up"
    $ Ellie_m="O3"
    with Shake((0, 0, 0, 0), 0.5, dist=20)
    play sound "sfx/Damage2.wav"

    e "HUUUUH?!"
    "Yikes. Did I say that out loud?"
    $ Ellie_eyes="closed"
    $ Ellie_e="down"
    $ Ellie_m="frown"

    pause
    e "As.. expected, I suppose."
    $ Ellie_eyes="open"

    e"Look me in the eyes!"
    j "Ah!"
    e "Okay... what do you like about her?"
    j "Ah!"
    "Ellie fixed her posture."
    e "Go on. Tell me."
    "She's..."
    j "She's an amazing person.. Lisa is.."
    e "Hold it. Nevermind. I don't want to hear you admit that you like her body, or her beauty. Or that she's smart."
    j "I haven't even-"
    "She's right though. To me, Lisa is perfect."
    "..."
    e "After thinking about it... Aren't you a topnotcher yourself?"
    j "Topnotcher?"
    e "You and Lisa. Topnotchers! Always Top-notch."
    e "You guys have had the highest grades in class ever since. I'm very carefree about my grades, so I respect you two."
    e "So... I don't think you're lying about Lisa wanting to go to your place for that internship thing."
    e "She probably doesn't realize she should be more reserved when it comes to boys."
    e "But...  I think she likes you too. That's why she is acting so boldly."
    "Lisa... likes me?"
    j "But..! That was just work!"
    e "I don't know, OK? You're not half bad when it comes to looks and you score high consistently in your class."
    e "Someone like you wouldn't have time to stalk her or anything.."
    j "..."
    "Safe!!"
    e "Lisa has been my roomie, and her bestie... But I don't know much about her as deeply as I'd wish. It really surprised me. Seeing her with you guys."
    j "You're a kind friend."
    e "Huh?"
    j "You seem to really care about Lisa."
    e"Don't flatter me."
    $ Ellie_m="smile"
    $ Ellie_e="normal"

    e "You did get this treat for her didn't you? That's quite something. I can chill with that."
    e "Red Velvet... Is her favorite, too. So that's good on you."
    "She can chill with it? So is she fine with me trying to date Lisa?"
    e "I'm also impressed that you're not scared to admit that you like her."
    scene cafeoutside2 with dissolve
    "I'm impressed at myself holding this conversation long enough, too. I thought I was gonna die."
    "She paused and looked away for a bit. She's thinking really deeply about this..."

    "Her words are also getting more clear to me. She's showing a side of her that's a lot different from what she lets on in her outside appearance."
    scene cafetable with dissolve
    show Ellie with dissolve
    e "We're old enough. We're adults now, right? We can talk about this kind of stuff? About where we go after studying?"
    e "About... Love and life-long partners?"
    "Wha..."
    e "I take back what I said."
    j "!!! ... Which one?"
    e "That you're forbidden from meeting her."
    j "Oh."
    e "Just... Let me join if you do meet."
    j "Huh? Of course! You can join and keep watch of Lisa! I won't do anything strange!"
    e "Idiot.. Go do whatever with Lisa."
    e "But, this isn't about Lisa anymore..."
    j "Wha?"

    e "I... I... piece it together yourself, genius."
    "What does she mean? \"Life-long partner\"... Not me.."
    "Him? She's interested in Hilbert?"
    j "Hi-Hilbert?"
    e "Yeah.."
    j "I don't think I should ask why?"
    # Ellie blushes
    e "Hilbert was... kind to me. He left a good impression, OK?"
    e "He's just... nice. I'd say he's not like other dudes."
    j "Hilbert... Yeah. He is kind. I owe him this internship."

    j "Why now? We're about to graduate..."
    e "I could say the same about you!! You're awfully late in making a move at Lisa. If you really like her."
    j "Ouch?"
    "She continues munching the croissant, almost finishing it."
    e "Time is limited, I know. So I think we have to... Hurry up."
    e "After our graduation... I don't want to... be alone, or just go separate ways. That's something my sister told me was inevitable. Maybe with the wrong attitude, it is."
    e "So.. Let's both make our moves already."
    "She's right... Lisa wasn't here in Connecht from Christmas break til New Year's... after getting her degree, she might just fly back to Germany...!"
    j "Th-thank you, Ellie.. for telling me all this."
    e "Wha? Why are you bowing your head?! You're the one with the treats!"
    e "Hmmm... Let me order some food here. I'm not quite done with you yet."
    e "We got a deal now! Tell me all about the  activities you were doing yesterday. What happened at your internship! And... what was Hilbert like..?"
    j "There's quite a bit!! Do I have to narrate all the details?"
    e "Yes."
    hide Ellie with dissolve 
    "I'm beginning to understand Ellie more..."
    "I thought she just hated my guts... I was just overthinking things, huh? Apparently she was just  interested in Hilbert."
    scene black with dissolve
    
    scene cafeoutside2 with dissolve
    $ Ellie_w=True
    "So... since she asked for it, I narrated to her what happened at SDS. And about ILY. I decided it's okay to tell her about FAI viruses being the cause of the internship project halting."
    e "A what?! An AI Virus?"

    "Here we go again..."
    "I continued to elaborate about the situation with Lisa and Hilbert who were infected by ILY.  About ILY and her odd directive to be my assistant..."

    e "I love you... Virus? Ahh! I remember! Hmmmm..."
    j "Sorry to ramble so much..."
    "Ellie is in deep thought."
    e "You received it from Lisa, so doesn't that make her your prime suspect? For the ILOVEYOU Virus thing?"
    j "Wh-what? But she was also infected! I don't think Lisa would..!"
    e "Well that's easy to say without evidence, it's not like you saw her PC. Isn't her dad a big-shot in some antivirus company? She might just know about all this from the start, you know..."
    j "I never thought of it that way...!"
    j "But..!"
    e "Don't really have solid proof. Lisa is kind of a strange one, I admit. She's unpredictable even speaking as her bestie."
    e "Don't confront her about that. Since we're not certain."
    j  "I'll think about it.."
    "Now I'm the one who is in deep thought!"
    "That's not some light conclusion to make. Why would Lisa intentionally try to hack me using ILY, makes no sense."
    "Lisa..."
    e "You still there?"
    j "Oh! Right! The internship."
    "What Ellie really wants to hear in all this is all about Hilbert's involvement."
    j "We couldn't have saved the internship without Hilbert."
    e "Save? What happened?"
    j "We encountered a virus. It messed up the web server for this Cafe's online market!"
    j "It was tough, but we managed to fight the virus off and restore the web server!"
    show CG1Pizza with dissolve:
        zoom 0.5
        xalign 0.5 yalign 0.5
    j "We worked together nicely there, so Hilbert took that picture after we solved the case! Now he thinks we're some kind of \"Heroic Hacker Party\"."
    
    e "... He's so corny."
    j "You think so too, huh!?"
    hide CG1Pizza with dissolve
    "So... that conversation was pretty long, and took us the whole afternoon.  It turns out Ellie is easy to talk to, and she opened my eyes too."
    "What could Lisa be thinking?"
    "If she turns out to be the one behind ILY, it's a really strange way to..."
    "It can't be, right?"

    return
