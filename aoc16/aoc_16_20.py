with open(r'aoc_16_20.txt', 'r') as f:
    raw_input = f.read().strip().split("\n")

def solutions(raw_input, day):
    blocked = [(int(line.split("-")[0]), int(line.split("-")[1])) for line in raw_input]
    blocked.sort(key=lambda x: x[0])

    nr = 0
    answers = 0
    max_ = 4294967295
    
    while True:
        new_block = False
        for block in blocked:
            if block[0] <= nr <= block[1]:
                nr = max(nr, block[1])
                new_block = True
        
        if not new_block:
            if day == 1:
                break
            answers += 1

        nr += 1

        if nr > max_:
            break

    if day == 1:
        return nr
    return answers

print(solutions(raw_input, day=1))
print(solutions(raw_input, day=2))