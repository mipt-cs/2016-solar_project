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
            elif object_type == "planet":
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
    data = line.split()
    star.R = int(data[1])
    star.color = data[2]
    star.m = float(data[3])
    star.x = float(data[4])
    star.y = float(data[5])
    star.Vx = float(data[6])
    star.Vy = float(data[7])
    star.type = 'star'


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
    data = line.split()
    planet.R = int(data[1])
    planet.color = data[2]
    planet.m = float(data[3])
    planet.x = float(data[4])
    planet.y = float(data[5])
    planet.Vx = float(data[6])
    planet.Vy = float(data[7])
    planet.type = 'planet'


def write_space_objects_data_to_file(output_filename, space_objects, time):
    """Сохраняет данные о космических объектах в файл.
    Предоставляет статистику.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    count = 0
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            if obj.type == "planet":
                print(f"{count} {time} {obj.type} {obj.x} {obj.y} {obj.vx} {obj.vy}", file=out_file)
                line = str(count) + " " + str(obj.get_distance_massive()) + " " + str(obj.get_v_massive()) + "\n"
                out_file.write(line)
            count += 1

if __name__ == "__main__":
    print("This module is not for direct call!")
