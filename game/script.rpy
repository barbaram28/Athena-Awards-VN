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

    "At the end of the hallway, there lies a cell. Stale, not beating, yet--no, you don't hear anything."
    "Strange."
    "You advance towards the chamber, and as you do, you see a figure sitting on the floor, back against the wall."
    " "
    V "HERO, you ghastly technophobe!" 
    V ". . . " 
    extend "You should be ashamed of yourself for keeping me waiting for so long."
    hide hero buff
    show villain sassy at center:
        yalign 1
    "Miss me so soon?"
    "There's the grating you haven't been able to forget. The splitting voice of VILLAIN. The earlier possibility that he 
    might've already become a problem in the past makes you ache with a different kind of displeasure."
    "If only the mob had disabled his voice synthesizer, you think to yourself."
    "It'd certaintly be worth more than what most of his antics have cost you. "
    extend "He's the kind of person to refresh someone's webpage simply to watch the loading screen, 
    having no doubt it'll function the more the touchpad is clicked."
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

    # This ends the game.

    return
