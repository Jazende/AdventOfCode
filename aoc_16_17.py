import hashlib
import cProfile

def get_md5(data):
    return hashlib.md5(data.encode()).hexdigest()

def get_open_doors(text):
    first_four = get_md5(text)[:4]
    open_doors = "".join([door[1] for door in list(zip(first_four, 'UDLR')) if door[0] in 'bcdef'])
    return open_doors

def is_valid(path):
    x = 0
    y = 0
    for char in path:
        if char == "D":
            x += 1
            if x > 3:
                return False
        if char == "U":
            x -= 1
            if x < 0:
                return False
        if char == "L":
            y -= 1
            if y < 0:
                return False
        if char == "R":
            y += 1
            if y > 3:
                return False

    return True

def is_solution(path):
    x = 0
    y = 0
    for char in path:
        if char == "D":
            x += 1
        if char == "U":
            x -= 1
        if char == "L":
            y -= 1
        if char == "R":
            y += 1
    
    if x == 3 and y == 3:
        return True
    return False

def get_path(text, log=False, day=1):
    paths = [text]
    index = 0
    longest_path = 0
    while True:
        current_path = paths[index]
        if log:
            print("Current Path:", current_path)

        if is_solution(current_path):
            if day==1:
                return current_path
            elif day==2:
                longest_path = max(len(current_path), longest_path)
            # break
        else:
            paths += [current_path + door for door in get_open_doors(current_path) if is_valid(current_path+door)]
            # open_doors = get_open_doors(current_path)
            # for door in open_doors:
            #     new_path = current_path + door
            #     if is_valid(new_path):
            #         paths.append(new_path)

        index += 1
        if index == len(paths):
            break
    if day==2:
        return longest_path - len(text)

print(get_path('ihgpwlah'))
print(get_path('kglvqrro'))
print(get_path('ulqzkmiv'))
print(get_path('qljzarfv'))

print(get_path('ihgpwlah', day=2))
print(get_path('kglvqrro', day=2))
print(get_path('ulqzkmiv', day=2))
print(get_path('qljzarfv', day=2))

# cProfile.run("get_path('qljzarfv', day=2)")