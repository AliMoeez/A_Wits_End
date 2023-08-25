import pygame,sys,json
from pytmx.util_pygame import load_pygame

pygame.init()

SCREEN_WIDTH=1100 ; SCREEN_HEIGHT=700 ; SCREEN=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

run=True
camera_x_y=[0,0]

#data=load_pygame(r"A_Wit's_End\Level 3_Tileset\test.tmx")

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

level_3_tile_set_part_2=load_pygame(r"A_Wit's_End\Level 4_Tileset\tile_set_level_4_test.tmx")
#level_3_tile_set_part_2=load_pygame(r"A_Wit's_End\Level 3_Tileset\test.tmx")

level_3_tile_set_part_2_rect=[]

rect_x=200
rect_y=200

rects=pygame.Rect(rect_x,rect_y,45,65)

rects_x_move=[0]
rects_y_move=[2]

while run:
    level_3_tile_set_part_2_rect=[]
    SCREEN.fill((0,0,0))

    key=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    for layer in level_3_tile_set_part_2:
       if layer.name=="Tile Layer 1":
            for tile in layer.tiles():
                x_val=tile[0]*16
                y_val=tile[1]*16
                SCREEN.blit(tile[2],(x_val-camera_x_y[0],y_val-camera_x_y[1]))
                level_3_tile_set_part_2_rect.append(pygame.Rect((x_val-camera_x_y[0],y_val-camera_x_y[1],16,16)))
       if layer.name=="Tile Layer 2":
            for tile in layer.tiles():
                x_val=tile[0]*16
                y_val=tile[1]*16
                SCREEN.blit(tile[2],(x_val-camera_x_y[0],y_val-camera_x_y[1]))
       if layer.name=="Tile Layer 3":
            for tile in layer.tiles():
                x_val=tile[0]*16
                y_val=tile[1]*16
                SCREEN.blit(tile[2],(x_val-camera_x_y[0],y_val-camera_x_y[1]))

    pygame.draw.rect(SCREEN,(200,100,100),rects)

    camera_x_y[0]+=rects.x-camera_x_y[0]-210

    if key[pygame.K_d]:
        rects_x_move[0]=4
    elif key[pygame.K_a]:
        rects_x_move[0]=-4
    else:
        rects_x_move[0]=0

    rects_y_move[0]=2

    if key[pygame.K_SPACE]:
        rects_y_move[0]=-4
    else:
        rects_y_move[0]=4
    
    def collision_with_object(level_3_tile_set_part_2_rect):
        tile_hit=[]
        for tiles in level_3_tile_set_part_2_rect:
            if rects.colliderect(tiles):
                tile_hit.append(tiles)
        return tile_hit

    def collision_with_object_logic(level_3_tile_set_part_2_rect):
            rects.x+=rects_x_move[0]
            collision=collision_with_object(level_3_tile_set_part_2_rect)
            for tile in collision:
                if rects_x_move[0]>0:
                    rects.right=tile.left
                elif rects_x_move[0]<0:
                    rects.left=tile.right
            rects.y+=rects_y_move[0]
            collision=collision_with_object(level_3_tile_set_part_2_rect)
            for tile in collision:
                if rects_y_move[0]>0:
                    rects.bottom=tile.top
                elif rects_y_move[0]<0:
                    rects.top=tile.bottom
            return rects
    

    collision_with_object(level_3_tile_set_part_2_rect)
    collision_with_object_logic(level_3_tile_set_part_2_rect)

    pygame.display.update()
            