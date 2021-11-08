# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """

    
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
        r = max(r, body.R+obj.R) 
        
        body.Fx += gravitational_constant*body.m*obj.m/(r**3)*(-body.x + obj.x)
        body.Fy += gravitational_constant*body.m*obj.m/(r**3)*(-body.y + obj.y)

    return body

def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """
    ax = body.Fx/body.m
    body.Vx += ax*dt
    body.x += body.Vx*dt
    ay = body.Fy/body.m
    body.Vy += ay*dt
    body.y += body.Vy*dt

    body.Fx = body.Fy = 0

    return body


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """

    for i in range(len(space_objects)):
        space_objects[i] = calculate_force(space_objects[i], space_objects)
    for i in range(len(space_objects)):
        space_objects[i] = move_space_object(space_objects[i], dt)

    return space_objects

    


if __name__ == "__main__":
    print("This module is not for direct call!")
