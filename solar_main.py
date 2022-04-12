# coding: utf-8
# license: GPLv3

import tkinter
from tkinter.filedialog import askopenfilename, asksaveasfilename
import solar_vis
import solar_model
import solar_input


class Quantities:
    def __init__(self):
        self.physical_time = 0
        self.displayed_time = 0
        self.time_step = 0
        self.time_speed = 0
        self.space = 0
        self.start_button = 0
        self.load_file_button = 0
        self.save_file_button = 0
        self.perform_execution = False
        self.space_objects = []


def execution(quantities_class, scale_factor_class):
    """
    Функция исполнения -- выполняется циклически, вызывая обработку всех небесных тел,
    а также обновляя их положение на экране.
    Цикличность выполнения зависит от значения глобальной переменной perform_execution.
    При perform_execution == True функция запрашивает вызов самой себя по таймеру через от 1 мс до 100 мс.

    :param quantities_class: класс, хранящий глобальные переменные
    :param scale_factor_class: класс, хранящий показатель масштабирования
    """
    quantities_class.space_objects = solar_model.recalculate_space_objects_positions(quantities_class.space_objects,
                                                                                     quantities_class.time_step.get())
    for body in quantities_class.space_objects:
        solar_vis.update_object_position(quantities_class.space, body, scale_factor_class)
    quantities_class.physical_time += quantities_class.time_step.get()
    quantities_class.displayed_time.set("%.1f" % quantities_class.physical_time + " seconds gone")

    print("execute")

    if quantities_class.perform_execution:
        quantities_class.space.after(101 - int(quantities_class.time_speed.get()),
                                     lambda: execution(quantities_class, scale_factor_class))


def start_execution(quantities_class, scale_factor_class):
    """
    Обработчик события нажатия на кнопку Start.
    Запускает циклическое исполнение функции execution.

    :param quantities_class: класс, хранящий глобальные переменные
    :param scale_factor_class: класс, хранящий показатель масштабирования
    """
    quantities_class.perform_execution = True
    quantities_class.start_button['text'] = "Pause"
    quantities_class.start_button['command'] = lambda: stop_execution(quantities_class, scale_factor_class)

    execution(quantities_class, scale_factor_class)
    print('Started execution...')


def stop_execution(quantities_class, scale_factor_class):
    """
    Обработчик события нажатия на кнопку Start.
    Останавливает циклическое исполнение функции execution.

    :param quantities_class: класс, хранящий глобальные переменные
    :param scale_factor_class: класс, хранящий показатель масштабирования
    """

    quantities_class.perform_execution = False
    quantities_class.start_button['text'] = "Start"
    quantities_class.start_button['command'] = lambda: start_execution(quantities_class, scale_factor_class)
    print('Paused execution.')


def open_file_dialog(quantities_class, scale_factor_class):
    """
    Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в глобальный список space_objects

    :param quantities_class: класс, хранящий глобальные переменные
    :param scale_factor_class: класс, хранящий показатель масштабирования
    """

    quantities_class.perform_execution = False
    for obj in quantities_class.space_objects:
        quantities_class.space.delete(obj.image)  # удаление старых изображений планет
    in_filename = askopenfilename(filetypes=(("Text file", ".txt"),))
    quantities_class.space_objects = solar_input.read_space_objects_data_from_file(in_filename)
    max_distance = max([max(abs(obj.x), abs(obj.y)) for obj in quantities_class.space_objects])
    solar_vis.calculate_scale_factor(max_distance, scale_factor_class)

    for obj in quantities_class.space_objects:
        if obj.type == 'star' or 'planet':
            solar_vis.create_image(quantities_class.space, obj, scale_factor_class)

        else:
            raise AssertionError()


def save_file_dialog(quantities_class):
    """
    Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в глобальный список space_objects

    :param quantities_class: класс, хранящий глобальные переменные
    """
    out_filename = asksaveasfilename(filetypes=(("Text file", ".txt"),))
    solar_input.write_space_objects_data_to_file(out_filename, quantities_class.space_objects)


def start_button(quantities_class, frame, scale_factor_class):
    """
    Отрисовка кнопки старт
    :param quantities_class: класс, хранящий глобальные переменные
    :param frame: кадр
    :param scale_factor_class: класс, хранящий показатель масштабирования
    """
    quantities_class.start_button = tkinter.Button(frame, text="Start",
                                                   command=lambda: start_execution(quantities_class,
                                                                                   scale_factor_class), width=6)
    quantities_class.start_button.pack(side=tkinter.LEFT)


def load_and_save_button(quantities_class, frame, scale_factor_class):
    """
    Отрисовка кнопок открыть и сохранить
    :param quantities_class: класс, хранящий глобальные переменные
    :param frame: кадр
    :param scale_factor_class: класс, хранящий показатель масштабирования
    """
    load_file_button = tkinter.Button(frame, text="Open file...",
                                      command=lambda: open_file_dialog(quantities_class, scale_factor_class))
    load_file_button.pack(side=tkinter.LEFT)
    save_file_button = tkinter.Button(frame, text="Save to file...",
                                      command=lambda: save_file_dialog(quantities_class))
    save_file_button.pack(side=tkinter.LEFT)


def time(quantities_class, frame):
    """
    Индикатор времени
    :param quantities_class: класс, хранящий глобальные переменные
    :param frame: кадр
    """
    quantities_class.displayed_time = tkinter.StringVar()
    quantities_class.displayed_time.set(str(quantities_class.physical_time) + " seconds gone")
    time_label = tkinter.Label(frame, textvariable=quantities_class.displayed_time, width=30)
    time_label.pack(side=tkinter.RIGHT)


def time_step(quantities_class, frame):
    """
    Настройка шага расчета
    :param quantities_class: класс, хранящий глобальные переменные
    :param frame: кадр
    :return:
    """
    quantities_class.time_step = tkinter.DoubleVar()
    quantities_class.time_step.set(1)
    time_step_entry = tkinter.Entry(frame, textvariable=quantities_class.time_step)
    time_step_entry.pack(side=tkinter.LEFT)


def set_quantities_class(root, frame, quantities_class, scale_factor_class):
    """
    Заполнение класса Quantities
    :param root: главное окно Tkinter
    :param frame: кадр
    :param quantities_class: класс, хранящий глобальные переменные
    :param scale_factor_class: класс, хранящий показатель масштабирования
    """
    start_button(quantities_class, frame, scale_factor_class)
    time(quantities_class, frame)
    time_step(quantities_class, frame)
    quantities_class.physical_time = 0
    quantities_class.space = tkinter.Canvas(root, width=solar_vis.WINDOW_WIDTH, height=solar_vis.WINDOW_HEIGHT,
                                            bg="black")
    quantities_class.space.pack(side=tkinter.TOP)
    quantities_class.time_speed = tkinter.DoubleVar()


def main(quantities_class, scale_factor_class):
    """
    Главная функция главного модуля.
    Создаёт объекты графического дизайна библиотеки tkinter: окно, холст, фрейм с кнопками, кнопки.

    :param quantities_class: класс, хранящий глобальные переменные
    :param scale_factor_class: класс, хранящий показатель масштабирования
    """

    print('Modelling started!')

    root = tkinter.Tk()

    frame = tkinter.Frame(root)
    frame.pack(side=tkinter.BOTTOM)

    set_quantities_class(root, frame, quantities_class, scale_factor_class)

    scale = tkinter.Scale(frame, variable=quantities_class.time_speed, orient=tkinter.HORIZONTAL)
    scale.pack(side=tkinter.LEFT)

    load_and_save_button(quantities_class, frame, scale_factor_class)

    root.mainloop()
    print('Modelling finished!')


if __name__ == "__main__":
    quantities = Quantities()
    scale_factor = solar_vis.ScaleFactor()
    main(quantities, scale_factor)
