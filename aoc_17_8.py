import re

def input_(test):
    test_input = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""
    lines = []
    if test == True:
        for line in test_input.split("\n"):
            lines.append(line)
    elif test == False:
        with open("adventofcode_8.txt", 'r') as f:
            for inc in f:
                lines.append(inc.strip())
    return lines

def handle(test):
    lines = input_(test)
    inputs = []
    list_ = {}
    max_ = 0
    for line in lines:
        x = re.findall('(\w{1,5}) (inc|dec) (-?\d{1,5}) if (\w{1,5}) ([>=<!]+) (-?\d{1,5})', line)[0]
        inputs.append([x[0], x[1], int(x[2]), x[3], x[4], int(x[5])])
        if not x[0] in list_.keys():
            list_[x[0]] = 0
    for line in inputs:
        eval_ = evaluate(list_, line[3], line[4], line[5])
        if eval_:
            if line[1] == "inc":
                list_[line[0]] += int(line[2])
            elif line[1] == "dec":
                list_[line[0]] -= line[2]
            else:
                raise ValueError("Operation {} not designated.".format(line[1]))
        cur_max = list_[sorted(list_, key= lambda y: list_[y], reverse=True)[0]]
        if cur_max > max_:
            max_ = cur_max
    print(max_)
    max_ = sorted(list_, key= lambda x: list_[x], reverse=True)[0]
    print(list_[max_])
    return list_

def evaluate(list_, variable, operator, value):
    if not variable in list_.keys():
        list_[variable] = 0
    if operator == "==":
        return list_[variable] == value
    elif operator == ">=":
        return list_[variable] >= value
    elif operator == "<=":
        return list_[variable] <= value
    elif operator == ">":
        return list_[variable] > value
    elif operator == "<":
        return list_[variable] < value
    elif operator == "!=":
        return list_[variable] != value
    else:
        raise ValueError("Operator {} not designated.".format(operator))
    
print(handle(False))
