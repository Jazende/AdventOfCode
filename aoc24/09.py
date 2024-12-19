import os
import cProfile
with open(f'input_{os.path.basename(__file__).split(".")[0]}.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '''2333133121414131402'''

### Part 1 ###

def translate_input(raw_inputs):
    idx = 0
    file_counter = 0
    file = True
    result = []

    while True:
        if idx >= len(raw_inputs):
            break
        if file:
            for _ in range(int(raw_inputs[idx])):
                result.append(file_counter)
            file = False
            file_counter += 1
        else:
            for _ in range(int(raw_inputs[idx])):
                result.append(-1)
            file = True
        idx += 1
    return result

def defragment(inputs):
    while True:
        try:
            first_empty = inputs.index(-1)
        except ValueError:
            break # No more empty spaces -> fully defragged
        inputs[first_empty] = inputs.pop() # Default pops last item in list
        while True:
            if inputs[-1] == -1:
                inputs.pop()
            else:
                break
    return inputs

def checksum(inputs):
    return sum(value * idx for idx, value in enumerate(inputs))

print(checksum(defragment(translate_input(raw_inputs.strip()))))

### Part 2 ###

def translate_file(raw_inputs):
    total_file_length = len(raw_inputs)
    inputs = [] # nr, start, end, length (for ease of use)
    len_counter = 0
    file_counter = 0
    idx = 0
    empty = False
    while True:
        if idx >= total_file_length:
            break
        value = file_counter if not empty else -1
        length = int(raw_inputs[idx])
        inputs.append([value, len_counter, len_counter + length, length])
        file_counter += empty
        empty = [True, False][empty]
        len_counter += length
        idx += 1
    return inputs

def defrag(inputs):
    idx_1 = len(inputs)
    while True:
        idx_1 -= 1
        if idx_1 <= 0: break
        if inputs[idx_1][0] == -1: continue
        file_counter, start, end, length = inputs[idx_1]
        if file_counter == -1: continue
        for idx_2, inp in enumerate(inputs):
            if not inp[0] == -1: continue
            fc, s, e, l = inp
            if s > start: break
            if l >= length:
                inputs[idx_1][0] = -1
                inputs[idx_2] = [file_counter, s, s + length, length]
                if length < l:
                    inputs.insert(idx_2+1, [-1, s + length, s + length + (l - length), l - length])
                break
    return inputs

def checksum(inputs):
    sum_ = 0
    for file_counter, start, end, length in inputs:
        if file_counter == -1: continue
        for i in range(length):
            sum_ += (start + i) * file_counter
    return sum_

print(checksum(defrag(translate_file(raw_inputs.strip()))))
