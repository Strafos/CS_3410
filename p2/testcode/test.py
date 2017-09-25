import random

f = open('generated_tests', 'w')

def int_32():
    return random.randint(-2**15, 2**15-1)

def int_32U():
    return random.randint(0, 2**16-1)

def rand_regis():
    r = random.randint(1, 4)
    regis = '$' + str(r)
    return regis

def rand_regisU():
    r = random.randint(4, 5)
    regis = '$' + str(r)
    return regis

def rand_regis_curr(i):
    r = random.randint(1, i)
    regis = '$' + str(r)
    return regis

def logical_immed():
    li = [
        'ANDI',
        'ORI',
        'XORI',
    ]
    return li[random.randint(0,2)]

def arith_immed():
    li = [
        # 'ADDIU',
        'SLTI',
        'SLTIU',
    ]
    return li[random.randint(0,1)]

def ADD_IU(i):
    word = 'ADDIU' + ' $' + str(i) + ', ' + '$zero, ' + str(int_32()) + '\n'
    f.write(word)

def logical_I(i):
    word = logical_immed() + ' $' + str(i) + ', ' + rand_regis() + ', ' + str(int_32U()) + '\n'
    f.write(word)

def arith_I(i):
    word = arith_immed() + ' $' + str(i) + ', ' + rand_regis() + ', ' + str(int_32()) + '\n'
    f.write(word)

def SLT_test(i):
    li = [
        'SLT',
        'SLTU',
    ]
    instru = li[random.randint(0,1)]
    word = instru + ' $' + str(i) + ', ' + rand_regis() + ', ' + rand_regis() + '\n'
    f.write(word)

def arith_U(i):
    li = [
        'ADDU',
        'SUBU',
    ]
    instru = li[random.randint(0,1)]
    word = instru + ' $' + str(i) + ', ' + rand_regis() + ', ' + rand_regis() + '\n'
    f.write(word)

def arith_U_hazard(i):
    li = [
        'ADDU',
        'SUBU',
    ]
    instru = li[random.randint(0,1)]
    # word = instru + ' $' + str(i) + ', $' + str(i-1) + ', $' + str(i-2) + '\n'
    word = instru + ' $' + str(5) + ', $' + str(5) + ', $' + str(random.randint(1,4)) + '\n'
    f.write(word)

def logical(i):
    li = [
        'AND',
        'OR',
        'XOR',
        'NOR',
    ]
    instru = li[random.randint(0,3)]
    # word = instru + ' $' + str(i) + ', ' + rand_regis() + ', ' + rand_regis() + '\n'
    # word = instru + ' $' + str(i) + ', $' + str(i-1) + ', $' + str(i-2) + '\n'
    word = instru + ' $' + str(5) + ', $' + str(5) + ', $' + str(random.randint(1,4)) + '\n'
    f.write(word)

def shift(i):
    li = [
        'SLL',
        'SRL',
        'SRA',
    ]
    instru = li[random.randint(0,2)]
    word = instru + ' $' + str(i) + ', ' + rand_regis() + ', ' + str(random.randint(0,15)) + '\n'
    # word = instru + ' $' + str(i) + ', $' + str(i-1) + ', $' + str(i-2) + '\n'
    # word = instru + ' $' + str(5) + ', $' + str(5) + ', $' + str(random.randint(1,4)) + '\n'
    f.write(word)

def LUI(i):
    word = 'LUI' + ' $' + str(i) + ', ' + str(int_32U()) + '\n'
    f.write(word)

def shift_var(i):
    li = [
        'SLLV',
        'SRLV',
        'SRAV',
    ]
    instru = li[random.randint(0,2)]
    word = instru + ' $' + str(i) + ', ' + rand_regis() + ', ' + rand_regis() + '\n'
    # word = instru + ' $' + str(i) + ', $' + str(i-1) + ', $' + str(i-2) + '\n'
    # word = instru + ' $' + str(5) + ', $' + str(5) + ', $' + str(random.randint(1,6)) + '\n'
    f.write(word)

def move(i):
    li = ['MOVN', 'MOVZ']
    instru = li[random.randint(0,1)]
    word = instru + ' $' + str(i) + ', ' + rand_regis() + ', ' + rand_regis() + '\n'
    f.write(word)

for i in range(1,32):
    ADD_IU(i)

load_store = [
    'LB',
    'LW',
    'LBU',
    'SB',
    'SW',
]
def divis4int():
    n = random.randint(0,5)
    return n*32

def memory():
    instru = load_store[random.randint(0,4)]
    word = instru + ' ' +  rand_regis_curr(31) + ', ' + str(divis4int()) + '(' + rand_regis_curr(31) + ')\n'
    f.write(word)

def jump():
    # for J and JAL
    # instru = jumps[random.randint(0,1)]
    # word = instru + ' ' + str(random.randint(0,2**16)*4) + '\n'
    
    # JR
    word = 'JR' + ' ' + rand_regis_curr(31) + '\n'
    f.write(word)
    # JALR
    word = 'JALR' + ' ' + rand_regis_curr(31) + ', ' + rand_regis_curr(31) + '\n'
    f.write(word)

# BEQ BNE BLEZ BGTZ BLTZ BGEZ
def branch():
    # BEQ/BNE
    # li = ['BEQ', 'BNE']
    # word = li[random.randint(0,1)] + ' ' +  rand_regis_curr(31) + ', ' + rand_regis_curr(31) + ', ' + str(divis4int()) + '\n'
    # f.write(word)
    # BLTZ/BGTZ/BLTZ/BGEZ
    others = ['BLTZ', 'BGTZ', 'BLTZ', 'BGEZ']
    word = others[random.randint(0,3)] + ' ' + rand_regis_curr(31) + ', ' + str(divis4int()) + '\n'
    f.write(word)

for i in range(100):
    # jump()
    branch()

# for i in range(7,32):
    # shift_var(i)
    # shift(i)
    # logical(i)
    # arith_U_hazard(i)
    # logical_I()
    # SLT_test(i)
    # arith_U_rand(i)
    # move(i)

# def ALL_RANDOM():
    # func_li = [shift_var, shift, logical, arith_U, logical_I, SLT_test, move, shift_var, LUI, arith_U]
#     for i in range(1000):
#         func = random.randint(0,9)
#         regis = random.randint(0,31)
#         func_li[func](regis)

# for i in range(0, 32):
#     move(i)
