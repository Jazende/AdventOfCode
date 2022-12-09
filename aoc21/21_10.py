with open(r'input_10.txt', 'r') as f:
    raw_inputs = f.read().strip()

# raw_inputs = '''[({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]'''

inputs = [x for x in raw_inputs.split('\n')]
openers = ["(", "[", "{", "<"]
closers = [")", "]", "}", ">"]
day_1_scores = {')': 3, ']': 57, '}': 1197, '>': 25137, None: 0}
day_2_scores = {'(': 1, '[': 2, '{': 3, '<': 4}

def parse(line):
    opened = []
    for char in line:
        if char in openers:
            opened.append(char)
        elif char in closers:
            if closers.index(char) == openers.index(opened[-1]):
                opened.pop(-1)
            else:
                return 'corrupt', char
    return 'incomplete', opened

# for line in inputs:
#     result, score = parse(line)
#     if result == 'corrupt':
#         print(result, score, scores[score])

score = sum(day_1_scores[parse(line)[1]] for line in inputs if parse(line)[0] == 'corrupt')
print('Day 1:', score)

day_2_results = []
for line in inputs:
    status, result = parse(line)
    if status == 'corrupt':
        continue
    score = 0
    for char in result[::-1]:
        score *= 5
        score += day_2_scores[char]
    day_2_results.append(score)
day_2_results.sort()
print('Day 2:', day_2_results[len(day_2_results)//2])