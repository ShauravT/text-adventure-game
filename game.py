import time
import textwrap
import words
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

def start():
    msg = textwrap.dedent('''
                            ********************************
                            *                              *
                            *  Welcome to Text Adventure!  *
                            *                              *
                            ********************************

                         ''')
    print_pause(msg)

def intro(item):  
    print_pause("You find yourself standing in an edge of "+ item[3] +", fliied with "+ item[4] +".")
    print_pause("Rumor has it that a "+ item[0] +" is somewhere around here, and has been terrifying the nearby area.")
    print_pause("In front of you is a house.")
    print_pause("In your right hand is a dark cave")
    print_pause("In your hand you have your trusty (but not very effective) "+ item[1] +".")

def generate_theme():
    # Generates random monster, weapons, place and a scenario for the game
    scene =[words.monster,words.weapon1,words.weapon2,words.place,words.scene]
    item =[]
    for list in scene:
        item.append(random.choice(list))

    intro(item)

def play_game():
    start()
    generate_theme()



play_game()
play_game()
play_game()




