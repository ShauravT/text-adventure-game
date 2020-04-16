import time
import textwrap
import words
import random


def print_pause(message_to_print, sleep_time):
    # change delay time according to sleep_time
    print(message_to_print)
    time.sleep(sleep_time)


def intro(item):
    # intro of the game
    msg = textwrap.dedent('''
                            ********************************
                            *                              *
                            *  Welcome to Text Adventure!  *
                            *                              *
                            ********************************

                         ''')
    print_pause(msg, 2)
    print_pause("You find yourself standing in an edge of "
                + item[3] + ", filled with " + item[4] + ".", 2)
    print_pause("Rumor has it that a " + item[0] +
                " is somewhere around here, and has been "
                "terrifying the nearby area.", 2)
    print_pause("In front of you is a house.", 2)
    print_pause("In your right hand is a dark cave", 2)
    print_pause("In your hand you have your trusty (but not very effective) "
                + item[1] + ".", 3)


def clear():
    # Gives the screen a clean look
    print("\n"*100)


def generate_theme(item):
    # Generates random monster, weapons, place and a scenario for the game
    scene = [words.monster, words.weapon1, words.weapon2,
             words.place, words.scene]
    for list in scene:
        item.append(random.choice(list))
        # item[0] is monster
        # item[1] is small weapon
        # item[2] is final weapon
        # item[3] is the type of place
        # item[4] is the scenary of the place
    return item


def house(item):
    # House activity
    print_pause("You approach the door of the house.", 2)
    print_pause("You are about to knock when the door opens and out steps a "
                + item[0] + ".", 2)
    print_pause("......", 3)
    print_pause("Eep. This is the " + item[0] + "'s house!", 2)
    print_pause("The " + item[0] + " attacks you!", 2)
    if '1' not in item:
        # user hasn't got the final weapon
        print_pause("You feel a bit under-prepared for this,"
                    " what with only having a "
                    + item[1] + ".", 3)

    option = ''
    while option != '1' or option != '2':
        option = input("Would you like to (1) fight or (2) run away?\n")
        if option == '1':
            if '1' in item:
                # user has the final weapon
                print_pause("As the " + item[0] +
                            " moves to attack, you unseath your new "
                            + item[2], 2)
                print_pause("The " + item[2] +
                            " shines brightly in your hands "
                            "as you brace yourself for the attack.", 3)
                print_pause("But the " + item[0] +
                            " takes one look at your shiny toy "
                            "and runs away!", 2)
                print_pause("You have rid the town of the gorgon. "
                            "You are victorious!", 2)
                game_finish()
            else:
                print_pause("You do your best....", 2)
                print_pause("....", 3)
                if random.randint(1, 10) % 2 != 0:
                    # random set of event
                    # without final weapon
                    print_pause("But your " + item[1] +
                                " is no match for the " + item[0] + ".", 2)
                    print_pause("You have been defeated!", 2)
                    game_finish()
                    break
                else:
                    print_pause("You manage to injure the " + item[0] +
                                "'s right eye with the help of your "
                                + item[1] + ".", 2)
                    print_pause("You barely make it back into the field. "
                                "Luckily, you dont seem to have "
                                "been followed.", 2)
                    choice(item)

        elif option == "2":
            print_pause("You run back into the field. "
                        "Luckily, you dont seem to have been followed.", 3)
            choice(item)


def cave(item):
    print_pause("You peer cautiously into the cave.", 2)
    if '1' in item:
        # Came into the cave before
        print_pause("You've been here before, and gotton all the good stuff. "
                    "It's just an empty cave now.", 1)

    else:
        # walks into the cave the first time
        print_pause("Your eye catches a glint of metal behind a rock.", 2)
        print_pause("You have found the magical " + item[2] + "!", 2)
        print_pause("You discard your silly old " + item[1] +
                    " and take the " + item[2] + " with you.", 2)
        item.append('1')
    print_pause("You walk back to the " + item[3] + ".", 2)
    choice(item)


def choice(item):
    print_pause("Enter 1 to knock on the door of the house.", 1)
    print_pause("Enter 2 to peer into the cave.", 1)
    area = input("What would like to do?\n(please enter 1 or 2.)\n")
    if area == '1':
        house(item)
    elif area == '2':
        cave(item)
    else:
        # if the user puts in anything except
        # 1 or 2 the function keeps repeating itself
        choice(item)


def game_finish():
    print_pause("Game Over!", 1)
    play_again = input("Would you like to play again? (y/n)\n").lower()
    if play_again == 'y':
        play_game()
    elif play_again == 'n':
        print_pause("Thank you for playing!", 5)
    else:
        game_finish()


def play_game():
    item = []

    clear()
    generate_theme(item)
    intro(item)
    choice(item)


play_game()
