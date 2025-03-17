# declare the characters used in the path
define e = Character("Eileen")
define b = Character("Brewer")
define i = Character("Ice Factory Owner")
define mc = Character("Main Character")
define mo = Character("Monster")

# initialize the path with a label
label ice_path:

    # show the background scene for the ice path
    scene bg_room

    # show the character sprite
    show eileen happy

    # display the first line of dialogue
    e "Welcome to the ice path!"

    # set the scene
    "You and the ice monster begin walking down the street heading into town."
    "As you continue walking down the pathway a man sees you and the ice monster."

    # conversation between the main character and the brewer
    b "Hey, is that a sentient ice cube you've got there or something?"

    mc "Yeah pretty much. I just found an egg a while ago and now it hatched into this."

    b "It's kind of cute actually, mind if I give it a pat?"

    mc "Sure go ahead, I think it likes that kind of stuff!"

    "The monster smiles and purrs happily"

    b "Whoa! It's freezing cold to the touch that's bizarre!"

    mc "well I'd better be going. we're getting hungry and I have no idea how I'm going to find enough food for the both of us today."

    b "Huh, okay. Say I think I've got an idea why don't you and this little fella come by the brewery later on. I think we might be able to work something out to get a meal for the two of you in exchange for a small favor."

    menu:
        "Okay!":
            mc "That would be great! We could really use a good meal. We'll see you later."
        "No thanks.":
            mc "I don't know, I'll think about it. We might need more than just a meal to get out of my current situation."

    b "Alright then. Goodbye for now!"

    "You and the ice monster continue walking down the street."
    "You are approached by another figure, seemingly appearing from thin air."

    # conversation between the ice factory owner and the main character
    i "Hello there, I couldn't help overhearing your discussion there. Is it true that your creature there has special freezing powers?"

    mc "Oh hi. Um yeah I guess so I don't really know what it is."

    "The ice monster stares blankly."
    "The strange figure holds their hand out towards the ice monster who shys away from it."

    i "It does appear indeed to be giving off some cold energy into the air how intriguing..."

    i "It sounded like you might be in need of some money from your discussion earlier. Why don't you skip the brewery and come visit the ice block factory later instead. I'll pay you for your time, and it'll be much more than anything that brewery owner could offer you."

    menu:
        "Okay!":
            mc "Oh okay, we could really use the money. We'll see you later."
        "Not interested.":
            mc "I'll think about it, I haven't made up my mind yet."
    
    i "Very well then."

    # decide which person you are going to visit
    mc "Hmmm decisions decisions... What should I do?"

    menu:
        "Visit the brewery":
            jump brewery_path
        "Visit the ice block factory":
            jump ice_block_factory_path

    # brewery scene
    label brewery_path:
        b "Hey there! Good to see you and your little pal again. Why don't the two of you have a seat over there."

        mc "Okay thanks!"

        b "Alright you two, here's my proposition. I've got a bunch of customers coming in soon but we ran out of money to buy ice to chill the drinks. So all I've got is some warm brews. That's not going to be too good."

        b "If I can bring the drinks by your table maybe this little fella could chill them real quick before I serve them up to the customers. In exchange I'll bring you anything to eat or drink that you want and I'll send you home with a little bit of the tips that we make if the customers are happy with their cold drinks too. What do you say?"

        menu:
            "Take the deal":
                mc "I think that's something we can work with! Are you feeling up to it ice monster?"

                mo "*chirps agreeably*"

                b "That's great! This is going to be a huge help. Here's the menu today take a look and let me know what you and the little fella would like to have."

                menu:
                    "food option #1":
                        mc "1"
                    "food option #2":
                        mc "2"
                    "food option #3":
                        mc "3"

            "Pass on the deal":
                mc "Actually I think we have to get out of here. Sorry!"

                b "Alright. That's too bad. The offer still stands and you know where to find me if things change."

                menu:
                    "Head back home":
                        "return to the house"
                    "Head to the ice block factory":
                        jump ice_block_factory_path

    # ice block factory scene
    label ice_block_factory_path:

        i "Welcome to our facilities. I'm glad you've decided to assist us with our production here. I think you'll find it can be well worth your while."

        mc "We could really use the money."

        i "Then let's not waste any time and get right down to business. I've got a warehouse full of ice blocks that need chilling and we need to reach our quota for new blocks created for the week as well."

        i "Why don't you send your little ice monster down to the warehouse for me where my associates can direct it's work and meanwhile you and I can discuss the financial agreements."

        menu:
            "Take the deal":
                mc "Alright. Lets get some money into my pockets. Go on ahead ice monster."

                i "Excellent, assistant take this creature down to the warehouse."

                "The monster whines quietly as it follows the assistant out of the room."
                
                i "Now, let's get down to business. Tell me, which of these offers interests you the most?"

                menu:
                    "offer 1":
                        "1"
                    "offer 2":
                        "2"
                    "offer 3":
                        "3"

                i "Come back tonight at the end of the day and you and the creature can go back to your home with your money."

            "Pass on the deal":
                mc "Actually I think that we have to get out of here. Sorry!"

                i "Suit yourself. Let me know when you want to become somebody important in this town."


    menu:
        "make the egg monster happy":
            "The ice egg monster smiles happily!"
        "make the egg monster sad":
            "The ice egg monster gets sad"

    # end the game
    return