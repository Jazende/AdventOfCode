with open(r'input_11.txt', 'r') as f:
    raw_inputs = f.read().strip()

# raw_inputs = '''5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526'''

class OctoGrid(dict):
    def __init__(self, raw_inputs, size=10):
        self.size = size
        for y, line in enumerate(raw_inputs.split('\n')):
            for x, char in enumerate(line):
                self[(x, y)] = {'energy': int(char), 'flashed': False, 'x': x, 'y': y}
        self.flashes = 0
        self.total_steps = 0

    def each(self):
        for y in range(self.size):
            for x in range(self.size):
                yield self[(x, y)]

    def step(self):
        self.flashes_this_turn = 0
        for octopus in self.each():
            octopus['energy'] += 1
        while True:
            changes = False
            for octopus in self.each():
                if octopus['energy'] > 9 and not octopus['flashed']:
                    octopus['flashed'] = True
                    self.flashes_this_turn += 1
                    self.flashes += 1
                    x = octopus['x']
                    y = octopus['y']
                    for oct in [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]:
                        if oct in self:
                            self[oct]['energy'] += 1
                    changes = True
            if not changes:
                break
        for octopus in self.each():
            if octopus['flashed']:
                octopus['energy'] = 0
                octopus['flashed'] = False
        self.total_steps += 1
        if self.flashes_this_turn == self.size*self.size:
            print(f'at step {self.total_steps} got {self.size*self.size} flashes in one turn.')

    def steps(self, steps=1):
        for _ in range(steps):
            self.step()

    def day_2(self):
        while True:
            self.step()
            if self.flashes_this_turn == self.size*self.size:
                break

    def __str__(self):
        return "\n".join("".join(str(self[(x, y)]['energy']) for x in range(self.size)) for y in range(self.size))

inputs = OctoGrid(raw_inputs)
inputs.steps(100)
print(inputs.flashes)

inputs.day_2()