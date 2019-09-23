# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mark")
define f = Character("Flying Spaghetti Monster")
define me = "me"



# The game starts here.

label start:
    scene bg rain
    play music "rain.mp3"

    me "What is my purpose right now...."

    show Mark

    me "Why's there some jackass wearing a colander on his head?"
    "That won't even keep the rain off of him."

    m "Hey man have you heard of the religious sensation that's sweeping the nation."
    "The being that has boiled for our sins."
    "The one and only Flying Spaghetti Monster."

    me "Are you drunk?"

    m "No I'm just trying to spread the word after all I just became the new minister for the Church of the Flying Spaghetti Monster around the corner."

    me "Yeah ok man. See ya."

    scene

    me "Well that was freaking weird. Not everyday some guy with a colander on his head trys to get you to worship a Giant Spaghetti Monster."
    "Well at least all that is behind me now that i'm home."



    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.



    # This ends the game.

    return
