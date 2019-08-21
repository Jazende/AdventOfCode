import re
import json

with open(r'aoc_15_12.txt', 'r') as f:
    print(sum([int(x) for x in re.findall('(\-?[0-9]+)', f.read().strip())]))

def traverse_dict(dictionary):
    sum_ = 0
    for key, value in dictionary.items():
        if type(value) == int:
            sum_ += value
        elif type(value) == list:
            sum_ += traverse_list(value)
        elif type(value) == dict:
            sum_ += traverse_dict(value)
        elif type(value) == str and value == "red":
            return 0
        elif type(value) == str:
            pass
        else:
            print("Not captured: ", type(value))
    return sum_

def traverse_list(list_):
    sum_ = 0
    for item in list_:
        if type(item) == int:
            sum_ += item
        elif type(item) == str:
            pass
        elif type(item) == dict:
            sum_ += traverse_dict(item)
        elif type(item) == list:
            sum_ += traverse_list(item)
        else:
            print("Not captured: ", type(item))
    return sum_

with open(r'aoc_15_12.txt', 'r') as f:
    print(traverse_dict(json.loads(f.read().strip())))
