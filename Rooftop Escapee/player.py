import pygame



class Player(pygame.sprite.Sprite):
    def __init__(self,pos,gravity,src=None):
        super().__init__()
        self.standard=pos
        self.x=pos.x
        self.y=pos.y
        self.surface=pygame.Surface((50,50))
        self.surface.fill((255,255,255))
        self.image=self.surface
        self.rect=self.image.get_rect(center=(self.x,self.y))
        self.speed=0
        self.gravity=gravity
        self.speedy=0
    
    def update(self,move,frame_rate,ground_collide,extra=None):

        if move=="jump":
            self.speedy+=self.gravity+2
            self.y-=self.speedy
        self.rect.center = (self.x,self.y)
        if not(extra):
            if not(ground_collide) and self.y<self.standard[1]:
                self.speedy-=self.gravity/frame_rate*2
                if self.speedy <-1*self.gravity*1.5:
                    self.speedy= -1*self.gravity
                self.y-=self.speedy
                
            elif ground_collide:
                self.speedy=0
                if self.y>=self.standard[1]:
                    self.y=self.standard[1]
            
        
        
            
