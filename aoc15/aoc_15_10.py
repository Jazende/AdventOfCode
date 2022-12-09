import cProfile

def expand(string_):
    new = ""
    idx = 0
    while True:
        start = string_[idx]
        count = 1
        while True:
            idx += 1
            if idx >= len(string_):
                break
            if string_[idx] == start:
                count += 1
            else:
                break
        new += str(count)
        new += start

        if idx >= len(string_):
            break
    return new

def expand_times(start, times):
    for i in range(times):
        start = expand(start)
    return len(start)

start = '1321131112'

cProfile.run('print(expand_times(start, 50))')

### --- ### --- ### --- ### --- ### --- ### --- ###

from itertools import groupby

def look_and_say(input_string, num_iterations):
    for i in range(num_iterations):
        input_string = ''.join([str(len(list(g))) + str(k) for k, g in groupby(input_string)])
    return input_string

cProfile.run('look_and_say("1321131112", 50)')