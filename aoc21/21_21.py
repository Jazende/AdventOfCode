with open(r'input_21.txt', 'r') as f:
    raw_input = f.read()

def die(up_to):
    x = 1
    while True:
        yield x
        x += 1
        if x == 101:
            x == 1
    return 

player_one = {'pos': 9, 'score': 0, 'player': 1}
player_two = {'pos': 4, 'score': 0, 'player': 2}

die_rolls = die(100)

count = 0
while True:
    player_one['pos'] = (player_one['pos'] + next(die_rolls) + next(die_rolls) + next(die_rolls))
    count += 3
    while player_one['pos'] > 10:
        player_one['pos'] -= 10
    player_one['score'] += player_one['pos']
    if player_one['score'] >= 1000:
        break
    player_two['pos'] = (player_two['pos'] + next(die_rolls) + next(die_rolls) + next(die_rolls))
    count += 3
    while player_two['pos'] > 10:
        player_two['pos'] -= 10
    player_two['score'] += player_two['pos']
    if player_two['score'] >= 1000:
        break

print(player_one, player_two)
print(player_one['score'] * count, player_two['score'] * count)