import re
import cProfile

with open('aoc_15_5.txt', 'r') as f:
    raw_input = f.read()

raw_input = raw_input.split("\n")
re_vowels = re.compile('[aeiou]')
re_duplicate = re.compile('(\\w)(\\1)')
re_non_overlapping = re.compile(r'(\w)(\w).*?\1\2')
re_aba = re.compile(r'(\w)\w\1')

def naughty_or_nice(string):
    vowels = re_vowels.findall(string)
    duplicate = re_duplicate.findall(string)
    if not len(vowels) >= 3: return False
    if not duplicate: return False
    if 'ab' in string or 'cd' in string or 'pq' in string or 'xy' in string:
        return False
    return True

def updated_non(string):
    non_overlapping = re_non_overlapping.findall(string)
    aba = re_aba.findall(string)
    if not non_overlapping or not aba: return False
    else: return True
    return True

def test_1():
    for i in range(100):
        count = 0
        for tekst in raw_input:
            if naughty_or_nice(tekst):
                count += 1

def test_2():
    for i in range(100):
        count = 0
        for tekst in raw_input:
            if updated_non(tekst):
                count += 1

count = 0
for tekst in raw_input:
    if naughty_or_nice(tekst):
        count += 1
print(count)
count = 0
for tekst in raw_input:
    if updated_non(tekst):
        count += 1
print(count)

# cProfile.run('test_1()')
# cProfile.run('test_2()')
