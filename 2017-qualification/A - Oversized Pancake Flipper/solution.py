lines = open('large.in').readlines()

nps = int(lines.pop(0))
sl = []
kl = []
for line in lines:
    splitline = line.split()
    sl.append(splitline[0])
    kl.append(int(splitline[1]))

def least_flips(s, k):
    final_dists = {}
    current_dists = [(s, 0)]
    while len(current_dists) is not 0:
        current = current_dists.pop(0)
        cs = current[0]       
        cd = current[1]       
        if cs in final_dists and cd < final_dists[cs]:
            final_dists[cs] = cd
        elif cs not in final_dists:
            final_dists[cs] = cd
            for n in range(len(cs) - k + 1):
                current_dists.append((flip(cs, k, n), cd + 1))
     
    solution = '+' * len(s)
    if solution not in final_dists:
        return 'IMPOSSIBLE'
    else:
        return final_dists[solution]

def flip(s, k, n):
    if n > len(s) - k or n < 0:
        raise ValueError('Invalid flip ({}, {}, {})'.format(s, k, n))
    
    fs = ''
    for i, c in enumerate(s):
        if i >= n and i < n + k:
            fs += opposite(c)
        else:
            fs += c

    return fs
    
def opposite(c):
    if c is '+':
        return '-'
    
    if c is '-':
        return '+'

    raise ValueError('Invalid pancake')

for n in range(nps):
    solution = least_flips(sl[n], kl[n])
    print('Case #{}: {}'.format(n + 1, solution))








