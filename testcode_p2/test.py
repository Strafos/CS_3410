import random

INSTRUCTION = [
    # 'ADDIU',
    # 'ANDI',
    # 'ORI',
    # 'XORI',
    'SLTI',
    'SLTIU',
    'ADDU',
    'SUBU',
    'AND',
    'OR',
    'XOR',
    'NOR',
    # 'SLT',
    'SLTU',
    # 'MOVN',
    # 'MOVZ',
    'SLL',
    'SRL',
    'SRA',
    # 'SLLV',
    # 'SRLV',
    # 'SRAV',
    # 'LUI',
]

def get_instru():
    return INSTRUCTION[random.randint(0,len(INSTRUCTION)-1)]

def int_32():
    return random.randint(-2**15, 2**15-1)

def int_32U():
    return random.randint(0, 2**16-1)

def rand_regis():
    r = random.randint(1, 3)
    regis = '$' + str(r)
    return regis

def rand_regisU():
    r = random.randint(4, 5)
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

f = open('generated_tests', 'w')


def ADD_IU(i):
    word = 'ADDIU' + ' $' + str(i) + ', ' + rand_regis() + ', ' + str(int_32()) + '\n'
    f.write(word)

def logical_I(i):
    word = logical_immed() + ' $' + str(i) + ', ' + rand_regis() + ', ' + str(int_32U()) + '\n'
    f.write(word)

def arith_I(i):
    word = arith_immed() + ' $' + str(i) + ', ' + rand_regis() + ', ' + str(int_32()) + '\n'
    f.write(word)

for i in range(1,5):
    ADD_IU(i)

for i in range(5,31):
    # logical_I()
    arith_I(i)

# for i in range(6, 32):
#     instr = get_instru()
#     if 'I' in instr and instr != 'LUI':
#         word = instr + ' $' + str(i) + ', ' + rand_regis() + ', ' + str(int_32U()) + '\n'
#         f.write(word)
#     elif 'U' in instr and instr != 'LUI':
#         word = instr + ' $' + str(i) + ', ' + rand_regis() + ', ' + rand_regisU() + '\n'
#         f.write(word)
#     elif ('SR' in instr or 'SL' in instr):
#         word = instr + ' $' + str(i) + ', ' + rand_regis() + ', ' + str(random.randint(0,31)) + '\n'
#         f.write(word)
#     else:
#         word = instr + ' $' + str(i) + ', ' + rand_regis() + ', ' + rand_regis() + '\n'
#         f.write(word)
    