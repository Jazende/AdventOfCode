from collections import Counter
with open('aoc_16_6.txt', 'r') as file:
    raw_input = file.read()

lines = raw_input.strip().split("\n")
for x in range(len(lines[0])):
    column_text = ""
    for line in lines:
        column_text += line[x]
    count = Counter(column_text)
    temp = sorted([[x, count[x]] for x in count], key=lambda x: x[1]*-1)
    print(temp[0][0], end="")

print("")
    
for x in range(len(lines[0])):
    column_text = ""
    for line in lines:
        column_text += line[x]
    count = Counter(column_text)
    temp = sorted([[x, count[x]] for x in count], key=lambda x: x[1])
    print(temp[0][0], end="")
