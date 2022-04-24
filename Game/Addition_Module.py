from tkinter import X
from webbrowser import Grail

import pygame
from graphic_elements import Graphic_elements
from random import randint



def check_mouse_cor(sprite,mouse_cor):
    if mouse_cor[0] > sprite.X and mouse_cor[0] < sprite.X + sprite.WIDTH and mouse_cor[1] > sprite.Y and mouse_cor[1] < sprite.Y + sprite.HEIGHT:
        return True


        
def move_map(event, list_map,SCREEN_W,SCREEN_H):
    #Изменяем координаты каждой клетки
    for cell in list_map:
        cell.X += event.rel[0]
        cell.Y += event.rel[1]
    #Если игровое поле ушло вправо от границы экрана
    if list_map[0].X > 0:
        change_x = list_map[0].X * -1
        #Возвращаем его к правой стороне экрана
        for cell in list_map:
            cell.X += change_x
    #Если игровое поле ушло влево от границы экрана
    elif  list_map[-1].X + list_map[-1].WIDTH   < SCREEN_W: 
        change_x = SCREEN_W - (list_map[-1].X + list_map[-1].WIDTH)
        #Возвращаем его к левой стороне экрана
        for cell in list_map:
            cell.X += change_x
    #Если игровое поле ушло вниз от границы экрана       
    if list_map[0].Y > 0:
        change_y = list_map[0].Y * -1
        #Возвращаем его к верхней стороне экрана
        for cell in list_map:
            cell.Y += change_y
    #Если игровое поле ушло вверх от границы экрана      
    elif  list_map[-1].Y + list_map[-1].WIDTH < SCREEN_H:
        change_y = SCREEN_H - (list_map[-1].Y + list_map[-1].WIDTH)
        #Возвращаем его к нижней стороне экрана
        for cell in list_map:
            cell.Y += change_y
def matrix_image(win, player_lvl1, gold, iron, crystal, wood, stone, tree_full, 
                tree,mat_objetcs_lvl1,list_objects_cells_lvl1,SCREEN_W,
                SCREEN_H,count_move,changed_x,changed_y,
                ironmine, goldmine, farm, gemsmine,sawmill, stonebreaker,flag_green,list_studied_map,portal, fog_war,
                list_cor_player_xy,W_CELL_MINI_MAP ,H_CELL_MINI_MAP,X_FRAME_MM,Y_FRAME_MM,list_cells_MM,list_cor_portals,
                LENGTH_MAP ):

    list_xy = [0,0]
    #Индекс клетки, к которой привязан объект
    index_cells = 0
    # Координата конкретной клетки для миникарты
    X_CELL_MM = X_FRAME_MM
    Y_CELL_MM = Y_FRAME_MM
    # Нужно ли добавлять клетку для мини-карты
    flag_cell_MM = True
    #Перебераем список объектов
    for obj_list1 in mat_objetcs_lvl1:
        for obj_list2 in obj_list1:
            for obj in obj_list2:
                flag_cell_MM =True
                    
                
                if obj == 'p':   
                    #Привязываем координаты персонажа к клетке
                    player_lvl1.X = list_objects_cells_lvl1[index_cells].X+changed_x
                    player_lvl1.Y = list_objects_cells_lvl1[index_cells].Y+changed_y
                    list_cor_player_xy[0] = list_objects_cells_lvl1[index_cells].X+changed_x
                    list_cor_player_xy[1] = list_objects_cells_lvl1[index_cells].Y+changed_y
                    #отображаем персонажа
                    player_lvl1.show_image(win)
                    flag_cell_MM = False
                    list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'yellow'))
                #Отрисовуем ресурсы
                elif obj == 'i':
                    iron.X = list_objects_cells_lvl1[index_cells].X
                    iron.Y = list_objects_cells_lvl1[index_cells].Y
                    iron.show_image(win)
                elif obj == 'g':
                    gold.X = list_objects_cells_lvl1[index_cells].X
                    gold.Y = list_objects_cells_lvl1[index_cells].Y
                    gold.show_image(win)
                elif obj == 'w':
                    wood.X = list_objects_cells_lvl1[index_cells].X
                    wood.Y = list_objects_cells_lvl1[index_cells].Y
                    wood.show_image(win)
                elif obj == 's':
                    stone.X = list_objects_cells_lvl1[index_cells].X
                    stone.Y = list_objects_cells_lvl1[index_cells].Y
                    stone.show_image(win)
                elif obj == 'c':
                    crystal.X = list_objects_cells_lvl1[index_cells].X
                    crystal.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2 
                    crystal.show_image(win)
                elif obj == 'T':
                    tree_full.X = list_objects_cells_lvl1[index_cells].X
                    tree_full.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2 
                    tree_full.show_image(win)
                elif obj == 't':
                    tree.X = list_objects_cells_lvl1[index_cells].X
                    tree.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2
                    tree.show_image(win)

                elif obj == 'F':
                    farm.X = list_objects_cells_lvl1[index_cells].X
                    farm.Y = list_objects_cells_lvl1[index_cells].Y 
                    farm.show_image(win)
                    list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'white'))
                    list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM,'white'))
                    list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP,'white'))
                    list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM+ H_CELL_MINI_MAP,'white'))
                    flag_cell_MM = False
                    
                elif obj == 'N':
                    stonebreaker.X = list_objects_cells_lvl1[index_cells].X
                    stonebreaker.Y = list_objects_cells_lvl1[index_cells].Y 
                    stonebreaker.show_image(win)
                    list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'white'))
                    list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM,'white'))
                    list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP,'white'))
                    list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM+ H_CELL_MINI_MAP,'white'))
                    flag_cell_MM = False
                elif obj == 'X':
                    gemsmine.X = list_objects_cells_lvl1[index_cells].X
                    gemsmine.Y = list_objects_cells_lvl1[index_cells].Y 
                    gemsmine.show_image(win)
                    list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'white'))
                    list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM,'white'))
                    list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP,'white'))
                    list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM+ H_CELL_MINI_MAP,'white'))
                    flag_cell_MM = False
                elif obj == 'R':
                    goldmine.X = list_objects_cells_lvl1[index_cells].X
                    goldmine.Y = list_objects_cells_lvl1[index_cells].Y 
                    goldmine.show_image(win)
                    list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'white'))
                    list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM,'white'))
                    list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP,'white'))
                    list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM+ H_CELL_MINI_MAP,'white'))
                    flag_cell_MM = False
                elif obj == 'H':
                    sawmill.X = list_objects_cells_lvl1[index_cells].X
                    sawmill.Y = list_objects_cells_lvl1[index_cells].Y 
                    sawmill.show_image(win)
                    list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'white'))
                    list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM,'white'))
                    list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP,'white'))
                    list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM+ H_CELL_MINI_MAP,'white'))
                    flag_cell_MM = False
                elif obj == 'D':
                    ironmine.X = list_objects_cells_lvl1[index_cells].X
                    ironmine.Y = list_objects_cells_lvl1[index_cells].Y 
                    ironmine.show_image(win)
                    list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'white'))
                    list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM,'white'))
                    list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP,'white'))
                    list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM+ H_CELL_MINI_MAP,'white'))
                    flag_cell_MM = False
                elif obj == 'P':
                    
                    portal.X = list_objects_cells_lvl1[index_cells].X
                    portal.Y = list_objects_cells_lvl1[index_cells].Y
                    portal.show_image(win)
                        
                        
                for i in player_lvl1.list_capture_buildings:
                    if list_xy[0] == i[1] and list_xy[1] == i[0]:
                        flag_green.X = list_objects_cells_lvl1[index_cells].X + SCREEN_W // 38
                        flag_green.Y = list_objects_cells_lvl1[index_cells].Y  - SCREEN_W // 40
                        flag_green.show_image(win)
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'green_dark'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM,'green_dark'))
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP,'green_dark'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM+ H_CELL_MINI_MAP,'green_dark'))
                        flag_cell_MM = False


                
                for c in list_cells_MM:
                    if c[0] == X_CELL_MM and c[1] == Y_CELL_MM:
                        flag_cell_MM = False
                        break
                if flag_cell_MM ==True :
                    list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'green'))
            """"Индексы текущей клетки по циклу"""
            
            list_xy[0]+= 1
            if list_xy[0] == LENGTH_MAP:
                list_xy[0] = 0
                list_xy[1] += 1
            index_cells += 1

            X_CELL_MM += W_CELL_MINI_MAP
        Y_CELL_MM += H_CELL_MINI_MAP
        X_CELL_MM = X_FRAME_MM
        



    X_CELL_MM = X_FRAME_MM
    Y_CELL_MM = Y_FRAME_MM
    list_xy = [0,0]
    #Индекс клетки, к которой привязан объект
    index_cells = 0
    # Цикл для отрисовки тумана
    for obj_list1 in mat_objetcs_lvl1:
        for obj_list2 in obj_list1:
            for obj in obj_list2:
                #Перебираем список с изучеными клетками и проверяем с текущей клеткой 
                for cor in list_studied_map:
                   

                    if list_xy == cor:
                        draw_frog = False
                        break
                    else: 
                        draw_frog = True

            if draw_frog:

                fog_war.X = list_objects_cells_lvl1[index_cells].X
                fog_war.Y = list_objects_cells_lvl1[index_cells].Y
                fog_war.show_image(win)

                list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'black'))
            list_xy[0]+= 1
            if list_xy[0] == LENGTH_MAP:
                list_xy[0] = 0
                list_xy[1] += 1
                
            index_cells += 1

            X_CELL_MM += W_CELL_MINI_MAP
        Y_CELL_MM += H_CELL_MINI_MAP
        X_CELL_MM = X_FRAME_MM         


def create_map(list_cells, list_objects_cells,SCREEN_W,SCREEN_H):
    #Стартовые координаты клеток
    x = 0
    y = 0
    #Перебераем ряды уровня
    for el in list_cells:
        #Перебераем каждую клетку
        for cell in el:
            #Если значение клетки равно нулю
            if cell == '0':
                #В список клеток добавляем объект клетки
                list_objects_cells.append(Graphic_elements(x,y,SCREEN_W//19,SCREEN_W//19,'images/cell.jpg'))
            #Увеличиваем х, двигаясь по ряду
            x += SCREEN_W//19
        #Увеличиваем y, двигаясь по столбцамя
        y += SCREEN_W //19
        #Обнуляем x
        x = 0

#Перебираем список захваченый зданий и игроку начесляем ресурсы
def resourse_accural(list_capture_buildings_symbol, resources_dict):
    for i in list_capture_buildings_symbol:
        if i == 'F':
            resources_dict['food'] += randint(5,6)
        elif i == 'H':
            resources_dict['wood'] += randint(4,5)
        elif i == 'D':
            resources_dict['iron'] += randint(2,3)
        elif i == 'N':
            resources_dict['stone'] += randint(3,4)
        elif i == 'R':
            resources_dict['gold'] += randint(1,2)
        elif i == 'X':
            resources_dict['crystal'] += 1


def move_to_hero(CENTER_CELL_COR,list_cor_player_xy,list_objects_cells_lvl1,SCREEN_W,SCREEN_H):
    #Перемещаемся к герою по X
    if CENTER_CELL_COR[0] >= list_cor_player_xy[0]:
        difference = CENTER_CELL_COR[0] - list_cor_player_xy[0]
        for cell in list_objects_cells_lvl1:
            cell.X += difference
    elif CENTER_CELL_COR[0] <= list_cor_player_xy[0]:
        difference = list_cor_player_xy[0] - CENTER_CELL_COR[0]  
        for cell in list_objects_cells_lvl1:
            cell.X -= difference
    #Перемещаемся к герою по Y
    if CENTER_CELL_COR[1] >= list_cor_player_xy[1]:
        difference = CENTER_CELL_COR[1] - list_cor_player_xy[1]
        for cell in list_objects_cells_lvl1:
            cell.Y += difference

    elif CENTER_CELL_COR[1] <= list_cor_player_xy[1]:
        difference = list_cor_player_xy[1] - CENTER_CELL_COR[1]  
        for cell in list_objects_cells_lvl1:
            cell.Y -= difference
            
    #Если игровое поле ушло вправо от границы экрана
    if list_objects_cells_lvl1[0].X > 0:
        change_x = list_objects_cells_lvl1[0].X * -1
        #Возвращаем его к правой стороне экрана
        for cell in list_objects_cells_lvl1:
            cell.X += change_x
    #Если игровое поле ушло влево от границы экрана
    elif  list_objects_cells_lvl1[-1].X + list_objects_cells_lvl1[-1].WIDTH < SCREEN_W:
        change_x = SCREEN_W - (list_objects_cells_lvl1[-1].X + list_objects_cells_lvl1[-1].WIDTH)
        #Возвращаем его к левой стороне экрана
        for cell in list_objects_cells_lvl1:
            cell.X += change_x
    #Если игровое поле ушло вниз от границы экрана       
    if list_objects_cells_lvl1[0].Y > 0:
        change_y = list_objects_cells_lvl1[0].Y * -1
        #Возвращаем его к верхней стороне экрана
        for cell in list_objects_cells_lvl1:
            cell.Y += change_y
    #Если игровое поле ушло вверх от границы экрана      
    elif  list_objects_cells_lvl1[-1].Y + list_objects_cells_lvl1[-1].WIDTH < SCREEN_H:
        change_y = SCREEN_H - (list_objects_cells_lvl1[-1].Y + list_objects_cells_lvl1[-1].WIDTH)
        #Возвращаем его к нижней стороне экрана
        for cell in list_objects_cells_lvl1:
            cell.Y += change_y


