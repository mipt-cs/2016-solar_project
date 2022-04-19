# coding: utf-8
# license: GPLv3

import tkinter
import tkinter.filedialog as filedialog
import solar_vis as vis
import solar_model as model
import solar_input as inp

perform_execution = [False]
"""Флаг цикличности выполнения расчёта"""

space_objects = [[]]
"""Список космических объектов."""


def execution(perform, _physical_time, _displayed_time, _time_step, time_speed, space):
    """Функция исполнения -- выполняется циклически, вызывая обработку всех небесных тел,
    а также обновляя их положение на экране.
    Цикличность выполнения зависит от значения глобальной переменной perform_execution.
    При perform_execution == True функция запрашивает вызов самой себя по таймеру через от 1 мс до 100 мс.
    """
    model.recalculate_space_objects_positions(space_objects[0], _time_step.get())
    for body in space_objects[0]:
        vis.update_object_position(space, body)
    _physical_time[0] += _time_step.get()
    _displayed_time[0].set("%.1f" % _physical_time[0] + " seconds gone")
    if perform[0]:
        space.after(101 - int(time_speed.get()),
                    lambda: execution(perform, _physical_time, _displayed_time, _time_step, time_speed, space))


def start_execution(perform, button, _physical_time, _displayed_time, _time_step, time_speed, space):
    """Обработчик события нажатия на кнопку Start.
    Запускает циклическое исполнение функции execution.
    """

    perform[0] = True
    button['text'] = "Pause"
    button['command'] = lambda: stop_execution(perform, button, _physical_time, _displayed_time, _time_step, time_speed,
                                               space)

    execution(perform, _physical_time, _displayed_time, _time_step, time_speed, space)
    print('Started execution...')


def stop_execution(perform, button, _physical_time, _displayed_time, _time_step, time_speed, space):
    """Обработчик события нажатия на кнопку Start.
    Останавливает циклическое исполнение функции execution.
    """
    perform[0] = False
    button['text'] = "Start"
    button['command'] = lambda: start_execution(perform, button, _physical_time, _displayed_time, _time_step,
                                                time_speed,
                                                space)
    print('Paused execution.')


def open_file_dialog(perform, space, _space_objects):
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в глобальный список space_objects
    """
    perform[0] = False
    for obj in _space_objects[0]:
        space.delete(obj.image)  # удаление старых изображений планет
    in_filename = filedialog.askopenfilename(filetypes=(("Text file", ".txt"),))
    _space_objects[0] = inp.read_space_objects_data_from_file(in_filename)
    max_distance = max([max(abs(obj.x), abs(obj.y)) for obj in _space_objects[0]])
    vis.calculate_scale_factor(max_distance, vis.scale_factor)

    for obj in _space_objects[0]:
        if obj.type == 'star':
            vis.create_star_image(space, obj)
        elif obj.type == 'planet':
            vis.create_planet_image(space, obj)
        else:
            raise AssertionError()


def save_file_dialog():
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в глобальный список space_objects
    """
    out_filename = filedialog.asksaveasfilename(filetypes=(("Text file", ".txt"),))
    inp.write_space_objects_data_to_file(out_filename, space_objects[0])


def main():
    """Главная функция главного модуля.
    Создаёт объекты графического дизайна библиотеки tkinter: окно, холст, фрейм с кнопками, кнопки.
    """

    print('Modelling started!')
    physical_time = [0]
    """Физическое время от начала расчёта.
    Тип: float"""

    root = tkinter.Tk()
    # космическое пространство отображается на холсте типа Canvas
    space = tkinter.Canvas(root, width=vis.window_width, height=vis.window_height, bg="black")
    space.pack(side=tkinter.TOP)
    # нижняя панель с кнопками
    frame = tkinter.Frame(root)
    frame.pack(side=tkinter.BOTTOM)

    displayed_time = [tkinter.StringVar()]
    """Отображаемое на экране время.
    Тип: переменная tkinter"""

    displayed_time[0].set(str(physical_time[0]) + " seconds gone")
    time_label = tkinter.Label(frame, textvariable=displayed_time[0], width=30)
    time_label.pack(side=tkinter.RIGHT)

    time_step = tkinter.DoubleVar()
    """Шаг по времени при моделировании.
    Тип: float"""

    time_step.set(1)
    time_step_entry = tkinter.Entry(frame, textvariable=time_step)
    time_step_entry.pack(side=tkinter.LEFT)

    time_speed = tkinter.DoubleVar()
    scale = tkinter.Scale(frame, variable=time_speed, orient=tkinter.HORIZONTAL)
    scale.pack(side=tkinter.LEFT)

    start_button = tkinter.Button(frame, text="Start",
                                  command=lambda: start_execution(perform_execution, start_button, physical_time,
                                                                  displayed_time, time_step, time_speed, space),
                                  width=6)
    start_button.pack(side=tkinter.LEFT)

    load_file_button = tkinter.Button(frame, text="Open file...",
                                      command=lambda: open_file_dialog(perform_execution, space, space_objects))
    load_file_button.pack(side=tkinter.LEFT)
    save_file_button = tkinter.Button(frame, text="Save to file...", command=save_file_dialog)
    save_file_button.pack(side=tkinter.LEFT)

    root.mainloop()
    print('Modelling finished!')


if __name__ == "__main__":
    main()
