import os
import re
with open(f'input_{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''

### Part 1 ###

re_find_mul = re.compile('mul\((\d+),(\d+)\)')

print(sum(int(x[0]) * int(x[1]) for x in re_find_mul.findall(raw_inputs)))

### Part 2 ###

# raw_inputs = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''

reduced_inputs = raw_inputs
while True:
    first_dont = reduced_inputs.find("don't()")
    if first_dont == -1:
        break
    first_post_dont_do = reduced_inputs.find("do()", first_dont)
    if first_post_dont_do == -1:
        reduced_inputs = reduced_inputs[0:first_dont]
    else:
        reduced_inputs = reduced_inputs[0:first_dont] + reduced_inputs[first_post_dont_do + 4:-1]

print(sum(int(x[0]) * int(x[1]) for x in re_find_mul.findall(reduced_inputs)))