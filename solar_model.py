# coding: utf-8
# license: GPLv3

<<<<<<< HEAD
import math as m
=======
import math

>>>>>>> 5de08bfa36a735aabbda3fe161961a32df85695b
gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


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
        r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
<<<<<<< HEAD
        if body.y - obj.y == 0:
            a = m.pi / 2
        else:
            a = m.atan(body.x - obj.x / body.y - obj.y)
        body.Fx += gravitational_constant*body.m*obj.m * m.cos(a) / r**2  # FIXME: нужно вывести формулу...
        body.Fy += gravitational_constant*body.m*obj.m * m.sin(a)/ r**2 # FIXME: нужно вывести формулу...
=======
        if body.x == obj.x:
            angle = math.pi/2
        else:
            angle = math.atan((body.y - obj.y) / (body.x - obj.x))
        df = gravitational_constant * obj.m * body.m / r**2
        body.Fx += df * math.cos(angle)
        body.Fy += df * math.sin(angle)  # FIXME: нужно вывести формулу...
>>>>>>> 5de08bfa36a735aabbda3fe161961a32df85695b


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой

    Параметры:

    **body** — тело, которое нужно переместить
    """

<<<<<<< HEAD
    ax = -body.Fx / body.m
=======
    ax = body.Fx
>>>>>>> 5de08bfa36a735aabbda3fe161961a32df85695b
    body.Vx += ax*dt
    body.x += body.Vx * dt

    ay = -body.Fy / body.m
    body.Vy += ay*dt
    body.x += body.Vy * dt


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
