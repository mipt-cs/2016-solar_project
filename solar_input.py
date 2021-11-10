# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """ Cчитывает данные о космических объектах из файла, создаёт сами объекты
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
                star = parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                planet = parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """ Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описанием звезды.
    **star** — объект звезды.

    """

    obj_type, r, color, m, x, y, vx, vy = line.split()
    star.R = float(r)
    star.color = color
    star.m = float(m)
    star.x = float(x)
    star.y = float(y)
    star.Vx = float(vx)
    star.Vy = float(vy)

    return star


def parse_planet_parameters(line, planet):
    """ Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.

    Нумерует пробелы. Радиус - то, что между первым и вторым пробелом в строке, и так далее.
    """

    obj_type, r, color, m, x, y, vx, vy = line.split()
    planet.R = float(r)
    planet.color = color
    planet.m = float(m)
    planet.x = float(x)
    planet.y = float(y)
    planet.Vx = float(vx)
    planet.Vy = float(vy)

    return planet


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
            obj_type, r, color, m, x, y, vx, vy = map(str,
                                                      [obj.type, obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx,
                                                       obj.Vy])
            out_file.write(
                obj_type + " " + r + " " + color + " " + m + " " + x + " " + y + " " + vx + " " + vy + "\n")


if __name__ == "__main__":
    print("This module is not for direct call!")
