import pygame

class Score:
  def __init__(self) -> None:
    self.val=0
    self.font = pygame.font.Font(None,25)
  def increase(self):
    self.val+=1
  
  def update(self,screen):
    score_surface = self.font.render('Score:'+str(self.val),True,(255,255,255))
    screen.blit(score_surface,(10,10))