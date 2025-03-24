# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define u = "Unknown"
define MO_Name = "Monster"
define MC_Name = "Nicholas Monkshire"
define MO = Character(MO_Name)
define MC = Character(MC_Name)
define u = Character("Unknown")
define Aff = 0

init: 
    image end = "end.png"
    image fire = "fire.png"
    image field = "field.png"
    image sky = "sky.png"
    image wings = "wings.png"
    image castle = "castle.png" 
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

    scene inside house

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    menu:
        "My name is Nicholas Monkshire":
            "You are Nicholas Monkshire."

        "That's not my name":
            $ MC_Name = renpy.input("What is your name?").capitalize()
            $ MC = Character(MC_Name)
            "You are [MC_Name]"

    $ a = MC
    
    label characterAlice:
        scene park:
            size(1920, 1080)

        "You are walking in a park. It's a nice sunny day"

        

        "You stray into a different path and accidentally go through a hidden way."

        scene lost park:
            size(1920, 1080)

        u "Look who has finally shown up"
        "You are startled."
        u "Your destiny calls you. I have protected this for years. But now you have to be responsible for what was meant to be yours."
        MC "Who is this?"
        u "You do not need to know this child."
        u "All you need to do is take the egg with you."
        u "I'll finally be free of this burden."

        

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
                MC "I'm really lost. Isn't this just the park near my house?"
                "As you go ahead suddenly you start to suffocate and die in there."
                MC "Mom!!! I can't breathe."
                MC "Plea.. sav..."
                u "You made your decision. See you next time."
                scene black
                return

            "Okay I'll take the egg. Am I supposed to take care of it?" : 
                u "Yes child. Take good care of it."
                u "This will be of use to you."

        "You are suddenly transported to the area of the park where you got lost."
        scene park:
            size(1920, 1080)
        MC "What am I supposed to do with this now?"
        MC "At least I am alive."
        "You walk your way home."

        scene Outside House
        MC "Where should I keep this egg?"
        "You sigh."
        MC "When is it going to hatch?"

        scene closet:
            size(1920, 1080)

        MC "Should I keep it in the closet?"
        scene fridge:
            size(1920, 1080)
        MC "Maybe in the fridge"

        scene fireplace:
            size(1920, 1080)
        MC "Or near the fireplace"
        
        scene living room:
            size(1920, 1080)
        "Where should you place it?"
        menu: 
            #"Fireplace":
                #jump fire_path
            "Fridge":
                "You go by your day. Few weeks pass by."
                "You see the egg sometimes when you open and close the fridge."
                "One day, you think you might need to take the egg out as it was stupid of you to put it inside the fridge"
                "Who puts an egg that would hatch into the fridge?"
                scene fridge:
                    size(1920, 1080)
                "You take the egg out"
                jump ice_path
            "Closet":
                scene closet:
                    size(1920, 1080)
                
                "You place it inside the closet, away from anybody's sight."
                MC "I am done for now."

                scene living room:
                    size(1920, 1080)
                MC "Hopefully, it is not something scary."
                scene black
                "You go to your normal life again "
                "After some weeks you remember the egg you placed in the closet."

                
                "You open the closet hoping the egg hasn't gone bad."
                scene closet:
                    size(1920, 1080)
                "You take the egg out."
                jump shadow_path

            

    label shadowGameEnding:
        if Aff <= -12:
            "You were in your house in the living room"
            scene living room:
                size(1920, 1080)
            "You and the monster had been living together for a few months. You weren't very close and didn't treat it nicely."
            "The monster was trying to get close to you."
            window hide
            show shadow baby with moveinbottom
            pause 0.15
            hide shadow baby with moveoutbottom
            pause 0.1
            show shadow baby happy with moveinbottom
            pause 0.2
            hide shadow baby happy with moveoutbottom
            pause 0.1
            show shadow baby with moveinbottom
            pause 0.15
            hide shadow baby with moveoutbottom
            window show

            show shadow baby happy

            "Kweh!!"
            "You didn't like it very much so you pushed it away."
            show shadow baby sad
            "The monster didn't like it."
            show shadow baby sad:
                linear 0.5 zoom 1.5
            "It grew bigger and started breathing fire."
            scene fire
            "You were startled."
            MC "STOP"
            MC "Hey, what are you doing?"
            "The monster was angry and didn't feel like stopping."
            show shadow baby sad:
                linear 0.75 zoom 1.5
            show outside house fire
            "It went out of the house and started breathing fire there as well."
            "The whole village was engulfed by the fire."
            MC "Please, stop"
            show shadow baby
            "The monster looked at you and felt a little bit of hesitation."
            "But, it disappeared in an instant."
            show shadow baby sad:
                linear 0.5 zoom 1.5
            "It breathed fire towards you."
            scene fire:
                size(1920,1080)
            MC "Nooooo"


        elif -12 < Aff <= 10:
            scene living room:
                size(1920, 1080)
            "It has been a while since you and the monster started living together."
            show shadow baby
            "You tolerate it and it tolerates you"
            "You have been getting along well"
            "The monster and you feel like an unconventional family"
            "The monster has grown up"
            show shadow baby:
                linear 0.5 zoom 1.5
            "It feels the need to part ways with you for its development"
            hide shadow baby
            MC "Are you finally leaving?"
            "It looks at you with its unwavering eyes"
            
            show shadow baby:
                linear 0.5 zoom 1.5
            hide shadow baby
            if Aff >-12 and Aff < 0 :
                "The monster finally says its goodbye to you."
                "It is both happy and sad leaving you."
                show shadow baby
                MC "I hope you'll have a nice life my friend. You'll always be welcomed here."
                MC "Bye!!"
                scene field:
                    size(1920, 1080)
                "Kweh!!"
                "THE END"                   
                scene end
            if Aff >= 0 and Aff <= 10 :
                "The monster is too attached to you to go anywhere far from you."
                MC "You love me that much?"
                show shadow baby happy
                MC "Aww, you can live with me for as long as you want to."
                window hide
                show shadow baby with moveinbottom
                pause 0.15
                hide shadow baby with moveoutbottom
                pause 0.1
                show shadow baby happy with moveinbottom
                pause 0.2
                hide shadow baby happy with moveoutbottom
                pause 0.1
                show shadow baby with moveinbottom
                pause 0.15
                hide shadow baby with moveoutbottom
                window show
                show shadow baby happy
                hide shadow baby happy
                "THE END"


        else:
            scene outside house
            "You really liked the monster. It was like your kid."
            "You took it with you everywhere you go and it was your bestfriend."
            "One fine day, you and the monster were chilling around the house."
            scene living room:
                size(1920, 1080)
            show shadow baby:
                linear 0.75
            "Suddenly you heard a sound coming from the monster."
            MO "Hey"
            show shadow baby happy
            hide shadow baby happy
            "You were shocked."
            "Your monster had never uttered a single word before this."
            MC "You can speak? Oh my god"
            MC "That's great"
            "You were overjoyed."
            show shadow baby happy
            MO "I am very happy too."
            MO "I want to thank you for taking care of me this well."
            MO "My kind rarely develops this attribute."
            MO "And its all because of how well you took care of me that I developed it."
            hide shadow baby happy
            MC "Aww, I did it because I wanted to. You do not need to thank me"
            show shadow baby
            MO "Since you have taken care of me I have something to say to you"
            MO "I can grant you a wish, whatever it may be it'll be fulfilled."
            MO "Ask away."
            menu:
                "I want to be able to fly. Can you do that for me?":
                    scene wings:
                        size(1920, 1080)
                    scene wings:
                        size(1920, 1080)
                        zoom 1.5

                    "All of a sudden wings got attached to you body."

                    MC "Thank you so much."
                    MO "That's alright."

                    scene sky
                    "You fly to the sky."
                    "Its nice and you and the monster live happily thereafter."
                    scene outside house
                    window hide
                    show shadow baby with moveinbottom
                    pause 0.15
                    hide shadow baby with moveoutbottom
                    pause 0.1
                    show shadow baby happy with moveinbottom
                    pause 0.2
                    hide shadow baby happy with moveoutbottom
                    pause 0.1
                    show shadow baby with moveinbottom
                    pause 0.15
                    hide shadow baby with moveoutbottom
                    window show

                    show shadow baby happy

                    hide shadow baby happy
                    scene end
                "I want a big house. So that I can live with you.":
                    "All of a sudden you saw your house turned to a big castle. You were even given the papers for the land and the hgouse. Your monster is very practical :)"
                    scene castle
                    MC "Thank you dear. Now you and I can live together forever."
                    MO "Yayyyyy."
                    show shadow baby happy
                    hide shadow baby happy
                    scene end
                "I do not want anything what I have is enough for now.":
                    scene living room:
                        size(1920, 1080)
                    "Hearing this the monster liked your sincerity. He was expecting something similar to come out of your mouth so, It wasn't shpcking."
                    MO "Okay, then. As you have said this, I'd like to grant every wish you ask for henceforth."
                    MC "I wish for you and I to live happily."
                    "You and the monster live happily and as the time goes the monster grants every wish you asked for. It knew you wouldn't ask for much."
                    "So, he was happy to comply."

                    window hide
                    show shadow baby with moveinbottom
                    pause 0.15
                    hide shadow baby with moveoutbottom
                    pause 0.1
                    show shadow baby happy with moveinbottom
                    pause 0.2
                    hide shadow baby happy with moveoutbottom
                    pause 0.1
                    show shadow baby with moveinbottom
                    pause 0.15
                    hide shadow baby with moveoutbottom
                    window show

                    show shadow baby happy
                    hide shadow baby happy
                    scene end
                    "THE END"

            
            
label iceGameEnding:
        if Aff <= -10 :
            "You were in your house in the living room"
            scene living room:
                size(1920, 1080)
            "You and the monster had been living together for a few months. You weren't very close and didn't treat it nicely."
            "The monster was trying to get close to you."
            window hide
            show ice baby with moveinbottom
            pause 0.15
            hide ice baby with moveoutbottom
            pause 0.1
            show ice baby happy with moveinbottom
            pause 0.2
            hide ice baby happy with moveoutbottom
            pause 0.1
            show ice baby with moveinbottom
            pause 0.15
            hide ice baby with moveoutbottom
            window show

            show ice baby happy

            "Kweh!!"
            "You didn't like it very much so you pushed it away."
            show ice baby sad
            "The monster didn't like it."
            show ice baby sad:
                linear 0.5 zoom 1.5
            "It grew bigger and started breathing fire."
            scene fire
            "You were startled."
            MC "STOP"
            MC "Hey, what are you doing?"
            "The monster was angry and didn't feel like stopping."
            show ice baby sad:
                linear 0.75 zoom 1.5
            show outside house fire
            "It went out of the house and started breathing fire there as well."
            "The whole village was engulfed by the fire."
            MC "Please, stop"
            show ice baby
            "The monster looked at you and felt a little bit of hesitation."
            "But, it disappeared in an instant."
            show ice baby sad:
                linear 0.5 zoom 1.5
            "It breathed fire towards you."
            scene fire:
                size(1920,1080)
            MC "Nooooo"
            return


        elif -10 < Aff <= 10:
            scene living room:
                size(1920, 1080)
            "It has been a while since you and the monster started living together."
            show ice baby
            "You tolerate it and it tolerates you"
            "You have been getting along well"
            "The monster and you feel like an unconventional family"
            "The monster has grown up"
            show ice baby:
                linear 0.5 zoom 1.5
            "It feels the need to part ways with you for its development"
            hide ice baby
            MC "Are you finally leaving?"
            "It looks at you with its unwavering eyes"
            
            show ice baby:
                linear 0.5 zoom 1.5
            hide ice baby
            if Aff > -10 or Aff < 0 :
                "The monster finally says its goodbye to you."
                "It is both happy and sad leaving you."
                show ice baby
                MC "I hope you'll have a nice life my friend. You'll always be welcomed here."
                MC "Bye!!"
                scene field:
                    size(1920, 1080)
                "Kweh!!"
                "THE END"                   
                scene end
                return
            if Aff >= 0:
                "The monster is too attached to you to go anywhere far from you."
                MC "You love me that much?"
                show ice baby happy
                MC "Aww, you can live with me for as long as you want to."
                window hide
                show ice baby with moveinbottom
                pause 0.15
                hide ice baby with moveoutbottom
                pause 0.1
                show ice baby happy with moveinbottom
                pause 0.2
                hide ice baby happy with moveoutbottom
                pause 0.1
                show ice baby with moveinbottom
                pause 0.15
                hide ice baby with moveoutbottom
                window show

                show ice baby happy
                hide ice baby happy
                "THE END"
                return


        else:
            scene outside house
            "You really liked the monster. It was like your kid."
            "You took it with you everywhere you go and it was your bestfriend."
            "One fine day, you and the monster were chilling around the house."
            scene living room:
                size(1920, 1080)
            show ice baby:
                linear 0.75
            "Suddenly you heard a sound coming from the monster."
            MO "Hey"
            hide ice baby happy
            show ice baby happy
            hide ice baby happy
            "You were shocked."
            "Your monster had never uttered a single word before this."
            MC "You can speak? Oh my god"
            MC "That's great"
            "You were overjoyed."
            show ice baby happy
            MO "I am very happy too."
            MO "I want to thank you for taking care of me this well."
            MO "My kind rarely develops this attribute."
            MO "And its all because of how well you took care of me that I developed it."
            hide ice baby happy
            MC "Aww, I did it because I wanted to. You do not need to thank me"
            show ice baby
            MO "Since you have taken care of me I have something to say to you"
            MO "I can grant you a wish, whatever it may be it'll be fulfilled."
            MO "Ask away."
            menu:
                "I want to be able to fly. Can you do that for me?":
                    scene wings:
                        size(1920, 1080)
                    scene wings:
                        size(1920, 1080)
                        zoom 1.5

                    "All of a sudden wings got attached to you body."

                    MC "Thank you so much."
                    MO "That's alright."

                    scene sky
                    "You fly to the sky."
                    "Its nice and you and the monster live happily thereafter."
                    scene outside house
                    window hide
                    show ice baby with moveinbottom
                    pause 0.15
                    hide ice baby with moveoutbottom
                    pause 0.1
                    show ice baby happy with moveinbottom
                    pause 0.2
                    hide ice baby happy with moveoutbottom
                    pause 0.1
                    show ice baby with moveinbottom
                    pause 0.15
                    hide ice baby with moveoutbottom
                    window show

                    show ice baby happy

                    hide ice baby happy
                    scene end
                "I want a big house. So that I can live with you.":
                    "All of a sudden you saw your house turned to a big castle. You were even given the papers for the land and the hgouse. Your monster is very practical :)"
                    scene castle
                    MC "Thank you dear. Now you and I can live together forever."
                    MO "Yayyyyy."
                    show ice baby happy
                    hide ice baby happy
                    scene end
                "I do not want anything what I have is enough for now.":
                    scene living room:
                        size(1920, 1080)
                    "Hearing this the monster liked your sincerity. He was expecting something similar to come out of your mouth so, It wasn't shpcking."
                    MO "Okay, then. As you have said this, I'd like to grant every wish you ask for henceforth."
                    MC "I wish for you and I to live happily."
                    "You and the monster live happily and as the time goes the monster grants every wish you asked for. It knew you wouldn't ask for much."
                    "So, he was happy to comply."

                    window hide
                    show ice baby with moveinbottom
                    pause 0.15
                    hide ice baby with moveoutbottom
                    pause 0.1
                    show ice baby happy with moveinbottom
                    pause 0.2
                    hide ice baby happy with moveoutbottom
                    pause 0.1
                    show ice baby with moveinbottom
                    pause 0.15
                    hide ice baby with moveoutbottom
                    window show

                    show ice baby happy
                    hide ice baby happy
                    scene end
                    "THE END"

            


    # This ends the game.

    #return
