class Player(Game):
    def __init__(self,player_x_movement,player_y_movement,player_rect,player_current_health):
        self.player_x_movement=player_x_movement ; self.player_y_movement=player_y_movement ; self.player_current_health=player_current_health
        self.player_rect=player_rect
        super().__init__(level_1_bg,tile_level_1,camera_x_y,tile_level_1_rect,tile_level_2,tile_level_2_rect)
    
    def movement(self,player_idle,player_idle_flip,player_run,player_run_flip,player_jump,player_jump_flip):
        global level_1,jump,jump_condition,player_idle_right,player_idle_left,attack,crouch,dialogue_move_condition,player_death,level_2
        self.player_idle=player_idle ; self.player_idle_flip=player_idle_flip ; self.player_idle_number=player_idle_number ; self.player_jump=player_jump
        self.player_run_number=player_run_number; self.player_run=player_run ; self.player_run_flip=player_run_flip ; self.player_jump_flip=player_jump_flip
        self.player_jump_number=player_jump_number ; self.player_jump_length=player_jump_length 
        if level_1 and not player_death or level_2 and not player_death:
            if key[pygame.K_SPACE] and not crouch:
                jump=True
                attack=False
                
            if jump and jump_condition and not attack and not dialogue_move_condition:
                self.player_y_movement[0]=+0
                if self.player_jump_length[0]>=-17:
                    self.player_y_movement[0]+=-7.50
                    self.player_jump_length[0]-=1
                else: 
                    self.player_jump_length[0]=0
                if player_idle_left: 
                    SCREEN.blit(self.player_jump_flip[int(self.player_jump_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y+5)) 
                else: 
                    SCREEN.blit(self.player_jump[int(self.player_jump_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y+5)) 

                self.player_jump_number[0]+=0.85
                if self.player_jump_number[0]>9:
                    self.player_jump_number[0]=0 ; jump=False ; jump_condition=False

            if not jump and not attack and not crouch and not dialogue_move_condition:
                if key[pygame.K_d] and not key[pygame.K_a] :
                    self.player_x_movement[0]=20 #20
    
                    self.player_y_movement[0]=+45
                    SCREEN.blit(self.player_run[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y+5)) ; self.player_run_number[0]+=1
                    if self.player_run_number[0]>10: 
                        self.player_run_number[0]=0
                    player_idle_right=True ; player_idle_left=False
                elif key[pygame.K_a] and not key[pygame.K_d]:
                    self.player_x_movement[0]=-20
                    self.player_y_movement[0]=+45
                    SCREEN.blit(self.player_run_flip[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y+5)) ; self.player_run_number[0]+=1
                    if self.player_run_number[0]>10: 
                        self.player_run_number[0]=0
                    player_idle_left=True ; player_idle_right=False
                else:
                    self.player_x_movement[0]=0
                    self.player_y_movement[0]=+10
                    if player_idle_right:
                        SCREEN.blit(self.player_idle[int(self.player_idle_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y+5)) ; self.player_idle_number[0]+=0.45
                    if player_idle_left:
                        SCREEN.blit(self.player_idle_flip[int(self.player_idle_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y+5)) ; self.player_idle_number[0]+=0.45                        
                    if self.player_idle_number[0]>9: self.player_idle_number[0]=0
                        
                if key[pygame.K_d] and key[pygame.K_a]:
                    self.player_x_movement[0]=0
                    if player_idle_right:
                        SCREEN.blit(self.player_idle[int(self.player_idle_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y+5)) ; self.player_idle_number[0]+=0.45
                    if player_idle_left:
                        SCREEN.blit(self.player_idle_flip[int(self.player_idle_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y+5)) ; self.player_idle_number[0]+=0.45          
                    if self.player_idle_number[0]>9: self.player_idle_number[0]=0
              #  self.player_y_movement[0]=+10
            if jump and not jump_condition and not attack:
                SCREEN.blit(self.player_jump[int(self.player_jump_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y+5)) 
                self.player_jump_number[0]+=0.5
                if self.player_jump_number[0]>9:
                    self.player_jump_number[0]=0
        if dialogue_move_condition:
            self.player_x_movement[0]=0
            if player_idle_right:
                SCREEN.blit(self.player_idle[int(self.player_idle_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y+5)) ; self.player_idle_number[0]+=0.45
            if player_idle_left:
                SCREEN.blit(self.player_idle_flip[int(self.player_idle_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y+5)) ; self.player_idle_number[0]+=0.45                        
            if self.player_idle_number[0]>9: self.player_idle_number[0]=0           
                 
    def attack(self,player_attack_type_1,player_attack_type_1_flip,player_attack_type_2,player_attack_type_2_flip,
              player_attack_type_3,player_attack_type_3_flip,player_attack_type_4,player_attack_type_4_flip,attack_jump,attack_jump_flip):
        self.player_attack_type_1=player_attack_type_1 ; self.player_attack_type_1_flip=player_attack_type_1_flip ; self.player_attack_type_2=player_attack_type_2 
        self.player_attack_type_2_flip=player_attack_type_2_flip ; self.player_attack_type_3=player_attack_type_3 ; self.player_attack_type_3_flip=player_attack_type_3_flip
        self.player_attack_type_4=player_attack_type_4 ; self.player_attack_type_4_flip=player_attack_type_4_flip ; self.attack_type=attack_type ; self.player_attack_number=player_attack_number
        self.attack_jump=attack_jump ; self.attack_jump_flip=attack_jump_flip ; self.player_attack_jump_number=player_attack_jump_number
        global attack,jump,jump_condition,player_idle_right,player_idle_left,attack_air, player_death,dialogue_move_condition, attack_done
        if (level_1 or level_2_part_2) and not player_death and not dialogue_move_condition:
            if key[pygame.K_e]:
                attack=True ; jump=False
            if attack and jump_condition and not attack_air:            
                if self.attack_type[0]==4:
                    if player_idle_right: SCREEN.blit(self.player_attack_type_1[int(self.player_attack_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y-self.camera_x_y[1]))
                    else: SCREEN.blit(self.player_attack_type_1_flip[int(self.player_attack_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y-self.camera_x_y[1]))
                    self.player_attack_number[0]+=1
                if self.attack_type[0]==3:
                    if player_idle_right: SCREEN.blit(self.player_attack_type_2[int(self.player_attack_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y-self.camera_x_y[1]))
                    else: SCREEN.blit(self.player_attack_type_2_flip[int(self.player_attack_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y-self.camera_x_y[1]))
                    self.player_attack_number[0]+=1 
                if self.attack_type[0]==2:
                    if player_idle_right: SCREEN.blit(self.player_attack_type_3[int(self.player_attack_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y-self.camera_x_y[1]))
                    else: SCREEN.blit(self.player_attack_type_3_flip[int(self.player_attack_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y-self.camera_x_y[1]))
                    self.player_attack_number[0]+=1
                if self.attack_type[0]==1:
                    if player_idle_right: SCREEN.blit(self.player_attack_type_4[int(self.player_attack_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y-self.camera_x_y[1]))
                    else: SCREEN.blit(self.player_attack_type_4_flip[int(self.player_attack_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y-self.camera_x_y[1]))
                    self.player_attack_number[0]+=2
                if self.player_attack_number[0]>5:
                    self.player_attack_number[0]=0 ; self.attack_type[0]-=1 ; attack=False ; attack_done=True
                if self.attack_type[0]<=0: self.attack_type[0]=4
        if attack and not jump_condition:
            attack_air=True ; jump=False
        if attack_air:
            if player_idle_right:
                SCREEN.blit(self.attack_jump[int(self.player_attack_jump_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y-self.camera_x_y[1])) ; self.player_attack_jump_number[0]+=1
            else:
                SCREEN.blit(self.attack_jump_flip[int(self.player_attack_jump_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y-self.camera_x_y[1])) ; self.player_attack_jump_number[0]+=1
            if self.player_attack_jump_number[0]>8:
                self.player_attack_jump_number[0]=0 ; attack_air=False ; attack=False
                
    def defeat(self):
        global player_death,player_idle_right,player_idle_left,player_death_final, level_screen, level_1,reset_enemy_position,level_1_enemy_fight_condition
        global level_1_dialogue_part_two, end_level_1_dialogue,level_one_dialogue_part_three,end_level_1_dialogue,dialogue_move_condition, level_2_part_2
        self.player_fallen=player_fallen ; self.player_fallen_flip=player_fallen_flip ; self.player_fallen_number=player_fallen_number ; self.defeat_blur=defeat_blur
        if level_1 or level_2_part_2:
            if self.player_current_health[0]<=0:
                player_death=True # ; level_1_enemy_fight_condition=False
                if player_death:
                    self.player_x_movement[0]=0
                    if player_idle_right and not player_death_final: SCREEN.blit(self.player_fallen[int(self.player_fallen_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y-self.camera_x_y[1]))
                    if player_idle_left and not player_death_final: SCREEN.blit(self.player_fallen_flip[int(self.player_fallen_number[0]//2)],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y-self.camera_x_y[1]))
                    self.player_fallen_number[0]+=0.45
                    if self.player_fallen_number[0]>5:
                        player_death_final=True ; self.player_fallen_number[0]=6
                        if player_idle_right: SCREEN.blit(self.player_fallen[int(self.player_fallen_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y-self.camera_x_y[1]+45))
                        if player_idle_left: SCREEN.blit(self.player_fallen_flip[int(self.player_fallen_number[0]//2)],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y-self.camera_x_y[1]+45))
                    self.defeat_blur[0]+=5
                    rectangle_blur=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT)) ; rectangle_blur.set_alpha(self.defeat_blur[0]) ; rectangle_blur.fill((0,0,0))  ; SCREEN.blit(rectangle_blur,(0,0))
                    if self.defeat_blur[0]>200:
                        self.defeat_blur[0]=200
                font_game=pygame.font.SysFont("Impact",48) ; show_font_defeat=font_game.render("GAME OVER",1,(255,70,71))  ; show_font_defeat_rect=show_font_defeat.get_rect(center=(SCREEN_WIDTH/2,200))  ; SCREEN.blit(show_font_defeat,show_font_defeat_rect)           
                rectangle_retry=pygame.Surface((100,30)) ; rectangle_retry.set_alpha(0)  ; rectangle_retry.fill((200,200,200)) ; rectangle_retry=SCREEN.blit(rectangle_retry,(SCREEN_WIDTH/2-150,387))
                font_game=pygame.font.SysFont("Impact",30) ; show_font_defeat=font_game.render("RETRY",1,(255,70,71)) ; show_font_defeat_rect=show_font_defeat.get_rect(center=(SCREEN_WIDTH/2-100,400))  ; SCREEN.blit(show_font_defeat,show_font_defeat_rect)
                rectangle_main_menu=pygame.Surface((150,30))  ; rectangle_main_menu.set_alpha(0) ; rectangle_main_menu.fill((200,200,200))  ; rectangle_main_menu=SCREEN.blit(rectangle_main_menu,(SCREEN_WIDTH/2+25,387))
                font_game=pygame.font.SysFont("Impact",30) ; show_font_defeat=font_game.render("MAIN MENU",1,(255,70,71)) ; show_font_defeat_rect=show_font_defeat.get_rect(center=(SCREEN_WIDTH/2+100,400)) ; SCREEN.blit(show_font_defeat,show_font_defeat_rect)
                level_1_dialogue_part_two=False ; end_level_1_dialogue=False ; level_one_dialogue_part_three=False ; end_level_1_dialogue=False
                dialogue_move_condition=False
                if pygame.Rect.collidepoint(rectangle_retry,pygame.mouse.get_pos()) and event.type==pygame.MOUSEBUTTONDOWN:
                    self.player_current_health[0]=1000 ; player_death=False ; reset_enemy_position=True 
                    level_1_enemy_fight_condition=False
                    
                if pygame.Rect.collidepoint(rectangle_main_menu,pygame.mouse.get_pos()) and event.type==pygame.MOUSEBUTTONDOWN:
                    level_selection=False ; level_1=False ; level_screen=False ; self.player_current_health[0]=1000 ; player_death=False ; reset_enemy_position=True; 
                    level_1_enemy_fight_condition=False
                    
    def reset_position(self):
        global level_1, reset_enemy_position,level_one_x_border
        if level_1 and reset_enemy_position or level_2_part_2 and reset_enemy_position:
            level_one_x_border=False
            if level_1 and reset_enemy_position:
                self.player_rect.x=100
            if level_2 and reset_enemy_position:
                self.player_rect.x=210
                self.player_rect.y=500
            if level_2_part_2 and reset_enemy_position:
                self.player_rect.x=210
                self.player_rect.y=500

    def collision_with_object(self,tile_level_1_rect,tile_level_2_rect):
        global level_2_part_2
        if level_1:
            tile_level=self.tile_level_1_rect
        if level_2_part_2:
            tile_level=self.tile_level_2_rect
        if level_1 or level_2_part_2:
            tile_hit=[]
            for tiles in tile_level:
                if self.player_rect.colliderect(tiles):
                    tile_hit.append(tiles)
            return tile_hit
        
    def collision_with_object_logic(self,tile_level_1_rect,tile_level_2_rect):
        global jump_condition,level_2_part_2
        if level_1 or level_2_part_2:
            self.player_rect.x+=self.player_x_movement[0]
            collision=Player.collision_with_object(self,tile_level_1_rect,tile_level_2_rect)
            for tile in collision:
                if self.player_x_movement[0]>0:
                    self.player_rect.right=tile.left
                if self.player_x_movement[0]<0:
                    self.player_rect.left=tile.right
            self.player_rect.y+=self.player_y_movement[0]
            collision=Player.collision_with_object(self,tile_level_1_rect,tile_level_2_rect)
            for tile in collision:
                if self.player_y_movement[0]>0:
                    self.player_rect.bottom=tile.top
                    jump_condition=True
                if self.player_y_movement[0]<0:
                    self.player_rect.top=tile.bottom
            return self.player_rect 