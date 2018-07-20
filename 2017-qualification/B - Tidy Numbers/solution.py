import sys

lines = open(sys.argv[1]).readlines()

n = int(lines.pop(0))
numbers = [int(line) for line in lines]

def is_tidy(number):
    last = 0
    for c in str(number):
        if last > int(c):
            return False

        last = int(c)

    return True

def largest_tidy(number):
    for curr in reversed(range(number + 1)):
        if is_tidy(curr):
            return curr


for case, number in enumerate(numbers):
    print('Case #{}: {}'.format(case + 1, largest_tidy(number)))
