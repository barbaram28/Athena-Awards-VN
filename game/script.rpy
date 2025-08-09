# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define V = Character("VILLAIN", color="#ff0080")
define H = Character("HERO", color="#ffee00")

# Determines whether the pauses are active at all
# default value: True
default persistent.speech_pauses = True

# Determines the pause length of commas and ellipses
# default value: 0.15
default persistent.speech_pause_comma = 0.15

# Determines the pause length of periods, questions, em dashes, and so on
# default value: 0.3
default persistent.speech_pause_period = 0.3

# Determines which version of pause to use
# Version A: Generally better and suitable for the vast majority of projects, since its pause lengths are 
#            relative to the text speed, it doesn't interfere with text shaders, and it allows lines with 
#            lots of pauses to still be displayed with one click.
# Version B: Doesn't have any of the above benefits, but it adds an audible pause in case you are using 
#            text bleeps. With version 1, text bleeps keep going at a constant pace despite the visual pause, 
#            so version 2 might be more natural in that case.
# default value: "A"
define speech_pause_version = "A"

## Definitions ################################################################################################

# Define what counts as a "comma" (shorter pause)
# default value: [",", "..."]
define speech_comma = [",", "..."]

# Define what counts as a "period" (longer pause)
# default value: [".", "?", "!", ":", ";", "—", "~"]
define speech_period = [".", "?", "!", ":", ";", "—", "~"]

# Define exceptions where any of the above symbols should not lead to a pause
# default value: ["Mr.", "Mrs.", "Dr."]
define speech_exceptions = ["Mr.", "Mrs.", "Dr."]

# Define additional text tags that should not interfere with pauses. The default ones are already included
#   For example, this will make sure that a line like "{b}What?!{/b} Are you serious?" still correctly registers
#   a pause, even though "?!" is followed up by "{/b}" instead of a blank space.
# example values: ["b", "a", "i"]
# default value: []
define speech_tags = []

## Spaceless definitions ######################################################################################

# Some punctuation marks do not require a space afterwards (which is how the need for a pause is usually detected).
# I tried a hacky solution that will add a pause whenever any of the below punctuation marks appear, 
#   UNLESS they are the last character in a line.

# Feel free to disable them if this leads to unexpected behavior.
# default value: True
define speech_pauses_nospace = True

# Comma-equivalents that require no space after
# default value: ["，","、", "…", "——"]
define speech_comma_nospace = ["，","、", "…", "——"]

# Period-equivalents that require no space after
# Note: If you use em-dashes [like—this] instead of [like — this], delete them from [speech_period] and add them down here!
# default value: ["。", "？", "！", "；", "：", "……"]
define speech_period_nospace = ["。", "？", "！", "；", "：", "……"]

## The Function ###############################################################################################

init python:
    def speech_pause_adder(text_input):

        tags = speech_tags + ["i", "b", "a", "color", "s", "size", "u", "alpha", "alt", "cps", "art", "font", "image", "k", "noalt", "outlinecolor", "plain", "rb", "rt", "shader"]
        open_tags = ["space", "vspace", "w", "p", "nw", "fast", "done", "clear"]

        pauses_add = {}

        if "b" in speech_pause_version or "B" in speech_pause_version:
            for i in speech_comma:
                pauses_add[i + " "] = i + "{w=" + str(persistent.speech_pause_comma) + "} "
                for j in tags:
                    pauses_add[i + "{/" + j + "} "] = i + "{/" + j + "}{w=" + str(persistent.speech_pause_comma) + "} "
                for j in open_tags:
                    pauses_add[i + "{" + j + "} "] = i + "{" + j + "}{w=" + str(persistent.speech_pause_comma) + "} "
            for i in speech_period:
                pauses_add[i + " "] = i + "{w=" + str(persistent.speech_pause_period) + "} "
                for j in tags:
                    pauses_add[i + "{/" + j + "} "] = i + "{/" + j + "}{w=" + str(persistent.speech_pause_period) + "} "
                for j in open_tags:
                    pauses_add[i + "{" + j + "} "] = i + "{" + j + "}{w=" + str(persistent.speech_pause_period) + "} "
            
            pauses_exceptions = {}
            for i in speech_exceptions:
                pauses_exceptions[i + "{w=" + str(persistent.speech_pause_comma) + "} "] = i + " "
                pauses_exceptions[i + "{w=" + str(persistent.speech_pause_period) + "} "] = i + " "
                
            for i in pauses_add:
                text_input = text_input.replace(i, pauses_add[i])

            for i in pauses_exceptions:
                text_input = text_input.replace(i, pauses_exceptions[i])

            if speech_pauses_nospace:
                text_copy = ""
                for i in range(len(text_input)):
                    text_copy += text_input[i]
                    if i < len(text_input)-1 and text_input[i:i+2] in speech_comma_nospace or text_input[i:i+2] in speech_period_nospace:
                        continue
                    elif i > 0 and text_input[i-1:i+1] in speech_comma_nospace:
                        text_copy += "{w=" + str(persistent.speech_pause_comma) + "}"
                    elif i > 0 and text_input[i-1:i+1] in speech_period_nospace:
                        text_copy += "{w=" + str(persistent.speech_pause_period) + "}"
                    elif text_input[i] in speech_comma_nospace and i < len(text_input)-1:
                        text_copy += "{w=" + str(persistent.speech_pause_comma) + "}"
                    elif text_input[i] in speech_period_nospace and i < len(text_input)-1:
                        text_copy += "{w=" + str(persistent.speech_pause_period) + "}"
                
                text_input = text_copy

        else:
            comma_slow = (1/persistent.speech_pause_comma)/100
            period_slow = (1/persistent.speech_pause_period)/100

            for i in speech_comma:
                pauses_add[i + " "] = i + "{cps=*" + str(comma_slow) + "} {/cps}"
                for j in tags:
                    pauses_add[i + "{/" + j + "} "] = i + "{/" + j + "}{cps=*" + str(comma_slow) + "} {/cps}"
                for j in open_tags:
                    pauses_add[i + "{" + j + "} "] = i + "{" + j + "}{cps=*" + str(comma_slow) + "} {/cps}"
            for i in speech_period:
                pauses_add[i + " "] = i + "{cps=*" + str(period_slow) + "} {/cps}"
                for j in tags:
                    pauses_add[i + "{/" + j + "} "] = i + "{/" + j + "}{cps=*" + str(period_slow) + "} {/cps}"
                for j in open_tags:
                    pauses_add[i + "{" + j + "} "] = i + "{" + j + "}{cps=*" + str(period_slow) + "} {/cps}"
            
            pauses_exceptions = {}
            for i in speech_exceptions:
                pauses_exceptions[i + "{cps=*" + str(comma_slow) + "} {/cps}"] = i + " "
                pauses_exceptions[i + "{cps=*" + str(period_slow) + "} {/cps}"] = i + " "
                
            for i in pauses_add:
                text_input = text_input.replace(i, pauses_add[i])

            for i in pauses_exceptions:
                text_input = text_input.replace(i, pauses_exceptions[i])

            if speech_pauses_nospace:
                text_copy = ""
                for i in range(len(text_input)):
                    text_copy += text_input[i]
                    if i < len(text_input)-1 and text_input[i:i+2] in speech_comma_nospace or text_input[i:i+2] in speech_period_nospace:
                        continue
                    elif i > 0 and text_input[i-1:i+1] in speech_comma_nospace:
                        text_copy += "{cps=*" + str(comma_slow) + "}"
                    elif i > 0 and text_input[i-1:i+1] in speech_period_nospace:
                        text_copy += "{cps=*" + str(period_slow) + "}"
                    elif text_input[i] in speech_comma_nospace and i < len(text_input)-1:
                        text_copy += "{cps=*" + str(comma_slow) + "}"
                    elif text_input[i] in speech_period_nospace and i < len(text_input)-1:
                        text_copy += "{cps=*" + str(period_slow) + "}"
                    if (text_input[i] in speech_comma_nospace or text_input[i] in speech_period_nospace) and i < len(text_input)-1 or i > 0 and text_input[i-1:i+1] in speech_comma_nospace or i > 0 and text_input[i-1:i+1] in speech_period_nospace:
                        text_copy += "\u200B{/cps}"
            
                text_input = text_copy

        return text_input
    

    def add_speech_pauses(text_input):
        if prev_filter:
            text_input = prev_filter(text_input)

        if persistent.speech_pauses is not True or preferences.text_cps == 0:
            return text_input

        return speech_pause_adder(text_input)

    ## Initialization #############################################################################################
    # If your project already makes use of [config.say_menu_text_filter], this makes sure
    # your filter is also called in addition to this one.

    prev_filter = config.say_menu_text_filter
    config.say_menu_text_filter = add_speech_pauses

# The game starts here.

label start:
    
    play music crime

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene cage:
        zoom 0.35
        yalign 0.5
        xalign 0.5

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show hero buff at center:
        yalign 1

    # These display lines of dialogue.

    "Nothing he did could've prevented what had transpired."
    "That's why it's not to anyone's surprise to see him here, waiting."
    " "
    "You make your way down the corridor. You've only been here a couple of times in the past, but never for this reason."
    "It's quiet. " 
    extend "You expected noise, but the only sound is the echo of your footsteps hitting the floor."
    "Turn left, then right, then left again."

    "At the end of the hallway, there lies a cell. Stale, not beating, yet--"
    extend "no, you don't hear anything."
    "Strange."
    "You advance towards the chamber, and as you do, you see a figure sitting on the floor, back against the wall."
    " "
    V "HERO...," 
    V ". . . " 
    hide hero buff
    show villain sassy at center:
        yalign 1
    extend "you should be ashamed of yourself for keeping me waiting for as long as you have."
    "There's the grating you haven't been able to forget. The splitting voice of VILLAIN. The earlier possibility that he 
    might've already become a problem in the past makes you ache with a different kind of displeasure."
    "If only the mob had disabled his voice synthesizer, you think to yourself."
    "It'd certaintly be worth more than what most of his antics have cost you."
    "Momentarily, you hear the faint pleas of a fleeting sound. The way you came seems to be calling you. It beckons you to leave, 
    and it desperately awaits your arrival back to the familiar exterior."
    "But you can't leave, as disappointing as it is. You're here for a reason, and you have to see it through."
    "Even if you don't know what that reason is."
    H "Can it, VILLAIN. I'm not here for the banter. What do you want? Why..."
    extend "why did you want to see me?"
    V "Of course, you're only here on business. " 
    extend "How typical of you, HERO. Even when basking in the city's triumph, you still manage
    to diminish the liveliness of the moment."
    V "Tell me, has it been bothersome not being able to take the sole credit for the city's success? " 
    extend "For my \"termination\"?"
    "Why do you deal with his taunts? You know he's just trying to get under your skin, but you can't help but feel a twinge of irritation."
    V "Whatever, I won't waste your precious time."
    "That's a first."
    V "You're...probably wondering why I asked to have your aquaintance here, if I had to take a guess."
    H "It's definitely unusual..."
    "Villain sinks a nail into his lip, as he flashes you a daunting grin."
    H "You have no reasoning to be smiling."
    V "What, not in a good mood? You should see how it feels to be in a cell, HERO."
    H "I mean it. You shouldn't be taking this lightly. Just get whatever you wanted to say over with."
    V "Wh--"
    H "--in as {i}little{/i} words as possible. " 
    extend "Please."
    ". . ."
    "His brittle smile shatters into an understanding expression. You've never seen him at such a loss for words before. 
    It's...almost frightening, unlike the usual persona he puts on."
    V "I..didn't tell you to come so I could insult you, as fun as that sounds."
    H "You didn't?"
    "Huh."
    V "No, I,,I--we've been at this whole..cat-and-mouse game for quite a while now, haven't we? "
    extend "I soak in what glory I can,
    you get jealous and try to push me off my pedestal.."
    H "That's not--"
    V "--well, I'm starting to believe that this is. . .the end of that chase."
    "Is..he being serious? You thought the implications of the cage were enough to suggest that, but perhaps you were wrong."
    "VILLAIN averts his eyes from you, and you can see sparks fly from his skull's augmentations, almost as if his head is finally being put to a good use."
    H "You just {i}now{/i} caught onto that?"
    V "Byte me. "
    extend "Look, in truth, my predicament has left me to ponder some things. Some..attributes associated with the aftermath of my. . ."
    extend "(cough)."
    "It's rare to find VILLAIN in such disarray. Since when has he ever been at a loss for words?"
    H "You want me to...give you closure? Answer some questions?"
    V "I don't know if that's the term {i}I{/i} would use, but yes. I suppose I'm in need of some...'closure'."
    H "Why couldn't you have asked a guard? Talking to me specifically wasn't necessary."
    "Besides, you could've been out of here by now if he just asked for clarification upfront."
    V "You truly believe any of these people have the nerve to speak to me outright? Even now, cowards, all of them. "
    extend "They isolate me in this cell 
    and don't even have the decency to conversate..."
    V "I suppose I must still hold some charm, even in the state I'm in."
    "Something in you makes you think it still isn't admiration they have for him, but to tell him this would only leave room for another one of his rants."
    V "Besides, despite your horrific IQ and lack of style, you, uh..., "
    extend "you seem to be the only option I have left for a questionnaire."
    "Flattering."
    H "Alright. I guess I've got some time to spare for a couple of questions. What do you want to know?"
    "Maybe you can get this over quicker if you answer the questions before he can ask them. Leaving VILLAIN to his own devices is a dangerous game, 
    and this conversation has already been dragging on for too long as it is."
    #ask some questions
    define visited = set()
    label question_menu:
    menu:
        set visited
        "So, tomorrow...":
            jump tomorrow
        "About your equipment...":
            jump equipment
        "Your efforts against me...":
            jump efforts

    jump after_choices

    label tomorrow:
        show villain sassy
    H "So, tommorrow...there's been mention about the event happening later at night. Y'know, to avoid having {i}it{/i} accidentally attract younger folk."
    V "Apologies--{i}event{/i}? They're making an event out of me?"
    " "
    "Maybe that wasn't the best thing to bring up."
    H "uh. . .Everyone is really excited to see you go."
    H "After tommorrow night, I heard some...festivities are planned to take place."
    jump question_menu

    label equipment:
        show villain sassy
    H "About your equipment...Most of it will probably be disgarded to the High Council."
    #show villain reaction
    V "Wait, {i}they're{/i} taking ownership? What ever happened to \"it's too dangerous\"?"
    H "I guess they decided it was the owner, not the product."
    "You say this under your breath, but just loud enough for him to hear. He scoffs at the jab made at his actions."
    V "What do they plan to do with my hardware? Just..keep hold of it?"
    H "Who do you take them for? Obviously your equipment is going to be used for something."
    H "Honestly, I'm not sure for what, but it'd be a waste to disgard all of that work."
    V "{i}My{/i} work, in case you've forgotten. Shouldn't I have some say in the matter? My machinery is intended to be a tool for my recognition, not areas of governance. "
    V "It's a complete misuse of what I've worked to accomplish."
    "\"Worked to accomplish.\""
    "Clearly whatever he tried to amount to didn't end in his favor."
    V "(sigh)...nevertheless, that isn't what I--"
    H "You know, I bet the council would give me a payment in your weaponry if I asked."
    V " "
    V "You wouldn't."
    H "Why wouldn't I? Not only would that be in favor of the city's security, but could you imagine how many more quests I'd be hired for?"
    H "And here I thought fighting you gave me a good income..."
    H "{size=*0.5}God, maybe I could retire a bit earlier than I thought..{/size}"
    V "Retire?? HERO, you're 26. Why're you already thinking about retirement?"
    H "Because what's the point in working, if I have enough cash to keep myself comfortable?"
    V "What happened to the check you recieved for defeating me? Don't tell me you've spent it."
    H "I didn't...I didn't exactly get that payment."
    V "You what."
    "Ever since your first encounter with VILLAIN, it's been abundantly clear to the both pf you that fighting eachother came with no hard feelings."
    "Instead, while VILLAIN would be able to gain the recognition he desired, you'd recieve an income from stopping his weekly antics."
    "I mean, it's not like he's ever caused too much harm."
    extend "If he ever stepped out of line, you'd make sure to stop him. . .sometimes."
    V "God knows the High Council won't give me any credit, either.."
    H "Does...it really matter what you think? Not to be harsh, but. . .you'll be dead."
    V " "
    H "oh--I,,I was just saying what they'd think. Y'know, give you their point of view. Not that I actually--"
    V "HERO. . ."
    H "Sorry."
    jump question_menu
    
    label efforts:
        show villain sassy
    H "Your efforts against me...were they worth it?"
    V "Excuse me?"
    H "Look at where you ended up."
    jump question_menu
    
    label after_choices:
    "VILLAIN's goggle lense flickers, and he attempt to stand up, but it proves rather difficult without the use of his missing leg."
    "His eye clenches shut, and he grips a fistful of his shirt, spine curved in a way that shatters the illusion of his prideful demeanor."
    V "I don't need you thinking for me, HERO. I can. . .I can ask my own questions."
    "You raise an eyebrow, but it's hard not to feel at least a little bit of sympathy for him."
    H "Do you..need help getting up?"
    "VILLAIN raises a hand to keep you at bay, still hunched over himself."
    V "No, I don't."
    H "You sure? I'm sure I could--"
    V "--you could {i}what{/i}, HERO? Help me from a distance?"
    H "No, but--"
    V "--just. . .alt+tab it."
    "Even when at his worst, he still manages to spew those puns of his. Though they're the bane of your existence, you have to admit, 
    that must take some dedication."
    H "What questions have I not answered yet that you still want a response to? I've covered almost every topic you care about possible."
    "For a second, it almost seems as if VILLAIN will refuse to respond, his chin lowered and jaw clenched. His head tilts at an angle and a voice comes
    out from underneath, but you suppose the sound is strained from the scratching of his neck."
    V "What. . ."
    extend "is going to happen to DAUGHTER?"
    "Amidst all of the recent panic, you completely forgot he bears custody of a little girl. Unfortunately for society, the heathen's been trained like a dog to resemble her father, and pleasing him 
    always seems to be paramount."
    "You contemplate how off-putting it is to never hear him talk about her, despite her appearance on the occassional heist and sceme. It's hard to think he has any thoughts 
    to spare for her, especially now."
    ". . ."
    "You guess being the daughter of a villain probably doesn't pay off as much as she's constantly made it out to be."
    H "...Excuse me? I thought you didn't care about DAUGHTER. Why be concerned with her {i}now{/i}?"
    V "Of course I'd be on edge regarding her livelihood. She's my off-spring. What kind of father would I be if I didn't want to assure she'll
    be somewhere safe?"
    "VILLAIN's tone turns sharp, and he flicks an open hand upward at your person."
    H "Uh, the kind of dad that'd let his daughter go commit felonies with a smile on her face? If you ask me, it's a little too late to start caring for her wellbeing."
    V "Oh please, she practically begs to come with me."
    H "That doesn't mean you {i}let{/i} her????"
    H "If DAUGHTER asked you to let her go on a murder spree, would you?"
    V "I mean..., what's the context?"
    "Oh dear god."
    H "Then, what if she would want to..I,,I dont know--vandalize the city? You'd let her do that?"
    V "She does that on a week-to-week basis, HERO. Just what point are you trying to make here?"
    H "The point that I'm trying to--the point I'm trying to make is that you've CLEARLY never been a good father. Why should it matter to you if she ends up at the bottom of a ditch somewhere?"
    V "Will she?"
    " "
    H "I,,I mean, not..likely?"
    V "That's not an answer, HERO."
    "A groan bellows from underneath your throat."
    H "I don't know. "
    extend "If I had to guess, she'll probably get put into a foster care system."
    V "what?"
    H "Y'know, like every other non-parented kid her age...?"
    H "The system isn't amazing, but it's not anything horrific. She'll do fine."
    "VILLAIN stares at you with an extreme lack of warmth."
    H "Oh, come on. Don't look at me, like that. I'm telling you she'll--"
    V "--she can't wind up at a place like that."
    "uh...?"
    H "Why...not?"
    V "Why n--? Use that thick head of your's. If they finally came after me, who do you think is next?"
    V "These people aren't going to wait to decide what to do with her."
    V "They're going to tear her apart, HERO. Call me superstitious all you want, but she can't be left in society's care."
    V "There'll be nothing left of her, I promise you that. They're going to {b}kill{/b} DAUGHTER because of the things she's done in relation to me."
    "For once, what he's telling you probably holds some truth. The way this town got violent when they had enough of VILLAIN's antics proves his worrying right."
    "Besides, she's always taken after her father."
    H "Look, I get that you're worried for her, but what do you want {i}me{/i} to do about it? I can't control her public image."
    H "Maybe she should've thought twice before following in your footsteps."
    V "You want an 11-year-old to be independent?"
    "Good point."
    H "No, but--mgh. . ., unless you want me to somehow erase her sins against the law, there's really nothing I can do for her. My hands are tied."
    V "You'd rather let her die, than do something to stop her death from happening? She's just a kid, and frankly--frankly, I...I can't do anything for her six feet under." 
    V "I need your help, HERO."
    V ". . .{b}please.{/b}"
    H "Listen, I..I wish I could help. Really, I do, but...it's high risk, low reward." 
    H "I'm not going to endanger my job to protect your spawn."
    ". . ."
    V "{i}What kind of hero are you.{/i}"
    " "
    H "Are you really going to ask me that? I thought you, out of everyone, already knew I don't do things with no incentive, especially when it comes to situations like this. Now, if that was all you had to ask me..."
    "You turn your back from the outcast. POOF."
    V "--wait! I,,I can...I can make it worth your while! HERO, please!"
        # This ends the game.

    return
