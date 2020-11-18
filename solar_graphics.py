# coding: utf-8
# license: GPLv3

"""
Модуль построения графиков
"""

from matplotlib import pyplot as pl


def py(a, b):
    """
    Теорема Пифагора на плоскости
    """
    return (a*a + b*b)**0.5


def delete_previous():
    """
    Функция очищает файл data.txt перед началом записи
    """
    open_file = open('_program_data\data.txt', 'w')
    open_file.close()
    pass


def get_moment(obj, time, i):
    """
    Функция записывает в файл данных текущее значение времени и параметров тела
        obj: космическое тело (star или planet)
        time: текущий момент времени
        i: номер тела среди всех тел
    """
    with open('_program_data\data.txt', 'a') as open_file:
        open_file.write("%s %f %f %i \n" % (i+1, py(obj.x, obj.y), py(obj.Vx, obj.Vy), int(time)))
    pass


def read_graph():
    """
    Функция считывает из файла с данными информацию.
    В файле находятся строки вида
    № тела; расстояние до точки 0,0; скорость тела; время
    """
    with open('_program_data\data.txt', 'r') as open_file:
        data = open_file.readlines()
    for i, line in enumerate(data):
        data[i] = line.strip().split(' ')

    all_the_needed_data = []
    elements = []
    for q, line in enumerate(data):
        num = int(line[0])
        if elements.count(num) == 0:
            elements.append(num)
            all_the_needed_data.append([num, [], [], []])  # массив для хранения координат, скоростей и времени
        for i, part in enumerate(line):  # для каждого элемента в строке [№, r, V, t]
            if i == 0:  # номер пропускаем
                continue
            elif i != 3:
                all_the_needed_data[num-1][i].append(float(line[i]))  # float r и V
            else:
                all_the_needed_data[num-1][i].append(int(line[i]))  # int time
    return all_the_needed_data


def draw_graph():
    """
    Функция строит графики зависимости v(t), r(t), v(r) для каждого тел
    Данные data из функции read_graph имеет вид [[]]
    """
    data = read_graph()
    for k in range(len(data)):
        pl.scatter(data[k][3], data[k][2])  # v(t)
    pl.show()
    pass


if __name__ == "__main__":
    print("This module is not for direct call!")
