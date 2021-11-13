# coding: utf-8
# license: GPLv3
# done
gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.
    Параметры:
    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.ax = body.ay = 0
    for obj in space_objects:
        if body != obj:
        #    continue  # тело не действует гравитационной силой на само себя!
            r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
            body.ax += -(body.x - obj.x)*gravitational_constant*obj.m/(r**3)
            body.ay += -(body.y - obj.y)*gravitational_constant*obj.m/(r**3)
            

def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.
    Параметры:
    **body** — тело, которое нужно переместить.
    """

    body.x += body.Vx*dt  
    body.Vx += body.ax*dt
    body.y += body.Vy*dt  
    body.Vy += body.ay*dt

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