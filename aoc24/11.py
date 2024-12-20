import os
with open(f'input_{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '''125 17'''
# raw_inputs = '''1'''

## Prepare Stone Cache
stone_cache = {}

def handle_stones(number_on_stone):
    if number_on_stone in stone_cache:
        return stone_cache[number_on_stone]

    text = str(number_on_stone)
    length = len(text)
    if number_on_stone == 0:
        result = (1, ) 
    elif length % 2 == 0:
        result = (int(text[:length // 2]), int(text[length // 2:]))
    else:
        result = number_on_stone * 2024, 
    stone_cache[number_on_stone] = result
    return result

raw_stones = [int(x) for x in raw_inputs.strip().split(' ')]

check_stones = [ i for i in range(10) ] + raw_stones
while True:
    if len(check_stones) == 0:
        break
    stone = check_stones.pop(0)
    if stone in stone_cache.keys():
        continue
    new_stones = handle_stones(stone)
    stone_cache[stone] = new_stones
    check_stones += new_stones

### Part 1 ### 

stones = { key: raw_stones.count(key) for key in stone_cache.keys() }

print(list((stone, amount) for stone, amount in stones.items() if amount > 0))

blinks_1 = 25
for i in range(blinks_1):
    new_stones = {}
    for stone, amount in stones.items():
        if amount == 0:
            continue
        if not stone in stone_cache:
            raise ValueError(f'{stone=} not in stonecache')
        for new_stone in stone_cache[stone]:
            if not new_stone in new_stones:
                new_stones[new_stone] = 0
            new_stones[new_stone] += amount
    stones = new_stones

print('total: ', sum(value for value in stones.values()))

### Part 2 ###

blinks_2 = 50
for i in range(blinks_2):
    new_stones = {}
    for stone, amount in stones.items():
        if amount == 0:
            continue
        if not stone in stone_cache:
            raise ValueError(f'{stone=} not in stonecache')
        for new_stone in stone_cache[stone]:
            if not new_stone in new_stones:
                new_stones[new_stone] = 0
            new_stones[new_stone] += amount
    stones = new_stones
    
print('total: ', sum(value for value in stones.values()))