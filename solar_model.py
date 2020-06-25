# coding: utf-8
# license: GPLv3

from math import hypot

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""

def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!

        dx = body.x - obj.x
        dy = body.y - obj.y

        r = hypot(dy, dx)
        # print(r)
        F = -gravitational_constant*(body.m * obj.m) / (r**2)

        body.Fx = F * dx/r
        body.Fy = F * dy/r


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """
    delta = 0.01
    ax = body.Fx/body.m
    body.x += dt*body.Vx
    body.Vx += ax*dt

    ay = body.Fy/body.m
    body.y += dt*body.Vy
    body.Vy += ay*dt


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
