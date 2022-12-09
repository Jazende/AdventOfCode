import re
with open(r'input_04.txt', 'r') as f:
    raw_input = f.read()

# raw_input = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7'''

def print_board(board):
    for idx, val in enumerate(board):
        if idx % 5 == 0:
            print('\n', end=" ")
        if val == -1:
            print('__', end=" ")
        else:
            print(f'{val:>2}', end=" ")

def check_board(board):
    for row in range(5):
        full_row = True
        for cell in range(5):
            if not board[cell+(row*5)] == -1:
                full_row = False
                break
        if full_row:
            return True
            
    for col in range(5):
        full_col = True
        for cell in range(5):
            if not board[col+(cell*5)] == -1:
                full_col = False
                break
        if full_col:
            return True
    
    return False

values, *boards = raw_input.split('\n\n')
values = [int(x) for x in values.split(',')]
boards = [[int(x) for x in re.findall('\d+', board)] for board in boards]

winning_board = None
winning_value = None
check_winning_board = True
check_boards = [True for board in boards]

for value in values:
    for idx, board in enumerate(boards):
        if not check_boards[idx]:
            continue 

        try:
            loc = board.index(value)
        except ValueError:
            pass
        else:
            board[loc] = -1

        if check_board(board):
            if sum([int(check) for check in check_boards]) == 1:
                score = sum(x for x in board if not x == -1) * value
                print("Day 2:", score)
            check_boards[idx] = False
            if check_winning_board:
                score = sum(x for x in board if not x == -1) * value
                print('Day 1:', score)
                check_winning_board = False
