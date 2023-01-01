from pygame.math import Vector2

cell_size, cell_count = 20, 20

HEIGHT, WIDTH = cell_count*cell_size, cell_size*cell_count

UP = Vector2(0, -1)
DOWN = Vector2(0, 1)
LEFT = Vector2(-1, 0)
RIGHT = Vector2(1, 0)
