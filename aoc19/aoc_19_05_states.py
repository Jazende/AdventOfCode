import cProfile

with open(r'aoc_19_05.txt', 'r') as f:
    raw_inputs = f.read()

class IntMachine:
    def __init__(self, raw_inputs):
        self.base_instructions = [int(x) for x in raw_inputs.split(',')]

    def get(self, index, mode):
        return self.instructions[self.instructions[index]] if mode == 0 else self.instructions[index]

    def set(self, index, value):
        self.instructions[self.instructions[index]] = value

    def run(self, input):
        self.instructions = [x for x in self.base_instructions]
        input = 1 if not input else input
        output, index = 0, 0

        while True:
            string = str(self.instructions[index]).zfill(5)
            opcode, mode_1, mode_2, mode_3 = int(string[-2:]), int(string[-3]), int(string[-4]), int(string[-5])

            if opcode == 99:
                print('PROGRAM HALT')
                break

            param_1 = self.get(index + 1, mode_1)

            if opcode == 3:
                self.set(index + 1, input)
                index += 2
                continue

            if opcode == 4:
                print(f'Output: {self.get(index + 1, mode_1)}')
                index += 2
                continue

            param_2 = self.get(index + 2, mode_2)

            if opcode == 1:
                self.set(index + 3, param_1 + param_2)
                index += 4

            if opcode == 2:
                self.set(index + 3, param_1 * param_2)
                index += 4

            if opcode == 5:
                index = index + 3 if param_1 == 0 else param_2

            if opcode == 6:
                index = param_2 if param_1 == 0 else index + 3

            if opcode == 7:
                value = 1 if param_1 < param_2 else 0
                self.set(index + 3, value)
                index += 4

            if opcode == 8:
                value = 1 if param_1 == param_2 else 0
                self.set(index + 3, value)
                index += 4

machine = IntMachine(raw_inputs)
machine.run(1)
machine.run(5)
