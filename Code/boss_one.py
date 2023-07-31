class BossOne(Player):
    #here
    def __init__(self,boss_1_rect,boss_1_level_2_part_2_x,boss_1_level_2_part_2_y,boss_1_x_movement,boss_1_y_movement):
        super().__init__(player_x_movement,player_y_movement,player_rect,player_current_health)
        self.camera_x_y=camera_x_y ; self.boss_1_rect=boss_1_rect ; self.boss_1_level_2_part_2_x=boss_1_level_2_part_2_x ; self.boss_1_level_2_part_2_y=boss_1_level_2_part_2_y
        self.boss_1_x_movement=boss_1_x_movement ; self.boss_1_y_movement=boss_1_y_movement
    
    def idle(self):
        global level_2_part_2
        self.boss_1_idle_flip=boss_1_idle_flip ; self.boss_1_idle_number=boss_1_idle_number ; self.boss_1_level_2_part_2_x=boss_1_level_2_part_2_x ; self.boss_1_level_2_part_2_y=boss_1_level_2_part_2_y
        if level_2_part_2:
            self.boss_1_y_movement[0]=10
            if not level_2_dialogue_part_two_once:
                SCREEN.blit(self.boss_1_idle_flip[int(self.boss_1_idle_number[0])//2],(self.boss_1_rect.x-self.camera_x_y[0]-5,self.boss_1_rect.y-self.camera_x_y[1]-5))
                self.boss_1_idle_number[0]+=0.50
                if self.boss_1_idle_number[0]>9:
                    self.boss_1_idle_number[0]=0
                    
    def move(self):
        global level_2_part_2, level_2_dialogue_part_two_once
        if level_2_dialogue_part_two_once:
            self.player_boss_1_distance=math.sqrt(math.pow(self.player_rect.x-self.boss_1_rect.x,2)+math.pow(self.player_rect.x-self.boss_1_rect.x,2))
            if self.player_boss_1_distance<200:
                print(self.player_boss_1_distance)
                
    def collision_with_object(self,tile_level_2):
        if level_2_part_2:
            hit_tile=[]
            for tiles in self.tile_level_2_rect:
                if self.boss_1_rect.colliderect(tiles):
                    hit_tile.append(tiles)
            return hit_tile
        
    def collision_with_object_logic(self,tile_level_2):
        if level_2_part_2:
            self.boss_1_rect.x+=self.boss_1_x_movement[0]
            collision=BossOne.collision_with_object(self,tile_level_2)
            for tile in collision:
                if self.boss_1_x_movement[0]>0:
                    self.boss_1_rect.right=tile.left
                if self.boss_1_x_movement[0]<0:
                    self.boss_1_rect.left=tile.right
            self.boss_1_rect.y+=self.boss_1_y_movement[0]
            collision=BossOne.collision_with_object(self,tile_level_2)
            for tile in collision:
                if self.boss_1_rect.colliderect(tile):
                    self.boss_1_rect.bottom=tile.top
            return self.boss_1_rect  