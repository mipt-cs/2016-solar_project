# coding: utf-8
# license: GPLv3

from solar_objects import *


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star" or object_type == "planet":
                objectt = SpaceObject()
                parse_parameters(line, objectt)
                objects.append(objectt)
            else:
                print("Unknown space object")

    return objects


def parse_parameters(line, object):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    line = line.replace('\n', '')
    line = line.split(' ')
    object.type = line[0]
    object.R = int(line[1])
    object.color = line[2]
    object.m = float(line[3])
    object.x = float(line[4])
    object.y = float(line[5])
    object.Vx = float(line[6])
    object.Vy = float(line[7])
    print(object.Vy)


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            out_file.write(str(obj.type) + ' ' + str(obj.R) + ' ' + str(obj.color) + ' ' + str(obj.m) + ' ' + str(obj.x)
                           + ' ' + str(obj.y) + ' ' + str(obj.Vx) + ' ' + str(obj.Vy) + '\n')


if __name__ == "__main__":
    print("This module is not for direct call!")
