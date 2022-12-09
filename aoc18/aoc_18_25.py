import sys; sys.path.append(r'C:\Users\kridder\Desktop\Python')
from custom import *
import cProfile

class Punt4D(BasePunt):
    points = ["x", "y", "z", "t"]

test_input_1 = """-1,2,2,0\n0,0,2,-2\n0,0,0,-2\n-1,2,0,0\n-2,-2,-2,2\n3,0,2,-1\n-1,3,2,2\n-1,0,-1,0\n0,2,1,-2\n3,0,0,0"""
test_input_2 = """0,0,0,0\n 3,0,0,0\n 0,3,0,0\n 0,0,3,0\n 0,0,0,3\n 0,0,0,6\n 9,0,0,0\n12,0,0,0"""
test_input_3 = """1,-1,0,1\n2,0,-1,0\n3,2,-1,0\n0,0,3,1\n0,0,-1,-1\n2,3,-2,0\n-2,2,0,0\n2,-2,0,-1\n1,-1,0,-1\n3,2,0,2"""
test_input_4 = """1,-1,-1,-2\n-2,-2,0,1\n0,2,1,3\n-2,3,-2,1\n0,2,3,-2\n-1,-1,1,-2\n0,-2,-1,0\n-2,2,3,-1\n1,2,2,0\n-1,-2,0,-2"""

with open(r'aoc_18_25.txt', 'r') as f:
   raw_input = f.read()

def lijst_naar_punten(inp):
    return [tuple([int(x) for x in line.strip().split(',')]) for line in inp.strip().split('\n')]

def count_constellations_2(input_):
    stars = [Punt4D(*[int(x) for x in line.strip().split(",")]) for line in input_.strip().split("\n")]
    constellations = [{star} for star in stars]

    for star in stars:
        for constellation in constellations:
            to_add = []
            for check_star in constellation:
                if star.manhattan_distance(check_star) <= 3:
                    to_add.append(star)
            for star in to_add:
                constellation.add(star)

    new_list = []
    
    while True:
        constellation = constellations[0]
        checking_idx = 1

        while True:
            if len(constellations) == checking_idx:
                break
            if not constellation.isdisjoint(constellations[checking_idx]):
                constellation |= constellations.pop(checking_idx)
            else:
                checking_idx += 1
        new_list.append(constellations.pop(0))

        if len(constellations) == 0:
            break

    second_list = []
    
    while True:
        constellation = new_list[0]
        checking_idx = 1

        while True:
            if len(new_list) == checking_idx:
                break
            if not constellation.isdisjoint(new_list[checking_idx]):
                constellation |= new_list.pop(checking_idx)
            else:
                checking_idx += 1
        second_list.append(new_list.pop(0))

        if len(new_list) == 0:
            break

    return len(second_list)


# print(4, count_constellations_2(test_input_1)) # 4
# print(2, count_constellations_2(test_input_2)) # 2
# print(3, count_constellations_2(test_input_3)) # 3
# print(8, count_constellations_2(test_input_4)) # 8

# cProfile.run('print(count_constellations_2(raw_input))')
print(count_constellations_2(raw_input))