# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color = "#234291")
define a = Character("Alice")
define u = Character("Unknown")

init: 
    image Outside House = "Outside House.png"
    image Egg = "Egg.png"
    image park = "park.png"
    image bright = "Bright.png"
    image lost park = "lost park.png"
    image closet = "closet.png"
    image fridge = "fridge.png"
    image fireplace = "fireplace.png"
    image living room = "living room.png"
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    menu:
        "Eileen":
            "Your character is Eileen."
            jump characterEileen
        "Alice":
            "Your character is Alice."
            jump characterAlice

    label characterEileen:
        scene park:
            size(1920, 1080)

        "You are walking in a park. It's a nice sunny day"

        show eileen happy

        "You stray into a different path and accidentally go through a hidden way."

        scene lost park:
            size(1920, 1080)

        u "Look who has finally shown up"
        "You are startled."
        u "Your destiny calls you. I have protected this for years. But now you have to be responsible for what was meant to be yours."
        e "Who is this?"
        u "You do not need to know this child."
        u "All you need to do is take the egg with you."
        u "I'll finally be free of this burden."

        hide eileen happy

        "A bright light appears."
        scene bright:
            size(1920, 1080)

        "There's suddenly an egg in front of you."
        scene lost park:
            size(1920, 1080)
        show Egg

        u "Take the egg and you'll be leaded outside."
        hide Egg
        menu:
            "No, I'll not take the egg. I'll find my way on my own." :
                u "Okay then. You have made your decision. I'll see you in your next life."
                "As you walk ahead the unknown voice fades away."
                "You stumble into stuff."
                e "I'm really lost. Isn't this just the park near my house?"
                "As you go ahead suddenly you start to suffocate and die in there."
                e "Mom!!!, I can't breathe."
                e "Plea.. sav..."
                u "You made your decision. See you next time."
                scene black
                return

            "Okay I'll take the egg. Am I supposed to take care of it?" : 
                u "Yes child. Take good care of it."
                u "This will be of use to you."

        "You are suddenly transported to the area of the park where you got lost."
        scene park:
            size(1920, 1080)
        e "What am I supposed to do with this now?"
        e "At least, I am alive."
        "You walk your way home."

        scene Outside House
        e "Where should I put this egg?"
        e "When is it going to hatch?"

        scene closet:
            size(1920, 1080)
        e "Should I keep it in the closet?"

        scene fridge:
            size(1920, 1080)
        e "Maybe in the fridge"
        scene fireplace:
            size(1920, 1080)
        e "Or near the fireplace"

        scene living room:
            size(1920, 1080)
        "Where should you place it?"
        menu: 
            "Fireplace":
                jump fire_path
            "Fridge":
                "You go by your day. Few weeks pass by."
                "You see the egg sometimes when you open and close the fridge."
                "One day, you think you might need to take the egg out as it was stupid of you to put it inside the fridge"
                "Who puts an egg that would hatch into the fridge?"
                scene fridge
                "You take the egg out"
                jump ice_path
                
            "Closet":
                scene closet:
                    size(1920, 1080)
                
                "You place it inside the closet, away from anybody's sight."
                e "I am done for now."

                scene living room:
                    size(1920, 1080)
                e "Hopefully, it is not something scary."
                scene black
                
                "You go to your normal life again "
                "After some weeks you remember the egg you placed in the closet."

                "You open the closet hoping the egg hasn't gone bad."
                scene closet:
                    size(1920, 1080)
                "You take the egg out."
                scene living room:
                    size(1920,1080)
                jump shadow_path
            


    label characterAlice:
        scene park:
            size(1920, 1080)

        "You are walking in a park. It's a nice sunny day"

        show alice happy

        "You stray into a different path and accidentally go through a hidden way."

        scene lost park:
            size(1920, 1080)

        u "Look who has finally shown up"
        "You are startled."
        u "Your destiny calls you. I have protected this for years. But now you have to be responsible for what was meant to be yours."
        a "Who is this?"
        u "You do not need to know this child."
        u "All you need to do is take the egg with you."
        u "I'll finally be free of this burden."

        hide alice happy

        "A bright light appears."
        scene bright:
            size(1920, 1080)

        "There's suddenly an egg in front of you."
        scene lost park:
            size(1920, 1080)
        show Egg

        u "Take the egg and you'll be leaded outside."
        hide Egg
        menu:
            "No, I'll not take the egg. I'll find my way on my own." :
                u "Okay then. You have made your decision. I'll see you in your next life."
                "As you walk ahead the unknown voice fades away."
                "You stumble into stuff."
                a "I'm really lost. Isn't this just the park near my house?"
                "As you go ahead suddenly you start to suffocate and die in there."
                a "Mom!!!, I can't breathe."
                a "Plea.. sav..."
                u "You made your decision. See you next time."
                scene black
                return

            "Okay I'll take the egg. Am I supposed to take care of it?" : 
                u "Yes child. Take good care of it."
                u "This will be of use to you."

        "You are suddenly transported to the area of the park where you got lost."
        scene park:
            size(1920, 1080)
        a "What am I supposed to do with this now?"
        a "Atleast I am alive."
        "You walk your way home."

        scene Outside House
        a "Where should I keep this egg?"
        "You sigh."
        a "When is it going to hatch?"

        scene closet:
            size(1920, 1080)

        a "Should I keep it in the closet?"
        scene fridge:
            size(1920, 1080)
        a "Maybe in the fridge"

        scene fireplace:
            size(1920, 1080)
        a "Or near the fireplace"
        
        scene living room:
            size(1920, 1080)
        "Where should you place it?"
        menu: 
            "Fireplace":
                jump fire_path
            "Fridge":
                jump ice_path
            "Closet":
                scene closet:
                    size(1920, 1080)
                
                "You place it inside the closet, away from anybody's sight."
                a "I am done for now."

                scene living room:
                    size(1920, 1080)
                a "Hopefully, it is not something scary."
                scene black
                "You go to your normal life again "
                "After some weeks you remember the egg you placed in the closet."

                
                "You open the closet hoping the egg hasn't gone bad."
                scene closet:
                    size(1920, 1080)
                "You take the egg out."
                jump shadow_path
            



    # This ends the game.

    return
