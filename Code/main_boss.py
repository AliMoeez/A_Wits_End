class MainBoss(Player):
    def __init__(self,main_boss_rect_level_1,main_boss_x_movement,main_boss_y_movement):
        super().__init__(player_x_movement,player_y_movement,player_rect,player_current_health)
        self.main_boss_rect_level_1=main_boss_rect_level_1 ; self.main_boss_x_movement=main_boss_x_movement ; self.main_boss_y_movement=main_boss_y_movement
        
    def movement(self):
        global level_1,level_1_dialogue_part_two,level_one_dialogue_part_three,end_level_1_dialogue
        self.main_boss_idle=main_boss_idle ; self.main_boss_idle_flip=main_boss_idle_flip ; self.main_boss_idle_number=main_boss_idle_number ; self.main_boss_run=main_boss_run ; self.main_boss_run_flip=main_boss_run_flip 
        self.main_boss_run_number=main_boss_run_number; self.main_boss_level_1_x=main_boss_level_1_x
        if level_1:
            if not level_1_dialogue_part_two:
                self.main_boss_x_movement[0]=0
                if self.player_rect.x>=self.main_boss_rect_level_1.x:
                    SCREEN.blit(self.main_boss_idle[int(self.main_boss_idle_number[0])//2],(self.main_boss_rect_level_1.x-self.camera_x_y[0],self.main_boss_rect_level_1.y-self.camera_x_y[1]+15))
                if self.player_rect.x<self.main_boss_rect_level_1.x:
                     SCREEN.blit(self.main_boss_idle_flip[int(self.main_boss_idle_number[0])//2],(self.main_boss_rect_level_1.x-self.camera_x_y[0],self.main_boss_rect_level_1.y-self.camera_x_y[1]+15))
                self.main_boss_idle_number[0]+=0.30
                if self.main_boss_idle_number[0]>9:
                    self.main_boss_idle_number[0]=0
                self.main_boss_y_movement[0]=8
            if level_1_dialogue_part_two and not end_level_1_dialogue:
                self.main_boss_x_movement[0]=-20
                SCREEN.blit(self.main_boss_run_flip[int(self.main_boss_run_number[0])//2],(self.main_boss_rect_level_1.x-self.camera_x_y[0],self.main_boss_rect_level_1.y-self.camera_x_y[1]+15))
                self.main_boss_run_number[0]+=0.45
                if self.main_boss_run_number[0]>7:
                    self.main_boss_run_number[0]=0
                if self.main_boss_rect_level_1.x<2100:
                    level_one_dialogue_part_three=True
                    
    def reset_position(self):
        global reset_enemy_position,level_1_enemy_fight_condition
        self.main_boss_level_1_x=main_boss_level_1_x ; self.main_boss_level_1_y=main_boss_level_1_y
        if level_1 and reset_enemy_position:
            self.main_boss_rect_level_1.x=self.main_boss_level_1_x[0]
            self.main_boss_rect_level_1.y=600
            reset_enemy_position=False
                    
    def collision_with_object(self,tile_level_1):
        if level_1:
            hit_tile=[]
            for tiles in self.tile_level_1_rect:
                if self.main_boss_rect_level_1.colliderect(tiles):
                    hit_tile.append(tiles)
            return hit_tile
        
    def collision_with_object_logic(self,tile_level_1):
        if level_1:
            if level_1_dialogue_part_two:
                self.main_boss_rect_level_1.x+=self.main_boss_x_movement[0]
            collision=MainBoss.collision_with_object(self,tile_level_1)
            for tile in collision:
                if self.main_boss_x_movement[0]>0:
                    self.main_boss_rect_level_1.right=tile.left
                if self.main_boss_x_movement[0]<0:
                    self.main_boss_rect_level_1.left=tile.right
            self.main_boss_rect_level_1.y+=self.main_boss_y_movement[0]
            collision=MainBoss.collision_with_object(self,tile_level_1)
            for tile in collision:
                if self.main_boss_rect_level_1.colliderect(tile):
                    self.main_boss_rect_level_1.bottom=tile.top
            return self.main_boss_rect_level_1  