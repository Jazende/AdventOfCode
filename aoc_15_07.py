import re 

with open(r'aoc_15_07.txt', 'r') as f:
    raw_input = f.read()

class Wire:
    def __init__(self, signal):
        self.signal = signal
    
    @property
    def signal(self):
        return self._signal

    @signal.setter
    def signal(self, value):
        if value < 0:
            value += 65536
        self._signal = value
    
    def __repr__(self):
        # return f"<W: {self._signal}>"
        return str(self._signal)

def INT_AND_STR(signal, wire):
    return Wire(signal & wire.signal)

def STR_AND_STR(first, second):
    return Wire(first.signal & second.signal)

def OR(first, second):
    return Wire(first.signal | second.signal)

def XOR(first, second):
    return Wire(first.signal ^ second.signal)

def NOT(wire):
    return Wire(~wire.signal)

def LSHIFT(wire, amount):
    return Wire(wire.signal << amount)

def RSHIFT(wire, amount):
    return Wire(wire.signal >> amount)

def NEW(value):
    return Wire(value)

def COPY(wire):
    return Wire(wire.signal)

re_new = re.compile("([0-9]+) -> ([a-z]+)")
re_copy = re.compile("([a-z]+) -> ([a-z]+)")
re_not = re.compile("NOT ([a-z]+) -> ([a-z]+)")
re_int_and_str = re.compile("([0-9]+) AND ([a-z]+) -> ([a-z]+)")
re_str_and_str = re.compile("([a-z]+) AND ([a-z]+) -> ([a-z]+)")
re_or = re.compile("([a-z]+) OR ([a-z]+) -> ([a-z]+)")
re_lshift = re.compile("([a-z]+) LSHIFT ([0-9]+) -> ([a-z]+)")
re_rshift = re.compile("([a-z]+) RSHIFT ([0-9]+) -> ([a-z]+)")

input_ = raw_input.strip().split("\n")
inputs = []

skipped = []

for inp in input_:
    int_and_str = re_int_and_str.match(inp)
    if int_and_str is not None:
        inputs.append([INT_AND_STR, int(int_and_str[1]), int_and_str[2], int_and_str[3]])
        continue

    str_and_str = re_str_and_str.match(inp)
    if str_and_str is not None:
        inputs.append([STR_AND_STR, str_and_str[1], str_and_str[2], str_and_str[3]])
        continue

    not_ = re_not.match(inp)
    if not_ is not None:
        inputs.append([NOT, not_[1], not_[2]])
        continue

    or_ = re_or.match(inp)
    if or_ is not None:
        inputs.append([OR, or_[1], or_[2], or_[3]])
        continue

    lshift = re_lshift.match(inp)
    if lshift is not None:
        inputs.append([LSHIFT, lshift[1], int(lshift[2]), lshift[3]])
        continue

    rshift = re_rshift.match(inp)
    if rshift is not None:
        inputs.append([RSHIFT, rshift[1], int(rshift[2]), rshift[3]])
        continue

    new = re_new.match(inp)
    if new is not None:
        inputs.append([NEW, int(new[1]), new[2]])
        continue

    copy = re_copy.match(inp)
    if copy is not None:
        inputs.append([COPY, copy[1], copy[2]])
        continue

    skipped.append(inp)

if len(skipped) > 0:
    print(f"Inputs skipped! {len(skipped)}")

wires = {}
day_two_idx = 0
day_two_inputs = inputs.copy()

while True:
    action = False

    for inp in inputs:
        if inp[0] == LSHIFT or inp[0] == RSHIFT:
            if not inp[1] in wires.keys():
                continue
            wires[inp[3]] = inp[0](wires[inp[1]], inp[2])
            inputs.remove(inp)
            action = True
            break

        if inp[0] == INT_AND_STR:
            if not inp[2] in wires.keys():
                continue
            wires[inp[3]] = inp[0](int(inp[1]), wires[inp[2]])
            inputs.remove(inp)
            action = True
            break

        if inp[0] == STR_AND_STR or inp[0] == OR:
            if not inp[1] in wires.keys():
                continue
            if not inp[2] in wires.keys():
                continue
            wires[inp[3]] = inp[0](wires[inp[1]], wires[inp[2]])
            inputs.remove(inp)
            action = True
            break

        if inp[0] == NEW:
            wires[inp[2]] = inp[0](inp[1])
            inputs.remove(inp)
            action = True
            break

        if inp[0] == COPY or inp[0] == NOT:
            if not inp[1] in wires.keys():
                continue
            wires[inp[2]] = inp[0](wires[inp[1]])
            inputs.remove(inp)
            action = True
            break

    if not action:
        break

print("Day 1:", wires["a"])


### --- ### --- ### --- ### --- ### --- ### --- ### --- ### 
#                         DAY TWO
### --- ### --- ### --- ### --- ### --- ### --- ### --- ### 

old_value = wires["a"]
inputs = day_two_inputs
for idx, inp in enumerate(inputs):
    if inp[2] == "b":
        day_two_idx = idx
        break

inputs[day_two_idx] = [NEW, old_value.signal, 'b']

wires = {}

while True:
    action = False

    for inp in inputs:
        if inp[0] == LSHIFT or inp[0] == RSHIFT:
            if not inp[1] in wires.keys():
                continue
            wires[inp[3]] = inp[0](wires[inp[1]], inp[2])
            inputs.remove(inp)
            action = True
            break

        if inp[0] == INT_AND_STR:
            if not inp[2] in wires.keys():
                continue
            wires[inp[3]] = inp[0](int(inp[1]), wires[inp[2]])
            inputs.remove(inp)
            action = True
            break

        if inp[0] == STR_AND_STR or inp[0] == OR:
            
            if not inp[1] in wires.keys():
                continue
            if not inp[2] in wires.keys():
                continue
            wires[inp[3]] = inp[0](wires[inp[1]], wires[inp[2]])
            inputs.remove(inp)
            action = True
            break

        if inp[0] == NEW:
            wires[inp[2]] = inp[0](inp[1])
            inputs.remove(inp)
            action = True
            break

        if inp[0] == COPY or inp[0] == NOT:
            if not inp[1] in wires.keys():
                continue
            wires[inp[2]] = inp[0](wires[inp[1]])
            inputs.remove(inp)
            action = True
            break

    if not action:
        break

print("Day 2:", wires["a"])