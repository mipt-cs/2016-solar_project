objects = []


def parse_star_parameters(line, star):
    star_list = []
    for i in range(len(line)):
        if line[i] == ' ':
            star_list.append(i)
    print(star_list)
    star.append(int(float(line[star_list[0] + 1:star_list[1]])))
    star.append((line[star_list[1] + 1:star_list[2]]))
    star.append(int(float(line[star_list[2] + 1:star_list[3]])))
    star.append(int(float(line[star_list[3] + 1:star_list[4]])))
    star.append(int(float(line[star_list[4] + 1:star_list[5]])))
    star.append(int(float(line[star_list[5] + 1:star_list[6]])))
    star.append(int(float(line[star_list[6] + 1:])))
    print(star)


def read_space_objects_data_from_file(input_filename):
    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            star = []
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                parse_star_parameters(line, star)
                objects.append(star)
            else:
                print("Unknown space object")

    return objects


#with open('double_star.txt') as input_file:
    #for line in input_file:
       #star_list = []
       #for i in range(len(line)):
        #if line[i] == ' ':
            #star_list.append(i)
    #width = int(line[star_list[0]+1:star_list[1]])

read_space_objects_data_from_file('double_star.txt')

print(objects)