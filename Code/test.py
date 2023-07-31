import pygame,sys
from test_2 import func

run=True
FPS=30
run=True

SCREEN_WIDTH=1100 ; SCREEN_HEIGHT=700 ; SCREEN=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

clock=pygame.time.Clock()

test_list=[]

class RunGame:
    def __init__(self):
        func.x=SCREEN

        while run:
            tile_level_1_rect=[] ; tile_level_2_rect=[] ; level_2_bg_list=[] ; level_2_dec_list=[] ; level_2_item_list=[]
            key=pygame.key.get_pressed()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()


run_game=RunGame()