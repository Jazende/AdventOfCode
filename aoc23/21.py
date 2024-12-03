with open('input_21.txt', 'r') as f:
    raw_inputs = f.read()

raw_inputs = '''...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........'''

garden = { (row, col): char for row, line in enumerate(raw_inputs.strip().split('\n')) for col, char in enumerate(line) }

print(garden)

########################## DAY 21 PREP 0 ########################## 

########################## DAY 22 PART 1 ########################## 

########################## DAY 23 PART 2 ########################## 
