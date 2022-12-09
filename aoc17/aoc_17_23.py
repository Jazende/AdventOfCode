with open(r'aoc_17_23.txt', 'r') as f:
    raw_input = f.read()

instructions = raw_input.strip().split('\n')

def get_register_value(key):
    try:
        return int(key)
    except ValueError:
        return register[key]

### DAY ONE ###
register = {x: 0 for x in 'abcdefgh'}

idx = 0
count_mul = 0
max_idx = len(instructions)
while True:
    if idx == max_idx:
        break

    instruction = instructions[idx]
    cmd, x, y = instruction.split(' ')

    if cmd == 'set':
        register[x] = get_register_value(y)
    elif cmd == 'sub':
        register[x] -= get_register_value(y)
    elif cmd == 'mul':
        register[x] *= get_register_value(y)
        count_mul += 1
    elif cmd == 'jnz'and not get_register_value(x) == 0:
        idx += (get_register_value(y) - 1)
    idx += 1
    
print(count_mul)


def day_two():
    count = 0
    for x in range(109300, 126317, 17):
        for i in range(2, int(x**(1/2))+1):
            if x % i == 0:
                count += 1
                break
    return count

print(day_two())
            
