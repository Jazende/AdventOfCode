import os
with open(f'input_{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '''7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9'''

### Part 1 ###

raw_lines = raw_inputs.strip().split('\n')
lines = [ [int(x) for x in line.split(' ')] for line in raw_lines ]

def check_line(line):
    if not ( all(line[idx] > line[idx+1] for idx in range(len(line)-1)) or 
        all(line[idx] < line[idx+1] for idx in range(len(line)-1)) ):
        return False
    if not ( all( 0 < abs(line[idx] - line[idx+1]) < 4 for idx in range(len(line)-1) ) ):
        return False
    return True

safe_lines = sum( check_line(line) for line in lines )
print(safe_lines)

### part 2 ###

def double_check(line):
    if check_line(line) == True:
        return True
    for skip in range(len(line)):
        new_line = [ nr for idx, nr in enumerate(line) if not idx == skip ]
        if check_line(new_line):
            return True
    return False

safe_lines = sum( double_check(line) for line in lines )
print(safe_lines)