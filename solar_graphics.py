# coding: utf-8
# license: GPLv3

"""
Модуль построения графиков
"""

from matplotlib import pyplot as pl


def py(a, b):
    return (a*a + b*b)**0.5


def get_moment(obj, time, i):
    """
    Функция записывает в файл данных текущее значение времени и параметров тела
        obj: космическое тело (star или planet)
        time: текущий момент времени
        i: номер тела среди всех тел
    """
    with open('_program_data\data.txt', 'a') as open_file:
        open_file.write("%s %f %f %f \n" % (i+1, py(obj.x, obj.y), py(obj.Vx, obj.Vy), time))
    pass


def read_graph():
    """
    Функция считывает из файла с данными информацию
    """
    with open('_program_data\data.txt', 'r') as open_file:
        data = open_file.readlines()
    for i, line in enumerate(data):
        data[i] = line.strip().split(' ')

    all_the_needed_data = []
    elements = []
    for q, line in enumerate(data):
        if elements.count(int(line[0])) == 0:
            elements.append(int(line[0]))
            all_the_needed_data.append([[], [], []])  # массив для хранения координат, скоростей и времени
        for i, part in enumerate(line):
            if i == 0:
                continue
            else:
                all_the_needed_data[int(line[0])-1][i-1].append(float(line[i]))


def draw_graph():  # строит несколько графиков
    pass


if __name__ == "__main__":
    print("This module is not for direct call!")
