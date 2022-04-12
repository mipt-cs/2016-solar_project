# coding: utf-8
# license: GPLv3

"""Модуль визуализации.
Нигде, кроме этого модуля, не используются экранные координаты объектов.
Функции, создающие графические объекты и перемещающие их на экране, принимают физические координаты
"""

HEADER_FONT = "Arial-16"
"""Шрифт в заголовке"""

WINDOW_WIDTH = 800
"""Ширина окна"""

WINDOW_HEIGHT = 800
"""Высота окна"""


class ScaleFactor:
    """
    Показатель масштабирования
    """
    value = None


"""Масштабирование экранных координат по отношению к физическим.
Тип: float
Мера: количество пикселей на один метр."""


def calculate_scale_factor(max_distance, scale_factor_class):
    """
    Вычисляет значение глобальной переменной **scale_factor** по данной характерной длине
    :param max_distance: физический размер поля
    :param scale_factor_class: класс, хранящий показатель масштабирования
    """
    scale_factor_class.value = 0.4 * min(WINDOW_HEIGHT, WINDOW_WIDTH) / max_distance
    print('Scale factor:', scale_factor_class.value)


def scale_x(x, scale_factor_class):
    """
    Возвращает экранную **x** координату по **x** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **x** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.

    :param x: координата
    :param scale_factor_class: класс, хранящий показатель масштабирования
    """

    return int(x * scale_factor_class.value) + WINDOW_WIDTH // 2


def scale_y(y, scale_factor_class):
    """
    Возвращает экранную **y** координату по **y** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **y** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.
    Направление оси развёрнуто, чтобы у модели ось **y** смотрела вверх.

    :param y: y-координата модели
    :param scale_factor_class: класс, хранящий показатель масштабирования
    """

    return - int(y * scale_factor_class.value) + WINDOW_HEIGHT // 2


def create_image(space, body, scale_factor_class):
    """
    Создание отображаемого объекта звезды.

    :param space: холст для рисования
    :param body: звезда
    :param scale_factor_class: класс, хранящий показатель масштабирования
    """

    x = scale_x(body.x, scale_factor_class)
    y = scale_y(body.y, scale_factor_class)
    r = body.R
    body.image = space.create_oval([x - r, y - r], [x + r, y + r], fill=body.color)


def update_system_name(space, system_name):
    """
    Создаёт на холсте текст с названием системы небесных тел.
    Если текст уже был, обновляет его содержание.

    :param space: холст для рисования.
    :param system_name: — название системы тел.
    """
    space.create_text(30, 80, tag="header", text=system_name, font=HEADER_FONT)


def update_object_position(space, body, scale_factor_class):
    """
    Перемещает отображаемый объект на холсте.

    :param space: — холст для рисования.
    :param body: — тело, которое нужно переместить.
    :param scale_factor_class: класс, хранящий показатель масштабирования
    """
    x = scale_x(body.x, scale_factor_class)
    y = scale_y(body.y, scale_factor_class)
    r = body.R
    if x + r < 0 or x - r > WINDOW_WIDTH or y + r < 0 or y - r > WINDOW_HEIGHT:
        space.coords(body.image, WINDOW_WIDTH + r, WINDOW_HEIGHT + r,
                     WINDOW_WIDTH + 2 * r, WINDOW_HEIGHT + 2 * r)
    space.coords(body.image, x - r, y - r, x + r, y + r)


if __name__ == "__main__":
    print("This module is not for direct call!")
