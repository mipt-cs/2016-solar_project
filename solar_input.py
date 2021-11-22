# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


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
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":  # FIXED: do the same for planet
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


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
    type, R, color, *physical_parameters = line.split()

    R = int(R)
    m, x, y, Vx, Vy = map(float, physical_parameters)

    star.R = R

    star.color = color

    star.m = m

    star.x = x

    star.y = y

    star.Vx = Vx

    star.Vy = Vy
    # FIXED: assign fileds of object from input


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

    type, R, color, *physical_parameters = line.split()

    R = int(R)
    m, x, y, Vx, Vy = map(float, physical_parameters)

    planet.R = R

    planet.color = color

    planet.m = m

    planet.x = x

    planet.y = y

    planet.Vx = Vx

    planet.Vy = Vy
    # FIXED: assign fileds of object from input


def print_data_to_file(obj_data, out_file):
    """Записывает данные об объекте в виде строки.

    Параметры:

    **obj_data** — список параметров объекта
    **out_file** — файл для записи
    """
    print(' '.join(map(str, obj_data)), file=out_file)


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки имеют следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            obj_data = (obj.type, obj.R, obj.color, obj.m,
                        obj.x, obj.y, obj.Vx, obj.Vy)
            print_data_to_file(obj_data, out_file)
        # FIXED: store real values of parameters in file


def reset_statistics(statistics_filename, space_objects):
    """Сбросить статистику в файле к начальному состоянию.
    В начале приводятся постоянные характеристики объектов:
    <тип объекта> <радиус в пикселах> <цвет> <масса>

    Параметры:

    **statistics_filename** — имя файла статистики
    **space_objects** — список объектов планет и звёзд
    """
    with open(statistics_filename, 'w') as out_file:
        for obj in space_objects:
            obj_data = (obj.type, obj.R, obj.color, obj.m)
            print_data_to_file(obj_data, out_file)
        print(file=out_file)


def save_statistics_to_file(statistics_filename, space_objects):
    """Сохраняет статистику значений положений и скоростей в заданный файл.

    Параметры:

    **statistics_filename** — имя заданного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(statistics_filename, 'a') as out_file:
        for obj in space_objects:
            obj_data = (obj.x, obj.y, obj.Vx, obj.Vy)
            print_data_to_file(obj_data, out_file)
        print(file=out_file)


def read_statistics_from_file(statistics_filename):
    """Получает статистику положений и скоростей из заданного файла.

    Параметры:

    **statistics_filename** — имя заданного файла
    """
    with open(statistics_filename, 'r') as stats_file:
        data = stats_file.read().split('\n\n')
    object_properties = [row.split() for row in data.pop(0).split('\n')]
    data = [[[float(x)
              for x in row.split()]
             for row in entry.split('\n')]
            for entry in data]
    print(object_properties, data[:5])
    return object_properties, data

# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл


if __name__ == "__main__":
    print("This module is not for direct call!")
