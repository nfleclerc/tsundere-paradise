# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define izzy = Character("Kristin", color="#FF003C")

image bg futon day = "bg/futon/futon day.png"
image izzy winter open = im.Scale("Miki/Miki Winter Uniform/Miki_A_WinterUniform_Open.png", 540, 960)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg futon day

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show izzy winter open

    # These display lines of dialogue.

    izzy "Hey there! Wanna watch some anime?"

    # This ends the game.

    return
