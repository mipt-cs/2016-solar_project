# coding: utf-8
# license: GPLv3
import matplotlib.pyplot as plt
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
    with open(output_filename, 'w+') as out_file:
        for obj in space_objects:
            out_file.write(
                str(obj.type) + ' ' +
                str(obj.R) + ' ' +
                str(obj.color) + ' ' +
                str(obj.m) + ' ' +
                str(obj.x) + ' ' +
                str(obj.y) + ' ' +
                str(obj.Vx) + ' ' +
                str(obj.Vy) + '\n')


def statistic(stat_file, space_objects): # Должна срабатывать каждый тик физического времени
    """
    Функция, записывающая статистику для движения только одного спутника вокруг звезды
    Параметры:

    **stat_file** - файл со статистикой
    **space_objects** - список космических объектов

    В итоговом файле будет строка вида r t v
    где r - расстояние между звездой и спутником, t - время, v - полная скорость спутника
    """
    with open(stat_file, 'w+') as out_file:
        dx = space_objects[0].x-space_objects[1].x
        dy = space_objects[1].y-space_objects[1].y
        dr = (dx**2 + dy**2)**0.5
        v = (space_objects ** 2 + dy ** 2) ** 0.5
        # FIXME    t = нужно время в солнечной системе из main
        out_file.write(
            str(dr) + ' ' +
            # FIXME    str(t) + ' ' +
            str(v) + '\n')
    with open(stat_file, 'w+') as input_file:
        for line in input_file:
            list = []
            V = []
            R = []
            t = []
            for i in range(len(line)):
                if line[i] == ' ':
                    list.append(i)
            V.append(int(float(line[:list[0]])))
            t.append(int(float(line[list[0] + 1:list[1]])))
            R.append(int(float(line[list[1] + 1:list[2]])))
            plt.plot(t, V)
            plt.show()
            plt.plot(t, R)
            plt.show()
            plt.plot(R, V)
            plt.show()


if __name__ == "__main__":
    print("This module is not for direct call!")
