import pygame

#initialise

pygame.init()

screen = pygame.display.set_mode((800,600))
#title and windowname
pygame.display.set_caption("Pygame test")
icon=pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
#player
playerImg=pygame.image.load('spaceship.png')
playerImg=pygame.transform.smoothscale(playerImg,(50,50))
player_pos = pygame.Vector2(400,300);
dt=0
clock = pygame.time.Clock()

def player(x,y):
    return screen.blit(playerImg,(x,y))
running=True

pygame.mouse.set_visible(False)
while running:
    screen.fill((160,160,160))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     player_pos.y -= 300 * dt
    # if keys[pygame.K_s]:
    #     player_pos.y += 300 * dt
    # if keys[pygame.K_a]:
    #     player_pos.x -= 300 * dt
    # if keys[pygame.K_d]:
    #     player_pos.x += 300 * dt

    player_pos.x,player_pos.y = pygame.mouse.get_pos()


    dt= clock.tick(60) / 1000
    player(player_pos.x,player_pos.y)
    pygame.display.update()
