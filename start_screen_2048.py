import time, random
from simple_colors import *
import os

def start_screen():

    os.system('cls')

    welcome = "Welcome to terminal based 2048 game... "
    print("\n")
    for i in welcome:
        r = random.randint(1, 5)
        time.sleep(float(r/100))
        print(green(i), end="")
    print("\n")


    time.sleep(0.2)
    print(" --- --- - - --- ")
    time.sleep(0.25)
    print("   - - - - - - - ")
    time.sleep(0.2)
    print(" --- - - --- --- ")
    time.sleep(0.25)
    print(" -   - -   - - - ")
    time.sleep(0.2)
    print(" --- ---   - --- \n")
	

    time.sleep(0.2)
    print("\x1B[3m" + "Designed by Demouse" + "\x1B[0m" + "\n")
    time.sleep(0.2)

    print("Loading", end="")
    for i in range(10):
        r = random.randint(1, 4)
        time.sleep(float(r/10))
        print('.', end="")
    print("\n")
    time.sleep(1)

    
