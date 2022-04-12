# coding: utf-8
# license: GPLv3

GRAVITATIONAL_CONSTANT = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """
    Вычисляет силу, действующую на тело.

    :param body: тело, для которого нужно вычислить действующую силу.
    :param space_objects: список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        r = ((body.x - obj.x) ** 2 + (body.y - obj.y) ** 2) ** 0.5
        body.Fx += GRAVITATIONAL_CONSTANT * body.m * obj.m / r ** 3 * (- (body.x - obj.x))
        body.Fy += GRAVITATIONAL_CONSTANT * body.m * obj.m / r ** 3 * (- (body.y - obj.y))


def move_space_object(body, dt):
    """
    Перемещает тело в соответствии с действующей на него силой.

    :param body: тело, которое нужно переместить.
    :param dt: шаг по времени
    """

    ax = body.Fx / body.m
    body.Vx += ax * dt
    body.x += body.Vx * dt

    ay = body.Fy / body.m
    body.Vy += ay * dt
    body.y += body.Vy * dt


def recalculate_space_objects_positions(space_objects, dt):
    """
    Пересчитывает координаты объектов.

    :param space_objects: список объектов, для которых нужно пересчитать координаты.
    :param dt: шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
        move_space_object(body, dt)

    return space_objects


if __name__ == "__main__":
    print("This module is not for direct call!")
