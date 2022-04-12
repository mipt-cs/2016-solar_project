# coding: utf-8
# license: GPLv3


class SpaceObject:
    """Тип данных, описывающий космический объект.
    Содержит имя типа( палнета или звезда), массу, координаты, скорость,
    а также визуальный радиус в пикселах и цвет.
    """

    def __init__(self):
        self.type = "object"
        self.m = 0
        self.x = 0
        self.y = 0
        self.Vx = 0
        self.Vy = 0
        self.Fx = 0
        self.Fy = 0
        self.R = 5
        self.color = "red"
        self.image = None
