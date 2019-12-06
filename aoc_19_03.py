import cProfile

with open(r'aoc_19_03.txt', 'r') as f:
    raw_input = f.read()

def traverse_wire(wire, day_two=False):
    wire_info = {}
    x, y, count = 0, 0, 0
    directions =  {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}
    for part in wire:
        for _ in range(int(part[1:])):
            offset = directions[part[0]]
            x += offset[0]
            y += offset[1]
            count += 1
            wire_info[(x, y)] = count
    return wire_info

def solutions(raw_input):
    wires = [x.split(',') for x in raw_input.strip().split('\n')]

    wire_one = traverse_wire(wires[0])
    wire_two = traverse_wire(wires[1])

    crossings = wire_one.keys() & wire_two.keys()

    fewest_steps = min(crossings, key=lambda x: wire_one[x] + wire_two[x])
    steps = wire_one[fewest_steps] + wire_two[fewest_steps]

    closest = min([x for x in crossings], key=lambda x: abs(x[0]) + abs(x[1]))
    distance = abs(closest[0]) + abs(closest[1])

    return ('day one', distance, 'day two', steps)


# test_small = """R8,U5,L5,D3\nU7,R6,D4,L4"""
# test_one = """R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83"""
# test_two = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""

# print(solutions(test_small))
# print(solutions(test_one))
# print(solutions(test_two))
print(solutions(raw_input))

cProfile.run('solutions(raw_input)')