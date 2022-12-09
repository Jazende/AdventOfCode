def main(rotations=303, end_nr=2017):
    list_ = [0]
    cur_pos = 1
    for i in range(1, end_nr+1):
        new_pos = (cur_pos + rotations) % i
        list_.insert(new_pos+1, i)
        cur_pos = new_pos + 1
    print(list_[list_.index(0)], list_[list_.index(0)+1])

def after_0(rotations=303, end_nr=2017):
    cur_pos = 1
    value_after_0 = 0
    for i in range(1, end_nr+1):
        new_pos = (cur_pos + rotations) % i
        if new_pos == 0:
            value_after_0 = i
        cur_pos = new_pos + 1
    print(value_after_0)

import cProfile
cProfile.run("main(303, 2017)")
cProfile.run("after_0(303, 50000000)")
