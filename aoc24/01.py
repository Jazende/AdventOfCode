import os
with open(f'input_{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '''3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3'''

### Part 1 ###

left_list = sorted( int(line.split('   ')[0]) for line in raw_inputs.strip().split('\n') )
right_list = sorted( int(line.split('   ')[1]) for line in raw_inputs.strip().split('\n') )

distance = sum(
    abs(left_list[idx] - right_list[idx])
    for idx in range(len(left_list))
)

print(distance)

### Part 2 ###

from collections import Counter
count_right_list = Counter(right_list)

print(sum(
    nr * count_right_list[nr]
    for nr in left_list
))
