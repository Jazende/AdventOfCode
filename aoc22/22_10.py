with open(r'22_10.txt', 'r') as f:
    raw_lines = f.read().strip()

class Register:
    def __init__(self):
        self.x      = 1
        self.cycles_part_1 = 0
        self.cycles_part_2 = 0
        self.part_1_signal_strength = []
        self.part_2_drawing = ""

    def addx(self, x):
        self.cycle()
        self.cycle()
        self.x += x

    def noop(self):
        self.cycle()

    def cycle(self):
        drawing = self.cycles_part_2 - 1 <= self.x <= self.cycles_part_2 + 1
        self.part_2_drawing += "#" if drawing else "."

        self.cycles_part_1 += 1
        self.cycles_part_2 += 1

        # 20, 60, 100, 140, 180, 220 = every 20 between newlines
        if self.cycles_part_1 in [20, 60, 100, 140, 180, 220]:
            self.part_1_signal_strength.append(self.x * self.cycles_part_1)

        if self.cycles_part_2 == 40:
            self.cycles_part_2 = 0
            self.part_2_drawing += "\n"

register = Register()
for system_call in raw_lines.split('\n'):
    if system_call.startswith('addx'):
        call, x = system_call.split(' ')
        register.addx(int(x))
    elif system_call.startswith('noop'):
        register.noop()

print('Part 1:', sum(register.part_1_signal_strength))
print('Part 2:', register.part_2_drawing)