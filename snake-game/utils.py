import pygame


def scale_and_load_image(file_url, scale_x, scale_y):
  pic = pygame.image.load(file_url)
  pic = pygame.transform.scale(pic, (scale_x, scale_y))
  return pic.convert_alpha()
