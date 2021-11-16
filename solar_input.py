# coding: utf-8
# license: GPLv3
import matplotlib.pyplot as plt
import pylab
from matplotlib.ticker import (AutoMinorLocator)
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


def statistic(stat_file, space_objects, physical_time):  # Должна срабатывать каждый тик физического времени
    """
    Функция, записывающая статистику для движения только одного спутника вокруг звезды
    Параметры:

    **stat_file** - файл со статистикой
    **space_objects** - список космических объектов

    В итоговом файле будет строка вида r t v
    где r - расстояние между звездой и спутником, t - время, v - полная скорость спутника
    """
    with open(stat_file, 'a') as out_file:
        for obj in space_objects:
            if obj.type == 'planet':
                dx = space_objects[0].x - space_objects[1].x
                dy = space_objects[0].y - space_objects[1].y
                dr = (dx ** 2 + dy ** 2) ** 0.5
                v = (space_objects[1].Vx ** 2 + space_objects[1].Vy ** 2) ** 0.5
                t = physical_time
                print(' '.join(["{:.0f}".format(item) for item in [dr, v, t]]), file=out_file)


def draw_ticks(name_graph):
    """Рисует сетку на графике.
    Параметры:

    **name_graph** - название графика, на котором рисуется сетка.
    """
    name_graph.xaxis.set_minor_locator(AutoMinorLocator())
    name_graph.tick_params(which='both', width=2)
    name_graph.tick_params(which='major', length=5)
    name_graph.tick_params(which='minor', length=4, color='r')

    name_graph.grid(which='minor', alpha=0.2)
    name_graph.grid(which='major', alpha=0.5)


def graphics(stat_file):
    """Рисует 3 графика по данным, считанным из файла.
    Параметры:

    **stat_file** - файл со статистикой
    """
    fig = plt.figure(figsize=(12, 12))
    v_t = fig.add_subplot(2, 2, 1)  # будет рисовать два на два графика, этот под номером 1
    r_t = fig.add_subplot(2, 2, 2)  # будет рисовать два на два графика, этот под номером 1
    v_r = fig.add_subplot(2, 2, 3)
    v = []
    r = []
    t = []
    list = []
    with open(stat_file, 'r') as input_file:
        for line in input_file:
            for i in range(len(line)):
                if line[i] == ' ':
                    list.append(i)
            r.append(int(line.split(' ')[0]))
            v.append(int(line.split(' ')[1]))
            t.append(int(line.split(' ')[2]))

    draw_ticks(v_t)  # рисуем сетку на графиках
    draw_ticks(r_t)
    draw_ticks(v_r)

    plt.grid(True)

    # Две строки, два столбца. Текущая ячейка - 1
    pylab.subplot(2, 2, 1)
    pylab.plot(t, v, color='red')
    pylab.xlabel(r'$t, c$', fontsize=7)
    plt.ylabel(r'$V, м/с$', fontsize=7)
    pylab.title("Зависимость скорости планеты от времени V(t)", fontsize=7)

    # Две строки, два столбца. Текущая ячейка - 2
    pylab.subplot(2, 2, 2)
    pylab.plot(t, r, color='blue')
    pylab.xlabel(r'$t, c$', fontsize=7)
    plt.ylabel(r'$R, м$', fontsize=7)
    pylab.title("Зависимость расстояния между звездой и планетой от времени R(t)", fontsize=7)

    # Две строки, два столбца. Текущая ячейка - 3
    pylab.subplot(2, 2, 3)
    pylab.plot(r, v, color='green', label="Зависимость скорости планеты от расстояния до звезды V(R)")
    pylab.xlabel(r'$R, м$', fontsize=7)
    plt.ylabel(r'$V, м/с$', fontsize=7)
    pylab.title("Зависимость скорости планеты от расстояния до звезды V(R)", fontsize=7)

    plt.show()  # отрисовка графиков


if __name__ == "__main__":
    print("This module is not for direct call!")
