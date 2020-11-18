from solar_objects import Star, Planet
import matplotlib.pyplot as plt
import numpy as np


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

    line = line.split()
    star.R = float(line[1])
    star.color = line[2]
    star.m = float(line[3])
    star.x = float(line[4])
    star.y = float(line[5])
    star.Vx = float(line[6])
    star.Vy = float(line[7])


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
    line = line.split()
    planet.R = float(line[1])
    planet.color = line[2]
    planet.m = float(line[3])
    planet.x = float(line[4])
    planet.y = float(line[5])
    planet.Vx = float(line[6])
    planet.Vy = float(line[7])


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
        output = []
        for obj in space_objects:
            planet = [str(obj.type), str(obj.R), str(obj.color), str(obj.m), str(obj.x), str(obj.y), str(obj.Vx),
                      str(obj.Vy)]
            planet = ' '.join(planet)
            planet = planet + '\n'
            output.append(planet)
        output = ''.join(output)
        out_file.write(output)


def data(space_objects, dt):
    with open('data.txt', 'a') as file:
        output_data = []
        for body in space_objects:
            for obj in space_objects:
                if body == obj or obj.type == 'star':
                    continue
                planet_data = [str((obj.Vx ** 2 + obj.Vy ** 2) ** (1 / 2)),
                               str(((body.x - obj.x) ** 2 + (body.y - obj.y) ** 2) ** 0.5), str(dt)]
                planet_data = ' '.join(planet_data)
                planet_data = planet_data + '\n'
                output_data.append(planet_data)
        output_data = ''.join(output_data)
        file.write(output_data)


def graph():
    input_data = []
    speed = []
    distance = []
    time = []
    with open('data.txt', 'r') as file:
        for line in file:
            input_data.append(line.split())
    for i in range(len(input_data)):
        speed.append(np.log(int(float(input_data[i][0]))) / np.log(10))
        distance.append(np.log(int(float(input_data[i][1]))) / np.log(10))
        time.append(np.log(int(float(input_data[i][2]))) / np.log(10))
    plt.subplot(221)
    plt.plot(time, speed)
    plt.xlabel(r'$log_{10} t$')
    plt.ylabel(r'$log_{10} Vx$')
    plt.title('Модуль скорости от времени')
    plt.subplot(222)
    plt.plot(time, distance)
    plt.xlabel(r'$log_{10} t$')
    plt.ylabel(r'$log_{10} S$')
    plt.title('Расстояние от времени')
    plt.subplot(223)
    plt.plot(distance, speed)
    plt.xlabel(r'$log_{10} S$')
    plt.ylabel(r'$log_{10} Vx$')
    plt.title('Модуль скорости от расстояния')
    plt.subplots_adjust(hspace=0.552, wspace=0.574, top=0.952)
    plt.savefig('graph.png')
    plt.show()
    file = open('data.txt', 'w')
    file.close()


if __name__ == "__main__":
    print("This module is not for direct call!")
