with open(r'aoc_19_06.txt', 'r') as f:
    raw_inputs = f.read()

def solutions(raw_inputs, day_two=False):
    orbits = [[x for x in x.split(')')] for x in raw_inputs.strip().split('\n')]

    chains = {}

    count = 0
    for orbit in orbits:
        cur_loc = orbit[1]
        chains[orbit[1]] = []
        while True:
            if cur_loc == "COM":
                break
            cur_loc = [orb for orb in orbits if orb[1] == cur_loc][0][0]
            chains[orbit[1]].append(cur_loc)
            count += 1
            if cur_loc in chains.keys():
                chains[orbit[1]] += chains[cur_loc]
                break

    count = sum([len(value) for key, value in chains.items()])

    if day_two:
        for jump in chains['YOU']:
            if jump in chains['SAN']:
                chain_length = chains['YOU'].index(jump) + chains['SAN'].index(jump)
                break
        return chain_length

    return count

print(solutions(raw_inputs))
print(solutions(raw_inputs, day_two=True))
