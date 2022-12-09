from collections import Counter

with open(r'input_14.txt', 'r') as f:
    raw_inputs = f.read().strip()

# raw_inputs = '''NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C'''

start, raw_transforms = raw_inputs.split('\n\n')

# All pairs in a dict with counter
temp_parts = [start[i:i+2] for i in range(len(start)-1)]
parts = dict(Counter(temp_parts))
# All pairs and their results
temp_transforms = [part.split(' -> ') for part in raw_transforms.split('\n')]
transforms = {tf[0]: [tf[0][0] + tf[1],  tf[1] + tf[0][1]] for tf in temp_transforms}
# On each transform, all are counted double except first and last.
# In the end, count all letters, add first and last letter, and divide by two.
    #                  NCN, NBC -> NCNBC -> 2x N, 2x C, 1x B
    # NNC -> NN, NC -> NC + CN, NB + BC  -> 3x N, 3x C, 2x B
    #                                       3x N, 3x C, 2x B + start + end -> 4x N, 4x C, 2x B / 2 =>
    #                                       2x N, 2x C, 1x B
    #
    # Even with multiple steps:
    # NNC -> NN, NC -> NC + CN, NB + BC -> NCN, NBC -> NCNBC
    # NCNBC -> NC, CN, NB, BC -> NB BC, CC CN, NB BB, BB BC -> NBC, CCN, NBB, BBC -> NBCCNBBBC
    #                            \                                                            \-> 2x N, 4x B, 3x C
    #                             \-> 3x N, 8x B, 5x C | + 1x N, 1x C -> 4x N, 8x B, 6x C | /2 -> 2x N, 4x B, 3x C

def day_results(day, parts):
    letters = {start[0]: 1, start[-1]: 1}
    for part, count in parts.items():
        for letter in part:
            if not letter in letters:
                letters[letter] = 0
            letters[letter] += count
    for letter in letters:
        letters[letter] //= 2

    print(f'Day {day}: {max(letters.values()) - min(letters.values())}')


for step in range(40):
    new_parts = {key: 0 for key in transforms.keys()}
    for part, count in parts.items():
        if part in transforms:
            new_parts[transforms[part][0]] += count
            new_parts[transforms[part][1]] += count
        else:
            new_parts[part] += count
    parts = new_parts

    if step == 9:
        day_results(1, parts)
    if step == 39:
        day_results(2, parts)
