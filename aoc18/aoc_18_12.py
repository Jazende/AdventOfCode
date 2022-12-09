import copy

with open(r'aoc_18_12.txt', 'r') as f:
    raw_input = f.read()

start, empty, *inputs = raw_input.strip().split("\n")
init = {}
for i in range(len(start)-15):
    init[i] = start[i+15]
inputs_splits = [x.split(" => ") for x in inputs]
inputs = {x[0]: x[1] for x in inputs_splits}

class Plant:
    def __init__(self, value):
        self.value = value
        self.temp_value = "."

    def set_temp(self, val):
        self.temp_value = val

    def commit(self):
        self.value = self.temp_value

class Plants:
    def __init__(self, inputs):
        self.plants = {}
        for idx, value in enumerate(inputs):
            self.plants[idx] = Plant(value)

    def generation(self):
        for i in range(min(self.plants.keys()), max(self.plants.keys())+1):
            for x in range(i-2, i+3):
                if not x in self.plants.keys():
                    self.plants[x] = Plant(".")
            compare = ""
            for x in range(i-2, i+3):
                compare += self.plants[x].value
            self.plants[i].set_temp(inputs[compare])

        for i in range(min(self.plants.keys()), max(self.plants.keys())+1):
            self.plants[i].commit()

    def print(self):
        print("".join([self.plants[x].value for x in self.plants.keys() if 0 <= x < 100]))

    def value(self):
        sum_ = 0
        for key, value in self.plants.items():
            if value.value == "#":
                sum_ += key
        return sum_

    def __repr__(self):
        return "".join([x[1].value for x in sorted([[key, value] for key, value in self.plants.items()])])

## DAY 1 ##
p = Plants(start[15:])

for i in range(20):
    p.generation()
    
print(p.value())

## DAY 2 ##
p = Plants(start[15:])
prev_value = 0
for i in range(102):
    p.generation()
    new_value = p.value()
    if new_value - prev_value == 46:
        print("i:", i)
        break
    prev_value = new_value

day_2 = new_value + (50000000000 - 102)*46
print(day_2)
