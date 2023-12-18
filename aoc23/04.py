import re

with open('input_04.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''

lines = raw_inputs.strip().split('\n')
re_card_info = re.compile('Card\s+(?P<raw_card_nr>\d+)\:\s+(?P<raw_winning_nrs>[\d\s]+)\s+\|\s+(?P<raw_chosen_nrs>[\d\s]+)$')

cards = {}
for line in lines:
    info = re_card_info.match(line).groupdict()
    card_nr = int(info['raw_card_nr'])
    winning_nrs = [int(x.strip()) for x in info['raw_winning_nrs'].replace('  ', ' ').split(' ')]
    chosen_nrs = [int(x.strip()) for x in info['raw_chosen_nrs'].replace('  ', ' ').split(' ')]
    correct_nrs = sum(1 for card in chosen_nrs if card in winning_nrs)
    cards[card_nr] = { 'winning_nrs': winning_nrs, 'chosen_nrs': chosen_nrs, 'correct_nrs': correct_nrs }

########################## DAY 4 PART 1 ########################## 

score = 0
for card in cards:
    count = sum(1 for nr in cards[card]['chosen_nrs'] if nr in cards[card]['winning_nrs'])
    score += 2 ** (count - 1) if count > 0 else 0

print(score)

########################## DAY 4 PART 2 ########################## 

have_cards = [1 for x in range(len(cards))]

for x in range(1, len(have_cards) + 1):
    print(f'{x=} -> {have_cards[x:min(x+20, len(have_cards))]}')
    for y in range(cards[x]['correct_nrs']):
        have_cards[x + y] += have_cards[x-1]

print(sum(have_cards))
print(have_cards)