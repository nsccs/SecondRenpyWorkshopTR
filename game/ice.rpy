# TODOLIST:
# Incorporate variables and statements for affection rating


# declare the characters used in the path
define e = Character("Eileen")
define b = Character("Brewer")
define i = Character("Ice Factory Owner")
define mc = Character("Main Character")

default monster_name = "Ice Monster"
define mo = Character("[monster_name]")

# initialize the path with a label
label ice_path:

    # show the background scene for the ice path
    scene inside house
    show ice egg

    "Standing inside the house, you feel as though the air is colder than usual."
    "You glance at the egg and notice a slight steam rising into the air."
    "Looking closely you notice it has a slightly reflective sparkle to it,  like morning frost on the grass."
    "The egg shakes slightly for a second."
    show ice egg
    with hpunch 
    mc "What is happening?"
    "The egg begins to crack open and hatch!"

    # EGG HATCHING TRANSITION HERE
    show ice egg:
        linear 1.0 align (0.5, 1.0) knot (0.0, .33) knot (1.0, .66)
        linear 0.25 zoom 1.4 
        linear 0.25 zoom 1.0
        repeat 2
    pause 3.1

    hide ice egg
    show ice baby
    with pixellate

    "The egg cracks open and melts away! A small frost and ice colored monster emerges!"
    "A pointy glacier like horn protrudes from it's forehead. It's distinctive tall ears are perked up and it's 
    long tail hovers in the air."
    "You can determine that the monster is the source of the chill in the room. Despite the dangerous appearance of it's
    horn it appears friendly and looks at you with slight expectancy, standing in a relaxed position."
    "The monster looks directly at you, as if waiting for something."

    menu:
        "Should I give it a name?":
            $ monster_name = renpy.input("Enter name: ", length = 32).capitalize()
            show ice baby happy
            mo "shreee"
            pause 1.0
            hide ice baby happy
            with moveoutright
            # ADD AFFECTION
        "Make it go away":
            mc "You're making me cold! Back up!"
            show ice baby sad
            "[monster_name] hangs it's head and shuffles away slowly."
            pause 1.0
            hide ice baby
            with moveoutright
            # SUBTRACT AFFECTION
    #show ice baby
    "In preparation of settling in for the colder than usual night you put on some extra clothes."
    "[monster_name] seems unbothered by the cold and curls up in the middle of the room."
    show ice baby
    with moveinright
    "A gentle breeze flows through the window adding even more to the chill."

    menu:
        "Shut the window to keep the cold air out and insulate the house more":
            show ice baby sad
            "[monster_name] looks longingly out the window and seems to miss the cooling breeze."
            mo "Rshhesss"
            # SUBTRACT AFFECTION
        "Bundle up as tightly as you can and leave the window alone":
            mc "I guess this is more like your natural habitat. Wherever that is."
            show ice baby happy
            "[monster_name] seems to let go of it's tenseness and gently drift off to sleep"
            # ADD AFFECTION
    
    show ice baby
    mc "I'm going to have to head into town in the morning and find a way to make some extra money to keep up 
    on supplies and food now that there's another mouth to feed here."

    "Feelings of uncertainty cloud your mind, but tiredness overrules your racing thoughts. 
    You close your eyes and fall asleep."

    hide ice baby
    with fade
    scene inside house
    
    # set the scene for the next morning
    "You wake up the next morning. The sun has risen, and it\'s a clear day outside. "
    "[monster_name] is already awake. [monster_name] stands next to the door quietly watching you awaiting something."
    mc "You're up already? I wonder if you slept much at all. Well what should I get started with today?"

    menu:
        "Head towards the door":
            jump door_path
        "Head towards the book shelf":
            jump bookshelf_path

    label bookshelf_path:
        "You move towards the other side of the room with the bookshelf."
        mc "What should I do?"
        menu:
            "Write journal entry":
                "You write in your journal"
            "Head towards the door":
                jump door_path

    label door_path:
        "As you approach the door the [monster_name] looks up at you expectantly"
        mo "shreeluu?"
        menu:
            "Open the door and go outside":
                "You go outside."
            "Move towards the bookshelf":
                jump bookshelf_path

    label outside_path:
        scene outside house
        "You step outside. The sun shines down on the front of the house and the surrounding garden plantlife. The air 
        is warm and heat shimmers in the distance."
        mc "What a nice day outside. I think I'll get started on so..."
        "You hear a scuffling sound coming from behind"
        mc "Wha?"
        show ice baby
        with moveinright
        "[monster_name] is scooping up dirt and attempting to carve out a burrow in the shade of your plants in the garden."
        menu:
            "It must be looking for some shade!":
                mc "You poor thing. You must be having a hard time in this heat."
                mc "I'll build you a little shelter."
                "You break a few branches off some nearby trees and form a small canopy by intertwining them with some
                leaves and other foliage from the surrounding plantlife."
                show ice baby happy
                mo "Sruuush!"
                # INCREASE AFFECTION
                "The [monster_name] seems to love it's new shady shelter."
            "Chase it away from the garden":
                mc "Hey get out of there! You're ruining my plants!"
                show ice baby sad
                with moveoutleft
                mo "Shuruu!!"
                # DECREASE AFFECTION
                "[monster_name] runs around towards the back side of the house, looking for some shade."
                hide ice baby
                with moveoutleft
        
    

    # end the game
    return