import math
# import argparse
#
# parser = argparse.ArgumentParser(description='Paint graph of some functions')
# parser.add_argument()
x_min = -100
x_max = 100
y_min = -2
y_max = 2
half_height = 20
half_width = 50


def print_x_axis():
    print('-' * half_width + '|' + '-' * half_width + '>')
    x_axis = str(x_min)
    x_axis += ' ' * int((half_width - 10) / 2)
    x_axis += str(x_min / 2)
    x_axis += ' ' * int((half_width - 10) / 2)
    x_axis += '0|'
    x_axis += ' ' * int((half_width - 8) / 2)
    x_axis += str(x_max / 2)
    x_axis += ' ' * int((half_width - 8) / 2)
    x_axis += str(x_max)
    print(x_axis)


def get_values() -> dict:
    ret = dict()
    for i in range(1, 100, 10):
        value = int(math.log10(i) * 10) / 10
        if value in ret.keys():
            ret[value].append(i)
        else:
            ret[value] = [i]

    return ret

items = get_values()

print(' ' * half_width + '^')
for i in range(half_height):
    if i == (half_height / 2):
        str_to_print = ' ' * (half_width - 3) + str(y_max / 2) + '|'
    elif i == 0:
        str_to_print = ' ' * (half_width - 1) + str(y_max) + '|'
    else:
        str_to_print = ' ' * half_width + '|'

    for item in items:
        if (half_height - i - 1) * y_max / half_height < item:
            if (half_height - i) * y_max / half_height >= item:
                x_coord = int((sum(items[item]) / len(items[item])) / 2)
                str_to_print += ' ' * x_coord + '*'
    print(str_to_print)

print_x_axis()

# for i in range(half_height):
#     if i == (half_height / 2 - 1):
#         print(' ' * (half_width - 4) + str(y_min / 2) + '|')
#     elif i == half_height - 1:
#         print(' ' * (half_width - 2) + str(y_min) + '|')
#     else:
#         print(' ' * half_width + '|')



for item in items:
    print('{0}: {1}'.format(item, items[item]))


