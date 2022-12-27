with open(r'22_04.txt', 'r') as f:
    raw_lines = f.read().strip()

assignments = [(*line.split(',')[0].split('-'), *line.split(',')[1].split('-')) for line in raw_lines.split('\n')]

def intify(assignment):
    assignment = [int(x) for x in assignment]
    return assignment

def encompasses(assignment):
    if (assignment[0] <= assignment[2] and assignment[1] >= assignment[3]) or (assignment[2] <= assignment[0] and assignment[3] >= assignment[1]):
        return True
    return False

print('Part 1:', sum(1 if encompasses(intify(assignment)) else 0 for assignment in assignments))

def overlaps(assignment):
    if (assignment[2] <= assignment[0] <= assignment[3]) or \
        (assignment[2] <= assignment[1] <= assignment[3]) or \
        (assignment[0] <= assignment[2] <= assignment[1]) or \
        (assignment[0] <= assignment[3] <= assignment[1]):
        return True
    return False

print('Part 2:', sum(1 if overlaps(intify(assignment)) else 0 for assignment in assignments))
