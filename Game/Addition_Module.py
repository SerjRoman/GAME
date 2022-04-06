from graphic_elements import Graphic_elements


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
    elif  list_map[-1].X + list_map[-1].WIDTH < SCREEN_W:
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
def matrix_image(win, player_lvl1, gold, iron, crystal, wood, stone, tree_full, tree,mat_objetcs_lvl1,list_objects_cells_lvl1,SCREEN_W,SCREEN_H,count_move,changed_x,changed_y):
    index_str = 0
            #Индекс элемента, где находиться объект
    index_obj = 0
            #Индекс клетки, к которой привязан объект
    index_cells = 0
            #Перебераем список объектов
    for obj_list1 in mat_objetcs_lvl1:
        for obj_list2 in obj_list1:
            for obj in obj_list2:
                        #Если объект - это персонаж
                if obj == 'p':   
                            #Привязываем координаты персонажа к клетке
                    player_lvl1.X = list_objects_cells_lvl1[index_cells].X+changed_x
                    player_lvl1.Y = list_objects_cells_lvl1[index_cells].Y+changed_y
                            #отображаем персонажа
                    player_lvl1.show_image(win)
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
                    crystal.Y = list_objects_cells_lvl1[index_cells].Y
                    crystal.show_image(win)
                elif obj == 'T':
                    tree_full.X = list_objects_cells_lvl1[index_cells].X
                    tree_full.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2 
                    tree_full.show_image(win)
                elif obj == 't':
                    tree.X = list_objects_cells_lvl1[index_cells].X
                    tree.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2
                    tree.show_image(win)
                index_obj += 1
                index_cells += 1
            index_str +=0
            index_obj = 0
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