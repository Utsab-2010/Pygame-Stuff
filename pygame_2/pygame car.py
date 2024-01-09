import pygame 
import os 
import math

white=(255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

pygame.init()

screen = pygame.display.set_mode((800,600))
surface=pygame.Surface((100,100))

images = [pygame.image.load('car/' + img) for img in os.listdir('car')]
print(images)

def render_images(surf,images,rotation,spread,pos,size=60):
    spread *= size/100
    for i,img in enumerate(images):
        rotated_img= pygame.transform.scale(img,(size,size))
        rotated_img= pygame.transform.rotate(rotated_img,rotation)
        
        img_rect= rotated_img.get_rect(center=(pos[0],pos[1]-i*spread))

        #surf.blit(rotated_img,(pos[0]- img.get_width(),pos[1] - img.get_height()//2 - i*spread))
        surf.blit(rotated_img,img_rect)
running= True
rotation=90
px=400
py=300
acc=0.0005
ret= 0.001
fric= - 0.0003
speed=0
turn = 0.2
clock=pygame.time.Clock()
i=0
speedcap=1
pygame.mouse.set_visible(False)
while running:
    
    screen.fill(white)
    surface.fill(white)
    
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running=False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        if speed<0:
            speed-= -ret + fric
        speed+=acc + fric
        # px += speed*math.cos(math.radians(rotation+90))
        # py -= speed*math.sin(math.radians(rotation+90))
        # if keys[pygame.K_LEFT]:
        #     rotation += turn
        # if keys[pygame.K_RIGHT]:
        #     rotation -= turn

    elif  keys[pygame.K_DOWN]:
        if speed>0:
            speed+= -ret + fric
        speed-= acc + fric
        # px += speed*math.cos(math.radians(rotation+90))
        # py -= speed*math.sin(math.radians(rotation+90))
        # if keys[pygame.K_LEFT]:
        #     rotation += turn
        # if keys[pygame.K_RIGHT]:
        #     rotation -= turn
    elif speed > 0.01:
        speed += fric
    elif speed < -0.01:
        speed -= fric
    else:
        speed=0
    if speed!=0:
        if keys[pygame.K_LEFT]:
                rotation += turn
        if keys[pygame.K_RIGHT]:
            rotation -= turn
        
    if speed>speedcap:
        speed=speedcap
    if speed<-1*speedcap//200:
        speed= -1*speedcap//200
    px += speed*math.cos(math.radians(rotation+90))
    py -= speed*math.sin(math.radians(rotation+90))
    render_images(screen,images,rotation,2,(px,py),70)
    #wrotation+=0.1
    # screen.blit(surface,(400,300))
    pygame.display.update()