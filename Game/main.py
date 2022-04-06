import pygame
import os
from graphic_elements import Graphic_elements
from sounds import Sounds
from random import randint, choice
from Hero import Main_Hero
from Menu import Menu
from Addition_Module import check_mouse_cor,move_map,matrix_image,create_map
from Text import Font

pygame.init()
pygame.font.init()
#Записываем размеры нашего экрана
# SCREEN_W = pygame.display.Info().current_w
# SCREEN_H = pygame.display.Info().current_h
SCREEN_W = 1500
SCREEN_H = 800
#Константа громкости звука
SOUNDS_VOLUME = 1
#Список из звуков подбора ресурсов
recourse_sounds = [Sounds('sounds/res1.wav',SOUNDS_VOLUME),Sounds('sounds/res2.wav',SOUNDS_VOLUME),Sounds('sounds/res3.wav',SOUNDS_VOLUME)]
################################################################################################################################################################
#Словарь отвечает за кол-во ресурсов у игрока
resources_dict = {
    'food':0,
    'iron':0,
    'wood':0,
    'gold':0,
    'crystal':0,
    'stone':0,
}


################################################################################################################################################################
#Размер карты первого уровня
LENGTH_MAP_LVL1 = 30
#Список из клеток первого уровня
list_cells_lvl1 = ['000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000',
                   '000000000000000000000000000000', 
                   '000000000000000000000000000000']
################################################################################################################################################################
#Список-матрица объектов(персонаж, здания, ресурсы)           
mat_objetcs_lvl1 =[ list('000000000000000000000000000000'),
                    list('00p0g0000000000000000000000000'),
                    list('0000giscw000000000000000000000'),
                    list('000000000000000000000000000000'),
                    list('00000000000000000T00000t000000'),
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

#Список, в которм будут храниться объекты клеток
list_objects_cells_lvl1 = []


################################################################################################################################################################


button_play = Menu(SCREEN_W//15, SCREEN_H//10, SCREEN_W//8, SCREEN_H//9,path='images/menu/play_b.png',image_button_b='images/menu/play_b.png',image_button_y='images/menu/play_y.png',x_divider=15,y_divider=10)
button_help = Menu(SCREEN_W//15, SCREEN_H//3.5, SCREEN_W//8, SCREEN_H//9, 'images/menu/help_b.png',image_button_b='images/menu/help_b.png',image_button_y='images/menu/help_y.png',x_divider=15,y_divider=3.5)
button_set = Menu(SCREEN_W//15, SCREEN_H//2.1, SCREEN_W//8, SCREEN_H//9, 'images/menu/settings_b.png',image_button_b='images/menu/settings_b.png',image_button_y='images/menu/settings_y.png',x_divider=15,y_divider=2.1)
button_exit = Menu(SCREEN_W//15, SCREEN_H//1.5, SCREEN_W//8, SCREEN_H//9, 'images/menu/exit_b.png',image_button_b='images/menu/exit_b.png',image_button_y='images/menu/exit_y.png',x_divider=15,y_divider=1.5)
list_buttons = [button_play,button_help,button_set,button_exit]                   



################################################################################################################################################################
#Основная фунуция
def run_game():
    #Создаем окно, с параметром БЕЗ РАМКИ
    win = pygame.display.set_mode((SCREEN_W, SCREEN_H) )#pygame.FULLSCREEN
    #Создаем книгу
    book = Graphic_elements(0, 0, SCREEN_W, SCREEN_H, 'images/book.png')
    #кнопки меню
    key_is_pressed = False
    count_move = 0
    where_move = None
    sound_book = Sounds('sounds/book_opened.wav', 1)
    #Создаем объект персонажа первого уровня
    player_lvl1 = Main_Hero(
                            x=0,y=0,
                            height=SCREEN_W//19,width=SCREEN_W//19,
                            path='images/player/player_front.png',
                            SCREEN_W=SCREEN_W,SCREEN_H=SCREEN_H,
                            where_move=where_move,count_move=count_move
                            );
    #Объекты картинок ресурсов
    gold = Graphic_elements(0, 0, SCREEN_W//19, SCREEN_W//19, 'images/resources/gold.png')
    iron = Graphic_elements(0, 0, SCREEN_W//19, SCREEN_W//19, 'images/resources/iron.png')
    crystal = Graphic_elements(0, 0, SCREEN_W//19, SCREEN_W//19, 'images/resources/gems.png')
    wood = Graphic_elements(0, 0, SCREEN_W//19, SCREEN_W//19, 'images/resources/wood.png')
    stone = Graphic_elements(0, 0, SCREEN_W//19, SCREEN_W//19, 'images/resources/stone.png')
    tree_full = Graphic_elements(0, 0, SCREEN_W//19, SCREEN_W//19*1.5, 'images/resources/tree_full.png')
    tree = Graphic_elements(0, 0, SCREEN_W//19, SCREEN_W//19*1.5, 'images/resources/tree.png')
    time = pygame.time.Clock()
    button_end_move = Graphic_elements(SCREEN_W-SCREEN_W//8, SCREEN_H-SCREEN_H//11, SCREEN_W//9,SCREEN_H//45 , 'images/game_interface/end_moves.png')

    text_step_count = Font('images/Font/pixel_font.ttf',SCREEN_W//75,'black','Осталось ходов: '+str(player_lvl1.count_step),SCREEN_W-SCREEN_W//8,SCREEN_H-SCREEN_H//7.5)
    #Переменная, отвечающяя за сцену
    scene = 'menu'
    #Создаем карту 1-го уровня
    create_map(list_cells_lvl1, list_objects_cells_lvl1,SCREEN_W,SCREEN_H)
    buttonIsPressed = False
    #Переменная игры
    game = True
    
    
    #Игровой цикл
    while game:
        # print(player_lvl1.X)
        #Цикл проверки событий
        for event in pygame.event.get():
            #Услове выхода из игры
            mouse_cor = pygame.mouse.get_pos() 
            if event.type == pygame.QUIT:
                game = False
 
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
                    #Левая кнопка мыши зажата
                    if check_mouse_cor(button_end_move,mouse_cor):
                        player_lvl1.count_step = 20
                        player_lvl1.where_move = None
                    buttonIsPressed = True
                #Кнопка мыши отпущена
                if event.type == pygame.MOUSEBUTTONUP:
                    buttonIsPressed = False
                #Если двигаем мышью и кнопка мыши зажата
                if event.type == pygame.MOUSEMOTION and buttonIsPressed:
                    #Вызываем функцию перемещения карты
                    move_map(event, list_objects_cells_lvl1,SCREEN_W=SCREEN_W,SCREEN_H=SCREEN_H)


                
               
        if scene == 'lvl1':
            player_lvl1.move_sprite(mat_objetcs_lvl1, LENGTH_MAP_LVL1,resources_dict,recourse_sounds)
            win.fill('red')
            # Отрисовуем клетки
            for cell in list_objects_cells_lvl1:
                cell.show_image(win)
            #Индекс строки, где находиться объект
            matrix_image(
                        win, player_lvl1, gold, iron, crystal, wood, stone, tree_full, tree,
                        mat_objetcs_lvl1,list_objects_cells_lvl1,SCREEN_W,SCREEN_H,
                        player_lvl1.count_move,player_lvl1.changed_x,player_lvl1.changed_y
                        )
            text_step_count.show_text(win)
            button_end_move.show_image(win)
            text_step_count.font_content = 'Осталось ходов: '+str(player_lvl1.count_step)
        time.tick(30)
        #Обновляем экран
        pygame.display.flip()


       


run_game()
