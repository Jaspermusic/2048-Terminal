# Movements a, w, s, d

import random

def print_box(box):
	for i in range(16):
		if i%4==0 and i!=0:
			print("\n")
		if box[i] == 0:
			print("-  ", end="")
		else:
			print(box[i], " ", end="")
		if i%4 != 3:
			print("| ", end="")
	print("\n\n")

def choose_random_grid(box):
	random_grid = random.randint(0,15)
	if box[random_grid] != 0:
		random_grid = choose_random_grid(box)
	return random_grid


def box_move_up(box):
	# Moves down empty grids
	for j in range(3):
		for i in range(16 - 4):
			if box[i] == 0:
				box[i] = box[i+4]
				box[i+4] = 0
	# Adds grids of same value
	for i in range(16 - 4):
		if box[i] == box[i+4]:
			box[i] = box[i] * 2
			box[i+4] = 0
	# Moves down empty grids
	for j in range(3):
		for i in range(16 - 4):
			if box[i] == 0:
				box[i] = box[i+4]
				box[i+4] = 0
	print_box(box)


def box_move_down(box):
	# Moves up empty grids
	for j in range(3):
		for i in range(4, 16):
			if box[i] == 0:
				box[i] = box[i-4]
				box[i-4] = 0
	# Adds grids of same value
	for i in range(15, 3, -1):
		if box[i] == box[i-4]:
			box[i] = box[i] * 2
			box[i-4] = 0
	# Moves up empty grids
	for j in range(3):
		for i in range(4, 16):
			if box[i] == 0:
				box[i] = box[i-4]
				box[i-4] = 0

	print_box(box)


def box_move_left(box):
	# Moves right empty grids
	for j in range(3):
		for i in range(0, 15):
			if (i+1)%4 != 0:
				if box[i] == 0:
					box[i] = box[i+1]
					box[i+1] = 0
	# Adds grids of same value
	for i in range(0, 15):
		if (i+1)%4 != 0:
			if box[i] == box[i+1]:
				box[i] = box[i] * 2
				box[i+1] = 0
	# Moves right empty grids
	for j in range(3):
		for i in range(0, 15):
			if (i+1)%4 != 0:
				if box[i] == 0:
					box[i] = box[i+1]
					box[i+1] = 0

	print_box(box)


def box_move_right(box):
	# Moves left empty grids
	for j in range(3):
		for i in range(0, 16):
			if i%4 != 0:
				if box[i] == 0:
					box[i] = box[i-1]
					box[i-1] = 0
	# Adds grids of same value
	for i in range(0, 15):
		if (i+1)%4 != 0:
			if box[i] == box[i+1]:
				box[i] = box[i] * 2
				box[i+1] = 0
	# Moves left empty grids
	for j in range(3):
		for i in range(0, 16):
			if i%4 != 0:
				if box[i] == 0:
					box[i] = box[i-1]
					box[i-1] = 0

	print_box(box)