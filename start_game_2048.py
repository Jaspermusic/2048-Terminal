import os, time
from simple_colors import *
import WConio2
from movements_2048 import print_box, choose_random_grid
from movements_2048 import box_move_up, box_move_down, box_move_left, box_move_right


def check_for_lose(box):
    
    for i in range(16 - 1):
        if not (i+1)%4 == 0:
            if box[i] == box[i+1]:
                return False
    for i in range(3):
        if box[i] == box[i+4] or box[i+4] == box[i+8] or box[i+8] == box[i+12]:
            return False
    return True

def box_filled(box):

    for i in range(16):
        if box[i] == 0:
            return False
    return True

def check_for_win(box, high_score):
 
    for i in box:
        if i > high_score:
            high_score = i
    return high_score



def start_game():
    
    os.system('cls')

    box = []
    high_score = 2

    for i in range(16):
        box.append(0)

    box[choose_random_grid(box)] = 2

    print_box(box)

    while True:

        choice = WConio2.getkey()

        os.system('cls')

        high_score = check_for_win(box, high_score)

        if high_score == 2048:

            os.system('cls')

            print(green("\n YOU WON \n"))
            print(blue(" Score: "), high_score, "\n")

            time.sleep(0.2)
            print("\x1B[3m" + " press 'enter' to play again" + "\x1B[0m\n" )
            time.sleep(0.2)

            press_enter = input(" : ")

            start_game()

        if check_for_lose(box):

            os.system('cls')

            print(red("\n YOU LOSE \n"))
            print(blue(" Score: "), high_score, "\n")

            time.sleep(0.2)
            print("\x1B[3m" + " press 'enter' to play again" + "\x1B[0m\n" )
            time.sleep(0.2)

            press_enter = input(" : ")

            start_game()
        
        if not box_filled(box) and choice in "wasd":

            box[choose_random_grid(box)] = 2


        if choice == 'w':

            box_move_up(box)

        elif choice == 'a':

            box_move_left(box)

        elif choice == 's':

            box_move_down(box)

        elif choice == 'd':

            box_move_right(box)

        elif choice == "q":

            return

        else:

            print_box(box)
            print("Invalid input.")
