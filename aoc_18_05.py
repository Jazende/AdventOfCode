import re
from collections import Counter

with open(r'aoc_18_05.txt', 'r') as f:
    raw_input = f.read()

text = raw_input.strip()

def day_1(text):
    l = len(text)  
    while True:
        for letter in "abcdefghijklomnopqrstuvwxyz":
            text = re.sub(f"{letter}{letter.upper()}", "", text)
            text = re.sub(f"{letter.upper()}{letter}", "", text)
        new_len = len(text)
        if new_len == l:
            return l
        l = new_len

print(day_1(text))

def day_2(text):
    c = Counter(text)
    letters = set()
    for key in c:
        letters.add(key.lower())
    letters = {x: day_1(text.replace(x, "").replace(x.upper(), "")) for x in letters}
    resp = [(key, value) for key, value in letters.items()]
    resp = sorted(resp, key=lambda x: x[1])
    return resp[0][1]

print(day_2(text))
    
