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
            elif object_type == "planet":
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
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    line = line.split()
    star.color = line[2]
    star.m, star.R = float(line[3]), float(line[1])
	star.x, star.y = float(line[4]), float(line[5])
	star.Vx, star.Vy = float(line[6]), float(line[7])  

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
    star.color = line[2]
    planet.m, planet.R = float(line[3]), float(line[1])
	planet.x, planet.y = float(line[4]), float(line[5])
	planet.Vx, planet.Vy = float(line[6]), float(line[7])


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
<<<<<<< Updated upstream
            print(out_file, "{0} {1} {2} {3} {4} {5} {6} {7}\n".format(obj.type.capitalize(), obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy))
            # FIXME: should store real values
=======
            param_list = [0, 0, 0, 0, 0, 0, 0, 0]
            param_list[0] = obj.type
            param_list[1] = str(round(obj.R, 2))
            param_list[2] = obj.color
            param_list[3] = str(round(obj.m, 2))
            param_list[4] = str(round(obj.x, 2))
            param_list[5] = str(round(obj.y, 2))
            param_list[6] = str(round(obj.Vx, 2))
            param_list[7] = str(round(obj.Vy, 2))
            parameters = ' '.join(param_list)
            print(out_file, parameters)
            out_file.write(parameters + "\n")
        out_file.close()
>>>>>>> Stashed changes

# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл.

if __name__ == "__main__":
    print("This module is not for direct call!")
