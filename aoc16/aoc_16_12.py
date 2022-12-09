import time

with open(r'aoc_16_12.txt', 'r') as f:
    raw_input = f.read()

instructions = raw_input.strip().split('\n')
index = -1

register = {letter: 0 for letter in 'abcd'}
register["c"] = 1

while True:
    index += 1

    if index == len(instructions):
        break

    actions = instructions[index].split(' ')

    if actions[0] == "cpy":
        try:
            value = int(actions[1])
        except:
            value = register[actions[1]]

        register[actions[2]] = value

    elif actions[0] == "inc":
        register[actions[1]] += 1

    elif actions[0] == "dec":
        register[actions[1]] -= 1

    elif actions[0] == "jnz":
        try:
            value = int(actions[1])
        except:
            value = register[actions[1]]

        if not value == 0:
            index += (int(actions[2]) - 1)

print(register["a"])