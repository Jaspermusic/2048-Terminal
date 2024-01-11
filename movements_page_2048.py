import os, time
from simple_colors import *

def movements_page():

    os.system('cls')
    print("\n")

    time.sleep(0.2)
    print(green(" MOVEMENT KEYS: \n"))

    time.sleep(0.2)
    print(blue("  'w'  ") + " -> " + red("UP"))

    time.sleep(0.2)
    print(blue("  'a'  ") + " -> " + red("LEFT"))

    time.sleep(0.2)
    print(blue("  's'  ") + " -> " + red("DOWN"))

    time.sleep(0.2)
    print(blue("  'd'  ") + " -> " + red("RIGHT"))

    time.sleep(0.2)
    print(blue("  'q'  ") + " -> " + red("QUIT \n"))

    time.sleep(0.2)
    print("\x1B[3m" + "press 'enter' to homescreen" + "\x1B[0m\n" )

    time.sleep(0.2)

    press_enter = input(" : ")
