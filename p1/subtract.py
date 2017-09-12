import random 

file = open('subtract_vector.txt', 'w')
file.write('''# Generates two random numbers between -2**31 and 2**31 - 1. Subtracts them and checks for overflow\n''')
file.write('A[32] B[32] Op[4] Sa[5] C[32] V')

for i in range(1000):
    r1 = random.randint(-2**31, 2**31-1)
    r2 = random.randint(-2**31, 2**31-1)
    Op = random.randint(6,7)
    Sa = 0
    C = r1 - r2
    V = 0
    if C >= 2**31:
        C = C - 2**32
        V = 1
    if C < -2**31:
        V = 1
        C = C + 2**32
    file.write('\n%s\t%s\t%s\t%s\t%s\t%s' %(r1, r2, Op, Sa, C, V))