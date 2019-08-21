input_test_1 = '<!!!>>'
input_ = ""

with open("adventofcode_9.txt", 'r') as f:
    for x in f:
        input_ += x

def garbage_points(text):
    text = clean_up_escape_chars(text)
    cur_level = 0
    cur_points = 0
    inside_garbage = False
    garbage_count = 0
    for char in text:
        if char == "{" and inside_garbage == False:
            cur_level += 1
            cur_points += cur_level
        if char == "}" and inside_garbage == False:
            cur_level -= 1
        if char == "<":
            inside_garbage = True
        if char == ">":
            if inside_garbage:
                garbage_count -= 1
            inside_garbage = False
        if inside_garbage:
            garbage_count += 1
    return cur_points, garbage_count

def clean_up_escape_chars(text):
    while "!" in text:
        nr = text.index("!")
        text = text[:nr]+text[nr+2:]
    return text

print(garbage_points(input_test_1))
