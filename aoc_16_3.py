import re

with open('aoc_16_3.txt', 'r') as file:
    raw_input = file.read()

triangles = raw_input.split("\n")
sides = re.findall("\s*(\d+)\s*(\d+)\s*(\d+)\s?\n", raw_input)
sides = [(int(x[0]), int(x[1]), int(x[2])) for x in sides]
print(len([x for x in sides if x[0]+x[1]>x[2] and x[1]+x[2]>x[0] and x[0]+x[2]>x[1]]))

revised_sides = []
for x in range(0, len(sides), 3):
    one = [sides[x][0], sides[x+1][0], sides[x+2][0]]
    two = [sides[x][1], sides[x+1][1], sides[x+2][1]]
    three = [sides[x][2], sides[x+1][2], sides[x+2][2]]
    
    revised_sides.append(one)
    revised_sides.append(two)
    revised_sides.append(three)

print(len([x for x in revised_sides if x[0]+x[1]>x[2] and x[1]+x[2]>x[0] and x[0]+x[2]>x[1]]))
