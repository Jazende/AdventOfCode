import load_jaz_funcs
from jaz_funcs.points import Punt
import cProfile

with open('aoc_15_3.txt', 'r') as f:
    raw_input = f.read()

def part_1():
    houses = [Punt(0, 0, value=1)]
    
    cur_x = 0
    cur_y = 0
    for move in raw_input:
        if move == ">":
            cur_y += 1
        elif move == "<":
            cur_y -= 1
        elif move == "v":
            cur_x -= 1
        elif move == "^":
            cur_x += 1
        temp = Punt(cur_x, cur_y)
        if temp in houses:
            houses[houses.index(temp)].value += 1
        else:
            temp.value = 1
            houses.append(temp)

def part_2():
    houses = [Punt(0, 0, value=1)]
    
    cur_x = 0
    cur_y = 0
    for move in raw_input[0::2]:
        if move == ">":
            cur_y += 1
        elif move == "<":
            cur_y -= 1
        elif move == "v":
            cur_x -= 1
        elif move == "^":
            cur_x += 1
        temp = Punt(cur_x, cur_y)
        if temp in houses:
            houses[houses.index(temp)].value += 1
        else:
            temp.value = 1
            houses.append(temp)
            
    cur_x = 0
    cur_y = 0
    for move in raw_input[1::2]:
        if move == ">":
            cur_y += 1
        elif move == "<":
            cur_y -= 1
        elif move == "v":
            cur_x -= 1
        elif move == "^":
            cur_x += 1
        temp = Punt(cur_x, cur_y)
        if temp in houses:
            houses[houses.index(temp)].value += 1
        else:
            temp.value = 1
            houses.append(temp)
    
    print(len(houses))

cProfile.run('part_1()')
