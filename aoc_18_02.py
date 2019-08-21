from collections import Counter

with open(r'aoc_18_02.txt', 'r') as f:
    raw_input = f.read()

inputs = raw_input.strip().split("\n")

def day_1():
    twos = 0
    threes = 0
    for box_id in inputs:
        c = Counter(box_id)
        for key in c:
            if c[key] == 2:
                twos += 1
                break
        for key in c:
            if c[key] == 3:
                threes += 1
                break
    result = twos * threes
    return result


def day_2():
    sorted_inputs = sorted(inputs)
    for i in range(len(sorted_inputs)):
        count = 0
        for j in range(len(sorted_inputs[i])):
            if not sorted_inputs[i][j] == sorted_inputs[i+1][j]:
                count += 1
        if count == 1:
            print(sorted_inputs[i], "\n", sorted_inputs[i+1], sep="")
            break

print(day_1())
print(day_2())
