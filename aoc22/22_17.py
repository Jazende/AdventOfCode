import time

with open(r'22_17.txt', 'r') as f:
    raw_lines = f.read().strip()

rock_formations = [
    [(2, 3), (3, 3), (4, 3), (5, 3)],           # - 
    [(2, 4), (3, 4), (4, 4), (3, 3), (3, 5)],   # +
    [(2, 3), (3, 3), (4, 3), (4, 4), (4, 5)],   # L reversed
    [(2, 3), (2, 4), (2, 5), (2, 6)],           # |
    [(2, 3), (3, 3), (2, 4), (3, 4)],           # block
]

def rock_generator(rocks):
    while True:
        for rock in rocks:
            yield rock

rocks = rock_generator(rock_formations)

while True:
    print(next(rocks))
    time.sleep(1)