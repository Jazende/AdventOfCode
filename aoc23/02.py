import re
re_game_id = re.compile('Game (\d+)\:(.*)$')
re_game_data = re.compile('(\d+)\s([red|green|blue]+)')

with open('input_02.txt') as f:
    lines = f.readlines()

########################## DAY 2 PART 1 ########################## 

max_checks = { 'red': 12, 'green': 13, 'blue': 14 }

def grabbed_too_many(input, checks):
    if int(input[0]) > checks[input[1]]:
        return True
    return False

sum_ = 0
for each in lines:
    game_id, rest = re_game_id.match(each).groups()
    game_data = re_game_data.findall(rest)
    if any(grabbed_too_many(data, max_checks) for data in game_data):
        continue
    sum_ += int(game_id)
print(sum_)

########################## DAY 2 PART 1 ########################## 

def game_power(inputs):
    d = { 'red': 0, 'green': 0, 'blue': 0 }
    for inp in inputs:
        d[inp[1]] = max(d[inp[1]], int(inp[0]))
    return d['red'] * d['green'] * d['blue']

sum_ = 0
for each in lines:
    game_id, rest = re_game_id.match(each).groups()
    game_data = re_game_data.findall(rest)
    sum_ += game_power(game_data)
print(sum_)
    

