import load_jaz_funcs
from jaz_funcs.points import Punt
import re
import cProfile

with open('aoc_15_6.txt', 'r') as f:
    raw_input = f.read()



commands = re.findall(r'(toggle|turn) (on|off)?\s?(\d{1,3}),(\d{1,3}) through (\d{1,3}),(\d{1,3})',
                      raw_input)

def part_1(commands):
    grid = {}
    for i in range(1000):
        for j in range(1000):
            grid[(i, j)] = False
    true_false = [True, False]
    
    for command in commands:
        func, on_off, start_x, start_y, end_x, end_y = command
        start_x, start_y, end_x, end_y = int(start_x), int(start_y), int(end_x), int(end_y)
        if func == 'toggle':
            for i in range(start_x, end_x+1):
                for j in range(start_y, end_y+1):
                    grid[(i, j)] = true_false[grid[(i, j)]]
        elif on_off == 'on':
            for i in range(start_x, end_x+1):
                for j in range(start_y, end_y+1):
                    grid[(i, j)] = True
        elif on_off == 'off':
            for i in range(start_x, end_x+1):
                for j in range(start_y, end_y+1):
                    grid[(i, j)] = False      
    print(len([x for x in grid if grid[x] == True]))

def part_2(commands):
    grid = {}
    for i in range(1000):
        for j in range(1000):
            grid[(i, j)] = 0
    
    for command in commands:
        func, on_off, start_x, start_y, end_x, end_y = command
        start_x, start_y, end_x, end_y = int(start_x), int(start_y), int(end_x), int(end_y)
        if func == 'toggle':
            for i in range(start_x, end_x+1):
                for j in range(start_y, end_y+1):
                    grid[(i, j)] += 2
        elif on_off == 'on':
            for i in range(start_x, end_x+1):
                for j in range(start_y, end_y+1):
                    grid[(i, j)] += 1
        elif on_off == 'off':
            for i in range(start_x, end_x+1):
                for j in range(start_y, end_y+1):
                    grid[(i, j)] = max(grid[(i, j)] - 1, 0)
    print(sum([grid[x] for x in grid]))

part_2(commands)
