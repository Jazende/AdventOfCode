with open(r'22_03.txt', 'r') as f:
    raw_lines = f.read().strip()

def letter_to_score(letter):
    letter = list(letter)[0]
    if letter.isupper():
        return ord(letter)-64+26
    if letter.islower():
        return ord(letter)-96

def split_backpack_find_common_item(backpack):
    # make a set of the first half and a set of the second half
    # then use intersection to find common item
    # return to list, take first item to get common
    return list(set(backpack[:len(backpack)//2]).intersection(set(backpack[len(backpack)//2:])))[0]

print(sum(map(letter_to_score, map(split_backpack_find_common_item, raw_lines.split('\n')))))

def list_per_three_lines(all_backpacks):
    return [all_backpacks[(x*3):(x*3)+3] for x in range(len(all_backpacks)//3)]

def common_item_in_backpacks(backpacks):
    return set(backpacks[0]).intersection(set(backpacks[1])).intersection(set(backpacks[2]))

print(sum(map(letter_to_score, map(common_item_in_backpacks, list_per_three_lines(raw_lines.split('\n'))))))
