with open('aoc_15_2.txt', 'r') as f:
    raw_input = f.read()

import cProfile

def paper_and_ribbon(width, height, length):
    w = int(width)
    h = int(height)
    l = int(length)
    by_size = sorted([w, h, l], key=lambda x: x)
    smallest = by_size[0]
    middle = by_size[1]
    largest =  by_size[2]
    extra = smallest*middle
    wrapping_paper = (2*l*w)+(2*w*h)+(2*h*l) +smallest*middle
    volume = l*h*w
    ribbon = 2*smallest + 2*middle + volume
    return wrapping_paper, ribbon

def calc():
    paper = 0
    ribbon = 0
    for box in raw_input.split("\n"):
        l, w, h = box.split("x")
        new_paper, new_ribbon = paper_and_ribbon(l, w, h)
        paper += new_paper
        ribbon += new_ribbon
    print(paper, ribbon)
    return paper, ribbon

def calc_two():
    paper = 0
    ribbon = 0
    for box in raw_input.split("\n"):
        l, w, h = box.split("x")
        l = int(l)
        w = int(w)
        h = int(h)
        by_size = sorted([w, h, l])
        paper += (2*l*w) + (2*w*h) + (2*h*l) + by_size[0] * by_size[1]
        ribbon += 2 * by_size[0] + 2 * by_size[1] + l*h*w
    print(paper, ribbon)


cProfile.run('calc_two()')
