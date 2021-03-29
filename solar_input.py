# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet
from tkinter import messagebox


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
            else:
                print("Unknown space object")

            if object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def display_full_name():
    messagebox.showinfo(" Python",
                        radius.get() + " " + colour.get() + " " + weight.get() + " " + coord_x.get() + " " + coord_y.get() + " " + coord_vx.get() + " " + coord_vy.get())


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
    root = Tk()
    root.title(" Star")

    radius = StringVar()
    colour = StringVar()
    weight = StringVar()
    coord_x = StringVar()
    coord_y = StringVar()
    coord_vx = StringVar()
    coord_vy = StringVar()

    radius_label = Label(text="Введите радиус в пикселях:")
    colour_label = Label(text="Введите цвет:")
    weight_label = Label(text="Введите массу:")
    coord_x_label = Label(text="Введите координату по x:")
    coord_y_label = Label(text="Введите координату по y:")
    coord_vx_label = Label(text="Введите скорость по x:")
    coord_vy_label = Label(text="Введите скорость по y:")

    radius_label.grid(row=0, column=0, sticky="w")
    colour_label.grid(row=1, column=0, sticky="w")
    weight_label.grid(row=1, column=0, sticky="w")
    coord_x_label.grid(row=1, column=0, sticky="w")
    coord_y_label.grid(row=1, column=0, sticky="w")
    coord_vx_label.grid(row=1, column=0, sticky="w")
    coord_vy_label.grid(row=1, column=0, sticky="w")

    radius_entry = Entry(textvariable=radius)
    colour_entry = Entry(textvariable=colour)
    weight_entry = Entry(textvariable=weight)
    coord_x_entry = Entry(textvariable=coord_x)
    coord_y_entry = Entry(textvariable=coord_y)
    coord_vx_entry = Entry(textvariable=coord_vx)
    coord_vy_entry = Entry(textvariable=coord_vy)

    radius_entry.grid(row=0, column=1, padx=5, pady=5)
    colour_entry.grid(row=1, column=1, padx=5, pady=5)
    weight_entry.grid(row=1, column=1, padx=5, pady=5)
    coord_x_entry.grid(row=1, column=1, padx=5, pady=5)
    coord_y_entry.grid(row=1, column=1, padx=5, pady=5)
    coord_vx_entry.grid(row=1, column=1, padx=5, pady=5)
    coord_vy_entry.grid(row=1, column=1, padx=5, pady=5)

    message_button = Button(text="Click Me", command=display_full_name)
    message_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

    pass  # FIXME: not done yet


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
    root = Tk()
    root.title(" Planet ")

    radius = StringVar()
    colour = StringVar()
    weight = StringVar()
    coord_x = StringVar()
    coord_y = StringVar()
    coord_vx = StringVar()
    coord_vy = StringVar()

    radius_label = Label(text="Введите радиус в пикселях:")
    colour_label = Label(text="Введите цвет:")
    weight_label = Label(text="Введите массу:")
    coord_x_label = Label(text="Введите координату по x:")
    coord_y_label = Label(text="Введите координату по y:")
    coord_vx_label = Label(text="Введите скорость по x:")
    coord_vy_label = Label(text="Введите скорость по y:")

    radius_label.grid(row=0, column=0, sticky="w")
    colour_label.grid(row=1, column=0, sticky="w")
    weight_label.grid(row=1, column=0, sticky="w")
    coord_x_label.grid(row=1, column=0, sticky="w")
    coord_y_label.grid(row=1, column=0, sticky="w")
    coord_vx_label.grid(row=1, column=0, sticky="w")
    coord_vy_label.grid(row=1, column=0, sticky="w")

    radius_entry = Entry(textvariable=radius)
    colour_entry = Entry(textvariable=colour)
    weight_entry = Entry(textvariable=weight)
    coord_x_entry = Entry(textvariable=coord_x)
    coord_y_entry = Entry(textvariable=coord_y)
    coord_vx_entry = Entry(textvariable=coord_vx)
    coord_vy_entry = Entry(textvariable=coord_vy)

    radius_entry.grid(row=0, column=1, padx=5, pady=5)
    colour_entry.grid(row=1, column=1, padx=5, pady=5)
    weight_entry.grid(row=1, column=1, padx=5, pady=5)
    coord_x_entry.grid(row=1, column=1, padx=5, pady=5)
    coord_y_entry.grid(row=1, column=1, padx=5, pady=5)
    coord_vx_entry.grid(row=1, column=1, padx=5, pady=5)
    coord_vy_entry.grid(row=1, column=1, padx=5, pady=5)

    message_button = Button(text="Click Me", command=display_full_name)
    message_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")
    pass  # FIXME: not done yet...


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
