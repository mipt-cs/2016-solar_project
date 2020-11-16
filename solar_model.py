# coding: utf-8
# license: GPLv3

import numpy as np

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def sum_of_squares(v):
    """ v1 * v1 + v2 * v2 ... + vn * vn"""
    # или return dot_product(v, v)
    return sum(vi ** 2 for vi in v)


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу
    **space_objects** — список объектов, которые воздействуют на тело
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой само на себя!
        vec = np.array([obj.x - body.x, obj.y - body.y])
        r = np.sqrt(sum_of_squares(vec))
        unit_vec = vec / r

        df = gravitational_constant * body.m * obj.m / r ** 2
        body.Fx += df * unit_vec[0]
        body.Fy += df * unit_vec[1]


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой

    Параметры:

    **body** — тело, которое нужно переместить
    """

    ax = body.Fx / body.m
    body.Vx += ax*dt
    body.x += body.Vx * dt

    ay = body.Fy / body.m
    body.Vy += ay*dt
    body.y += body.Vy * dt


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
