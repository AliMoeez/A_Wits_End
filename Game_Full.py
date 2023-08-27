import pygame,sys,json,random, math
from pytmx.util_pygame import load_pygame

pygame.init()

FPS=30
run=True

SCREEN_WIDTH=1100 ; SCREEN_HEIGHT=700 ; SCREEN=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

clock=pygame.time.Clock()

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

file_3=open(r"A_Wit's_End\Level 3_Tileset\tile_set\level_3_tile_set.txt","r")

data_3=file_3.readlines()

tile_level_3=[] ; tile_level_3_rect=[]

list_data_3=[] 

for i in data_3:
    if i[-1]=="\n": list_data_3.append(i[:-1])
    else: list_data_3.append(i)
        
for idx,num in enumerate(list_data_3): tile_level_3.append(list_data_3[idx].split(","))

level_3_tile_set_part_2=load_pygame(r"A_Wit's_End\Level 3_Tileset\test.tmx")

level_3_tile_set_part_2_rect=[]

level_3_tile_1=pygame.transform.scale(level_2_floor_2_15,(65,45))

    
tile_level_1_ground=pygame.image.load(r"A_Wit's_End\Level_1_Tileset\GothicVania-town-files\GothicVania-town-files\PNG\environment\layers\sliced-tileset\ground.png") ; tile_level_1_ground=pygame.transform.scale(tile_level_1_ground,(65,45))

tile_level_1_dirt=pygame.transform.flip(tile_level_1_ground,False,True)


level_3_bg_top_1=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\background\background_layer_1.png")
level_3_bg_top_2=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\background\background_layer_2.png")
level_3_bg_top_3=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\background\background_layer_3.png")

level_3_bg_top_1=pygame.transform.scale(level_3_bg_top_1,(SCREEN_WIDTH,SCREEN_HEIGHT))
level_3_bg_top_2=pygame.transform.scale(level_3_bg_top_2,(SCREEN_WIDTH,SCREEN_HEIGHT))
level_3_bg_top_3=pygame.transform.scale(level_3_bg_top_3,(SCREEN_WIDTH,SCREEN_HEIGHT))

level_3_hill_1=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\tiles\hill_1.png").convert_alpha()
level_3_hill_2=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\tiles\hill_2.png").convert_alpha()
level_3_hill_3=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\tiles\hill_3.png").convert_alpha()
level_3_hill_4=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\tiles\hill_4.png").convert_alpha()
level_3_hill_5=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\tiles\hill_5.png").convert_alpha()
level_3_hill_6=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\tiles\hill_6.png").convert_alpha()
level_3_hill_7=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\tiles\hill_7.png").convert_alpha()
level_3_door=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\tiles\door_1.png").convert_alpha()
level_3_pillar_1=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\tiles\tile_14.png").convert_alpha()
level_3_pillar_2=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\tiles\tile_15.png").convert_alpha()
level_3_pillar_3=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\tiles\tile_16.png").convert_alpha()

level_3_door=pygame.transform.scale(level_3_door,(80,100))


level_3_bg_1_1=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\background1.png").convert_alpha()
level_3_bg_2_1=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\background2.png").convert_alpha()
level_3_bg_3_1=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\background3.png").convert_alpha()
level_3_bg_4_1=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\background4a.png").convert_alpha()
level_3_bg_5_1=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\background4b.png").convert_alpha()
level_3_bg_1_1=pygame.transform.scale(level_3_bg_1_1,(SCREEN_WIDTH,SCREEN_HEIGHT))
level_3_bg_2_1=pygame.transform.scale(level_3_bg_2_1,(SCREEN_WIDTH,SCREEN_HEIGHT))
level_3_bg_3_1=pygame.transform.scale(level_3_bg_3_1,(SCREEN_WIDTH,SCREEN_HEIGHT))
level_3_bg_4_1=pygame.transform.scale(level_3_bg_4_1,(SCREEN_WIDTH,SCREEN_HEIGHT))
level_3_bg_5_1=pygame.transform.scale(level_3_bg_5_1,(SCREEN_WIDTH,SCREEN_HEIGHT))

level_3_bg_part_2_list=[level_3_bg_1_1,level_3_bg_2_1,level_3_bg_3_1,level_3_bg_4_1,level_3_bg_5_1]


level_3_part_2=False ; level_3_transition_1=False

mouse_button_left_image=pygame.image.load(r"A_Wit's_End\Menu Design\Buttons Pack\Buttons Pack\MOUSE\MOUSEBUTTONLEFT.png")
mouse_button_left_image=pygame.transform.scale(mouse_button_left_image,(40,40)) 

camera_x_y_bg=[0,0] ; camera_x_y=[100,0] 

level_screen=False ; level_1=False ; level_2=False ; level_3=False ; level_4=False ; change_dialogue=False ; dialogue_start_condition=False ; change_dialogue_cond_1=False ;  end_dialogue=False
level_1_dialogue_part_two=False ; level_one_x_border=False ; dialogue_move_condition=False ; level_one_dialogue_part_three=False ; end_level_1_dialogue=False ; level_win=False ; win_blur=[0]
level_2_dialogue_part_one=False ; level_2_dialogue_part_two=False ; level_2_dialogue_once_two=False ; level_2_tile_index=[] ; level_2_part_2_boss_dialogue=False; level_2_dialogue_part_two_once=False
level_2_dialogue_part_three_once=False ; level_2_dialogue_part_four_once=False ; level_2_part_win_boss_dialogue=False ; level_2_part_lose_boss_dialogue=False

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


enemy_1_level_3_x=[800,900,1200,1800,1900,2700,2900,3000,3100,3400,3500,3700]

enemy_1_level_3_y=[575,575,575,575,575,575,575,575,575,575,575,575,575]

enemy_1_level_3_rect=[pygame.Rect(enemy_1_level_3_x[0],enemy_1_level_3_y[0],45,67),pygame.Rect(enemy_1_level_3_x[1],enemy_1_level_3_y[1],45,67),
                      pygame.Rect(enemy_1_level_3_x[2],enemy_1_level_3_y[2],45,67),pygame.Rect(enemy_1_level_3_x[3],enemy_1_level_3_y[3],45,67),
                      pygame.Rect(enemy_1_level_3_x[4],enemy_1_level_3_y[4],45,67),pygame.Rect(enemy_1_level_3_x[5],enemy_1_level_3_y[5],45,67),
                      pygame.Rect(enemy_1_level_3_x[6],enemy_1_level_3_y[6],45,67),pygame.Rect(enemy_1_level_3_x[7],enemy_1_level_3_y[7],45,67),
                      pygame.Rect(enemy_1_level_3_x[8],enemy_1_level_3_y[8],45,67),pygame.Rect(enemy_1_level_3_x[9],enemy_1_level_3_y[9],45,67),
                      pygame.Rect(enemy_1_level_3_x[10],enemy_1_level_3_y[10],45,67),pygame.Rect(enemy_1_level_3_x[11],enemy_1_level_3_y[11],45,67)

]

enemy_1_walk_length=[0] ; enemy_1_idle_length=[0] ; level_1_enemy_fight_condition=False ; enemy_1_x_movement=[0] ; enemy_1_y_movement=[0] ; enemy_1_friendly_dialogue=False ; enemy_one_dialogue_list=[0] ; enemy_list_level_1=[]
enemy_1_attack_length=[0] ; enemy_1_distance_list=[] ; enemy_1_health_list=[] ; enemy_one_fall_number=[] ; enemy_one_fall_direction_set=[] ; enemy_list_level_2=[] ; enemy_list_level_3=[]

attack_list=[]

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

enemy_two_level_4_x_1=[2000,2200,3400,3450,3500,3550,3600,4300,4325,5300,5400,5500,5500]


enemy_two_level_4_y_1=[450,450,400,400,400,400,400,600,600,600,600,600,600]

enemy_two_level_4_rect_1=[]

for idx,number in enumerate(enemy_two_level_4_x_1):
    enemy_two_level_4_rect_1.append(pygame.Rect(enemy_two_level_4_x_1[idx],enemy_two_level_4_y_1[idx],45,55))

enemy_two_level_1_rect=[pygame.Rect(enemy_two_level_1_x[0],enemy_two_level_1_y[0],45,55),pygame.Rect(enemy_two_level_1_x[1],enemy_two_level_1_y[1],45,55)] 



enemy_two_rect_list=[]


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


general_boss_idle_1=pygame.image.load(r"A_Wit's_End\Level_2_General\Idle\sprite_1.png") ; general_boss_idle_2=pygame.image.load(r"A_Wit's_End\Level_2_General\Idle\sprite_2.png") ; general_boss_idle_3=pygame.image.load(r"A_Wit's_End\Level_2_General\Idle\sprite_3.png") ; general_boss_idle_4=pygame.image.load(r"A_Wit's_End\Level_2_General\Idle\sprite_4.png")
general_boss_idle_5=pygame.image.load(r"A_Wit's_End\Level_2_General\Idle\sprite_5.png") ; general_boss_idle_6=pygame.image.load(r"A_Wit's_End\Level_2_General\Idle\sprite_6.png") ; general_boss_idle_7=pygame.image.load(r"A_Wit's_End\Level_2_General\Idle\sprite_7.png")
general_boss_idle_8=pygame.image.load(r"A_Wit's_End\Level_2_General\Idle\sprite_8.png") ; general_boss_idle_9=pygame.image.load(r"A_Wit's_End\Level_2_General\Idle\sprite_9.png")
general_boss_idle_1=pygame.transform.scale(general_boss_idle_1,(55,60)) ; general_boss_idle_2=pygame.transform.scale(general_boss_idle_2,(55,60)) ; general_boss_idle_3=pygame.transform.scale(general_boss_idle_3,(55,60)) ; general_boss_idle_4=pygame.transform.scale(general_boss_idle_4,(55,60))
general_boss_idle_5=pygame.transform.scale(general_boss_idle_5,(55,60)) ; general_boss_idle_6=pygame.transform.scale(general_boss_idle_6,(55,60)) ; general_boss_idle_7=pygame.transform.scale(general_boss_idle_7,(55,60)) ; general_boss_idle_8=pygame.transform.scale(general_boss_idle_8,(55,60)) ; general_boss_idle_9=pygame.transform.scale(general_boss_idle_9,(55,60))
general_boss_idle_left_1=pygame.transform.flip(general_boss_idle_1,True,False) ; general_boss_idle_left_2=pygame.transform.flip(general_boss_idle_2,True,False) ; general_boss_idle_left_3=pygame.transform.flip(general_boss_idle_3,True,False) ; general_boss_idle_left_4=pygame.transform.flip(general_boss_idle_4,True,False)
general_boss_idle_left_5=pygame.transform.flip(general_boss_idle_5,True,False) ; general_boss_idle_left_6=pygame.transform.flip(general_boss_idle_6,True,False) ; general_boss_idle_left_7=pygame.transform.flip(general_boss_idle_7,True,False) ; general_boss_idle_left_8=pygame.transform.flip(general_boss_idle_8,True,False) ; general_boss_idle_left_9=pygame.transform.flip(general_boss_idle_9,True,False)
general_boss_idle=[general_boss_idle_1,general_boss_idle_2,general_boss_idle_3,general_boss_idle_4,general_boss_idle_5,general_boss_idle_6,general_boss_idle_7,general_boss_idle_8,general_boss_idle_9]
general_boss_idle_left=[general_boss_idle_left_1,general_boss_idle_left_2,general_boss_idle_left_3,general_boss_idle_left_4,general_boss_idle_left_5,general_boss_idle_left_6,general_boss_idle_left_7,general_boss_idle_left_8,general_boss_idle_left_9]

general_boss_icon=pygame.image.load(r"A_Wit's_End\Level_2_General\Icon\Icon.png")
general_boss_icon=pygame.transform.scale(general_boss_icon,(120,100))

general_boss_idle_number=[0] ; general_boss_x=[1400] ; general_boss_y=[585]

#here

boss_1_idle_1=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Idle\idle_1.png").convert_alpha() ; boss_1_idle_2=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Idle\idle_2.png").convert_alpha() ; boss_1_idle_3=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Idle\idle_3.png").convert_alpha()
boss_1_idle_4=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Idle\idle_4.png").convert_alpha() ; boss_1_idle_5=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Idle\idle_5.png").convert_alpha() ; boss_1_idle_6=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Idle\idle_6.png").convert_alpha()
boss_1_idle_7=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Idle\idle_7.png").convert_alpha() ; boss_1_idle_8=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Idle\idle_8.png").convert_alpha()
boss_1_idle_1=pygame.transform.scale(boss_1_idle_1,(55,75)) ; boss_1_idle_2=pygame.transform.scale(boss_1_idle_2,(55,75)) ; boss_1_idle_3=pygame.transform.scale(boss_1_idle_3,(55,75))  ; boss_1_idle_4=pygame.transform.scale(boss_1_idle_4,(55,75))
boss_1_idle_5=pygame.transform.scale(boss_1_idle_5,(55,75)) ; boss_1_idle_6=pygame.transform.scale(boss_1_idle_6,(55,75)) ; boss_1_idle_7=pygame.transform.scale(boss_1_idle_7,(55,75)) ; boss_1_idle_8=pygame.transform.scale(boss_1_idle_8,(55,75))
boss_1_idle_flip_1=pygame.transform.flip(boss_1_idle_1,True,False) ; boss_1_idle_flip_2=pygame.transform.flip(boss_1_idle_2,True,False) ; boss_1_idle_flip_3=pygame.transform.flip(boss_1_idle_3,True,False) ; boss_1_idle_flip_4=pygame.transform.flip(boss_1_idle_4,True,False)
boss_1_idle_flip_5=pygame.transform.flip(boss_1_idle_5,True,False) ; boss_1_idle_flip_6=pygame.transform.flip(boss_1_idle_6,True,False) ; boss_1_idle_flip_7=pygame.transform.flip(boss_1_idle_7,True,False) ; boss_1_idle_flip_8=pygame.transform.flip(boss_1_idle_8,True,False)
boss_1_idle=[boss_1_idle_1,boss_1_idle_2,boss_1_idle_3,boss_1_idle_4,boss_1_idle_5,boss_1_idle_6,boss_1_idle_7,boss_1_idle_8]
boss_1_idle_flip=[boss_1_idle_flip_1,boss_1_idle_flip_2,boss_1_idle_flip_3,boss_1_idle_flip_4,boss_1_idle_flip_5,boss_1_idle_flip_6,boss_1_idle_flip_7,boss_1_idle_flip_8]

boss_1_move_1=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Run\run_1.png") ; boss_1_move_2=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Run\run_2.png") ; boss_1_move_3=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Run\run_3.png") ; boss_1_move_4=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Run\run_4.png")
boss_1_move_5=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Run\run_5.png") ; boss_1_move_6=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Run\run_6.png") ;  boss_1_move_7=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Run\run_7.png") ; boss_1_move_8=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Run\run_8.png")
boss_1_move_1=pygame.transform.scale(boss_1_move_1,(65,85)) ; boss_1_move_2=pygame.transform.scale(boss_1_move_2,(65,85)) ; boss_1_move_3=pygame.transform.scale(boss_1_move_3,(65,85)) ; boss_1_move_4=pygame.transform.scale(boss_1_move_4,(65,85))
boss_1_move_5=pygame.transform.scale(boss_1_move_5,(65,85)) ; boss_1_move_6=pygame.transform.scale(boss_1_move_6,(65,85)) ; boss_1_move_7=pygame.transform.scale(boss_1_move_7,(65,85)) ; boss_1_move_8=pygame.transform.scale(boss_1_move_8,(65,85))
boss_1_move_flip_1=pygame.transform.flip(boss_1_move_1,True,False) ; boss_1_move_flip_2=pygame.transform.flip(boss_1_move_2,True,False) ; boss_1_move_flip_3=pygame.transform.flip(boss_1_move_3,True,False) ; boss_1_move_flip_4=pygame.transform.flip(boss_1_move_4,True,False)
boss_1_move_flip_5=pygame.transform.flip(boss_1_move_5,True,False) ; boss_1_move_flip_6=pygame.transform.flip(boss_1_move_6,True,False) ; boss_1_move_flip_7=pygame.transform.flip(boss_1_move_7,True,False) ; boss_1_move_flip_8=pygame.transform.flip(boss_1_move_8,True,False)
boss_1_move=[boss_1_move_1,boss_1_move_2,boss_1_move_3,boss_1_move_4,boss_1_move_5,boss_1_move_6,boss_1_move_7,boss_1_move_8]
boss_1_move_flip=[boss_1_move_flip_1,boss_1_move_flip_2,boss_1_move_flip_3,boss_1_move_flip_4,boss_1_move_flip_5,boss_1_move_flip_6,boss_1_move_flip_7,boss_1_move_flip_8]

boss_1_attack_1=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Attack\attack_1.png") ; boss_1_attack_2=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Attack\attack_2.png") ; boss_1_attack_3=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Attack\attack_3.png") ; boss_1_attack_4=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Attack\attack_4.png")
boss_1_attack_5=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Attack\attack_5.png") ; boss_1_attack_6=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Attack\attack_6.png") ; boss_1_attack_7=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Attack\attack_7.png") ; boss_1_attack_8=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Attack\attack_8.png")
boss_1_attack_1=pygame.transform.scale(boss_1_attack_1,(75,75)) ; boss_1_attack_2=pygame.transform.scale(boss_1_attack_2,(75,75)) ; boss_1_attack_3=pygame.transform.scale(boss_1_attack_3,(75,75)) ; boss_1_attack_4=pygame.transform.scale(boss_1_attack_4,(75,75)) ; boss_1_attack_5=pygame.transform.scale(boss_1_attack_5,(75,75))
boss_1_attack_6=pygame.transform.scale(boss_1_attack_6,(75,75)) ; boss_1_attack_7=pygame.transform.scale(boss_1_attack_7,(75,75)) ; boss_1_attack_8=pygame.transform.scale(boss_1_attack_8,(75,75))
boss_1_attack_flip_1=pygame.transform.flip(boss_1_attack_1,True,False) ; boss_1_attack_flip_2=pygame.transform.flip(boss_1_attack_2,True,False) ; boss_1_attack_flip_3=pygame.transform.flip(boss_1_attack_3,True,False) ; boss_1_attack_flip_4=pygame.transform.flip(boss_1_attack_4,True,False)
boss_1_attack_flip_5=pygame.transform.flip(boss_1_attack_5,True,False) ; boss_1_attack_flip_6=pygame.transform.flip(boss_1_attack_6,True,False) ; boss_1_attack_flip_7=pygame.transform.flip(boss_1_attack_7,True,False) ;boss_1_attack_flip_8=pygame.transform.flip(boss_1_attack_8,True,False)
boss_1_attack=[boss_1_attack_1,boss_1_attack_2,boss_1_attack_3,boss_1_attack_4,boss_1_attack_5,boss_1_attack_6,boss_1_attack_7,boss_1_attack_8]
boss_1_attack_flip=[boss_1_attack_flip_1,boss_1_attack_flip_2,boss_1_attack_flip_3,boss_1_attack_flip_4,boss_1_attack_flip_5,boss_1_attack_flip_6,boss_1_attack_flip_7,boss_1_attack_flip_8]

boss_1_fall_1=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Fall\fall_1.png") ; boss_1_fall_2=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Fall\fall_2.png") ; boss_1_fall_3=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Fall\fall_3.png") ; boss_1_fall_4=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Fall\fall_4.png") ; boss_1_fall_5=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Fall\fall_5.png")
boss_1_fall_1=pygame.transform.scale(boss_1_fall_1,(55,75)) ; boss_1_fall_2=pygame.transform.scale(boss_1_fall_2,(55,75)) ; boss_1_fall_3=pygame.transform.scale(boss_1_fall_3,(45,60)) ; boss_1_fall_4=pygame.transform.scale(boss_1_fall_4,(45,60)) ; boss_1_fall_5=pygame.transform.scale(boss_1_fall_5,(45,60))
boss_1_fall_flip_1=pygame.transform.flip(boss_1_fall_1,True,False) ; boss_1_fall_flip_2=pygame.transform.flip(boss_1_fall_2,True,False) ; boss_1_fall_flip_3=pygame.transform.flip(boss_1_fall_3,True,False) ; boss_1_fall_flip_4=pygame.transform.flip(boss_1_fall_4,True,False) ; boss_1_fall_flip_5=pygame.transform.flip(boss_1_fall_5,True,False)
boss_1_fall=[boss_1_fall_1,boss_1_fall_2,boss_1_fall_3,boss_1_fall_4,boss_1_fall_5]
boss_1_fall_flip=[boss_1_fall_flip_1,boss_1_fall_flip_2,boss_1_fall_flip_3,boss_1_fall_flip_4,boss_1_fall_flip_5]

boss_1_icon=pygame.image.load(r"A_Wit's_End\Enemy_Boss_1\Icon\icon.png")
boss_1_icon=pygame.transform.scale(boss_1_icon,(120,100))

boss_1_idle_number=[0] ; boss_1_move_number=[0] ; boss_1_attack_number=[0] ; boss_1_fall_number=[0] ;  boss_1_level_2_part_2_x=[5600] ; boss_1_level_2_part_2_y=[480]
boss_1_x_movement=[0] ; boss_1_y_movement=[0] ; boss_1_attack_timer=[200] ; boss_1_rest_time=[0] ; boss_1_health=[1000] ; boss_fall_right=False ; boss_Fall_left=False
boss_1_rect=pygame.Rect(boss_1_level_2_part_2_x[0],boss_1_level_2_part_2_y[0],55,75) 


level_3_bg_test=pygame.image.load(r"A_Wit's_End\Level 3_Tileset\background\backround.PNG").convert_alpha()
level_3_bg_test=pygame.transform.scale(level_3_bg_test,(SCREEN_WIDTH,SCREEN_HEIGHT))

level_3_fade_level=[0] ; level_3_dialogue_part_1=False ; level_3_dialogue_part_1_once=False

ally_1_idle_1=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Heavy Bandit\Idle\HeavyBandit_Idle_0.png") ; ally_1_idle_2=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Heavy Bandit\Idle\HeavyBandit_Idle_1.png")
ally_1_idle_3=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Heavy Bandit\Idle\HeavyBandit_Idle_2.png") ; ally_1_idle_4=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Heavy Bandit\Idle\HeavyBandit_Idle_3.png")
ally_1_idle_1=pygame.transform.scale(ally_1_idle_1,(75,85)) ; ally_1_idle_2=pygame.transform.scale(ally_1_idle_2,(75,85)) ; ally_1_idle_3=pygame.transform.scale(ally_1_idle_3,(75,85)) ; ally_1_idle_4=pygame.transform.scale(ally_1_idle_4,(75,85))
ally_1_idle_flip_1=pygame.transform.flip(ally_1_idle_1,True,False) ; ally_1_idle_flip_2=pygame.transform.flip(ally_1_idle_2,True,False) ; ally_1_idle_flip_3=pygame.transform.flip(ally_1_idle_3,True,False) ; ally_1_idle_flip_4=pygame.transform.flip(ally_1_idle_4,True,False)
ally_1_idle=[ally_1_idle_1,ally_1_idle_2,ally_1_idle_3,ally_1_idle_4]
ally_1_idle_flip=[ally_1_idle_flip_1,ally_1_idle_flip_2,ally_1_idle_flip_3,ally_1_idle_flip_4]

ally_1_run_1=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Heavy Bandit\Run\HeavyBandit_Run_0.png")
ally_1_run_2=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Heavy Bandit\Run\HeavyBandit_Run_1.png")
ally_1_run_3=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Heavy Bandit\Run\HeavyBandit_Run_2.png")
ally_1_run_4=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Heavy Bandit\Run\HeavyBandit_Run_3.png")
ally_1_run_5=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Heavy Bandit\Run\HeavyBandit_Run_4.png")
ally_1_run_6=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Heavy Bandit\Run\HeavyBandit_Run_5.png")
ally_1_run_7=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Heavy Bandit\Run\HeavyBandit_Run_6.png")
ally_1_run_8=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Heavy Bandit\Run\HeavyBandit_Run_7.png")

ally_1_run_1=pygame.transform.scale(ally_1_run_1,(75,85))
ally_1_run_2=pygame.transform.scale(ally_1_run_2,(75,85))
ally_1_run_3=pygame.transform.scale(ally_1_run_3,(75,85))
ally_1_run_4=pygame.transform.scale(ally_1_run_4,(75,85))
ally_1_run_5=pygame.transform.scale(ally_1_run_5,(75,85))
ally_1_run_6=pygame.transform.scale(ally_1_run_6,(75,85))
ally_1_run_7=pygame.transform.scale(ally_1_run_7,(75,85))
ally_1_run_8=pygame.transform.scale(ally_1_run_8,(75,85))

ally_1_run_flip_1=pygame.transform.flip(ally_1_run_1,True,False)
ally_1_run_flip_2=pygame.transform.flip(ally_1_run_2,True,False)
ally_1_run_flip_3=pygame.transform.flip(ally_1_run_3,True,False)
ally_1_run_flip_4=pygame.transform.flip(ally_1_run_4,True,False)
ally_1_run_flip_5=pygame.transform.flip(ally_1_run_5,True,False)
ally_1_run_flip_6=pygame.transform.flip(ally_1_run_6,True,False)
ally_1_run_flip_7=pygame.transform.flip(ally_1_run_7,True,False)
ally_1_run_flip_8=pygame.transform.flip(ally_1_run_8,True,False)

ally_1_icon=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Heavy Bandit\Icon\HeavyBandit_Icon.png")
ally_1_icon=pygame.transform.scale(ally_1_icon,(120,120))

ally_1_run=[ally_1_run_1,ally_1_run_2,ally_1_run_3,ally_1_run_4,ally_1_run_5,ally_1_run_6,ally_1_run_7,ally_1_run_8]
ally_1_run_flip=[ally_1_run_flip_1,ally_1_run_flip_2,ally_1_run_flip_3,ally_1_run_flip_4,ally_1_run_flip_5,ally_1_run_flip_6,ally_1_run_flip_7,ally_1_run_flip_8]


ally_1_level_3_part_1_x_idle=[1710,3795,3910]
ally_1_level_3_part_1_y_idle=[570,570,570]

ally_1_level_3_part_1_x_run=[3200,4300]
ally_1_level_3_part_1_y_run=[570,570]

ally_1_level_3_part_2_x_idle=[400,1500,2050,2700,3100]
ally_1_level_3_part_2_y_idle=[570,570,570,570,570]

ally_1_level_3_part_2_x_run=[800,1200,1700,2100,2200]
ally_1_level_3_part_2_y_run=[570,570,570,570,570]

ally_1_level_3_part_1_idle_rect=[pygame.Rect(ally_1_level_3_part_1_x_idle[0],ally_1_level_3_part_1_y_idle[0],75,85), 
                            pygame.Rect(ally_1_level_3_part_1_x_idle[1],ally_1_level_3_part_1_y_idle[1],75,85), 
                            pygame.Rect(ally_1_level_3_part_1_x_idle[2],ally_1_level_3_part_1_y_idle[2],75,85)]


ally_1_level_3_part_1_run_rect=[pygame.Rect(ally_1_level_3_part_1_x_run[0],ally_1_level_3_part_1_y_run[0],75,85),
                            pygame.Rect(ally_1_level_3_part_1_x_run[1],ally_1_level_3_part_1_y_run[1],75,85)]


ally_1_level_3_part_2_idle_rect=[pygame.Rect(ally_1_level_3_part_2_x_idle[0],ally_1_level_3_part_2_y_idle[0],75,85), 
                            pygame.Rect(ally_1_level_3_part_2_x_idle[1],ally_1_level_3_part_2_y_idle[1],75,85), 
                            pygame.Rect(ally_1_level_3_part_2_x_idle[2],ally_1_level_3_part_2_y_idle[2],75,85),
                            pygame.Rect(ally_1_level_3_part_2_x_idle[3],ally_1_level_3_part_2_y_idle[3],75,85),
                            pygame.Rect(ally_1_level_3_part_2_x_idle[4],ally_1_level_3_part_2_y_idle[4],75,85)

]

ally_1_level_3_part_2_run_rect=[pygame.Rect(ally_1_level_3_part_2_x_run[0],ally_1_level_3_part_2_y_run[0],75,85),
                            pygame.Rect(ally_1_level_3_part_2_x_run[1],ally_1_level_3_part_2_y_run[1],75,85),
                            pygame.Rect(ally_1_level_3_part_2_x_run[2],ally_1_level_3_part_2_y_run[2],75,85),
                            pygame.Rect(ally_1_level_3_part_2_x_run[3],ally_1_level_3_part_2_y_run[3],75,85),
                            pygame.Rect(ally_1_level_3_part_2_x_run[4],ally_1_level_3_part_2_y_run[4],75,85)
]

ally_1_rect_list=[]

ally_1_x_movement=[] ; ally_1_y_movement=[]

ally_1_idle_number=[] ; ally_1_run_number=[] 

ally_1_run_direction=[1,0,1,0,1] ; ally_1_run_length=[20,30,10,30,10]

ally_1_player_distance_list=[] ; player_ally_one_dialogue=False ; level_3_dialogue_part_2_once=False
level_3_dialogue_part_3_once=False ; level_3_dialogue_part_4_once=False ; level_3_dialogue_part_5_once=False
level_3_dialogue_part_6_once=False ; level_3_dialogue_part_7_once=False ; level_3_dialogue_part_8_once=False

player_ally_one=False ; player_ally_two=False ;  player_ally_three=False ; player_ally_four=False ;  player_ally_five=False

boss_2_idle_1=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Idle\LightBandit_Idle_0.png") ; boss_2_idle_2=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Idle\LightBandit_Idle_1.png") ; boss_2_idle_3=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Idle\LightBandit_Idle_2.png") ; boss_2_idle_4=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Idle\LightBandit_Idle_3.png")
boss_2_idle_1=pygame.transform.scale(boss_2_idle_1,(75,85)) ; boss_2_idle_2=pygame.transform.scale(boss_2_idle_2,(75,85)) ; boss_2_idle_3=pygame.transform.scale(boss_2_idle_3,(75,85)) ; boss_2_idle_4=pygame.transform.scale(boss_2_idle_4,(75,85))
boss_2_idle_flip_1=pygame.transform.flip(boss_2_idle_1,True,False) ; boss_2_idle_flip_2=pygame.transform.flip(boss_2_idle_2,True,False) ; boss_2_idle_flip_3=pygame.transform.flip(boss_2_idle_3,True,False) ; boss_2_idle_flip_4=pygame.transform.flip(boss_2_idle_4,True,False)
boss_2_idle=[boss_2_idle_1,boss_2_idle_2,boss_2_idle_3,boss_2_idle_4] ; boss_2_idle_flip=[boss_2_idle_flip_1,boss_2_idle_flip_2,boss_2_idle_flip_3,boss_2_idle_flip_4] ; boss_2_idle_number=[0] 

boss_2_icon_level_3=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Icon\boss_two_icon.png") ; boss_2_icon_level_3=pygame.transform.scale(boss_2_icon_level_3,(120,120))

boss_2_run_1=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Run\LightBandit_Run_0.png") ; boss_2_run_2=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Run\LightBandit_Run_1.png") ; boss_2_run_3=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Run\LightBandit_Run_2.png") ; boss_2_run_4=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Run\LightBandit_Run_3.png")
boss_2_run_5=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Run\LightBandit_Run_4.png") ; boss_2_run_6=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Run\LightBandit_Run_5.png") ; boss_2_run_7=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Run\LightBandit_Run_6.png") ; boss_2_run_8=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Run\LightBandit_Run_7.png")
boss_2_run_1=pygame.transform.scale(boss_2_run_1,(75,85)) ; boss_2_run_2=pygame.transform.scale(boss_2_run_2,(75,85)) ; boss_2_run_3=pygame.transform.scale(boss_2_run_3,(75,85)) ; boss_2_run_4=pygame.transform.scale(boss_2_run_4,(75,85))
boss_2_run_5=pygame.transform.scale(boss_2_run_5,(75,85)) ; boss_2_run_6=pygame.transform.scale(boss_2_run_6,(75,85)) ; boss_2_run_7=pygame.transform.scale(boss_2_run_7,(75,85)) ; boss_2_run_8=pygame.transform.scale(boss_2_run_8,(75,85))
boss_2_run_flip_1=pygame.transform.flip(boss_2_run_1,True,False) ; boss_2_run_flip_2=pygame.transform.flip(boss_2_run_2,True,False) ; boss_2_run_flip_3=pygame.transform.flip(boss_2_run_3,True,False) ; boss_2_run_flip_4=pygame.transform.flip(boss_2_run_4,True,False)
boss_2_run_flip_5=pygame.transform.flip(boss_2_run_5,True,False) ; boss_2_run_flip_6=pygame.transform.flip(boss_2_run_6,True,False) ; boss_2_run_flip_7=pygame.transform.flip(boss_2_run_7,True,False) ; boss_2_run_flip_8=pygame.transform.flip(boss_2_run_8,True,False)
boss_2_run=[boss_2_run_1,boss_2_run_2,boss_2_run_3,boss_2_run_4,boss_2_run_5,boss_2_run_6,boss_2_run_7,boss_2_run_8]
boss_2_run_flip=[boss_2_run_flip_1,boss_2_run_flip_2,boss_2_run_flip_3,boss_2_run_flip_4,boss_2_run_flip_5,boss_2_run_flip_6,boss_2_run_flip_7,boss_2_run_flip_8]

boss_2_run_number=[0]

boss_2_level_3_x=[4575] ; boss_2_level_3_y=[390]
boss_2_level_3_x_movement=[0] ; boss_2_level_3_y_movement=[0]
boss_2_level_3_health=[1000]
boss_2_level_3_rect=pygame.Rect(boss_2_level_3_x[0],boss_2_level_3_y[0],75,80)

boss_2_attack_1=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Attack\LightBandit_Attack_0.png") ; boss_2_attack_2=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Attack\LightBandit_Attack_1.png") ; boss_2_attack_3=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Attack\LightBandit_Attack_2.png") ; boss_2_attack_4=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Attack\LightBandit_Attack_3.png")
boss_2_attack_5=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Attack\LightBandit_Attack_4.png") ; boss_2_attack_6=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Attack\LightBandit_Attack_5.png") ; boss_2_attack_7=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Attack\LightBandit_Attack_6.png") ; boss_2_attack_8=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Attack\LightBandit_Attack_7.png")
boss_2_attack_1=pygame.transform.scale(boss_2_attack_1,(75,85)) ; boss_2_attack_2=pygame.transform.scale(boss_2_attack_2,(75,85)) ; boss_2_attack_3=pygame.transform.scale(boss_2_attack_3,(75,85)) ; boss_2_attack_4=pygame.transform.scale(boss_2_attack_4,(75,85)) ; boss_2_attack_5=pygame.transform.scale(boss_2_attack_5,(75,85)) ; boss_2_attack_6=pygame.transform.scale(boss_2_attack_6,(75,85)) ; boss_2_attack_7=pygame.transform.scale(boss_2_attack_7,(75,85)) ; boss_2_attack_8=pygame.transform.scale(boss_2_attack_8,(75,85))
boss_2_attack_flip_1=pygame.transform.flip(boss_2_attack_1,True,False) ; boss_2_attack_flip_2=pygame.transform.flip(boss_2_attack_2,True,False) ; boss_2_attack_flip_3=pygame.transform.flip(boss_2_attack_3,True,False) ; boss_2_attack_flip_4=pygame.transform.flip(boss_2_attack_4,True,False) ; boss_2_attack_flip_5=pygame.transform.flip(boss_2_attack_5,True,False) ; boss_2_attack_flip_6=pygame.transform.flip(boss_2_attack_6,True,False) ; boss_2_attack_flip_7=pygame.transform.flip(boss_2_attack_7,True,False) ; boss_2_attack_flip_8=pygame.transform.flip(boss_2_attack_8,True,False)
boss_2_attack=[boss_2_attack_1,boss_2_attack_2,boss_2_attack_3,boss_2_attack_4,boss_2_attack_5,boss_2_attack_6,boss_2_attack_7,boss_2_attack_8]
boss_2_attack_flip=[boss_2_attack_flip_1,boss_2_attack_flip_2,boss_2_attack_flip_3,boss_2_attack_flip_4,boss_2_attack_flip_5,boss_2_attack_flip_6,boss_2_attack_flip_7,boss_2_attack_flip_8]

boss_2_recover_1=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Recover\LightBandit_Recover_0.png") ; boss_2_recover_2=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Recover\LightBandit_Recover_1.png") ; boss_2_recover_3=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Recover\LightBandit_Recover_2.png") ; boss_2_recover_4=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Recover\LightBandit_Recover_3.png") ; boss_2_recover_5=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Recover\LightBandit_Recover_4.png") ; boss_2_recover_6=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Recover\LightBandit_Recover_5.png") ; boss_2_recover_7=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Recover\LightBandit_Recover_6.png") ; boss_2_recover_8=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Recover\LightBandit_Recover_7.png")
boss_2_recover_1=pygame.transform.scale(boss_2_recover_1,(75,85)) ; boss_2_recover_2=pygame.transform.scale(boss_2_recover_2,(75,85)) ; boss_2_recover_3=pygame.transform.scale(boss_2_recover_3,(75,85)) ; boss_2_recover_4=pygame.transform.scale(boss_2_recover_4,(75,85)) ; boss_2_recover_5=pygame.transform.scale(boss_2_recover_5,(75,85)) ; boss_2_recover_6=pygame.transform.scale(boss_2_recover_6,(75,85)) ; boss_2_recover_7=pygame.transform.scale(boss_2_recover_7,(75,85)) ; boss_2_recover_8=pygame.transform.scale(boss_2_recover_8,(75,85))
boss_2_recover_flip_1=pygame.transform.flip(boss_2_recover_1,True,False) ; boss_2_recover_flip_2=pygame.transform.flip(boss_2_recover_2,True,False) ; boss_2_recover_flip_3=pygame.transform.flip(boss_2_recover_3,True,False) ; boss_2_recover_flip_4=pygame.transform.flip(boss_2_recover_4,True,False) ; boss_2_recover_flip_5=pygame.transform.flip(boss_2_recover_5,True,False) ; boss_2_recover_flip_6=pygame.transform.flip(boss_2_recover_6,True,False) ; boss_2_recover_flip_7=pygame.transform.flip(boss_2_recover_7,True,False) ; boss_2_recover_flip_8=pygame.transform.flip(boss_2_recover_8,True,False)
boss_2_recover=[boss_2_recover_1,boss_2_recover_2,boss_2_recover_3,boss_2_recover_4,boss_2_recover_5,boss_2_recover_6,boss_2_recover_7,boss_2_recover_8]
boss_2_recover_flip=[boss_2_recover_flip_1,boss_2_recover_flip_2,boss_2_recover_flip_3,boss_2_recover_flip_4,boss_2_recover_flip_5,boss_2_recover_flip_6,boss_2_recover_flip_7,boss_2_recover_flip_8]

boss_2_fall_image=pygame.image.load(r"A_Wit's_End\Allies_1\Sprites\Light Bandit\Death\LightBandit_Death_0.png") ; boss_2_fall_image=pygame.transform.scale(boss_2_fall_image,(75,85)) ; boss_2_fall_flip_image=pygame.transform.flip(boss_2_fall_image,True,False)
boss_2_fall=[boss_2_fall_image]
boss_2_fall_flip=[boss_2_fall_flip_image]


boss_2_attack_number=[0] ; boss_2_recover_number=[0] ; boss_2_rise_number=[0]

boss_2_fall_right=False ; boss_2_fall_left=False

level_3_dialogue_boss_fight=False ; boss_one_fall_once=False ; level_3_dialogue_rise_boss=False ; enemy_stage_two=False

level_3_part_2_lose_dialogue=False ; level_3_dialogue_part_9_once=False
level_3_part_2_win_dialogue=False ; level_3_dialogue_part_10_once=False 
level_3_dialogue_part_11_once=False

level_3_fade_level_2=[0] ; level_3_part_3=False

level_4_tile_set=load_pygame(r"A_Wit's_End\Level 4_Tileset\tile_set_level_4_test.tmx")
level_4_tile_set_rect=[]



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
            font_game=pygame.font.SysFont("Impact",36)  ; show_game=font_game.render("A_Wit's_End ",1,(120,159,179))  ; SCREEN.blit(show_game,(SCREEN_WIDTH//2-75,100))
            rectangle_play=pygame.Surface((60,30))  ; rectangle_play.set_alpha(0)  ; rectangle_play.fill((200,200,200)) ; rect_play_show=SCREEN.blit(rectangle_play,(SCREEN_WIDTH//2-25,405))
            font_game=pygame.font.SysFont("Impact",36)  ; show_game=font_game.render("Play",1,(120,159,179))  ; SCREEN.blit(show_game,(SCREEN_WIDTH//2-25,400))

            if pygame.Rect.collidepoint(rect_play_show,pygame.mouse.get_pos()) and event.type==pygame.MOUSEBUTTONDOWN: level_screen=True

    def level_selection(self):
        self.camera_x_y=camera_x_y ; self.player_rect=player_rect
        global level_screen, level_1, level_2, level_2_part_2, level_3, level_4 , level_3_part_3
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
            rectangle_level_3=pygame.Surface((60,90))    
            """rectangle_level_1.set_alpha(0)""" ; rectangle_level_3.fill((50,50,50))  ; rectangle_level_3=SCREEN.blit(rectangle_level_3,(SCREEN_WIDTH//2+150,SCREEN_HEIGHT//2-50))    
            rectangle_level_4=pygame.Surface((60,90))    
            """rectangle_level_1.set_alpha(0)""" ; rectangle_level_4.fill((20,20,20))  ; rectangle_level_4=SCREEN.blit(rectangle_level_4,(SCREEN_WIDTH//2+250,SCREEN_HEIGHT//2-50))           
            if pygame.Rect.collidepoint(rectangle_level_1,pygame.mouse.get_pos()) and event.type==pygame.MOUSEBUTTONDOWN:
                level_scren=False ; level_1=True ; level_2=False ; level_3=False ; level_4=False
            if pygame.Rect.collidepoint(rectangle_level_2,pygame.mouse.get_pos()) and event.type==pygame.MOUSEBUTTONDOWN:
                level_scren=False ; level_1=False ; level_2=True ; level_3=False ; level_4=False
            if pygame.Rect.collidepoint(rectangle_level_3,pygame.mouse.get_pos()) and event.type==pygame.MOUSEBUTTONDOWN:
                level_scren=False ; level_1=False ; level_2=False ; level_3=True ; level_4=False
            if pygame.Rect.collidepoint(rectangle_level_4,pygame.mouse.get_pos()) and event.type==pygame.MOUSEBUTTONDOWN:
                level_scren=False ; level_1=False ; level_2=False ; level_3=False ; level_4=True
                self.player_rect.x=20 ; self.player_rect.y=200
        if level_1:
            level_screen=False
            if key[pygame.K_r]:
                level_1=False ; level_screen=True ; level_2=False ; reset_enemy_position=True ; level_3=False ; level_2_part_2=False ; level_4=False
        if level_2 or level_2_part_2:
            level_screen=False
            if key[pygame.K_r]:
                level_2=False ; level_2_part_2=False ; level_screen=True ; level_1=False ; level_3=False ; reset_enemy_position=True ; level_4=False
        if level_3: #change to level_3
            level_screen=False
            if key[pygame.K_r]:
                level_3=False ; level_2_part_2=False ; level_screen=True ; level_1=False ; level_2=False ; reset_enemy_position=True ; level_4=False
        if level_4:
            level_screen=False
            if key[pygame.K_r]:
                level_3=False ; level_2_part_2=False ; level_screen=True ; level_1=False ; level_2=False ; reset_enemy_position=True ; level_4=False
                
class Game:
    def __init__(self,level_1_bg,tile_level_1,camera_x_y,tile_level_1_rect,tile_level_2,tile_level_2_rect,tile_level_3,tile_level_3_rect,level_3_tile_set_part_2,level_3_tile_set_part_2_rect,level_4_tile_set,level_4_tile_set_rect):
        self.level_1_bg=level_1_bg ; self.tile_level_1=tile_level_1 ; self.camera_x_y=camera_x_y ; self.tile_level_1_rect=tile_level_1_rect
        self.tile_level_2=tile_level_2; self.tile_level_2_rect=tile_level_2_rect ; self.tile_level_3=tile_level_3 ; self.tile_level_3_rect=tile_level_3_rect
        self.level_3_tile_set_part_2=level_3_tile_set_part_2 ; self.level_3_tile_set_part_2_rect=level_3_tile_set_part_2_rect ; self.level_4_tile_set=level_4_tile_set ; self.level_4_tile_set_rect=level_4_tile_set_rect
    
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
        self.enemy_1_health_list=enemy_1_health_list ; self.enemy_two_health=enemy_two_health ; self.win_blur=win_blur ; self.boss_1_health=boss_1_health
        self.enemy_1_x_movement=enemy_1_x_movement
        global level_1,level_win, level_2, level_3, reset_enemy_position,level_2_part_2,level_2_dialogue_part_two_once,level_3_part_3
        if level_1 and all(idx<=0 for idx in self.enemy_1_health_list) and all(idx<=0 for idx in self.enemy_two_health) and self.player_rect.x>=6050:
            level_win=True
        if level_2_part_2 and self.boss_1_health[0]<=0 and self.player_rect.x>=6050:
            level_win=True
        if level_3_part_3 and all(idx<=0 for idx in self.enemy_1_health_list) and self.player_rect.x>=5250:
            level_win=True
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
                level_1=False ; level_2=False ; level_3=False ; reset_enemy_position=True ; level_2_part_2=False ; level_2_dialogue_part_two_once=False
                self.player_current_health[0]=1000  ; level_1_enemy_fight_condition=False ; level_win=False ; level_3_part_3=False

            if pygame.Rect.collidepoint(rectangle_main_menu,pygame.mouse.get_pos()) and event.type==pygame.MOUSEBUTTONDOWN:
                level_selection=False ; level_1=False ; level_screen=False ; self.player_current_health[0]=1000 ; player_death=False ; reset_enemy_position=True
                level_1_enemy_fight_condition=False ; level_2_dialogue_part_two_once=False         
                level_2=False ; level_3=False  ; level_2_part_2=False ; level_win=False; level_3_part_3=False
                
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
        self.level_2_tile_index=level_2_tile_index ; self.player_current_health=player_current_health ; self.enemy_1_health_list=enemy_1_health_list
        

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
               # self.player_rect.y=200
                if self.player_rect.x<210:
                    self.player_rect.x=210
                if self.player_rect.x>=210 and self.player_rect.x<=5300:
                    self.camera_x_y[0]+=self.player_rect.x-self.camera_x_y[0]-210
                if self.player_rect.y>800:
                    self.player_current_health[0]-=100
                    if self.player_current_health[0]<0:
                        self.player_rect.y=795
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
                
                if self.player_rect.x>5300 and not level_2_dialogue_part_two_once and any(idx<=0 for idx in self.enemy_1_health_list):
                    level_2_part_2_boss_dialogue=True
                    
            if level_2 or level_2_part_2:
                health_icons=pygame.draw.rect(SCREEN,(165,42,42),pygame.Rect(10,10,self.player_current_health[0]/self.health_bar_ratio,25))
                SCREEN.blit(self.health_icon,(15,12))
                health_border=pygame.draw.rect(SCREEN,(220,220,220),pygame.Rect(10,10,self.health_bar_length,25),4) 
                    
    def level_two_dialogue(self):
        #here
        global level_2, level_2_part_2, level_2_dialogue_part_one,dialogue_move_condition,change_dialogue_cond_1,change_dialogue,end_dialogue,level_2_dialogue_part_one_once
        global level_2_dialogue_part_two,level_2_dialogue_once_two,level_2_part_2_boss_dialogue, level_2_dialogue_part_two_once,level_2_dialogue_part_three_once,level_2_dialogue_part_four_once
        global level_2_part_win_boss_dialogue, level_2_part_lose_boss_dialogue
        self.general_boss_icon=general_boss_icon ; self.level_2_dialogue_list_part_1_length=level_2_dialogue_list_part_1_length ; self.player_icon=player_icon ; self.enemy_one_icon=enemy_one_icon
        self.level_2_blur_list_2=level_2_blur_list_2 ; self.boss_1_icon=boss_1_icon ; self.player_current_health=player_current_health ; self.boss_1_health=boss_1_health

        self.level_2_dialogue_list_part_1=[
        ("I don't want to have to do this!","You",self.player_icon),
        ("Do what? I have heard of your defection and the warrant for your arrest! I stand with you!","General Lopen",self.general_boss_icon),
        ("What? Are you against Kornos now?","You",self.player_icon),
        ("Yes, I have made a clear order for my men to stage a coup against him! Do you want to help?","General Lopen",self.general_boss_icon),
        ("What is your request?","You",self.player_icon),
        ("I know Kornos's location. If you are intrested, are you willing to deal with him?","General Lopen",self.general_boss_icon),
        ("Yes, I want to end this tyrants regin! Where is he located?","You",self.player_icon),
        ("He is located at the District 10 Fortress. It is a good area to hide, so he wont expect you there!.","General Lopen",self.general_boss_icon),
        ("I will deal with him in the same way he dealt with Onis....","You",self.player_icon)
        ]
        
        self.level_2_dialogue_list_part_2=[
        ("He fell for it! Get him!!!","Knight",self.enemy_one_icon),
        ("Wait what!?","You",self.player_icon)
        ]
        
        self.level_2_dialogue_list_3=[
        ("HehHAHAAHA, YOu've aRrived!!!","???",self.boss_1_icon),
        ("Are you ok? Who are you? Where is Kornos!?","You",self.player_icon),
        ("iM Fine, ThANK yoU fOr asKINg...My nAmE is HIgH LoRD STepHeN...... He IS noT HERE!!","High Lord Stephen",self.boss_1_icon),
        ("Did Kornos do this to you?","You",self.player_icon),
        ("He GaVE mE pOWerS onE caNNOT ImagINE, lOOK aT thE pOTionS aROUnd hERE, yoU FOOL!!","High Lord Stephen",self.boss_1_icon),
        ("I assume you want me to surrender right?","You",self.player_icon),
        ("YeS, YES, yES, YES!!!!! IT is EaSiER tHAt wAY, oR I wILL FORcE yOU tO SURrenDER!","High Lord Stephen",self.boss_1_icon),
        ("Force me then.....","You",self.player_icon)
        ]

        self.level_2_dialogue_list_lose=[
        ("YoU'RE tO wEAK tO UnDERstAnD ReAL POWER!!!!!!!!","High Lord Stephen",self.boss_1_icon)
        ]

        self.level_2_dialogue_list_win=[
        ("NOOO, WHAT HAVE YOU DONE TO ME!!!! NOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!!!","High Lord Stephen",self.boss_1_icon)
        ]

        if level_2_dialogue_part_one or level_2_dialogue_part_two and self.level_2_blur_list_2[0]<=0 or level_2_part_2_boss_dialogue or level_2_part_lose_boss_dialogue or level_2_part_win_boss_dialogue:
            
            
            if level_2_dialogue_part_one:
                level_2_dialogue=self.level_2_dialogue_list_part_1 ; colour_box=(1,50,32) ; colour_font=(1,150,71)
            if level_2_dialogue_part_two:
                level_2_dialogue=self.level_2_dialogue_list_part_2 ; colour_box=(128,128,128) ; colour_font=(192,192,192)
            if level_2_part_2_boss_dialogue:
                level_2_dialogue=self.level_2_dialogue_list_3 ; colour_box=(128,128,128) ; colour_font=(192,192,192)
            if level_2_part_lose_boss_dialogue:
                level_2_dialogue=self.level_2_dialogue_list_lose ; colour_box=(128,128,128) ; colour_font=(192,192,192)
            if level_2_part_win_boss_dialogue:
                level_2_dialogue=self.level_2_dialogue_list_win ; colour_box=(128,128,128) ; colour_font=(192,192,192)
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
                    if level_2_part_lose_boss_dialogue : level_2_dialogue_part_three_once=True
                    if level_2_part_win_boss_dialogue: level_2_dialogue_part_four_once=True
                    level_2_dialogue_part_one=False ; level_2_dialogue_part_two=False ; level_2_part_2_boss_dialogue=False ; level_2_part_lose_boss_dialogue=False ; level_2_part_win_boss_dialogue=False
                    self.level_2_dialogue_list_part_1_length[0]=0 ;  dialogue_move_condition=False ;  level_2_dialogue_part_one_once=True
            
            if event.type==pygame.MOUSEBUTTONDOWN:  change_dialogue_cond_1=True
            if event.type==pygame.MOUSEBUTTONUP and change_dialogue_cond_1:
                change_dialogue_cond_1=False ; change_dialogue=True  
            if change_dialogue:
                change_dialogue=False ; self.level_2_dialogue_list_part_1_length[0]+=1

    def level_three(self):
        global level_3,level_screen,level_3_part_2,level_3_transition_1,level_3_dialogue_boss_fight,level_3_dialogue_part_7_once,reset_enemy_position,enemy_stage_two,level_3_part_3
        self.camera_x_y=camera_x_y ; self.player_x_movement=player_x_movement ; self.mouse_button_left_image=mouse_button_left_image ; self.level_3_fade_level_2=level_3_fade_level_2
        self.list_2_bg_y_pos=list_2_bg_y_pos ; self.level_3_hill_list=level_3_hill_list ; self.level_3_bg_list=level_3_bg_list ; self.level_3_door=level_3_door ; self.boss_2_level_3_health=boss_2_level_3_health
        self.level_3_hill_1=level_3_hill_1 ; self.level_3_hill_2=level_3_hill_2 ; self.level_3_hill_3=level_3_hill_3 ; self.level_3_hill_4=level_3_hill_4 ; self.level_3_hill_5=level_3_hill_5
        self.level_3_hill_6=level_3_hill_6 ; self.level_3_hill_7=level_3_hill_7 ; self.level_3_pillar_1=level_3_pillar_1 ; self.level_3_pillar_2=level_3_pillar_2 ; self.level_3_pillar_3=level_3_pillar_3
        self.level_3_fade_level=level_3_fade_level ; self.level_3_part_2_fade_intro=[140] ; self.level_3_bg_test=level_3_bg_test ; self.level_3_tile_1=level_3_tile_1 ; self.level_3_bg_part_2_list=level_3_bg_part_2_list
        if level_3 and not level_3_part_2:
            level_screen=False
            if self.player_rect.x>=100 and self.player_rect.x<4500: self.camera_x_y[0]+=self.player_rect.x-self.camera_x_y[0]-210
            if self.player_rect.x<15: self.player_rect.x=15    
            if self.player_rect.x>=4500: 
                self.camera_x_y[0]=4500-210 
                if self.player_rect.x>5300:
                    self.player_rect.x=5300
            if self.camera_x_y[0]<0: self.camera_x_y[0]=0

            self.level_3_hill_list=[(self.level_3_hill_3,100,545),(self.level_3_hill_1,400,505),(self.level_3_hill_2,700,590),(self.level_3_hill_3,1100,545),(self.level_3_hill_4,1400,505),(self.level_3_hill_5,1500,545),
                   (self.level_3_hill_4,1900,505),(self.level_3_hill_1,2100,505),(self.level_3_hill_2,2200,590),(self.level_3_hill_4,2400,505),(self.level_3_hill_2,2700,590),
                   (self.level_3_hill_1,2800,505),(self.level_3_hill_5,2900,545),(self.level_3_hill_3,3200,545),(self.level_3_hill_4,3300,505),(self.level_3_hill_2,3400,585),
                   (self.level_3_hill_6,3580,385),(self.level_3_hill_2,3900,590),(self.level_3_hill_4,4000,505),(self.level_3_hill_5,4100,545),
                   (self.level_3_hill_1,4300,505),(self.level_3_hill_4,4400,505),(self.level_3_hill_2,4500,590),(self.level_3_hill_4,5100,505),
                   (self.level_3_hill_5,5200,545),(self.level_3_hill_1,5250,505),(self.level_3_door,3850,550)]

            self.player_door_distance=math.sqrt(math.pow(self.player_rect.x-3850,2)+math.pow(self.player_rect.y-545,2))

            y_1=0
            for row in self.tile_level_3:  #48,43
                x_1=0
                for tile in row:
                    if tile in ["1","2"]:
                        SCREEN.blit(self.level_3_tile_1,(x_1*48-self.camera_x_y[0],y_1*43-self.camera_x_y[1]))
                    if tile!="0":
                        self.tile_level_3_rect.append(pygame.Rect((x_1*48,y_1*43,48,43)))
                    x_1+=1
                y_1+=1

            SCREEN.blit(self.level_3_bg_test,(-self.camera_x_y[0],0))
            SCREEN.blit(self.level_3_bg_test,(-self.camera_x_y[0]+1100,0))
            SCREEN.blit(self.level_3_bg_test,(-self.camera_x_y[0]+2200,0))
            SCREEN.blit(self.level_3_bg_test,(-self.camera_x_y[0]+3300,0))
            SCREEN.blit(self.level_3_bg_test,(-self.camera_x_y[0]+4400,0))
            
            for idx,hill in enumerate(self.level_3_hill_list):
                SCREEN.blit(self.level_3_hill_list[idx][0],(self.level_3_hill_list[idx][1]-self.camera_x_y[0],self.level_3_hill_list[idx][2]))


            if self.player_door_distance<75:
                SCREEN.blit(self.mouse_button_left_image,(3875-self.camera_x_y[0],500-self.camera_x_y[1]))
                font_game=pygame.font.SysFont("Impact",20)  ; show_font=font_game.render("to interact",1,(255,70,71))  
                SCREEN.blit(show_font,(3855-self.camera_x_y[0],470-self.camera_x_y[1]))
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if event.button==1:
                        level_3_transition_1=True

            if level_3_transition_1:
                self.level_3_fade_level[0]+=10 ; rectangle_blur=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))  ; rectangle_blur.set_alpha(self.level_3_fade_level[0])  ; rectangle_blur.fill((0,0,0))   ; SCREEN.blit(rectangle_blur,(0,0))
                if self.level_3_fade_level[0]>=200:
                    self.level_3_fade_level[0]=200
                    level_3_part_2=True
                    self.player_rect.x=200
                    self.camera_x_y[0]=0
                    self.player_rect.y=600

        if level_3_part_2 and not level_3_part_3: 
            self.player_rect.height=64
            level_3=False
          #  print(self.level_3_fade_level[0])
          #  self.level_3_fade_level[0]-=10 ; rectangle_blur=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))  ; rectangle_blur.set_alpha(self.level_3_fade_level[0]) ; rectangle_blur.fill((0,0,0))   ; SCREEN.blit(rectangle_blur,(0,0))
          #  if self.level_3_fade_level[0]<=0:
          #      self.level_3_fade_level[0]=0
            if self.player_rect.x>=100 and self.player_rect.x<4540: self.camera_x_y[0]+=self.player_rect.x-self.camera_x_y[0]-210
            if self.player_rect.x<15: self.player_rect.x=15    
            if self.player_rect.x>=4540: 
                self.camera_x_y[0]=4540-210 
                if self.player_rect.x>5375:
                    self.player_rect.x=5375
            if self.camera_x_y[0]<0: self.camera_x_y[0]=0

            if self.player_rect.x>4300 and not level_3_dialogue_part_7_once:
                level_3_dialogue_boss_fight=True

            if level_3_dialogue_part_7_once:
                if self.player_rect.x<4050:
                    self.camera_x_y[0]=4050-210 
                    self.player_rect.x=4050

            for idx,bg in enumerate(self.level_3_bg_part_2_list):
                SCREEN.blit(bg,(0,0))
        
            for layer in self.level_3_tile_set_part_2:
                for tile in layer.tiles():
                    x_val=tile[0]*32
                    y_val=tile[1]*32
                    SCREEN.blit(tile[2],(x_val-self.camera_x_y[0],y_val-self.camera_x_y[1]))
                    self.level_3_tile_set_part_2_rect.append(pygame.Rect((x_val,y_val,32,40)))
            
            self.level_3_fade_level[0]-=8 ; rectangle_blur=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))  ; rectangle_blur.set_alpha(self.level_3_fade_level[0]) ; rectangle_blur.fill((0,0,0))   ; SCREEN.blit(rectangle_blur,(0,0))
            if self.level_3_fade_level[0]<=0:
                self.level_3_fade_level[0]=0

        if level_3_part_2 and enemy_stage_two and self.boss_2_level_3_health[0]<=0:
            if self.player_rect.x>=5300:
                self.level_3_fade_level_2[0]+=10 ; rectangle_blur=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))  ; rectangle_blur.set_alpha(self.level_3_fade_level_2[0])  ; rectangle_blur.fill((0,0,0))   ; SCREEN.blit(rectangle_blur,(0,0))
                if self.level_3_fade_level_2[0]>=200:
                    level_3_part_3=True
                    self.player_current_health[0]=1000
                    self.player_rect.x=200
                    self.camera_x_y[0]=0
                    self.player_rect.y=570

        if level_3_part_3:
            self.player_rect.height=48
            level_3_part_2=False
            if self.player_rect.x>=100 and self.player_rect.x<4500: self.camera_x_y[0]+=self.player_rect.x-self.camera_x_y[0]-210
            if self.player_rect.x<15: self.player_rect.x=15    
            if self.player_rect.x>=4500: 
                self.camera_x_y[0]=4500-210 
                if self.player_rect.x>5300:
                    self.player_rect.x=5300
            if self.camera_x_y[0]<0: self.camera_x_y[0]=0

            y_1=0
            for row in self.tile_level_3:
                x_1=0
                for tile in row:
                    if tile in ["1","2"]:
                        SCREEN.blit(self.level_3_tile_1,(x_1*48-self.camera_x_y[0],y_1*43-self.camera_x_y[1]))
                    if tile!="0":
                        self.tile_level_3_rect.append(pygame.Rect((x_1*48,y_1*43,48,43)))
                    x_1+=1
                y_1+=1
            
            SCREEN.blit(self.level_3_bg_test,(-self.camera_x_y[0],0))
            SCREEN.blit(self.level_3_bg_test,(-self.camera_x_y[0]+1100,0))
            SCREEN.blit(self.level_3_bg_test,(-self.camera_x_y[0]+2200,0))
            SCREEN.blit(self.level_3_bg_test,(-self.camera_x_y[0]+3300,0))
            SCREEN.blit(self.level_3_bg_test,(-self.camera_x_y[0]+4400,0))

            self.hill_list_level_3_part_3=[
                (self.level_3_hill_2,200,590),(self.level_3_hill_4,500,505),(self.level_3_hill_3,1000,545),(self.level_3_hill_1,1200,505),(self.level_3_hill_5,1400,545),
                (self.level_3_hill_1,1500,505),(self.level_3_hill_4,1950,505),(self.level_3_hill_2,2100,590),(self.level_3_hill_4,2200,505),(self.level_3_hill_1,2350,505),
                (self.level_3_hill_5,2750,545),(self.level_3_hill_3,2900,545),(self.level_3_hill_2,3050,590),(self.level_3_hill_1,3100,505),(self.level_3_hill_3,3200,545),
                (self.level_3_hill_2,3300,590),(self.level_3_hill_4,3500,505),(self.level_3_hill_5,3700,545),(self.level_3_hill_3,4100,545),(self.level_3_hill_1,4400,505)
            ]

            for idx,hill in enumerate(self.hill_list_level_3_part_3):
                SCREEN.blit(self.hill_list_level_3_part_3[idx][0],(self.hill_list_level_3_part_3[idx][1]-self.camera_x_y[0],self.hill_list_level_3_part_3[idx][2]-self.camera_x_y[1]))

            self.level_3_fade_level_2[0]-=10 ; rectangle_blur=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))  ; rectangle_blur.set_alpha(self.level_3_fade_level_2[0])  ; rectangle_blur.fill((0,0,0))   ; SCREEN.blit(rectangle_blur,(0,0))
            if self.level_3_fade_level_2[0]<0:
                self.level_3_fade_level_2[0]=0

        if level_3 or level_3_part_2 or level_3_part_3:
            health_icons=pygame.draw.rect(SCREEN,(165,42,42),pygame.Rect(10,10,self.player_current_health[0]/self.health_bar_ratio,25))
            SCREEN.blit(self.health_icon,(15,12))
            health_border=pygame.draw.rect(SCREEN,(220,220,220),pygame.Rect(10,10,self.health_bar_length,25),4) 

    def level_three_dialogue(self):
        global level_3,level_3_part_2,level_3_dialogue_part_1,level_3_dialogue_part_1_once,level_3_dialogue_part_2_once,level_3_dialogue_boss_fight,level_3_dialogue_rise_boss
        global level_3_dialogue_part_3_once,level_3_dialogue_part_4_once,level_3_dialogue_part_5_once,level_3_dialogue_part_6_once,level_3_dialogue_part_7_once,level_3_dialogue_part_8_once
        global player_ally_one, player_ally_two,player_ally_three,player_ally_four, player_ally_five,enemy_stage_two,level_3_part_2_lose_dialogue,level_3_dialogue_part_9_once,level_3_part_3
        global dialogue_move_condition ,change_dialogue,change_dialogue_cond_1,enemy_stage_two,level_3_part_2_win_dialogue,level_3_dialogue_part_10_once,level_3_dialogue_part_11_once
        self.ally_1_icon=ally_1_icon ; self.player_icon=player_icon ; self.ally_1_level_3_part_2_idle_rect=ally_1_level_3_part_2_idle_rect ; self.boss_2_icon_level_3=boss_2_icon_level_3
        self.boss_2_level_3_health=boss_2_level_3_health ; self.player_current_health=player_current_health 

        self.level_3_dialogue_1=[

            ("Halt this moment!","???",self.ally_1_icon),
            ("I will end you if you try anything!!","You",self.player_icon),
            ("We know your cause quite well, as we to are working against Kornos. We are the Men of Ayus. ","Men of Ayus Trooper",self.ally_1_icon),
            ("Who is your leader? Can I speak to them?","You",self.player_icon),
            ("His name is the Great Alexandros of Hemmite. He is in our fortress ahead! But....","Men of Ayus Trooper",self.ally_1_icon),
            ("I will meet with this 'Great' leader of yours....","You",self.player_icon)
            ]

        self.ally_one_1_dialogue=[
            ("You are falling into a path of destruction. Only if you knew what you were doing.","Men of Ayus Trooper",self.ally_1_icon),
            ("You are falling into a path of destruction. Only if you knew what you were doing..","Men of Ayus Trooper",self.ally_1_icon),
            ("What do you mean?","You",self.player_icon),
            ("I've been here for a while now! I know the types that won't last. Just a fair warning though!","Men of Ayus Trooper",self.ally_1_icon)
        ]

        self.ally_one_2_dialogue=[
            ("Your time is done whether you move north or south, east or west...Its over for you.","Men of Ayus Trooper",self.ally_1_icon),
            ("Your time is done whether you move north or south, east or west...Its over for you.","Men of Ayus Trooper",self.ally_1_icon),
            ("You people are weird.....","You",self.player_icon)
        ]

        self.ally_one_3_dialogue=[
            ("You reak of arrogance.... Time will tell as I was once quite arrogant.","Men of Ayus Trooper",self.ally_1_icon),
            ("You reak of arrogance.... Time will tell as I was once quite arrogant.","Men of Ayus Trooper",self.ally_1_icon),
            ("Who are you?","You",self.player_icon),
            ("The one who was just like you.","Men of Ayus Trooper",self.ally_1_icon),
            ("That isn't very helpul.","You",self.player_icon)

        ]

        self.ally_one_4_dialogue=[
            ("Leave while you can, it is your only hope....","Men of Ayus Trooper",self.ally_1_icon),
            ("Leave while you can, it is your only hope....","Men of Ayus Trooper",self.ally_1_icon),
            ("Hope? What hope?","You",self.player_icon),
            ("Trust me it isnt worth it...","Men of Ayus Trooper",self.ally_1_icon),
        ]

        self.ally_one_5_dialogue=[
            ("He is ahead. But you will meet him where we are not. Alone...","Men of Ayus Trooper",self.ally_1_icon),
            ("He is ahead. But you will meet him where we are not. Alone...","Men of Ayus Trooper",self.ally_1_icon),
            ("Sounds good!","You",self.player_icon),
            ("Good luck, you'll need it.","Men of Ayus Trooper",self.ally_1_icon),
        ]

        self.boss_two_dialogue=[
            ("I was waiting with great anticipation for your arrival.","Alexandros of Hemmite",self.boss_2_icon_level_3),
            ("Who are you really? I'm assuming Kornos betrayed you at some point.","You",self.player_icon),
            ("Betryal is a weak way to describe it......","Alexandros of Hemmite",self.boss_2_icon_level_3),
            ("What did you do?","You",self.player_icon),
            ("I won't speak of it with you...yet.... But, would you like to work with me to end Kornos?","Alexandros of Hemmite",self.boss_2_icon_level_3),
            ("In what regards? I've been betrayed enough already at this point.","You",self.player_icon),
            ("You would have to join my army, and we can begin operations against Kornos at Fort Creed.","Alexandros of Hemmite",self.boss_2_icon_level_3),
            ("Is he actaully at Fort Creed?","You",self.player_icon),
            ("Yes, but you have to accept my offer or else....","Alexandros of Hemmite",self.boss_2_icon_level_3),
            ("Else what?","You",self.player_icon),
            ("Your death.....There is no way out of this....","Alexandros of Hemmite",self.boss_2_icon_level_3),
            ("You can try to end me but it won't work in your favour.","You",self.player_icon),
        ]

        self.boss_two_rise_dialogue=[
            ("YOU THOUGHT YOU COULD BEAT ME! NEVER!!!!!!!","Alexandros of Hemmite",self.boss_2_icon_level_3),
            ("WAIT WHAT?","You",self.player_icon)
        ]

        self.boss_two_lose_dialouge=[
            ("Your mind is weak and so was your strength....","Alexandros of Hemmite",self.boss_2_icon_level_3)
        ]

        self.boss_two_win_dialogue=[
            ("AHHHHHHHH","Alexandros of Hemmite",self.boss_2_icon_level_3),
            ("Finnaly you die","You",self.player_icon)
        ]

        self.level_3_part_3_dialogue=[
            ("Fortress 10 is nearby and should be heavily guarded.... Kornos will not survive","You",self.player_icon),
            ("Fortress 10 is nearby and should be heavily guarded.... Kornos will not survive","You",self.player_icon)
        ]

        if level_3 and not level_3_part_2 and not level_3_dialogue_part_1_once:
            if self.player_rect.x>1400:
                level_3_dialogue_part_1=True

        if level_3_part_2 and self.player_current_health[0]<=0 and not level_3_dialogue_part_9_once:
            level_3_part_2_lose_dialogue=True
            level_3_dialogue_part_9_once=False

        if enemy_stage_two and self.boss_2_level_3_health[0]<=0 and not level_3_dialogue_part_10_once:
            level_3_part_2_win_dialogue=True
            level_3_dialogue_part_10_once=False
        
        if level_3_dialogue_part_1 or player_ally_one  or player_ally_two or player_ally_three or player_ally_four or player_ally_five or level_3_dialogue_boss_fight or level_3_dialogue_rise_boss or level_3_part_2_lose_dialogue or level_3_part_2_win_dialogue or (level_3_part_3 and not level_3_dialogue_part_11_once):
            if level_3_dialogue_part_1:
                level_3_dialogue=self.level_3_dialogue_1 ; colour_box=(1,50,32) ; colour_font=(1,150,71)
            if player_ally_one and not level_3_dialogue_part_2_once:
                level_3_dialogue=self.ally_one_1_dialogue ; colour_box=(119,136,153) ; colour_font=(112,128,144)
            if player_ally_two and not level_3_dialogue_part_3_once:
                level_3_dialogue=self.ally_one_2_dialogue ; colour_box=(119,136,153)  ; colour_font=(112,128,144)
            if player_ally_three and not level_3_dialogue_part_4_once:
                level_3_dialogue=self.ally_one_3_dialogue ; colour_box=(119,136,153) ; colour_font=(112,128,144)
            if player_ally_four and not level_3_dialogue_part_5_once:
                level_3_dialogue=self.ally_one_4_dialogue ; colour_box=(119,136,153)  ; colour_font=(112,128,144)
            if player_ally_five and not level_3_dialogue_part_6_once:
                level_3_dialogue=self.ally_one_5_dialogue ; colour_box=(119,136,153)  ; colour_font=(112,128,144)
            if level_3_dialogue_boss_fight and not level_3_dialogue_part_7_once:
                level_3_dialogue=self.boss_two_dialogue ; colour_box=(119,136,153)  ; colour_font=(112,128,144)
            if level_3_dialogue_rise_boss and not level_3_dialogue_part_8_once:
                level_3_dialogue=self.boss_two_rise_dialogue ; colour_box=(119,136,153)  ; colour_font=(112,128,144)
            if level_3_part_2_lose_dialogue and not level_3_dialogue_part_9_once:
                level_3_dialogue=self.boss_two_lose_dialouge ; colour_box=(119,136,153)  ; colour_font=(112,128,144)
            if level_3_part_2_win_dialogue and not level_3_dialogue_part_10_once:
                level_3_dialogue=self.boss_two_win_dialogue ; colour_box=(119,136,153)  ; colour_font=(112,128,144)
            if level_3_part_3 and not level_3_dialogue_part_11_once:
                level_3_dialogue=self.level_3_part_3_dialogue ; colour_box=(1,50,32) ; colour_font=(1,150,71)
            
            dialogue_move_condition=True ; rectangle_blur=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))  ; rectangle_blur.set_alpha(100) ; rectangle_blur.fill((0,0,0))  ; SCREEN.blit(rectangle_blur,(0,0)) 
            rectangle_box_1=pygame.Surface((SCREEN_WIDTH,200))  ; rectangle_box_1.fill(colour_box)  ; rectangle_box_1.set_alpha(75)  ; SCREEN.blit(rectangle_box_1,(0,500))
            
            for idx, number in enumerate(level_3_dialogue):
            
                if idx==self.level_2_dialogue_list_part_1_length[0]:
                    SCREEN.blit(level_3_dialogue[idx][2],(80,525))  ; font_game=pygame.font.SysFont("Impact",28) 
                    show_font_knight=font_game.render(level_3_dialogue[idx][1],1,colour_font) 
                    if level_3_dialogue[idx][2]==self.player_icon: SCREEN.blit(show_font_knight,(110,645))
                    if level_3_dialogue[idx][1]=="Men of Ayus Trooper": SCREEN.blit(show_font_knight,(55,645))  
                    if level_3_dialogue[idx][1]=="???": SCREEN.blit(show_font_knight,(115,645)) 
                    if level_3_dialogue[idx][1]=="High Lord Stephen": SCREEN.blit(show_font_knight,(55,645)) 
                    if level_3_dialogue[idx][1]=="Alexandros of Hemmite": SCREEN.blit(show_font_knight,(50,645))  
                    font_game=pygame.font.SysFont("Impact",24) ; show_font_knight=font_game.render(level_3_dialogue[idx][0],1,colour_font) ; SCREEN.blit(show_font_knight,(200,545))
                
                if self.level_2_dialogue_list_part_1_length[0]>=len(level_3_dialogue):
                    level_3_dialogue_part_1=False ; level_3_dialogue_part_1_once=True
                    self.level_2_dialogue_list_part_1_length[0]=0 ;  dialogue_move_condition=False 
                    if player_ally_one : level_3_dialogue_part_2_once=True
                    player_ally_one=False
                    if player_ally_two : level_3_dialogue_part_3_once=True
                    player_ally_two=False
                    if player_ally_three : level_3_dialogue_part_4_once=True
                    player_ally_three=False
                    if player_ally_four : level_3_dialogue_part_5_once=True
                    player_ally_four=False
                    if player_ally_five : level_3_dialogue_part_6_once=True
                    player_ally_five=False
                    if level_3_dialogue_boss_fight: level_3_dialogue_part_7_once=True
                    level_3_dialogue_boss_fight=False
                    if level_3_dialogue_rise_boss: 
                        level_3_dialogue_part_8_once=True
                        self.boss_2_level_3_health[0]=1000
                    level_3_dialogue_rise_boss=False 
                    if level_3_part_2_lose_dialogue: level_3_dialogue_part_9_once=True
                    level_3_part_2_lose_dialogue=False  
                    if level_3_part_2_win_dialogue: level_3_dialogue_part_10_once=True
                    level_3_dialogue_rise_boss=False
                    level_3_part_2_win_dialogue=False
                    if level_3_part_3: level_3_dialogue_part_11_once=True

            if event.type==pygame.MOUSEBUTTONDOWN:  change_dialogue_cond_1=True
            if event.type==pygame.MOUSEBUTTONUP and change_dialogue_cond_1:
                change_dialogue_cond_1=False ; change_dialogue=True  
            if change_dialogue:
                change_dialogue=False ; self.level_2_dialogue_list_part_1_length[0]+=1

    def level_four(self):
        self.camera_x_y=camera_x_y
        global level_4
        if level_4:
            self.player_rect.width=31
            self.player_rect.height=45
            SCREEN.fill((39,38,56))
            for layer in self.level_4_tile_set:
                if layer.name=="Tile Layer 1":
                        for tile in layer.tiles():
                            x_val=tile[0]*16 ; y_val=tile[1]*16 ; SCREEN.blit(tile[2],(x_val-self.camera_x_y[0],y_val-self.camera_x_y[1]))
                            self.level_4_tile_set_rect.append(pygame.Rect((x_val,y_val,16,16)))
                if layer.name=="Tile Layer 2" or layer.name=="Tile Layer 3":
                        for tile in layer.tiles():
                            x_val=tile[0]*16 ; y_val=tile[1]*16 ; SCREEN.blit(tile[2],(x_val-self.camera_x_y[0],y_val-self.camera_x_y[1]))

            if self.player_rect.x>=100 and self.player_rect.x<4850: self.camera_x_y[0]+=self.player_rect.x-self.camera_x_y[0]-210
            if self.player_rect.x<20: self.player_rect.x=20   
            if self.player_rect.x>=4850: 
                self.camera_x_y[0]=4850-210 
                if self.player_rect.x>5685:
                    self.player_rect.x=5685
            if self.camera_x_y[0]<0: self.camera_x_y[0]=0

class Player(Game):
    def __init__(self,player_x_movement,player_y_movement,player_rect,player_current_health):
        self.player_x_movement=player_x_movement ; self.player_y_movement=player_y_movement ; self.player_current_health=player_current_health
        self.player_rect=player_rect
        super().__init__(level_1_bg,tile_level_1,camera_x_y,tile_level_1_rect,tile_level_2,tile_level_2_rect,tile_level_3,
                         tile_level_3_rect,level_3_tile_set_part_2,level_3_tile_set_part_2_rect,level_4_tile_set,level_4_tile_set_rect)
    
    def movement(self,player_idle,player_idle_flip,player_run,player_run_flip,player_jump,player_jump_flip):
        global level_1,jump,jump_condition,player_idle_right,player_idle_left,attack,crouch,dialogue_move_condition,player_death,level_2,level_3,level_3_part_2,level_4
        self.player_idle=player_idle ; self.player_idle_flip=player_idle_flip ; self.player_idle_number=player_idle_number ; self.player_jump=player_jump
        self.player_run_number=player_run_number; self.player_run=player_run ; self.player_run_flip=player_run_flip ; self.player_jump_flip=player_jump_flip
        self.player_jump_number=player_jump_number ; self.player_jump_length=player_jump_length 
        if (level_1 or level_2 or level_3 or level_3_part_2 or level_3_part_3 or level_4) and not player_death:
            if key[pygame.K_SPACE] and not crouch:
                jump=True
                attack=False
                
            if jump and jump_condition and not attack and not dialogue_move_condition:
                self.player_y_movement[0]=+0
                if self.player_jump_length[0]>=-17:
                    self.player_y_movement[0]=-9.50 #+=-7.50
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

                    SCREEN.blit(self.player_run[int(self.player_run_number[0])//2],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y+5)) ; self.player_run_number[0]+=1
                    if self.player_run_number[0]>10: 
                        self.player_run_number[0]=0
                    player_idle_right=True ; player_idle_left=False
                
                elif key[pygame.K_a] and not key[pygame.K_d]:
                    self.player_x_movement[0]=-20
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
                self.player_y_movement[0]=+10
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

      #  if level_3_part_2:
      #      if key[pygame.K_d]:
      #          self.player_x_movement[0]=2
      #      if key[pygame.K_a]:
      #          self.player_x_movement[0]=-2
      #      self.player_y_movement[0]=2
      #      pygame.draw.rect(SCREEN,(200,200,200),pygame.Rect(player_rect.x-self.camera_x_y[0],player_rect.y-self.camera_x_y[1],35,60),width=1)
      #      SCREEN.blit(self.player_jump_flip[0],(self.player_rect.x-self.camera_x_y[0],self.player_rect.y+5))          
                 
    def attack(self,player_attack_type_1,player_attack_type_1_flip,player_attack_type_2,player_attack_type_2_flip,
              player_attack_type_3,player_attack_type_3_flip,player_attack_type_4,player_attack_type_4_flip,attack_jump,attack_jump_flip):
        self.player_attack_type_1=player_attack_type_1 ; self.player_attack_type_1_flip=player_attack_type_1_flip ; self.player_attack_type_2=player_attack_type_2 
        self.player_attack_type_2_flip=player_attack_type_2_flip ; self.player_attack_type_3=player_attack_type_3 ; self.player_attack_type_3_flip=player_attack_type_3_flip
        self.player_attack_type_4=player_attack_type_4 ; self.player_attack_type_4_flip=player_attack_type_4_flip ; self.attack_type=attack_type ; self.player_attack_number=player_attack_number
        self.attack_jump=attack_jump ; self.attack_jump_flip=attack_jump_flip ; self.player_attack_jump_number=player_attack_jump_number
        global attack,jump,jump_condition,player_idle_right,player_idle_left,attack_air, player_death,dialogue_move_condition, attack_done
        if (level_1 or level_2_part_2 or level_3 or level_3_part_2 or level_3_part_3) and not player_death and not dialogue_move_condition:
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
        global level_1_dialogue_part_two, end_level_1_dialogue,level_one_dialogue_part_three,end_level_1_dialogue,dialogue_move_condition, level_2_part_2,level_3_part_2
        global level_3,level_3_part_3
        self.player_fallen=player_fallen ; self.player_fallen_flip=player_fallen_flip ; self.player_fallen_number=player_fallen_number ; self.defeat_blur=defeat_blur
        if level_1 or level_2_part_2 or level_3 or level_3_part_2 or level_3_part_3:
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
                    level_1_enemy_fight_condition=False ; level_3_part_2=False ; level_3=False
                    
    def reset_position(self):
        global level_1, reset_enemy_position,level_one_x_border,level_3_part_2,level_3_dialogue_boss_fight,level_3_dialogue_part_7_once
        if (level_1 and reset_enemy_position) or (level_2_part_2 and reset_enemy_position) or (level_3_part_2 and reset_enemy_position):
            level_one_x_border=False
            if level_1 and reset_enemy_position:
                self.player_rect.x=100
            if level_2 and reset_enemy_position:
                self.player_rect.x=210
                self.player_rect.y=500
            if level_2_part_2 and reset_enemy_position:
                self.player_rect.x=210
                self.player_rect.y=500
                self.player_current_health[0]=1000
            if level_3_part_2 and reset_enemy_position:
                print("HERE")
                level_3_dialogue_boss_fight=False
                level_3_dialogue_part_7_once=False
                self.player_rect.x=210
                self.player_rect.y=200
                self.player_current_health[0]=1000
               # reset_enemy_position=False

    def collision_with_object(self,tile_level_1_rect,tile_level_2_rect,tile_level_3_rect,level_3_tile_set_part_2_rect,level_4_tile_set_rect):
        global level_2_part_2, level_3,level_3_part_2,level_3_part_3,level_4
        if level_1:
            tile_level=self.tile_level_1_rect
        if level_2_part_2:
            tile_level=self.tile_level_2_rect
        if level_3 or level_3_part_3:
            tile_level=self.tile_level_3_rect
        if level_3_part_2:
            tile_level=self.level_3_tile_set_part_2_rect
        if level_4:
            tile_level=self.level_4_tile_set_rect
        if level_1 or level_2_part_2 or level_3 or level_3_part_2 or level_3_part_3 or level_4:
            tile_hit=[]
            for tiles in tile_level:
                if self.player_rect.colliderect(tiles):
                    tile_hit.append(tiles)
            return tile_hit

    def collision_with_object_logic(self,tile_level_1_rect,tile_level_2_rect,tile_level_3_rect,level_3_tile_set_part_2_rect,level_4_tile_set_rect):
        global jump_condition,level_2_part_2,level_3,level_3_part_2,level_3_part_3,level_4
        if level_1 or level_2_part_2 or level_3 or level_3_part_2 or level_3_part_3 or level_4:
            self.player_rect.x+=self.player_x_movement[0]
            collision=Player.collision_with_object(self,tile_level_1_rect,tile_level_2_rect,tile_level_3_rect,level_3_tile_set_part_2_rect,level_4_tile_set_rect)
            for tile in collision:
                if self.player_x_movement[0]>0:
                    self.player_rect.right=tile.left
                elif self.player_x_movement[0]<0:
                    self.player_rect.left=tile.right
            self.player_rect.y+=self.player_y_movement[0]
            collision=Player.collision_with_object(self,tile_level_1_rect,tile_level_2_rect,tile_level_3_rect,level_3_tile_set_part_2_rect,level_4_tile_set_rect)
            for tile in collision:
                if self.player_y_movement[0]>0:
                    self.player_rect.bottom=tile.top
                    jump_condition=True
                elif self.player_y_movement[0]<0:
                    self.player_rect.top=tile.bottom
            return self.player_rect

class EnemyOne(Player):
    #here
    def __init__(self,enemy_list_level_1,npc_walk_length,npc_direction_choice,enemy_1_distance_list,enemy_1_health_list,enemy_1_level_3_rect,enemy_list_level_3):
        self.enemy_list_level_1=enemy_list_level_1 ;  self.npc_walk_length=npc_walk_length ; self.npc_direction_choice=npc_direction_choice ; self.enemy_1_distance_list=enemy_1_distance_list
        self.enemy_1_health_list=enemy_1_health_list ; self.enemy_1_level_3_rect=enemy_1_level_3_rect ; self.enemy_list_level_3=enemy_list_level_3
        super().__init__(player_x_movement,player_y_movement,player_rect,player_current_health)
    
    def move(self,enemy_1_level_1_rect,enemy_level_1_rect,enemy_1_level_1_rect_idle,enemy_1_x_movement,enemy_1_y_movement,enemy_1_level_2_rect):
        global level_1, level_1_enemy_fight_condition,x,y,off_x, level_2_part_2,level_3_part_3
        self.enemy_1_level_1_rect=enemy_1_level_1_rect ; self.enemy_1_walk=enemy_1_walk ; self.enemy_level_1_rect=enemy_level_1_rect ; self.enemy_1_level_1_rect_idle=enemy_1_level_1_rect_idle
        self.enemy_1_idle=enemy_1_idle ; self.enemy_1_walk_length=enemy_1_walk_length ; self.enemy_1_idle_length=enemy_1_idle_length ; self.enemy_1_idle_flip=enemy_1_idle_flip
        self.enemy_1_x_movement=enemy_1_x_movement ; self.enemy_1_y_movement=enemy_1_y_movement ; self.camera_x_y=camera_x_y ; self.enemy_1_walk_flip=enemy_1_walk_flip
        self.enemy_1_level_1_x=enemy_1_level_1_x ; self.enemy_type_1_level_1_x=enemy_type_1_level_1_x ; self.enemy_1_attack_length=enemy_1_attack_length ; self.attack_list=attack_list
        self.enemy_one_fall_number=enemy_one_fall_number ; self.enemy_one_fall_direction_set=enemy_one_fall_direction_set ; self.enemy_1_level_2_rect=enemy_1_level_2_rect
        self.tile_level_2_rect=tile_level_2_rect ; self.enemy_list_level_2=enemy_list_level_2 ; self.level_2_tile_index=level_2_tile_index ; self.tile_level_2_rect=tile_level_2_rect
        
        if level_1 or level_2_part_2 or level_3_part_3:
            if level_1: enemy_1_rect=self.enemy_level_1_rect
            if level_2_part_2 : enemy_1_rect=self.enemy_1_level_2_rect
            if level_3_part_3 : enemy_1_rect=self.enemy_1_level_3_rect
            for idx,knight in enumerate(enemy_1_rect):
                player_enemy_1_distance=math.sqrt(math.pow(self.player_rect.x-enemy_1_rect[idx].x,2)+math.pow(self.player_rect.y-enemy_1_rect[idx].y,2))
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

        if level_3_part_3:
            for idx,enemy_knight in enumerate(self.enemy_1_level_3_rect): self.enemy_list_level_3.append(pygame.Rect(enemy_knight.x,enemy_knight.y,45,55))
        
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
                if level_1 or level_2_part_2 and self.enemy_1_distance_list[idx]>200 and self.enemy_1_health_list[idx]>0:
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
           # if level_2_part_2 : enemy_1_rect=self.enemy_1_level_2_rect
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
            if level_2_part_2 and self.enemy_1_distance_list[idx]<=200 and self.enemy_1_distance_list[idx]>50: 
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
        
        for idx,enemy_knight in enumerate(self.enemy_1_level_3_rect):
            self.attack_list.append(False)
            if len(self.attack_list)>len(self.enemy_1_level_3_rect):
                del self.attack_list[-1]
            self.enemy_1_y_movement[0]=2
            if level_3_part_3 and self.enemy_1_distance_list[idx]<=900 and self.enemy_1_distance_list[idx]>50 and self.enemy_1_health_list[idx]>0:
                self.enemy_1_walk_length[0]+=0.20
                if self.enemy_1_walk_length[0]>10: self.enemy_1_walk_length[0]=0
                if self.player_rect.x>=enemy_knight.x:
                    self.enemy_1_x_movement[idx]=3
                    SCREEN.blit(self.enemy_1_walk[int(self.enemy_1_walk_length[0])//2],(enemy_knight.x-self.camera_x_y[0],enemy_knight.y-self.camera_x_y[1]+25)) 
                if self.player_rect.x<enemy_knight.x:
                    self.enemy_1_x_movement[idx]=-3
                    SCREEN.blit(self.enemy_1_walk_flip[int(self.enemy_1_walk_length[0])//2],(enemy_knight.x-self.camera_x_y[0],enemy_knight.y-self.camera_x_y[1]+25)) 
            if level_3_part_3 and self.enemy_1_distance_list[idx]>900:
                enemy_1_rect=self.enemy_1_level_3_rect
                if self.player_rect.x>enemy_knight.x: SCREEN.blit(self.enemy_1_idle[int(self.enemy_1_idle_length[0]//2)],(enemy_knight.x-self.camera_x_y[0],enemy_knight.y-self.camera_x_y[1]+25))
                else: SCREEN.blit(self.enemy_1_idle_flip[int(self.enemy_1_idle_length[0]//2)],(enemy_knight.x-self.camera_x_y[0],enemy_knight.y-self.camera_x_y[1]+25))
                self.enemy_1_idle_length[0]+=0.15
                if self.enemy_1_idle_length[0]>12: self.enemy_1_idle_length[0]=0

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
        self.enemy_1_attack=enemy_1_attack ; self.enemy_1_attack_flip=enemy_1_attack_flip ; self.enemy_1_attack_length=enemy_1_attack_length  ; self.attack_list=attack_list
        global level_1_enemy_fight_condition
        if level_1 and level_1_enemy_fight_condition or level_2_part_2 or level_3_part_3: #here
            if level_1: enemy_1_rect=self.enemy_level_1_rect
            if level_2_part_2 : enemy_1_rect=self.enemy_1_level_2_rect
            if level_3_part_3 : enemy_1_rect=self.enemy_1_level_3_rect
            for idx,knight in enumerate(enemy_1_rect):
                if  (level_1 and self.enemy_1_distance_list[idx]<50 and self.enemy_1_health_list[idx]>0) or (level_2_part_2 and self.enemy_1_distance_list[idx]<=50 and self.enemy_1_health_list[idx]>0) or (level_3_part_3 and self.enemy_1_distance_list[idx]<=50 and self.enemy_1_health_list[idx]>0):
                    self.enemy_1_x_movement[idx]=0
                    if level_3_part_3:
                        if self.player_rect.x>=enemy_1_rect[idx].x:
                            SCREEN.blit(self.enemy_1_attack[int(self.enemy_1_attack_length[idx])//2],(enemy_1_rect[idx].x-self.camera_x_y[0],enemy_1_rect[idx].y-self.camera_x_y[1]+10))
                        if self.player_rect.x<enemy_1_rect[idx].x:
                            SCREEN.blit(self.enemy_1_attack_flip[int(self.enemy_1_attack_length[idx])//2],(enemy_1_rect[idx].x-self.camera_x_y[0],enemy_1_rect[idx].y-self.camera_x_y[1]+10))
                    else:
                        if self.player_rect.x>=enemy_1_rect[idx].x:
                            SCREEN.blit(self.enemy_1_attack[int(self.enemy_1_attack_length[idx])//2],(enemy_1_rect[idx].x-self.camera_x_y[0],enemy_1_rect[idx].y-self.camera_x_y[1]))
                        if self.player_rect.x<enemy_1_rect[idx].x:
                            SCREEN.blit(self.enemy_1_attack_flip[int(self.enemy_1_attack_length[idx])//2],(enemy_1_rect[idx].x-self.camera_x_y[0],enemy_1_rect[idx].y-self.camera_x_y[1]))
                    self.enemy_1_attack_length[idx]+=0.50
                    if self.enemy_1_attack_length[idx]>9:
                        self.enemy_1_attack_length[idx]=0
                        self.player_current_health[0]-=50
    
    def player_hit(self):
        global level_1, attack,level_1_enemy_fight_condition,attack_done, player_idle_right, player_idle_left,level_2_part_2,level_3_part_3
        if level_1 or level_2_part_2 or level_3_part_3:
            if level_1: enemy_1_rect=self.enemy_level_1_rect
            if level_2_part_2 : enemy_1_rect=self.enemy_1_level_2_rect
            if level_3_part_3: enemy_1_rect=self.enemy_1_level_3_rect
            if attack_done and level_1_enemy_fight_condition or attack_done:
                for idx,knight in enumerate(enemy_1_rect):
                    if self.enemy_1_distance_list[idx]<50:
                        if player_idle_right and self.player_rect.x<=enemy_1_rect[idx].x:
                            self.enemy_1_health_list[idx]-=100 #25
                        if player_idle_left and self.player_rect.x>enemy_1_rect[idx].x:
                            self.enemy_1_health_list[idx]-=100
                        attack_done=False
                    if self.enemy_1_health_list[idx]<0:
                        self.enemy_1_x_movement[idx]=0
      
    def fall(self):
        global reset_enemy_position
        self.enemy_1_fall=enemy_1_fall ; self.enemy_1_fall_flip=enemy_1_fall_flip ; self.enemy_one_fall_number=enemy_one_fall_number
        if (level_1 or level_2_part_2 or level_3_part_3) and not reset_enemy_position:
            if level_1: enemy_1_rect=self.enemy_level_1_rect
            if level_2_part_2 : enemy_1_rect=self.enemy_1_level_2_rect ; self.cam_y_1=10 ; self.cam_y_2=45
            if level_3_part_3 : enemy_1_rect=self.enemy_1_level_3_rect ; self.cam_y_1=25 ; self.cam_y_2=60
            for idx,knight in enumerate(enemy_1_rect):
                if self.enemy_1_health_list[idx]<=0:
                    self.enemy_1_x_movement[idx]=0
                    self.enemy_1_health_list[idx]=0
                    if self.enemy_one_fall_direction_set[idx]==1:
                        if self.enemy_one_fall_number[idx]<16:
                            SCREEN.blit(self.enemy_1_fall[int(self.enemy_one_fall_number[idx])//2],(enemy_1_rect[idx].x-self.camera_x_y[0],knight.y-self.camera_x_y[1]+self.cam_y_1))
                        else:
                            self.enemy_one_fall_number[idx]=16  
                            SCREEN.blit(self.enemy_1_fall[int(self.enemy_one_fall_number[idx])//2],(enemy_1_rect[idx].x-self.camera_x_y[0],knight.y-self.camera_x_y[1]+self.cam_y_2))
                    if self.enemy_one_fall_direction_set[idx]==2:
                        if self.enemy_one_fall_number[idx]<16:
                            SCREEN.blit(self.enemy_1_fall_flip[int(self.enemy_one_fall_number[idx])//2],(enemy_1_rect[idx].x-self.camera_x_y[0],knight.y-self.camera_x_y[1]+self.cam_y_1))
                        else:
                            self.enemy_one_fall_number[idx]=16  
                            SCREEN.blit(self.enemy_1_fall_flip[int(self.enemy_one_fall_number[idx])//2],(enemy_1_rect[idx].x-self.camera_x_y[0],knight.y-self.camera_x_y[1]+self.cam_y_2))                           
                    self.enemy_one_fall_number[idx]+=0.50

    def reset_position(self):
        global reset_enemy_position,level_2_part_2,level_1,level_2_part_2
        self.enemy_1_level_1_x=enemy_1_level_1_x ; self.enemy_1_level_1_x_idle=enemy_1_level_1_x_idle ; self.enemy_1_level_2_x=enemy_1_level_2_x
        #here
        if reset_enemy_position:
            self.enemy_1_distance_list.clear() ; self.enemy_one_fall_number.clear() ; self.enemy_one_fall_direction_set.clear() ; self.enemy_1_x_movement.clear() ; self.enemy_1_attack_length.clear() ; self.enemy_1_health_list.clear()
            if level_1:
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
                
    def collision_with_object(self,tile_level_1,tile_level_2,tile_level_3_rect):
        self.level_2_tile_index=level_2_tile_index ; self.npc_direction_choice=npc_direction_choice
        if level_1 or level_2_part_2 or level_3_part_3:
            if level_1: enemy_1_rect=self.enemy_level_1_rect ; tile_level=self.tile_level_1_rect
            if level_2_part_2 : enemy_1_rect=self.enemy_1_level_2_rect ; tile_level=self.tile_level_2_rect
            if level_3_part_3: enemy_1_rect=self.enemy_1_level_3_rect ; tile_level=self.tile_level_3_rect
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
                                self.npc_direction_choice[idx]=1
                            if self.level_2_tile_index[index]=="17":
                                self.npc_direction_choice[idx]=2 
            return hit_tile
        
    def collision_with_object_logic(self,tile_level_1,tile_level_2,tile_level_3_rect):
        global level_1_enemy_fight_condition, level_2_part_2
        if level_1 or level_2_part_2 or level_3_part_3:
            if level_1: enemy_1_rect=self.enemy_level_1_rect ; enemy_list=self.enemy_list_level_1
            if level_2_part_2 : enemy_1_rect=self.enemy_1_level_2_rect ; enemy_list=self.enemy_list_level_2
            if level_3_part_3: enemy_1_rect=self.enemy_1_level_3_rect ; enemy_list=self.enemy_list_level_3
            for idx,enemy_knight in enumerate(enemy_1_rect):
                try:
                    enemy_knight.x+=self.enemy_1_x_movement[idx]
                except IndexError : pass
            collision=EnemyOne.collision_with_object(self,tile_level_1,tile_level_2,tile_level_3_rect)
            for idx,enemy_knight in enumerate(enemy_1_rect):
                enemy_knight.y+=self.enemy_1_y_movement[0]
            collision=EnemyOne.collision_with_object(self,tile_level_1,tile_level_2,tile_level_3_rect)
            for tile in collision:
                for idx,enemy_knight in enumerate(enemy_1_rect):
                    if enemy_knight.colliderect(tile):
                        enemy_knight.bottom=tile.top
            return enemy_list     
        
class EnemyTwo(Player):
    def __init__(self,enemy_two_level_1_rect,enemy_two_x_movement,enemy_two_y_movement,enemy_two_rect_list,enemy_two_distance_list,enemy_two_health,enemy_two_level_4_rect_1):
        self.enemy_two_level_1_rect=enemy_two_level_1_rect ; self.enemy_two_x_movement=enemy_two_x_movement ; self.enemy_two_y_movement=enemy_two_y_movement ; self.enemy_two_rect_list=enemy_two_rect_list
        self.enemy_two_distance_list=enemy_two_distance_list ; self.enemy_two_health=enemy_two_health ; self.enemy_two_level_4_rect_1=enemy_two_level_4_rect_1
        super().__init__(player_x_movement,player_y_movement,player_rect,player_current_health)
    
    def movement(self):
        global level_1, level_1_enemy_fight_condition,level_4,level_screen
        self.enemy_two_idle=enemy_two_idle ; self.enemy_two_idle_flip=enemy_two_idle_flip ; self.enemy_two_idle_number=enemy_two_idle_number ; self.enemy_two_run=enemy_two_run 
        self.enemy_two_run_flip=enemy_two_run_flip ; self.enemy_two_run_number=enemy_two_run_number ; self.enemy_two_level_1_x=enemy_two_level_1_x ; self.enemy_two_fall_number=enemy_two_fall_number
        self.enemy_two_fall_direction_set=enemy_two_fall_direction_set
        if level_screen:
            self.enemy_two_distance_list.clear() ; self.enemy_two_rect_list.clear() ; self.enemy_two_x_movement.clear() ; self.enemy_two_health.clear()
            self.enemy_two_fall_number.clear() ; self.enemy_two_fall_direction_set.clear()

        if level_1 or level_4:
            if level_1:
                enemy_rect=self.enemy_two_level_1_rect
            if level_4:
                enemy_rect=self.enemy_two_level_4_rect_1
            for idx,enemy_knight in enumerate(enemy_rect):
                enemy_two_player_distance=math.sqrt(math.pow(self.player_rect.x-enemy_knight.x,2)+math.pow(self.player_rect.y-enemy_knight.y,2))
                self.enemy_two_distance_list.append(enemy_two_player_distance) ; self.enemy_two_rect_list.append(pygame.Rect(enemy_knight.x,enemy_knight.y,45,55)) 
                self.enemy_two_x_movement.append(0) ; self.enemy_two_health.append(100), self.enemy_two_fall_number.append(0) ; self.enemy_two_fall_direction_set.append(0)
                #150
                if self.enemy_two_x_movement[idx]>0:
                    self.enemy_two_fall_direction_set[idx]=1
                if self.enemy_two_x_movement[idx]<0:
                    self.enemy_two_fall_direction_set[idx]=2
                    
                if len(self.enemy_two_distance_list)>len(enemy_rect):
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
            if level_4:
                
        
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
                        if player_idle_left and self.player_rect.x>self.enemy_two_level_1_rect[idx].x:
                            self.enemy_two_health[idx]-=25
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

class AllyOne(Player):
    def __init__(self,ally_1_x_movement,ally_1_y_movement,ally_1_level_3_part_1_idle_rect,ally_1_level_3_part_1_run_rect,ally_1_rect_list,
                 ally_1_level_3_part_2_idle_rect,ally_1_level_3_part_2_run_rect):
        super().__init__(player_x_movement,player_y_movement,player_rect,player_current_health)
        self.camera_x_y=camera_x_y ; self.ally_1_x_movement=ally_1_x_movement ; self.ally_1_y_movement=ally_1_y_movement
        self.ally_1_level_3_part_1_idle_rect=ally_1_level_3_part_1_idle_rect ; self.ally_1_level_3_part_1_run_rect=ally_1_level_3_part_1_run_rect
        self.ally_1_run_direction=ally_1_run_direction ; self.ally_1_run_length=ally_1_run_length ; self.ally_1_rect_list=ally_1_rect_list
        self.ally_1_level_3_part_2_idle_rect=ally_1_level_3_part_2_idle_rect ; self.ally_1_level_3_part_2_run_rect=ally_1_level_3_part_2_run_rect

    def idle(self):
        global level_3,level_3_part_2
        self.ally_1_idle=ally_1_idle ; self.ally_1_idle_flip=ally_1_idle_flip ; self.ally_1_idle_number=ally_1_idle_number

        if level_3 or level_3_part_2:
            if level_3:
                ally_total_list=self.ally_1_level_3_part_1_idle_rect+self.ally_1_level_3_part_1_run_rect
                ally_1_idle_list=ally_1_level_3_part_1_idle_rect
            if level_3_part_2:
                ally_total_list=self.ally_1_level_3_part_2_idle_rect+self.ally_1_level_3_part_2_run_rect
                ally_1_idle_list=self.ally_1_level_3_part_2_idle_rect
            for idx,ally in enumerate(ally_total_list):
                self.ally_1_rect_list.append(pygame.Rect(ally.x,ally.y,75,85))
                self.ally_1_y_movement.append(2)
            for idx,ally in enumerate(ally_1_idle_list):
                self.ally_1_idle_number.append(0) ; self.ally_1_y_movement.append(2)
                if level_3 or level_3_part_2:
                    self.ally_1_y_movement[idx]=2
                    if self.player_rect.x<ally_1_idle_list[idx].x:
                        SCREEN.blit(self.ally_1_idle[int(self.ally_1_idle_number[idx])//2],(ally_1_idle_list[idx].x-self.camera_x_y[0],ally.y-self.camera_x_y[1]+17))
                    if self.player_rect.x>=ally_1_idle_list[idx].x:
                        SCREEN.blit(self.ally_1_idle_flip[int(self.ally_1_idle_number[idx])//2],(ally_1_idle_list[idx].x-self.camera_x_y[0],ally.y-self.camera_x_y[1]+17))
                    self.ally_1_idle_number[idx]+=0.25
                    if self.ally_1_idle_number[idx]>5:
                        self.ally_1_idle_number[idx]=0
                    if level_3_part_2:
                        ally.height=95
            
    def run(self):
        global level_3,level_3_part_2
        self.ally_1_run=ally_1_run ; self.ally_1_run_flip=ally_1_run_flip ; self.ally_1_run_number=ally_1_run_number
        if level_3 or level_3_part_2:
            if level_3:
                ally_1_run_list=self.ally_1_level_3_part_1_run_rect
            if level_3_part_2:
                ally_1_run_list=self.ally_1_level_3_part_2_run_rect
            
            for idx,ally in enumerate(ally_1_run_list):
                self.ally_1_run_number.append(0)  ; self.ally_1_x_movement.append(0)
            for idx,ally in enumerate(ally_1_run_list):
                if self.ally_1_run_direction[idx]==1 and self.ally_1_run_length[idx]>0:
                    self.ally_1_x_movement[idx]=-2
                    SCREEN.blit(self.ally_1_run[int(self.ally_1_run_number[idx])//2],(ally.x-self.camera_x_y[0],ally.y-self.camera_x_y[1]+17))
                if self.ally_1_run_direction[idx]==0 and self.ally_1_run_length[idx]>0:
                    self.ally_1_x_movement[idx]=2
                    SCREEN.blit(self.ally_1_run_flip[int(self.ally_1_run_number[idx])//2],(ally.x-self.camera_x_y[0],ally.y-self.camera_x_y[1]+17))
                if level_3_part_2:
                    ally.height=95

            for idx,ally in enumerate(ally_1_run_list):
                self.ally_1_run_number[idx]+=0.40
                if self.ally_1_run_number[idx]>10:
                    self.ally_1_run_number[idx]=0
                self.ally_1_run_length[idx]-=0.5
                if self.ally_1_run_length[idx]<=0:
                    self.ally_1_run_direction[idx]=random.randint(0,1)
                    self.ally_1_run_length[idx]=random.randint(50,75)

    def player_interaction(self):
        global level_3_part_2,player_ally_one, player_ally_two,player_ally_three,player_ally_four, player_ally_five
        global level_3_dialogue_part_2_once, level_3_dialogue_part_3_once,level_3_dialogue_part_4_once,level_3_dialogue_part_5_once,level_3_dialogue_part_6_once
        self.ally_1_player_distance_list=ally_1_player_distance_list ; self.mouse_button_left_image=mouse_button_left_image
        if level_3_part_2:
            for idx,ally in enumerate(self.ally_1_level_3_part_2_idle_rect):
                self.player_ally_distance=math.sqrt(math.pow(self.player_rect.x-ally.x,2)+math.pow(self.player_rect.y-ally.y,2))
                self.ally_1_player_distance_list.append(self.player_ally_distance)
                if len(self.ally_1_player_distance_list)>len(self.ally_1_level_3_part_2_idle_rect):
                    del self.ally_1_player_distance_list[0]
            for idx,ally in enumerate(self.ally_1_level_3_part_2_idle_rect):
                if self.ally_1_player_distance_list[idx]<120:
                    SCREEN.blit(self.mouse_button_left_image,(ally.x-self.camera_x_y[0]+20,ally.y-self.camera_x_y[1]-45))
                    font_game=pygame.font.SysFont("Impact",20)  ; show_font=font_game.render("to interact",1,(255,70,71))  
                    SCREEN.blit(show_font,(ally.x-self.camera_x_y[0],ally.y-self.camera_x_y[1]-5))
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        if event.button==1:
                            if idx==0:
                                player_ally_one=True ; level_3_dialogue_part_2_once=False#
                            if idx==1:
                                player_ally_two=True ; level_3_dialogue_part_3_once=False
                            if idx==2:
                                player_ally_three=True ; level_3_dialogue_part_4_once=False
                            if idx==3:
                                player_ally_four=True ; level_3_dialogue_part_5_once=False
                            if idx==4:
                                player_ally_five=True ; level_3_dialogue_part_6_once=False

    def reset_position(self):
        global level_3_part_2, reset_enemy_position
        self.ally_1_level_3_part_2_x_run=ally_1_level_3_part_2_x_run ; self.ally_1_level_3_part_2_y_run=ally_1_level_3_part_2_y_run
        if level_3_part_2 and reset_enemy_position:
            for idx,ally in enumerate(self.ally_1_level_3_part_2_run_rect):
                self.ally_1_level_3_part_2_run_rect[idx].x=self.ally_1_level_3_part_2_x_run[idx]
                self.ally_1_level_3_part_2_run_rect[idx].y=self.ally_1_level_3_part_2_y_run[idx]

    def collision_with_object(self,tile_level_3,level_3_tile_set_part_2):
        global level_3,level_3_part_2
        if level_3:
            ally_1_rect=self.ally_1_level_3_part_1_idle_rect+self.ally_1_level_3_part_1_run_rect
            tile_lvl_3=self.tile_level_3_rect
        if level_3_part_2:
            ally_1_rect=self.ally_1_level_3_part_2_idle_rect+self.ally_1_level_3_part_2_run_rect
            tile_lvl_3=self.level_3_tile_set_part_2_rect
        if level_3 or level_3_part_2:
            hit_tile=[]
            for idx,ally_1 in enumerate(ally_1_rect):
                for tiles in tile_lvl_3:
                    if ally_1.colliderect(tiles):
                        hit_tile.append(tiles)
            return hit_tile
        
    def collision_with_object_logic(self,tile_level_3,level_3_tile_set_part_2):
        global level_3,level_3_part_2
        if level_3:
            ally_1_rect=self.ally_1_level_3_part_1_idle_rect+self.ally_1_level_3_part_1_run_rect
            ally_1_run_rect=self.ally_1_level_3_part_1_run_rect
        if level_3_part_2:
            ally_1_rect=self.ally_1_level_3_part_2_idle_rect+self.ally_1_level_3_part_2_run_rect
            ally_1_run_rect=self.ally_1_level_3_part_2_run_rect
        if level_3 or level_3_part_2:
            for idx,ally_1 in enumerate(ally_1_run_rect):
                ally_1.x+=self.ally_1_x_movement[idx]
            collision=AllyOne.collision_with_object(self,tile_level_3,level_3_tile_set_part_2)
            for idx,ally_1 in enumerate(ally_1_rect):
                ally_1.y+=self.ally_1_y_movement[idx]
            collision=AllyOne.collision_with_object(self,tile_level_3,level_3_tile_set_part_2)
            for tile in collision:
                for idx,ally_1 in enumerate(ally_1_rect):
                    if ally_1.colliderect(tile):
                        if self.ally_1_y_movement[idx]>0:
                            ally_1_rect[idx].bottom=tile.top
                        if self.ally_1_y_movement[idx]<0:
                            ally_1_rect[idx].top=tile.bottom
            return self.ally_1_rect_list  

class MainBoss(Player):
    def __init__(self,main_boss_rect_level_1,main_boss_x_movement,main_boss_y_movement,):
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
                
class BossOne(Player):
    def __init__(self,boss_1_rect,boss_1_level_2_part_2_x,boss_1_level_2_part_2_y,boss_1_x_movement,boss_1_y_movement,boss_1_health):
        super().__init__(player_x_movement,player_y_movement,player_rect,player_current_health)
        self.camera_x_y=camera_x_y ; self.boss_1_rect=boss_1_rect ; self.boss_1_level_2_part_2_x=boss_1_level_2_part_2_x ; self.boss_1_level_2_part_2_y=boss_1_level_2_part_2_y
        self.boss_1_x_movement=boss_1_x_movement ; self.boss_1_y_movement=boss_1_y_movement ; self.boss_1_rest_time=boss_1_rest_time ; self.boss_1_health=boss_1_health
    
    def idle(self):
        global level_2_part_2
        self.boss_1_idle_flip=boss_1_idle_flip ; self.boss_1_idle_number=boss_1_idle_number ; self.boss_1_level_2_part_2_x=boss_1_level_2_part_2_x ; self.boss_1_level_2_part_2_y=boss_1_level_2_part_2_y
        self.boss_1_attack_timer=boss_1_attack_timer ; self.boss_1_idle=boss_1_idle ; self.enemy_1_health_list=enemy_1_health_list
        if level_2_part_2:
            self.player_boss_1_distance=math.sqrt(math.pow(self.player_rect.x-self.boss_1_rect.x,2)+math.pow(self.player_rect.x-self.boss_1_rect.x,2))
        if level_2_part_2 and self.boss_1_health[0]>0 and any(idx<=0 for idx in self.enemy_1_health_list):
            if self.boss_1_attack_timer[0]<=0:
                self.boss_1_y_movement[0]=-1
                if self.boss_1_rest_time[0]>40:
                    self.boss_1_attack_timer[0]=200 ; self.boss_1_rest_time[0]=0
                self.boss_1_rest_time[0]+=0.50
            if self.boss_1_attack_timer[0]>0:
                self.boss_1_y_movement[0]=4
            if not level_2_dialogue_part_two_once or self.boss_1_attack_timer[0]<=0 and self.player_boss_1_distance<=50:
                if self.player_rect.x<self.boss_1_rect.x:
                    SCREEN.blit(self.boss_1_idle_flip[int(self.boss_1_idle_number[0])//2],(self.boss_1_rect.x-self.camera_x_y[0]-5,self.boss_1_rect.y-self.camera_x_y[1]-5))
                if self.player_rect.x>=self.boss_1_rect.x:
                    SCREEN.blit(self.boss_1_idle[int(self.boss_1_idle_number[0])//2],(self.boss_1_rect.x-self.camera_x_y[0]-5,self.boss_1_rect.y-self.camera_x_y[1]-5))
                self.boss_1_idle_number[0]+=0.50
                if self.boss_1_idle_number[0]>9: self.boss_1_idle_number[0]=0
             
    def move(self):
        global level_2_part_2, level_2_dialogue_part_two_once
        self.boss_1_move=boss_1_move ; self.boss_1_move_flip=boss_1_move_flip ; self.boss_1_move_number=boss_1_move_number ; self.boss_1_attack_timer=boss_1_attack_timer
        if level_2_dialogue_part_two_once and self.boss_1_health[0]>0:
            if self.player_boss_1_distance>50:
                if self.player_rect.x>=self.boss_1_rect.x:
                    SCREEN.blit(self.boss_1_move[int(self.boss_1_move_number[0])//2],(self.boss_1_rect.x-self.camera_x_y[0]-5,self.boss_1_rect.y-self.camera_x_y[1]-5))
                    self.boss_1_x_movement[0]=2
                if self.player_rect.x<self.boss_1_rect.x:
                    SCREEN.blit(self.boss_1_move_flip[int(self.boss_1_move_number[0])//2],(self.boss_1_rect.x-self.camera_x_y[0]-5,self.boss_1_rect.y-self.camera_x_y[1]-5))
                    self.boss_1_x_movement[0]=-2
                self.boss_1_move_number[0]+=0.50
                if self.boss_1_move_number[0]>10:
                    self.boss_1_move_number[0]=0  

    def attack(self):
        global level_2_dialogue_part_two_once
        self.boss_1_attack=boss_1_attack ; self.boss_1_attack_flip=boss_1_attack_flip ; self.boss_1_attack_number=boss_1_attack_number ; self.boss_1_attack_timer=boss_1_attack_timer
        if level_2_dialogue_part_two_once and self.boss_1_health[0]>0:
            if self.player_boss_1_distance<=50 and self.boss_1_attack_timer[0]>0:
                self.boss_1_x_movement[0]=0
                if self.player_rect.x>=self.boss_1_rect.x:
                    SCREEN.blit(self.boss_1_attack[int(self.boss_1_attack_number[0])//2],(self.boss_1_rect.x-self.camera_x_y[0]-5,self.boss_1_rect.y-self.camera_x_y[1]-5))
                if self.player_rect.x<self.boss_1_rect.x:
                    SCREEN.blit(self.boss_1_attack_flip[int(self.boss_1_attack_number[0])//2],(self.boss_1_rect.x-self.camera_x_y[0]-5,self.boss_1_rect.y-self.camera_x_y[1]-5))
                self.boss_1_attack_timer[0]-=2 ; self.boss_1_attack_number[0]+=0.50
                if self.boss_1_attack_number[0]>9: self.boss_1_attack_number[0]=0  
                self.player_current_health[0]-=2 #2  

    def health(self):
        global attack, level_2_dialogue_part_two_once, player_idle_right, player_idle_left,level_2_part_win_boss_dialogue,level_2_part_lose_boss_dialogue
        global level_2_dialogue_part_three_once, level_2_dialogue_part_four_once
        self.health_bar_length=500 ; self.maximum_health=1000 ; self.health_bar_ratio=self.maximum_health/self.health_bar_length ; self.health_icon=health_icon
        if level_2_dialogue_part_two_once:
            health_icons=pygame.draw.rect(SCREEN,(172,144,32),pygame.Rect(590,10,self.boss_1_health[0]/self.health_bar_ratio,25))
            SCREEN.blit(self.health_icon,(605,12))
            health_border=pygame.draw.rect(SCREEN,(220,220,220),pygame.Rect(590,10,self.health_bar_length,25),4) 
            if attack and self.player_boss_1_distance<100 and self.boss_1_attack_timer[0]>0:
                if player_idle_right and self.player_rect.x<self.boss_1_rect.x or player_idle_left and self.player_rect.x>=self.boss_1_rect.x:
                    self.boss_1_health[0]-=100    #5
            if boss_1_attack_timer[0]<=0:
                self.boss_1_health[0]+=1  
            if self.boss_1_health[0]>1000:
                self.boss_1_health[0]=1000
            if self.boss_1_health[0]<=0 and not level_2_dialogue_part_four_once:
                level_2_part_win_boss_dialogue=True
            if self.player_current_health[0]<=0 and not level_2_dialogue_part_three_once:
                level_2_part_lose_boss_dialogue=True

    def fall(self):
        global level_2_dialogue_part_two_once,boss_fall_right,boss_fall_left
        self.boss_1_fall=boss_1_fall ; self.boss_1_fall_flip=boss_1_fall_flip ; self.boss_1_fall_number=boss_1_fall_number
        if level_2_dialogue_part_two_once:
            if self.boss_1_health[0]<=0:
                self.boss_1_x_movement[0]=0
                if self.player_rect.x>self.boss_1_rect.x and self.boss_1_fall_number[0]<6:
                    SCREEN.blit(self.boss_1_fall[int(self.boss_1_fall_number[0])//2],(self.boss_1_rect.x-self.camera_x_y[0]-5,self.boss_1_rect.y-self.camera_x_y[1]+30))
                    boss_fall_right=True ; boss_fall_left=False
                if self.player_rect.x<=self.boss_1_rect.x:
                    SCREEN.blit(self.boss_1_fall_flip[int(self.boss_1_fall_number[0])//2],(self.boss_1_rect.x-self.camera_x_y[0]-5,self.boss_1_rect.y-self.camera_x_y[1]+30))
                    boss_fall_left=True ; boss_fall_right=False
                self.boss_1_fall_number[0]+=0.50
                if self.boss_1_fall_number[0]>=6:
                    self.boss_1_fall_number[0]=6
                    if boss_fall_right:
                        SCREEN.blit(self.boss_1_fall[int(self.boss_1_fall_number[0])//2],(self.boss_1_rect.x-self.camera_x_y[0]-5,self.boss_1_rect.y-self.camera_x_y[1]+30))
                    if boss_fall_left:
                        SCREEN.blit(self.boss_1_fall_flip[int(self.boss_1_fall_number[0])//2],(self.boss_1_rect.x-self.camera_x_y[0]-5,self.boss_1_rect.y-self.camera_x_y[1]+30))

    def reset_position(self):
        global level_2_part_2, reset_enemy_position,level_2_dialogue_part_two_once
        self.boss_1_level_2_part_2_x=boss_1_level_2_part_2_x; self.boss_1_level_2_part_2_y=boss_1_level_2_part_2_y
        if level_2_part_2 and reset_enemy_position:
            self.boss_1_rect.x=self.boss_1_level_2_part_2_x[0]
            self.boss_1_rect.y=self.boss_1_level_2_part_2_y[0]
            self.boss_1_x_movement[0]=0
            self.boss_1_health[0]=1000
            level_2_dialogue_part_two_once=False
            reset_enemy_position=False

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
                
class BossTwo(Player):
    #stage 1 boss two is kind of like a normal enemy but hits harder than enemy two. then
    # in stage 2 boss two is faster and hits alot harder than before. 
    def __init__(self,boss_2_level_3_x,boss_2_level_3_y,boss_2_level_3_x_movement,boss_2_level_3_y_movement,boss_2_level_3_rect,boss_2_level_3_health):
        super().__init__(player_x_movement,player_y_movement,player_rect,player_current_health)
        self.camera_x_y=camera_x_y
        self.boss_2_level_3_x=boss_2_level_3_x
        self.boss_2_level_3_y=boss_2_level_3_y
        self.boss_2_level_3_x_movement=boss_2_level_3_x_movement
        self.boss_2_level_3_y_movement=boss_2_level_3_y_movement
        self.boss_2_level_3_rect=boss_2_level_3_rect
        self.boss_2_level_3_health=boss_2_level_3_health
        self.health_icon=health_icon
        self.player_boss_two_distance=math.sqrt(math.pow(self.player_rect.x-self.boss_2_level_3_rect.x,2)+math.pow(self.player_rect.y-self.boss_2_level_3_rect.y,2))

    def idle(self):
        self.boss_2_idle=boss_2_idle ; self.boss_2_idle_flip=boss_2_idle_flip ; self.boss_2_idle_number=boss_2_idle_number
        global level_3_part_2,level_3_dialogue_part_7_once
        if level_3_part_2 and not level_3_dialogue_part_7_once:
            self.boss_2_level_3_y_movement[0]=8
            if self.player_rect.x<=self.boss_2_level_3_rect.x:
                SCREEN.blit(self.boss_2_idle[int(self.boss_2_idle_number[0])//2],(self.boss_2_level_3_rect.x-self.camera_x_y[0],self.boss_2_level_3_rect.y-self.camera_x_y[1]))
            if self.player_rect.x>self.boss_2_level_3_rect.x:
                SCREEN.blit(self.boss_2_idle_flip[int(self.boss_2_idle_number[0])//2],(self.boss_2_level_3_rect.x-self.camera_x_y[0],self.boss_2_level_3_rect.y-self.camera_x_y[1]))
            self.boss_2_idle_number[0]+=0.25
            if self.boss_2_idle_number[0]>6:
                self.boss_2_idle_number[0]=0

    def run(self):
        global level_3_part_2,level_3_dialogue_part_7_once
        self.boss_2_run_number=boss_2_run_number ; self.boss_2_run=boss_2_run ; self.boss_2_run_flip=boss_2_run_flip
        if level_3_part_2 and ( level_3_dialogue_part_7_once or level_3_dialogue_part_8_once) and self.player_boss_two_distance>=50 and self.boss_2_level_3_health[0]>0:
            if self.player_rect.x<=self.boss_2_level_3_rect.x:
                SCREEN.blit(self.boss_2_run[int(self.boss_2_run_number[0])//2],(self.boss_2_level_3_rect.x-self.camera_x_y[0],self.boss_2_level_3_rect.y-self.camera_x_y[1]))
                if not enemy_stage_two:
                    self.boss_2_level_3_x_movement[0]=-3
                if enemy_stage_two:
                    self.boss_2_level_3_x_movement[0]=-14
            if self.player_rect.x>self.boss_2_level_3_rect.x:
                SCREEN.blit(self.boss_2_run_flip[int(self.boss_2_run_number[0])//2],(self.boss_2_level_3_rect.x-self.camera_x_y[0],self.boss_2_level_3_rect.y-self.camera_x_y[1]))
                if not enemy_stage_two:
                    self.boss_2_level_3_x_movement[0]=3
                if enemy_stage_two:
                    self.boss_2_level_3_x_movement[0]=14
            self.boss_2_run_number[0]+=0.30
            if self.boss_2_run_number[0]>9:
                self.boss_2_run_number[0]=0

    def attack(self):
        self.boss_2_attack=boss_2_attack ; self.boss_2_attack_flip=boss_2_attack_flip ; self.boss_2_attack_number=boss_2_attack_number
        if level_3_part_2 and (level_3_dialogue_part_7_once or level_3_dialogue_part_8_once) and self.player_boss_two_distance<50 and self.boss_2_level_3_health[0]>0:
            if self.player_rect.x<=self.boss_2_level_3_rect.x:
                SCREEN.blit(self.boss_2_attack[int(self.boss_2_attack_number[0])//2],(self.boss_2_level_3_rect.x-self.camera_x_y[0],self.boss_2_level_3_rect.y-self.camera_x_y[1]))
                self.boss_2_level_3_x_movement[0]=0
            if self.player_rect.x>self.boss_2_level_3_rect.x:
                SCREEN.blit(self.boss_2_attack_flip[int(self.boss_2_attack_number[0])//2],(self.boss_2_level_3_rect.x-self.camera_x_y[0],self.boss_2_level_3_rect.y-self.camera_x_y[1]))
                self.boss_2_level_3_x_movement[0]=0
            self.boss_2_attack_number[0]+=0.40
            if self.boss_2_attack_number[0]>9:
                self.boss_2_attack_number[0]=0
                if not enemy_stage_two:
                    self.player_current_health[0]-=550   #50
                if enemy_stage_two:
                    self.player_current_health[0]-=550  #150

    def health(self):
        global attack,player_idle_right,player_idle_left,boss_one_fall_once,boss_2_fall_right,boss_2_fall_left
        self.maximum_health=1000
        self.health_bar_length=500
        self.health_bar_ratio=self.maximum_health/self.health_bar_length
        if level_3_part_2 and (level_3_dialogue_part_7_once or level_3_dialogue_part_8_once) and self.boss_2_level_3_health[0]>0:
            health_icons=pygame.draw.rect(SCREEN,(112,128,144),pygame.Rect(590,10,self.boss_2_level_3_health[0]/self.health_bar_ratio,25))
            SCREEN.blit(self.health_icon,(605,12))
            health_border=pygame.draw.rect(SCREEN,(220,220,220),pygame.Rect(590,10,self.health_bar_length,25),4) 
            if attack:
                if player_idle_right and self.player_rect.x<=self.boss_2_level_3_rect.x and self.player_boss_two_distance<75:
                    self.boss_2_level_3_health[0]-=1000 #50
                    boss_2_fall_right=True ; boss_2_fall_left=False
                if player_idle_left and self.player_rect.x>self.boss_2_level_3_rect.x and self.player_boss_two_distance<75:
                    self.boss_2_level_3_health[0]-=1000 #50
                    boss_2_fall_right=False ; boss_2_fall_left=True
                if self.boss_2_level_3_health[0]<=0 and not boss_one_fall_once:
                    boss_one_fall_once=True

    def recovery(self):
        global boss_one_fall_once,level_3_dialogue_rise_boss, level_3_dialogue_part_8_once, boss_2_fall_right,boss_2_fall_left,enemy_stage_two
        self.boss_2_recover=boss_2_recover ; self.boss_2_recover_flip=boss_2_recover_flip ; self.boss_2_recover_number=boss_2_recover_number ; self.boss_2_fall=boss_2_fall ; self.boss_2_fall_flip=boss_2_fall_flip
        self.boss_2_rise_number=boss_2_rise_number
        if boss_one_fall_once:

            if boss_2_fall_right and self.boss_2_rise_number[0]<=10:
                SCREEN.blit(self.boss_2_fall[0],(self.boss_2_level_3_rect.x-self.camera_x_y[0],self.boss_2_level_3_rect.y-self.camera_x_y[1]))
                self.boss_2_level_3_x_movement[0]=0
            if boss_2_fall_left and self.boss_2_rise_number[0]<=10:
                SCREEN.blit(self.boss_2_fall_flip[0],(self.boss_2_level_3_rect.x-self.camera_x_y[0],self.boss_2_level_3_rect.y-self.camera_x_y[1]))
                self.boss_2_level_3_x_movement[0]=0
            self.boss_2_rise_number[0]+=0.25
            if self.boss_2_rise_number[0]>10:
                if self.player_rect.x<=self.boss_2_level_3_rect.x:
                    SCREEN.blit(self.boss_2_recover[int(self.boss_2_recover_number[0]//2)],(self.boss_2_level_3_rect.x-self.camera_x_y[0],self.boss_2_level_3_rect.y-self.camera_x_y[1]))
                if self.player_rect.x>=self.boss_2_level_3_rect.x:
                    SCREEN.blit(self.boss_2_recover_flip[int(self.boss_2_recover_number[0]//2)],(self.boss_2_level_3_rect.x-self.camera_x_y[0],self.boss_2_level_3_rect.y-self.camera_x_y[1]))
                self.boss_2_recover_number[0]+=0.50
                if self.boss_2_recover_number[0]>11:
                    self.boss_2_recover_number[0]=11
                    if not level_3_dialogue_part_8_once:
                        level_3_dialogue_rise_boss=True 
                    else: 
                        level_3_dialogue_rise_boss=False
                        boss_one_fall_once=False
                        enemy_stage_two=True
                     #   boss_2_fall_right=False
                     #   boss_2_fall_left=False

    def fall(self):
        global enemy_stage_two,level_3_part_3
        self.boss_2_fall=boss_2_fall ; self.boss_2_fall_flip=boss_2_fall_flip
        if enemy_stage_two and self.boss_2_level_3_health[0]<=0 and level_3_part_2:
            if boss_2_fall_right:
                SCREEN.blit(self.boss_2_fall[0],(self.boss_2_level_3_rect.x-self.camera_x_y[0],self.boss_2_level_3_rect.y-self.camera_x_y[1]))
                self.boss_2_level_3_x_movement[0]=0
            if boss_2_fall_left:
                SCREEN.blit(self.boss_2_fall_flip[0],(self.boss_2_level_3_rect.x-self.camera_x_y[0],self.boss_2_level_3_rect.y-self.camera_x_y[1]))
                self.boss_2_level_3_x_movement[0]=0

    def reset_position(self):
        global reset_enemy_position
        self.boss_2_level_3_x=boss_2_level_3_x ; self.boss_2_level_3_y=boss_2_level_3_y
        if level_3_part_2 and reset_enemy_position:
            self.boss_2_level_3_rect.x=self.boss_2_level_3_x[0]
            self.boss_2_level_3_rect.y=self.boss_2_level_3_y[0]
            # reset_enemy_position=False

    def collision_with_object(self,level_3_tile_set_part_2):
        global level_3_part_2
        self.level_3_tile_set_part_2_rect=level_3_tile_set_part_2_rect
        if level_3_part_2:
            tiles=[]
            for tile in self.level_3_tile_set_part_2_rect:
                if self.boss_2_level_3_rect.colliderect(tile):
                    tiles.append(tile)
            return tiles

    def collision_with_object_logic(self):
        global level_3_part_2
        if level_3_part_2:
            self.boss_2_level_3_rect.x+=self.boss_2_level_3_x_movement[0]
            collision=BossTwo.collision_with_object(self,level_3_tile_set_part_2)
            for tile in collision:
                if self.boss_2_level_3_x_movement[0]>0:
                    self.boss_2_level_3_rect.right=tile.left
                if self.boss_2_level_3_x_movement[0]<0:
                    self.boss_2_level_3_rect.left=tile.right
            self.boss_2_level_3_rect.y+=self.boss_2_level_3_y_movement[0]
            collision=BossTwo.collision_with_object(self,level_3_tile_set_part_2)
            for tile in collision:
                if self.boss_2_level_3_y_movement[0]>0:
                    self.boss_2_level_3_rect.bottom=tile.top
                if self.boss_2_level_3_y_movement[0]<0:
                    self.boss_2_level_3_rect.top=tile.bottom
            return self.boss_2_level_3_rect   
            
while run:
    tile_level_1_rect=[] ; tile_level_2_rect=[] ; level_2_bg_list=[] ; level_2_dec_list=[] ; level_2_item_list=[] ; tile_level_3_rect=[]
    level_3_bg_list=[] ; level_3_hill_list=[] ; level_3_tile_set_part_2_rect=[] ; level_4_tile_set_rect=[]

    key=pygame.key.get_pressed()
    x=clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    menu=Menu(camera_x_y_bg)
    menu.home(level_3_bg_1,level_3_bg_2)
    menu.level_selection()
    
    game=Game(level_1_bg,tile_level_1,camera_x_y,tile_level_1_rect,tile_level_2,tile_level_2_rect,tile_level_3,tile_level_3_rect,level_3_tile_set_part_2,level_3_tile_set_part_2_rect,level_4_tile_set,level_4_tile_set_rect)
    game.level_one(tile_level_1_ground,tile_level_1_dirt)
    game.level_two()
    game.level_three()
    game.level_four()
    
    player=Player(player_x_movement,player_y_movement,player_rect,player_current_health)
    player.movement(player_idle,player_idle_flip,player_run,player_run_flip,player_jump,player_jump_flip)
    player.attack(player_attack_type_1,player_attack_type_1_flip,player_attack_type_2,player_attack_type_2_flip,
              player_attack_type_3,player_attack_type_3_flip,player_attack_type_4,player_attack_type_4_flip,attack_jump,attack_jump_flip)
    player.reset_position()
    player.collision_with_object(tile_level_1_rect,tile_level_2_rect,tile_level_3_rect,level_3_tile_set_part_2_rect,level_4_tile_set_rect)
    player.collision_with_object_logic(tile_level_1_rect,tile_level_2_rect,tile_level_3_rect,level_3_tile_set_part_2_rect,level_4_tile_set_rect)
    
    enemy_one=EnemyOne(enemy_list_level_1,npc_walk_length,npc_direction_choice,enemy_1_distance_list,enemy_1_health_list,enemy_1_level_3_rect,enemy_list_level_3)
    enemy_one.move(enemy_1_level_1_rect,enemy_level_1_rect,enemy_1_level_1_rect_idle,enemy_1_x_movement,enemy_1_y_movement,enemy_1_level_2_rect)
    enemy_one.player_interaction()
    enemy_one.attack()
    enemy_one.player_hit()
    enemy_one.fall()
    enemy_one.reset_position()
    enemy_one.collision_with_object(tile_level_1,tile_level_2,tile_level_3_rect)
    enemy_one.collision_with_object_logic(tile_level_1,tile_level_2,tile_level_3_rect)
    
    enemy_two=EnemyTwo(enemy_two_level_1_rect,enemy_two_x_movement,enemy_two_y_movement,enemy_two_rect_list,enemy_two_distance_list,enemy_two_health,enemy_two_level_4_rect_1)
    enemy_two.movement()
    enemy_two.attack()
    enemy_two.player_hit()
    enemy_two.fall()
    enemy_two.reset_position()
    enemy_two.collision_with_object(tile_level_1)
    enemy_two.collision_with_object_logic(tile_level_1)

    allyone=AllyOne(ally_1_x_movement,ally_1_y_movement,ally_1_level_3_part_1_idle_rect,ally_1_level_3_part_1_run_rect,ally_1_rect_list,ally_1_level_3_part_2_idle_rect,ally_1_level_3_part_2_run_rect)
    allyone.idle()
    allyone.run()
    allyone.reset_position()
    allyone.player_interaction()
    allyone.collision_with_object(tile_level_3,level_3_tile_set_part_2)
    allyone.collision_with_object_logic(tile_level_3,level_3_tile_set_part_2)
    
    main_boss=MainBoss(main_boss_rect_level_1,main_boss_x_movement,main_boss_y_movement)
    main_boss.movement()
    main_boss.reset_position()
    main_boss.collision_with_object(tile_level_1)
    main_boss.collision_with_object_logic(tile_level_1)
    
    general_boss=GeneralBoss()
    general_boss.idle()
                        
    boss_one=BossOne(boss_1_rect,boss_1_level_2_part_2_x,boss_1_level_2_part_2_y,boss_1_x_movement,boss_1_y_movement,boss_1_health)
    boss_one.idle()
    boss_one.move()
    boss_one.attack()
    boss_one.health()
    boss_one.fall()
    boss_one.reset_position()
    boss_one.collision_with_object(tile_level_2)
    boss_one.collision_with_object_logic(tile_level_2)

    boss_two=BossTwo(boss_2_level_3_x,boss_2_level_3_y,boss_2_level_3_x_movement,boss_2_level_3_y_movement,boss_2_level_3_rect,boss_2_level_3_health)
    boss_two.idle()
    boss_two.run()
    boss_two.attack()
    boss_two.health()
    boss_two.recovery()
    boss_two.fall()
    boss_two.reset_position()
    boss_two.collision_with_object(level_3_tile_set_part_2)
    boss_two.collision_with_object_logic()
    
    game.level_one_dialogue()
    game.level_two_dialogue()
    game.level_three_dialogue()
    game.level_one_win()
    
    player.defeat()

    pygame.display.update()