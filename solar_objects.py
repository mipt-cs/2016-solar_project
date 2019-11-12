# coding: utf-8
# license: GPLv3


class Star:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    # type = "Star"
    """Признак объекта звезды"""

    # m = 0
    """Масса звезды"""

    # x = 0
    """Координата по оси **x**"""

    # y = 0
    """Координата по оси **y**"""

    # Vx = 0
    """Скорость по оси **x**"""

    # Vy = 0
    """Скорость по оси **y**"""

    # Fx = 0
    """Сила по оси **x**"""

    # Fy = 0
    """Сила по оси **y**"""

    # R = 5
    """Радиус звезды"""

    # color = "red"
    """Цвет звезды"""

    # image = None
    """Изображение звезды"""

    def __init__(self):
        self.type = 'star'
        self.m = 0
        self.x = 0
        self.y = 0
        self.Vx = 0
        self.Vy = 0
        self.Fx = 0
        self.Fy = 0
        self.R = 5
        self.color = 'red'
        self.image = None
        

class Planet:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    # type = "Planet"
    """Признак объекта планеты"""

    # m = 0
    """Масса планеты"""

    # x = 0
    """Координата по оси **x**"""

    # y = 0
    """Координата по оси **y**"""

    # Vx = 0
    """Скорость по оси **x**"""

    # Vy = 0
    """Скорость по оси **y**"""

    # Fx = 0
    """Сила по оси **x**"""

    # Fy = 0
    """Сила по оси **y**"""

    # R = 5
    """Радиус планеты"""

    # color = "green"
    """Цвет планеты"""

    # image = None
    """Изображение планеты"""

    def __init__(self):
        self.type = 'planet'
        self.m = 0
        self.x = 0
        self.y = 0
        self.Vx = 0
        self.Vy = 0
        self.Fx = 0
        self.Fy = 0
        self.R = 5
        self.color = 'red'
        self.image = None

