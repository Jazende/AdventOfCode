from itertools import combinations

with open('input_11.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '''
# ...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....'''

def calculate_drift(galaxies, drift):
    idx = 0

    cols = max( key[0] for key in galaxies.keys() ) + 10
    rows = max( key[1] for key in galaxies.keys() ) + 10

    idx = 0
    while True:
        if idx < cols:
            if not any( key[0] == idx for key in galaxies.keys()):
                for key in galaxies.keys():
                    if key[0] > idx:
                        galaxies[key]['col_drift'] += galaxy_drift - 1

        if idx < rows:
            if not any( key[1] == idx for key in galaxies.keys()):
                for key in galaxies.keys():
                    if key[1] > idx:
                        galaxies[key]['row_drift'] += galaxy_drift - 1

        idx += 1

        if idx > cols and idx > rows:
            break
    
    adjusted_galaxies = [ (key[0] + value['col_drift'], key[1] + value['row_drift']) for key, value in galaxies.items()]
    return adjusted_galaxies

def calculate_distances(galaxies):
    cum_dist = 0
    for combination in combinations(galaxies, r=2):
        first, second = combination

        first_x, first_y = first
        second_x, second_y = second

        dist = abs(first_x - second_x) + abs(first_y - second_y)

        cum_dist += dist
    
    return cum_dist


# Drift of 2 (double as big) -> increased by 1
# Drift of 10 (10 times as big) -> from 1 to 10 = increase by 9

########################## DAY 8 PART 1 ########################## 

galaxy_drift = 2
galaxies = { 
    (col, row): { 'col_drift': 0, 'row_drift': 0 } 
    for row, line in enumerate(raw_inputs.strip().split('\n')) 
    for col, char in enumerate(line) if char == '#' 
}

adjusted_galaxies = calculate_drift(galaxies, galaxy_drift)
print(calculate_distances(adjusted_galaxies))

########################## DAY 8 PART 2 ########################## 

galaxy_drift = 1_000_000
galaxies = { 
    (col, row): { 'col_drift': 0, 'row_drift': 0 } 
    for row, line in enumerate(raw_inputs.strip().split('\n')) 
    for col, char in enumerate(line) if char == '#' 
}

adjusted_galaxies = calculate_drift(galaxies, galaxy_drift)
print(calculate_distances(adjusted_galaxies))