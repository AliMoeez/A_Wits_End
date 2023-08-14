import pygame,sys,json
from pytmx.util_pygame import load_pygame

pygame.init()

SCREEN_WIDTH=1100 ; SCREEN_HEIGHT=700 ; SCREEN=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

run=True
camera_x_y=[0,0]

data=load_pygame(r"A_Wit's_End\Level 3_Tileset\test.tmx")

test=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\tiles\top_tile_3.png")

bg_1=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\background1.png").convert_alpha()
bg_2=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\background2.png").convert_alpha()
bg_3=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\background3.png").convert_alpha()
bg_4=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\background4a.png").convert_alpha()
bg_5=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\background4b.png").convert_alpha()

bg_1=pygame.transform.scale(bg_1,(SCREEN_WIDTH,SCREEN_HEIGHT))
bg_2=pygame.transform.scale(bg_2,(SCREEN_WIDTH,SCREEN_HEIGHT))
bg_3=pygame.transform.scale(bg_3,(SCREEN_WIDTH,SCREEN_HEIGHT))
bg_4=pygame.transform.scale(bg_4,(SCREEN_WIDTH,SCREEN_HEIGHT))
bg_5=pygame.transform.scale(bg_5,(SCREEN_WIDTH,SCREEN_HEIGHT))


while run:
    SCREEN.fill((0,0,0))
    SCREEN.blit(bg_1,(0,0))
    SCREEN.blit(bg_2,(0,0))
    SCREEN.blit(bg_3,(0,0))
    SCREEN.blit(bg_4,(0,0))
    SCREEN.blit(bg_5,(0,0))
    key=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    for layer in data:
         for tile in layer.tiles():
              x_val=tile[0]*32
              y_val=tile[1]*32
              SCREEN.blit(tile[2],(x_val-camera_x_y[0],y_val))

    if key[pygame.K_d]:
        camera_x_y[0]+=20
    if key[pygame.K_a]:
         camera_x_y[0]-=20
    
    

    pygame.display.update()
            