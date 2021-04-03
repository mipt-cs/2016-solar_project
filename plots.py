import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as mpatches


def get_points(filename):
    """
    Считываю данные из файлика в массив и возвращю его
    """
    list_of_velocity = []
    list_of_distance = []

    list_of_strings = []
    list_of_data = []

    with open(filename, 'r') as in_file:
        list_of_strings = in_file.read().splitlines()

    for string in list_of_strings:
        list_of_data.append(string.split(" "))

    for lists in list_of_data:
        print(lists)
        if lists[0] == "Planet":
            list_of_distance.append(math.sqrt(float(lists[4])**2 + float(lists[5])**2))
            list_of_velocity.append(math.sqrt(float(lists[6])**2 + float(lists[7])**2))

    print (list_of_velocity, list_of_distance)


def build_plot(tup_data, color, name):
    plt.plot(tup_data[0], tup_data[1], '-', label='stl', color=color)
    return mpatches.Patch(color=color, label=name)


'''

size_v, time_v = get_points('size_access_stl.txt', 'access_stl.txt', 1)
#size_v_foreach, time_v_foreach = get_points('size_for_erase_my.txt', 'erase_my.txt', 1)

size_fl, time_fl = get_points('size_for_walk_on_f_list.txt', 'walk_on_f_list.txt', 1)
size_l, time_l = get_points('size_for_walk_on_list.txt', 'walk_on_list.txt', 1)
size_set, time_set = get_points('size_for_walk_on_set.txt', 'walk_on_set.txt', 1)
size_map, time_map = get_points('size_for_walk_on_map.txt', 'walk_on_map.txt', 1)


fig = plt.figure()

vector = build_plot((size_v, time_v), 'red', 'My vector')


f_list = build((size_fl, time_fl), 'blue', 'Forward list')
list = build((size_l, time_l), 'orange', 'List')
set = build((size_set, time_set), 'green', 'Set')
map = build((size_map, time_map), 'black', 'Map')


plt.grid()
plt.title('STL vector')
plt.xlabel('Size')
plt.ylabel('Time of access')
#plt.legend(handles=[vector, foreach])

plt.show()
fig.savefig('access_stl_norm.png')
'''
get_points("test_file.txt")
