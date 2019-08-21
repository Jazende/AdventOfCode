import re

match = re.compile("([spx])([a-p0-9]+)(\/)?([a-p0-9]+)?")

def get_lineup(test=False):
    res = "abcdefghijklmnop"
    return res if not test else res[:5]

def get_input(test=False):
    if test:
        return ["s1", "x3/4", "pe/b"]
    else:
        with open('adventofcode_16.txt', 'r') as f:
            res = f.read().strip().split(',')
        return res

def spin(lu, value):
    '''lu = lineup'''
    return lu[-value:] + lu[:len(lu)-value]

def exchange(line, val_1, val_2):
    '''lu = lineup'''
    max_, min_ = max(val_1, val_2), min(val_1, val_2)
    return line[:min_] + line[max_] + line[min_+1:max_] + line[min_] + line[max_+1:]

def partner(lu, v1, v2):
    '''lu = lineup'''
    max_, min_ = max(lu.index(v1), lu.index(v2)), min(lu.index(v1), lu.index(v2))
    return lu[:min_] + lu[max_] + lu[min_+1:max_] + lu[min_] + lu[max_+1:]

def cycler(lineup, input_):
    while True:
        for inp in input_:
            a = re.match(match, inp)
            if a.group(1) == "s":
                lineup = spin(lineup, int(a.group(2)))
            if a.group(1) == "x":
                lineup = exchange(lineup, int(a.group(2)), int(a.group(4)))
            if a.group(1) == "p":
                lineup = partner(lineup, a.group(2), a.group(4))
        yield lineup

def part1(test=False):
    lineup = get_lineup(test)
    input_ = get_input(test)

    gen = cycler(lineup, input_)
    return next(gen)

print(part1())

def part2(test=False):
    lineup = get_lineup(test)
    input_ = get_input(test)
    
    gen = cycler(lineup, input_)

    count = None
    lineups = [lineup]
    for x in range(1000000000):
        lineup = next(gen)
        if lineup in lineups:
            count = 1000000000%len(lineups)
            break
        lineups.append(lineup)
    return lineups[count]

print(part2())
