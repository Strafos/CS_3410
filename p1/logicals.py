import random 

file = open('logicals.txt', 'w')
file.write('''# Generates two random numbers between -2**31 and 2**31 - 1. Randomly generates one of eight comparison operators and assigns that value to C\n''')
file.write('A[32] B[32] Op[4] Sa[5] C[32] V')

for i in range(5000):
    r1 = random.randint(-2**31, 2**31-1)
    r2 = random.randint(-2**31, 2**31-1)
    Op = random.randint(0,7)
    Sa = 0
    if Op is 0:
        Op = 10
        C = r1 | r2
    elif Op is 1:
        Op = 8
        C = r1 & r2
    elif Op is 2:
        Op = 12
        C = r1 ^ r2
    elif Op is 3:
        Op = 14
        C = ~(r1 | r2)
    elif Op is 4:
        Op = 11
        C = r1 != r2
    elif Op is 5:
        Op = 9
        C = r1 == r2
    elif Op is 6:
        Op = 15
        C = r1 <= 0
    elif Op is 7:
        Op =13
        C = r1 > 0
    C = int(C)
    V = 0
    file.write('\n%s\t%s\t%s\t%s\t%s\t%s' %(r1, r2, Op, Sa, C, V))

# file.write('0\t0\t0\t0\t0\t0')