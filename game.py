import time
import textwrap
import words
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

def intro(item):  
    # intro of the game
    msg = textwrap.dedent('''
                            ********************************
                            *                              *
                            *  Welcome to Text Adventure!  *
                            *                              *
                            ********************************

                         ''')
    print_pause(msg)
    print_pause("You find yourself standing in an edge of "+ item[3] +", fliied with "+ item[4] +".")
    print_pause("Rumor has it that a "+ item[0] +" is somewhere around here, and has been terrifying the nearby area.")
    print_pause("In front of you is a house.")
    print_pause("In your right hand is a dark cave")
    print_pause("In your hand you have your trusty (but not very effective) "+ item[1] +".")

def clear():
    print("\n\"*100)     

def generate_theme(item):
    # Generates random monster, weapons, place and a scenario for the game
    scene =[words.monster,words.weapon1,words.weapon2,words.place,words.scene]
    for list in scene:
        item.append(random.choice(list))

    return item

def house(item):

    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a "+ item[0] + ".")
    print_pause("Eep. This is the "+item[0]+"'s house!")
    print_pause("The "+item[0]+" attacks you!")
    if '1' not in item:
        print_pause("You feel a bit under-prepared for this, what with only having a "+item[1] +".")

    option = input("Would you like to (1) fight or (2) run away?")
    if option == '1':
        if '1' in item:
            print_pause("As the "+item[0]+" moves to attack, you unseath your new "+item[2])
            print_pause("The "+ item[2]+ " shines brightly in your hands as you brace yourself for the attack.")
            print_pause("But the "+item[0] +" takes one look at your shiny toy and runs away!")
            print_pause("You have rid the town of the gorgon. You are victorious!")
        elif random.randint(0,10)/2 == 0:
            print_pause("You do your best....")
            print_pause("But your "+item[1]+" is no match for the "+item[0]".")
            print_pause("You have been defeated!")
        else:
            print_pause("You do your best....")
            print_pause("You manage to injure the "+item[0]"'s right eye with the help of your"+item[1]".")
            print_pause("You barely make it back into the field. Luckily, you dont seem to have been followed.")
            choice(item)

    elif option =="2":
        print_pause("You run back into the field. Luckily, you dont seem to have been followed.")
        choice(item)


def cave(item):
    print_pause("You peer cautiously into the cave.")
    if '1' in item: 
        # has already come into the cave
        print_pause("You've been here before, and gotton all the good stuff. It's just an empty cave now.")
    
    else:
        # walks into the cave the first time
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical "+item[2]+"!")
        print_pause("You discard your silly old "+item[1]+"and take the "+item[2]+"with you.")
        item.append('1')
    print_pause("You walk back to the "+item[3]".")
    choice(item)

def choice(item):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would like to do?")
    area= input("(please enter 1 or 2.)")
    if area =='1':
        house(item)
    elif area =='2':
        cave(item)
    else:
        # if the user puts in anything except 1 or 2 the function keeps repeating itself
        choice(item)             

def game_finish(item):


def play_game():
    item =[]

    clear()
    generate_theme(item)
    intro(item)
    choice(item)





