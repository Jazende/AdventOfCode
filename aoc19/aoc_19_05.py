with open(r'aoc_19_05.txt', 'r') as f:
    raw_inputs = f.read()

def solutions(raw_inputs, day_two=False):
    inputs = [int(x) for x in raw_inputs.split(',')]

    index = 0
    output = 0
    input = 1 if not day_two else 5

    while True:
        string = "0000" + str(inputs[index])

        new_opcode = int(string[-2:])
        mode_digits = string[-5:-2]

        if new_opcode == 1:
            if mode_digits[-1] == "0":
                val_1 = inputs[inputs[index+1]]
            elif mode_digits[-1] == "1":
                val_1 = inputs[index+1]
            
            if mode_digits[-2] == "0":
                val_2 = inputs[inputs[index+2]]
            elif mode_digits[-2] == "1":
                val_2 = inputs[index+2]
            
            inputs[inputs[index+3]] = val_1 + val_2
            index += 4

        elif new_opcode == 2:
            if mode_digits[-1] == "0":
                val_1 = inputs[inputs[index+1]]
            elif mode_digits[-1] == "1":
                val_1 = inputs[index+1]
            
            if mode_digits[-2] == "0":
                val_2 = inputs[inputs[index+2]]
            elif mode_digits[-2] == "1":
                val_2 = inputs[index+2]
            
            inputs[inputs[index+3]] = val_1 * val_2
            index += 4

        elif new_opcode == 3:
            if mode_digits[-1] == "0":
                inputs[inputs[index+1]] = input
            elif mode_digits[-1] == "1":
                inputs[index+1] = input

            index += 2

        elif new_opcode == 4:
            if mode_digits[-1] == "0":
                val_1 = inputs[inputs[index+1]]
            elif mode_digits[-1] == "1":
                val_1 = inputs[index+1]
                
            output = val_1
            print("L Output:", output)

            index += 2

        elif new_opcode == 5 and day_two:
            if mode_digits[-1] == "0":
                val_1 = inputs[inputs[index+1]]
            elif mode_digits[-1] == "1":
                val_1 = inputs[index+1]
            
            if mode_digits[-2] == "0":
                val_2 = inputs[inputs[index+2]]
            elif mode_digits[-2] == "1":
                val_2 = inputs[index+2]

            if val_1 == 0:
                index += 3
            else:
                index = val_2
            
        elif new_opcode == 6 and day_two:
            if mode_digits[-1] == "0":
                val_1 = inputs[inputs[index+1]]
            elif mode_digits[-1] == "1":
                val_1 = inputs[index+1]
            
            if mode_digits[-2] == "0":
                val_2 = inputs[inputs[index+2]]
            elif mode_digits[-2] == "1":
                val_2 = inputs[index+2]
            
            if val_1 == 0:
                index = val_2
            else:
                index += 3

        elif new_opcode == 7 and day_two:
            if mode_digits[-1] == "0":
                val_1 = inputs[inputs[index+1]]
            elif mode_digits[-1] == "1":
                val_1 = inputs[index+1]
            
            if mode_digits[-2] == "0":
                val_2 = inputs[inputs[index+2]]
            elif mode_digits[-2] == "1":
                val_2 = inputs[index+2]
            
            inputs[inputs[index+3]] = 1 if val_1 < val_2 else 0
            index += 4

        elif new_opcode == 8 and day_two:
            if mode_digits[-1] == "0":
                val_1 = inputs[inputs[index+1]]
            elif mode_digits[-1] == "1":
                val_1 = inputs[index+1]
            
            if mode_digits[-2] == "0":
                val_2 = inputs[inputs[index+2]]
            elif mode_digits[-2] == "1":
                val_2 = inputs[index+2]
            
            inputs[inputs[index+3]] = 1 if val_1 == val_2 else 0
            index += 4

        elif new_opcode == 99:
            break

        else:
            print("Opcode", opcode, "not handled. Halting prematurely at index", index)
            break

    return output

print(solutions(raw_inputs))
print(solutions(raw_inputs, day_two=True))
