import math

def part_1(steps = 12523873):
    tape = [0 for _ in range(steps)]
    state = "A"
    pos = math.ceil(steps/2)
    for i in range(steps):
        if state == "A":
            if tape[pos] == 0:
                tape[pos] = 1
                pos += 1
                state = "B"
                continue
            else:
                tape[pos] = 1
                pos -= 1
                state = "E"
                continue
            
        elif state == "B":
            if tape[pos] == 0:
                tape[pos] = 1
                pos += 1
                state = "C"
                continue
            else:
                tape[pos] = 1
                pos += 1
                state = "F"
                continue
            
        elif state == "C":
            if tape[pos] == 0:
                tape[pos] = 1
                pos -= 1
                state = "D"
                continue
            else:
                tape[pos] = 0
                pos += 1
                state = "B"
                continue
            
        elif state == "D":
            if tape[pos] == 0:
                tape[pos] = 1
                pos += 1
                state = "E"
                continue
            else:
                tape[pos] = 0
                pos -= 1
                state = "C"
                continue
            
        elif state == "E":
            if tape[pos] == 0:
                tape[pos] = 1
                pos -= 1
                state = "A"
                continue
            else:
                tape[pos] = 0
                pos += 1
                state = "D"
                continue
            
        elif state == "F":
            if tape[pos] == 0:
                tape[pos] = 1
                pos += 1
                state = "A"
                continue
            else:
                tape[pos] = 1
                pos += 1
                state = "C"
                continue
    print(tape.count(1))
part_1()
