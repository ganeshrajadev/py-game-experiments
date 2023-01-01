import pygame
import sys

from snake import Snake
from fruit import Fruit
from score import Score

from constants import cell_count
class Board:
  def __init__(self,screen) -> None:
    self.snake=Snake()
    self.food=Fruit()
    self.score=Score()
    self.screen=screen
  
  def update(self):
    self.snake.move_snake()
    self.check_collision()

  def draw_elements(self):
    self.food.draw_fruit(screen=self.screen)
    self.snake.draw_snake(screen=self.screen)
    self.score.update(screen=self.screen)
  
  def check_collision(self):
    # snake captured food
    if self.food.pos == self.snake.body[0]:
      self.food.update_pos()
      self.snake.grow()
      self.score.increase()
    
    # Snake hit board end
    if not (0 <=self.snake.body[0].x < cell_count and 0 <=self.snake.body[0].y < cell_count) :
      self.game_over()
    
    #snake hits itself
    for block in self.snake.body[1:]:
      if block == self.snake.body[0]:
        print('hitself')
        self.game_over()
  
  def game_over(self):
    pygame.quit()
    sys.exit()