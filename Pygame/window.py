import pygame, sys
from pygame.locals import *

pygame.init() # initialize game

pygame.display.set_caption("Hello Pygame")  # set title of window
frame = pygame.time.Clock() # set frame frequency of window (FPS)

# load assets
# player_image = pygame.image.load('')
# player_location = [50, 50]

# key settings
move_left = False
move_right = False

# initialize window
WINDOW_SIZE = (400, 400)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

# every game runs in loop, so add a game loop
while True:
    
    # screen.blit(player_image, player_location)

    # if move_right == True:
    #   player_location += 4
    # if move_left == True:
    #   player_location -= 4

    for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        if event.type == KEYDOWN:
          if event.key == K_LEFT:
            move_left = True
          if event.key == K_RIGHT:
            move_right = True
        if event.type == KEYUP:
          if event.key == K_LEFT:
            move_left = False
          if event.key == K_RIGHT:
            move_right = False
          

    pygame.display.update() # update screen so screen move
    frame.tick(60)  #frame rate=60