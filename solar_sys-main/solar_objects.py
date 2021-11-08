# coding: utf-8
# license: GPLv3

class space_objects():

    def __init__ (self,R,color,m,x,y,Vx,Vy):
        """Тип данных, описывающий звезду.
        Содержит массу, координаты, скорость звезды,
        а также визуальный радиус звезды в пикселах и её цвет.
        """

        #self.type = int(type)
        """Признак объекта звезды"""

        self.m = float(m)
        """Масса звезды"""

        self.x = float(x)
        """Координата по оси **x**"""

        self.y = float(y)
        """Координата по оси **y**"""

        self.Vx = float(Vx)
        """Скорость по оси **x**"""

        self.Vy = float(Vy)
        """Скорость по оси **y**"""

        self.Fx = int(0)
        """Сила по оси **x**"""

        self.Fy = int(0)
        """Сила по оси **y**"""

        self.R = float(R)
        """Радиус звезды"""

        self.color = color
        """Цвет звезды"""

       # self.image = image

class Star(space_objects):

    pass



class Planet(space_objects):

    pass
