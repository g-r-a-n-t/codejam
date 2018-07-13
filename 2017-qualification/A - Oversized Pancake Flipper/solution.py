lines = open('small.in').readlines()

n = lines.pop(0)
sl = []
kl = []
for line in lines:
    splitline = line.split()
    sl.append(splitline[0])
    kl.append(splitline[1])

def least_flips(s, k):
    dists = {s:0}

def flip(s, k, i):
    if i > len(s) - k or i < 0:
        raise ValueError('Invalid flip')

    

def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

print(n)
print(sl)
print(kl)
