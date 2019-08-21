from adventofcode_10 import *
import copy
import sys

real = "hwlqcszp"
test = "flqrgnkx"

def knots(text):
    return [text + "-" + str(x) for x in range(128)]

real_knots = knots(real)
test_knots = knots(test)

def char_to_binary(char):
    return bin(int(char, base=16))[2:].zfill(4)

def hash_to_binary(hash_):
    binary = ""
    for char in hash_:
        binary += char_to_binary(char)
    return binary

m_grid = lambda y: "".join([hash_to_binary(full_hash(x, 64)) for x in y])

def part1(grid):
    return grid.count("1")

# print(part1(m_grid(real_knots)))

def part2(grid, size, print_=False, regions=0):
    print(grid.count("1"))
    if grid.count("1") == 0:
        return regions
    else:
        if print_:
            print("xxxxx")
        first = grid.find("1")
        regions += 1
        checklist = [first]
        while True:
            if len(checklist) == 0:
                break
            check_item = checklist.pop(0)
            if print_:
                print("Checking:", check_item, checklist)
            if grid[check_item] == "1":
                grid = grid[:check_item] + "0" + grid[check_item+1:]
                if check_item < size:
                    if check_item == 0:
                        checklist.append(check_item+1)
                        checklist.append(check_item+size)
                    elif check_item == size-1:
                        checklist.append(check_item-1)
                        checklist.append(check_item+size)
                    elif 0 < check_item < size-1:
                        checklist.append(check_item-1)
                        checklist.append(check_item+size)
                        checklist.append(check_item+1)
                elif check_item+size > len(grid)-1:
                    if check_item%size == 0:
                        checklist.append(check_item+1)
                        checklist.append(check_item-size)
                    elif check_item%size == size-1:
                        checklist.append(check_item-1)
                        checklist.append(check_item-size)
                    elif 0 < check_item%size < size-1:
                        checklist.append(check_item-1)
                        checklist.append(check_item-size)
                        checklist.append(check_item+1)
                else:
                    if check_item%size == 0:
                        checklist.append(check_item+1)
                        checklist.append(check_item+size)
                        checklist.append(check_item-size)
                    elif check_item%size == size-1:
                        checklist.append(check_item-1)
                        checklist.append(check_item+size)
                        checklist.append(check_item-size)
                    elif 0 < check_item%size < size-1:
                        checklist.append(check_item-1)
                        checklist.append(check_item+size)
                        checklist.append(check_item-size)
                        checklist.append(check_item+1)
            if print_:
                print(checklist)
        return part2(grid, size, print_, regions)

def part2(grid, size, print_=False):
    regions = 0
    while grid.count("1") > 0:
        regions += 1
        if print_:
            print("xxxxx")
        first = grid.find("1")
        checklist = [first]
        while True:
            if len(checklist) == 0:
                break
            check_item = checklist.pop(0)
            if print_:
                print("Checking:", check_item, checklist)
            if grid[check_item] == "1":
                grid = grid[:check_item] + "0" + grid[check_item+1:]
                if check_item < size:
                    if check_item == 0:
                        checklist.append(check_item+1)
                        checklist.append(check_item+size)
                    elif check_item == size-1:
                        checklist.append(check_item-1)
                        checklist.append(check_item+size)
                    elif 0 < check_item < size-1:
                        checklist.append(check_item-1)
                        checklist.append(check_item+size)
                        checklist.append(check_item+1)
                elif check_item+size > len(grid)-1:
                    if check_item%size == 0:
                        checklist.append(check_item+1)
                        checklist.append(check_item-size)
                    elif check_item%size == size-1:
                        checklist.append(check_item-1)
                        checklist.append(check_item-size)
                    elif 0 < check_item%size < size-1:
                        checklist.append(check_item-1)
                        checklist.append(check_item-size)
                        checklist.append(check_item+1)
                else:
                    if check_item%size == 0:
                        checklist.append(check_item+1)
                        checklist.append(check_item+size)
                        checklist.append(check_item-size)
                    elif check_item%size == size-1:
                        checklist.append(check_item-1)
                        checklist.append(check_item+size)
                        checklist.append(check_item-size)
                    elif 0 < check_item%size < size-1:
                        checklist.append(check_item-1)
                        checklist.append(check_item+size)
                        checklist.append(check_item-size)
                        checklist.append(check_item+1)
    return regions

print(part2(m_grid(real_knots), 128))
