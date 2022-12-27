with open(r'22_06.txt', 'r') as f:
    raw_lines = f.read().strip()

idx = 0
four = raw_lines[idx:idx+4]
while True:
    if len(set(four)) == 4:
        break
    four = four[1:] + raw_lines[idx+4]
    idx += 1

print('Part 1:', idx+4)

fourteen = raw_lines[idx:idx+14]
while True:
    if len(set(fourteen)) == 14:
        break
    fourteen = fourteen[1:] + raw_lines[idx+14]
    idx += 1

print('Part 2:', idx+14)
