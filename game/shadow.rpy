 
#fade, dissolve, pixellate, move,
#moveinright (Also: moveinleft, moveintop, moveinbottom),
#moveoutright (Also: moveoutleft, moveouttop, moveoutbottom),
#ease (Also: easeinright, easeinleft, easeintop, easeinbottom, easeoutright, easeoutleft, easeouttop, easeoutbottom),
#zoomin, zoomout, zoominout, vpunch, hpunch, blinds, squares,
#wipeleft (Also: wiperight, wipeup, wipedown),
#slideleft (Also:  slideright, slideup, slidedown),
#slideawayleft (Also: slideawayright, slideawayup, slideawaydown),
#irisin, irisout. 
define WithShadow = False


label shadow_path:
    scene inside house
    show shadow egg
    "When you check the egg, you find it's changed colors and feels cool to the touch"
    "You might've thought it had died and started to rot, if not for the faint heartbeat pulsing through the shell"
    "Looking closer, you see that it retained its pearly sheen despite the darker color, but seems to have become 
    matte as if it's absorbing the light that hits it"
    "Suddenly, the egg rocks in your hands and starts to hatch"
    show shadow egg:
        linear 1.0 align (0.5, 1.0) knot (0.0, .33) knot (1.0, .66)
        linear 0.25 zoom 1.4 
        linear 0.25 zoom 1.0
        repeat 2
    pause 3.1
    hide shadow egg
    show shadow baby
    with pixellate
    "In a blur of magic the egg disappears, and you're left with a strange bird-like monster with bright red eyes"
    "You have to swallow down instinctive revulsion and fear as you realize you've hatched a shadow monster, known
    to be the most dangerous and violent monsters around, to the point where most are culled as soon as they're born, 
    or trained harshly to ensure obedience for warfare"
    "But then, maybe that's {i}why{/i} they're so violent?"
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
        "It doesn't need a name.":
            $ Aff -= 5
            $ MO_Name = "the monster"
            "It stares expectantly at you"
            "The creature follows you around for a few minutes glancing hopefully at you"
            MC"Shoo, stop bothering me"
            show shadow baby sad
            "Finally, the dense thing understands that you aren't going to name it, 
            and slinks away into a dark corner to leave you alone"
    show shadow baby
    "You're unsure what you'll have to feed [MO_Name], but thankfully it seems whatever kind of shadow monster they are is 
    herbivorous and perfectly happy with a few vegetables from your garden"
    "That night, you set out a blanket and [MO_Name] happily hides under it to sleep"

    scene outside house
    with fade
    "The next day, you wake up early and take care of your garden and various chores around the house, [MO_Name] playfully 
    jumping in and out of shadows, especially yours, as you work"
    show shadow baby
    with moveinbottom
    pause 0.15
    hide shadow baby
    with moveoutbottom
    pause 0.1
    show shadow baby happy
    with moveinbottom
    pause 0.2
    hide shadow baby happy
    with moveoutbottom
    pause 0.1
    show shadow baby
    with moveinbottom
    pause 0.15
    hide shadow baby
    with moveoutbottom
    "Chores done, you need to head into town to buy some ingredients for dinner"
    show shadow baby
    with moveinbottom
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
            hide shadow baby happy
            with moveoutbottom
    scene village
    "You go about your shopping as normal, quickly finding and buying the ingredients you need"
    if WithShadow == True:
        "Thankfully, [MO_Name] stays in your shadow the entire time, as far as you can tell, 
        you'll have to reward them somehow when you get back"
    "On your way back home, you notice a market stall with charms, a string of shiny black beads tipped by iridescent black
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
                    "Whisper at [MO_Name] to hide":
                        $ ShadowSeen = True
                        show shadow baby at center
                        with moveinbottom
                        MC"{i}Shh! Hide!{/i}" 
                        hide shadow baby
                        with moveoutbottom
                        "You don't see anyone looking your way but hurry to leave just in case"
        "Go straight home":
            $ ShadowSeen = False
            "You decide not to buy the charm and head home"
            if WithShadow == True:
                "You'll just have to find some other way to reward [MO_Name] later"
            



    
