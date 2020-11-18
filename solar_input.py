# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet  # импорт класса Star и Planet из solar_objects


def read_space_objects_data_from_file(input_filename):
    """Считывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []  # массив со звездами и планетами вперемешку
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":  # добавляем звезду
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":  # добавляем планету
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def split_and_brush_values(line):
    """
    Разделяет и "очисляет" элементы принятой линии вида
    Класс(стр) радиус(числ) цвет(стр) масса(числ) коорд_x(числ) коорд_y(числ) скор_x(числ) скор_y(числ)
    """
    params = line.strip().split(' ')  # разделение частей строки по пробелам
    for i in range(len(params)):
        params[i] = params[i].strip()
        if i == 0 or i == 2:
            continue  # пропускаем строки с буквенными обозначениями
        else:
            params[i] = float(params[i])  # делаем числовые параметры числами
    return params


def parse_star_parameters(line, star):
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

    params = split_and_brush_values(line)
    star.type = 'star'
    star.R = params[1]
    star.color = params[2]
    star.m = params[3]
    star.x = params[4]
    star.y = params[5]
    star.Vx = params[6]
    star.Vy = params[7]

    pass


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """

    params = split_and_brush_values(line)
    planet.type = 'planet'
    planet.R = params[1]
    planet.color = params[2]
    planet.m = params[3]
    planet.x = params[4]
    planet.y = params[5]
    planet.Vx = params[6]
    planet.Vy = params[7]

    pass


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
        for obj in space_objects:  # для каждого объекта среди всех движущихся...
            out_file.write("%s %d %s %f %f %f %f %f \n"
                           % (obj.type, obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy))
        # нужно как-то сделать запись чисел в стандартном виде!


if __name__ == "__main__":
    print("This module is not for direct call!")
