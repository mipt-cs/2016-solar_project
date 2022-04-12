# coding: utf-8
# license: GPLv3

from solar_objects import SpaceObject


def read_float_quantity(number_str):
    """
    Функция, переводящее число в виде строки в тип float.
    Считывает степень и значащие цифры, затем компонует и возвращает полученное число с плавающей точкой
    :param number_str: строковое предстваление числа (ожидается нечто подобное:
                                                            1.9889200000000002e+30
                                                            2.0
                                                            3.302E23
                                                            2)
    :return: число типа float
    """
    chislo = ""
    stepen = ""
    stepen_flag = 0
    for i in range(len(number_str)):
        if not number_str[i] == "e" or number_str[i] == "E":
            if stepen_flag:
                stepen += number_str[i]
            else:
                chislo += number_str[i]
        else:
            stepen_flag = 1
    print(stepen, chislo)
    if stepen != "":
        return float(chislo) * (10 ** int(stepen))
    else:
        return float(chislo)


def read_space_objects_data_from_file(input_filename):
    """
    Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов добавляет их в массив объектов
    :param: input_filename: имя файла, в котором записаны параметры объектов
    :return: массив объектов с записанными в поля параметрами
    """
    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            obj = SpaceObject()
            parse_object_parameters(line, obj)
            objects.append(obj)
    return objects


def parse_object_parameters(parameters_line, target_obj):
    """Считывает данные о космическом объекте из строки и записывает их в поля объекта класса SpaceObject.
    Входная строка должна иметь слеюущий формат:
    <тип объекта> <радиус в пикселях> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4
    :param: parameters_line строка в котрой черезе пробел записаны параметры объекта
    :param: target_obj объект класса SpaceObject, в поля котрого будем записывать данные
    """
    line_quantities = parameters_line.split()
    (target_obj.type, target_obj.R, target_obj.color, target_obj.m, target_obj.x, target_obj.y, target_obj.Vx,
     target_obj.Vy) = (
        line_quantities[0], read_float_quantity(line_quantities[1]), line_quantities[2],
        read_float_quantity(line_quantities[3]),
        read_float_quantity(line_quantities[4]),
        read_float_quantity(line_quantities[5]), read_float_quantity(line_quantities[6]),
        read_float_quantity(line_quantities[7]))


def write_space_objects_data_to_file(output_filename, objects_array):
    """Сохраняет данные о космических объектах в файл.
    Строки будут иметь следующий формат:
    <тип объекта> <радиус в пикселях> <цвет> <масса> <x> <y> <Vx> <Vy>
    :param: output_filename — имя файла, в который будут записаны параметры
    :param: space_objects — список космических объектов
    """
    write_lines = []
    for obj in objects_array:
        write_lines += str(obj.type) + " " + str(obj.R) + " " + str(obj.color) + " " + str(obj.m) + " " + str(
            obj.x) + " " + str(obj.y) + " " + str(obj.Vx) + " " + str(obj.Vy) + "\n"
    with open(output_filename, 'w') as out_file:
        out_file.writelines(write_lines)


if __name__ == "__main__":
    print("This module is not for direct call!")
