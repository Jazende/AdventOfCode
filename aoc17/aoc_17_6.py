day_6_input = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6]
day_6_test = [0, 2, 7, 0]

from time import sleep

def balance_blocks(input_, print_ = False):
    lists_seen = []
    cur_list = []+input_
    while True:
        if print_:
            print(cur_list)
        lists_seen.append([]+cur_list)
        max_index = cur_list.index(max(cur_list))
        max_value = cur_list[max_index]
        cur_list[max_index] = 0
        for i in range(max_value):
            cur_list[(i + max_index + 1)%len(cur_list)] += 1
        if cur_list in lists_seen:
            print("bonus: ", len(lists_seen) - lists_seen.index(cur_list))
            break
    if print_:
        print(cur_list)
    print(len(lists_seen))
    return lists_seen

def chain(input_):
    list_ = balance_blocks(input_)
    il = iter(list_[::-1])
    while True:
        print(next(il))
        sleep(0.3)

##def bbiter(input_):
##    cur_list = input_
##    while True:
##        max_index = cur_list.index(max(cur_list))
##        max_value = cur_list[max_index]
##        cur_list[max_index] = 0
##        for i in range(max_value):
##            cur_list[(i + max_index + 1)%len(cur_list)] += 1
##        yield cur_list
##
##def inf_chain(input_):
##    norm_length = balance_blocks(input_)
##    iter_ = bbiter(input_)
##    lists = []
##    for i in range(norm_length+1):
##        lists.append(next(iter_))
##    l = len(lists)
##    for i in range(1, len(lists)):
##        if lists[l-i:] == lists[l-i-i: l-i]:
##            print(l-i-i)
##            break

if __name__ == '__main__':
    balance_blocks(day_6_input)
