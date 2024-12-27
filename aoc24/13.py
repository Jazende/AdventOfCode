import os
import re
with open(f'input_{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '''Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176

# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450

# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279'''

### Part 1 & 2 ###

re_inputs_a = re.compile('Button A.*X\+(\d+), Y\+(\d+)')
re_inputs_b = re.compile('Button B.*X\+(\d+), Y\+(\d+)')
re_inputs_prize = re.compile('Prize.*X\=(\d+), Y\=(\d+)')
results_a = re_inputs_a.findall(raw_inputs.strip())
results_b = re_inputs_b.findall(raw_inputs.strip())
results_prize = re_inputs_prize.findall(raw_inputs.strip())

prizes_1 = []
prizes_2
for i in range(len(results_a)):
    x_1 = int(results_a[i][0])
    x_2 = int(results_b[i][0])
    y_1 = int(results_a[i][1])
    y_2 = int(results_b[i][1])
    r_x = int(results_prize[i][0])
    r_y = int(results_prize[i][1])

    if not ((x_1 * r_y) - (y_1 * r_x)) % ((x_1 * y_2) - (y_1 * x_2)) == 0:
        continue

    b_presses = ((x_1 * r_y) - (y_1 * r_x)) / ((x_1 * y_2) - (y_1 * x_2))

    if not (r_x - (b_presses * x_2)) % x_1 == 0:
        continue

    a_presses = (r_x - (b_presses * x_2)) / x_1

    if a_presses <= 100 and b_presses <= 100:
        prizes_1.append(int(a_presses)*3 + int(b_presses))

print(sum(prizes))

### Part 2 ###

prizes = []
for i in range(len(results_a)):
    x_1 = int(results_a[i][0])
    x_2 = int(results_b[i][0])
    y_1 = int(results_a[i][1])
    y_2 = int(results_b[i][1])
    r_x = int(results_prize[i][0]) + 10000000000000
    r_y = int(results_prize[i][1]) + 10000000000000

    if not ((x_1 * r_y) - (y_1 * r_x)) % ((x_1 * y_2) - (y_1 * x_2)) == 0:
        continue

    b_presses = ((x_1 * r_y) - (y_1 * r_x)) / ((x_1 * y_2) - (y_1 * x_2))

    if not (r_x - (b_presses * x_2)) % x_1 == 0:
        continue

    a_presses = (r_x - (b_presses * x_2)) / x_1

    prizes.append(int(a_presses)*3 + int(b_presses))

print(sum(prizes))
