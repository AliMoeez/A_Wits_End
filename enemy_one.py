class EnemyOne(Player):
    #here
    def __init__(self,enemy_list_level_1,npc_walk_length,npc_direction_choice,enemy_1_distance_list,enemy_1_health_list):
        self.enemy_list_level_1=enemy_list_level_1 ;  self.npc_walk_length=npc_walk_length ; self.npc_direction_choice=npc_direction_choice ; self.enemy_1_distance_list=enemy_1_distance_list
        self.enemy_1_health_list=enemy_1_health_list
        super().__init__(player_x_movement,player_y_movement,player_rect,player_current_health)
    
    def move(self,enemy_1_level_1_rect,enemy_level_1_rect,enemy_1_level_1_rect_idle,enemy_1_x_movement,enemy_1_y_movement,enemy_1_level_2_rect):
        global level_1, level_1_enemy_fight_condition,x,y,off_x, level_2_part_2
        self.enemy_1_level_1_rect=enemy_1_level_1_rect ; self.enemy_1_walk=enemy_1_walk ; self.enemy_level_1_rect=enemy_level_1_rect ; self.enemy_1_level_1_rect_idle=enemy_1_level_1_rect_idle
        self.enemy_1_idle=enemy_1_idle ; self.enemy_1_walk_length=enemy_1_walk_length ; self.enemy_1_idle_length=enemy_1_idle_length ; self.enemy_1_idle_flip=enemy_1_idle_flip
        self.enemy_1_x_movement=enemy_1_x_movement ; self.enemy_1_y_movement=enemy_1_y_movement ; self.camera_x_y=camera_x_y ; self.enemy_1_walk_flip=enemy_1_walk_flip
        self.enemy_1_level_1_x=enemy_1_level_1_x ; self.enemy_type_1_level_1_x=enemy_type_1_level_1_x ; self.enemy_1_attack_length=enemy_1_attack_length
        self.enemy_one_fall_number=enemy_one_fall_number ; self.enemy_one_fall_direction_set=enemy_one_fall_direction_set ; self.enemy_1_level_2_rect=enemy_1_level_2_rect
        self.tile_level_2_rect=tile_level_2_rect ; self.enemy_list_level_2=enemy_list_level_2 ; self.level_2_tile_index=level_2_tile_index ; self.tile_level_2_rect=tile_level_2_rect
        
        if level_1 or level_2_part_2:
            if level_1: enemy_1_rect=self.enemy_level_1_rect
            if level_2_part_2 : enemy_1_rect=self.enemy_1_level_2_rect
            for idx,knight in enumerate(enemy_1_rect):
                player_enemy_1_distance=math.sqrt(math.pow(self.player_rect.x-knight.x,2)+math.pow(self.player_rect.y-knight.y,2))
                self.enemy_1_x_movement.append(0) ; self.enemy_1_attack_length.append(0) ; self.enemy_1_distance_list.append(player_enemy_1_distance)
                self.enemy_1_health_list.append(100) ; self.enemy_one_fall_number.append(0) ; self.enemy_one_fall_direction_set.append(0)    
                if self.enemy_1_x_movement[idx]>0:
                    self.enemy_one_fall_direction_set[idx]=1
                if self.enemy_1_x_movement[idx]<0:
                    self.enemy_one_fall_direction_set[idx]=2
                if len(self.enemy_1_distance_list)>len(enemy_1_rect):
                    del self.enemy_1_x_movement[-1], self.enemy_1_attack_length[-1] , self.enemy_1_distance_list[0], self.enemy_1_health_list[-1], self.enemy_one_fall_number[-1], self.enemy_one_fall_direction_set[-1]
                
        if level_1: 
            for idx,enemy_knight in enumerate(self.enemy_level_1_rect): self.enemy_list_level_1.append(pygame.Rect(enemy_knight.x,enemy_knight.y,45,55))
                
        if level_2_part_2:
            for idx,enemy_knight in enumerate(self.enemy_1_level_2_rect): self.enemy_list_level_2.append(pygame.Rect(enemy_knight.x,enemy_knight.y,45,55))
        
        
        if level_1 and not level_1_enemy_fight_condition or level_2_part_2:
            if level_1: enemy_1_rect=self.enemy_1_level_1_rect
            if level_2_part_2 : enemy_1_rect=self.enemy_1_level_2_rect

            self.enemy_1_y_movement[0]=2
            for idx,number in enumerate(enemy_1_rect):
                self.npc_walk_length.append(random.randint(200,400))
                self.npc_direction_choice.append(random.randint(1,2))
                if len(self.npc_walk_length)>len(enemy_1_rect):
                    del self.npc_walk_length[-1], self.npc_direction_choice[-1]
               

            for idx,enemy_knight in enumerate(enemy_1_rect): 
                if self.enemy_1_level_1_rect[idx].y>575:
                    self.enemy_1_level_1_rect[idx].y=575
                self.enemy_1_walk_length[0]+=0.20
                if self.enemy_1_walk_length[0]>10: self.enemy_1_walk_length[0]=0
                #for idx,length in enumerate(self.npc_walk_length): #############
                if level_1 or level_2_part_2 and self.enemy_1_distance_list[idx]>200:
                    if self.npc_direction_choice[idx]==1:
                            self.enemy_1_x_movement[idx]=3.95
                            SCREEN.blit(self.enemy_1_walk[int(self.enemy_1_walk_length[0])//2],(enemy_1_rect[idx].x-self.camera_x_y[0],enemy_knight.y-self.camera_x_y[1]+10)) 
                            self.npc_walk_length[idx]-=1.25
                    if self.npc_direction_choice[idx]==2:
                            self.enemy_1_x_movement[idx]=-2.95 
                            SCREEN.blit(self.enemy_1_walk_flip[int(self.enemy_1_walk_length[0])//2],(enemy_1_rect[idx].x-self.camera_x_y[0],enemy_knight.y-self.camera_x_y[1]+10)) #; self.npc_walk_length[idx]-=2
                    if self.npc_walk_length[idx]<=0:
                            self.npc_walk_length[idx]=random.randint(500,700) ; self.npc_direction_choice[idx]=random.randint(1,2)   
                        
        
            if level_1 and not level_1_enemy_fight_condition:
                for idx,enemy_knight in enumerate(self.enemy_1_level_1_rect_idle):
                    self.enemy_1_x_movement[idx+len(self.npc_walk_length)]=0
                    if self.player_rect.x>enemy_knight.x: SCREEN.blit(self.enemy_1_idle[int(self.enemy_1_idle_length[0]//2)],(enemy_knight.x-self.camera_x_y[0],enemy_knight.y-self.camera_x_y[1]+10))
                    else: SCREEN.blit(self.enemy_1_idle_flip[int(self.enemy_1_idle_length[0]//2)],(enemy_knight.x-self.camera_x_y[0],enemy_knight.y-self.camera_x_y[1]+10))
                    self.enemy_1_idle_length[0]+=0.15
                    if self.enemy_1_idle_length[0]>12: self.enemy_1_idle_length[0]=0
                    
             #   for idx,enemy_knight in enumerate(self.enemy_level_1_rect): self.enemy_list_level_1.append(pygame.Rect(enemy_knight.x,enemy_knight.y,45,55))
        
        if level_1 and level_1_enemy_fight_condition : 
            if level_1: enemy_1_rect=self.enemy_level_1_rect
            if level_2_part_2 : enemy_1_rect=self.enemy_1_level_2_rect
            for idx,knight in enumerate(enemy_1_rect):
                if self.enemy_1_distance_list[idx]>=50 and self.enemy_1_health_list[idx]>0:
                    self.enemy_1_walk_length[0]+=0.20
                    if self.enemy_1_walk_length[0]>10: self.enemy_1_walk_length[0]=0
                    if self.player_rect.x>=knight.x:
                        self.enemy_1_x_movement[idx]=4
                        SCREEN.blit(self.enemy_1_walk[int(self.enemy_1_walk_length[0])//2],(enemy_1_rect[idx].x-self.camera_x_y[0],knight.y-self.camera_x_y[1]+10)) 
                    if self.player_rect.x<knight.x:
                        self.enemy_1_x_movement[idx]=-4
                        SCREEN.blit(self.enemy_1_walk_flip[int(self.enemy_1_walk_length[0])//2],(enemy_1_rect[idx].x-self.camera_x_y[0],knight.y-self.camera_x_y[1]+10)) 
        
        for idx,knight in enumerate(self.enemy_1_level_2_rect):
            if level_2_part_2 and self.enemy_1_distance_list[idx]<=200 and self.enemy_1_distance_list[idx]>50 : 
                if level_2_part_2 : enemy_1_rect=self.enemy_1_level_2_rect
                if self.enemy_1_distance_list[idx]>=50 and self.enemy_1_health_list[idx]>0:
                    self.enemy_1_walk_length[0]+=0.20
                    if self.enemy_1_walk_length[0]>10: self.enemy_1_walk_length[0]=0
                    if self.player_rect.x>=knight.x:
                            self.enemy_1_x_movement[idx]=4
                            SCREEN.blit(self.enemy_1_walk[int(self.enemy_1_walk_length[0])//2],(enemy_1_rect[idx].x-self.camera_x_y[0],knight.y-self.camera_x_y[1]+10)) 
                    if self.player_rect.x<knight.x:
                            self.enemy_1_x_movement[idx]=-4
                            SCREEN.blit(self.enemy_1_walk_flip[int(self.enemy_1_walk_length[0])//2],(enemy_1_rect[idx].x-self.camera_x_y[0],knight.y-self.camera_x_y[1]+10)) 
    
    def player_interaction(self):
        global level_1 , level_1_enemy_fight_condition , enemy_1_friendly_dialogue,change_dialogue , dialogue_start_condition , end_dialogue ,change_dialogue_cond_1,dialogue_move_condition
        self.mouse_button_left_image=mouse_button_left_image ; self.enemy_one_icon=enemy_one_icon ; self.enemy_one_dialogue_list=enemy_one_dialogue_list ; self.player_icon=player_icon
        self.player_current_health=player_current_health
        if level_1 and not level_1_enemy_fight_condition and self.player_current_health[0]>0:
            for idx,enemy_knight in enumerate(self.enemy_1_level_1_rect_idle):
                player_enemy_distance=math.sqrt(math.pow(self.player_rect.x-enemy_knight.x,2)+math.pow(self.player_rect.y-enemy_knight.y,2))
                if player_enemy_distance<100 and enemy_1_friendly_dialogue is False:
                    SCREEN.blit(self.mouse_button_left_image,(enemy_knight.x-self.camera_x_y[0]+10,enemy_knight.y-self.camera_x_y[1]-50))
                    font_game=pygame.font.SysFont("Impact",20)  ; show_font=font_game.render("to interact",1,(255,70,71))  
                    SCREEN.blit(show_font,(enemy_knight.x-self.camera_x_y[0]+55,enemy_knight.y-self.camera_x_y[1]-40))
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        if event.button==1: dialogue_start_condition=True
                    if  event.type==pygame.MOUSEBUTTONUP and dialogue_start_condition is True: 
                        enemy_1_friendly_dialogue=True ; dialogue_move_condition=True
                if enemy_1_friendly_dialogue:
                    if player_enemy_distance<200:
                        if idx==0 or idx==1 or idx==2 or idx==3: 
                            rectangle_blur=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT)) ; rectangle_blur.set_alpha(100) ; rectangle_blur.fill((0,0,0))  ; SCREEN.blit(rectangle_blur,(0,0)) ; rectangle_box_1=pygame.Surface((SCREEN_WIDTH,200)) ; rectangle_box_1.fill((112,41,99))  ;  rectangle_box_1.set_alpha(75) ; SCREEN.blit(rectangle_box_1,(0,500))
                        if idx==0:
                            if self.enemy_one_dialogue_list[0]==0: 
                                SCREEN.blit(self.enemy_one_icon,(100,525)) ; font_game=pygame.font.SysFont("Impact",28)  ; show_font_knight=font_game.render("Knight",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(100,645)) ; font_game=pygame.font.SysFont("Impact",24)  ; show_font_knight=font_game.render("The great Kornos has been awaiting your arrival after your brave conquest!",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(200,545)) ; show_font_knight_1=font_game.render("He lies straight ahead.",1,(255,70,71)) ; SCREEN.blit(show_font_knight_1,(200,575))
                            if self.enemy_one_dialogue_list[0]==-1:
                                SCREEN.blit(self.player_icon,(100,525)) ; font_game=pygame.font.SysFont("Impact",28)  ; show_font_knight=font_game.render("You",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(125,645)) ; font_game=pygame.font.SysFont("Impact",24)  ; show_font_knight=font_game.render("Thank you! I will be sure to meet him...",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(200,545))
                            if self.enemy_one_dialogue_list[0]==-2: end_dialogue=True
                        if idx==1:
                            if self.enemy_one_dialogue_list[0]==0:
                                SCREEN.blit(self.enemy_one_icon,(100,525)) ; font_game=pygame.font.SysFont("Impact",28)  ; show_font_knight=font_game.render("Knight",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(100,645)) ; font_game=pygame.font.SysFont("Impact",24)  ; show_font_knight=font_game.render("Your great courage has saved our nation! A feast has been named in your honour!",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(200,545))
                            if self.enemy_one_dialogue_list[0]==-1: end_dialogue=True
                        if idx==2:
                            if self.enemy_one_dialogue_list[0]==0:
                                SCREEN.blit(self.enemy_one_icon,(100,525)) ; font_game=pygame.font.SysFont("Impact",28)  ; show_font_knight=font_game.render("Knight",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(100,645))  ; font_game=pygame.font.SysFont("Impact",24)   ; show_font_knight=font_game.render("Look at you, thinking you are worth something. You did nothing out of the ordinary!",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(200,545)) ; show_font_knight_1=font_game.render("Prove yourself in a duel with me.",1,(255,70,71)) ; SCREEN.blit(show_font_knight_1,(200,575))
                            if self.enemy_one_dialogue_list[0]==-1:
                                SCREEN.blit(self.player_icon,(100,525)) ; font_game=pygame.font.SysFont("Impact",28)  ; show_font_knight=font_game.render("You",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(125,645))  ; font_game=pygame.font.SysFont("Impact",24)  ; show_font_knight=font_game.render("I could care less for your duel. You have done nothing important yourself.",1,(255,70,71))  ; SCREEN.blit(show_font_knight,(200,545))
                            if self.enemy_one_dialogue_list[0]==-2:
                                SCREEN.blit(self.enemy_one_icon,(100,525)) ; font_game=pygame.font.SysFont("Impact",28)  ; show_font_knight=font_game.render("Knight",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(100,645))  ; font_game=pygame.font.SysFont("Impact",24)  ; show_font_knight=font_game.render("....",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(200,545))
                            if self.enemy_one_dialogue_list[0]==-3: end_dialogue=True       
                        if idx==3:
                            if self.enemy_one_dialogue_list[0]==0:
                                SCREEN.blit(self.enemy_one_icon,(100,525)) ; font_game=pygame.font.SysFont("Impact",28)  ; show_font_knight=font_game.render("Knight",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(100,645))  ; font_game=pygame.font.SysFont("Impact",24)   ; show_font_knight=font_game.render("Thank you! Your service has not gone unoted! Our men will now sleep in peace!!!",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(200,545))
                            if self.enemy_one_dialogue_list[0]==-1: end_dialogue=True
                        if event.type==pygame.MOUSEBUTTONDOWN:  change_dialogue_cond_1=True
                        if event.type==pygame.MOUSEBUTTONUP and change_dialogue_cond_1:
                            change_dialogue_cond_1=False ; change_dialogue=True  
                        if change_dialogue:
                            change_dialogue=False ; self.enemy_one_dialogue_list[0]-=1
                        if end_dialogue:
                            enemy_1_friendly_dialogue=False ; dialogue_start_condition=False ; self.enemy_one_dialogue_list[0]=0 ; end_dialogue=False ; dialogue_move_condition=False
                                    
    def attack(self):
        self.enemy_1_attack=enemy_1_attack ; self.enemy_1_attack_flip=enemy_1_attack_flip ; self.enemy_1_attack_length=enemy_1_attack_length 
        global level_1_enemy_fight_condition
        if level_1 and level_1_enemy_fight_condition or level_2_part_2: #here
            if level_1: enemy_1_rect=self.enemy_level_1_rect
            if level_2_part_2 : enemy_1_rect=self.enemy_1_level_2_rect
            for idx,knight in enumerate(enemy_1_rect):
                if  level_1 and self.enemy_1_distance_list[idx]<50 and self.enemy_1_health_list[idx]>0 or level_2_part_2 and self.enemy_1_distance_list[idx]<=50 and self.enemy_1_health_list[idx]>0:
                    self.enemy_1_x_movement[idx]=0
                    if self.player_rect.x>=enemy_1_rect[idx].x:
                        SCREEN.blit(self.enemy_1_attack[int(self.enemy_1_attack_length[idx])//2],(enemy_1_rect[idx].x-self.camera_x_y[0],enemy_1_rect[idx].y-self.camera_x_y[1]))
                    if self.player_rect.x<enemy_1_rect[idx].x:
                        SCREEN.blit(self.enemy_1_attack_flip[int(self.enemy_1_attack_length[idx])//2],(enemy_1_rect[idx].x-self.camera_x_y[0],enemy_1_rect[idx].y-self.camera_x_y[1]))
                    self.enemy_1_attack_length[idx]+=0.75
                    if self.enemy_1_attack_length[idx]>9:
                        self.enemy_1_attack_length[idx]=0
                        self.player_current_health[0]-=50#50
    
    def player_hit(self):
        global level_1, attack,level_1_enemy_fight_condition,attack_done, player_idle_right, player_idle_left,level_2_part_2
        if level_1 or level_2_part_2:
            if level_1: enemy_1_rect=self.enemy_level_1_rect
            if level_2_part_2 : enemy_1_rect=self.enemy_1_level_2_rect
            if attack_done and level_1_enemy_fight_condition:
                for idx,knight in enumerate(enemy_1_rect):
                    if self.enemy_1_distance_list[idx]<50:
                        if player_idle_right and self.player_rect.x<=enemy_1_rect[idx].x:
                            self.enemy_1_health_list[idx]-=100 #25
                        if player_idle_left and self.player_rect.x>enemy_1_rect[idx].x:
                            self.enemy_1_health_list[idx]-=100
                        attack_done=False
      
    def fall(self):
        global reset_enemy_position
        self.enemy_1_fall=enemy_1_fall ; self.enemy_1_fall_flip=enemy_1_fall_flip ; self.enemy_one_fall_number=enemy_one_fall_number
        if level_1 or level_2_part_2 and not reset_enemy_position:
            if level_1: enemy_1_rect=self.enemy_level_1_rect
            if level_2_part_2 : enemy_1_rect=self.enemy_1_level_2_rect
            for idx,knight in enumerate(enemy_1_rect):
                if self.enemy_1_health_list[idx]<=0:
                    self.enemy_1_health_list[idx]=0
                    if self.enemy_one_fall_direction_set[idx]==1:
                        if self.enemy_one_fall_number[idx]<16:
                            SCREEN.blit(self.enemy_1_fall[int(self.enemy_one_fall_number[idx])//2],(enemy_1_rect[idx].x-self.camera_x_y[0],knight.y-self.camera_x_y[1]+10))
                        else:
                            self.enemy_one_fall_number[idx]=16  
                            SCREEN.blit(self.enemy_1_fall[int(self.enemy_one_fall_number[idx])//2],(enemy_1_rect[idx].x-self.camera_x_y[0],knight.y-self.camera_x_y[1]+45))
                    if self.enemy_one_fall_direction_set[idx]==2:
                        if self.enemy_one_fall_number[idx]<16:
                            SCREEN.blit(self.enemy_1_fall_flip[int(self.enemy_one_fall_number[idx])//2],(enemy_1_rect[idx].x-self.camera_x_y[0],knight.y-self.camera_x_y[1]+10))
                        else:
                            self.enemy_one_fall_number[idx]=16  
                            SCREEN.blit(self.enemy_1_fall_flip[int(self.enemy_one_fall_number[idx])//2],(enemy_1_rect[idx].x-self.camera_x_y[0],knight.y-self.camera_x_y[1]+45))                           
                    self.enemy_one_fall_number[idx]+=0.50
    
    def reset_position(self):
        global reset_enemy_position,level_2_part_2,level_1
        self.enemy_1_level_1_x=enemy_1_level_1_x ; self.enemy_1_level_1_x_idle=enemy_1_level_1_x_idle ; self.enemy_1_level_2_x=enemy_1_level_2_x
        #here
        if reset_enemy_position:
            self.enemy_1_distance_list.clear() ; self.enemy_one_fall_number.clear() ; self.enemy_one_fall_direction_set.clear() ; self.enemy_1_x_movement.clear() ; self.enemy_1_attack_length.clear() ; self.enemy_1_health_list.clear()
            if level_1:
                print("here")
                for idx,knight in enumerate(self.enemy_1_level_1_rect):
                    self.enemy_1_level_1_rect[idx].x=self.enemy_1_level_1_x[idx]
                for idx,knight in enumerate(self.enemy_1_level_1_rect_idle):
                    self.enemy_1_level_1_rect_idle[idx].x=self.enemy_1_level_1_x_idle[idx]
                for idx,knight in enumerate(self.enemy_1_health_list):
                    self.enemy_1_health_list[idx]=100
            if level_2_part_2:
                for idx,knight in enumerate(self.enemy_1_level_2_rect):
                    self.enemy_1_level_2_rect[idx].x=self.enemy_1_level_2_x[idx]
                for idx,knight in enumerate(self.enemy_1_health_list):
                    self.enemy_1_health_list[idx]=100
                reset_enemy_position=False
                
    def collision_with_object(self,tile_level_1,tile_level_2):
        self.level_2_tile_index=level_2_tile_index ; self.npc_direction_choice=npc_direction_choice
        if level_1 or level_2_part_2:
            if level_1: enemy_1_rect=self.enemy_level_1_rect ; tile_level=self.tile_level_1_rect
            if level_2_part_2 : enemy_1_rect=self.enemy_1_level_2_rect ; tile_level=self.tile_level_2_rect
            hit_tile=[]
            for idx,enemy_knight in enumerate(enemy_1_rect):
                for tiles in tile_level:
                    if enemy_knight.colliderect(tiles):
                        hit_tile.append(tiles)
            if level_2_part_2:
                for idx,enemy_knight in enumerate(enemy_1_rect):
                    for index,number in enumerate(tile_level):
                        if enemy_knight.colliderect(number):
                            if self.level_2_tile_index[index]=="14":
          #                      print("this")
                                self.npc_direction_choice[idx]=1
                            if self.level_2_tile_index[index]=="17":
         #                       print("tihs is")
                                self.npc_direction_choice[idx]=2 
            return hit_tile
        
    def collision_with_object_logic(self,tile_level_1,tile_level_2):
        global level_1_enemy_fight_condition, level_2_part_2
        if level_1 or level_2_part_2:
            if level_1: enemy_1_rect=self.enemy_level_1_rect ; enemy_list=self.enemy_list_level_1
            if level_2_part_2 : enemy_1_rect=self.enemy_1_level_2_rect ; enemy_list=self.enemy_list_level_2
         #   if not level_1_enemy_fight_condition:
            for idx,enemy_knight in enumerate(enemy_1_rect):
                try:
                    enemy_knight.x+=self.enemy_1_x_movement[idx]
                except IndexError : pass
         #       for idx,enemy_knight in enumerate(enemy_1_rect):
          #          enemy_knight.x+=self.enemy_1_x_movement[idx]
            collision=EnemyOne.collision_with_object(self,tile_level_1,tile_level_2)
          #  for tile in collision:
          #      for idx,enemy_knight in enumerate(enemy_1_rect):
             #       if self.enemy_1_x_movement[0]>0:
             #           enemy_knight.right=tile.left
             #       if self.enemy_1_x_movement[0]<0:
             #           enemy_knight.left=tile.right
            for idx,enemy_knight in enumerate(enemy_1_rect):
                enemy_knight.y+=self.enemy_1_y_movement[0]
            collision=EnemyOne.collision_with_object(self,tile_level_1,tile_level_2)
            for tile in collision:
                for idx,enemy_knight in enumerate(enemy_1_rect):
                    if enemy_knight.colliderect(tile):
                        enemy_knight.bottom=tile.top
            return enemy_list     