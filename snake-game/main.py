import pygame
from pygame.math import Vector2
import sys


from fruit import Fruit
from snake import Snake
from constants import cell_size,cell_count,WIDTH,HEIGHT,UP,DOWN,LEFT,RIGHT
from game_board import Board
pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

board_obj = Board(screen=screen)


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == SCREEN_UPDATE:
      board_obj.update()
    if event.type == pygame.KEYDOWN:
      key=event.key
      if key == pygame.K_UP and board_obj.snake.current_direction!= DOWN:
        board_obj.snake.current_direction = UP
      elif key== pygame.K_DOWN and board_obj.snake.current_direction!= UP:
        board_obj.snake.current_direction = DOWN
      elif key==pygame.K_LEFT and board_obj.snake.current_direction!= RIGHT:
        board_obj.snake.current_direction = LEFT
      elif key==pygame.K_RIGHT and board_obj.snake.current_direction!= LEFT:
        board_obj.snake.current_direction = RIGHT
  screen.fill((0,0,0))
  board_obj.draw_elements()
  pygame.display.update()
  clock.tick(60)