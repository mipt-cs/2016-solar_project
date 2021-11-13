# coding: utf-8
# license: GPLv3
# without write_space_objects_data_to_file
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
                print('Yes')
                objects.append(star)
            elif object_type == "planet":  
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
                print('Yes yes')
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
    
    line = line.split(' ')
    star.R = int(line[1])
    star.color = line[2]           
    star.m = exp_to_alg(line[3])
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
    
    line = line.split(' ')
    planet.R = int(line[1])
    planet.color = line[2]
    #Переводит экспоненциальную запись числа в нормальную
            
    planet.m = exp_to_alg(line[3])
    planet.x = exp_to_alg(line[4])
    planet.y = float(line[5])
    planet.Vx = float(line[6])
    planet.Vy = exp_to_alg(line[7])


def exp_to_alg(s):
    s = s.rstrip()
    sum1 = ''
    i = 0
    a = s[i]
    while a != '.':
        sum1 += a
        i += 1
        a = s[i]
    sum1 = float(sum1)
    i += 1
    a = s[i]
    after_comma = -1
    while a != 'E':
        sum1 += float(a) * 10 ** after_comma
        after_comma -= 1
        i += 1
        a = s[i] 
    power = 0
    for l in range(i + 1, len(s), 1):
        power += int(s[l]) * 10 ** (len(s) - l - 1)
        
    return sum1 * 10 ** power   
    



def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star   <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Параметры:
    **output_filename** — имя входного файла
    **space_objects**   — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(out_file, "%s %d %s %f" % ('1', 2, '3', 4.5))
            # FIXME: should store real values

# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")