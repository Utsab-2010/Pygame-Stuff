import pygame
import random

class object(pygame.sprite.Sprite):
    def __init__(self,size,pos,speed):
        super().__init__()
        self.x=pos.x
        self.y=pos.y
        self.size=size
        self.image=pygame.Surface(self.size)
        self.image.fill((0,0,0))
        self.rect=self.image.get_rect(center=(self.x,self.y))
        self.speed=speed

    def update(self,speed):
        self.speed=speed
        self.x -= self.speed
        self.rect.center = (self.x,self.y)


def object_func(group,width,height,speed):
    copy=group.sprites().copy()
    for item in copy:
        if item.x+item.size[0]//2 <=0:
            group.remove(item)
    if len(group.sprites())<3:

        rx=random.randint(width,2*width)
        ry=height-80
        group.add(object((80,60),pygame.Vector2(rx,ry),speed))



        