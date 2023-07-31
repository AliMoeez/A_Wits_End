class EnemyTwo(player.Player):
    def __init__(self,enemy_two_level_1_rect,enemy_two_x_movement,enemy_two_y_movement,enemy_two_rect_list,enemy_two_distance_list,enemy_two_health):
        self.enemy_two_level_1_rect=enemy_two_level_1_rect ; self.enemy_two_x_movement=enemy_two_x_movement ; self.enemy_two_y_movement=enemy_two_y_movement ; self.enemy_two_rect_list=enemy_two_rect_list
        self.enemy_two_distance_list=enemy_two_distance_list ; self.enemy_two_health=enemy_two_health
        super().__init__(player_x_movement,player_y_movement,player_rect,player_current_health)
    
    def movement(self):
        global level_1, level_1_enemy_fight_condition
        self.enemy_two_idle=enemy_two_idle ; self.enemy_two_idle_flip=enemy_two_idle_flip ; self.enemy_two_idle_number=enemy_two_idle_number ; self.enemy_two_run=enemy_two_run 
        self.enemy_two_run_flip=enemy_two_run_flip ; self.enemy_two_run_number=enemy_two_run_number ; self.enemy_two_level_1_x=enemy_two_level_1_x ; self.enemy_two_fall_number=enemy_two_fall_number
        self.enemy_two_fall_direction_set=enemy_two_fall_direction_set
        if level_1:
            for idx,enemy_knight in enumerate(self.enemy_two_level_1_rect):
                enemy_two_player_distance=math.sqrt(math.pow(self.player_rect.x-enemy_knight.x,2)+math.pow(self.player_rect.y-enemy_knight.y,2))
                self.enemy_two_distance_list.append(enemy_two_player_distance) ; self.enemy_two_rect_list.append(pygame.Rect(enemy_knight.x,enemy_knight.y,45,55)) 
                self.enemy_two_x_movement.append(0) ; self.enemy_two_health.append(100), self.enemy_two_fall_number.append(0) ; self.enemy_two_fall_direction_set.append(0)
                #150
                if self.enemy_two_x_movement[idx]>0:
                    self.enemy_two_fall_direction_set[idx]=1
                if self.enemy_two_x_movement[idx]<0:
                    self.enemy_two_fall_direction_set[idx]=2
                
                if len(self.enemy_two_distance_list)>2:
                    del self.enemy_two_x_movement[-1]
                    del self.enemy_two_distance_list[0]
                    del self.enemy_two_health[-1]
                    del self.enemy_two_fall_number[-1]
                    
                    del self.enemy_two_fall_direction_set[-1]
            
            if not level_1_enemy_fight_condition:
                for idx,enemy_knight in enumerate(self.enemy_two_level_1_rect):
                    self.enemy_two_x_movement[idx]=0
                    SCREEN.blit(self.enemy_two_idle_flip[int(self.enemy_two_idle_number[0]//2)],(enemy_knight.x-self.camera_x_y[0]-25,enemy_knight.y-self.camera_x_y[1]-25))
                    self.enemy_two_idle_number[0]+=0.10
                    if self.enemy_two_idle_number[0]>4:
                        self.enemy_two_idle_number[0]=0
            if level_1_enemy_fight_condition:
                for idx,enemy_knight in enumerate(self.enemy_two_level_1_rect):
                    if self.player_rect.x>=enemy_knight.x and self.enemy_two_distance_list[idx]>30 and self.enemy_two_health[idx]>0:
                        SCREEN.blit(self.enemy_two_run[int(self.enemy_two_run_number[0]//2)],(enemy_knight.x-self.camera_x_y[0]-25,enemy_knight.y-self.camera_x_y[1]-25))
                        self.enemy_two_x_movement[idx]=4
                    if self.player_rect.x<enemy_knight.x and self.enemy_two_distance_list[idx]>30 and self.enemy_two_health[idx]>0: 
                        SCREEN.blit(self.enemy_two_run_flip[int(self.enemy_two_run_number[0]//2)],(enemy_knight.x-self.camera_x_y[0]-25,enemy_knight.y-self.camera_x_y[1]-25))
                        self.enemy_two_x_movement[idx]=-4
                    self.enemy_two_run_number[0]+=0.35
                    if self.enemy_two_run_number[0]>10:
                        self.enemy_two_run_number[0]=0
            self.enemy_two_y_movement[0]=4
        
    def attack(self):
        global level_1, level_1_enemy_fight_condition
        self.enemy_two_attack_1=enemy_two_attack_1 ; self.enemy_two_attack_2=enemy_two_attack_2 ; self.enemy_two_attack_1_flip=enemy_two_attack_1_flip ; self.enemy_two_attack_2_flip=enemy_two_attack_2_flip
        self.enemy_two_attack_type=enemy_two_attack_type ; self.enemy_two_attack_number=enemy_two_attack_number ; self.enemy_two_attack_number=enemy_two_attack_number
        if level_1 and level_1_enemy_fight_condition:
            for idx,enemy_knight in enumerate(self.enemy_two_level_1_rect):
                self.enemy_two_attack_number.append(0)
                if self.enemy_two_attack_number[0]>len(self.enemy_two_level_1_rect):
                    del self.enemy_two_attack_number[-1]
                if self.enemy_two_distance_list[idx]<=30 and self.enemy_two_health[idx]>0:
                    self.enemy_two_x_movement[idx]=0
                    if self.enemy_two_attack_type[0]>2:
                        self.enemy_two_attack_type[0]=1
                    if self.enemy_two_attack_type[0]==1:
                        if self.player_rect.x>=enemy_knight.x:
                            SCREEN.blit(self.enemy_two_attack_1[int(self.enemy_two_attack_number[idx]//2)],(enemy_knight.x-self.camera_x_y[0]-80,enemy_knight.y-self.camera_x_y[1]-57))
                        if self.player_rect.x<enemy_knight.x:
                            SCREEN.blit(self.enemy_two_attack_1_flip[int(self.enemy_two_attack_number[idx]//2)],(enemy_knight.x-self.camera_x_y[0]-80,enemy_knight.y-self.camera_x_y[1]-57))
                    if self.enemy_two_attack_type[0]==2:
                        if self.player_rect.x>=enemy_knight.x:
                            SCREEN.blit(self.enemy_two_attack_2[int(self.enemy_two_attack_number[idx]//2)],(enemy_knight.x-self.camera_x_y[0]-80,enemy_knight.y-self.camera_x_y[1]-57))
                        if self.player_rect.x<enemy_knight.x:
                            SCREEN.blit(self.enemy_two_attack_2_flip[int(self.enemy_two_attack_number[idx]//2)],(enemy_knight.x-self.camera_x_y[0]-80,enemy_knight.y-self.camera_x_y[1]-57))
                    self.enemy_two_attack_number[idx]+=0.50
                    if self.enemy_two_attack_number[idx]>8:
                        self.enemy_two_attack_number[idx]=0
                        self.player_current_health[0]-=25  #50
                        self.enemy_two_attack_type[0]+=1
                
    def player_hit(self):
        global level_1, attack,level_1_enemy_fight_condition,attack_done, player_idle_right, player_idle_left
        if level_1:
            if attack_done and level_1_enemy_fight_condition:
                for idx,knight in enumerate(self.enemy_two_level_1_rect):
                    if self.enemy_two_distance_list[idx]<50:
                        if player_idle_right and self.player_rect.x<=self.enemy_two_level_1_rect[idx].x:
                            self.enemy_two_health[idx]-=25
                            print(self.enemy_two_health)
                        if player_idle_left and self.player_rect.x>self.enemy_two_level_1_rect[idx].x:
                            self.enemy_two_health[idx]-=25
                            print(self.enemy_two_health)
                        attack_done=False   
    def fall(self):
        global reset_enemy_position
        self.enemy_two_fall=enemy_two_fall ; self.enemy_two_fall_flip=enemy_two_fall_flip ; self.enemy_two_fall_number=enemy_two_fall_number
        if level_1 and not reset_enemy_position:
            for idx,knight in enumerate(self.enemy_two_level_1_rect):
                if self.enemy_two_health[idx]<=0:
                    self.enemy_two_health[idx]=0
                    self.enemy_two_x_movement[idx]=0
                    if self.enemy_two_fall_direction_set[idx]==1:
                        if self.enemy_two_fall_number[idx]<6:
                                SCREEN.blit(self.enemy_two_fall[int(self.enemy_two_fall_number[idx])//2],(self.enemy_two_level_1_rect[idx].x-self.camera_x_y[0],knight.y-self.camera_x_y[1]-25))
                        else:
                                self.enemy_two_fall_number[idx]=6     
                                SCREEN.blit(self.enemy_two_fall[int(self.enemy_two_fall_number[idx])//2],(self.enemy_two_level_1_rect[idx].x-self.camera_x_y[0],knight.y-self.camera_x_y[1]-25))
                    if self.enemy_two_fall_direction_set[idx]==2:
                        if self.enemy_two_fall_number[idx]<6:
                            SCREEN.blit(self.enemy_two_fall_flip[int(self.enemy_two_fall_number[idx])//2],(self.enemy_two_level_1_rect[idx].x-self.camera_x_y[0],knight.y-self.camera_x_y[1]-25))
                        else:
                            self.enemy_two_fall_number[idx]=6
                            SCREEN.blit(self.enemy_two_fall_flip[int(self.enemy_two_fall_number[idx])//2],(self.enemy_two_level_1_rect[idx].x-self.camera_x_y[0],knight.y-self.camera_x_y[1]-25))                         
                    self.enemy_two_fall_number[idx]+=0.50  
                          
    def reset_position(self):
        global reset_enemy_position,level_1_enemy_fight_condition
        if level_1 and reset_enemy_position:
            self.enemy_two_fall_number.clear() ; self.enemy_two_distance_list.clear() ; self.enemy_two_fall_direction_set.clear()
            for idx,knight in enumerate(self.enemy_two_level_1_rect):
                self.enemy_two_level_1_rect[idx].x=self.enemy_two_level_1_x[idx]
            for idx,knight in enumerate(self.enemy_two_level_1_rect):
                self.enemy_two_health[idx]=150
                
    def collision_with_object(self,tile_level_1):
        if level_1:
            hit_tile=[]
            for idx,enemy_knight in enumerate(self.enemy_two_level_1_rect):
                for tiles in self.tile_level_1_rect:
                    if enemy_knight.colliderect(tiles):
                        hit_tile.append(tiles)
            return hit_tile
        
    def collision_with_object_logic(self,tile_level_1):
        global level_1_enemy_fight_condition
        if level_1:
            for idx,enemy_knight in enumerate(self.enemy_two_level_1_rect):
                    enemy_knight.x+=self.enemy_two_x_movement[idx]
            collision=EnemyTwo.collision_with_object(self,tile_level_1)
            for tile in collision:
                for idx,enemy_knight in enumerate(self.enemy_two_level_1_rect):
                    if self.enemy_two_x_movement[idx]>0:
                        enemy_knight.right=tile.left
                    if self.enemy_two_x_movement[idx]<0:
                        enemy_knight.left=tile.right
            for idx,enemy_knight in enumerate(self.enemy_two_level_1_rect):
                enemy_knight.y+=self.enemy_two_y_movement[0]
            collision=EnemyTwo.collision_with_object(self,tile_level_1)
            for tile in collision:
                for idx,enemy_knight in enumerate(self.enemy_two_level_1_rect):
                    if enemy_knight.colliderect(tile):
                        enemy_knight.bottom=tile.top
            return self.enemy_two_rect_list   