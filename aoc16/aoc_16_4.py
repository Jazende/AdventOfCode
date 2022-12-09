import re
from collections import Counter

with open('aoc_16_4.txt', 'r') as file:
    raw_input = file.read()

room_names = re.findall("([\w-]+?)(\d+)\[(\w{1,5})\]", raw_input)

def checksum(room_name):
    room_name = room_name.replace("-", "")
    count = Counter(room_name)
    temp = sorted([[key, count[key]] for key in count], key=lambda x: (x[1]*-1, x[0]))
    return "".join([x[0] for x in temp[0:5]])

valid_rooms = []
for room in room_names:
    if checksum(room[0]) == room[2]:
        valid_rooms.append(room)

print(sum([int(x[1]) for x in valid_rooms]))

alphabet = [x for x in "abcdefghijklmnopqrstuvwxyz"]

def decrypt(name, id_):
    name = name.replace("-", "")
    new_name = "".join([alphabet[(alphabet.index(x)+id_)%26] for x in name])
    return new_name
    
for room in valid_rooms:
    if "northpole" in decrypt(room[0], int(room[1])):
        print(room)
