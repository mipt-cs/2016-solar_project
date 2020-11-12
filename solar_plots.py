import matplotlib.pyplot as plt
import numpy as np
from solar_model import gravitational_constant


def isfloat(value):
    '''Check, is the value float or not.

    Parameters:

    **value** — checking value.

    Returns:

    ***boolean*** - result of inspection.
    '''
    try:
        float(value)
        return True
    except ValueError:
        return False


def read_data(file_name):
    '''Read data from file.

    Parameters:

    ***file_name*** - name of reading file.

    Returns:

    ***masses*** - list of floats - star and satellite masses correspondingly.
    ***x, y*** - float - coordinates of satellite in X and Y directions.
    ***vx, vy*** - float - velocities of satellite along X and Y directions.
    ***time*** - float - time from simulation start.
    '''

    data = []
    with open(file_name) as file:
        for line in file:
            data += line.rstrip().split()

    data = ([float(each) if isfloat(each) or each[0] == '-' and isfloat(each[1:])
             else each for each in data])

    masses = data[0:2]
    x = y = vx = vy = time = []
    if len(data) > 2:
        x = np.array(data[2::5])
        y = np.array(data[3::5])
        vx = np.array(data[4::5])
        vy = np.array(data[5::5])
        time = np.array(data[6::5])

    return masses, x, y, vx, vy, time


def draw_and_save_plots():
    '''Draw and save plots of:
        - velocity-time,
        - distance to star-time,
        - velocity-distance to star,
        - energy-time dependencies.
    '''
    masses, x, y, vx, vy, time = read_data('stats.txt')

    distance = (x ** 2 + y ** 2) ** 0.5
    velocity = (vx ** 2 + vy ** 2) ** 0.5
    energy = (velocity**2 * masses[1] / 2
         - gravitational_constant * masses[0] * masses[1] / distance**2)

    plt.figure(figsize=(8, 12))

    plt.subplot(2, 2, 1)

    plt.title(r'Рис. 1. График $|v|(t)$', fontsize=10)

    plt.xlabel(r'$t, с$')
    plt.ylabel(r'$|v|, \frac{м}{с}$')
    plt.autoscale(tight=False)

    plt.minorticks_on()
    plt.grid(which='major', color='k', linewidth=1)
    plt.grid(which='minor', color='k', linestyle=':')
    plt.plot(time, velocity, color='b')

    plt.subplot(2, 2, 2)

    plt.title(r'Рис. 2. График $|r|(t)$', fontsize=10)

    plt.xlabel(r'$t, с$')
    plt.ylabel(r'$|r|, м$')
    plt.autoscale(tight=False)

    plt.minorticks_on()
    plt.grid(which='major', color='k', linewidth=1)
    plt.grid(which='minor', color='k', linestyle=':')

    plt.plot(time, distance, color='b')

    plt.subplots_adjust(wspace=0.5, hspace=0.5)

    plt.subplot(2, 2, 3)

    plt.title(r'Рис. 3. График $|v|(|r|)$', fontsize=10)

    plt.xlabel(r'$|v|, \frac{м}{с}$')
    plt.ylabel(r'$|r|, м$')
    plt.autoscale(tight=False)

    plt.minorticks_on()
    plt.grid(which='major', color='k', linewidth=1)
    plt.grid(which='minor', color='k', linestyle=':')

    plt.plot(velocity, distance, color='b')

    plt.subplot(2, 2, 4)

    plt.title(r'Рис. 4. График $E(t)$', fontsize=10)

    plt.xlabel(r'$t, с$')
    plt.ylabel(r'$E, Дж$')
    plt.autoscale(tight=False)

    plt.minorticks_on()
    plt.grid(which='major', color='k', linewidth=1)
    plt.grid(which='minor', color='k', linestyle=':')

    plt.plot(time, energy, color='b')

    plt.subplots_adjust(wspace=0.5, hspace=0.5)

    plt.savefig('plot.png', dpi=300)


if __name__ == "__main__":
    print("This module is not for direct call!")