import Data

class Game:
    def __init__(self,level_1_bg,tile_level_1,camera_x_y,tile_level_1_rect,tile_level_2,tile_level_2_rect):
        self.level_1_bg=level_1_bg ; self.tile_level_1=tile_level_1 ; self.camera_x_y=camera_x_y ; self.tile_level_1_rect=tile_level_1_rect
        self.tile_level_2=tile_level_2; self.tile_level_2_rect=tile_level_2_rect
    
    def level_one(self,tile_level_1_ground,tile_level_1_dirt):
        global level_1,level_one_x_border,level_2,level_2_part_2
        self.tile_level_1_ground=tile_level_1_ground ; self.tile_level_1_dirt=tile_level_1_dirt ; self.level_1_bg_1=level_1_bg_1 ; self.level_1_houses=level_1_houses ; self.level_1_entity_type=level_1_entity_type
        self.level_1_entity_x=level_1_entity_x ; self.level_1_entity_y=level_1_entity_y ; self.level_1_wagon=level_1_wagon ; self.level_1_well=level_1_well ; self.level_1_lamp=level_1_lamp
        self.level_1_house_a=level_1_house_a ; self.level_1_house_b=level_1_house_b ; self.level_1_house_c=level_1_house_c ; self.level_1_crates=level_1_crates ; self.level_1_crate=level_1_crate
        self.player_x_movement=player_x_movement ; self.player_rect=player_rect ; self.player_current_health=player_current_health ; self.health_bar_length=500 ; self.maximum_health=1000
        self.health_bar_ratio=self.maximum_health/self.health_bar_length ; self.health_icon=health_icon
        if level_1:
        #test
            SCREEN.blit(self.level_1_bg,(0,0)) ; SCREEN.blit(self.level_1_bg_1,(0,0)) 
            if self.player_rect.x>=100 and self.player_rect.x<5350: self.camera_x_y[0]+=self.player_rect.x-self.camera_x_y[0]-210
            if self.player_rect.x<15: self.player_rect.x=15    
            if self.player_rect.x>=5350: self.camera_x_y[0]=5350-210
            if self.camera_x_y[0]<0: self.camera_x_y[0]=0
            if level_one_x_border:
                if self.player_rect.x<=2400:
                    self.player_rect.x=2400
            for idx,interger in enumerate(self.level_1_entity_type):
                if self.level_1_entity_type[idx]=="Houses": SCREEN.blit(self.level_1_houses,(self.level_1_entity_x[idx]-self.camera_x_y[0],self.level_1_entity_y[idx]))
                if self.level_1_entity_type[idx]=="HouseA": SCREEN.blit(self.level_1_house_a,(self.level_1_entity_x[idx]-self.camera_x_y[0],self.level_1_entity_y[idx]))
                if self.level_1_entity_type[idx]=="HouseB": SCREEN.blit(self.level_1_house_b,(self.level_1_entity_x[idx]-self.camera_x_y[0],self.level_1_entity_y[idx]))
                if self.level_1_entity_type[idx]=="HouseC": SCREEN.blit(self.level_1_house_c,(self.level_1_entity_x[idx]-self.camera_x_y[0],self.level_1_entity_y[idx]))
                if self.level_1_entity_type[idx]=="Wagon": SCREEN.blit(self.level_1_wagon,(self.level_1_entity_x[idx]-self.camera_x_y[0],self.level_1_entity_y[idx]))
                if self.level_1_entity_type[idx]=="Lamp": SCREEN.blit(self.level_1_lamp,(self.level_1_entity_x[idx]-self.camera_x_y[0],self.level_1_entity_y[idx]))
                if self.level_1_entity_type[idx]=="Well": SCREEN.blit(self.level_1_well,(self.level_1_entity_x[idx]-self.camera_x_y[0],self.level_1_entity_y[idx]))
                if self.level_1_entity_type[idx]=="Crates": SCREEN.blit(self.level_1_crates,(self.level_1_entity_x[idx]-self.camera_x_y[0],self.level_1_entity_y[idx]))
                if self.level_1_entity_type[idx]=="Crate": SCREEN.blit(self.level_1_crate,(self.level_1_entity_x[idx]-self.camera_x_y[0],self.level_1_entity_y[idx]))
            y_1=0
            for row in self.tile_level_1:
                x_1=0
                for tile in row:
                    if tile=="1":
                        SCREEN.blit(self.tile_level_1_ground,(x_1*48-self.camera_x_y[0],y_1*45-self.camera_x_y[1]))
                    if tile=="2":
                        SCREEN.blit(self.tile_level_1_dirt,(x_1*48-self.camera_x_y[0],y_1*45-self.camera_x_y[1]))
                    if tile!="0":
                        self.tile_level_1_rect.append(pygame.Rect(x_1*48,y_1*45,48,45))
                    x_1+=1
                y_1+=1  
            
        if level_1:
            health_icons=pygame.draw.rect(SCREEN,(165,42,42),pygame.Rect(10,10,self.player_current_health[0]/self.health_bar_ratio,25))
            SCREEN.blit(self.health_icon,(15,12))
            health_border=pygame.draw.rect(SCREEN,(220,220,220),pygame.Rect(10,10,self.health_bar_length,25),4) 
            
                
    def level_one_dialogue(self):
        global change_dialogue , dialogue_start_condition , end_dialogue ,change_dialogue_cond_1,level_1_enemy_fight_condition,level_1_dialogue_part_two, level_one_x_border, dialogue_move_condition,level_one_dialogue_part_three,end_level_1_dialogue
        self.main_boss_icon=main_boss_icon ; self.enemy_one_dialogue_list=enemy_one_dialogue_list ; self.player_icon=player_icon ; self.enemy_two_icon=enemy_two_icon ; self.player_current_health=player_current_health
        if self.player_rect.x>=2400 and not level_1_dialogue_part_two and self.player_current_health[0]>0 and level_1: 
        #    level_one_x_border=True 
            dialogue_move_condition=True
            rectangle_blur=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT)) ; rectangle_blur.set_alpha(100) ; rectangle_blur.fill((0,0,0))  ; SCREEN.blit(rectangle_blur,(0,0)) ; rectangle_box_1=pygame.Surface((SCREEN_WIDTH,200)) ; rectangle_box_1.fill((112,41,99))  ;  rectangle_box_1.set_alpha(75) ; SCREEN.blit(rectangle_box_1,(0,500))
            if self.enemy_one_dialogue_list[0]==0:
                SCREEN.blit(self.main_boss_icon,(80,525)) ; font_game=pygame.font.SysFont("Impact",28)  ; show_font_knight=font_game.render("Kornos",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(100,645))  
                font_game=pygame.font.SysFont("Impact",24)   ; show_font_knight=font_game.render("Behold the man that has saved our Empire from a war with those beasts!",1,(255,70,71))  ; SCREEN.blit(show_font_knight,(200,545))
                show_font_knight=font_game.render("Justice for our people is secrued!",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(200,575))
            if self.enemy_one_dialogue_list[0]==-1:
                SCREEN.blit(self.player_icon,(100,525)) ; font_game=pygame.font.SysFont("Impact",28) ;  show_font_knight=font_game.render("You",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(125,645))  
                font_game=pygame.font.SysFont("Impact",24)   ; show_font_knight=font_game.render("I know what you did to Onis! What justice will he get! You turned him",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(200,545))
                font_game=pygame.font.SysFont("Impact",24)   ; show_font_knight=font_game.render("into that monster!",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(200,575))
            if self.enemy_one_dialogue_list[0]==-2:
                SCREEN.blit(self.main_boss_icon,(80,525)) ; font_game=pygame.font.SysFont("Impact",28)  ; show_font_knight=font_game.render("Kornos",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(100,645))  
                font_game=pygame.font.SysFont("Impact",24)   ; show_font_knight=font_game.render("Hmmm... You've seen to catch on my good freind. Sometimes, certain actions",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(200,545))
                font_game=pygame.font.SysFont("Impact",24)   ; show_font_knight=font_game.render("must be taken to ensure the greater good....",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(200,575))
            if self.enemy_one_dialogue_list[0]==-3:
                SCREEN.blit(self.player_icon,(100,525)) ; font_game=pygame.font.SysFont("Impact",28) ;  show_font_knight=font_game.render("You",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(125,645))  
                font_game=pygame.font.SysFont("Impact",24)   ; show_font_knight=font_game.render("What greater good? The one that secures your power? You clearly left",1,(255,70,71))  ; SCREEN.blit(show_font_knight,(200,545))
                font_game=pygame.font.SysFont("Impact",24)   ; show_font_knight=font_game.render("Onis for dead.",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(200,575))
            if self.enemy_one_dialogue_list[0]==-4:
                SCREEN.blit(self.main_boss_icon,(80,525)) ; font_game=pygame.font.SysFont("Impact",28)  ; show_font_knight=font_game.render("Kornos",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(100,645))  
                font_game=pygame.font.SysFont("Impact",24)   ; show_font_knight=font_game.render("What is your play? Will you kill me for this action?",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(200,545))
                font_game=pygame.font.SysFont("Impact",24)   ; show_font_knight=font_game.render("I suggest that you back down......",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(200,575))  
            if self.enemy_one_dialogue_list[0]==-5:
                SCREEN.blit(self.player_icon,(100,525)) ; font_game=pygame.font.SysFont("Impact",28) ;  show_font_knight=font_game.render("You",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(125,645))  
                font_game=pygame.font.SysFont("Impact",24)   ; show_font_knight=font_game.render("Back down for what? Power has made you mad!",1,(255,70,71))  ; SCREEN.blit(show_font_knight,(200,545))
            if self.enemy_one_dialogue_list[0]==-6:
                SCREEN.blit(self.main_boss_icon,(80,525)) ; font_game=pygame.font.SysFont("Impact",28)  ; show_font_knight=font_game.render("Kornos",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(100,645))  
                font_game=pygame.font.SysFont("Impact",24)   ; show_font_knight=font_game.render("You speak to much. Arrest him now, and ensure to not hurt him.",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(200,545))
                font_game=pygame.font.SysFont("Impact",24)   ; show_font_knight=font_game.render("I must go and deal with other more important affairs.",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(200,575))  
            if self.enemy_one_dialogue_list[0]==-7: end_dialogue=True
            if event.type==pygame.MOUSEBUTTONDOWN:  change_dialogue_cond_1=True
            if event.type==pygame.MOUSEBUTTONUP and change_dialogue_cond_1:
                change_dialogue_cond_1=False ; change_dialogue=True  
            if change_dialogue:
                change_dialogue=False ; self.enemy_one_dialogue_list[0]-=1
            if end_dialogue:
                enemy_1_friendly_dialogue=False ; dialogue_start_condition=False ; self.enemy_one_dialogue_list[0]=0 ; end_dialogue=False ; level_1_dialogue_part_two=True
        if level_one_dialogue_part_three and not end_level_1_dialogue:
            rectangle_blur=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT)) ; rectangle_blur.set_alpha(100) ; rectangle_blur.fill((0,0,0))  ; SCREEN.blit(rectangle_blur,(0,0)) ; rectangle_box_1=pygame.Surface((SCREEN_WIDTH,200)) ; rectangle_box_1.fill((112,41,99))  ;  rectangle_box_1.set_alpha(75) ; SCREEN.blit(rectangle_box_1,(0,500))
            if self.enemy_one_dialogue_list[0]==0:
                SCREEN.blit(self.enemy_two_icon,(80,525)) ; font_game=pygame.font.SysFont("Impact",28)  ; show_font_knight=font_game.render("Elite Knight",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(80,645))  
                font_game=pygame.font.SysFont("Impact",24)   ; show_font_knight=font_game.render("You heard him, put your weapon down and surrender!",1,(255,70,71))  ; SCREEN.blit(show_font_knight,(200,545))
            if self.enemy_one_dialogue_list[0]==-1:
                SCREEN.blit(self.player_icon,(100,525)) ; font_game=pygame.font.SysFont("Impact",28) ;  show_font_knight=font_game.render("You",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(125,645))  
                font_game=pygame.font.SysFont("Impact",24)   ; show_font_knight=font_game.render("Never, you will have to kill me before I surrender!",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(200,545))
            if self.enemy_one_dialogue_list[0]==-2:
                SCREEN.blit(self.enemy_two_icon,(80,525)) ; font_game=pygame.font.SysFont("Impact",28)  ; show_font_knight=font_game.render("Elite Knight",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(80,645))  
                font_game=pygame.font.SysFont("Impact",24)   ; show_font_knight=font_game.render("So be it..... Arrest this man now by any means neccesary!",1,(255,70,71)) ; SCREEN.blit(show_font_knight,(200,545))
            if self.enemy_one_dialogue_list[0]==-3: end_dialogue=True
            if event.type==pygame.MOUSEBUTTONDOWN:  change_dialogue_cond_1=True
            if event.type==pygame.MOUSEBUTTONUP and change_dialogue_cond_1:
                change_dialogue_cond_1=False ; change_dialogue=True  
            if change_dialogue:
                change_dialogue=False ; self.enemy_one_dialogue_list[0]-=1
            if end_dialogue:
                enemy_1_friendly_dialogue=False ; dialogue_start_condition=False ; self.enemy_one_dialogue_list[0]=0 ; end_dialogue=False ; dialogue_move_condition=False ; level_1_enemy_fight_condition=True
                end_level_1_dialogue=True
                
    def level_one_win(self):
        self.enemy_1_health_list=enemy_1_health_list ; self.enemy_two_health=enemy_two_health ; self.win_blur=win_blur
        global level_1,level_win, level_2, level_3, reset_enemy_position
        if level_1 and all(idx<=0 for idx in self.enemy_1_health_list) and all(idx<=0 for idx in self.enemy_two_health) and self.player_rect.x>6100:
            print("here") ; level_win=True
        if level_win:
            self.win_blur[0]+=5
            rectangle_blur=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT)) ; rectangle_blur.set_alpha(self.win_blur[0]) ; rectangle_blur.fill((0,0,0))  ; SCREEN.blit(rectangle_blur,(0,0))
            if self.win_blur[0]>280: self.win_blur[0]=280
            font_game=pygame.font.SysFont("Impact",48) ; show_font_defeat=font_game.render("LEVEL COMPLETED",1,(255,70,71))  ; show_font_defeat_rect=show_font_defeat.get_rect(center=(SCREEN_WIDTH/2,200))  ; SCREEN.blit(show_font_defeat,show_font_defeat_rect)           
            rectangle_retry=pygame.Surface((100,30)) ; rectangle_retry.set_alpha(0)  ; rectangle_retry.fill((200,200,200)) ; rectangle_retry=SCREEN.blit(rectangle_retry,(SCREEN_WIDTH/2-150,387))
            font_game=pygame.font.SysFont("Impact",30) ; show_font_defeat=font_game.render("NEXT LEVEL",1,(255,70,71)) ; show_font_defeat_rect=show_font_defeat.get_rect(center=(SCREEN_WIDTH/2-100,400))  ; SCREEN.blit(show_font_defeat,show_font_defeat_rect)
            rectangle_main_menu=pygame.Surface((150,30))  ; rectangle_main_menu.set_alpha(0) ; rectangle_main_menu.fill((200,200,200))  ; rectangle_main_menu=SCREEN.blit(rectangle_main_menu,(SCREEN_WIDTH/2+25,387))
            font_game=pygame.font.SysFont("Impact",30) ; show_font_defeat=font_game.render("MAIN MENU",1,(255,70,71)) ; show_font_defeat_rect=show_font_defeat.get_rect(center=(SCREEN_WIDTH/2+100,400)) ; SCREEN.blit(show_font_defeat,show_font_defeat_rect)
            level_1_dialogue_part_two=False ; end_level_1_dialogue=False ; level_one_dialogue_part_three=False ; end_level_1_dialogue=False
            dialogue_move_condition=False
            
            if pygame.Rect.collidepoint(rectangle_retry,pygame.mouse.get_pos()) and event.type==pygame.MOUSEBUTTONDOWN:
                level_1=False ; level_2=False ; level_3=False ; reset_enemy_position=True
             #   if level_1:
             #       level_1_enemy_fight_condition=False
             #       level_1=False ; level_2=True ; level_3=False
             #   if level_2:
             #       level_1=False ; level_2=False ; level_3=True
                self.player_current_health[0]=1000  ; level_1_enemy_fight_condition=False ; level_win=False

            if pygame.Rect.collidepoint(rectangle_main_menu,pygame.mouse.get_pos()) and event.type==pygame.MOUSEBUTTONDOWN:
                level_selection=False ; level_1=False ; level_screen=False ; self.player_current_health[0]=1000 ; player_death=False ; reset_enemy_position=True
                level_1_enemy_fight_condition=False          
                level_2=False ; level_3=False 
                
    def level_two(self):
        global level_2,level_screen,level_2_passive_condition,level_2_part_2,level_2_dialogue_part_two,level_2_dialogue_once_two,level_2_part_2_boss_dialogue,level_2_dialogue_part_two_once
        self.level_2_bg_list=level_2_bg_list ; self.list_2_bg_y_pos=list_2_bg_y_pos ; self.level_2_dec_list=level_2_dec_list ; self.level_2_item_list=level_2_item_list
        self.level_2_bg_1=level_2_bg_1 ; self.level_2_bg_2=level_2_bg_2 ; self.level_2_bg_3=level_2_bg_3; self.level_2_bg_4=level_2_bg_4; self.level_2_bg_5=level_2_bg_5
        self.level_2_bg_6=level_2_bg_6; self.level_2_bg_7=level_2_bg_7; self.level_2_bg_8=level_2_bg_8; self.level_2_bg_9=level_2_bg_9 ; self.level_2_bg_10=level_2_bg_10
        self.level_2_bg_11=level_2_bg_11 ; self.level_2_bg_12=level_2_bg_12 ; self.level_2_blur_list=level_2_blur_list ; self.level_2_blur_list_2=level_2_blur_list_2 ; self.camera_x_y=camera_x_y ; self.player_rect=player_rect; self.player_x_movement=player_x_movement
        self.level_2_2=level_2_2 ; self.level_2_8=level_2_8 ; self.level_2_3=level_2_3 ; self.level_2_10=level_2_10 ; self.level_2_11=level_2_11 ; self.level_2_22=level_2_22 ; self.level_2_23=level_2_23 ; self.level_2_24=level_2_24 ; self.level_2_25=level_2_25
        self.level_2_5=level_2_5 ; self.level_2_6=level_2_6 ; self.level_2_34=level_2_34 ; self.level_2_35=level_2_35 ; self.level_2_19=level_2_19 ; self.level_2_20=level_2_20 ; self.level_2_1=level_2_1 ; self.level_2_12=level_2_12
        self.level_2_15=level_2_15 ; self.level_2_16=level_2_16 ; self.level_2_17=level_2_17 ; self.level_2_14=level_2_14 ; self.level_2_32=level_2_32 ; self.level_2_33=level_2_33 ; self.level_2_26=level_2_26
        self.level_2_7=level_2_7 ; self.level_2_36=level_2_36 ; self.level_2_37=level_2_37; self.level_2_dec_1=level_2_dec_1 ; self.level_2_dec_2=level_2_dec_2 
        self.level_2_table=level_2_table ; self.level_2_crate=level_2_crate ; self.level_2_crate_damage=level_2_crate_damage ; self.level_2_bag=level_2_bag ; self.level_2_books=level_2_books
        self.level_2_flag=level_2_flag ; self.level_2_potion_1=level_2_potion_1 ; self.level_2_potion_2=level_2_potion_2 ; self.level_2_torch=level_2_torch ; self.level_2_fixture=level_2_fixture
        self.level_2_candle=level_2_candle ; self.level_2_dec_number=level_2_dec_number ; self.level_2_animated_item_list=level_2_animated_item_list ; self.level_2_torch_1_bg=level_2_torch_1_bg; self.level_2_bag_2=level_2_bag_2
        self.level_2_tile_index=level_2_tile_index
        

        if level_2:
            level_screen=False
            self.level_2_bg_list=[self.level_2_bg_8,self.level_2_bg_9,self.level_2_bg_6,self.level_2_bg_7,self.level_2_bg_4,self.level_2_bg_3,
                                  self.level_2_bg_5,self.level_2_bg_2,self.level_2_bg_1,self.level_2_bg_11,self.level_2_bg_10,self.level_2_bg_12]
            
            self.level_2_dec_list=[(self.level_2_1,"1"), (self.level_2_2,"2"), (self.level_2_3,"3"),(self.level_2_5,"5"), (self.level_2_6,"6"), (self.level_2_8,"8"),
                                   (self.level_2_10,"10"), (self.level_2_11,"11"), (self.level_2_12,"12"), (self.level_2_14,"14"), (self.level_2_15,"15"), (self.level_2_16,"16"),
                                   (self.level_2_17,"17"), (self.level_2_19,"19"), (self.level_2_20,"20"), (self.level_2_22,"22"), (self.level_2_23,"23"), (self.level_2_24,"24"),
                                   (self.level_2_25,"25"), (self.level_2_26,"26"), (self.level_2_32,"32"), (self.level_2_33,"33"), (self.level_2_34,"34"), (self.level_2_35,"35"),
                                   (self.level_2_7,"7"),(self.level_2_36,"36"),(self.level_2_37,"37")]
            
            #dec1 421 #dec2 420 #table 520 #crate 500 #crate_damage 500 #bag 520 #books 520 #flag 300 #potion_1 520 #potion_2 520
            
            self.level_2_item_list=[(self.level_2_dec_1,295,421), (self.level_2_dec_2,895,421), (self.level_2_table,240,520), (self.level_2_books,435,520), (self.level_2_bag_2,2200,605),
                                    (self.level_2_crate_damage,700,500), (self.level_2_bag,750,520), (self.level_2_potion_1,775,520), (self.level_2_crate,1400,585), (self.level_2_crate_damage,1450,585),
                                    (self.level_2_potion_2,1750,605), (self.level_2_potion_1,2705,560), (self.level_2_crate,3225,495), (self.level_2_bag,3250,515), (self.level_2_flag,300,300),
                                    (self.level_2_flag,900,300), (self.level_2_flag,2500,300), (self.level_2_flag,3100,300), (self.level_2_crate_damage,3750,540), (self.level_2_potion_2,3550,555), (self.level_2_bag_2,4300,555),
                                    (self.level_2_potion_1,5275,520), (self.level_2_potion_2,5750,520), (self.level_2_bag_2,4500,520), (self.level_2_potion_1,4735,520), (self.level_2_flag,5350,300),(self.level_2_flag,5800,300), (self.level_2_dec_1,5345,421),(self.level_2_dec_2,5800,421)]
            
            
            self.level_2_animated_item_list=[(self.level_2_torch,265,400), (self.level_2_fixture,1000,470), (self.level_2_torch,1020,400), (self.level_2_torch,2530,400), (self.level_2_torch,3130,400),
                                             (self.level_2_torch,3900,400), (self.level_2_torch,5325,400), (self.level_2_torch,5895,400), (self.level_2_fixture,5325,470),(self.level_2_fixture,5895,470)]
                
            
            if level_2_passive_condition:
                self.player_rect.x+=self.player_x_movement[0]
                for idx, item in enumerate(self.level_2_bg_list):
                    SCREEN.blit(item,(-self.camera_x_y[0]-self.player_rect.x-100,self.list_2_bg_y_pos[idx]))
                    SCREEN.blit(item,(-self.camera_x_y[0]-self.player_rect.x+1100-100,self.list_2_bg_y_pos[idx]))
                if self.player_rect.x>500:
                    for idx,item in enumerate(self.level_2_bg_list):
                        SCREEN.blit(item,(-self.camera_x_y[0]-self.player_rect.x+2200-100,self.list_2_bg_y_pos[idx])) #1100
                        SCREEN.blit(item,(-self.camera_x_y[0]-self.player_rect.x+3300-100,self.list_2_bg_y_pos[idx]))
                        SCREEN.blit(item,(-self.camera_x_y[0]-self.player_rect.x+4400-100,self.list_2_bg_y_pos[idx]))
                if self.player_rect.x<100: self.player_rect.x=100
                if self.player_rect.x>=500: self.camera_x_y[0]+=0
                else: self.camera_x_y[0]+=self.player_rect.x-self.camera_x_y[0]
              
                if self.player_rect.x>=1500 and not level_2_part_2:
                        self.level_2_blur_list[0]+=5 #50
                        rectangle_blur=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT)) ; rectangle_blur.set_alpha(self.level_2_blur_list[0]) ; rectangle_blur.fill((0,0,0))  ; SCREEN.blit(rectangle_blur,(0,0))
                        if self.level_2_blur_list[0]>300:
                            self.level_2_blur_list[0]=300
                            self.level_2_blur_list_2[0]-=5 #50
                            self.player_rect.x=0
                            self.player_rect.y=500 #500
                            level_2_part_2=True
                        
            if level_2_part_2:
                if self.player_rect.x<210:
                    self.player_rect.x=210
                if self.player_rect.x>=210 and self.player_rect.x<=5300:
                    self.camera_x_y[0]+=self.player_rect.x-self.camera_x_y[0]-210
                SCREEN.blit(self.level_1_bg,(0,0))
                self.level_2_blur_list_2[0]-=10 #50
                if self.level_2_blur_list_2[0]<0:
                    self.level_2_blur_list_2[0]=0
              #  rectangle_blur=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT)) ; rectangle_blur.set_alpha(self.level_2_blur_list_2[0]) ; rectangle_blur.fill((0,0,0))  ; SCREEN.blit(rectangle_blur,(0,0))
                y_1=0
                for row in self.tile_level_2:
                    x_1=0
                    for tile in row:
                        for idx,number in enumerate(self.level_2_dec_list):
                            if tile==self.level_2_dec_list[idx][1]:
                                SCREEN.blit(self.level_2_dec_list[idx][0],(x_1*48-self.camera_x_y[0],y_1*45-self.camera_x_y[1]))
                        if tile in ["15","16","32","33","19","22","19","20","10","23","25","27","14","17","26"]:
                            self.tile_level_2_rect.append(pygame.Rect(x_1*48,y_1*45,48,45))
                            self.level_2_tile_index.append(tile)
                        x_1+=1
                    y_1+=1 

                if not level_2_dialogue_once_two:
                    level_2_dialogue_part_two=True
                    
                for idx,number in enumerate(self.level_2_item_list):
                    SCREEN.blit(self.level_2_item_list[idx][0],(self.level_2_item_list[idx][1]-self.camera_x_y[0],self.level_2_item_list[idx][2]))
                    
                for idx,number in enumerate(self.level_2_animated_item_list):
                    if self.level_2_animated_item_list[idx][0]==self.level_2_torch:
                        SCREEN.blit(self.level_2_torch_1_bg,(self.level_2_animated_item_list[idx][1]-self.camera_x_y[0]-14,self.level_2_animated_item_list[idx][2]))
                    SCREEN.blit(self.level_2_animated_item_list[idx][0][int(self.level_2_dec_number[0])//2],(self.level_2_animated_item_list[idx][1]-self.camera_x_y[0],self.level_2_animated_item_list[idx][2]))

                rectangle_blur=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT)) ; rectangle_blur.set_alpha(self.level_2_blur_list_2[0]) ; rectangle_blur.fill((0,0,0))  ; SCREEN.blit(rectangle_blur,(0,0))
   
                self.level_2_dec_number[0]+=0.60
                
                if self.level_2_dec_number[0]>6:
                    self.level_2_dec_number[0]=0
                    
                if self.player_rect.x>=6100:
                    self.player_rect.x=6100
                
                if self.player_rect.x>5300 and not level_2_dialogue_part_two_once:
                    level_2_part_2_boss_dialogue=True
                    
            if level_2 or level_2_part_2:
                health_icons=pygame.draw.rect(SCREEN,(165,42,42),pygame.Rect(10,10,self.player_current_health[0]/self.health_bar_ratio,25))
                SCREEN.blit(self.health_icon,(15,12))
                health_border=pygame.draw.rect(SCREEN,(220,220,220),pygame.Rect(10,10,self.health_bar_length,25),4) 
                    
    def level_two_dialogue(self):
        #here
        global level_2, level_2_part_2, level_2_dialogue_part_one,dialogue_move_condition,change_dialogue_cond_1,change_dialogue,end_dialogue,level_2_dialogue_part_one_once
        global level_2_dialogue_part_two,level_2_dialogue_once_two,level_2_part_2_boss_dialogue, level_2_dialogue_part_two_once
        self.general_boss_icon=general_boss_icon ; self.level_2_dialogue_list_part_1_length=level_2_dialogue_list_part_1_length ; self.player_icon=player_icon ; self.enemy_one_icon=enemy_one_icon
        self.level_2_blur_list_2=level_2_blur_list_2 ; self.boss_1_icon=boss_1_icon
        self.level_2_dialogue_list_part_1=[
        ("I don't want to have to do this!","You",self.player_icon),
        ("Do what? I have heard of your defection and arrest! I stand with you!","General Lopen",self.general_boss_icon),
        ("What? Are you against Kornos now?","You",self.player_icon),
        ("Yes, I have made a clear order for my men to stage a coup against him! Do you want to help?","General Lopen",self.general_boss_icon),
        ("What is your request?","You",self.player_icon),
        ("I know Kornos's location. If you are intrested, are you willing to deal with him?","General Lopen",self.general_boss_icon),
        ("Yes, I want to end this tyrants regin! Where is he located?","You",self.player_icon),
        ("He is located at the District 10 Fortress. It is a good area to hide, so he wont expect it.","General Lopen",self.general_boss_icon),
        ("I will deal with him and return here in a days time to discuss how it went.","You",self.player_icon)
        ]
        
        self.level_2_dialogue_list_part_2=[
        ("He's fell for it! Get him!!!","Knight",self.enemy_one_icon),
        ("Wait what!?","You",self.player_icon)
        ]
        
        self.level_2_dialogue_list_3=[
        ("HehHAHAAHA, YOu've aRrived!!!","???",self.boss_1_icon),
        ("Are you ok? Who are you? Where is Kornos!?","You",self.player_icon),
        ("iM Fine, ThANK yoU fOr asKINg...My nAmE is HIgH LoRD STepHeN.. SaME mE!","High Lord Stephen",self.boss_1_icon),
        ("Why are you like this? Did Kornos do this to you?","You",self.player_icon),
        ("He GaVE mE pOWerS onE caNNOT ImagINE, lOOK aT thE pOTionS aROUnd hERE, yoU FOOL!!","High Lord Stephen",self.boss_1_icon),
        ("I assume you want me to surrder right?","You",self.player_icon),
        ("YeS, YES, yES, YES!!!!! IT is EaSiER tHAt wAY, oR I wILL FORcE yOU tO SURrenDER!","High Lord Stephen",self.boss_1_icon),
        ("Force me then.....","You",self.player_icon)
        ]
        
        if level_2_dialogue_part_one or level_2_dialogue_part_two and self.level_2_blur_list_2[0]<=0 or level_2_part_2_boss_dialogue:
            if level_2_dialogue_part_one:
                level_2_dialogue=self.level_2_dialogue_list_part_1 ; colour_box=(1,50,32) ; colour_font=(1,150,71)
            if level_2_dialogue_part_two:
                level_2_dialogue=self.level_2_dialogue_list_part_2 ; colour_box=(128,128,128) ; colour_font=(192,192,192)
            if level_2_part_2_boss_dialogue:
                level_2_dialogue=self.level_2_dialogue_list_3 ; colour_box=(128,128,128) ; colour_font=(192,192,192)
            dialogue_move_condition=True ; rectangle_blur=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))  ; rectangle_blur.set_alpha(100) ; rectangle_blur.fill((0,0,0))  ; SCREEN.blit(rectangle_blur,(0,0)) 
            rectangle_box_1=pygame.Surface((SCREEN_WIDTH,200))  ; rectangle_box_1.fill(colour_box)  ; rectangle_box_1.set_alpha(75)  ; SCREEN.blit(rectangle_box_1,(0,500))
            for idx, number in enumerate(level_2_dialogue):
                if idx==self.level_2_dialogue_list_part_1_length[0]:
                    SCREEN.blit(level_2_dialogue[idx][2],(80,525))  ; font_game=pygame.font.SysFont("Impact",28) 
                    show_font_knight=font_game.render(level_2_dialogue[idx][1],1,colour_font) 
                    if level_2_dialogue[idx][2]==self.player_icon: SCREEN.blit(show_font_knight,(110,645))
                    if level_2_dialogue[idx][2]==self.general_boss_icon: SCREEN.blit(show_font_knight,(55,645))  
                    if level_2_dialogue[idx][2]==self.enemy_one_icon: SCREEN.blit(show_font_knight,(55,645)) 
                    if level_2_dialogue[idx][1]=="???": SCREEN.blit(show_font_knight,(110,645)) 
                    if level_2_dialogue[idx][1]=="High Lord Stephen": SCREEN.blit(show_font_knight,(55,645)) 
                    font_game=pygame.font.SysFont("Impact",24) ; show_font_knight=font_game.render(level_2_dialogue[idx][0],1,colour_font) ; SCREEN.blit(show_font_knight,(200,545))
                if self.level_2_dialogue_list_part_1_length[0]>=len(level_2_dialogue):
                    if level_2_dialogue_part_two: level_2_dialogue_once_two=True
                    if level_2_part_2_boss_dialogue:  level_2_dialogue_part_two_once=True
                    level_2_dialogue_part_one=False ; level_2_dialogue_part_two=False ; level_2_part_2_boss_dialogue=False ; self.level_2_dialogue_list_part_1_length[0]=0 ;  
                    dialogue_move_condition=False ;  level_2_dialogue_part_one_once=True
            if event.type==pygame.MOUSEBUTTONDOWN:  change_dialogue_cond_1=True
            if event.type==pygame.MOUSEBUTTONUP and change_dialogue_cond_1:
                change_dialogue_cond_1=False ; change_dialogue=True  
            if change_dialogue:
                change_dialogue=False ; self.level_2_dialogue_list_part_1_length[0]+=1