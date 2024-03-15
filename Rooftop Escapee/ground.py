import pygame


class Ground(pygame.sprite.Sprite):
    def __init__(self,size,pos):
        super().__init__()
        self.x=pos.x
        self.y=pos.y
        self.size=size
        self.image=pygame.Surface(self.size)
        self.image.fill((58,41,55))
        self.rect=self.image.get_rect(topleft=(self.x,self.y))
        

    def update(self,speed):
        pass