with open('aoc_16_7.txt', 'r') as file:
    raw_input = file.read()

import re

ips = raw_input.strip().split("\n")

def convert(full_ip):
    full_outside = []
    full_inside = []
    outside = ""
    inside = ""
    switch = 0
    for char in full_ip:
        if char == "[":
            switch = 1
            full_outside.append(outside)
            outside = ""
        elif char == "]":
            full_inside.append(inside)
            inside = ""
            switch = 0
        else:
            if switch == 0:
                outside += char
            elif switch == 1:
                inside += char
    if not outside == "":
        full_outside.append(outside)
    if not inside == "":
        full_inside.append(inside)
    return full_outside, full_inside


def abba(ip_part):
    for x in range(0, len(ip_part)-3):
        if ip_part[x:x+2] == ip_part[x+2:x+4][::-1] and not ip_part[x] == ip_part[x+1]:
            return True
    return False


def valid_abba(converted):
    outside, inside = converted
    for ins in inside:
        if abba(ins):
            # print("found inside, invalid")
            return False
    for outs in outside:
        if abba(outs):
            # print("not found inside, found outside, valid")
            return True
    # print("not found at all, invalid")
    return False


count = 0
for ip in ips:
    if valid_abba(convert(ip)):
        count += 1

print("part 1: ", count)

def aba(ip_part):
    results = []
    for x in range(0, len(ip_part)-2):
        if ip_part[x:x+2] == ip_part[x+1:x+3][::-1] and not ip_part[x] == ip_part[x+1]:
            results.append([ip_part[x:x+2]+ip_part[x], ip_part[x+1]+ip_part[x]+ip_part[x+1]])
    if not len(results) == 0:
        return True, results
    return False, None

def valid_aba(converted):
    outside, inside = converted
    to_match_inside = []
    for outs in outside:
        result, list_ = aba(outs)
        # print(outs, result, list_)
        if result:
            for aba_bab in list_:
                to_match_inside.append(aba_bab[1])
    # print(to_match_inside, inside, end=" ")
    for ins in inside:
        for match in to_match_inside:
            if match in ins:
                # print("Valid")
                return True
    # print("Invalid")
    return False
    
count = 0
for ip in ips:
    if valid_aba(convert(ip)):
        count += 1
        
print("part 2: ", count)
