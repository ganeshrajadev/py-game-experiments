from pygame.math import Vector2
from utils import scale_and_load_image
import pygame
import random

cell_size = 20
cell_count = 20


class Fruit:
  def __init__(self) -> None:
    self.update_pos()
    self.apple = scale_and_load_image('./Graphics/apple.png',cell_size,cell_size)
  
  def draw_fruit(self, screen):
    fruit_rect = pygame.Rect(
        self.pos.x*cell_size, self.pos.y*cell_size, cell_size, cell_size)
    screen.blit(self.apple,fruit_rect)
  
  def update_pos(self):
    self.x = random.randint(0,cell_count-1)
    self.y = random.randint(0,cell_count-1)
    self.pos = Vector2(self.x, self.y)