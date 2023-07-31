class Menu:
    def __init__(self,camera_x_y_bg):
        self.camera_x_y_bg=camera_x_y_bg
    
    def home(self,level_3_bg_1,level_3_bg_2):
        global level_screen, reset_enemy_position
        self.level_3_bg_1=level_3_bg_1 ; self.level_3_bg_2=level_3_bg_2 ; self.level_screen=level_screen ; self.camera_x_y=camera_x_y
        SCREEN.blit(self.level_3_bg_1,(self.camera_x_y_bg[0],self.camera_x_y_bg[1]))  ; SCREEN.blit(self.level_3_bg_2,(self.camera_x_y_bg[0],self.camera_x_y_bg[1]))
        if not level_1:
            if self.camera_x_y_bg[0]>=-10: self.camera_x_y_bg[0]-=1
            else:
                self.camera_x_y_bg[0]-=1
                SCREEN.blit(self.level_3_bg_1,(self.camera_x_y_bg[0]+1100,self.camera_x_y_bg[1])) ; SCREEN.blit(self.level_3_bg_2,(self.camera_x_y_bg[0]+1100,self.camera_x_y_bg[1]))
                if self.camera_x_y_bg[0]<=-1100: self.camera_x_y_bg[0]=0
        
        if not level_screen:
            font_game=pygame.font.SysFont("Impact",36)  ; show_game=font_game.render("A Wit's End ",1,(120,159,179))  ; SCREEN.blit(show_game,(SCREEN_WIDTH//2-75,100))
            rectangle_play=pygame.Surface((60,30))  ; rectangle_play.set_alpha(0)  ; rectangle_play.fill((200,200,200)) ; rect_play_show=SCREEN.blit(rectangle_play,(SCREEN_WIDTH//2-25,405))
            font_game=pygame.font.SysFont("Impact",36)  ; show_game=font_game.render("Play",1,(120,159,179))  ; SCREEN.blit(show_game,(SCREEN_WIDTH//2-25,400))

            if pygame.Rect.collidepoint(rect_play_show,pygame.mouse.get_pos()) and event.type==pygame.MOUSEBUTTONDOWN: level_screen=True

    def level_selection(self):
        self.camera_x_y=camera_x_y ; self.player_rect=player_rect
        global level_screen, level_1, level_2, level_3, level_4 ; 
        if level_screen:
            self.player_rect.x=0
            self.player_rect.y=585
            self.camera_x_y[0]=0
            if key[pygame.K_q]:
                level_screen=False
            rectangle_level_1=pygame.Surface((60,90))  
            """rectangle_level_1.set_alpha(0)""" ; rectangle_level_1.fill((200,200,200))  ; rectangle_level_1=SCREEN.blit(rectangle_level_1,(SCREEN_WIDTH//2-250,SCREEN_HEIGHT//2-50))
            rectangle_level_2=pygame.Surface((60,90))  
            """rectangle_level_1.set_alpha(0)""" ; rectangle_level_2.fill((100,100,100))  ; rectangle_level_2=SCREEN.blit(rectangle_level_2,(SCREEN_WIDTH//2-50,SCREEN_HEIGHT//2-50))           
            if pygame.Rect.collidepoint(rectangle_level_1,pygame.mouse.get_pos()) and event.type==pygame.MOUSEBUTTONDOWN:
                level_scren=False ; level_1=True ; level_2=False ; level_3=False ; level_4=False
            if pygame.Rect.collidepoint(rectangle_level_2,pygame.mouse.get_pos()) and event.type==pygame.MOUSEBUTTONDOWN:
                level_scren=False ; level_1=False ; level_2=True ; level_3=False ; level_4=False
        if level_1:
            level_screen=False
            if key[pygame.K_r]:
                level_1=False ; level_screen=True ; level_2=False ; reset_enemy_position=True
        if level_2:
            level_screen=False
            if key[pygame.K_r]:
                level_2=False ; level_screen=True ; level_1=False ; reset_enemy_position=True