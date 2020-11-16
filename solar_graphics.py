# coding: utf-8
# license: GPLv3

"""
Модуль построения графиков
"""

from matplotlib import pyplot as pl


def py(a, b):
    return (a*a + b*b)**0.5


def get_moment(obj, time, i):  # собирает информацию об объекте в некоторый момент времени
    with open('_program_data\data.txt', 'a') as open_file:
        open_file.write("%s %f %f %f \n" % (i+1, py(obj.x, obj.y), py(obj.Vx, obj.Vy), time))
    pass


def draw_graph():  # строит несколько графиков

    pass


if __name__ == "__main__":
    print("This module is not for direct call!")
