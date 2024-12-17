import os
with open(f'input_{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '''
# 47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47'''

raw_rules, raw_orders = raw_inputs.strip().split('\n\n')
rules = [(int(x.split('|')[0]), int(x.split('|')[1])) for x in raw_rules.split('\n')]
orders = [[int(x) for x in line.split(',')] for line in raw_orders.split('\n')]

### Part 1 ###

count = 0
incorrect_orders = []
for order_idx, order in enumerate(orders):

    correct_order = True
    for left, right in rules:
        idx_left = -1 if not left in order else order.index(left)
        idx_right = -1 if not right in order else order.index(right)

        if idx_left == -1:
            continue
        if idx_right == -1:
            continue
        if idx_left > idx_right:
            correct_order = False
            incorrect_orders.append(order)
            break

    if correct_order:
        count += order[len(order)//2]

print(count)
# print(len(incorrect_orders))
# print(incorrect_orders)

### Part 2 ###

for order in incorrect_orders:
    while True:
        error = False

        for left, right in rules:
            idx_left = -1 if not left in order else order.index(left)
            idx_right = -1 if not right in order else order.index(right)

            if idx_left == -1:
                continue
            if idx_right == -1:
                continue
            if idx_left > idx_right:
                error = True
                order[idx_right] = left
                order[idx_left] = right
                break
        
        if not error:
            break

# print(incorrect_orders)
print(sum(x[len(x)//2] for x in incorrect_orders))