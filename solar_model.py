# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""
vc=3*(10**8)

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
        r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
        body.Fx += (((obj.x - body.x)/r) * (gravitational_constant * obj.m * body.m))/(r**2)
        body.Fy += (((obj.y - body.y)/r) * (gravitational_constant * obj.m * body.m))/(r**2)

    #FIXED

def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """
    body.me=body.m*(1/(1+(((body.Vy**2+body.Vx**2)**(1/2))/vc)**(1/2)))
    ax = body.Fx/body.me
    body.x += body.Vx*dt
    body.Vx += ax*dt
    ay = body.Fy/body.me
    body.y += body.Vy*dt
    body.Vy += ay*dt
    body.me=body.m/(1+(((body.Vy**2+body.Vx**2)**(1/2))/vc)**(1/2))
    #FIXED


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