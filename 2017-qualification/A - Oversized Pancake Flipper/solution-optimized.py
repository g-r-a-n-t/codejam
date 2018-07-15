import sys

lines = open(sys.argv[1]).readlines()

nps = int(lines.pop(0))
sl = []
kl = []
for line in lines:
    splitline = line.split()
    sl.append(splitline[0])
    kl.append(int(splitline[1]))

def least_flips(s, k):
    flips = 0
    index = s.find('-')
    while index <= len(s) - k:
        if index == -1:
            return flips

        s = flip(s, k, index)
        flips += 1
        index = s.find('-')

    return 'IMPOSSIBLE'

def flip(s, k, n):
    if n > len(s) - k or n < 0:
        raise ValueError('Invalid flip ({}, {}, {})'.format(s, k, n))

    start = s[:n]
    middle = s[n:n+k]
    end = s[n+k:]

    new_middle = ''
    for c in middle:
        new_middle += opposite(c)

    return '{}{}{}'.format(start, new_middle, end)
    
def opposite(c):
    if c is '+':
        return '-'
    
    if c is '-':
        return '+'

    raise ValueError('Invalid pancake')

for n in range(nps):
    solution = least_flips(sl[n], kl[n])
    print('Case #{}: {}'.format(n + 1, solution))








