import pygame

from pygame.math import Vector2
from constants import cell_size, UP, DOWN, LEFT, RIGHT
from utils import scale_and_load_image


class Snake:
  def __init__(self) -> None:
    self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
    self.current_direction = Vector2(1, 0)
    self.new_block = False
    self.head_up=scale_and_load_image(
        './Graphics/head_up.png', cell_size, cell_size)
    self.head_down = scale_and_load_image(
        './Graphics/head_down.png', cell_size, cell_size)
    self.head_left =scale_and_load_image(
        './Graphics/head_left.png', cell_size, cell_size)
    self.head_right = scale_and_load_image(
        './Graphics/head_right.png', cell_size, cell_size)
    self.tail_up = scale_and_load_image(
        './Graphics/tail_up.png', cell_size, cell_size)
    self.tail_down = scale_and_load_image(
        './Graphics/tail_down.png', cell_size, cell_size)
    self.tail_left = scale_and_load_image(
        './Graphics/tail_left.png', cell_size, cell_size)
    self.tail_right = scale_and_load_image(
        './Graphics/tail_right.png', cell_size, cell_size)
    self.body_vert = scale_and_load_image(
      './Graphics/body_vertical.png',cell_size,cell_size)
    self.body_hori = scale_and_load_image(
      './Graphics/body_horizontal.png',cell_size,cell_size)
    self.body_tl = scale_and_load_image(
      './Graphics/body_topleft.png',cell_size,cell_size)
    self.body_tr = scale_and_load_image(
      './Graphics/body_topright.png',cell_size,cell_size)
    self.body_bl = scale_and_load_image(
      './Graphics/body_bottomleft.png',cell_size,cell_size)
    self.body_br = scale_and_load_image(
      './Graphics/body_bottomright.png',cell_size,cell_size)
      
  def draw_snake(self, screen):
    n=len(self.body)
    for index, block in enumerate(self.body):
      x_pos = block.x*cell_size
      y_pos = block.y*cell_size
      block_react = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
      if index == 0:
        screen.blit(self.get_head_image(),block_react)
      elif index==n-1:
        screen.blit(self.get_tail_image(),block_react)
      else:
        prev = self.body[index-1] -block
        nex = self.body[index+1] - block
        if prev.x == nex.x:
          screen.blit(self.body_vert,block_react)
        elif prev.y == nex.y:
          screen.blit(self.body_hori,block_react)
        elif (prev.x,nex.y) in {(-1,-1)} or (nex.x,prev.y) in {(-1,-1)}:
          screen.blit(self.body_tl,block_react)
        elif (prev.x,nex.y) in {(-1,1)} or (nex.x,prev.y) in {(-1,1)}:
          screen.blit(self.body_bl,block_react)
        elif (prev.x,nex.y) in {(1,-1)} or (nex.x,prev.y) in {(1,-1)}:
          screen.blit(self.body_tr,block_react)
        elif (prev.x,nex.y) in {(1,1)} or (nex.x,prev.y) in {(1,1)}:
          screen.blit(self.body_br,block_react)

  def move_snake(self):
    body_copy = self.body[:-1]
    if self.new_block:
      body_copy = self.body[:]
      self.new_block = False
    new_pos = body_copy[0]+self.current_direction
    body_copy.insert(0, new_pos)
    self.body = body_copy[:]
  
  def get_head_image(self):
    head_relation = self.body[0] - self.body[1]
    if head_relation==UP: return self.head_up
    if head_relation==DOWN: return self.head_down
    if head_relation==LEFT: return self.head_left
    if head_relation==RIGHT: return self.head_right

  def get_tail_image(self):
    head_relation = self.body[-1] - self.body[-2]
    if head_relation==UP: return self.tail_up
    if head_relation==DOWN: return self.tail_down
    if head_relation==LEFT: return self.tail_left
    if head_relation==RIGHT: return self.tail_right

  def grow(self):
    self.new_block = True
