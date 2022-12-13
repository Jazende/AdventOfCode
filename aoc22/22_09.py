with open(r'22_09.txt', 'r') as f:
    raw_lines = f.read().strip()

motions = raw_lines.split('\n')

## Functions 
def move_head(head_addition):
    head_location[0] += head_addition[0]
    head_location[1] += head_addition[1]

def update_tail_location(head_location, tail_location):
    head_x, head_y = head_location

    while True:
        tail_x, tail_y = tail_location

        if abs(head_location[0] - tail_location[0]) <= 1 and abs(head_location[1] - tail_location[1]) <= 1:
            break

        if head_x == tail_x:
            if head_y > tail_y:
                tail_location[0] += 0
                tail_location[1] += 1

            elif head_y == tail_y:
                tail_location[0] += 0
                tail_location[1] += 0    

            elif head_y < tail_y:
                tail_location[0] += 0
                tail_location[1] += -1

        elif head_y == tail_y:
            if head_x > tail_x:
                tail_location[0] += 1
                tail_location[1] += 0   

            elif head_x == tail_x:
                tail_location[0] += 0
                tail_location[1] += 0   

            elif head_x < tail_x:
                tail_location[0] += -1
                tail_location[1] += 0

        elif head_x > tail_x and head_y > tail_y:
                tail_location[0] += 1
                tail_location[1] += 1

        elif head_x > tail_x and head_y < tail_y:
                tail_location[0] += 1
                tail_location[1] += -1

        elif head_x < tail_x and head_y > tail_y:
                tail_location[0] += -1
                tail_location[1] += 1

        elif head_x < tail_x and head_y < tail_y:
                tail_location[0] += -1
                tail_location[1] += -1
    
    return head_location, tail_location

def part_1_update_tail(head_location, tail_location, tails_locations_visited):
    head_location, tail_location = update_tail_location(head_location, tail_location)
    tails_locations_visited.add(tuple(tail_location))
    return head_location, tail_location, tails_locations_visited

def part_2_update_tails(head_location, tails_locations, tails_locations_visited):
    head_location, tails_locations[0] = update_tail_location(head_location, tails_locations[0])
    tails_locations[0:2] = update_tail_location(*tails_locations[0:2])
    tails_locations[1:3] = update_tail_location(*tails_locations[1:3])
    tails_locations[2:4] = update_tail_location(*tails_locations[2:4])
    tails_locations[3:5] = update_tail_location(*tails_locations[3:5])
    tails_locations[4:6] = update_tail_location(*tails_locations[4:6])
    tails_locations[5:7] = update_tail_location(*tails_locations[5:7])
    tails_locations[6:8] = update_tail_location(*tails_locations[6:8])
    tails_locations[7:9] = update_tail_location(*tails_locations[7:9])

    tails_locations_visited.add(tuple(tails_locations[-1]))

    return head_location, tails_locations, tails_locations_visited

## Part 1 & 2
head_location = [0, 0]

part_1_visited = set()
part_1_tail_location = [0, 0]

part_2_visited = set()
part_2_tails_locations = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], ]

for motion in motions:
    direction, distance = motion.split(' ')
    distance = int(distance)

    for unit in range(distance):
        if direction == 'U':
            move_head((0, 1))
        elif direction == 'D':
            move_head((0, -1))
        elif direction == 'L':
            move_head((-1, 0))
        elif direction == 'R':
            move_head((1, 0))
        else:
            print('Undeclared motion:', motion)
        head_location, part_1_tail_location,   part_1_visited = part_1_update_tail( head_location, part_1_tail_location,   part_1_visited)
        head_location, part_2_tails_locations, part_2_visited = part_2_update_tails(head_location, part_2_tails_locations, part_2_visited)

print('Part 1:', len(part_1_visited))
print('Part 2:', len(part_2_visited))
