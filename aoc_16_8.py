with open("aoc_16_8.txt", 'r') as file:
    raw_input = file.read()
    
instructions = raw_input.split("\n")

max_ = 50
min_ = 6

keypad = [[" " for _ in range(max_)] for _ in range(6)]

def print_keypad(keypad):
    print("/" + "-"*max_ + "\\")
    for row in keypad:
        print("|" + "".join([x for x in row]) + "|")
    print("\\" + "-"*max_ + "/")


for instruction in instructions:
    if instruction.startswith('rect'):
        command = instruction[5:]
        x, y = command.split("x")
        for i in range(int(x)):
            for j in range(int(y)):
                keypad[j][i] = "#"
    elif instruction.startswith('rotate column'):
        command = instruction[16:]
        column, amount = command.split(" by ")
        column = int(column)
        amount = int(amount)
        cur_line = [row[column] for row in keypad]
        new_line = cur_line[min_-amount:min_] + cur_line[0:min_]
        for x in range(min_):
            keypad[x][column] = new_line[x]
    elif instruction.startswith('rotate row'):
        command = instruction[13:]
        row, amount = command.split(" by ")
        row = int(row)
        amount = int(amount)
        keypad[row] = keypad[row][max_-amount:max_] + keypad[row][0:max_-amount]
print_keypad(keypad)

count = 0
for row in keypad:
    for index in row:
        if index == "#":
            count += 1
print(count)
