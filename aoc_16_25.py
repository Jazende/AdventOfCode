import time

def signal():
    while True:
        yield 0
        yield 1

def solutions(raw_input, start_reg_a):
    register = {letter: 0 for letter in 'abcd'}
    register['a'] =  start_reg_a

    instructions = raw_input.strip().split('\n')
    index = -1

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

        elif actions[0] == "out":
            yield register[actions[1]]

with open(r'aoc_16_25.txt', 'r') as f:
    raw_input = f.read()

index = 0

while True:
    generator = solutions(raw_input, index)
    reference_signal = signal()
    count = 0
    while True:
        g = next(generator)
        r = next(reference_signal)
        # print(f'{index} > g: {g:>2} r: {r:>}')
        if not g == r:
            # print("\n")
            break
        else:
            count += 1
    
        if count == 20:
            break
    if count == 20:
        print(index)
        break
    index += 1

print(index)