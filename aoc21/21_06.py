with open(r'input_06.txt', 'r') as f:
    raw_inputs = f.read()

raw_inputs = '3,4,3,1,2'

inputs = [int(x) for x in raw_inputs.split(',')]
old_lanternfish = {x: 0 for x in range(9)}
for fish in inputs:
    old_lanternfish[fish] += 1

for cycle in range(80):
    new_lanternfish = {}
    for age in range(9):
        new_lanternfish[age] = old_lanternfish[(age+1)%9]
    new_lanternfish[6] += old_lanternfish[0]
    old_lanternfish = new_lanternfish
    
print(sum(count for age, count in old_lanternfish.items()))

for cycle in range(256-80):
    new_lanternfish = {}
    for age in range(9):
        new_lanternfish[age] = old_lanternfish[(age+1)%9]
    new_lanternfish[6] += old_lanternfish[0]
    old_lanternfish = new_lanternfish

print(sum(count for age, count in old_lanternfish.items()))