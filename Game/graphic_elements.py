import os
from pygame import*
#Класс для удобного отображения графических єлементов
class Graphic_elements():
    def __init__(self,x,y,width,height,path,name = 'name',start_x=None,start_y=None):
        self.start_x = start_x
        self.start_y = start_y
        self.X = x
        self.Y = y
        self.HEIGHT = height
        self.WIDTH = width
        self.NAME = name
        self.path = path
        if self.path != None:   
            self.image_load()
    #Метод для подгрузки, задания размера картинке и ее отображения
    def show_image(self,screen_object):
        screen_object.blit(self.IMG, (self.X,self.Y))
    def image_load(self):
        self.IMG = os.path.join(os.path.abspath(__file__ + "/.."), self.path)
        self.IMG = image.load(self.IMG)
        self.IMG = transform.scale(self.IMG, (self.WIDTH,self.HEIGHT))

