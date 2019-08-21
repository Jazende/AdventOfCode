import random

input_test = ["0 <-> 2", "1 <-> 1", "2 <-> 0, 3, 4", "3 <-> 2, 4",
  "4 <-> 2, 3, 6", "5 <-> 6", "6 <-> 4, 5"]
input_ = []
dict_ = {}
list_ = []
with open("adventofcode_12.txt", "r") as f:
    for line in f:
        input_.append(line.replace("\n", ""))
for line in input_:
    temp_line = line.replace("\n","").replace(" <-> ",";").split(";")
    dict_[int(temp_line[0])] = [int(x) for x in temp_line[1].split(", ")]
    list_.append([int(x) for x in temp_line[1].split(", ")])

def check_connections_0_dict(input_):
    connections = [0]
    for point in input_[0]:
        connections.append(point)
    del input_[0]
    while True:
        check = 0
        changed = []
        for sleutel in input_.keys():
            if sleutel in connections:
                for point in input_[sleutel]:
                    connections.append(point)
                check += 1
                changed.append(sleutel)
        for x in changed:
            del input_[x]
        connections = sorted(list(set(connections)))
        if check == 0:
            break
    return connections

def check_connections_dict_start(input_, start_point=0):
    connections = [start_point]
    for point in input_[start_point]:
        connections.append(point)
    del input_[start_point]
    while True:
        check = 0
        changed = []
        for sleutel in input_.keys():
            if sleutel in connections:
                for point in input_[sleutel]:
                    connections.append(point)
                check += 1
                changed.append(sleutel)
        for x in changed:
            del input_[x]
        connections = sorted(list(set(connections)))
        if check == 0:
            break
    return connections, input_

def get_groups(input_):
    groups = 0
    while not len(input_) == 0:
        random_key = random.choice([x for x in dict_.keys()])
        items, input_ = check_connections_dict_start(dict_, random_key)
        groups += 1
    print(groups)
    return groups
        
#check_connections_dict_start(dict_, 0)
get_groups(dict_)
