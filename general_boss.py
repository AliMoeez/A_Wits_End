class GeneralBoss(Player):
    def __init__(self):
        super().__init__(player_x_movement,player_y_movement,player_rect,player_current_health)
        self.general_boss_idle_1=general_boss_idle_1; self.camera_x_y=camera_x_y
        
    def idle(self):
        global level_2, level_2_part_2,level_2_dialogue_part_one,level_2_dialogue_part_one_once
        self.general_boss_idle=general_boss_idle ; self.general_boss_idle_left=general_boss_idle_left ; self.general_boss_idle_number=general_boss_idle_number
        self.general_boss_x=general_boss_x ; self.general_boss_y=general_boss_y
        if level_2 and not level_2_part_2:
            if self.player_rect.x>=self.general_boss_x[0]-700: SCREEN.blit(self.general_boss_idle[int(self.general_boss_idle_number[0])//2],(self.general_boss_x[0]-self.player_rect.x-self.camera_x_y[0],self.general_boss_y[0]-self.camera_x_y[1]))
            if self.player_rect.x<self.general_boss_x[0]-700: SCREEN.blit(self.general_boss_idle_left[int(self.general_boss_idle_number[0])//2],(self.general_boss_x[0]-self.player_rect.x-self.camera_x_y[0],self.general_boss_y[0]-self.camera_x_y[1]))
            self.general_boss_idle_number[0]+=0.27 #17
            if self.general_boss_idle_number[0]>10: self.general_boss_idle_number[0]=0
            if self.player_rect.x-self.general_boss_x[0]-700>-1500 and not level_2_dialogue_part_one_once:
                level_2_dialogue_part_one=True