import cProfile

with open('aoc_15_1.txt', 'r') as f:
    raw_input = f.read()

def floor(input_):
    count = 0
    for idx, char in enumerate(raw_input):
        if char == '(':
            count += 1
        if char == ')':
            count -= 1
        if count == -1:
            print(idx+1)
    print(count)
    return count

cProfile.run('floor(raw_input)')
