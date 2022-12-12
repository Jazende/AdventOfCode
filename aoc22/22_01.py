with open(r'22_01.txt', 'r') as f:
    raw_lines = f.read().strip()

elves = [sum(int(x) for x in elf.split('\n')) for elf in raw_lines.split('\n\n')]
print(max(elves))

elves.sort()
print(sum(elves[-3:]))