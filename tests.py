from solar_input import *


class TestSolarInput:
    space_objects = []
    def test_parse_object_parameters():

        objects = [
            'Planet 5 green 5.974E24 149.60E9 0 0 29.76E3',
            # 'Star 30 red 1.98892E30 0 0 0 0',
            # 'foe negn prekk mkmktk mmop409 09'

            ]

        for i in objects:
            object_type = i.split()[0].lower()
            if object_type == 'planet':
                o = parse_object_parameters(i)
                assert o.type_ == 'planet'
                assert o.R == 5
                assert o.color == 'green'
                assert o.m == complex(5.974E24)

            elif object_type == 'star':
                o = parse_object_parameters(i)
                assert o.type_ == 'star'
                assert o.R == 30
                assert o.color == 'red'
                assert o.m == complex(1.98892E30)
            else:
                raise ValueError

            space_objects.append(o)

    def test_reader_and_writer():

        write_space_objects_data_to_file('test.txt', space_objects)

        output_obj = read_space_objects_data_from_file('test.txt')

        for i in range(len(space_objects)):
            assert space_objects[i].type_ == output_obj[i].type_
            assert space_objects[i].R == output_obj[i].R
            assert space_objects[i].color == output_obj[i].color
            assert space_objects[i].m == output_obj[i].m
