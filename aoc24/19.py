import os
import time
import copy
from functools import cache
with open(f'input_{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '''r, wr, b, g, bwu, rb, gb, br

# brwrr
# bggr
# gbbr
# rrbgbr
# ubwu
# bwurrg
# brgr
# bbrgwb'''

raw_towels, raw_designs = raw_inputs.strip().split('\n\n')
towels = raw_towels.strip().split(', ')
designs = raw_designs.strip().split('\n')


### Part 1 ###

@cache
def design_tester(design, design_so_far=None):
    if design_so_far is None:
        design_so_far = ''
    if design in towels:
        return True
    fitting_towels = [towel for towel in towels if design.startswith(towel)]
    if len(fitting_towels) == 0:
        return False
    else:
        for towel in fitting_towels:
            shortened_design = design[len(towel):]
            if succes := design_tester(shortened_design, design_so_far=f'{design_so_far}{towel}'):
                return succes
        return False

print(sum(1 for design in designs if design_tester(design)), '\n')

### Part 2 ###

@cache
def design_tester_all(design):
    if design == '':
        return 1
    fitting_towels = [towel for towel in towels if design.startswith(towel)]
    if len(fitting_towels) == 0:
        return 0
    else:
        sum_ = 0
        for towel in fitting_towels:
            shortened_design = design[len(towel):]
            sum_ += design_tester_all(shortened_design)
        return sum_

print(sum(design_tester_all(design) for design in designs))