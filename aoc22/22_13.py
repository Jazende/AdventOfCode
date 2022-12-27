with open(r'22_13.txt', 'r') as f:
    raw_lines = f.read().strip()

raw_pairs = [line.split('\n') for line in raw_lines.split('\n\n')]

def parse_inputs(text):
    result = []
    temp = ''

    idx = 0
    while True:
        if len(text) == idx:
            break
        match text[idx]:
            case '[':
                matching_close = text.find(']', idx)
                returned = parse_inputs(text[idx+1:matching_close+1])
                result.append(returned)
                idx = matching_close
            case ',' | ']':
                try:
                    int(temp)
                except:
                    pass
                else:
                    result.append(int(temp))
                finally:
                    temp = ''
            case char:
                temp += char
        idx += 1
    return result

pairs = [(parse_inputs(pair[0][1:]), parse_inputs(pair[1][1:])) for pair in raw_pairs]

def compare_inputs(pairs):
    left, right = pairs

    if type(left) == int and type(right) == int:
        if left < right:
            return True
        elif left > right:
            return False
        elif left == right:
            return None

    else:
        if type(left) == int and type(right) == list:
            left = [left, ]
        elif type(left) == list and type(right) == int:
            right = [right, ]
    
        left_length = len(left)
        right_length = len(right)

        idx = 0
        while True:
            if idx == left_length == right_length:
                return None
            elif idx == left_length:
                return True
            elif idx == right_length:
                return False
    
            left_item = left[idx]
            right_item = right[idx]

            result = compare_inputs((left_item, right_item))
            if result == None:
                pass
            elif result == True:
                return True
            elif result == False:
                return False
        
            idx += 1
    return None

# 1-index count where ordered
print('Part 1:', sum(idx+1 for idx, value in enumerate(compare_inputs(pair) for pair in pairs) if value == True)) 

divider_one = [[2]]
divider_two = [[6]]
unsorted = []
for pair in pairs:
    unsorted.append(pair[0])
    unsorted.append(pair[1])
unsorted.append(divider_one)
unsorted.append(divider_two)

def sort_list(unsorted_list):
    sorted_list = []
    for item in unsorted_list:
        
        insert_index = 0
        while True:
            if insert_index >= len(sorted_list):
                sorted_list.append(item)
                break
            if compare_inputs((item, sorted_list[insert_index])) == True:
                sorted_list.insert(insert_index, item)
                break
            insert_index += 1

    return sorted_list

sorted_list = sort_list(unsorted)

print('Part 2:', (sorted_list.index(divider_one)+1) * (sorted_list.index(divider_two)+1))
