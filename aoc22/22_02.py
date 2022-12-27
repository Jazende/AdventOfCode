with open(r'22_02.txt', 'r') as f:
    raw_lines = f.read().strip()

translate_code = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper', 
    'Z': 'scissors',
}

def play_play_to_score(their, yours):
    match their, yours:
        case 'rock', 'rock':
            return 1 + 3
        case 'rock', 'paper':
            return 2 + 6
        case 'rock', 'scissors':
            return 3 + 0
        case 'paper', 'rock':
            return 1 + 0
        case 'paper', 'paper':
            return 2 + 3
        case 'paper', 'scissors':
            return 3 + 6
        case 'scissors', 'rock':
            return 1 + 6
        case 'scissors', 'paper':
            return 2 + 0
        case 'scissors', 'scissors':
            return 3 + 3

def play_result_to_play(their, result):
    # select what to play: X lose, Y draw, Z win
    match their, result:
        case 'rock', 'X':
            return 'scissors'
        case 'rock', 'Y':
            return 'rock'
        case 'rock', 'Z':
            return 'paper'
        case 'paper', 'X':
            return 'rock'
        case 'paper', 'Y':
            return 'paper'
        case 'paper', 'Z':
            return 'scissors'
        case 'scissors', 'X':
            return 'paper'
        case 'scissors', 'Y':
            return 'scissors'
        case 'scissors', 'Z':
            return 'rock'

def rps_one(first, second):
    # rock = 1, paper = 2, scissors = 3
    # loss = 0, draw = 3, win = 6
    enemy = translate_code[first]
    s_elf = translate_code[second]
    score = play_play_to_score(enemy, s_elf)
    return score

scores = [rps_one(*line.split(' ')) for line in raw_lines.split('\n')]
print('Part 1:', sum(scores))

def rps_two(their, result_to_get):
    enemy = translate_code[their]
    what_to_play = play_result_to_play(enemy, result_to_get)
    score = play_play_to_score(enemy, what_to_play)
    return score

adj_scores = [rps_two(*line.split(' ')) for line in raw_lines.split('\n')]
print('Part 2:', sum(adj_scores))
