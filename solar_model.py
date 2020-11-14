# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects, dt):
    """Вычисляет силу, действующую на тело.

    Параметры:

    ***body*** — тело, для которого нужно вычислить дейстующую силу.
    ***space_objects*** — список объектов, которые воздействуют на тело.
    ***dt*** - шаг времени.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        body_x_future = body.x + body.Vx * dt
        body_y_future = body.y + body.Vy * dt

        obj_x_future = obj.x + obj.Vx * dt
        obj_y_future = obj.y + obj.Vy * dt

        r_current = ((body.x - obj.x) ** 2 +
                     (body.y - obj.y) ** 2) ** 0.5
        r_future = ((body_x_future - obj_x_future) ** 2 +
                    (body_y_future - obj_y_future) ** 2) ** 0.5

        force_x_current_point = - (gravitational_constant * body.m * obj.m *
                                 (body.x - obj.x) / r_current ** 3)
        force_x_future_point = - (gravitational_constant * body.m * obj.m *
                                  (body_x_future - obj_x_future) / r_future ** 3)
        body.Fx += (force_x_current_point + force_x_future_point) / 2
        # DONE: FIXME: нужно вывести формулу...
        force_y_current_point = - (gravitational_constant * body.m * obj.m *
                                   (body.y - obj.y) / r_current ** 3)
        force_y_future_point = - (gravitational_constant * body.m * obj.m *
                                  (body_y_future - obj_y_future) / r_future ** 3)
        body.Fy += (force_y_current_point + force_y_future_point) / 2
        # DONE: FIXME: нужно вывести формулу...


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx / body.m
    ay = body.Fy / body.m
    body.x += body.Vx * dt + ax * dt**2 / 2
    body.y += body.Vy * dt + ay * dt ** 2 / 2
    # DONE: FIXME: не понимаю как менять...
    body.Vx += ax * dt
    body.Vy += ay * dt
    # DONE: FIXME: not done recalculation of y coordinate!


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects, dt)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")