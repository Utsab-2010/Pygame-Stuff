import pygame
import random
import math

#initialise
HEIGHT= 600
WIDTH=800
pygame.init()

white=(255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

screen = pygame.display.set_mode((800,600))
#coutner font

font = pygame.font.SysFont("cambriamath", 30,bold=True)


#title and windowname
pygame.display.set_caption("Space Nibbas")
icon=pygame.image.load('spaceship.png').convert_alpha()
pygame.display.set_icon(icon)
backimg=pygame.image.load('bg3.jpg')
backimg=pygame.transform.smoothscale(backimg,(800,600))

#player
playerImg=pygame.image.load('spaceship.png').convert_alpha()
playerImg=pygame.transform.smoothscale(playerImg,(60,60))
player_pos = pygame.Vector2(400,500);    #intitial coordinates
dt=0
clock = pygame.time.Clock()

#player and objects
def player(img,x,y):
    screen.blit(img,(x,y))
running=True

class Object:
    def __init__(self,x,y,size) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.img = pygame.image.load('asteroid2.png').convert_alpha()
        self.img = pygame.transform.smoothscale(self.img,(size,size))
        screen.blit(self.img,(x,y))

    def display(self):
        screen.blit(self.img,(self.x,self.y))

count = 30
Objlist=[]

for i in range(count):
    rx=random.randint(1,800)
    ry=random.randint(-100,300)
    rs=random.randint(50,80)
    Objlist.append(Object(rx,ry,rs))
#cursor image
cursor_img=pygame.image.load('aim.png').convert_alpha()
cursor_img=pygame.transform.smoothscale(cursor_img,(30,30))


#laser
laser_list=[]
class laser:
    Img=pygame.image.load('beam2.png')
    Img=pygame.transform.smoothscale(Img,(20,20))
    
    def __init__(self,angle,x,y) -> None:
        self.x=x
        self.y=y
        self.angle=angle
        self.img= pygame.transform.rotate(laser.Img,angle-90)
        screen.blit(self.img,(x,y))
        # self.ox=x
        # self.oy=y

    def proceed(self,speed):
        self.x+=speed*math.cos(math.radians(self.angle))
        self.y-=speed*math.sin(math.radians(self.angle))
        screen.blit(self.img,(self.x,self.y))

pygame.mouse.set_visible(False)

laser_time=0
score=0
gameover=False
while running:
    # screen.fill((160,160,160))
    click= False

    screen.blit(backimg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click=True
            

    if gameover == True:
        font = pygame.font.SysFont("bookmanoldstyle",40,bold=True)
        gameover_text= font.render("GAME OVER", True, red)
        screen.blit(gameover_text,(WIDTH/2-gameover_text.get_width()/2,HEIGHT/2))
        screen.blit(txtsurf,(WIDTH/2-gameover_text.get_width()/2,HEIGHT/2 + gameover_text.get_height()+ 5))
        pygame.display.update()

        continue


    keys = pygame.key.get_pressed()
    # if player_pos.x >= 0 and player_pos.x <= 800 and player_pos.y >=0 and player_pos.y <=600 :
    # if keys[pygame.K_w]:
    #     player_pos.y -= 200 * dt
    # if keys[pygame.K_s]:
    #     player_pos.y += 200 * dt
    if keys[pygame.K_a] and player_pos.x>30:
        player_pos.x -= 250 * dt
    if keys[pygame.K_d] and player_pos.x<800-30:
        player_pos.x += 250 * dt

    mx,my = pygame.mouse.get_pos()

    #asteroid movement
    speed = 0.5 + score/50
    if speed>=5:
        speed = 5
    for i in range(len(Objlist)):
        Objlist[i].y+=speed
        Objlist[i].display()
        if Objlist[i].y>=620:
            rx=random.randint(1,800)
            ry=random.randint(-100,0)
            rs=random.randint(50,80)
            Objlist[i]=Object(rx,ry,rs)

    dx = mx-player_pos.x
    dy = -(my-player_pos.y)
    
    angle = math.degrees(math.atan2(dy,dx))

    # if keys[pygame.K_SPACE]:
    #     laser_list.append(laser(angle,player_pos.x,player_pos.y))
        
    
    # for event in pygame.event.get():
        
    #         laser_list.append(laser(angle,player_pos.x,player_pos.y))
    #     if event.type == pygame.MOUSEBUTTONUP:
    #         print('mouse up')
    if click== True:
        laser_list.append(laser(angle,player_pos.x-15,player_pos.y-15))
    try:
        laser_list2 = laser_list.copy()
        for item in laser_list2:
            item.proceed(10)
            if item.y in [-20,620] or item.x in [-20,820]:
                    laser_list.remove(item)
                    continue
            for ast in Objlist:
                    if math.sqrt((item.x - ast.x)**2 + (item.y - ast.y)**2 ) < ast.size*0.7 :
                        laser_list.remove(item)
                        Objlist.remove(ast)
                        score +=1    
                        rx=random.randint(1,800)
                        ry=random.randint(-100,0)
                        rs=random.randint(50,80) 
                        Objlist.append(Object(rx,ry,rs)) 
                    
    except ValueError:   
        pass
            
    for ast in Objlist:
    #spaceship coliision detection
        if math.sqrt((player_pos.x - ast.x)**2 + (player_pos.y - ast.y)**2 ) < 30 :
            gameover=True    
    
    #score printing
    txtsurf = font.render("SCORE: " + str(score), True, white)
    screen.blit(txtsurf,(10,550))

    player_model = pygame.transform.rotate(playerImg,angle-90)
    player_rect= player_model.get_rect(center=(player_pos.x,player_pos.y))

    dt= clock.tick(60) / 1000
    # player(player_model,player_pos.x,player_pos.y)
    screen.blit(cursor_img,(mx,my))
    screen.blit(player_model,player_rect)
    pygame.display.update()