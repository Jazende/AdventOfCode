import re

re_sue = re.compile('Sue (\d{1,3}): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)')

with open('aoc_15_16.txt', 'r') as f:
    raw_input = f.read()

lines = raw_input.strip().split("\n")
all_aunts = [re_sue.match(line) for line in lines]

present_sue = {
    'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5,
    'trees': 3, 'cars': 2, 'perfumes': 1}

def check_value(prop_name, value):
    if prop_name == "goldfish" or prop_name == "pomeranians":
        if present_sue[prop_name] > int(value):
            return True
        return False
    elif prop_name == "trees" or prop_name == "cats":
        if present_sue[prop_name] < int(value):
            return True
        return False
    if present_sue[prop_name] == int(value):
        return True
    return False

for sue in all_aunts:
    if not present_sue[sue[2]] == int(sue[3]):
        continue
    if not present_sue[sue[4]] == int(sue[5]):
        continue
    if not present_sue[sue[6]] == int(sue[7]):
        continue
    print("Day One:", sue[1])

for sue in all_aunts:
    if not check_value(sue[2], sue[3]):
        continue
    if not check_value(sue[4], sue[5]):
        continue
    if not check_value(sue[6], sue[7]):
        continue
    print("Day Two:", sue[1])

