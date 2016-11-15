# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""
G=gravitational_constant

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
        dx,dy=obj.x-body.x,obj.y-body.y
        r_sq=dx**2+dy**2
        r=r_sq**(0.5)
        force=gravitational_constant*body.m*obj.m/r_sq
        body.Fx +=force*dx/r
        body.Fy +=force*dy/r


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """
    print(body.Vx, body.Vy, body.x, body.y,  body.m)
    ax = body.Fx/body.m
    body.x +=(body.Vx*dt+ax*dt*dt/2)
    body.Vx += ax*dt
    ay = body.Fy/body.m
    body.y+=(body.Vy*dt+ay*dt*dt/2)
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

#FINAL VERSION#
