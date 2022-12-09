import time

with open('input_15.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '''
# 1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581'''

def calculate_risk(raw_inputs, day=1):
    risk_map = {(x, y): int(char) for y, line in enumerate(raw_inputs.strip().split('\n')) for x, char in enumerate(line)}

    prelim_height = len(raw_inputs.strip().split('\n'))
    prelim_width = len(raw_inputs.strip().split('\n')[0])

    if day == 2:
        for mul_y in range(5):
            for mul_x in range(5):
                if mul_x == 0 and mul_y == 0:
                    continue
                for y in range(prelim_height):
                    for x in range(prelim_width):
                        new_risk = (risk_map[(x, y)] + mul_x + mul_y)
                        risk_map[(mul_x*prelim_width + x, mul_y*prelim_height + y)] = new_risk if new_risk <= 9 else new_risk - 9

    height = max(y for x, y in risk_map.keys())
    width = max(x for x, y in risk_map.keys())
    end = (width, height)

    lowest_costs = {(0, 0): 0}
    points = [(0, 0)]

    count = 0
    while True:
        if len(points) == 0:
            break
        count += 1
        current_point = points.pop(0)
        x, y = current_point
        current_point_cost = lowest_costs[current_point]
        connected_points = [
            loc for loc in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            if loc in risk_map
        ]
        for connected in connected_points:
            new_cost = current_point_cost + risk_map[connected]
            if not connected in lowest_costs:
                lowest_costs[connected] = new_cost
                points.append(connected)
            else:
                if new_cost < lowest_costs[connected]:
                    lowest_costs[connected] = new_cost
                    points.append(connected)

    return lowest_costs[(width, height)]

print(calculate_risk(raw_inputs, day=1))
print(calculate_risk(raw_inputs, day=2))
