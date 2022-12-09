from collections import Counter

with open(r'input_08.txt') as f:
    raw_inputs = f.read().strip()

# raw_inputs = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
# fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''

# raw_inputs = '''acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'''

lines = [line for line in raw_inputs.split('\n')]

numbers = [set('abcefg'), set('cf'), set('acdeg'), set('acdfg'), set('bcdf'), 
    set('abdfg'), set('abdefg'), set('acf'), set('abcdfeg'), set('abcdfg')]

sum_ = 0
count = 0
for line in lines:
    left, right = line.split(' | ')

    # Day 1    
    count += sum(1 for part in right.strip().split(' ') if len(part) in [2, 3, 4, 7])

    # Day 2
    left_parts = left.split(' ')
    translations =  {}
    counter = Counter(left)
    del counter[' ']
    del counter['|']

    # prep
    two_length_part = set(*[part for part in left_parts if len(part) == 2])
    three_length_part = set(*[part for part in left_parts if len(part) == 3])
    four_length_part = set(*[part for part in left_parts if len(part) == 4])
    shows_up_4_times = [k for k, v in counter.items() if v == 4]
    shows_up_6_times = [k for k, v in counter.items() if v == 6]
    shows_up_9_times = [k for k, v in counter.items() if v == 9]

    # in expected answers, e shows up 4 times overall, b 6, d and g 7, a and c 8, f 9 times
    translations[shows_up_4_times[0]] = 'e'
    translations[shows_up_6_times[0]] = 'b'
    translations[shows_up_9_times[0]] = 'f'

    # len 2 (cf) - f = c
    f = set(*shows_up_9_times)
    c = list(two_length_part - f)[0]
    translations[c] = 'c'

    # len 3 (acf) - len 2 (cf) = a
    a = list(three_length_part - two_length_part)[0]
    translations[a] = 'a'

    # len 4 (bcdf) - len 2 (cf) - b = d
    b = set(*shows_up_6_times)
    d = list(four_length_part - two_length_part - b)[0]
    translations[d] = 'd'
    
    full_set = set('abcdefg')
    current_keys = set(translations.keys())
    current_values = set(translations.values())
    
    last_key = full_set - current_keys
    last_value = full_set - current_values

    translations[list(last_key)[0]] = list(last_value)[0]

    # Translate right, changed to normal numbers
    # for part in right.split(' '):
    #     normal = set(translations[x] for x in part)
    #     normal_number = numbers.index(normal)
    sum_ += int("".join(str(numbers.index(set(translations[x] for x in part))) for part in right.split(' ')))
    # break

print('Day 1: ', count)
print('Day 2: ', sum_)