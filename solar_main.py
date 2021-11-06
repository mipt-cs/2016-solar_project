# coding: utf-8
# license: GPLv3

import tkinter
from tkinter import Button
from tkinter.filedialog import asksaveasfilename, askopenfilename

from solar_input import read_space_objects_data_from_file, write_space_objects_data_to_file
from solar_model import recalculate_space_objects_positions
from solar_vis import calculate_scale_factor, create_star_image, create_planet_image, \
    update_object_position, window_height, window_width


# def start():
#     """Главная функция главного модуля.
#     Создаёт объекты графического дизайна библиотеки tkinter: окно, холст, фрейм с кнопками, кнопки.
#     """
#
#     print('Modelling started!')
#     _physical_time = 0
#
#     root = tkinter.Tk()
#     # космическое пространство отображается на холсте типа Canvas
#     space = tkinter.Canvas(root, width=window_width, height=window_height, bg="black")
#     space.pack(side=tkinter.TOP)
#     # нижняя панель с кнопками
#     frame = tkinter.Frame(root)
#     frame.pack(side=tkinter.BOTTOM)
#
#     start_button = tkinter.Button(frame, text="Start", command=start_execution, width=6)
#     start_button.pack(side=tkinter.LEFT)
#
#     _time_step = tkinter.DoubleVar()
#     _time_step.set(1)
#     time_step_entry = tkinter.Entry(frame, textvariable=_time_step)
#     time_step_entry.pack(side=tkinter.LEFT)
#
#     _time_speed = tkinter.DoubleVar()
#     scale = tkinter.Scale(frame, variable=_time_speed, orient=tkinter.HORIZONTAL)
#     scale.pack(side=tkinter.LEFT)
#
#     load_file_button = tkinter.Button(frame, text="Open file...", command=open_file_dialog)
#     load_file_button.pack(side=tkinter.LEFT)
#     save_file_button = tkinter.Button(frame, text="Save to file...", command=save_file_dialog)
#     save_file_button.pack(side=tkinter.LEFT)
#
#     _displayed_time = tkinter.StringVar()
#     _displayed_time.set(str(_physical_time) + " seconds gone")
#     time_label = tkinter.Label(frame, textvariable=_displayed_time, width=30)
#     time_label.pack(side=tkinter.RIGHT)
#
#     return root, space, frame, start_button, _time_step, time_step_entry, _time_speed, scale, load_file_button, \
#            save_file_button, _displayed_time, time_label


class App:

    def __init__(self):
        print('Modelling started!')

        self.perform_execution = False
        """Флаг цикличности выполнения расчёта"""

        self.physical_time = 0
        """Физическое время от начала расчёта.
        Тип: float"""

        self.displayed_time = None
        """Отображаемое на экране время.
        Тип: переменная tkinter"""

        self.time_step = None
        """Шаг по времени при моделировании.
        Тип: float"""

        self.space_objects = []
        """Список космических объектов."""

        self.root = tkinter.Tk()
        # космическое пространство отображается на холсте типа Canvas
        self.space = tkinter.Canvas(self.root, width=window_width, height=window_height, bg="black")
        self.space.pack(side=tkinter.TOP)
        # нижняя панель с кнопками
        self.frame = tkinter.Frame(self.root)
        self.frame.pack(side=tkinter.BOTTOM)

        self.start_button = Button(self.frame, text="Start", command=self.start_execution, width=6)
        self.start_button.pack(side=tkinter.LEFT)

        self.time_step = tkinter.DoubleVar()
        self.time_step.set(1)
        self.time_step_entry = tkinter.Entry(self.frame, textvariable=self.time_step)
        self.time_step_entry.pack(side=tkinter.LEFT)

        self.time_speed = tkinter.DoubleVar()
        self.scale = tkinter.Scale(self.frame, variable=self.time_speed, orient=tkinter.HORIZONTAL)
        self.scale.pack(side=tkinter.LEFT)

        self.load_file_button = tkinter.Button(self.frame, text="Open file...", command=self.open_file_dialog)
        self.load_file_button.pack(side=tkinter.LEFT)
        self.save_file_button = tkinter.Button(self.frame, text="Save to file...", command=self.save_file_dialog)
        self.save_file_button.pack(side=tkinter.LEFT)

        self.displayed_time = tkinter.StringVar()
        self.displayed_time.set(str(self.physical_time) + " seconds gone")
        self.time_label = tkinter.Label(self.frame, textvariable=self.displayed_time, width=30)
        self.time_label.pack(side=tkinter.RIGHT)

    def main(self):
        self.root.mainloop()
        print('Modelling finished!')

    def save_file_dialog(self):
        """Открывает диалоговое окно выбора имени файла и вызывает
        функцию считывания параметров системы небесных тел из данного файла.
        Считанные объекты сохраняются в глобальный список space_objects
        """
        out_filename = asksaveasfilename(filetypes=(("Text file", ".txt"),))
        write_space_objects_data_to_file(out_filename, self.space_objects)

    def open_file_dialog(self):
        """Открывает диалоговое окно выбора имени файла и вызывает
        функцию считывания параметров системы небесных тел из данного файла.
        Считанные объекты сохраняются в глобальный список space_objects
        """
        self.perform_execution = False
        for obj in self.space_objects:
            self.space.delete(obj.image)  # удаление старых изображений планет
        in_filename = askopenfilename(filetypes=(("Text file", ".txt"),))
        self.space_objects = read_space_objects_data_from_file(in_filename)
        max_distance = max([max(abs(obj.x), abs(obj.y)) for obj in self.space_objects])
        calculate_scale_factor(max_distance)

        for obj in self.space_objects:
            if obj.type == 'star':
                create_star_image(self.space, obj)
            elif obj.type == 'planet':
                create_planet_image(self.space, obj)
            else:
                raise AssertionError()

    def stop_execution(self):
        """Обработчик события нажатия на кнопку Start.
        Останавливает циклическое исполнение функции execution.
        """
        self.perform_execution = False
        self.start_button['text'] = "Start"
        self.start_button['command'] = self.start_execution
        print('Paused execution.')

    def start_execution(self):
        """Обработчик события нажатия на кнопку Start.
        Запускает циклическое исполнение функции execution.
        """
        self.perform_execution = True
        self.start_button['text'] = "Pause"
        self.start_button['command'] = self.stop_execution

        self.execution()
        print('Started execution...')

    def execution(self):
        """Функция исполнения -- выполняется циклически, вызывая обработку всех небесных тел,
        а также обновляя их положение на экране.
        Цикличность выполнения зависит от значения глобальной переменной perform_execution.
        При perform_execution == True функция запрашивает вызов самой себя по таймеру через от 1 мс до 100 мс.
        """
        recalculate_space_objects_positions(self.space_objects, self.time_step.get())
        for body in self.space_objects:
            update_object_position(self.space, body)
        self.physical_time += self.time_step.get()
        self.displayed_time.set("%.1f" % self.physical_time + " seconds gone")

        if self.perform_execution:
            self.space.after(101 - int(self.time_speed.get()), self.execution)


if __name__ == "__main__":
    app = App()
    app.main()
