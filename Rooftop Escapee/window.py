import pygame,os


def get_bg(bg_list):
    for img in os.listdir('background'):
        bg_list.append(pygame.image.load('background/' + img))

def draw_bg(bg_list,screen,scroll,offsets=[0,0,0,0]):
    
    width=bg_list[0].get_width() 
    speed=1
    for j,img in enumerate(bg_list):
        for x in range(2):
            pos=x*width - scroll*speed + offsets[j]
            if x==1 and pos<=0:
                offsets[j]+=width    

            screen.blit(img,(pos,0))

        speed+=0.2
