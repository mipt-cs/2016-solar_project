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
            if object_type == "planet":
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
    star_list = []
    for i in range(len(line)): 
        if line[i] == ' ': 
            star_list.append(i)
    star.R = int(float(line[star_list[0]+1:star_list[1]]))
    star.color = (line[star_list[1] + 1:star_list[2]])
    star.m = int(float(line[star_list[2] + 1:star_list[3]]))
    star.x = int(float(line[star_list[3] + 1:star_list[4]]))
    star.y = int(float(line[star_list[4] + 1:star_list[5]]))
    star.Vx = int(float(line[star_list[5] + 1:star_list[6]]))
    star.Vy = int(float(line[star_list[6] + 1:]))


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
    planet_list = []
    for i in range(len(line)):
        if line[i] == ' ':
            planet_list.append(i)
    planet.R = int(float(line[planet_list[0] + 1:planet_list[1]]))
    planet.color = (line[planet_list[1] + 1:planet_list[2]])
    planet.m = int(float(line[planet_list[2] + 1:planet_list[3]]))
    planet.x = int(float(line[planet_list[3] + 1:planet_list[4]]))
    planet.y = int(float(line[planet_list[4] + 1:planet_list[5]]))
    planet.Vx = int(float(line[planet_list[5] + 1:planet_list[6]]))
    planet.Vy = int(float(line[planet_list[6] + 1:]))


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
            out_file.write(str(out_file) +
                  str(obj.type) +
                  str(obj.R) +
                  str(obj.color) +
                  str(obj.m) +
                  str(obj.x) +
                  str(obj.y) +
                  str(obj.Vx) +
                  str(obj.Vy) +  '\n')


# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл..


if __name__ == "__main__":
    print("This module is not for direct call!")
