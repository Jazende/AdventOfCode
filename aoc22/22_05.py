import re

with open(r'22_05.txt', 'r') as f:
    raw_lines = f.read().strip()

re_move_order = re.compile('move (\d+) from (\d+) to (\d+)')
orders = re_move_order.findall(raw_lines)

def intify(order):
    return [int(x) for x in order]

crates = [
    ['M', 'J', 'C', 'B', 'F', 'R', 'L', 'H'], 
    ['Z', 'C', 'D', ], 
    ['H', 'J', 'F', 'C', 'N', 'G', 'W', ], 
    ['P', 'J', 'D', 'M', 'T', 'S', 'B', ], 
    ['N', 'C', 'D', 'R', 'J', ], 
    ['W', 'L', 'D', 'Q', 'P', 'J', 'G', 'Z', ],
    ['P', 'Z', 'T', 'F', 'R', 'H', ],
    ['L', 'V', 'M', 'G', ], 
    ['C', 'B', 'G', 'P', 'F', 'Q', 'R', 'J', ], 
]

def execute_order_9000(amount, from_, to_):
    for _ in range(amount):
        crates[to_-1].append(crates[from_-1].pop(len(crates[from_-1])-1))

for order in orders:
    execute_order_9000(*intify(order))

print('Part 1:', ''.join(crate[-1] for crate in crates))

## Day 2

crates = [
    ['M', 'J', 'C', 'B', 'F', 'R', 'L', 'H'], 
    ['Z', 'C', 'D', ], 
    ['H', 'J', 'F', 'C', 'N', 'G', 'W', ], 
    ['P', 'J', 'D', 'M', 'T', 'S', 'B', ], 
    ['N', 'C', 'D', 'R', 'J', ], 
    ['W', 'L', 'D', 'Q', 'P', 'J', 'G', 'Z', ],
    ['P', 'Z', 'T', 'F', 'R', 'H', ],
    ['L', 'V', 'M', 'G', ], 
    ['C', 'B', 'G', 'P', 'F', 'Q', 'R', 'J', ], 
]

def execute_order_9001(amount, from_, to_):
    crates[to_-1] += crates[from_-1][-amount:]
    crates[from_-1] = crates[from_-1][0:len(crates[from_-1])-amount]

for order in orders:
    execute_order_9001(*intify(order))

print('Part 1:', ''.join(crate[-1] for crate in crates))
