from tkinter import *
import random 

# ==== Constants ====
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100			# time that frame refresh, the smaller the faster
SPACE_SIZE = 50		# grid size
BODY_PARTS = 3		# body length begin with 3
SNAKE_COLOR = '#00DD00'
BG_COLOR = '#000000'
FOOD_COLOR = '#FF3300'

# ==== Define Structure ====
class Snake:
	def __init__(self):
		self.body_size = BODY_PARTS
		self.coordinates = []
		self.squares = []

		for i in range(0, BODY_PARTS):
			# store every coords. of body part
			self.coordinates.append([0, 0])

		for x, y in self.coordinates:
			# a list of rectangles that have different coords.
			square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, tags='snake')
			self.squares.append(square)

class Food:
	def __init__(self):
		# initial coord. of food (x, y)
		x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
		y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

		self.coordinate = [x, y]

		canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags='food')

def next_turn(snake, food):
	x, y = snake.coordinates[0]	# the head coord. of snake
	if direction == 'up':
		y -= SPACE_SIZE
	elif direction == 'down':
		y += SPACE_SIZE
	elif direction == 'left':
		x -= SPACE_SIZE
	elif direction == 'right':
		x += SPACE_SIZE

	snake.coordinates.insert(0, (x, y))	# overwrite head coord.

	square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

	snake.squares.insert(0, square)

	if x == food.coordinate[0] and y == food.coordinate[1]:
		global score 

		score += 1

		label.config(text="Score:{}".format(score))

		# delete food by its tag
		canvas.delete('food')
		food = Food()

	else:
		# only delete last coord. if not eating food
		# because eating food extend one body length
		del snake.coordinates[-1]
		canvas.delete(snake.squares[-1])
		del snake.squares[-1]

	if check_collision(snake):
		game_over()

	else:
		# keep update out of main thread using after(), so frame keep update
		window.after(SPEED, next_turn, snake, food)	
		# print(f'x:{snake.coordinates[0][0]}, y:{snake.coordinates[0][1]}')



def change_direction(new_direction):
	global direction

	if new_direction == 'left' and direction != 'right':
		direction = new_direction
	elif new_direction == 'right' and direction != 'left':
		direction = new_direction
	elif new_direction == 'up' and direction != 'down':
		direction = new_direction
	elif new_direction == 'down' and direction != 'up':
		direction = new_direction

def check_collision(snake):
	x, y = snake.coordinates[0]

	if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
		print("Game Over")
		return True

	for body_coord in snake.coordinates[1:]:
		# check if every body's coords. collide in head
		if body_coord[0] == x and body_coord[1] == y:
			print("Game Over")
			return True

	return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70), text="GAME OVER", fill='#FFFFFF')


# ==== Main Loop ====
window = Tk()
window.title("Snake Game | Python TKinter")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 48))
label.pack()

canvas = Canvas(window, bg=BG_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

# ---- Create window at the center of your screen ----
window_width = window.winfo_width()			# width of tkinter frame
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()	# width of your computer screen
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f'{window_width}x{window_height}+{x}+{y}')

window.bind('<Left>', lambda e: change_direction('left'))
window.bind('<Right>', lambda e: change_direction('right'))
window.bind('<Up>', lambda e: change_direction('up'))
window.bind('<Down>', lambda e: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()