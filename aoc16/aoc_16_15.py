discs = [(17, 15), (3, 2), (19, 4), (13, 2), (7, 2), (5, 0), (11, 0)]

max_ = 10000000
solutions = {idx+1: set(disc[0] * i - disc[1]-(idx+1) for i in range(0, (max_//disc[0])+1)) for idx, disc in enumerate(discs)}

#Day 1
answers = solutions[1] & solutions[2] & solutions[3] & solutions[4] & solutions[5] & solutions[6]
print(min(answers))

# Day 2
answers = answers & solutions[7]
print(min(answers))
