import math
# import argparse
#
# parser = argparse.ArgumentParser(description='Paint graph of some functions')
# parser.add_argument()
x_min = -100
x_max = 100
y_min = -100
y_max = 100
half_height = 10
half_width = 40

print(' ' * half_width + '^')
for i in range(half_height):
    if i == (half_height / 2):
        print(' ' * (half_width - 4) + str(y_max / 2) + '|')
    elif i == 0:
        print(' ' * (half_width - 3) + str(y_max) + '|')
    else:
        print(' ' * half_width + '|')
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
for i in range(half_height):
    if i == (half_height / 2 - 1):
        print(' ' * (half_width - 5) + str(y_min / 2) + '|')
    elif i == half_height - 1:
        print(' ' * (half_width - 4) + str(y_min) + '|')
    else:
        print(' ' * half_width + '|')


