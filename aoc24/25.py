import os
from itertools import product
with open(f'input_{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '''#####
# .####
# .####
# .####
# .#.#.
# .#...
# .....

# #####
# ##.##
# .#.##
# ...##
# ...#.
# ...#.
# .....

# .....
# #....
# #....
# #...#
# #.#.#
# #.###
# #####

# .....
# .....
# #.#..
# ###..
# ###.#
# ###.#
# #####

# .....
# .....
# .....
# #....
# #.#..
# #.#.#
# #####'''

### Part 1 ###

def read_lock(raw_lock):
    lock = [-1 for _ in range(len(raw_lock.strip().split('\n')[0]))]
    for line in raw_lock.strip().split('\n'):
        for idx, letter in enumerate(line):
            if letter == '#':
                lock[idx] += 1
    return lock

def read_key(raw_key):
    key = [-1 for _ in range(len(raw_key.strip().split('\n')[0]))]
    for line in raw_key.strip().split('\n')[::-1]:
        for idx, letter in enumerate(line):
            if letter == '#':
                key[idx] += 1
    return key

raw_locks_and_keys = raw_inputs.strip().split('\n\n')

keys = []
locks = { 0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {} }
locks_list = []

for lock_or_key in raw_locks_and_keys:
    if lock_or_key[0][0] == '.':
        lock = read_lock(lock_or_key)
        locks_list.append(lock)
    else:
        keys.append(read_key(lock_or_key))

count = 0
for key in keys:
    for lock in locks_list:
        stop = False
        for idx in range(5):
            if lock[idx] + key[idx] > 5:
                stop = True
                break
        if stop:
            continue
        count += 1
print(f'{count=}')