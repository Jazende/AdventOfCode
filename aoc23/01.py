with open('input_01.txt') as f:
    lines = f.readlines()

translations = [
    ('zero', '0'), ('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), 
    ('five', '5'), ('six', '6'), ('seven', '7'), ('eight', '8'), ('nine', '9'), 
]

########################## DAY 1 PART 1 ########################## 

sum_ = 0
for line in lines:
    l = "".join([c for c in line if c in "123456789"])
    d = l[0] + l[-1]
    sum_ += int(d)
print(sum_)

########################## DAY 1 PART 2 ########################## 

def front_to_back(text):
    l = len(text)
    for x in range(l):
        if text[x] in "123456789":
            return text[x]
        for word, nummer in translations: 
            if text[x:].startswith(word):
                return nummer

def back_to_front(text):
    l = len(text)
    for x in range(l):
        if text[l-x-1] in "123456789":
            return text[l-x-1]
        for word, nummer in translations:
            if text[l-x-1:].startswith(word):
                return nummer

sum_ = 0
for line in lines:
    line = line.strip()
    first = front_to_back(line)
    last = back_to_front(line)
    sum_ += int(first) * 10 + int(last)
print(sum_)