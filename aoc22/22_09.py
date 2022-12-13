with open(r'22_09.txt', 'r') as f:
    raw_lines = f.read().strip()

motions = raw_lines.split('\n')

tails_locations_visited = set()
tail_location = [0, 0]
head_location = [0, 0]

def move_head(head_addition):
    head_location[0] += head_addition[0]
    head_location[1] += head_addition[1]

def update_tail_location(head_location, tail_location, tails_locations_visited):
    head_x, head_y = head_location

    while True:
        tails_locations_visited.add(tuple(tail_location))

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
    
    return head_location, tail_location, tails_locations_visited

for motion in motions:
    direction, distance = motion.split(' ')
    distance = int(distance)

    for unit in range(distance):
        if direction == 'U':
            move_head((0, 1))
        if direction == 'D':
            move_head((0, -1))
        if direction == 'L':
            move_head((-1, 0))
        if direction == 'R':
            move_head((1, 0))
        head_location, tail_location, tails_locations_visited = update_tail_location(head_location, tail_location, tails_locations_visited)

print(len(tails_locations_visited))

## Day 2 

def reduced_update_tail_location(head_location, tail_location):
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

def update_nine_tails_location(head_location, tails_locations, tails_locations_visited):
    head_location, tails_locations[0] = reduced_update_tail_location(head_location, tails_locations[0])
    tails_locations[0:2] = reduced_update_tail_location(*tails_locations[0:2])
    tails_locations[1:3] = reduced_update_tail_location(*tails_locations[1:3])
    tails_locations[2:4] = reduced_update_tail_location(*tails_locations[2:4])
    tails_locations[3:5] = reduced_update_tail_location(*tails_locations[3:5])
    tails_locations[4:6] = reduced_update_tail_location(*tails_locations[4:6])
    tails_locations[5:7] = reduced_update_tail_location(*tails_locations[5:7])
    tails_locations[6:8] = reduced_update_tail_location(*tails_locations[6:8])
    tails_locations[7:9] = reduced_update_tail_location(*tails_locations[7:9])

    tails_locations_visited.add(tuple(tails_locations[-1]))

    return head_location, tails_locations, tails_locations_visited

tails_locations_visited = set()
tails_locations = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], ]
head_location = [0, 0]

for motion in motions:
    direction, distance = motion.split(' ')
    distance = int(distance)

    for unit in range(distance):
        if direction == 'U':
            move_head((0, 1))
        if direction == 'D':
            move_head((0, -1))
        if direction == 'L':
            move_head((-1, 0))
        if direction == 'R':
            move_head((1, 0))
        head_location, tails_locations, tails_locations_visited = update_nine_tails_location(head_location, tails_locations, tails_locations_visited)

print(head_location, tails_locations, len(tails_locations_visited))
