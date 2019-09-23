# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mark")
define f = Character("Flying Spaghetti Monster")
define me = "me"
define r = Character("Rick")




# The game starts here.

label start:
    scene bg rain
    play music "rain.mp3"

    me "What is my purpose right now...."

    show mark

    me "Why's there some jackass wearing a colander on his head?"
    me "That won't even keep the rain off of him."

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





    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.



    # This ends the game.

    return
