from collections import Counter
from itertools import product
from functools import lru_cache

with open('input_07.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '''32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483'''

########################## DAY 7 PART 1 ########################## 

raw_hands = raw_inputs.strip().split('\n')
card_values = { 'A': 14, 'T': 10, 'J': 11, 'Q': 12, 'K': 13 }

def card_value(card):
    if card in card_values:
        return card_values[card]
    return int(card)

def hands_value(raw_data):
    hand, bet = raw_data

    counter = Counter(hand)
    values = [x for x in counter.values()]

    value = 1
    value_name = ""
    
    if 5 in values:
        value = 7
        value_name = "5 of a kind"
    elif 4 in values:
        value = 6
        value_name = "4 of a kind"
    elif 3 in values:
        if 2 in values:
            value = 5
            value_name = "Full house"
        else:
            value = 4
            value_name = "3 of a kind"
    elif values.count(2) == 2:
        value = 3
        value_name = "Double Pair"
    elif values.count(2) == 1:
        value = 2
        value_name = "Pair"
    else:
        value = 1
        value_name = "High Card"

    return value, card_value(hand[0]), card_value(hand[1]), card_value(hand[2]), card_value(hand[3]), card_value(hand[4])

hands = [raw_hand.strip().split(' ') for raw_hand in raw_hands]
hands.sort(key=hands_value)

total_score = 0
hand_score = 1
for hand in hands:
    bid = int(hand[1])
    total_score += hand_score * bid
    hand_score += 1 
print(total_score)


########################## DAY 7 PART 2 ########################## 

raw_hands = raw_inputs.strip().split('\n')
card_values = { 'A': 14, 'T': 10, 'J': 1, 'Q': 12, 'K': 13 }

def hands_value(hand):
    counter = Counter(hand)
    values = [x for x in counter.values()]


    value = 1
    value_name = ""
    
    if 5 in values:
        value = 7
        value_name = "5 of a kind"
    elif 4 in values:
        value = 6
        value_name = "4 of a kind"
    elif 3 in values:
        if 2 in values:
            value = 5
            value_name = "Full house"
        else:
            value = 4
            value_name = "3 of a kind"
    elif values.count(2) == 2:
        value = 3
        value_name = "Double Pair"
    elif values.count(2) == 1:
        value = 2
        value_name = "Pair"
    else:
        value = 1
        value_name = "High Card"

    return value, card_value(hand[0]), card_value(hand[1]), card_value(hand[2]), card_value(hand[3]), card_value(hand[4])

@lru_cache()
def parse_hands(raw_data):
    hand, bet = raw_data
    jokers = hand.count("J")
    other_letters = "".join(char for char in hand if not char == 'J')

    if jokers == 0:
        return hands_value(hand)
    elif jokers == 5:
        return 7, 1, 1, 1, 1, 1
    else:
        max_value = 0, 0, 0, 0, 0, 0
        for other_letter in other_letters:
            new_hand = "".join(x for x in hand) 
            new_hand = new_hand.replace("J", other_letter, 1)
            
            parsed_value = parse_hands((new_hand, bet))
            if parsed_value > max_value:
                max_value = parsed_value

        return max_value[0], card_value(hand[0]), card_value(hand[1]), card_value(hand[2]), card_value(hand[3]), card_value(hand[4])

    return 0, 0, 0, 0, 0, 0

hands = [raw_hand.strip().split(' ') for raw_hand in raw_hands]
hands.sort(key=lambda x: parse_hands(tuple(x)))

total_score = 0
hand_score = 1
for hand in hands:
    bid = int(hand[1])
    total_score += hand_score * bid
    hand_score += 1 
print(total_score)
