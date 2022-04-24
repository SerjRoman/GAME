import pygame
import os
from graphic_elements import Graphic_elements
from sounds import Sounds
from random import randint, choice
from Hero import Main_Hero
from Menu import Menu
from Addition_Module import*
from Text import Font

pygame.init()
pygame.font.init()
#Записываем размеры нашего экрана
# SCREEN_W = pygame.display.Info().current_w
# SCREEN_H = pygame.display.Info().current_h
SCREEN_W = 1280
SCREEN_H = 720
# КООРДИНАТЫ ЦЕНТРАЛЬНОЙ КЛЕТКИ
CENTER_CELL_COR = [SCREEN_W//19*8,SCREEN_H//2]
#Константа громкости звука
SOUNDS_VOLUME = 1
#Размер клеточки в мини-карте
W_CELL_MINI_MAP = SCREEN_W//6.9//30
H_CELL_MINI_MAP = SCREEN_W//6.9//30
# Координаты для старта отрисовки клеток в мини-карте
X_FRAME_MM, Y_FRAME_MM = (SCREEN_W - SCREEN_W//19*2.9//1) + SCREEN_W//200,  SCREEN_W//19 + SCREEN_W//220 
# список клеток для мини-карты
list_cells_MM = list()
#Список из звуков подбора ресурсов
recourse_sounds = [Sounds('sounds/res1.wav',SOUNDS_VOLUME),Sounds('sounds/res2.wav',SOUNDS_VOLUME),Sounds('sounds/res3.wav',SOUNDS_VOLUME)]
################################################################################################################################################################
#Словарь отвечает за кол-во ресурсов у игрока
resources_dict = {
    'food':1,
    'iron':1,
    'wood':1,
    'gold':1,
    'crystal':1,
    'stone':1,
}


################################################################################################################################################################
#Размер карты первого уровня
LENGTH_MAP_LVL1 = 30
#Список из клеток первого уровня
list_cells_lvl1 = [list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'), 
                   list('000000000000000000000000000000')]
################################################################################################################################################################
#Список-матрица объектов(персонаж, здания, ресурсы)           
mat_objetcs_lvl1 =[ list('000000000000000000000000000100'),
                    list('00pPg000000000000P000000000100'),
                    list('0000giscw000000000000000000100'),
                    list('000000000000000000000000000100'),
                    list('00Ff0000000000000T00000t000100'),
                    list('00ff00000000000000000000000100'),
                    list('00000Hh00000000000000000000100'),
                    list('00000hh00000000000000000000100'),
                    list('00000000Dd00000000000000000100'),
                    list('00000000dd00000000000000000100'),
                    list('000000000000Nn0000000000000100'),
                    list('000000000000nn0000000000000100'),
                    list('000000000000000Rr0000000000100'),
                    list('000000000000000rr0000000000100'),
                    list('0000000000000000000Xx000000100'),
                    list('0000000000000000000xx000000100'),
                    list('000000000000000000000000000100'),
                    list('000000000000000000000000000100'),
                    list('000000000000000000000000000100'),
                    list('000000000000000000000000000100'),
                    list('000000000000000000000000000100'),
                    list('000000000000000000000000000100'),
                    list('000000000000000000000000000100'),
                    list('000000000000000000000000000100'),
                    list('000000000000000000000000000100'),
                    list('000000000000000000000000000100'),
                    list('000000000000000000000000000100'),
                    list('000000000000000000000000000100'),
                    list('000000000000000000000000000100'), 
                    list('000000000000000000000000000100')]


################################################################################################################################################################

#Список, в которм будут храниться объекты клеток
list_objects_cells_lvl1 = []


################################################################################################################################################################


button_play = Menu(SCREEN_W//15, SCREEN_H//10, SCREEN_W//8, SCREEN_H//9,path='images/menu/play_b.png',image_button_b='images/menu/play_b.png',image_button_y='images/menu/play_y.png',x_divider=15,y_divider=10)
button_help = Menu(SCREEN_W//15, SCREEN_H//3.5, SCREEN_W//8, SCREEN_H//9, 'images/menu/help_b.png',image_button_b='images/menu/help_b.png',image_button_y='images/menu/help_y.png',x_divider=15,y_divider=3.5)
button_set = Menu(SCREEN_W//15, SCREEN_H//2.1, SCREEN_W//8, SCREEN_H//9, 'images/menu/settings_b.png',image_button_b='images/menu/settings_b.png',image_button_y='images/menu/settings_y.png',x_divider=15,y_divider=2.1)
button_exit = Menu(SCREEN_W//15, SCREEN_H//1.5, SCREEN_W//8, SCREEN_H//9, 'images/menu/exit_b.png',image_button_b='images/menu/exit_b.png',image_button_y='images/menu/exit_y.png',x_divider=15,y_divider=1.5)
list_buttons = [button_play,button_help,button_set,button_exit]                   

list_cards_pl = [['бард',1,2],['бард',5,0],['подрывник',3,5],['арбалетчик',4,3],['гигант',2,3],['ями',4,1]]
list_card_pl_reserv = [['бард',1,2],['клаус',5,0],['подрывник',3,5],['арбалетчик',4,3],['гигант',2,3],['ями',4,1]]
list_cards_menu_hero = list()
def create_icon_card():
    
    x = SCREEN_W//2.133
    y = SCREEN_H//44
    width = SCREEN_W//1.8666 - x
    for i in range(6):#
        path = 'images/cards/'+list_cards_pl[i][0]+'.png'
        card = Graphic_elements(x=x,y=y,width=width,height=SCREEN_H//7.5,path=path,name=list_cards_pl[i][0],start_x=x,start_y=y)
        if not card in list_cards_menu_hero:
            list_cards_menu_hero.append(card)
        x+= SCREEN_W//11
    y = SCREEN_H//5.333
    x = SCREEN_W//2.133
    for i in range(len(list_card_pl_reserv)):
        path = 'images/cards/'+list_card_pl_reserv[i][0]+'.png'
        card = Graphic_elements(x=x,y=y,width=width,height=SCREEN_H//7.5,path=path,name=list_cards_pl[i][0],start_x=x,start_y=y)
        if not card in list_cards_menu_hero:
            list_cards_menu_hero.append(card)
        x+= SCREEN_W//11


    


################################################################################################################################################################
#Основная фунуция
def run_game():
    #Создаем окно, с параметром БЕЗ РАМКИ
    win = pygame.display.set_mode((SCREEN_W, SCREEN_H), )#,#pygame.FULLSCREEN
    desc = Graphic_elements(SCREEN_W//2-SCREEN_W//4,SCREEN_H//2-SCREEN_H//4,SCREEN_W//2,SCREEN_H//2,path=None)
    #Создаем книгу
    book = Graphic_elements(0, 0, SCREEN_W, SCREEN_H, 'images/book.png')
    #кнопки меню
    key_is_pressed = False
    count_move = 0
    #Направление движения игрока
    where_move = None
    #Звук отткрытия книги
    sound_book = Sounds('sounds/book_opened.wav', 1)
    menu_hero = Graphic_elements(0,0,SCREEN_W,SCREEN_H,'images/hero_menu.bmp')

    #Создаем объект персонажа первого уровня
    player_lvl1 = Main_Hero(
                            x=0,y=0,
                            height=SCREEN_W//19,width=SCREEN_W//19,
                            path='images/player/player_front.png',
                            SCREEN_W=SCREEN_W,SCREEN_H=SCREEN_H,
                            where_move=where_move,count_move=count_move,
                            win=win)
    #Объекты картинок ресурсов
    gold = Graphic_elements(0, 0, SCREEN_W//19, SCREEN_W//19, 'images/resources/gold.png')
    iron = Graphic_elements(0, 0, SCREEN_W//19, SCREEN_W//19, 'images/resources/iron.png')
    crystal = Graphic_elements(0, 0, SCREEN_W//19, SCREEN_W//19*1.5, 'images/resources/gems.png')
    wood = Graphic_elements(0, 0, SCREEN_W//19, SCREEN_W//19, 'images/resources/wood.png')
    stone = Graphic_elements(0, 0, SCREEN_W//19, SCREEN_W//19, 'images/resources/stone.png')
    apple = Graphic_elements(SCREEN_W - SCREEN_W//19*2.9//1, SCREEN_W//19*6.7, SCREEN_W//30, SCREEN_W//30, 'images/resources/apple.png')
    iron_bullion = Graphic_elements(SCREEN_W - SCREEN_W//19*2.9//1, SCREEN_W//19*7.5, SCREEN_W//30, SCREEN_W//30, 'images/resources/iron_bullion.png')
    wood2 = Graphic_elements(SCREEN_W - SCREEN_W//19*2.9//1, SCREEN_W//19*8.3, SCREEN_W//30, SCREEN_W//30, 'images/resources/wood.png')
    gold_bullion = Graphic_elements(SCREEN_W - SCREEN_W//19*1.4//1, SCREEN_W//19*6.7, SCREEN_W//30, SCREEN_W//30, 'images/resources/gold_bullion.png')
    crystal_purified = Graphic_elements(SCREEN_W - SCREEN_W//19*1.4//1, SCREEN_W//19*7.5, SCREEN_W//30, SCREEN_W//30, 'images/resources/cristal.png')
    stone_purified = Graphic_elements(SCREEN_W - SCREEN_W//19*1.4//1, SCREEN_W//19*8.3, SCREEN_W//30, SCREEN_W//30, 'images/resources/stone2.png')
    tree_full = Graphic_elements(0, 0, SCREEN_W//19, SCREEN_W//19*1.5, 'images/resources/tree_full.png')
    tree = Graphic_elements(0, 0, SCREEN_W//19, SCREEN_W//19*1.5, 'images/resources/tree.png')
    time = pygame.time.Clock()
    button_end_move = Graphic_elements(SCREEN_W-SCREEN_W//7.6, SCREEN_H-SCREEN_H//11, SCREEN_W//9,SCREEN_H//20 , 'images/game_interface/end_moves.png')
    #Картинка зеленого флага
    flag_green = Graphic_elements(0, 0, SCREEN_W//19, SCREEN_W//19, 'images/flags/flag_g.png')
    #Картинки зданий
    gemsmine = Graphic_elements(0,0,int(SCREEN_W//9.5),int(SCREEN_W//9.5),'images/buildings/gemsmine.png')
    farm = Graphic_elements(0,0,int(SCREEN_W//9.5),int(SCREEN_W//9.5),'images/buildings/farm.png')
    goldmine = Graphic_elements(0,0,int(SCREEN_W//9.5),int(SCREEN_W//9.5),'images/buildings/goldmine.png')
    ironmine = Graphic_elements(0,0,int(SCREEN_W//9.5),int(SCREEN_W//9.5),'images/buildings/ironmine.png')
    sawmill = Graphic_elements(0,0,int(SCREEN_W//9.5),int(SCREEN_W//9.5),'images/buildings/sawmill.png')
    stonebreaker = Graphic_elements(0,0,int(SCREEN_W//9.5),int(SCREEN_W//9.5),'images/buildings/stinebreaker.png')
    #Текст количества ходов
    text_step_count = Font('images/Font/pixel_font.ttf',SCREEN_W//65,'white','Осталось ходов: '+str(player_lvl1.count_step),SCREEN_W-SCREEN_W//6.8,SCREEN_H-SCREEN_H//7.5)
    #Картинки иконок ресурсов
    amount_food = Font('images/Font/pixel_font.ttf',SCREEN_W//43,'white','0',SCREEN_W - SCREEN_W//19*2.2//1,SCREEN_W//19*6.9)
    amount_iron = Font('images/Font/pixel_font.ttf',SCREEN_W//43,'white','0',SCREEN_W - SCREEN_W//19*2.2//1,SCREEN_W//19*7.7)
    amount_wood = Font('images/Font/pixel_font.ttf',SCREEN_W//43,'white','0',SCREEN_W - SCREEN_W//19*2.2//1,SCREEN_W//19*8.4)
    amount_gold = Font('images/Font/pixel_font.ttf',SCREEN_W//43,'white','0',SCREEN_W - SCREEN_W//29, SCREEN_W//19*6.9)
    amount_crystal=Font('images/Font/pixel_font.ttf',SCREEN_W//43,'white','0',SCREEN_W - SCREEN_W//29, SCREEN_W//19*7.7)
    amount_stone = Font('images/Font/pixel_font.ttf',SCREEN_W//43,'white','0',SCREEN_W - SCREEN_W//29, SCREEN_W//19*8.4)
    fog_war = Graphic_elements(None,None,SCREEN_W//19, SCREEN_W//19,'images/fog_war.bmp')
    # картинки для интерфейса в игре
    interface_bg  = Graphic_elements(SCREEN_W-SCREEN_W//19*3,0,SCREEN_W//19*3,SCREEN_H,'images/game_interface/sheet.png')
    button_to_hero = Graphic_elements( SCREEN_W - SCREEN_W//19*2.9//1 +SCREEN_W//13.5,SCREEN_W//19*4.7,SCREEN_W//15,SCREEN_W//30,'images/game_interface/to_hero.png')
    button_to_castle = Graphic_elements( SCREEN_W - SCREEN_W//19*2.9//1 +SCREEN_W//13.5,SCREEN_W//19*4.7 + SCREEN_W//30,SCREEN_W//15,SCREEN_W//30,'images/game_interface/to_castle.png')
    frame = Graphic_elements(SCREEN_W - SCREEN_W//19*2.9//1,  SCREEN_W//19*4.7, SCREEN_W//15, SCREEN_W//15, 'images/game_interface/ramka.png')
    frame_mini_map = Graphic_elements(SCREEN_W - SCREEN_W//19*2.9//1,  SCREEN_W//19 , SCREEN_W//6.7, SCREEN_W//6.7, 'images/game_interface/ramka.png')
    elliot_img = Graphic_elements(SCREEN_W - SCREEN_W//19*2.9//1 + SCREEN_W//350,  SCREEN_W//19*4.74, SCREEN_W//16, SCREEN_W//16, 'images/game_interface/elliot_img.png')
    player_info = Font('images/Font/pixel_font.ttf',SCREEN_W//65,'white','Эллиот, ур 1',SCREEN_W-SCREEN_W//19*3 + SCREEN_W//350,SCREEN_W//19*4.7 + SCREEN_W//15)
    list_interface_button = [button_to_hero,button_to_castle,button_end_move]
    list_paths_pressed = [['images/game_interface/to_hero.png','images/game_interface/to_hero_w.png'],['images/game_interface/to_castle.png','images/game_interface/to_castle_w.png',],['images/game_interface/end_moves.png','images/game_interface/end_moves_w.png',]]
    list_cor_portals = [ [[1,3],[1,17]] ]
    portal = Graphic_elements(0, 0, SCREEN_W//19, SCREEN_W//19, 'images/portal.png')
    #Картинки клеточек для мини карты
    green = Graphic_elements(0,0,W_CELL_MINI_MAP,H_CELL_MINI_MAP,'images/green.png')
    black = Graphic_elements(0,0,W_CELL_MINI_MAP,H_CELL_MINI_MAP,'images/black.png')
    yellow = Graphic_elements(0,0,W_CELL_MINI_MAP,H_CELL_MINI_MAP,'images/yellow.png')
    white = Graphic_elements(0,0,W_CELL_MINI_MAP,H_CELL_MINI_MAP,'images/white.png')
    green_dark = Graphic_elements(0,0,W_CELL_MINI_MAP,H_CELL_MINI_MAP,'images/green_dark.png')
    button_menu_hero_back = Graphic_elements(0,SCREEN_H-SCREEN_W//19,SCREEN_W//19*2,SCREEN_W//19,'images/menu_hero_back_y.png')
    # координаты игрока
    list_cor_player_xy = [0,0]
    # for i in range(2):
    #     list_portal.append()

    create_icon_card()

    draw_cells = False
    #Переменная, отвечающяя за сцену
    scene = 'menu'
    #Создаем карту 1-го уровня
    create_map(list_cells_lvl1, list_objects_cells_lvl1,SCREEN_W,SCREEN_H)
    buttonIsPressed = False
    #Переменная игры
    game = True
    card_pressed = None
    index_card = None
    desc_count = 0
    #Игровой цикл
    while game:
        
        # print(player_lvl1.X)
        #Цикл проверки событий
        for event in pygame.event.get():
            #Услове выхода из игры
            mouse_cor = pygame.mouse.get_pos() 
            if event.type == pygame.QUIT:
                game = False
            if scene == 'menu_hero':

                menu_hero.show_image(win)
                button_menu_hero_back.show_image(win)
                #Условия кнопки назад
                if check_mouse_cor(button_menu_hero_back,mouse_cor):
                    button_menu_hero_back.path = 'images/menu_hero_back_b.png'
                    button_menu_hero_back.image_load()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        scene = 'lvl1'
                else:
                    button_menu_hero_back.path = 'images/menu_hero_back_y.png'
                    button_menu_hero_back.image_load()

                
                for obj in list_cards_menu_hero:
                    obj.show_image(win)
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if check_mouse_cor(obj,mouse_cor=mouse_cor):
                            card_pressed = obj 

                    if event.type == pygame.MOUSEMOTION:
                        pos  = pygame.mouse.get_pos()
                        if card_pressed != None:
                            card_pressed.X = pos[0] - card_pressed.WIDTH//2
                            card_pressed.Y = pos[1] - card_pressed.HEIGHT//2
                            index_card = list_cards_menu_hero.index(card_pressed)

                    if event.type == pygame.MOUSEBUTTONUP:
                        if card_pressed != None:
                            for sprite in list_cards_menu_hero:
                                if check_mouse_cor(sprite,mouse_cor=mouse_cor) and index_card != list_cards_menu_hero.index(sprite):

                                    sprite.X = card_pressed.start_x
                                    sprite.Y = card_pressed.start_y
                                    card_pressed.X = sprite.start_x
                                    card_pressed.Y = sprite.start_y
                                    sprite.start_x = sprite.X
                                    sprite.start_y = sprite.Y
                                    card_pressed.start_x = card_pressed.X
                                    card_pressed.start_y = card_pressed.Y
                                    break
                                else:
                                    card_pressed.X = card_pressed.start_x
                                    card_pressed.Y = card_pressed.start_y
                            card_pressed = None

                for obj in list_cards_menu_hero:
                    if check_mouse_cor(obj,mouse_cor) and card_pressed == None:

                        desc.path = 'images/cards/desc/desc_'+obj.NAME+'.png'
                        desc.image_load()
                        desc.show_image(win)
                        break
                    else:
                        desc.path = None
                        
                


            if scene == 'menu':
                book.show_image(win)
                #Изменяем размер кнопки при наводке
                for button in list_buttons:
                    button.resize_button_menu(mouse_cor=mouse_cor,SCREEN_W=SCREEN_W,SCREEN_H=SCREEN_H)
                    button.show_image(win)
                # Реакция на нажатие кнопок
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if check_mouse_cor(button_play,mouse_cor):
                        sound_book.play_sound()
                        scene = 'lvl1'
                    elif check_mouse_cor(button_exit,mouse_cor):
                        sound_book.play_sound()
                        game = False
                            #Отрисовуем книгу
                
                #Отрисовуем кнопки
                
                
            if scene == 'lvl1':
                
                #Если нажата левая кнопка мыши
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    #Если заканчиваем ход
                    if check_mouse_cor(button_end_move,mouse_cor):
                        #Обновляем количество ходов игрока
                        player_lvl1.count_step = 20
                        player_lvl1.where_move = None
                        #Начисляем русурсы за захваченые здания
                        resourse_accural(player_lvl1.list_capture_buildings_symbol, resources_dict)
                    #Когда нажали на кнопку "К ГЕРОЮ" 
                    if check_mouse_cor(button_to_hero,mouse_cor):
                        #Перемещаемся к герою 
                        move_to_hero(CENTER_CELL_COR,list_cor_player_xy,list_objects_cells_lvl1,SCREEN_W,SCREEN_H)
                    if check_mouse_cor(frame,mouse_cor):
                        scene = 'menu_hero'
                       



                        
                    buttonIsPressed = True
                #Кнопка мыши отпущена
                if event.type == pygame.MOUSEBUTTONUP:
                    buttonIsPressed = False
                #Если двигаем мышью и кнопка мыши зажата
                if event.type == pygame.MOUSEMOTION and buttonIsPressed:
                    #Вызываем функцию перемещения карты
                    move_map(event, list_objects_cells_lvl1,SCREEN_W=SCREEN_W,SCREEN_H=SCREEN_H)

                if event.type == pygame.MOUSEMOTION:
                    if scene == 'lvl1':
                        i=0
                        for b in list_interface_button:
                            if check_mouse_cor(b,mouse_cor):
                                b.path = list_paths_pressed[i][1]
                                b.image_load()
                            else:
                                b.path = list_paths_pressed[i][0]
                                b.image_load()
                            

                            i+=1

                                




                
               
        if scene == 'lvl1':
            amount_crystal.font_content = str(resources_dict['crystal'])
            amount_food.font_content = str(resources_dict['food'])
            amount_iron.font_content = str(resources_dict['iron'])
            amount_gold.font_content = str(resources_dict['gold'])
            amount_wood.font_content = str(resources_dict['wood'])
            amount_stone.font_content = str(resources_dict['stone'])
            win.fill('black')
            # Отрисовуем клетки
            list_xy = [0,0]
            for cell in list_objects_cells_lvl1:
                
                for cor in player_lvl1.list_studied_map:
                    if list_xy == cor:
                        draw_cells=True
                        break
                    else: 
                        draw_cells = False
                list_xy[0]+= 1
                if list_xy[0] == LENGTH_MAP_LVL1:
                    list_xy[0] = 0
                    list_xy[1] += 1
                if draw_cells:
                    cell.show_image(win)
            
            #Индекс строки, где находиться объект
            player_lvl1.blind_move(index=2)
            list_cells_MM = []
            matrix_image(
                        win, player_lvl1, gold, iron, crystal, wood, stone, tree_full, tree,
                        mat_objetcs_lvl1,list_objects_cells_lvl1,SCREEN_W,SCREEN_H,
                        player_lvl1.count_move,player_lvl1.changed_x,player_lvl1.changed_y,
                        ironmine, goldmine, farm, gemsmine,sawmill, stonebreaker,flag_green,
                        list_studied_map=player_lvl1.list_studied_map,portal = portal,
                        fog_war=fog_war,list_cor_player_xy=list_cor_player_xy,W_CELL_MINI_MAP=W_CELL_MINI_MAP,
                        H_CELL_MINI_MAP=H_CELL_MINI_MAP,X_FRAME_MM=X_FRAME_MM,
                        Y_FRAME_MM=Y_FRAME_MM, list_cells_MM = list_cells_MM, list_cor_portals = list_cor_portals,
                        LENGTH_MAP = LENGTH_MAP_LVL1)
            
            # matrix_image_blind(list_objects_cells_lvl1,mat_objetcs_lvl1,player_lvl1,list_objects_cells_lvl1,player_lvl1.changed_x,player_lvl1.changed_y,win)
            #Отрисовуем полоску справа
            # pygame.draw.rect(win, (255,223,196), (SCREEN_W-SCREEN_W//19*3,0,SCREEN_W//19*3,SCREEN_H))
            interface_bg.show_image(win)
            frame.show_image(win)
            button_to_hero.show_image(win)
            button_to_castle.show_image(win)
            frame_mini_map.show_image(win)
            elliot_img.show_image(win)
            player_info.show_text(win)
            # отрисовуем клетки на мини-карте
            for cor in list_cells_MM:
                if cor[2] == 'green':
                    green.X = cor[0]
                    green.Y = cor[1]
                    green.show_image(win)
                elif cor[2] == 'black':
                    black.X = cor[0]
                    black.Y = cor[1]
                    black.show_image(win)
                elif cor[2] == 'yellow':
                    yellow.X = cor[0]
                    yellow.Y = cor[1]
                    yellow.show_image(win)
                elif cor[2] == 'white':
                    white.X = cor[0]
                    white.Y = cor[1]
                    white.show_image(win)
                elif cor[2] == 'green_dark':
                    green_dark.X = cor[0]
                    green_dark.Y = cor[1]
                    green_dark.show_image(win)
                
            #Отображаем кол-во ресурсов на экране
            if resources_dict['food'] != 0:
                apple.show_image(win)
                amount_food.show_text(win)
            if resources_dict['iron'] != 0:
                iron_bullion.show_image(win)
                amount_iron.show_text(win)
            if resources_dict['gold'] != 0:
                gold_bullion.show_image(win)
                amount_gold.show_text(win)
            if resources_dict['crystal'] != 0:
                crystal_purified.show_image(win)
                amount_crystal.show_text(win)
            if resources_dict['stone'] != 0:
                stone_purified.show_image(win)
                amount_stone.show_text(win)
            if resources_dict['wood'] != 0:
                wood2.show_image(win)
                amount_wood.show_text(win)
            text_step_count.show_text(win)
            button_end_move.show_image(win)
            text_step_count.font_content = 'Осталось ходов: '+str(player_lvl1.count_step)
            player_lvl1.move_sprite(mat_objetcs_lvl1, LENGTH_MAP_LVL1,resources_dict,recourse_sounds,list_cor_portals=list_cor_portals,
            move_to_hero = move_to_hero,CENTER_CELL_COR = CENTER_CELL_COR,list_cor_player_xy = list_cor_player_xy,
            list_objects_cells_lvl1=list_objects_cells_lvl1,SCREEN_W = SCREEN_W,SCREEN_H = SCREEN_H)
            # if player_lvl1.count_move == 10:
            #     move_to_hero(CENTER_CELL_COR, list_cor_player_xy, list_objects_cells_lvl1, SCREEN_W, SCREEN_H)
        
           

        
        time.tick(144)
        #Обновляем экран
        pygame.display.flip()


       


run_game()
