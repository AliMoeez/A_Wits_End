import pygame,sys,json,random, math

pygame.init()

SCREEN_WIDTH=1100 ; SCREEN_HEIGHT=700 ; SCREEN=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


pygame.display.set_caption("A_Wit's_End")

level_1_bg=pygame.image.load(r"A_Wit's_End\Level_1_Tileset\GothicVania-town-files\GothicVania-town-files\PNG\environment\layers\background.png") ; level_1_bg=pygame.transform.scale(level_1_bg,(SCREEN_WIDTH,SCREEN_HEIGHT))
level_1_bg_1=pygame.image.load(r"A_Wit's_End\Level_1_Tileset\GothicVania-town-files\GothicVania-town-files\PNG\environment\layers\middleground.png") ; level_1_bg_1=pygame.transform.scale(level_1_bg_1,(SCREEN_WIDTH,SCREEN_HEIGHT))

level_1_houses=pygame.image.load(r"A_Wit's_End\Level_1_Tileset\GothicVania-town-files\GothicVania-town-files\PNG\environment\props\houses.png") 
level_1_houses=pygame.transform.scale(level_1_houses,(1100,500))

level_1_wagon=pygame.image.load(r"A_Wit's_End\Level_1_Tileset\GothicVania-town-files\GothicVania-town-files\PNG\environment\props-sliced\wagon.png")  
level_1_well=pygame.image.load(r"A_Wit's_End\Level_1_Tileset\GothicVania-town-files\GothicVania-town-files\PNG\environment\props-sliced\well.png")   ; level_1_well=pygame.transform.scale(level_1_well,(100,80))
level_1_lamp=pygame.image.load(r"A_Wit's_End\Level_1_Tileset\GothicVania-town-files\GothicVania-town-files\PNG\environment\props-sliced\street-lamp.png")  ; level_1_lamp=pygame.transform.scale(level_1_lamp,(50,200))
level_1_house_a=pygame.image.load(r"A_Wit's_End\Level_1_Tileset\GothicVania-town-files\GothicVania-town-files\PNG\environment\props-sliced\house-a.png") 

level_1_house_a=pygame.transform.scale(level_1_house_a,(375,300))
level_1_house_b=pygame.image.load(r"A_Wit's_End\Level_1_Tileset\GothicVania-town-files\GothicVania-town-files\PNG\environment\props-sliced\house-b.png")  
level_1_house_b=pygame.transform.scale(level_1_house_b,(375,500))
level_1_house_c=pygame.image.load(r"A_Wit's_End\Level_1_Tileset\GothicVania-town-files\GothicVania-town-files\PNG\environment\props-sliced\house-c.png") ;
level_1_house_c=pygame.transform.scale(level_1_house_c,(375,350))

level_1_crates=pygame.image.load(r"A_Wit's_End\Level_1_Tileset\GothicVania-town-files\GothicVania-town-files\PNG\environment\props-sliced\crate-stack.png")
level_1_crate=pygame.image.load(r"A_Wit's_End\Level_1_Tileset\GothicVania-town-files\GothicVania-town-files\PNG\environment\props-sliced\crate.png")

level_1_entity_type=["HouseA","HouseB","HouseC","Wagon","HouseB","Lamp","Well","Lamp","Crates","HouseA","HouseC","HouseB","Crate","Crates","Crate","HouseC","HouseA","HouseB","HouseA","HouseC","HouseA","HouseB","HouseC","Crates","Crate","Wagon","Crates","Crate","Wagon","Crate"] 
level_1_entity_x=[20,395,780,900,1190,1600,1650,1745,40,1800,2200,2600,700,1100,1900,3000,3400,3800,4190,4590,5000,5400,5800,2350,2900,3670,4100,4470,4700,5100] 
level_1_entity_y=[340,140,295,565,140,445,563,445,572,340,295,140,605,572,605,295,340,140,340,295,340,140,295,572,605,565,572,605,565,605]

#HouseAA : 340
#HouseB : 140
#HouseC : 295
#Wagon : 565
#Lamp : 445
#Well : 563
#Crates: 572
#Crate: 605

level_2_bg_1=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Assets\Background_1.png"); level_2_bg_1=pygame.transform.scale(level_2_bg_1,(SCREEN_WIDTH,SCREEN_HEIGHT))
level_2_bg_2=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Assets\Background_2.png"); level_2_bg_2=pygame.transform.scale(level_2_bg_2,(SCREEN_WIDTH,SCREEN_HEIGHT))

level_2_bg_1=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Free Pixel Art Forest\PNG\Background layers\Layer_0003_6.png").convert_alpha()
level_2_bg_1=pygame.transform.scale(level_2_bg_1,(SCREEN_WIDTH,SCREEN_HEIGHT+600))
level_2_bg_2=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Free Pixel Art Forest\PNG\Background layers\Layer_0004_Lights.png").convert_alpha()
level_2_bg_2=pygame.transform.scale(level_2_bg_2,(SCREEN_WIDTH,SCREEN_HEIGHT+600))
level_2_bg_3=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Free Pixel Art Forest\PNG\Background layers\Layer_0005_5.png").convert_alpha()
level_2_bg_3=pygame.transform.scale(level_2_bg_3,(SCREEN_WIDTH,SCREEN_HEIGHT+600))
level_2_bg_4=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Free Pixel Art Forest\PNG\Background layers\Layer_0006_4.png").convert_alpha()
level_2_bg_4=pygame.transform.scale(level_2_bg_4,(SCREEN_WIDTH,SCREEN_HEIGHT+600))
level_2_bg_5=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Free Pixel Art Forest\PNG\Background layers\Layer_0007_Lights.png").convert_alpha() 
leve1_2_bg_5=pygame.transform.scale(level_2_bg_5,(SCREEN_WIDTH,SCREEN_HEIGHT+600))
level_2_bg_6=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Free Pixel Art Forest\PNG\Background layers\Layer_0008_3.png").convert_alpha() 
level_2_bg_6=pygame.transform.scale(level_2_bg_6,(SCREEN_WIDTH,SCREEN_HEIGHT+600))
level_2_bg_7=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Free Pixel Art Forest\PNG\Background layers\Layer_0009_2.png").convert_alpha() 
level_2_bg_7=pygame.transform.scale(level_2_bg_7,(SCREEN_WIDTH,SCREEN_HEIGHT+600))
level_2_bg_8=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Free Pixel Art Forest\PNG\Background layers\Layer_0010_1.png").convert_alpha() 
level_2_bg_8=pygame.transform.scale(level_2_bg_8,(SCREEN_WIDTH,SCREEN_HEIGHT))
level_2_bg_9=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Free Pixel Art Forest\PNG\Background layers\Layer_0011_0.png").convert_alpha() 
level_2_bg_9=pygame.transform.scale(level_2_bg_9,(SCREEN_WIDTH,SCREEN_HEIGHT))

level_2_bg_10=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Free Pixel Art Forest\PNG\Background layers\Layer_0000_9.png").convert_alpha() 
level_2_bg_10=pygame.transform.scale(level_2_bg_10,(SCREEN_WIDTH,SCREEN_HEIGHT))
level_2_bg_11=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Free Pixel Art Forest\PNG\Background layers\Layer_0001_8.png").convert_alpha() 
level_2_bg_11=pygame.transform.scale(level_2_bg_11,(SCREEN_WIDTH,SCREEN_HEIGHT))
level_2_bg_12=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Free Pixel Art Forest\PNG\Background layers\Layer_0002_7.png").convert_alpha() 
level_2_bg_12=pygame.transform.scale(level_2_bg_12,(SCREEN_WIDTH,SCREEN_HEIGHT+600))


#8,2,3,19,20,1,12

level_2_brick_1_2=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\brick_1_#2.png").convert_alpha() ; level_2_brick_7_8=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\brick_7_#8.png").convert_alpha()
level_2_brick_2_3=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\brick_2_#3.png").convert_alpha() ; level_2_brick_4_5=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\brick_4_#5.png").convert_alpha()
level_2_brick_5_6=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\brick_5_#6.png").convert_alpha() ; level_2_brick_1_34=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\damaged_brick_1_#34.png").convert_alpha()
level_2_brick_2_35=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\damaged_brick_2_#35.png").convert_alpha() ; level_2_brick_9_10=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\brick_9_#10.png").convert_alpha() 
level_2_brick_10_11=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\brick_10_#11.png").convert_alpha() ; level_2_carpet_2_19=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\floor_wood_carpet_2_#19.png").convert_alpha()
level_2_carpet_3_20=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\floor_wood_carpet_3_#20.png").convert_alpha() ; level_2_blank_1=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\blank_#1.png").convert_alpha()
level_2_brick_11_12=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\brick_11_#12.png").convert_alpha() ; level_2_brick_9_10=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\brick_9_#10.png").convert_alpha()
level_2_floor_2_15=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\floor_tile_2_#15.png").convert_alpha() ; level_2_floor_3_16=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\floor_tile_3_#16.png").convert_alpha()
level_2_floor_right=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\floor_tile_4_#17.png").convert_alpha() ; level_2_floor_left=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\floor_tile_1_#14.png").convert_alpha()
level_2_carpet_transition_left=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\floor_tile_carpet_transition_1_#32.png").convert_alpha() ; level_2_carpet_transition_right=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\floor_tile_carpet_transition_2_#33.png").convert_alpha()
level_2_platform_1_22=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\platform_1_#22.png").convert_alpha() ; level_2_platform_2_23=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\platform_2_#23.png").convert_alpha()
level_2_platform_3_24=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\platform_3_#24.png").convert_alpha() ; level_2_platform_4_25=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\platform_4_#25.png").convert_alpha()
level_2_stair_down=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\stairs_tile_1_#26_bg.png").convert_alpha() ; level_2_stair_up=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\stairs_tile_3_#27_bg.png").convert_alpha()
level_2_brick_6_7=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\brick_6_#7.png").convert_alpha() ; level_2_brick_15_36=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\brick_15_#36.png").convert_alpha() ; level_2_brick_16_37=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\level_2_tile_images\brick_16_#37.png").convert_alpha()

level_2_2=pygame.transform.scale(level_2_brick_1_2,(65,45)) ; level_2_8=pygame.transform.scale(level_2_brick_7_8,(65,45)) ; level_2_3=pygame.transform.scale(level_2_brick_2_3,(65,45))
level_2_10=pygame.transform.scale(level_2_brick_9_10,(65,45)) ; level_2_11=pygame.transform.scale(level_2_brick_10_11,(65,45)) ; level_2_7=pygame.transform.scale(level_2_brick_6_7,(65,45))
level_2_36=pygame.transform.scale(level_2_brick_15_36,(65,45)) ; level_2_37=pygame.transform.scale(level_2_brick_16_37,(65,45)) ; level_2_22=pygame.transform.scale(level_2_platform_1_22,(65,45)) ; level_2_23=pygame.transform.scale(level_2_platform_2_23,(65,45))
level_2_24=pygame.transform.scale(level_2_platform_3_24,(65,45)) ; level_2_25=pygame.transform.scale(level_2_platform_4_25,(65,45)) ; level_2_5=pygame.transform.scale(level_2_brick_4_5,(65,45)) ; level_2_6=pygame.transform.scale(level_2_brick_5_6,(65,45)) ; level_2_34=pygame.transform.scale(level_2_brick_1_34,(65,45)) ; level_2_35=pygame.transform.scale(level_2_brick_2_35,(65,45))
level_2_19=pygame.transform.scale(level_2_carpet_2_19,(65,45)) ; level_2_20=pygame.transform.scale(level_2_carpet_3_20,(65,45)) ; level_2_1=pygame.transform.scale(level_2_blank_1,(65,45)) ; level_2_12=pygame.transform.scale(level_2_brick_11_12,(65,45)) ; level_2_10=pygame.transform.scale(level_2_brick_9_10,(65,45))
level_2_15=pygame.transform.scale(level_2_floor_2_15,(65,45)) ; level_2_16=pygame.transform.scale(level_2_floor_3_16,(65,45)) ; level_2_17=pygame.transform.scale(level_2_floor_right,(65,45)) ; level_2_14=pygame.transform.scale(level_2_floor_left,(65,45))
level_2_32=pygame.transform.scale(level_2_carpet_transition_left,(65,45)) ; level_2_33=pygame.transform.scale(level_2_carpet_transition_right,(65,45)) ; level_2_26=pygame.transform.scale(level_2_stair_down,(65,45)) ; level_2_27=pygame.transform.scale(level_2_stair_up,(65,45))

level_2_dec_1=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\bookshelf_1.png")
level_2_dec_2=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\bookshelf_2.png")

level_2_bag_2=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\bag_2.png")

level_2_table=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\table_noshadow.png")
level_2_crate=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\crate_1.png")

level_2_crate_damage=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\crate_1_damaged.png")
level_2_books=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\books.png")

level_2_bag=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\bag_1.png")
level_2_flag=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\flag_red.png")

level_2_potion_1=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\potion_1.png")
level_2_potion_2=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\potions_2.png")


level_2_dec_1=pygame.transform.scale(level_2_dec_1,(90,130))
level_2_dec_2=pygame.transform.scale(level_2_dec_2,(90,130))

level_2_table=pygame.transform.scale(level_2_table,(50,30))
level_2_crate=pygame.transform.scale(level_2_crate,(40,50))

level_2_crate_damage=pygame.transform.scale(level_2_crate_damage,(40,50))
level_2_books=pygame.transform.scale(level_2_books,(30,30))

level_2_bag=pygame.transform.scale(level_2_bag,(30,30))
level_2_bag_2=pygame.transform.scale(level_2_bag_2,(30,30))
level_2_flag=pygame.transform.scale(level_2_flag,(80,120))

level_2_potion_1=pygame.transform.scale(level_2_potion_1,(20,30))
level_2_potion_2=pygame.transform.scale(level_2_potion_2,(20,30))

level_2_torch_1=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\Animated Decorations\torch_big\torch_big_1.png")
level_2_torch_2=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\Animated Decorations\torch_big\torch_big_2.png")
level_2_torch_3=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\Animated Decorations\torch_big\torch_big_3.png")
level_2_torch_4=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\Animated Decorations\torch_big\torch_big_4.png")
level_2_torch_5=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\Animated Decorations\torch_big\torch_big_5.png")
level_2_torch_1_bg=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\Animated Decorations\torch_big\torch_big_background.png")

level_2_fixture_1=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\Animated Decorations\candelabrum_tall\candelabrum_tall_1.png")
level_2_fixture_2=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\Animated Decorations\candelabrum_tall\candelabrum_tall_2.png")
level_2_fixture_3=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\Animated Decorations\candelabrum_tall\candelabrum_tall_3.png")
level_2_fixture_4=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\Animated Decorations\candelabrum_tall\candelabrum_tall_4.png")
level_2_fixture_5=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\Animated Decorations\candelabrum_tall\candelabrum_tall_5.png")
level_2_fixture_6=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\Animated Decorations\candelabrum_tall\candelabrum_tall_5.png")

level_2_candle_1=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\Animated Decorations\candle_1\candle_1_1.png")
level_2_candle_2=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\Animated Decorations\candle_1\candle_1_2.png")
level_2_candle_3=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\Animated Decorations\candle_1\candle_1_3.png")
level_2_candle_4=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\Animated Decorations\candle_1\candle_1_4.png")
level_2_candle_5=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\Animated Decorations\candle_1\candle_1_5.png")
level_2_candle_6=pygame.image.load(r"A_Wit's_End\Level 2_Tileset\Medieval_Castle_Asset_Pack\Decorations\Animated Decorations\candle_1\candle_1_6.png")

level_2_torch=[level_2_torch_1,level_2_torch_2,level_2_torch_3,level_2_torch_4,level_2_torch_5]
level_2_fixture=[level_2_fixture_1,level_2_fixture_2,level_2_fixture_3,level_2_fixture_4,level_2_fixture_5,level_2_fixture_6]
level_2_candle=[level_2_candle_1,level_2_candle_2,level_2_candle_3,level_2_candle_4,level_2_candle_5,level_2_candle_6]

level_2_bg_list=[] ; level_2_dec_list=[] ; level_2_item_list=[] ; level_2_dec_number=[0] ; level_2_animated_item_list=[]
list_2_bg_y_pos=[0,0,-550,-550,-550,-550,-550,-550,-550,0,0,-550]

level_2_passive_condition=True ; level_2_blur_list=[0] ; level_2_blur_list_2=[300] ; level_2_part_2=False

level_2_dialogue_list_part_1_length=[0] ; level_2_dialogue_part_one_once=False

level_3_bg_1=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\background\background_layer_1.png"); level_3_bg_1=pygame.transform.scale(level_3_bg_1,(SCREEN_WIDTH,SCREEN_HEIGHT))
level_3_bg_2=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\background\background_layer_2.png"); level_3_bg_2=pygame.transform.scale(level_3_bg_2,(SCREEN_WIDTH,SCREEN_HEIGHT))

tile_level_1=[] ; tile_level_1_rect=[]

file_1=open(r"A_Wit's_End\Level_1_Tileset\level_1_tile_set.txt","r") 

data_1=file_1.readlines()

list_data_1=[] 

for i in data_1:
    if i[-1]=="\n": list_data_1.append(i[:-1])
    else: list_data_1.append(i)
        
for idx,num in enumerate(list_data_1): tile_level_1.append(list_data_1[idx].split(","))
    
file_2=open(r"A_Wit's_End\Level 2_Tileset\level_2_tile_set.txt","r")

data_2=file_2.readlines()

tile_level_2=[] ; tile_level_2_rect=[]

list_data_2=[] 

for i in data_2:
    if i[-1]=="\n": list_data_2.append(i[:-1])
    else: list_data_2.append(i)
        
for idx,num in enumerate(list_data_2): tile_level_2.append(list_data_2[idx].split(","))
    
tile_level_1_ground=pygame.image.load(r"A_Wit's_End\Level_1_Tileset\GothicVania-town-files\GothicVania-town-files\PNG\environment\layers\sliced-tileset\ground.png") ; tile_level_1_ground=pygame.transform.scale(tile_level_1_ground,(65,45))

tile_level_1_dirt=pygame.transform.flip(tile_level_1_ground,False,True)

mouse_button_left_image=pygame.image.load(r"A_Wit's_End\Menu Design\Buttons Pack\Buttons Pack\MOUSE\MOUSEBUTTONLEFT.png")
mouse_button_left_image=pygame.transform.scale(mouse_button_left_image,(40,40))

camera_x_y_bg=[0,0] ; camera_x_y=[100,0] 

level_screen=False ; level_1=False ; level_2=False ; level_3=False ; level_4=False ; change_dialogue=False ; dialogue_start_condition=False ; change_dialogue_cond_1=False ;  end_dialogue=False
level_1_dialogue_part_two=False ; level_one_x_border=False ; dialogue_move_condition=False ; level_one_dialogue_part_three=False ; end_level_1_dialogue=False ; level_win=False ; win_blur=[0]
level_2_dialogue_part_one=False ; level_2_dialogue_part_two=False ; level_2_dialogue_once_two=False ; level_2_tile_index=[] ; level_2_part_2_boss_dialogue=False; level_2_dialogue_part_two_once=False

player_x=[100] ; player_x_movement=[0]
player_y=[600] ; player_y_movement=[0] #585

player_rect=pygame.Rect(player_x[0],player_y[0],45,48)

jump=False ; jump_condition=False ; player_idle_right=True ; player_idle_left=False ; attack=False ; crouch=False ; attack_air=False

health_icon=pygame.image.load(r"A_Wit's_End\Player\health\health_icon.png")
health_icon=pygame.transform.scale(health_icon,(25,25))

defeat_blur=[0]


#PLAYER SPRITES 

player_icon=pygame.image.load(r"A_Wit's_End\Player\Icon\idle_1.png")
player_icon=pygame.transform.scale(player_icon,(100,100))

player_idle_1=pygame.image.load(r"A_Wit's_End\Player\Idle\idle_1.png") ; player_idle_2=pygame.image.load(r"A_Wit's_End\Player\Idle\idle_2.png")
player_idle_3=pygame.image.load(r"A_Wit's_End\Player\Idle\idle_3.png") ; player_idle_4=pygame.image.load(r"A_Wit's_End\Player\Idle\idle_4.png")
player_idle_5=pygame.image.load(r"A_Wit's_End\Player\Idle\idle_5.png") ; player_idle_6=pygame.image.load(r"A_Wit's_End\Player\Idle\idle_6.png")
player_idle_7=pygame.image.load(r"A_Wit's_End\Player\Idle\idle_7.png") ; player_idle_8=pygame.image.load(r"A_Wit's_End\Player\Idle\idle_8.png")
player_idle_1=pygame.transform.scale(player_idle_1,(35,60)) ; player_idle_2=pygame.transform.scale(player_idle_2,(35,60)) ; player_idle_3=pygame.transform.scale(player_idle_3,(35,60)) ;  player_idle_4=pygame.transform.scale(player_idle_4,(35,60)) 
player_idle_5=pygame.transform.scale(player_idle_5,(35,60)) ; player_idle_6=pygame.transform.scale(player_idle_6,(35,60))  ; player_idle_7=pygame.transform.scale(player_idle_7,(35,60)) ; player_idle_8=pygame.transform.scale(player_idle_8,(35,60))
player_idle_flip_1=pygame.transform.flip(player_idle_1,True,False) ; player_idle_flip_2=pygame.transform.flip(player_idle_2,True,False) ; player_idle_flip_3=pygame.transform.flip(player_idle_3,True,False) ; player_idle_flip_4=pygame.transform.flip(player_idle_4,True,False)
player_idle_flip_5=pygame.transform.flip(player_idle_5,True,False) ; player_idle_flip_6=pygame.transform.flip(player_idle_6,True,False) ; player_idle_flip_7=pygame.transform.flip(player_idle_7,True,False) ; player_idle_flip_8=pygame.transform.flip(player_idle_8,True,False)

player_idle=[player_idle_1,player_idle_2,player_idle_3,player_idle_4,player_idle_5,player_idle_6,
             player_idle_7,player_idle_8]
player_idle_flip=[player_idle_flip_1,player_idle_flip_2,player_idle_flip_3,player_idle_flip_4,
                  player_idle_flip_5,player_idle_flip_6,player_idle_flip_7,player_idle_flip_8]

player_run_1=pygame.image.load(r"A_Wit's_End\Player\Running\run_1.png") ; player_run_2=pygame.image.load(r"A_Wit's_End\Player\Running\run_2.png")
player_run_3=pygame.image.load(r"A_Wit's_End\Player\Running\run_3.png") ; player_run_4=pygame.image.load(r"A_Wit's_End\Player\Running\run_4.png")
player_run_5=pygame.image.load(r"A_Wit's_End\Player\Running\run_5.png") ; player_run_6=pygame.image.load(r"A_Wit's_End\Player\Running\run_6.png")
player_run_7=pygame.image.load(r"A_Wit's_End\Player\Running\run_7.png") ; player_run_8=pygame.image.load(r"A_Wit's_End\Player\Running\run_8.png")
player_run_1=pygame.transform.scale(player_run_1,(35,60)) ; player_run_2=pygame.transform.scale(player_run_2,(35,60)) ; player_run_3=pygame.transform.scale(player_run_3,(35,60)) ; player_run_4=pygame.transform.scale(player_run_4,(35,60))
player_run_5=pygame.transform.scale(player_run_5,(35,60)) ; player_run_6=pygame.transform.scale(player_run_6,(35,60)) ; player_run_7=pygame.transform.scale(player_run_7,(35,60)) ; player_run_8=pygame.transform.scale(player_run_8,(35,60))
player_run_1_flip=pygame.transform.flip(player_run_1,True,False) ; player_run_2_flip=pygame.transform.flip(player_run_2,True,False) ; player_run_3_flip=pygame.transform.flip(player_run_3,True,False)
player_run_4_flip=pygame.transform.flip(player_run_4,True,False) ; player_run_5_flip=pygame.transform.flip(player_run_5,True,False) ; player_run_6_flip=pygame.transform.flip(player_run_6,True,False)
player_run_7_flip=pygame.transform.flip(player_run_7,True,False) ; player_run_8_flip=pygame.transform.flip(player_run_8,True,False)

player_run=[player_run_1,player_run_2,player_run_3,player_run_4,player_run_5,player_run_6,player_run_7,player_run_8]
player_run_flip=[player_run_1_flip,player_run_2_flip,player_run_3_flip,player_run_4_flip,player_run_5_flip,player_run_6_flip,player_run_7_flip,player_run_8_flip]

player_jump_1=pygame.image.load(r"A_Wit's_End\Player\Jumping\jump_1.png") ; player_jump_2=pygame.image.load(r"A_Wit's_End\Player\Jumping\jump_2.png") ; player_jump_3=pygame.image.load(r"A_Wit's_End\Player\Jumping\jump_3.png")
player_jump_4=pygame.image.load(r"A_Wit's_End\Player\Jumping\jump_4.png") ; player_jump_5=pygame.image.load(r"A_Wit's_End\Player\Jumping\jump_5.png") ; player_jump_6=pygame.image.load(r"A_Wit's_End\Player\Jumping\jump_6.png")
player_jump_7=pygame.image.load(r"A_Wit's_End\Player\Jumping\jump_7.png") ; player_jump_8=pygame.image.load(r"A_Wit's_End\Player\Jumping\jump_8.png")
player_jump_1=pygame.transform.scale(player_jump_1,(35,60)) ; player_jump_2=pygame.transform.scale(player_jump_2,(35,60)) ; player_jump_3=pygame.transform.scale(player_jump_3,(35,60)) ; player_jump_4=pygame.transform.scale(player_jump_4,(35,60))
player_jump_5=pygame.transform.scale(player_jump_5,(35,60)) ; player_jump_6=pygame.transform.scale(player_jump_6,(35,60)) ; player_jump_7=pygame.transform.scale(player_jump_7,(35,60)) ; player_jump_8=pygame.transform.scale(player_jump_8,(35,60))
player_jump_1_flip=pygame.transform.flip(player_jump_1,True,False) ; player_jump_2_flip=pygame.transform.flip(player_jump_2,True,False) ; player_jump_3_flip=pygame.transform.flip(player_jump_3,True,False) ; player_jump_4_flip=pygame.transform.flip(player_jump_4,True,False)
player_jump_5_flip=pygame.transform.flip(player_jump_5,True,False) ; player_jump_6_flip=pygame.transform.flip(player_jump_6,True,False) ; player_jump_7_flip=pygame.transform.flip(player_jump_7,True,False) ; player_jump_8_flip=pygame.transform.flip(player_jump_8,True,False)

player_jump=[player_jump_1,player_jump_2,player_jump_3,player_jump_4,player_jump_5,player_jump_6,player_jump_7,player_jump_8]
player_jump_flip=[player_jump_1_flip,player_jump_2_flip,player_jump_3_flip,player_jump_4_flip,player_jump_5_flip,player_jump_6_flip,player_jump_7_flip,player_jump_8_flip]

player_attack_type_1_1=pygame.image.load(r"A_Wit's_End\Player\attack_1\attack_4.png")  ; player_attack_type_1_2=pygame.image.load(r"A_Wit's_End\Player\attack_1\attack_5.png") 
player_attack_type_1_3=pygame.image.load(r"A_Wit's_End\Player\attack_1\attack_6.png")  ; player_attack_type_1_4=pygame.image.load(r"A_Wit's_End\Player\attack_1\attack_7.png")
player_attack_type_1_1=pygame.transform.scale(player_attack_type_1_1,(35,60)) ; player_attack_type_1_2=pygame.transform.scale(player_attack_type_1_2,(35,60))  ; player_attack_type_1_3=pygame.transform.scale(player_attack_type_1_3,(35,60))  ; player_attack_type_1_4=pygame.transform.scale(player_attack_type_1_4,(35,60))
player_attack_type_1_1_flip=pygame.transform.flip(player_attack_type_1_1,True,False) ; player_attack_type_1_2_flip=pygame.transform.flip(player_attack_type_1_2,True,False)  ; player_attack_type_1_3_flip=pygame.transform.flip(player_attack_type_1_3,True,False)  ; player_attack_type_1_4_flip=pygame.transform.flip(player_attack_type_1_4,True,False)
player_attack_type_2_1=pygame.image.load(r"A_Wit's_End\Player\attack_2\attack_4.png")  ; player_attack_type_2_2=pygame.image.load(r"A_Wit's_End\Player\attack_2\attack_5.png")  ; player_attack_type_2_3=pygame.image.load(r"A_Wit's_End\Player\attack_2\attack_6.png")
player_attack_type_2_1=pygame.transform.scale(player_attack_type_2_1,(35,60)) ; player_attack_type_2_2=pygame.transform.scale(player_attack_type_2_2,(35,60))  ; player_attack_type_2_3=pygame.transform.scale(player_attack_type_2_3,(35,60))
player_attack_type_2_1_flip=pygame.transform.flip(player_attack_type_2_1,True,False)  ; player_attack_type_2_2_flip=pygame.transform.flip(player_attack_type_2_2,True,False)  ; player_attack_type_2_3_flip=pygame.transform.flip(player_attack_type_2_3,True,False)
player_attack_type_3_1=pygame.image.load(r"A_Wit's_End\Player\attack_3\attack_4.png") ; player_attack_type_3_2=pygame.image.load(r"A_Wit's_End\Player\attack_3\attack_5.png")  
player_attack_type_3_3=pygame.image.load(r"A_Wit's_End\Player\attack_3\attack_6.png")  ; player_attack_type_3_4=pygame.image.load(r"A_Wit's_End\Player\attack_3\attack_7.png")
player_attack_type_3_1=pygame.transform.scale(player_attack_type_3_1,(35,60))  ; player_attack_type_3_2=pygame.transform.scale(player_attack_type_3_2,(35,60))  ; player_attack_type_3_3=pygame.transform.scale(player_attack_type_3_3,(35,60))  ; player_attack_type_3_4=pygame.transform.scale(player_attack_type_3_4,(35,60))
player_attack_type_3_1_flip=pygame.transform.flip(player_attack_type_3_1,True,False)  ; player_attack_type_3_2_flip=pygame.transform.flip(player_attack_type_3_2,True,False)  ; player_attack_type_3_3_flip=pygame.transform.flip(player_attack_type_3_3,True,False)  ; player_attack_type_3_4_flip=pygame.transform.flip(player_attack_type_3_4,True,False)
player_attack_type_4_1=pygame.image.load(r"A_Wit's_End\Player\attack_4\attack_4.png")  ; player_attack_type_4_2=pygame.image.load(r"A_Wit's_End\Player\attack_4\attack_5.png")  ; player_attack_type_4_3=pygame.image.load(r"A_Wit's_End\Player\attack_4\attack_6.png")
player_attack_type_4_4=pygame.image.load(r"A_Wit's_End\Player\attack_4\attack_7.png")  ; player_attack_type_4_5=pygame.image.load(r"A_Wit's_End\Player\attack_4\attack_8.png")  ; player_attack_type_4_6=pygame.image.load(r"A_Wit's_End\Player\attack_4\attack_9.png")
player_attack_type_4_1=pygame.transform.scale(player_attack_type_4_1,(35,60)) ; player_attack_type_4_2=pygame.transform.scale(player_attack_type_4_2,(35,60))  ; player_attack_type_4_3=pygame.transform.scale(player_attack_type_4_3,(35,60)) 
player_attack_type_4_4=pygame.transform.scale(player_attack_type_4_4,(35,60))  ; player_attack_type_4_5=pygame.transform.scale(player_attack_type_4_5,(35,60))  ; player_attack_type_4_6=pygame.transform.scale(player_attack_type_4_6,(35,60))
player_attack_type_4_1_flip=pygame.transform.flip(player_attack_type_4_1,True,False)  ; player_attack_type_4_2_flip=pygame.transform.flip(player_attack_type_4_2,True,False)  ; player_attack_type_4_3_flip=pygame.transform.flip(player_attack_type_4_3,True,False)
player_attack_type_4_4_flip=pygame.transform.flip(player_attack_type_4_4,True,False)  ; player_attack_type_4_5_flip=pygame.transform.flip(player_attack_type_4_5,True,False)  ; player_attack_type_4_6_flip=pygame.transform.flip(player_attack_type_4_6,True,False)

player_attack_type_1=[player_attack_type_1_1,player_attack_type_1_2,player_attack_type_1_3,player_attack_type_1_4]
player_attack_type_1_flip=[player_attack_type_1_1_flip,player_attack_type_1_2_flip,player_attack_type_1_3_flip,player_attack_type_1_4_flip]
player_attack_type_2=[player_attack_type_2_1,player_attack_type_2_2,player_attack_type_2_3]
player_attack_type_2_flip=[player_attack_type_2_1_flip,player_attack_type_2_2_flip,player_attack_type_2_3_flip]
player_attack_type_3=[player_attack_type_3_1,player_attack_type_3_2,player_attack_type_3_3,player_attack_type_3_4]
player_attack_type_3_flip=[player_attack_type_3_1_flip,player_attack_type_3_2_flip,player_attack_type_3_3_flip,player_attack_type_3_4_flip]
player_attack_type_4=[player_attack_type_4_1,player_attack_type_4_2,player_attack_type_4_3,player_attack_type_4_4,player_attack_type_4_5,player_attack_type_4_6]
player_attack_type_4_flip=[player_attack_type_4_1_flip,player_attack_type_4_2_flip,player_attack_type_4_3_flip,player_attack_type_4_4_flip,player_attack_type_4_5_flip,player_attack_type_4_6_flip]

attack_jump_1=pygame.image.load(r"A_Wit's_End\Player\attack_jump\attack_jump_1.png") ; attack_jump_2=pygame.image.load(r"A_Wit's_End\Player\attack_jump\attack_jump_2.png")  ; attack_jump_3=pygame.image.load(r"A_Wit's_End\Player\attack_jump\attack_jump_3.png")  ; attack_jump_4=pygame.image.load(r"A_Wit's_End\Player\attack_jump\attack_jump_4.png") 
attack_jump_5=pygame.image.load(r"A_Wit's_End\Player\attack_jump\attack_jump_5.png")  ; attack_jump_6=pygame.image.load(r"A_Wit's_End\Player\attack_jump\attack_jump_6.png")  ; attack_jump_7=pygame.image.load(r"A_Wit's_End\Player\attack_jump\attack_jump_7.png") 
attack_jump_1=pygame.transform.scale(attack_jump_1,(35,60)) ; attack_jump_2=pygame.transform.scale(attack_jump_2,(35,60)) ; attack_jump_3=pygame.transform.scale(attack_jump_3,(35,60)) ; attack_jump_4=pygame.transform.scale(attack_jump_4,(35,60))
attack_jump_5=pygame.transform.scale(attack_jump_5,(35,60)) ; attack_jump_6=pygame.transform.scale(attack_jump_6,(35,60)) ; attack_jump_7=pygame.transform.scale(attack_jump_7,(35,60))
attack_jump_1_flip=pygame.transform.flip(attack_jump_1,True,False) ; attack_jump_2_flip=pygame.transform.flip(attack_jump_2,True,False)  ; attack_jump_3_flip=pygame.transform.flip(attack_jump_3,True,False) ; attack_jump_4_flip=pygame.transform.flip(attack_jump_4,True,False) 
attack_jump_5_flip=pygame.transform.flip(attack_jump_5,True,False) ; attack_jump_6_flip=pygame.transform.flip(attack_jump_6,True,False) ; attack_jump_7_flip=pygame.transform.flip(attack_jump_7,True,False)

attack_jump=[attack_jump_1,attack_jump_2,attack_jump_3,attack_jump_4,attack_jump_5,attack_jump_6,attack_jump_7]
attack_jump_flip=[attack_jump_1_flip,attack_jump_2_flip,attack_jump_3_flip,attack_jump_4_flip,attack_jump_5_flip,attack_jump_6_flip,attack_jump_7_flip]

player_fallen_1=pygame.image.load(r"A_Wit's_End\Player\fallen\fallen_0.png")  ; player_fallen_2=pygame.image.load(r"A_Wit's_End\Player\fallen\fallen_1.png") ; player_fallen_3=pygame.image.load(r"A_Wit's_End\Player\fallen\fallen_2.png")  ; player_fallen_4=pygame.image.load(r"A_Wit's_End\Player\fallen\fallen_3.png")
player_fallen_1=pygame.transform.scale(player_fallen_1,(35,60))  ; player_fallen_2=pygame.transform.scale(player_fallen_2,(35,60))  ; player_fallen_3=pygame.transform.scale(player_fallen_3,(35,60))  ; player_fallen_4=pygame.transform.scale(player_fallen_4,(35,20))
player_fallen_flip_1=pygame.transform.flip(player_fallen_1,True,False) ; player_fallen_flip_2=pygame.transform.flip(player_fallen_2,True,False)  ; player_fallen_flip_3=pygame.transform.flip(player_fallen_3,True,False)  ;player_fallen_flip_4=pygame.transform.flip(player_fallen_4,True,False)
player_fallen=[player_fallen_1,player_fallen_2,player_fallen_3,player_fallen_4]
player_fallen_flip=[player_fallen_flip_1,player_fallen_flip_2,player_fallen_flip_3,player_fallen_flip_4]
 
player_idle_number=[0] ; player_run_number=[0] ; player_jump_number=[0] ; player_jump_length=[0] ; player_attack_number=[0] ; player_attack_jump_number=[0] ; player_fallen_number=[0]
attack_type=[4] ; player_current_health=[1000] ; player_death=False ; player_death_final=False ; reset_enemy_position=False ; attack_done=False


#ENEMY 1 KINGHT SPRITES

enemy_one_icon=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\Icon\Icon.png")
enemy_one_icon=pygame.transform.scale(enemy_one_icon,(100,100))

enemy_1_idle_1=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\Idle\Idle_1 (1).png") ; enemy_1_idle_2=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\Idle\Idle_2 (1).png") ; enemy_1_idle_3=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\Idle\Idle_3 (1).png")
enemy_1_idle_4=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\Idle\Idle_4 (1).png") ; enemy_1_idle_5=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\Idle\Idle_5 (1).png") ; enemy_1_idle_6=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\Idle\Idle_6 (1).png")
enemy_1_idle_7=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\Idle\Idle_7 (1).png") ; enemy_1_idle_8=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\Idle\Idle_8 (1).png") ; enemy_1_idle_9=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\Idle\Idle_9.png")
enemy_1_idle_10=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\Idle\Idle_10.png") ; enemy_1_idle_11=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\Idle\Idle_11.png")
enemy_1_idle_1=pygame.transform.scale(enemy_1_idle_1,(55,60))  ; enemy_1_idle_2=pygame.transform.scale(enemy_1_idle_2,(55,60)) ; enemy_1_idle_3=pygame.transform.scale(enemy_1_idle_3,(55,60)) ; enemy_1_idle_4=pygame.transform.scale(enemy_1_idle_4,(55,60))  ; enemy_1_idle_5=pygame.transform.scale(enemy_1_idle_5,(55,60))
enemy_1_idle_6=pygame.transform.scale(enemy_1_idle_6,(55,60))  ;enemy_1_idle_7=pygame.transform.scale(enemy_1_idle_7,(55,60)) ; enemy_1_idle_8=pygame.transform.scale(enemy_1_idle_8,(55,60)) ; enemy_1_idle_9=pygame.transform.scale(enemy_1_idle_9,(55,60)) ; enemy_1_idle_10=pygame.transform.scale(enemy_1_idle_10,(55,60)) ; enemy_1_idle_11=pygame.transform.scale(enemy_1_idle_11,(55,60))
enemy_1_idle_1_flip=pygame.transform.flip(enemy_1_idle_1,True,False) ; enemy_1_idle_2_flip=pygame.transform.flip(enemy_1_idle_2,True,False) ; enemy_1_idle_3_flip=pygame.transform.flip(enemy_1_idle_3,True,False) ; enemy_1_idle_4_flip=pygame.transform.flip(enemy_1_idle_4,True,False) ; enemy_1_idle_5_flip=pygame.transform.flip(enemy_1_idle_5,True,False)
enemy_1_idle_6_flip=pygame.transform.flip(enemy_1_idle_6,True,False) ; enemy_1_idle_7_flip=pygame.transform.flip(enemy_1_idle_7,True,False) ; enemy_1_idle_8_flip=pygame.transform.flip(enemy_1_idle_8,True,False) ; enemy_1_idle_9_flip=pygame.transform.flip(enemy_1_idle_9,True,False) ; enemy_1_idle_10_flip=pygame.transform.flip(enemy_1_idle_10,True,False) ; enemy_1_idle_11_flip=pygame.transform.flip(enemy_1_idle_11,True,False)
enemy_1_idle=[enemy_1_idle_1,enemy_1_idle_2,enemy_1_idle_3,enemy_1_idle_4,enemy_1_idle_5,enemy_1_idle_6,enemy_1_idle_7,enemy_1_idle_8,enemy_1_idle_9,
              enemy_1_idle_10,enemy_1_idle_11]
enemy_1_idle_flip=[enemy_1_idle_1_flip,enemy_1_idle_2_flip,enemy_1_idle_3_flip,enemy_1_idle_4_flip,enemy_1_idle_5_flip,enemy_1_idle_6_flip,enemy_1_idle_7_flip,
                   enemy_1_idle_8_flip,enemy_1_idle_9_flip,enemy_1_idle_10_flip,enemy_1_idle_11_flip]

enemy_1_walk_1=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\Run\Knight_Walk_1 (1).png")  ; enemy_1_walk_2=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\Run\Knight_Walk_2 (1).png")  ; enemy_1_walk_3=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\Run\Knight_Walk_3 (1).png")
enemy_1_walk_4=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\Run\Knight_Walk_4 (1).png")  ; enemy_1_walk_5=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\Run\Knight_Walk_5 (1).png")  ; enemy_1_walk_6=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\Run\Knight_Walk_6 (1).png")
enemy_1_walk_7=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\Run\Knight_Walk_7 (1).png") ; enemy_1_walk_8=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\Run\Knight_Walk_8 (1).png")
enemy_1_walk_1=pygame.transform.scale(enemy_1_walk_1,(55,60)) ; enemy_1_walk_2=pygame.transform.scale(enemy_1_walk_2,(55,60)) ; enemy_1_walk_3=pygame.transform.scale(enemy_1_walk_3,(55,60)) ; enemy_1_walk_4=pygame.transform.scale(enemy_1_walk_4,(55,60))
enemy_1_walk_5=pygame.transform.scale(enemy_1_walk_5,(55,60)) ; enemy_1_walk_6=pygame.transform.scale(enemy_1_walk_6,(55,60)) ; enemy_1_walk_7=pygame.transform.scale(enemy_1_walk_7,(55,60)) ; enemy_1_walk_8=pygame.transform.scale(enemy_1_walk_8,(55,60))
enemy_1_walk_1_flip=pygame.transform.flip(enemy_1_walk_1,True,False) ; enemy_1_walk_2_flip=pygame.transform.flip(enemy_1_walk_2,True,False) ; enemy_1_walk_3_flip=pygame.transform.flip(enemy_1_walk_3,True,False) ; enemy_1_walk_4_flip=pygame.transform.flip(enemy_1_walk_4,True,False)
enemy_1_walk_5_flip=pygame.transform.flip(enemy_1_walk_5,True,False) ; enemy_1_walk_6_flip=pygame.transform.flip(enemy_1_walk_6,True,False) ; enemy_1_walk_7_flip=pygame.transform.flip(enemy_1_walk_7,True,False) ; enemy_1_walk_8_flip=pygame.transform.flip(enemy_1_walk_8,True,False)
enemy_1_walk=[enemy_1_walk_1,enemy_1_walk_2,enemy_1_walk_3,enemy_1_walk_4,enemy_1_walk_5,enemy_1_walk_6,enemy_1_walk_7,enemy_1_walk_8]
enemy_1_walk_flip=[enemy_1_walk_1_flip,enemy_1_walk_2_flip,enemy_1_walk_3_flip,enemy_1_walk_4_flip,enemy_1_walk_5_flip,enemy_1_walk_6_flip,
                   enemy_1_walk_7_flip,enemy_1_walk_8_flip]


enemy_1_fall_1=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\fallen\fallen_1.png") ; enemy_1_fall_2=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\fallen\fallen_2.png") ; enemy_1_fall_3=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\fallen\fallen_3.png") ; enemy_1_fall_4=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\fallen\fallen_4.png")
enemy_1_fall_5=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\fallen\fallen_5.png") ; enemy_1_fall_6=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\fallen\fallen_6.png") ; enemy_1_fall_7=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\fallen\fallen_7.png")
enemy_1_fall_8=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\fallen\fallen_8.png") ; enemy_1_fall_9=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\fallen\fallen_9.png")
enemy_1_fall_1=pygame.transform.scale(enemy_1_fall_1,(55,60)) ; enemy_1_fall_2=pygame.transform.scale(enemy_1_fall_2,(55,60)) ; enemy_1_fall_3=pygame.transform.scale(enemy_1_fall_3,(55,60)) ; enemy_1_fall_4=pygame.transform.scale(enemy_1_fall_4,(55,60)) ; enemy_1_fall_5=pygame.transform.scale(enemy_1_fall_5,(55,60))
enemy_1_fall_6=pygame.transform.scale(enemy_1_fall_6,(55,60)) ; enemy_1_fall_7=pygame.transform.scale(enemy_1_fall_7,(55,60)) ; enemy_1_fall_8=pygame.transform.scale(enemy_1_fall_8,(55,60)) ; enemy_1_fall_9=pygame.transform.scale(enemy_1_fall_9,(55,25))
enemy_1_fall_flip_1=pygame.transform.flip(enemy_1_fall_1,True,False) ; enemy_1_fall_flip_2=pygame.transform.flip(enemy_1_fall_2,True,False) ; enemy_1_fall_flip_3=pygame.transform.flip(enemy_1_fall_3,True,False) ; enemy_1_fall_flip_4=pygame.transform.flip(enemy_1_fall_4,True,False)
enemy_1_fall_flip_5=pygame.transform.flip(enemy_1_fall_5,True,False) ; enemy_1_fall_flip_6=pygame.transform.flip(enemy_1_fall_6,True,False) ; enemy_1_fall_flip_7=pygame.transform.flip(enemy_1_fall_7,True,False) ; enemy_1_fall_flip_8=pygame.transform.flip(enemy_1_fall_8,True,False) ; enemy_1_fall_flip_9=pygame.transform.flip(enemy_1_fall_9,True,False)
enemy_1_fall=[enemy_1_fall_1,enemy_1_fall_2,enemy_1_fall_3,enemy_1_fall_4,enemy_1_fall_5,enemy_1_fall_6,enemy_1_fall_7,enemy_1_fall_8,enemy_1_fall_9]
enemy_1_fall_flip=[enemy_1_fall_flip_1,enemy_1_fall_flip_2,enemy_1_fall_flip_3,enemy_1_fall_flip_4,enemy_1_fall_flip_5,enemy_1_fall_flip_6,enemy_1_fall_flip_7,
                   enemy_1_fall_flip_8,enemy_1_fall_flip_9]


enemy_1_attack_1=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\attack\attack_1.png") ; enemy_1_attack_2=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\attack\attack_2.png") ; enemy_1_attack_3=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\attack\attack_3.png")
enemy_1_attack_4=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\attack\attack_4.png") ; enemy_1_attack_5=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\attack\attack_5.png") ; enemy_1_attack_6=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_1\attack\attack_6.png")
enemy_1_attack_1=pygame.transform.scale(enemy_1_attack_1,(55,70)) ; enemy_1_attack_2=pygame.transform.scale(enemy_1_attack_2,(55,70)) ; enemy_1_attack_3=pygame.transform.scale(enemy_1_attack_3,(55,70)) ; enemy_1_attack_4=pygame.transform.scale(enemy_1_attack_4,(55,70)) ; enemy_1_attack_5=pygame.transform.scale(enemy_1_attack_5,(55,70)) ; enemy_1_attack_6=pygame.transform.scale(enemy_1_attack_6,(55,70))
enemy_1_attack_flip_1=pygame.transform.flip(enemy_1_attack_1,True,False) ; enemy_1_attack_flip_2=pygame.transform.flip(enemy_1_attack_2,True,False) ; enemy_1_attack_flip_3=pygame.transform.flip(enemy_1_attack_3,True,False) ; enemy_1_attack_flip_4=pygame.transform.flip(enemy_1_attack_4,True,False) ; enemy_1_attack_flip_5=pygame.transform.flip(enemy_1_attack_5,True,False) ; enemy_1_attack_flip_6=pygame.transform.flip(enemy_1_attack_6,True,False)
enemy_1_attack=[enemy_1_attack_1,enemy_1_attack_2,enemy_1_attack_3,enemy_1_attack_4,enemy_1_attack_5,enemy_1_attack_6]
enemy_1_attack_flip=[enemy_1_attack_flip_1,enemy_1_attack_flip_2,enemy_1_attack_flip_3,enemy_1_attack_flip_4,enemy_1_attack_flip_5,enemy_1_attack_flip_6]

enemy_1_level_1_x=[300,900,1500,1700,3500,4400,5200,5500,5700,5800,5900] ; enemy_1_level_1_y=[575,575,575,575,575,575,575,575,575,575,575]
enemy_1_level_1_rect=[pygame.Rect(enemy_1_level_1_x[0],enemy_1_level_1_y[0],45,55),pygame.Rect(enemy_1_level_1_x[1],enemy_1_level_1_y[1],45,55),  #45
                      pygame.Rect(enemy_1_level_1_x[2],enemy_1_level_1_y[2],45,55),pygame.Rect(enemy_1_level_1_x[3],enemy_1_level_1_y[3],45,55),
                      pygame.Rect(enemy_1_level_1_x[4],enemy_1_level_1_y[4],45,55),pygame.Rect(enemy_1_level_1_x[5],enemy_1_level_1_y[5],45,55),
                      pygame.Rect(enemy_1_level_1_x[6],enemy_1_level_1_y[6],45,55),pygame.Rect(enemy_1_level_1_x[7],enemy_1_level_1_y[7],45,55),
                      pygame.Rect(enemy_1_level_1_x[8],enemy_1_level_1_y[8],45,55),pygame.Rect(enemy_1_level_1_x[9],enemy_1_level_1_y[9],45,55),
                      pygame.Rect(enemy_1_level_1_x[10],enemy_1_level_1_y[10],45,55)]
enemy_1_level_1_x_idle=[200,500,1400,1900] ; enemy_1_level_1_y_idle=[575,575,575,575]
enemy_1_level_1_rect_idle=[pygame.Rect(enemy_1_level_1_x_idle[0],enemy_1_level_1_y_idle[0],45,55),pygame.Rect(enemy_1_level_1_x_idle[1],enemy_1_level_1_y_idle[1],45,55),
                      pygame.Rect(enemy_1_level_1_x_idle[2],enemy_1_level_1_y_idle[2],45,55),pygame.Rect(enemy_1_level_1_x_idle[3],enemy_1_level_1_y_idle[3],45,55)]

enemy_type_1_level_1_x=enemy_1_level_1_x+enemy_1_level_1_x_idle
enemy_level_1_rect=enemy_1_level_1_rect+enemy_1_level_1_rect_idle

enemy_1_level_2_x=[700,800,900,1100,1400,1700,3200,3700] ; enemy_1_level_2_y=[575,575,575,575,575,575,575,575]

enemy_1_level_2_rect=[pygame.Rect(enemy_1_level_2_x[0],enemy_1_level_2_y[0],45,55),pygame.Rect(enemy_1_level_2_x[1],enemy_1_level_2_y[1],45,55),
                      pygame.Rect(enemy_1_level_2_x[2],enemy_1_level_2_y[2],45,55),pygame.Rect(enemy_1_level_2_x[3],enemy_1_level_2_y[3],45,55),
                      pygame.Rect(enemy_1_level_2_x[4],enemy_1_level_2_y[4],45,55),pygame.Rect(enemy_1_level_2_x[5],enemy_1_level_2_y[5],45,55),
                      pygame.Rect(enemy_1_level_2_x[6],enemy_1_level_2_y[6],45,55),pygame.Rect(enemy_1_level_2_x[7],enemy_1_level_2_y[7],45,55)]

enemy_1_walk_length=[0] ; enemy_1_idle_length=[0] ; level_1_enemy_fight_condition=False ; enemy_1_x_movement=[0] ; enemy_1_y_movement=[0] ; enemy_1_friendly_dialogue=False ; enemy_one_dialogue_list=[0] ; enemy_list_level_1=[]
enemy_1_attack_length=[0] ; enemy_1_distance_list=[] ; enemy_1_health_list=[] ; enemy_one_fall_number=[] ; enemy_one_fall_direction_set=[] ; enemy_list_level_2=[]

npc_walk_length=[random.randint(200,400),random.randint(200,400),random.randint(200,400),random.randint(200,400)] 
npc_direction_choice=[random.randint(1,2),random.randint(1,2),random.randint(1,2),random.randint(1,2),random.randint(1,2)]

#ENEMY TWO KNIGHT SPRITES

enemy_two_icon=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\icon.png") ; enemy_two_icon=pygame.transform.scale(enemy_two_icon,(120,100))

enemy_two_idle_1=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\ready_1.png") ; enemy_two_idle_2=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\ready_2.png") ; enemy_two_idle_3=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\ready_3.png")
enemy_two_idle_1=pygame.transform.scale(enemy_two_idle_1,(105,105))  ; enemy_two_idle_2=pygame.transform.scale(enemy_two_idle_2,(105,105)) ; enemy_two_idle_3=pygame.transform.scale(enemy_two_idle_3,(105,105))
enemy_two_idle_1_flip=pygame.transform.flip(enemy_two_idle_1,True,False) ; enemy_two_idle_2_flip=pygame.transform.flip(enemy_two_idle_2,True,False) ; enemy_two_idle_3_flip=pygame.transform.flip(enemy_two_idle_3,True,False)
enemy_two_idle=[enemy_two_idle_1,enemy_two_idle_2,enemy_two_idle_3] ; enemy_two_idle_flip=[enemy_two_idle_1_flip,enemy_two_idle_2_flip,enemy_two_idle_3_flip]

enemy_two_run_1=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\run_1.png") ; enemy_two_run_2=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\run_2.png") ; enemy_two_run_3=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\run_3.png")
enemy_two_run_4=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\run_4.png") ; enemy_two_run_5=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\run_5.png") ; enemy_two_run_6=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\run_6.png")
enemy_two_run_1=pygame.transform.scale(enemy_two_run_1,(105,105)) ; enemy_two_run_2=pygame.transform.scale(enemy_two_run_2,(105,105)) ; enemy_two_run_3=pygame.transform.scale(enemy_two_run_3,(105,105)) ; enemy_two_run_4=pygame.transform.scale(enemy_two_run_4,(105,105)) ; enemy_two_run_5=pygame.transform.scale(enemy_two_run_5,(105,105)) ; enemy_two_run_6=pygame.transform.scale(enemy_two_run_6,(105,105))
enemy_two_run_1_flip=pygame.transform.flip(enemy_two_run_1,True,False) ; enemy_two_run_2_flip=pygame.transform.flip(enemy_two_run_2,True,False) ; enemy_two_run_3_flip=pygame.transform.flip(enemy_two_run_3,True,False)
enemy_two_run_4_flip=pygame.transform.flip(enemy_two_run_4,True,False) ; enemy_two_run_5_flip=pygame.transform.flip(enemy_two_run_5,True,False) ; enemy_two_run_6_flip=pygame.transform.flip(enemy_two_run_6,True,False)
enemy_two_run=[enemy_two_run_1,enemy_two_run_2,enemy_two_run_3,enemy_two_run_4,enemy_two_run_5,enemy_two_run_6]
enemy_two_run_flip=[enemy_two_run_1_flip,enemy_two_run_2_flip,enemy_two_run_3_flip,enemy_two_run_4_flip,enemy_two_run_5_flip,enemy_two_run_6_flip]

enemy_two_attack_1_1=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\attack1_1.png") ; enemy_two_attack_1_2=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\attack1_2.png") ; enemy_two_attack_1_3=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\attack1_3.png")
enemy_two_attack_1_4=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\attack1_4.png") ; enemy_two_attack_1_5=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\attack1_5.png") ; enemy_two_attack_1_6=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\attack1_6.png")
enemy_two_attack_1_1=pygame.transform.scale(enemy_two_attack_1_1,(200,105*1.29)) ; enemy_two_attack_1_2=pygame.transform.scale(enemy_two_attack_1_2,(200,105*1.29))  ; enemy_two_attack_1_3=pygame.transform.scale(enemy_two_attack_1_3,(200,105*1.29))  ; enemy_two_attack_1_4=pygame.transform.scale(enemy_two_attack_1_4,(200,105*1.29))   ; enemy_two_attack_1_5=pygame.transform.scale(enemy_two_attack_1_5,(200,105*1.29))  ; enemy_two_attack_1_6=pygame.transform.scale(enemy_two_attack_1_6,(200,105*1.29)) 
enemy_two_attack_2_1=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\attack4_1.png")  ; enemy_two_attack_2_2=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\attack4_2.png")  ; enemy_two_attack_2_3=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\attack4_3.png") 
enemy_two_attack_2_4=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\attack4_4.png") ; enemy_two_attack_2_5=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\attack4_5.png") ; enemy_two_attack_2_6=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\attack4_6.png")
enemy_two_attack_2_1=pygame.transform.scale(enemy_two_attack_2_1,(200,105*1.29))  ; enemy_two_attack_2_2=pygame.transform.scale(enemy_two_attack_2_2,(200,105*1.29))  ; enemy_two_attack_2_3=pygame.transform.scale(enemy_two_attack_2_3,(200,105*1.29))  ; enemy_two_attack_2_4=pygame.transform.scale(enemy_two_attack_2_4,(200,105*1.29))  ; enemy_two_attack_2_5=pygame.transform.scale(enemy_two_attack_2_5,(200,105*1.29))  ; enemy_two_attack_2_6=pygame.transform.scale(enemy_two_attack_2_6,(200,105*1.29)) 
enemy_two_attack_1_flip_1=pygame.transform.flip(enemy_two_attack_1_1,True,False) ; enemy_two_attack_1_flip_2=pygame.transform.flip(enemy_two_attack_1_2,True,False) ; enemy_two_attack_1_flip_3=pygame.transform.flip(enemy_two_attack_1_3,True,False) ; enemy_two_attack_1_flip_4=pygame.transform.flip(enemy_two_attack_1_4,True,False) ; enemy_two_attack_1_flip_5=pygame.transform.flip(enemy_two_attack_1_5,True,False) ; enemy_two_attack_1_flip_6=pygame.transform.flip(enemy_two_attack_1_6,True,False)
enemy_two_attack_2_flip_1=pygame.transform.flip(enemy_two_attack_2_1,True,False) ; enemy_two_attack_2_flip_2=pygame.transform.flip(enemy_two_attack_2_2,True,False) ; enemy_two_attack_2_flip_3=pygame.transform.flip(enemy_two_attack_2_3,True,False)  ; enemy_two_attack_2_flip_4=pygame.transform.flip(enemy_two_attack_2_4,True,False) ; enemy_two_attack_2_flip_5=pygame.transform.flip(enemy_two_attack_2_5,True,False) ; enemy_two_attack_2_flip_6=pygame.transform.flip(enemy_two_attack_2_6,True,False)
enemy_two_attack_1=[enemy_two_attack_1_1,enemy_two_attack_1_2,enemy_two_attack_1_3,enemy_two_attack_1_4,enemy_two_attack_1_5,enemy_two_attack_1_6]
enemy_two_attack_2=[enemy_two_attack_2_1,enemy_two_attack_2_2,enemy_two_attack_2_3,enemy_two_attack_2_4,enemy_two_attack_2_5,enemy_two_attack_2_6]
enemy_two_attack_1_flip=[enemy_two_attack_1_flip_1,enemy_two_attack_1_flip_2,enemy_two_attack_1_flip_3,enemy_two_attack_1_flip_4,enemy_two_attack_1_flip_5,enemy_two_attack_1_flip_6]
enemy_two_attack_2_flip=[enemy_two_attack_2_flip_1,enemy_two_attack_2_flip_2,enemy_two_attack_2_flip_3,enemy_two_attack_2_flip_4,enemy_two_attack_2_flip_5,enemy_two_attack_2_flip_6]

enemy_two_fall_1=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\fall_back_1.png") ; enemy_two_fall_2=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\fall_back_2.png") ; enemy_two_fall_3=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\fall_back_3.png") ; enemy_two_fall_4=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\fall_back_4.png") ; enemy_two_fall_5=pygame.image.load(r"A_Wit's_End\Enemy_Knights\Knight_2\pack_loreon_char_free\sword_1\fall_back_5.png")
enemy_two_fall_1=pygame.transform.scale(enemy_two_fall_1,(105,105)) ; enemy_two_fall_2=pygame.transform.scale(enemy_two_fall_2,(105,105)) ; enemy_two_fall_3=pygame.transform.scale(enemy_two_fall_3,(105,105)) ; enemy_two_fall_4=pygame.transform.scale(enemy_two_fall_4,(105,105)) ; enemy_two_fall_5=pygame.transform.scale(enemy_two_fall_5,(105,105))
enemy_two_fall_flip_1=pygame.transform.flip(enemy_two_fall_1,True,False) ; enemy_two_fall_flip_2=pygame.transform.flip(enemy_two_fall_2,True,False) ; enemy_two_fall_flip_3=pygame.transform.flip(enemy_two_fall_3,True,False) ; enemy_two_fall_flip_4=pygame.transform.flip(enemy_two_fall_4,True,False) ; enemy_two_fall_flip_5=pygame.transform.flip(enemy_two_fall_5,True,False)
enemy_two_fall=[enemy_two_fall_1,enemy_two_fall_2,enemy_two_fall_3,enemy_two_fall_4,enemy_two_fall_5]
enemy_two_fall_flip=[enemy_two_fall_flip_1,enemy_two_fall_flip_2,enemy_two_fall_flip_3,enemy_two_fall_flip_4,enemy_two_fall_flip_5]
enemy_two_level_1_x=[2700,3000] ; enemy_two_level_1_y=[557,557]
enemy_two_level_1_rect=[pygame.Rect(enemy_two_level_1_x[0],enemy_two_level_1_y[0],45,55),pygame.Rect(enemy_two_level_1_x[1],enemy_two_level_1_y[1],45,55)] ; enemy_two_rect_list=[]
enemy_two_idle_number=[0] ; enemy_two_run_number=[0] ; enemy_two_x_movement=[] ; enemy_two_y_movement=[0,0] ; enemy_two_distance_list=[] ; enemy_two_attack_type=[1] ; enemy_two_attack_number=[]
enemy_two_fall_number=[] ; enemy_two_health=[] ; enemy_two_fall_direction_set=[]

#MAIN BOSS SPRITES

main_boss_icon=pygame.image.load(r"A_Wit's_End\Enemy_Boss_2\Icon\icon.png") ; main_boss_icon=pygame.transform.scale(main_boss_icon,(100,100))

main_boss_idle_1=pygame.image.load(r"A_Wit's_End\Enemy_Boss_2\Idle\idle_1.png") ; main_boss_idle_2=pygame.image.load(r"A_Wit's_End\Enemy_Boss_2\Idle\idle_2.png") ; main_boss_idle_3=pygame.image.load(r"A_Wit's_End\Enemy_Boss_2\Idle\idle_3.png")
main_boss_idle_4=pygame.image.load(r"A_Wit's_End\Enemy_Boss_2\Idle\idle_4.png") ; main_boss_idle_5=pygame.image.load(r"A_Wit's_End\Enemy_Boss_2\Idle\idle_5.png") ; main_boss_idle_6=pygame.image.load(r"A_Wit's_End\Enemy_Boss_2\Idle\idle_6.png")
main_boss_idle_7=pygame.image.load(r"A_Wit's_End\Enemy_Boss_2\Idle\idle_7.png") ; main_boss_idle_8=pygame.image.load(r"A_Wit's_End\Enemy_Boss_2\Idle\idle_8.png")
main_boss_idle_1=pygame.transform.scale(main_boss_idle_1,(55,65)) ; main_boss_idle_2=pygame.transform.scale(main_boss_idle_2,(55,65)) ; main_boss_idle_3=pygame.transform.scale(main_boss_idle_3,(55,65)) ; main_boss_idle_4=pygame.transform.scale(main_boss_idle_4,(55,65))
main_boss_idle_5=pygame.transform.scale(main_boss_idle_5,(55,65)) ; main_boss_idle_6=pygame.transform.scale(main_boss_idle_6,(55,65)) ; main_boss_idle_7=pygame.transform.scale(main_boss_idle_7,(55,65)) ; main_boss_idle_8=pygame.transform.scale(main_boss_idle_8,(55,65))
main_boss_idle_flip_1=pygame.transform.flip(main_boss_idle_1,True,False) ; main_boss_idle_flip_2=pygame.transform.flip(main_boss_idle_2,True,False) ; main_boss_idle_flip_3=pygame.transform.flip(main_boss_idle_3,True,False) ; main_boss_idle_flip_4=pygame.transform.flip(main_boss_idle_4,True,False)
main_boss_idle_flip_5=pygame.transform.flip(main_boss_idle_5,True,False) ; main_boss_idle_flip_6=pygame.transform.flip(main_boss_idle_6,True,False) ; main_boss_idle_flip_7=pygame.transform.flip(main_boss_idle_7,True,False) ; main_boss_idle_flip_8=pygame.transform.flip(main_boss_idle_8,True,False)
main_boss_idle=[main_boss_idle_1,main_boss_idle_2,main_boss_idle_3,main_boss_idle_4,main_boss_idle_5,main_boss_idle_6,main_boss_idle_7,main_boss_idle_8]
main_boss_idle_flip=[main_boss_idle_flip_1,main_boss_idle_flip_2,main_boss_idle_flip_3,main_boss_idle_flip_4,main_boss_idle_flip_5,main_boss_idle_flip_6,main_boss_idle_flip_7,main_boss_idle_flip_8]

main_boss_run_1=pygame.image.load(r"A_Wit's_End\Enemy_Boss_2\Run\run_1.png") ; main_boss_run_2=pygame.image.load(r"A_Wit's_End\Enemy_Boss_2\Run\run_2.png") ; main_boss_run_3=pygame.image.load(r"A_Wit's_End\Enemy_Boss_2\Run\run_3.png") ; main_boss_run_4=pygame.image.load(r"A_Wit's_End\Enemy_Boss_2\Run\run_4.png")
main_boss_run_5=pygame.image.load(r"A_Wit's_End\Enemy_Boss_2\Run\run_5.png") ; main_boss_run_6=pygame.image.load(r"A_Wit's_End\Enemy_Boss_2\Run\run_6.png") ; main_boss_run_7=pygame.image.load(r"A_Wit's_End\Enemy_Boss_2\Run\run_7.png") ; main_boss_run_8=pygame.image.load(r"A_Wit's_End\Enemy_Boss_2\Run\run_8.png")
main_boss_run_1=pygame.transform.scale(main_boss_run_1,(55,65)) ; main_boss_run_2=pygame.transform.scale(main_boss_run_2,(55,65)) ; main_boss_run_3=pygame.transform.scale(main_boss_run_3,(55,65)) ; main_boss_run_4=pygame.transform.scale(main_boss_run_4,(55,65))
main_boss_run_5=pygame.transform.scale(main_boss_run_5,(55,65)) ; main_boss_run_6=pygame.transform.scale(main_boss_run_6,(55,65)) ; main_boss_run_7=pygame.transform.scale(main_boss_run_7,(55,65)) ; main_boss_run_8=pygame.transform.scale(main_boss_run_8,(55,65))
main_boss_run_flip_1=pygame.transform.flip(main_boss_run_1,True,False) ; main_boss_run_flip_2=pygame.transform.flip(main_boss_run_2,True,False) ; main_boss_run_flip_3=pygame.transform.flip(main_boss_run_3,True,False) ; main_boss_run_flip_4=pygame.transform.flip(main_boss_run_4,True,False)
main_boss_run_flip_5=pygame.transform.flip(main_boss_run_5,True,False) ; main_boss_run_flip_6=pygame.transform.flip(main_boss_run_6,True,False) ; main_boss_run_flip_7=pygame.transform.flip(main_boss_run_7,True,False) ; main_boss_run_flip_8=pygame.transform.flip(main_boss_run_8,True,False)
main_boss_run=[main_boss_run_1,main_boss_run_2,main_boss_run_3,main_boss_run_4,main_boss_run_5,main_boss_run_6,main_boss_run_7,main_boss_run_8]
main_boss_run_flip=[main_boss_run_flip_1,main_boss_run_flip_2,main_boss_run_flip_3,main_boss_run_flip_4,main_boss_run_flip_5,main_boss_run_flip_6,main_boss_run_flip_7,main_boss_run_flip_8]

main_boss_idle_number=[0] ; main_boss_run_number=[0]

main_boss_level_1_x=[2850] ; main_boss_level_1_y=[577] ; main_boss_x_movement=[0] ; main_boss_y_movement=[0]

main_boss_rect_level_1=pygame.Rect(main_boss_level_1_x[0],main_boss_level_1_y[0],55,65)


general_boss_idle_1=pygame.image.load(r"A_Wit's_End\Level_2_General\Idle\sprite_1.png")
general_boss_idle_2=pygame.image.load(r"A_Wit's_End\Level_2_General\Idle\sprite_2.png")
general_boss_idle_3=pygame.image.load(r"A_Wit's_End\Level_2_General\Idle\sprite_3.png")
general_boss_idle_4=pygame.image.load(r"A_Wit's_End\Level_2_General\Idle\sprite_4.png")
general_boss_idle_5=pygame.image.load(r"A_Wit's_End\Level_2_General\Idle\sprite_5.png")
general_boss_idle_6=pygame.image.load(r"A_Wit's_End\Level_2_General\Idle\sprite_6.png")
general_boss_idle_7=pygame.image.load(r"A_Wit's_End\Level_2_General\Idle\sprite_7.png")
general_boss_idle_8=pygame.image.load(r"A_Wit's_End\Level_2_General\Idle\sprite_8.png")
general_boss_idle_9=pygame.image.load(r"A_Wit's_End\Level_2_General\Idle\sprite_9.png")

general_boss_idle_1=pygame.transform.scale(general_boss_idle_1,(55,60))
general_boss_idle_2=pygame.transform.scale(general_boss_idle_2,(55,60))
general_boss_idle_3=pygame.transform.scale(general_boss_idle_3,(55,60))
general_boss_idle_4=pygame.transform.scale(general_boss_idle_4,(55,60))
general_boss_idle_5=pygame.transform.scale(general_boss_idle_5,(55,60))
general_boss_idle_6=pygame.transform.scale(general_boss_idle_6,(55,60))
general_boss_idle_7=pygame.transform.scale(general_boss_idle_7,(55,60))
general_boss_idle_8=pygame.transform.scale(general_boss_idle_8,(55,60))
general_boss_idle_9=pygame.transform.scale(general_boss_idle_9,(55,60))

general_boss_idle_left_1=pygame.transform.flip(general_boss_idle_1,True,False)
general_boss_idle_left_2=pygame.transform.flip(general_boss_idle_2,True,False)
general_boss_idle_left_3=pygame.transform.flip(general_boss_idle_3,True,False)
general_boss_idle_left_4=pygame.transform.flip(general_boss_idle_4,True,False)
general_boss_idle_left_5=pygame.transform.flip(general_boss_idle_5,True,False)
general_boss_idle_left_6=pygame.transform.flip(general_boss_idle_6,True,False)
general_boss_idle_left_7=pygame.transform.flip(general_boss_idle_7,True,False)
general_boss_idle_left_8=pygame.transform.flip(general_boss_idle_8,True,False)
general_boss_idle_left_9=pygame.transform.flip(general_boss_idle_9,True,False)

general_boss_idle=[general_boss_idle_1,general_boss_idle_2,general_boss_idle_3,general_boss_idle_4,general_boss_idle_5,general_boss_idle_6,general_boss_idle_7,general_boss_idle_8,general_boss_idle_9]
general_boss_idle_left=[general_boss_idle_left_1,general_boss_idle_left_2,general_boss_idle_left_3,general_boss_idle_left_4,general_boss_idle_left_5,general_boss_idle_left_6,general_boss_idle_left_7,general_boss_idle_left_8,general_boss_idle_left_9]

general_boss_icon=pygame.image.load(r"A_Wit's_End\Level_2_General\Icon\Icon.png")
general_boss_icon=pygame.transform.scale(general_boss_icon,(120,100))

general_boss_idle_number=[0] ; general_boss_x=[1400] ; general_boss_y=[585]

#here

boss_1_idle_1=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Idle\idle_1.png").convert_alpha()
boss_1_idle_2=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Idle\idle_2.png").convert_alpha()
boss_1_idle_3=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Idle\idle_3.png").convert_alpha()
boss_1_idle_4=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Idle\idle_4.png").convert_alpha()
boss_1_idle_5=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Idle\idle_5.png").convert_alpha()
boss_1_idle_6=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Idle\idle_6.png").convert_alpha()
boss_1_idle_7=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Idle\idle_7.png").convert_alpha()
boss_1_idle_8=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Idle\idle_8.png").convert_alpha()

boss_1_idle_1=pygame.transform.scale(boss_1_idle_1,(55,75))
boss_1_idle_2=pygame.transform.scale(boss_1_idle_2,(55,75))
boss_1_idle_3=pygame.transform.scale(boss_1_idle_3,(55,75))
boss_1_idle_4=pygame.transform.scale(boss_1_idle_4,(55,75))
boss_1_idle_5=pygame.transform.scale(boss_1_idle_5,(55,75))
boss_1_idle_6=pygame.transform.scale(boss_1_idle_6,(55,75))
boss_1_idle_7=pygame.transform.scale(boss_1_idle_7,(55,75))
boss_1_idle_8=pygame.transform.scale(boss_1_idle_8,(55,75))

boss_1_idle_flip_1=pygame.transform.flip(boss_1_idle_1,True,False)
boss_1_idle_flip_2=pygame.transform.flip(boss_1_idle_2,True,False)
boss_1_idle_flip_3=pygame.transform.flip(boss_1_idle_3,True,False)
boss_1_idle_flip_4=pygame.transform.flip(boss_1_idle_4,True,False)
boss_1_idle_flip_5=pygame.transform.flip(boss_1_idle_5,True,False)
boss_1_idle_flip_6=pygame.transform.flip(boss_1_idle_6,True,False)
boss_1_idle_flip_7=pygame.transform.flip(boss_1_idle_7,True,False)
boss_1_idle_flip_8=pygame.transform.flip(boss_1_idle_8,True,False)

boss_1_idle_flip=[boss_1_idle_flip_1,boss_1_idle_flip_2,boss_1_idle_flip_3,boss_1_idle_flip_4,boss_1_idle_flip_5,boss_1_idle_flip_6,boss_1_idle_flip_7,boss_1_idle_flip_8]

boss_1_move_1=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Run\run_1.png")
boss_1_move_2=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Run\run_2.png")
boss_1_move_3=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Run\run_3.png")
boss_1_move_4=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Run\run_4.png")
boss_1_move_5=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Run\run_5.png")
boss_1_move_6=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Run\run_6.png")
boss_1_move_7=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Run\run_7.png")
boss_1_move_8=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Run\run_8.png")

boss_1_move_1=pygame.transform.scale(boss_1_move_1,(55,75))
boss_1_move_2=pygame.transform.scale(boss_1_move_2,(55,75))
boss_1_move_3=pygame.transform.scale(boss_1_move_3,(55,75))
boss_1_move_4=pygame.transform.scale(boss_1_move_4,(55,75))
boss_1_move_5=pygame.transform.scale(boss_1_move_5,(55,75))
boss_1_move_6=pygame.transform.scale(boss_1_move_6,(55,75))
boss_1_move_7=pygame.transform.scale(boss_1_move_7,(55,75))
boss_1_move_8=pygame.transform.scale(boss_1_move_8,(55,75))

boss_1_move_flip_1=pygame.transform.flip(boss_1_move_1,True,False)
boss_1_move_flip_2=pygame.transform.flip(boss_1_move_2,True,False)
boss_1_move_flip_3=pygame.transform.flip(boss_1_move_3,True,False)
boss_1_move_flip_4=pygame.transform.flip(boss_1_move_4,True,False)
boss_1_move_flip_5=pygame.transform.flip(boss_1_move_5,True,False)
boss_1_move_flip_6=pygame.transform.flip(boss_1_move_6,True,False)
boss_1_move_flip_7=pygame.transform.flip(boss_1_move_7,True,False)
boss_1_move_flip_8=pygame.transform.flip(boss_1_move_8,True,False)

boss_1_move=[boss_1_move_1,boss_1_move_2,boss_1_move_3,boss_1_move_4,boss_1_move_5,boss_1_move_6,boss_1_move_7,boss_1_move_8]
boss_1_move_flip=[boss_1_move_flip_1,boss_1_move_flip_2,boss_1_move_flip_3,boss_1_move_flip_4,boss_1_move_flip_5,boss_1_move_flip_6,boss_1_move_flip_7,boss_1_move_flip_8]

boss_1_attack_1=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Attack\attack_1.png")
boss_1_attack_2=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Attack\attack_2.png")
boss_1_attack_3=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Attack\attack_3.png")
boss_1_attack_4=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Attack\attack_4.png")
boss_1_attack_5=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Attack\attack_5.png")
boss_1_attack_6=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Attack\attack_6.png")
boss_1_attack_7=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Attack\attack_7.png")
boss_1_attack_8=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Attack\attack_8.png")

boss_1_attack_1=pygame.transform.scale(boss_1_attack_1,(55,75))
boss_1_attack_2=pygame.transform.scale(boss_1_attack_2,(55,75))
boss_1_attack_3=pygame.transform.scale(boss_1_attack_3,(55,75))
boss_1_attack_4=pygame.transform.scale(boss_1_attack_4,(55,75))
boss_1_attack_5=pygame.transform.scale(boss_1_attack_5,(55,75))
boss_1_attack_6=pygame.transform.scale(boss_1_attack_6,(55,75))
boss_1_attack_7=pygame.transform.scale(boss_1_attack_7,(55,75))
boss_1_attack_8=pygame.transform.scale(boss_1_attack_8,(55,75))

boss_1_attack_flip_1=pygame.transform.flip(boss_1_attack_1,True,False)
boss_1_attack_flip_2=pygame.transform.flip(boss_1_attack_2,True,False)
boss_1_attack_flip_3=pygame.transform.flip(boss_1_attack_3,True,False)
boss_1_attack_flip_4=pygame.transform.flip(boss_1_attack_4,True,False)
boss_1_attack_flip_5=pygame.transform.flip(boss_1_attack_5,True,False)
boss_1_attack_flip_6=pygame.transform.flip(boss_1_attack_6,True,False)
boss_1_attack_flip_7=pygame.transform.flip(boss_1_attack_7,True,False)
boss_1_attack_flip_8=pygame.transform.flip(boss_1_attack_8,True,False)

boss_1_attack=[boss_1_attack_1,boss_1_attack_2,boss_1_attack_3,boss_1_attack_4,boss_1_attack_5,boss_1_attack_6,boss_1_attack_7,boss_1_attack_8]
boss_1_attack_flip=[boss_1_attack_flip_1,boss_1_attack_flip_2,boss_1_attack_flip_3,boss_1_attack_flip_4,boss_1_attack_flip_5,boss_1_attack_flip_6,boss_1_attack_flip_7,boss_1_attack_flip_8]

boss_1_fall_1=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Fall\fall_1.png")
boss_1_fall_2=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Fall\fall_2.png")
boss_1_fall_3=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Fall\fall_3.png")
boss_1_fall_4=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Fall\fall_4.png")
boss_1_fall_5=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Fall\fall_5.png")


boss_1_fall_1=pygame.transform.scale(boss_1_fall_1,(55,75))
boss_1_fall_2=pygame.transform.scale(boss_1_fall_2,(55,75))
boss_1_fall_3=pygame.transform.scale(boss_1_fall_3,(55,75))
boss_1_fall_4=pygame.transform.scale(boss_1_fall_4,(55,75))
boss_1_fall_5=pygame.transform.scale(boss_1_fall_5,(55,75))


boss_1_fall_flip_1=pygame.transform.flip(boss_1_fall_1,True,False)
boss_1_fall_flip_2=pygame.transform.flip(boss_1_fall_2,True,False)
boss_1_fall_flip_3=pygame.transform.flip(boss_1_fall_3,True,False)
boss_1_fall_flip_4=pygame.transform.flip(boss_1_fall_4,True,False)
boss_1_fall_flip_5=pygame.transform.flip(boss_1_fall_5,True,False)

boss_1_fall=[boss_1_fall_1,boss_1_fall_2,boss_1_fall_3,boss_1_fall_4,boss_1_fall_5]
boss_1_fall_flip=[boss_1_fall_flip_1,boss_1_fall_flip_2,boss_1_fall_flip_3,boss_1_fall_flip_4,boss_1_fall_flip_5]

boss_1_icon=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Icon\icon.png")
boss_1_icon=pygame.transform.scale(boss_1_icon,(120,100))

boss_1_idle_number=[0] ; boss_1_move_number=[0] ; boss_1_attack_number=[0] ; boss_1_fall_number=[0] ;  boss_1_level_2_part_2_x=[5600] ; boss_1_level_2_part_2_y=[480]
boss_1_x_movement=[0] ; boss_1_y_movement=[0]
boss_1_rect=pygame.Rect(boss_1_level_2_part_2_x[0],boss_1_level_2_part_2_y[0],55,75)