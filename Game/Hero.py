from numpy import where
import pygame
from random import choice,randint
from sounds import Sounds
from graphic_elements import Graphic_elements
import os

pygame.init()

class Main_Hero(Graphic_elements):
    def __init__(self,x,y,width,height,path,SCREEN_W,SCREEN_H,where_move,count_move):
        super().__init__(x,y,width,height,path)
        self.player_cor = [1,2]
        self.SCREEN_W = SCREEN_W
        self.SCREEN_H = SCREEN_H
        self.where_move = where_move
        self.count_move = count_move
        self.changed_x = 0
        self.changed_y = 0
        self.index = 0
        self.list_images_right = []
        self.list_images_left = []
        self.list_images_up = []
        self.list_images_down = []
        self.count_step = 20
        for i in range(4):
            path = os.path.join(os.path.abspath(__file__+'/..'),'images/player/right/'+str(i)+'.png')
            self.list_images_right.append(path)
            path = os.path.join(os.path.abspath(__file__+'/..'),'images/player/left/'+str(i)+'.png')
            self.list_images_left.append(path)
            path = os.path.join(os.path.abspath(__file__+'/..'),'images/player/up/'+str(i)+'.png')
            self.list_images_up.append(path)
            path = os.path.join(os.path.abspath(__file__+'/..'),'images/player/down/'+str(i)+'.png')
            self.list_images_down.append(path)
        self = Graphic_elements(0, 0, SCREEN_W//19, SCREEN_W//19, 'images/player/player_front.png')
        

        
        
    def move_sprite(self, mat_objetcs, LENGTH_MAP,resources_dict,recourse_sounds):
        
        #Если нажата клавиша ВПРАВО
        if self.count_step != 0:
            if self.where_move == 'right' and self.count_move <= 9:
                if self.count_move == 0 or self.count_move == 3 or self.count_move == 6 or self.count_move == 9:
                    self.path = self.list_images_right[self.index]
                    self.image_load()
                    self.index+=1
                self.X += (self.SCREEN_W//19)/10
                self.changed_x = self.count_move*(self.SCREEN_W//19)/10
                self.count_move+=1

            elif self.count_move > 9 and self.where_move == 'right':
                self.index = 0
                self.count_move = 0
                # self.path = 'images/player/player_front.png'
                # self.image_load()
                self.where_move = None
                self.changed_x = 0
                mat_objetcs[self.player_cor[0]][self.player_cor[1] + 1] = 'p'
                mat_objetcs[self.player_cor[0]][self.player_cor[1]] = '0'
                self.player_cor[1] += 1
                
            if self.where_move == 'left' and self.count_move <= 9:
                if self.count_move == 0 or self.count_move == 3 or self.count_move == 6 or self.count_move == 9:
                    self.path = self.list_images_left[self.index]
                    self.image_load()
                    self.index+=1
                self.X -= (self.SCREEN_W//19)/10
                self.changed_x = -1*self.count_move*(self.SCREEN_W//19)/10
                self.count_move+=1
            elif self.count_move > 9 and self.where_move == 'left':
                self.index = 0
                self.count_move = 0
                # self.path = 'images/player/player_front.png'
                # self.image_load()
                self.where_move = None
                self.changed_x = 0
                mat_objetcs[self.player_cor[0]][self.player_cor[1] - 1] = 'p'
                #Указываем, что на метсе, где стоя игрок - пустая клетка
                mat_objetcs[self.player_cor[0]][self.player_cor[1]] = '0'
                #Изменяем координату игрока
                self.player_cor[1] -= 1
            if self.where_move == 'up' and self.count_move <= 9:
                if self.count_move == 0 or self.count_move == 3 or self.count_move == 6 or self.count_move == 9:
                    self.path = self.list_images_up[self.index]
                    self.image_load()
                    self.index+=1
                self.Y -= (self.SCREEN_W//19)/10
                self.changed_y = -1*self.count_move*(self.SCREEN_W//19)/10
                self.count_move+=1

            elif self.count_move > 9 and self.where_move == 'up':
                self.count_move = 0
                self.index = 0
                self.where_move = None
                # self.path = 'images/player/player_front.png'
                # self.image_load()
                self.changed_y = 0
                mat_objetcs[self.player_cor[0] - 1][self.player_cor[1]] = 'p'
                mat_objetcs[self.player_cor[0]][self.player_cor[1]] = '0'
                self.player_cor[0] -= 1

            if self.where_move == 'down' and self.count_move <= 9:
                if self.count_move == 0 or self.count_move == 3 or self.count_move == 6 or self.count_move == 9:
                    self.path = self.list_images_down[self.index]
                    self.image_load()
                    self.index+=1
                self.X += (self.SCREEN_W//19)/10
                self.changed_y = self.count_move*(self.SCREEN_W//19)/10
                self.count_move+=1

            elif self.count_move > 9 and self.where_move == 'down':
                self.index = 0
                self.count_move = 0
                self.where_move = None
                # self.path = 'images/player/player_front.png'
                # self.image_load()
                self.changed_y = 0
                mat_objetcs[self.player_cor[0] + 1][self.player_cor[1]] = 'p'
                mat_objetcs[self.player_cor[0]][self.player_cor[1]] = '0'
                self.player_cor[0] += 1
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                #Если мы стоим не с правого краю карты
                if self.player_cor[1] != LENGTH_MAP - 1:
                    #Вызываем функции подбора ресрусов
                    self.take_resource(self.player_cor[0],self.player_cor[1] + 1,'gold','g',mat_objetcs,2,4,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0],self.player_cor[1] + 1,'iron','i',mat_objetcs,4,6,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0],self.player_cor[1] + 1,'wood','w',mat_objetcs,8,10,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0],self.player_cor[1] + 1,'stone','s',mat_objetcs,6,8,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0],self.player_cor[1] + 1,'crystal','c',mat_objetcs,1,2,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0],self.player_cor[1] + 1,'food','T',mat_objetcs,10,12,resources_dict,recourse_sounds)
                    #Если двигаемся вправо
                    if mat_objetcs[self.player_cor[0]][self.player_cor[1] + 1] == '0' and self.where_move == None:
                        self.where_move = 'right'
                        self.count_step -= 1
                        #Указываем, что игрок переместился на клетку вправо
                    
            #Если нажата клавиша ВЛЕВО
            elif keys[pygame.K_LEFT]:
                if self.player_cor[1] != 0:
                    self.take_resource(self.player_cor[0],self.player_cor[1] - 1,'gold','g',mat_objetcs,2,4,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0],self.player_cor[1] - 1,'iron','i',mat_objetcs,4,6,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0],self.player_cor[1] - 1,'wood','w',mat_objetcs,8,10,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0],self.player_cor[1] - 1,'stone','s',mat_objetcs,6,8,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0],self.player_cor[1] - 1,'crystal','c',mat_objetcs,1,2,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0],self.player_cor[1] - 1,'food','T',mat_objetcs,10,12,resources_dict,recourse_sounds)
                    if mat_objetcs[self.player_cor[0]][self.player_cor[1] - 1] == '0' and self.where_move == None:
                        self.where_move = 'left'
                        self.count_step -= 1

                        
            #Если нажата клавиша ВВЕРХ
            elif keys[pygame.K_UP]:
                if self.player_cor[0] != 0:
                    
                    self.take_resource(self.player_cor[0]-1,self.player_cor[1],'gold','g',mat_objetcs,2,4,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0]-1,self.player_cor[1],'iron','i',mat_objetcs,4,6,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0]-1,self.player_cor[1],'wood','w',mat_objetcs,8,10,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0]-1,self.player_cor[1],'stone','s',mat_objetcs,6,8,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0]-1,self.player_cor[1],'crystal','c',mat_objetcs,1,2,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0]-1,self.player_cor[1],'food','T',mat_objetcs,10,12,resources_dict,recourse_sounds)
                    if mat_objetcs[self.player_cor[0] - 1][self.player_cor[1]] == '0' and self.where_move == None:
                        self.where_move = 'up'
                        self.count_step -= 1
                        
            #Если нажата клавиша ВНИЗ
            elif keys[pygame.K_DOWN]:
                if self.player_cor[0] != LENGTH_MAP - 1:
                    self.take_resource(self.player_cor[0]+1,self.player_cor[1],'gold','g',mat_objetcs,2,4,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0]+1,self.player_cor[1],'iron','i',mat_objetcs,4,6,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0]+1,self.player_cor[1],'wood','w',mat_objetcs,8,10,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0]+1,self.player_cor[1],'stone','s',mat_objetcs,6,8,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0]+1,self.player_cor[1],'crystal','c',mat_objetcs,1,2,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0]+1,self.player_cor[1],'food','T',mat_objetcs,10,12,resources_dict,recourse_sounds)
                    if mat_objetcs[self.player_cor[0] + 1][self.player_cor[1]] == '0' and self.where_move == None:
                        self.where_move = 'down'
                        self.count_step -= 1
        
        
        



    def take_resource(self,index_x,index_y,name_resource,resource_symb,mat_objetcs,min_count,max_count,resources_dict,recourse_sounds):
        if mat_objetcs[index_x][index_y] == resource_symb:
            resources_dict[name_resource] += randint(min_count, max_count)
            choice(recourse_sounds).play_sound()
            if resource_symb == 'T':
                mat_objetcs[index_x][index_y] = 't'
            else:
                mat_objetcs[index_x][index_y] = '0'