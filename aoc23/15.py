import string
import re

with open('input_15.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'

box_label = re.compile('([a-z]+)[-|=0-9]+')

########################## DAY 15 PART 1 ########################## 

def full_hash_value(sub_string):
    value = 0
    for char in sub_string:
        value += ord(char)
        value *= 17
        value %= 256
    return value

print(sum(full_hash_value(HASH) for HASH in raw_inputs.strip().split(',')))

########################## DAY 15 PART 2 ########################## 

def hash_value(sub_string):
    if sub_string.endswith('-'):
        sub_string = sub_string[:-1]
    else:
        sub_string = sub_string[:-2]

    value = 0
    for char in sub_string:
        value += ord(char)
        value *= 17
        value %= 256
    return value

hashmap = [ [] for idx in range(256) ]

for inp in raw_inputs.strip().split(','):
    box_nr = hash_value(inp)

    if inp.endswith('-'):
        label = inp[:-1]

        found_idx = -1
        for idx, text in enumerate(hashmap[box_nr]):
            if label in text:
                found_idx = idx
                break
        if found_idx >= 0:
            hashmap[box_nr].pop(found_idx)            
    else:
        label, box = inp.split('=')
        found_idx = -1
        for idx, text in enumerate(hashmap[box_nr]):
            if label in text:
                found_idx = idx
                break
        if found_idx >= 0:
            hashmap[box_nr][found_idx] = inp
        else:
            hashmap[box_nr].append(inp)


score = 0
for box_idx, box in enumerate(hashmap):
    for lens_idx, lens in enumerate(box):
        label, focal_length = lens.split('=')
        score += (box_idx + 1) * (lens_idx + 1) * int(focal_length)

print(score)