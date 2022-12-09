with open('input_03.txt', 'r') as f:
    raw_inputs = f.read().strip().split('\n')

## DAY 1 ##
def max_val(options):
    if options[0] > options[1]:
        return "0"
    return "1"

def min_val(options):
    if options[0] > options[1]:
        return "1"
    return "0"

def parse(inputs):
    bits = {x: {0: 0, 1: 0} for x in range(len(inputs[0]))}
    for binary in inputs:
        for idx, bit in enumerate(binary):
            bits[idx][int(bit)] += 1
    
    gamma_rate = "".join(max_val(bits[x]) for x in bits)
    epsilon_rate = "".join(min_val(bits[x]) for x in bits)
    return int(gamma_rate, 2) * int(epsilon_rate, 2)

print(parse(raw_inputs))

## DAY 2 ##
def oxygen_rating(inputs):
    ratings = [x for x in inputs]
    idx = 0
    while True:
        zeros = sum(1 for x in ratings if x[idx] == "0")
        ones = sum(1 for x in ratings if x[idx] == "1")

        if ones >= zeros:
            filter = "1"
        else:
            filter = "0"
        
        ratings = [x for x in ratings if x[idx] == filter]

        if len(ratings) == 1:
            break

        idx += 1
    return int(ratings[0], 2)

def co2_scrubber(inputs):
    ratings = [x for x in inputs]
    idx = 0
    while True:
        zeros = sum(1 for x in ratings if x[idx] == "0")
        ones = sum(1 for x in ratings if x[idx] == "1")

        if zeros <= ones:
            filter = "0"
        else:
            filter = "1"

        ratings = [x for x in ratings if x[idx] == filter]

        if len(ratings) == 1:
            break

        idx += 1
    return int(ratings[0], 2)

print(oxygen_rating(raw_inputs) * co2_scrubber(raw_inputs))