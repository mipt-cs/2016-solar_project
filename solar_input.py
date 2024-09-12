# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def translate_number_to_line_with_e(x):
    """Преобразует заданное число в строку с символом Е.

    Параметры:

    **x** — число, которое необходимо трансформировать в строку.
    """

    log = 0
    while x > 10:
        x = x / 10
        log = log + 1
    x = str(x)
    if len(x) > 4:
        x = x[0] + x[1] + x[2] + x[3] + x[4] + 'E' + str(log)
    else:
        x = x + 'E' + str(log)
    return x


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
                parse_star_parameters(line, planet)
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
    Planet 10 red 1E3 1E0 2E0 3E0 4E0
    Здесь число после Е обозначает спорядок величины

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """

    star.R = int(line.split()[1])
    star.color = line.split()[2]
    m = line.split()[3]
    star.m = float(m.split('E')[0]) * 10 ** int(m.split('E')[1])
    x = line.split()[4]
    star.x = float(x.split('E')[0]) * 10 ** int(x.split('E')[1])
    y = line.split()[5]
    star.y = float(y.split('E')[0]) * 10 ** int(y.split('E')[1])
    Vx = line.split()[6]
    star.Vx = float(Vx.split('E')[0]) * 10 ** int(Vx.split('E')[1])
    Vy = line.split()[7]
    star.Vy = float(Vy.split('E')[0]) * 10 ** int(Vy.split('E')[1])


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1E3 1E0 2E0 3E0 4E0
    Здесь число после Е обозначает спорядок величины

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """

    planet.R = int(line.split()[1])
    planet.color = line.split()[2]
    m = line.split()[3]
    planet.m = float(m.split('E')[0]) * 10 ** int(m.split('E')[1])
    x = line.split()[4]
    planet.x = float(x.split('E')[0]) * 10 ** int(x.split('E')[1])
    y = line.split()[5]
    planet.y = float(y.split('E')[0]) * 10 ** int(y.split('E')[1])
    Vx = line.split()[6]
    planet.Vx = float(Vx.split('E')[0]) * 10 ** int(Vx.split('E')[1])
    Vy = line.split()[7]
    planet.Vy = float(Vy.split('E')[0]) * 10 ** int(Vy.split('E')[1])


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
            m = translate_number_to_line_with_e(obj.m)
            x = translate_number_to_line_with_e(obj.x)
            y = translate_number_to_line_with_e(obj.y)
            Vx = translate_number_to_line_with_e(obj.Vx)
            Vy = translate_number_to_line_with_e(obj.Vy)
            print(obj.type, obj.R, obj.color, m, x, y, Vx, Vy, file=out_file)


if __name__ == "__main__":
    print("This module is not for direct call!")
