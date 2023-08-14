import pygame

"""pygame.init()

FPS=30
run=True

SCREEN_WIDTH=1100 ; SCREEN_HEIGHT=700 ; SCREEN=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

clock=pygame.time.Clock()

test_list=[]

while run:
    tile_level_1_rect=[] ; tile_level_2_rect=[] ; level_2_bg_list=[] ; level_2_dec_list=[] ; level_2_item_list=[]
    key=pygame.key.get_pressed()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    menu=Menu(Data.camera_x_y_bg)
    menu.home(Data.level_3_bg_1,Data.level_3_bg_2)
    menu.level_selection()
    
    game=game.Game(level_1_bg,tile_level_1,camera_x_y,tile_level_1_rect,tile_level_2,tile_level_2_rect)
    game.level_one(tile_level_1_ground,tile_level_1_dirt)
    game.level_two()
    
    
    player=Player(player_x_movement,player_y_movement,player_rect,player_current_health)
    player.movement(player_idle,player_idle_flip,player_run,player_run_flip,player_jump,player_jump_flip)
    player.attack(player_attack_type_1,player_attack_type_1_flip,player_attack_type_2,player_attack_type_2_flip,
              player_attack_type_3,player_attack_type_3_flip,player_attack_type_4,player_attack_type_4_flip,attack_jump,attack_jump_flip)
    player.reset_position()
    player.collision_with_object(tile_level_1_rect,tile_level_2_rect)
    player.collision_with_object_logic(tile_level_1_rect,tile_level_2_rect)
    
    enemy_one=EnemyOne(enemy_list_level_1,npc_walk_length,npc_direction_choice,enemy_1_distance_list,enemy_1_health_list)
    enemy_one.move(enemy_1_level_1_rect,enemy_level_1_rect,enemy_1_level_1_rect_idle,enemy_1_x_movement,enemy_1_y_movement,enemy_1_level_2_rect)
    enemy_one.player_interaction()
    enemy_one.attack()
    enemy_one.player_hit()
    enemy_one.fall()
    enemy_one.reset_position()
    enemy_one.collision_with_object(tile_level_1,tile_level_2)
    enemy_one.collision_with_object_logic(tile_level_1,tile_level_2)
    
    enemy_two=EnemyTwo(enemy_two_level_1_rect,enemy_two_x_movement,enemy_two_y_movement,enemy_two_rect_list,enemy_two_distance_list,enemy_two_health)
    enemy_two.movement()
    enemy_two.attack()
    enemy_two.player_hit()
    enemy_two.fall()
    enemy_two.reset_position()
    enemy_two.collision_with_object(tile_level_1)
    enemy_two.collision_with_object_logic(tile_level_1)
    
    main_boss=MainBoss(main_boss_rect_level_1,main_boss_x_movement,main_boss_y_movement)
    main_boss.movement()
    main_boss.reset_position()
    main_boss.collision_with_object(tile_level_1)
    main_boss.collision_with_object_logic(tile_level_1)
    
    general_boss=GeneralBoss()
    general_boss.idle()
                        
    boss_one=BossOne(boss_1_rect,boss_1_level_2_part_2_x,boss_1_level_2_part_2_y,boss_1_x_movement,boss_1_y_movement)
    boss_one.idle()
    boss_one.move()
    boss_one.collision_with_object(tile_level_2)
    boss_one.collision_with_object_logic(tile_level_2)
    
    game.level_one_dialogue()
    game.level_two_dialogue()
    game.level_one_win()
    
    player.defeat()
    
    pygame.display.update()"""
    