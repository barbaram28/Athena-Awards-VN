# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define V = Character("VILLAIN", color="#ff0080")
define H = Character("HERO", color="#ffee00")


# The game starts here.

label start:
    
    play music gameover

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene miami:
        zoom 2
        yalign 0.5

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
    V "HERO, you ghastly technophobe!" 
    V ". . . " 
    hide hero buff
    show villain sassy at center:
        yalign 1
    extend "You should be ashamed of yourself for keeping me waiting for as long as you have."
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
    "You've never seen VILLAIN in such disarray. Since when has he ever been at a loss for words?"
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
    "Maybe you can get this over quicker if you ask the questions. Leaving VILLAIN to his own devices is a dangerous game, 
    and this conversation has already been dragging on for too long as it is."
    #ask some questions
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
    V "--just..Alt+Tab it."
    "Even when at his worst, he still manages to spew those puns of his. Though they're the bane of your existence, you have to admit, 
    that must take some dedication."
    H "What questions have I not answered yet that you still want to know the answers to? I've covered almost every topic you care about possible."
    "For a second, it almost seems as if VILLAIN will refuse to respond, his chin lowered and jaw clenched. His head tilts at an angle and a voice comes
    out from underneath, but you suppose the sound is strained from the scratching of his neck."
    V "What. . ."
    extend "is going to happen to DAUGHTER?"
    "Amidst all of the recent panic, you completely forgot he bears custody of a little girl. Unfortunately for society, the heathen's been trained like a dog to resemble her father, and pleasing him 
    always seems to be paramount. You contemplate how off-putting it is to never hear him talk about her, despite her appearance on the occassional heist and sceme. It's hard to think he has any thoughts 
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
    V "What if they even force her to present herself in...in tacky clothing? In a t-shirt and..white sneakers?"
    "He gags at the thought, but come on. Really? There's a far worse fashion choice that needs to be confronted here."
    H "Okay, stop."
    H "Look, I get that you're all..worried for her, or something, but what do you want {i}me{/i} to do about it? Maybe she should've thought twice before following in your footsteps."
    V "You want an 11-year-old to be independent?"
    "Good point."
    H "No, but--mgh, unless you want me to somehow erase her sins against the law, there's really nothing I can do for her. My hands are tied."
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
