with open(r'input_24.txt', 'r') as f:
    raw_inputs = f.read().strip()

## Running through commands:
## input_1: z = input_1 + 15 
## input_2: z = current z * 26 + input 2 + 8 
## input_3: z = current z * 26 + input_3 + 2

## input_4: z = z mod 26; if z mod 26 - 9 == 1: z * 1 else z * 25
## because prev nr = z*26 + input_3 + 2: -> input_3 + 2 - 9 = 1 -> input_3 = 1 + 9 - 2 = 8
## input_4: z = z // 26; if input_3 == 8: z * 1, else z * 26 + inp_4
## -> input 3 must be 8
## prev: input 3 + 2 - 9 = input 4
## prev: input 3 - 7 = input 4

## input 5: z = current z * 26 + input_5 + 13
## input 6: z = current z * 26 + input_6 + 4
## input 7: z = current z * 26 + input_7 + 1

## input 8: z = z // 26; if z mod 26 - 5 == input_8: z * 1 else z * 26
## prev = ... * 26 + input_7 + 1/ -> input_7 + 1 - 5 = input 8 -> input_7 - 4 = input_8
## input 8: z = z // 26: if input_7 is input_8 + 4, else z * 26 || z + input_8 + 9
## prev: input 7 - 4 = input 8

## input 9: z = z * 26 + input_9 + 5

## input 10: z = z // 26; if z mod 26 - 7 == input_10; z * 1 else z * 26
## last z * 26 = input 9
## prev = ... *  26 + input_9 + 5: input_9 + 5  - 7 = input_10: -> input 9 - 2 = input_10
## input 10: z = z // 26; if input 9 - 2 == input 10: z*1 else z*26 || -> z + input_10 + 13
## prev: input 9 - 2 == input 10

## input 11: z = z // 26; if z mod 26 - 12 == input_11: z * 1 else z * 26
## last z * 26 : input 9 (used in input 10) -> input 7 (used in input 8) -> input 6
## prev = z* 26 + input 6 + 4 - 12 = input 11
## prev = input_6 - 8 = input 11

## input 12: z = z // 26; if z mod 26 - 10 == input 12: z * 1 else z * 26
## last z * 26: 9 (used in 10), 7 (used in 8), 6 (used in 11), 5
## prev = ... z*26 + input 5 + 13
## prev: input 5 + 13 - 10 = input 12
## prev: input 5 + 3 = input 12

## input 13: z = z // 26; if z mod 26 - 1 == input 13: z * 1 else z * 26
## last z * 26: 9 (used in10), 7 (used in 8), 6 (used in 11), 5 (used in 12), 3 (used in 4), input 2
## prev = ..z * 26 + input_2 + 8
## prev: input 2 + 8 - 1 = input 13
## prev: input 2 + 7 = input 13

## input 14: z = z // 26; if z mod 26 - 11 == input 14: z*1 else z*26
## last z*26: input 1
## prev = z*26 + input 1 + 15
## prev: input 1 + 15 - 11 = input 14
## prev: input 1 + 4 = input 14

######################################

## in_1 + 4 = in_14
## in_2 + 7 = in_13
## in_3 - 7 = in_4
## in_5 + 3 = in_12
## in_6 - 8 = in_11
## in_7 - 4 = in_8
## in_9 - 2 = in_10

######################################

## highest model nr:
## 12345678901234
## 52926995971999

######################################

## lowest model nr:
## 12345678901234
## 11811951311485



stop_at_counter = 14

class ALU:
    def __init__(self, monad):
        self.w = 0
        self.x = 0
        self.y = 0
        self.z = 0

        self.monad = monad
        self.monad_idx = 0

    def _get_register_value(self, register):
        if register in ['w', 'x', 'y', 'z']:
            return getattr(self, register)
        return int(register)

    def inp(self, register_a):
        val = int(self.monad[self.monad_idx])
        self.monad_idx += 1
        setattr(self, register_a, val)
    
    def add(self, register_a, register_b):
        a = self._get_register_value(register_a)
        b = self._get_register_value(register_b) 
        setattr(self, register_a, a + b)
    
    def mul(self, register_a, register_b):
        a = self._get_register_value(register_a)
        b = self._get_register_value(register_b)
        setattr(self, register_a, a * b)
    
    def div(self, register_a, register_b):
        a = self._get_register_value(register_a)
        b = self._get_register_value(register_b)
        setattr(self, register_a, a // b)
    
    def mod(self, register_a, register_b):
        a = self._get_register_value(register_a)
        b = self._get_register_value(register_b)
        setattr(self, register_a, a % b)

    def eql(self, register_a, register_b):
        a = self._get_register_value(register_a)
        b = self._get_register_value(register_b)
        val = 1 if a == b else 0
        setattr(self, register_a, val)

    def reset(self):
        self.w = 0
        self.x = 0
        self.y = 0
        self.z = 0

    @staticmethod
    def from_inputs(raw_inputs, monad):
        new = ALU(monad)
        input_counter = 0
        for line in raw_inputs.split('\n'):
            instr, *inputs = line.split(' ')
            fn = getattr(new, instr)
            fn(*inputs)
        return new

    def __str__(self):
        return f'{self.w}\t{self.x}\t{self.y}\t{self.z}'

#                                   12345678901234
test = ALU.from_inputs(raw_inputs, '11812962421585')
print(test)
day_1 = ALU.from_inputs(raw_inputs, '52926995971999')
print(day_1)
day_2 = ALU.from_inputs(raw_inputs, '11811951311485')
print(day_2)