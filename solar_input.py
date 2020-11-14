# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet
masses_written = False

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
            if object_type == "star":  # FIXME: do the same for planet
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)          # done the same with planet
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
    line_list = line.split()

    star.R = float(line_list[1])
    star.color = line_list[2]
    star.m = float(line_list[3])
    star.x = float(line_list[4])
    star.y = float(line_list[5])
    star.Vx = float(line_list[6])
    star.Vy = float(line_list[7])
    # Probably fixed


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
    line_list = line.split()
    planet.R = float(line_list[1])
    planet.color = line_list[2]
    planet.m = float(line_list[3])
    planet.x = float(line_list[4])
    planet.y = float(line_list[5])
    planet.Vx = float(line_list[6])
    planet.Vy = float(line_list[7])
    # Probably fixed


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
            print(obj.type, obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy, file=out_file) # probably fixed
            # FIXME: should store real values

# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...


def delete_last_stats(output_filename):
    """Функция удаляет предыдущие значения, записанные в файл stats.txt"""
    with open(output_filename, 'w') as out_file:
        print('', file=out_file)


def write_stats_data_to_file(output_filename, space_objects, t):
    """ Функция сохраняет координаты, скорости и время. Строки имеют следующий формат:
    <x>, <y>, <Vx>, <Vy>, <time>"""
    global masses_written

    output_file = open(output_filename, 'r')
    file_list = output_file.readlines()

    for i in range(len(file_list)):
        file_list[i] = file_list[i].rstrip()
    output_file.close()
    for obj in space_objects:

        x = '{} '.format(obj.x)
        y = '{} '.format(obj.y)
        Vx = '{} '.format(obj.Vx)
        Vy = '{} '.format(obj.Vy)
        t = '{}'.format(t)
        line = x + y + Vx + Vy + t
        file_list.append(line)

    output_file = open(output_filename, 'w')
    if not masses_written:
        print(space_objects[0].m, space_objects[1].m, file=output_file)

        masses_written = True
    for line in file_list:
        print(line, file=output_file)
    output_file.close()


if __name__ == "__main__":
    print("This module is not for direct call!")
