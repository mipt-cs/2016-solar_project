# coding: utf-8
# license: GPLv3


class Star:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселях и её цвет.
    """
    def __init__(self, type, R, color, m, x, y, velocity_x, velocity_y):
        self.type = type
        """Признак объекта звезды"""
        self.m = m
        """Масса звезды"""

        self.x = x
        """Координата по оси **x**"""

        self.y = y
        """Координата по оси **y**"""

        self.Vx = velocity_x
        """Скорость по оси **x**"""

        self.Vy = velocity_y
        """Скорость по оси **y**"""

        self.Fx = 0
        """Сила по оси **x**"""

        self.Fy = 0
        """Сила по оси **y**"""

        self.R = R
        """Радиус звезды"""

        self.color = color
        """Цвет звезды"""

        self.image = None
        """Изображение звезды"""


class Planet:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """
    def __init__(self, type, R, color, m, x, y, velocity_x, velocity_y):

        self.type = type
        """Признак объекта звезды"""
        self.m = m
        """Масса звезды"""

        self.x = x
        """Координата по оси **x**"""

        self.y = y
        """Координата по оси **y**"""

        self.Vx = velocity_x
        """Скорость по оси **x**"""

        self.Vy = velocity_y
        """Скорость по оси **y**"""

        self.Fx = 0
        """Сила по оси **x**"""

        self.Fy = 0
        """Сила по оси **y**"""

        self.R = R
        """Радиус звезды"""

        self.color = color
        """Цвет звезды"""

        self.image = None
        """Изображение звезды"""