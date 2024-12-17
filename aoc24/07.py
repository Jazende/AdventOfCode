import os
from itertools import product
from functools import cache

with open(f'input_{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    raw_inputs = f.read()

raw_inputs = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''

### Part 1 ###

inputs = {int(line.split(':' )[0]): list(int(x) for x in line.split(': ')[1].split(' ')) for line in raw_inputs.strip().split('\n')}

def func_add(x, y): return x + y
def func_mul(x, y): return x * y

operators = [ func_add, func_mul, func_concat ]

count = 0
for result, inp in inputs.items():
    for test in product(operators, repeat=len(inp)-1):
        copy_inp = [x for x in inp]
        test_result = copy_inp.pop(0)
        test = [x for x in test]
        while True:
            if len(test) == 0:
                break
            test_result = test.pop(0)(test_result, copy_inp.pop(0))
        if result == test_result:
            count += test_result
            break

print(count)

### Part 2 ###

inputs = {int(line.split(':' )[0]): list(int(x) for x in line.split(': ')[1].split(' ')) for line in raw_inputs.strip().split('\n')}

def func_concat(x, y): return int(f'{x}{y}')

operators = [ func_add, func_mul, func_concat ]

count = 0
for result, inp in inputs.items():
    for test in product(operators, repeat=len(inp)-1):
        copy_inp = [x for x in inp]
        test_result = copy_inp.pop(0)
        test = [x for x in test]
        while True:
            if len(test) == 0:
                break
            test_result = test.pop(0)(test_result, copy_inp.pop(0))
        if result == test_result:
            count += test_result
            break

print(count)