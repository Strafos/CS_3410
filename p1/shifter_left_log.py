import random 

file = open('shifter_vector.txt', 'w')
file.write('''# Generates two random numbers between -2**31 and 2**31 - 1. Shifts the second number by Sa units to the left\n''')
file.write('A[32] B[32] Op[4] Sa[5] C[32] V')

for i in range(1000):
    r1 = random.randint(-2**31, 2**31-1)
    r2 = random.randint(-2**31, 2**31-1)
    Op = random.randint(0,1)
    Sa = random.randint(0,31)
    C = r2 << Sa
    if C > 2**31 or C < -2**31:
        C = int(((C/2**32) % 1) * 2**32)
    V = 0
    file.write('\n%s\t%s\t%s\t%s\t%s\t%s' %(r1, r2, Op, Sa, C, V))

# file.write('0\t0\t0\t0\t0\t0')