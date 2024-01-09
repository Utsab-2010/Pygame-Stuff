import pygame

pygame.init()
screen = pygame.display.set_mode((800, 300))
done = False
white=(255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
fonts = pygame.font.get_fonts()
bg = (127,127,127) 

count = 0

print(fonts[count])


while not done:
    click = False
    for event in pygame.event.get():
      
      screen.fill(bg)
      if event.type == pygame.QUIT:
         done = True
      if event.type == pygame.MOUSEBUTTONDOWN:
         click=True

        
    font = pygame.font.SysFont(fonts[count] , 36)
    txtsurf = font.render(fonts[count]+ " xX SCORE Xx", True, white)
    screen.blit(txtsurf,(300 - txtsurf.get_width() // 2, 150 - txtsurf.get_height() // 2))
    
    if click== True: 
      
      count +=1
      print(fonts[count])
    pygame.display.update()

# fonts = pygame.font.get_fonts()
# for f in fonts:
#    print(f)