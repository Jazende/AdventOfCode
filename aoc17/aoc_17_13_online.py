import itertools

real = []
with open("adventofcode_13.txt", 'r') as f:
    for line in f:
        real.append(line.strip())

lines = [line.split(': ') for line in real]

heights = {int(pos): int(height) for pos, height in lines}

def scanner(height, time):
    offset = time % ((height - 1) * 2)

    return 2 * (height - 1) - offset if offset > height - 1 else offset

part1 = sum(pos * heights[pos] for pos in heights if scanner(heights[pos], pos) == 0)

part2 = next(wait for wait in itertools.count() if not any(scanner(heights[pos], wait + pos) == 0 for pos in heights))
