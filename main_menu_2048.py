import os, random, time
from simple_colors import *
from start_game_2048 import start_game
from movements_page_2048 import movements_page

def main_menu():

	os.system('cls')

	print("\n")
	welcome = "    MAIN MENU "
	print(green(welcome), end="")
	print("\n")

	print(" --- --- - - --- ")
	print("   - - - - - - - ")
	print(" --- - - --- --- ")
	print(" -   - -   - - - ")
	print(" --- ---   - --- \n")

	time.sleep(0.2)
	print(blue(" 's'") + " :" + yellow(" START GAME"))
	time.sleep(0.2)
	print(blue(" 'm'") + " :" + yellow(" MOVEMENTS"))
	time.sleep(0.2)
	print(blue(" 'e'") + " :" + yellow(" EXIT"))
	time.sleep(0.2)
	print("\n")

	while True:

		os.system('cls')

		print("\n")
		welcome = "    MAIN MENU "
		print(green(welcome), end="")
		print("\n")

		print(" --- --- - - --- ")
		print("   - - - - - - - ")
		print(" --- - - --- --- ")
		print(" -   - -   - - - ")
		print(" --- ---   - --- \n")

		print(blue(" 's'") + " :" + yellow(" START GAME"))
		print(blue(" 'm'") + " :" + yellow(" MOVEMENTS"))
		print(blue(" 'e'") + " :" + yellow(" EXIT"))
		print("\n")
		
		choice = input(": ")
		if choice == 's':
			print("Loading", end="")
			for i in range(10):
				r = random.randint(1, 4)
				time.sleep(float(r/50))
				print('.', end="")
			print("\n")
			time.sleep(0.2)

			start_game()
		
		elif choice == 'm':

			movements_page()

		elif choice == 'e':

			os.system('cls')

			return False

		else:

			continue

