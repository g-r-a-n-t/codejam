import sys

lines = open(sys.argv[1]).read().splitlines()

n = int(lines.pop(0))
numbers = lines

def largest_tidy(number):
    fault = -1
    last = '0'
    for index, digit in enumerate(number):
        if int(digit) < int(last):
            fault = index - 1
            break

        last = digit

    if fault == -1:
        return number

    return number[:fault] + str(int(number[fault]) - 1) + (len(number) - fault) * '9'


for case, number in enumerate(numbers):
    print('Case #{}: {}'.format(case + 1, largest_tidy(number)))
