# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_float_quantity(number_str):
    if number_str.isdigit():
        return float(number_str)
    else:
        chislo = ""
        stepen = ""
        stepen_flag = 0
        for i in range(len(number_str)):
            if not number_str[i].isalpha():
                if stepen_flag:
                    stepen += number_str[i]
                else:
                    chislo += number_str[i]
            else: stepen_flag = 1
        print(stepen, chislo)
        return float(chislo) * (10 ** int(stepen))


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
    return objects


def parse_star_parameters(parameters_line, star_obj):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4
    """
    line_quantities = parameters_line.split()
    (star_obj.R, star_obj.color, star_obj.m, star_obj.x, star_obj.y, star_obj.Vx, star_obj.Vy) = (
        read_float_quantity(line_quantities[1]), line_quantities[2], read_float_quantity(line_quantities[3]),
        read_float_quantity(line_quantities[4]),
        read_float_quantity(line_quantities[5]), read_float_quantity(line_quantities[6]),
        read_float_quantity(line_quantities[7]))


def parse_planet_parameters(parameters_line, planet_obj):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4
    """
    line_quantities = parameters_line.split()
    (planet_obj.R, planet_obj.color, planet_obj.m, planet_obj.x, planet_obj.y, planet_obj.Vx, planet_obj.Vy) = (
        read_float_quantity(line_quantities[1]), line_quantities[2], read_float_quantity(line_quantities[3]),
        read_float_quantity(line_quantities[4]),
        read_float_quantity(line_quantities[5]), read_float_quantity(line_quantities[6]),
        read_float_quantity(line_quantities[7]))



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
            print(out_file, "%s %d %s %f" % ('1', 2, '3', 4.5))
            # FIXME: should store real values


# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")
