# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


space_objects = []


# Заменила функции parse_planet_parameters и parse_star_parameters на эту:
def parse_object_parameters(line):

    """Считывает данные о звезде или планете из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы или планеты, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4
    """
    type_, R, color, m, x, y, Vx, Vy = line.split(' ')
    type_ = type_.lower()

    if type_ == 'planet':
        obj = Planet()
    elif type_ == 'star':
        obj = Star()
    else:
        print('Invalid type of object.')
        raise ValueError

    obj.type_ = type_
    obj.R = float(R)
    obj.color = color
    obj.m = float(m)
    obj.y = float(y)
    obj.x = float(x)
    obj.Vy = float(Vy)
    obj.Vx = float(Vx)

    space_objects.append(obj)

    return obj


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
            out_file.write(' '.join([obj.type_, str(obj.R), obj.color, str(obj.m), str(obj.Fx), str(obj.Fy), str(obj.Vx), str(obj.Vy)]))


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
            object_type = line.split(' ')[0].lower()
            if object_type == 'star' or object_type == 'planet':
                obj = parse_object_parameters(line)
                objects.append(obj)

            else:
                print("Unknown space object")

    return objects
# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...
# D: Статистику чего?

if __name__ == "__main__":
    print("This module is not for direct call!")
