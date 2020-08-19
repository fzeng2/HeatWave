# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pov = Character("[povName]")


# The game starts here.


label start:
    python:
        povName = renpy.input("what is your name?")
        poveName = povName.strip()

        if not povName:
            povName = "Harry Potter"

    pov "My name is [povName]!"
    scene wizard
    "Hello [povName], wecomle to Howgratwards!"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    pause
    scene sorting_hat
    pause
    menu:
        "You have four choices:"
        "Gryffindor":
            "you selected Gryffindor"
        "Hufflepuff":
            "you selected Hufflepuff"
        "Ravenclaw":
            "you selected Ravenclaw"
        "Slytherin":
            "you selected Slytherin"
    label Gryffindor:
        "welcome to Gryffindor!"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.


    # This ends the game.

    return
