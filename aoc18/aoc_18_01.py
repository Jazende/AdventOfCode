with open(r'aoc_18_01.txt', 'r') as f:
    raw_input = f.read()

inputs = raw_input.strip().split("\n")

def day_1():
    start = 0
    for x in inputs:
        start += int(x)
    return start

def day_2():
    check = set()
    start = 0
    stop = False
    while True:
        for x in inputs:
            start += int(x)

            if not start in check:
                check.add(start)
            else:
                print(start)
                stop = True
                break
        if stop:
            break
