import math
# import argparse
#
# parser = argparse.ArgumentParser(description='Paint graph of some functions')
# parser.add_argument()

half_height = 10
half_width = 40

print(' ' * half_width + '^')
for i in range(half_height):
    print(' ' * half_width + '|')
print('-' * half_width + '|' + '-' * half_width + '>')
print(' ' * (half_width - 1) + '0|')
for i in range(half_height):
    print(' ' * half_width + '|')


