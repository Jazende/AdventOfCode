import time

with open(r'aoc_16_23.txt', 'r') as f:
    raw_input = f.read()

# raw_input = """
# cpy 2 a
# tgl a
# tgl a
# tgl a
# cpy 1 a
# dec a
# dec a
# """

with open(r'aoc_16_23_2.txt', 'r') as f:
    raw_input_2 = f.read()

def solutions(raw_input, day=1):
    register = {letter: 0 for letter in 'abcd'}
    if day == 1:
        register["a"] = 7
    if day == 2:
        register["a"] = 12

    instructions = raw_input.strip().split('\n')
    index = -1

    while True:
        index += 1

        if index == len(instructions):
            break

        actions = instructions[index].split(' ')
        print(index, register, actions)

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

            try:
                jump = int(actions[2])
            except:
                jump = register[actions[2]]

            if not value == 0:
                index += jump - 1

        elif actions[0] == "tgl":
            instruction_to_change = register[actions[1]] + index
            try:
                actions_to_change = instructions[instruction_to_change].split(" ")
            except:
                print("Errors:", len(instructions), index, instruction_to_change)
            else:
                if len(actions_to_change) == 2:
                    if actions_to_change[0] == "inc":
                        actions_to_change[0] = "dec"
                    else:
                        actions_to_change[0] = "inc"

                elif len(actions_to_change) == 3:
                    if actions_to_change[0] == "jnz":
                        actions_to_change[0] = "cpy"
                    else:
                        actions_to_change[0] = "jnz"

                instructions[instruction_to_change] = " ".join(actions_to_change)

        elif actions[0] == "add":
            try:
                value = int(actions[2])
            except:
                value = register[actions[2]]
            
            register[actions[1]] += value

        elif actions[0] == "mul":
            register[actions[1]] += (register[actions[2]] * register[actions[3]])

        if index == 17:
            break

    return register["a"]

# print(solutions(raw_input, day=1))
print(solutions(raw_input_2, day=2))