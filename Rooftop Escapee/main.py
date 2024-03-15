import pygame
from window import get_bg,draw_bg
from Objects import object,object_func
from player import Player
from ground import Ground
from collision_detect import object_collide,ground_collide

white=(255,255,255)
red = (255,0,0)
bg_list=[]
get_bg(bg_list)

pygame.init()

WIDTH,HEIGHT=pygame.display.get_desktop_sizes()[0]
WIDTH=1200
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Rooftop Escape")
pygame.display.set_icon(pygame.image.load('icon.png').convert_alpha())

clock=pygame.time.Clock()

width=bg_list[0].get_width()
for i,img in enumerate(bg_list):
    img=img.convert_alpha()
    bg_list[i]=pygame.transform.smoothscale(img,(width,HEIGHT-50))

font = pygame.font.SysFont("cambriamath", 35,bold=True)

#game variables and constants
gravity=12
speed=3
scroll=0
running=True
frame_rate=60
gameover=False
score=0

#ground initialization
grounds=pygame.sprite.Group()
grounds.add(Ground((WIDTH,100),pygame.Vector2(0,HEIGHT-50)))


#object initialization
objects=pygame.sprite.Group()
objects.add(object((80,60),pygame.Vector2(WIDTH+100*3,HEIGHT-80),speed))
objects.add(object((80,60),pygame.Vector2(WIDTH+250*3,HEIGHT-80),speed))
objects.add(object((80,60),pygame.Vector2(WIDTH+400*3,HEIGHT-80),speed))

#player initialization
players=pygame.sprite.Group()
players.add(Player(pygame.Vector2(WIDTH//3-100,HEIGHT-75 +1 ),gravity))


#Game runner
while(running):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and ground_collide(players.sprites()[0],grounds):
                players.update("jump",frame_rate,None,True)

    if gameover:
        continue

    if object_collide(players.sprites()[0],objects):
        gameover=True
        font = pygame.font.SysFont("bookmanoldstyle",50,bold=True)
        gameover_text= font.render("GAME OVER", True, red)
        screen.blit(gameover_text,(WIDTH/2-gameover_text.get_width()/2,HEIGHT/2))
        screen.blit(txtsurf,(WIDTH/2-gameover_text.get_width()/2,HEIGHT/2 + gameover_text.get_height()+ 5))
        pygame.display.update()
        continue
    
    keys=pygame.key.get_pressed()

    scroll+=speed

    object_func(objects,WIDTH,HEIGHT,speed)
    for obj in objects.sprites():
        if obj.x<players.sprites()[0].x and obj.x>players.sprites()[0].x - speed :
            score+=1
            print(score)
    players.update(None,frame_rate,ground_collide(players.sprites()[0],grounds))
    objects.update(speed)
    
    draw_bg(bg_list,screen,scroll)
    objects.draw(screen)
    grounds.draw(screen)
    players.draw(screen)

    txtsurf = font.render("SCORE: " + str(score), True, white)
    screen.blit(txtsurf,(10,550))

    if speed<=14:
       speed+=0.1/frame_rate
    clock.tick(frame_rate)
    pygame.display.update()
