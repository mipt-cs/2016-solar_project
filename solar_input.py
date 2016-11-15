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
            if object_type == "star":  # FIXME: do the same for planet
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == 'planet':
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
    a=line.split(' ')
    print(a)
    star.R=int(a[1])
    star.color=a[2]
    star.m=float(a[3])
    star.x=float(a[4])
    star.y=float(a[5])
    star.Vx=float(a[6])
    star.Vy=float(a[7])
    print(star.R, star.m, star.x, star.y, star.Vx, star.Vy, star.color)
    return star

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
    a=line.split(' ')
    planet.R=float(a[1])
    planet.color=a[2]
    planet.m=float(a[3])
    planet.x=float(a[4])
    planet.y=float(a[5])
    planet.Vx=float(a[6])
    planet.Vy=float(a[7])
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
            out_file.write("%s %d %s %f %f %f %f %f" % (obj.type, obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy) + '\n')

def graph(objects, performance):
    import numpy as np
    import matplotlib.pyplot as plt
    objects = tuple(objects)

    y_pos = np.arange(len(objects))

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Value')
    plt.title('Bar title')

    plt.show()

if __name__ == "__main__":
    print("This module is not for direct call!")
