

define m = Character("Mark")
define f = Character("Flying Spaghetti Monster")
define me = "me"
define r = Character("Rick")






label start:
    scene bg church
    play music "Hymm.mp3"

    me "What is my purpose right now...."

    show mark

    me "Why's there some jackass wearing a colander on his head?"


    m "Hey man have you heard of the religious sensation that's sweeping the nation."
    m "The being that has boiled for our sins."
    m "The one and only Flying Spaghetti Monster."

    me "Are you drunk?"

    m "No I'm just trying to spread the word of our lord and savior."
    m "After all I just became the new minister for the Church of the Flying Spaghetti Monster around the corner."

    me "Yeah ok man. See ya."
    stop music
    scene kitchen
    with Dissolve(.5)

    me "Well that was freaking weird. Not everyday some guy with a colander on his head trys to get you to worship a Giant Spaghetti Monster."
    me "Well at least all that is behind me now that i'm home."


    scene table
    with Dissolve(0)
    show spaghetti
    play sound "spaghetclip.mp3"
    me "where'd this spaghetti come from"
    me "What kind of creep makes a bowl of spaghetti then leaves the house"

    f "It twas I."

    scene kitchen
    with Dissolve(.5)
    show spaghettimonster

    me "Oh my god."
    me "IT'S A FLYING SPAGHETTI MONSTER!"

    f "Yes it is I. I made you this sacred bounty to quench your hunger."

    me "What?! This doesn't make any sense. That lunatic must've drugged me somehow."

    f "I assure you my child that you are not inebriated, and this is very much real."

    f "Now dine on my body and allow me into you."

    me "I gotta get the fuck out of here."

    scene frontporch
    with Dissolve(0)

    me "(to self) I'll call Rick and see if he's willing to meet up. I need a drink."

    scene bar
    with Dissolve(.5)

    me "Glad it's not crowded in here today, but where the hell is Rick?"

    r "What's up man?"

    show rick

    me "Oh there you are man. It's a long story lets sit down and get a drink first."
    "(I tell Rick everything that's happened over the past day.)"

    "...... and then I called you  and here we are."

    r "That's uh quite the story, and you better not be high right now because I've been tying to get you to smoke stones with me for years so I'm gonna be pissed if it turns out you just got high without me."

    me "For the last time I'm not high unless that nut job drugged me somehow, and I will never smoke stone
     with you. I don't care how much fun you say it is to smoke it and then stare out your peephole and just freak the f*** out."

    r "Fine then lets just drink to forget."

    me "(A few hours of revelry later)"

    r "You know I was thinking all this started because of that guy Mark so what do you say we teach him a lesson?"

    menu:
        "What should I do?"


        "Teach that collandar wearing dick a lesson.":
            "Yeah let's go kick his ass."
            jump Sin


        "No I should rethink my purpose for being alive.":
            "Actually I do want to see Mark, but just to talk. I'll see you later."


    scene bg church




    return
