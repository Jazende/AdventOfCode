with open('input_09.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '''0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45'''

raw_history = [[int(x) for x in line.strip().split(' ')] for line in raw_inputs.strip().split('\n')]

########################## DAY 9 PART 1 ########################## 

def find_increasing_value(history):
    result = []
    for idx in range(len(history)-1):
        result.append(history[idx+1]-history[idx])

    if all(x == 0 for x in result):
        return [result]
    else:
        return find_increasing_value(result) + [result]

total_sum = 0
for history in raw_history:
    increasing_list = find_increasing_value(history)
    increasing_list += [history]

    for idx, each in enumerate(increasing_list):
        # skip first cus its 0 anyway and makes code easier
        if idx == 0:
            continue
        increasing_list[idx].append(increasing_list[idx][-1] + increasing_list[idx-1][-1])

    total_sum += increasing_list[-1][-1]

print(total_sum)

########################## DAY 9 PART 2 ########################## 

raw_history = [[int(x) for x in line.strip().split(' ')] for line in raw_inputs.strip().split('\n')]

total_sum = 0
for history in raw_history:
    increasing_list = find_increasing_value(history)
    increasing_list += [history]

    for idx, each in enumerate(increasing_list):
        if idx == 0:
            continue
        increasing_list[idx].insert(0, increasing_list[idx][0] - increasing_list[idx-1][0])

    total_sum += increasing_list[-1][0]

print(total_sum)

