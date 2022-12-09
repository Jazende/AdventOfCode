import timeit

with open('input_01.txt', 'r') as f:
    raw_inputs = f.read().strip().split('\n')
inputs = [int(x) for x in raw_inputs]


## Day 1 ##
def rolling(iterable, function):
    idx = 1
    output = []
    while True:
        output.append(function(iterable[idx-1], iterable[idx]))
        idx += 1
        if idx == len(iterable):
            break
    return output

def higher(a, b):
    if a < b: return True
    return False

count = sum(rolling(inputs, higher))
print(count)

setup = """
with open('input_01.txt', 'r') as f:
    raw_inputs = f.read().strip().split('\\n')
inputs = [int(x) for x in raw_inputs]

def rolling(iterable, function):
    idx = 1
    output = []
    while True:
        output.append(function(iterable[idx-1], iterable[idx]))
        idx += 1
        if idx == len(iterable):
            break
    return output

def higher(a, b):
    if a < b: return True
    return False
"""

code = '''
sum(rolling(inputs, higher))
'''

print(timeit.timeit(setup=setup, stmt=code, number=1)*1_000_000)

## Day 2 ##
# 199  A      
# 200  A B    
# 208  A B C  
# 210    B C D
# 200  E   C D
# ...

# A = idx: 0, 1, 2
# B = idx:    1, 2, 3
# A vs B = idx 0 vs 3

# B = idx: 1, 2, 3
# C = idx:    2, 3, 4
# B vs C = idx 1 vs 4

def rolling_2(iterable, function):
    idx = 3
    output = []
    while True:
        output.append(function(iterable[idx-3], iterable[idx]))
        idx += 1
        if idx == len(iterable):
            break
    return output

count = sum(rolling_2(inputs, higher))
print(count)

setup = """
with open('input_01.txt', 'r') as f:
    raw_inputs = f.read().strip().split('\\n')
inputs = [int(x) for x in raw_inputs]

def rolling_2(iterable, function):
    idx = 3
    output = []
    while True:
        output.append(function(iterable[idx-3], iterable[idx]))
        idx += 1
        if idx == len(iterable):
            break
    return output

def higher(a, b):
    if a < b: return True
    return False
"""

code = '''
sum(rolling_2(inputs, higher))
'''

print(timeit.timeit(setup=setup, stmt=code, number=1)*1_000_000)