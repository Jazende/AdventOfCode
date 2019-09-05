class Register:
    def __init__(self):
        self._a = 0
        self._b = 0

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if value < 0 or not isinstance(value, int):
            raise ValueError('Register can only be positive integer.')
        self._a = value
    
    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if value < 0 or not isinstance(value, int):
            raise ValueError('Register can only be positive integer.')
        self._b = value
    
    def __repr__(self):
        return f'A: {self.a}, B: {self.b}'

def load_instructions(raw_input):
    instructions = [line.split(' ') for line in raw_input.strip().split('\n')]
    return instructions

def run_instructions(instruction_set, register=None):
    index = -1
    if register is None:
        register = Register()
        
    while True:
        index += 1 
        if index == len(instruction_set):
            break
        
        instruction = instruction_set[index]
        if instruction[0] == "hlf":
            setattr(register, instruction[1], getattr(register, instruction[1]) // 2)
        elif instruction[0] == "tpl":
            setattr(register, instruction[1], getattr(register, instruction[1]) * 3)
        elif instruction[0] == "inc":
            setattr(register, instruction[1], getattr(register, instruction[1]) + 1)
        elif instruction[0] == "jmp":
            index += int(instruction[1]) - 1
        elif instruction[0] == "jie":
            if getattr(register, instruction[1][0]) % 2 == 0:
                index += int(instruction[2]) - 1
        elif instruction[0] == "jio":
            if getattr(register, instruction[1][0]) == 1:
                index += int(instruction[2]) - 1
        else:
            error = f"Instruction {instruction[0]} not found."
            raise ValueError(error)
    print(register)

sample_instructions = """inc a\njio a, +2\ntpl a\ninc a"""
with open(r'aoc_15_23.txt', 'r') as f:
    real_instructions = f.read().strip()

run_instructions(load_instructions(real_instructions))

day_two_register = Register()
day_two_register.a = 1
run_instructions(load_instructions(real_instructions), day_two_register)