from copy import copy
import re

with open(r'aoc_18_16.txt', 'r') as f:
    raw_input = f.read()

op_re = 'Before:\s+\[(\d+), (\d+), (\d+), (\d+)\]\s+(\d+)\s(\d+)\s(\d+)\s(\d+)\s+After:\s+\[(\d+), (\d+), (\d+), (\d+)\]'
opcode_tests = [tuple(int(x) for x in y) for y in re.findall(op_re, raw_input)]
inp_re = '(\d+)\s(\d+)\s(\d+)\s(\d+)(?!\s+After)'
inputs = [tuple(int(i) for i in j) for j in re.findall(inp_re, raw_input)]

def addr(registers, a, b, c):
    registers[c] = registers[a] + registers[b]
    return registers

def addi(registers, a, b, c):
    registers[c] = registers[a] + b
    return registers

def mulr(registers, a, b, c):
    registers[c] = registers[a] * registers[b]
    return registers

def muli(registers, a, b, c):
    registers[c] = registers[a] * b
    return registers

def banr(registers, a, b, c):
    registers[c] = registers[a] & registers[b]
    return registers

def bani(registers, a, b, c):
    registers[c] = registers[a] & b
    return registers

def borr(registers, a, b, c):
    registers[c] = registers[a] | registers[b]
    return registers

def bori(registers, a, b, c):
    registers[c] = registers[a] | b
    return registers

def setr(registers, a, b, c):
    registers[c] = registers[a]
    return registers

def seti(registers, a, b, c):
    registers[c] = a
    return registers

def gtir(registers, a, b, c):
    if a > registers[b]:
        registers[c] = 1
    else:
        registers[c] = 0
    return registers

def gtri(registers, a, b, c):
    if registers[a] > b:
        registers[c] = 1
    else:
        registers[c] = 0
    return registers

def gtrr(registers, a, b, c):
    if registers[a] > registers[b]:
        registers[c] = 1
    else:
        registers[c] = 0
    return registers

def eqir(registers, a, b, c):
    if a == registers[b]:
        registers[c] = 1
    else:
        registers[c] = 0
    return registers

def eqri(registers, a, b, c):
    if registers[a] == b:
        registers[c] = 1
    else:
        registers[c] = 0
    return registers

def eqrr(registers, a, b, c):
    if registers[a] == registers[b]:
        registers[c] = 1
    else:
        registers[c] = 0
    return registers

instructions = [addr, addi, mulr, muli, banr, bani, borr, bori,
                setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

def opcode_test(before, opcode, a, b, c, after):
    poss_codes = []
    for instr in instructions:
        if after == instr(copy(before), a, b, c):
            poss_codes.append(instr)
    return len(poss_codes), poss_codes

count = 0
opcode_instr = {x: None for x in range(16)}
opcodes_per_test = {}
for test in opcode_tests:
    before = [test[0], test[1], test[2], test[3]]
    after = [test[8], test[9], test[10], test[11]]
    rep = opcode_test(before, test[4], test[5], test[6], test[7], after)
    opcodes_per_test[test] = []
    for func in rep[1]:
        opcodes_per_test[test].append(func)
    if rep[0] >= 3:
        count += 1
print(count)

while True:
    for func, value in opcodes_per_test.items():
        if len(value) == 1:
            opcode_instr[func[4]] = value[0]
            to_del = value[0]
            break
        
    for func, value in opcodes_per_test.items():
        opcodes_per_test[func] = [x for x in opcodes_per_test[func] if not x == to_del]

    opcodes_per_test = {x: y for x, y in opcodes_per_test.items() if not len(y) == 0}

    if len([x for x, y in opcode_instr.items() if y is None]) == 0:
        break


start = [0, 0, 0, 0]
for i in inputs:
    start = opcode_instr[i[0]](start, i[1], i[2], i[3])
    
print(start[0])
