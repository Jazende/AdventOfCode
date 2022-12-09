import load_jaz_funcs
from functools import reduce
from jaz_funcs import *

@print_result
def run_single_knot_hash(list_size, lengths):
    list_ = [x for x in range(list_size+1)]
    cur_pos = 0
    skipsize = 0
    for length in lengths:
        selection = []
        for x in range(length):
            selection.insert(0, list_[(cur_pos+x)%(list_size+1)])
        for x in range(length):
            list_[(cur_pos+x)%(list_size+1)] = selection[x]
        cur_pos = (cur_pos + length + skipsize) % (list_size+1)
        skipsize += 1
    return list_[0] * list_[1]

def convert_char_to_ascii(input_):
    return ord(input_)

def convert_list_to_input(input_, first=False):
    result = []
    for x in input_:
        result.append(convert_char_to_ascii(x))
    if first:
        result += [17, 31, 73, 47, 23]
    return result

def knot_hash(list_size, input_, list_=None, cur_pos=0,
              skipsize=0, round_=0, max_rounds=1):
    if list_ == None:
        list_ = [x for x in range(list_size)]
    if type(input_) == str:
        if round_ == 0:
            lengths = convert_list_to_input(input_, first=True)
        else:
            lengths = convert_list_to_input(input_)
    else:
        lengths = input_
    for length in lengths:
        selection = []
        for x in range(length):
            selection.insert(0, list_[(cur_pos+x)%(list_size)])
        for x in range(length):
            list_[(cur_pos+x)%(list_size)] = selection[x]
        cur_pos = (cur_pos + length + skipsize) % (list_size)
        skipsize += 1
    round_ += 1
    if round_ == max_rounds:
        return list_size, lengths, list_, cur_pos, skipsize
    else:
        return knot_hash(list_size, lengths, list_, cur_pos, skipsize,
                         round_, max_rounds)

def dense_hash(list_):
    hash_ = lambda x, y: x ^ y
    res_dense_hash = []
    for x in range(len(list_[::16])):
        res_dense_hash.append(reduce(hash_, list_[16*x:16*(x+1)]))
    return res_dense_hash

def hexadecimel_repr(input_):
    hexa = ""
    for x in input_:
        double = format(x, '0>8b')
        left = hex(int(double[0:4], 2))
        right = hex(int(double[4:], 2))
        hexa += left[2:]+ right[2:]
    return hexa

# @print_result
def full_hash(input_, rounds):
    _, _, list_, _, _ = knot_hash(256, input_, max_rounds=rounds)
    dense = dense_hash(list_)
    return hexadecimel_repr(dense)

if __name__ == "__main__":
    # run_single_knot_hash(4, [3, 4, 1, 5])
    run_single_knot_hash(255, [165, 1, 255, 31, 87, 52, 24, 113, 0, 91, 148, 254, 158, 2, 73, 153])

    full_hash("165,1,255,31,87,52,24,113,0,91,148,254,158,2,73,153", 64)
