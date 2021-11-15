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
    par=line.split()
    star.R = float(par[1])
    star.color = par[2]
    star.m = float(par[3])
    star.x = float(par[4])
    star.y = float(par[5])
    star.Vx = float(par[6])
    star.Vy = float(par[7])


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
    par = line.split()
    planet.R = float(par[1])
    planet.color = par[2]
    planet.m = float(par[3])
    planet.x = float(par[4])
    planet.y = float(par[5])
    planet.Vx = float(par[6])
    planet.Vy = float(par[7])


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
            if obj.type == 'star':
                type = 'Star'
            elif obj.type == 'planet':
                type = 'Planet'
            else:
                type = 'Unknown'
            out_file.write(type + ' ' + str(obj.R) + ' ' + str(obj.color) + ' ' + str(obj.m) + ' ' +
                           str(obj.x) + ' ' + str(obj.y) + ' ' + str(obj.Vx) + ' ' + str(obj.Vy) + '\n')
            out_file.write('\n')


def write_obj_stats(physical_time, space_objects, first_time):
    """Сохраняет данные о спутнике в файл stats.txt
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **physical_time** — физическое прошедшее время
    **space_objects** — список объектов планет и звёзд
    **first_time** — флаг:
        1 — перезаписываем файл при первом обращении к нему,
        0 — добавляем новые строки при повторном обращении
    """
    if first_time:
        operation = 'w'
    else:
        operation = 'a'
    with open('stats.txt', operation) as out_file:
        V = str(int((space_objects[1].Vx ** 2 + space_objects[1].Vy ** 2) ** (1/2)))
        R = str(int(((space_objects[1].x - space_objects[0].x) ** 2 + (space_objects[1].y - space_objects[0].y) ** 2)**(1/2)))
        out_file.write(str(physical_time) + ' ' + V + ' ' + R + '\n')


def read_stats(stats = 'stats.txt'):
    """Читает данные о спутнике из файла stats.txt
        Строки должны иметь следующий формат:

        Параметры:

        **stats** — файл, из которого читать (по умолчанию "stats.txt")

        Вывод:

        [time, velocity, radius] — массив из 3-х массивов, в которых содержатся контрольные значения времени,
        модуля скорости и расстояния до притягивающего центра
    """
    time = []
    velocity = []
    radius = []
    with open(stats, 'r') as input_file:
        for line in input_file:
            time.append(float(line.split()[0]))
            velocity.append(float(line.split()[1]))
            radius.append(float(line.split()[2]))
    if len(time) > 1000:
        temp_time = []
        temp_velocity = []
        temp_radius = []
        n = 1000
        """Параметр n отвечает за количество контрольных точек для графика"""
        for i in range(n):
            temp_time.append(time[i * len(time) // n])
            temp_velocity.append(velocity[i * len(time) // n])
            temp_radius.append(radius[i * len(time) // n])
        time = temp_time
        velocity = temp_velocity
        radius = temp_radius
    return [time, velocity, radius]


if __name__ == "__main__":
    print("This module is not for direct call!")
