define WithShadow = False

label shadow_path:
    scene inside house
    show shadow egg
    "When you check the egg, you find it's changed colors and feels cool to the touch"
    "You might've thought it had died and started to rot, if not for the faint heartbeat pulsing through the shell"
    "Looking closer, you see that it retained its pearly sheen despite the darker color, but seems to have become 
    matte as if it's absorbing the light that hits it"
    "Suddenly, the egg rocks in your hands and starts to hatch"
    window hide
    show shadow egg:
        linear 1.0 align (0.5, 1.0) knot (0.0, .33) knot (1.0, .66)
        linear 0.25 zoom 1.4 
        linear 0.25 zoom 1.0
        repeat 2
    pause 3.1
    hide shadow egg
    show shadow baby
    with pixellate
    window show
    "In a blur of magic the egg disappears, and you're left with a strange bird-like monster with bright red eyes"
    "You have to swallow down instinctive revulsion and fear as you realize you've hatched a shadow monster" 
    "Shadow beasts are known to be the most dangerous and violent monsters around, to the point where most are 
    culled as soon as they're born, or trained harshly to ensure obedience for warfare"
    "But then, maybe that's {i}why{/i} they're so violent?"
    "Regardless, you've hatched it, so it's your responsiblility now"
    "You can't quite tell whether it has wings or claws, and they almost seem to shift between states as you stare"
    "The air around the monster feels dense with energy, and somehow darker than the rest of the room"
    "The monster stares deeply into your eyes, seemingly waiting for something"
    menu:
        "Name the monster":
            $ MO_Name = renpy.input("Enter name:", length=32).capitalize()
            $ MO = Character(MO_Name)
            $ Aff += 5
            show shadow baby happy
            "They chirp happily"
            MO"Kwee!"
        "It doesn't need a name":
            $ Aff -= 5
            $ MO_Name = "the monster"
            "It stares expectantly at you"
            "The creature follows you around for a few minutes glancing hopefully at you"
            MC"Shoo, stop bothering me"
            show shadow baby sad
            "Finally, the dense thing understands that you aren't going to name it, 
            and slinks away into a dark corner to leave you alone"
    show shadow baby
    "You're unsure what you'll have to feed [MO_Name], but thankfully it seems whatever kind of shadow monster they are isn't
    carnivorous, as it's very interested in a few vegetables from your garden"
    menu:
        "Feed [MO_Name]":
            $ Aff += 5
            show shadow baby happy
            "They give a happy chirp and quickly eat"
        "It can fend for itself":
            $ Aff -= 5
            "You grab the food and move it out of reach, vegetables are valueable and you aren't about to waste them when
            it could probably feed itself"
            show shadow baby sad
            "It stares mornfully at the veggies, but leaves to forage in the forest when you remain steadfast and nudge 
            it in that direction"
            hide shadow baby with fade
            pause 1.5
            "It takes a few hours, but eventually [MO_Name] returns, dragging its clawed feet"
            show shadow baby sad with moveinleft
    show shadow baby      
    "That night, you set out a blanket and [MO_Name] hides under it to sleep, happy with the warm darkness"
    hide shadow baby with moveoutbottom

    scene outside house
    with fade
    "The next day, you wake up early and take care of your garden and various chores around the house, [MO_Name] playfully 
    jumping in and out of shadows, especially yours, as you work"
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
    "Chores done, you need to head into town to buy some ingredients for dinner"
    show shadow baby with moveinbottom
    MO"Kweh?"
    "[MO_Name!c] notices you preparing to leave and goes to follow you"
    menu:
        "Lock the monster in the house":
            MC"Nope. Not happening."
            $ Aff -= 2
            scene inside house
            show shadow baby sad
            MC"You're staying right here, I can't have anyone realizing I hatched a {i}shadow monster{/i}"
            MO"Kwehh..."
            hide shadow baby
        "Have it hide in your shadow as you shop":
            $ Aff += 5
            $ WithShadow = True
            MC"Alright, alright, you can come...\n
            Just be careful to stay hidden in my shadow, okay?"
            show shadow baby happy
            MO"Kwee!"
            hide shadow baby happy with moveoutbottom
    scene village
    with fade
    "You go about your shopping as normal, quickly finding and buying the ingredients you need"
    if WithShadow == True:
        "Thankfully, [MO_Name] stays in your shadow the entire time, as far as you can tell. 
        You'll have to reward them somehow when you get back"
    "On your way back home, you notice a market stall with charms; a string of shiny black beads tipped by iridescent black
    feathers stands out as something [MO_Name] would like"
    menu:
        "Buy the charm":
            MC"Excuse me, I'd like to buy this charm"
            "You point to the one you want and the woman running the stall smiles and starts the process of checking out"
            $ BoughtCharm = True
            if WithShadow == True:
                "The moment you have the charm in your hand your shadow starts moving, [MO_Name] trying to climb out and 
                see what's going on"
                menu:
                    "Stomp on your shadow to keep [MO_Name] inside":
                        $ Aff -= 2
                        $ ShadowSeen = False
                        "There's a muffled \"kwehh\" from under your foot, but no one else seems to notice"
                        "You quickly pay and head home"
                    "Whisper at [MO_Name] to hide":
                        $ ShadowSeen = True
                        show shadow baby with easeinbottom
                        MC"{i}Shh! Hide!{/i}" 
                        hide shadow baby with moveoutbottom
                        "You glance around urgently, no one {i}seems{/i} to be paying attention to you, but you can see some gossips
                        whispering to each other, and the woman running the stall is seems confused"
                        "With a strained smile, you pay and rush home before anything else goes wrong"
        "Go straight home":
            $ BoughtCharm = False
            $ ShadowSeen = False
            "You decide not to buy the charm and head home"
            if WithShadow == True:
                "You'll just have to find some other way to reward [MO_Name] later"
    scene outside house
    with fade
    if WithShadow == True:
        show shadow baby with moveinbottom
        if BoughtCharm == True:
            MO"Kweh?"
            show charm
            menu:
                "Give [MO_Name] the charm":
                    $ Aff += 10
                    MC"Here, for you"
                    show shadow baby happy
                    MO"Kwee!"
                    hide charm with dissolve
                    "You both head inside"
                "Keep it for yourself":
                    $ Aff -= 1
                    MC"No, this is mine"
                    show shadow baby sad
                    hide charm with moveoutbottom
                    "You walk inside and [MO_Name] follows"
                "Throw it away to spite [MO_Name]":
                    $ Aff -= 10
                    MC"Tch, you don't deserve this"
                    "You walk inside and throw the charm in the fireplace"
                    scene inside house
                    hide charm with zoomout
                    show shadow baby sad
                    MO"Kwooooh..."
                    "[MO_Name] lets out a mournful coo"
scene inside house
if WithShadow == False:
    "[MO_Name!c] has been pacing back and forth, waiting for you to come home"
    "The moment you open the door they perk up and rush towards you"
    show shadow baby happy
    MO"Kweh!"
    menu:
        "Greet [MO_Name] with a hug":
            $ Aff += 2
            "You hug [MO_Name] and they purr happily"
            show shadow baby happy:
                linear 0.5 zoom 1.5
                linear 0.5 zoom 1.0
        "Dodge [MO_Name]":
            $ Aff -= 1
            show shadow baby
            MO"Kweh?"
            "It seems confused and slightly disappointed"
        "Push [MO_Name] away before it can touch you":
            if Aff > 0:
                $ Aff -= 2
                show shadow baby sad:
                    linear 0.5 zoom 0.75
                MO"Nyehh?"
                "It seems sad and confused at your rejection"
            else:
                show shadow baby:
                    linear 0.5 zoom 0.75
                MO"Krrr..."
                "[MO_Name] growls at you before lunging, claws out and sharp"
                show shadow baby:
                    linear 0.5 zoom 2.5 yalign 0.5
                "The last thing you see is the vivid red of [MO_Name]'s eyes as it guts you like a fish and the world fades to black"
                pause 0.5
                scene game over 
                with fade
                "You treated [MO_Name] poorly and they decided you would be better as prey than a parent"
                "Perhaps next time you should be kinder"
                return

