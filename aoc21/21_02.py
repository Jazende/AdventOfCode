with open('input_02.txt', 'r') as f:
    raw_inputs = f.read().strip().split('\n')

## Day 1 ##
def calculate(raw_inputs):
    horizon = 0
    vertical = 0

    for input_ in raw_inputs:
        match input_.split(' '):
            case ('forward', dist):
                horizon += int(dist)
            case ('down', dist):
                vertical += int(dist)
            case ('up', dist):
                vertical -= int(dist)
    return horizon * vertical

print(calculate(raw_inputs))

## Day 2 ##
def calculate_2(raw_inputs):
    horizon = 0
    vertical = 0
    aim = 0

    for input_  in raw_inputs:
        match input_.split(' '):
            case ('up', dist):
                aim -= int(dist)
            case ('down', dist):
                aim += int(dist)
            case ('forward', dist):
                horizon += int(dist)
                vertical += (aim * int(dist))

    return horizon * vertical

print(calculate_2(raw_inputs))