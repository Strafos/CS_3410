import random 

file = open('vector.txt', 'w')
file.write('B[32] Sa[5] Cin C[32]')

for i in range(100000):
    r = random.randint(0, 2**31)
    s = random.randint(0, 2**5)
    c = r << s
    if c < 2**31:
        file.write('\n%s\t%s\t%s\t%s' %(r, s, 0, c))