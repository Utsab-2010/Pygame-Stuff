import pygame

def ground_collide(sprite,group):
    if len(pygame.sprite.spritecollide(sprite,group,False))==1:
        return True
    else:
        return False

def object_collide(sprite,group):
    if len(pygame.sprite.spritecollide(sprite,group,False))>0:
           return True
    else:
         return False
