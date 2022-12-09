from functools import wraps
import re

match = re.compile("^([acdegjlmnorstuvz]{3})\s?(\w)?\s?([-a-z0-9]*)?$")

class Register:
    pass

def get_input(test=False):
    if test:
        return ["set a 1", "add a 2", "mul a a", "mod a 5", "snd a",
                "set a 0", "rcv a", "jgz a -1", "set a 1", "jgz a -2"]
    else:
        with open('adventofcode_18.txt', 'r') as f:
            res = f.read().strip().split('\n')
        return res

def value_parser_three(fn):
    @wraps(fn)
    def wrapped(*args):
        reg, two, three = args
        try:
            three = int(three)
        except:
            three = getattr(reg, three)
        fn(reg, two, three)
    return wrapped

@value_parser_three
def setter(register, variable, value):
    setattr(register, variable, value)
    return register

def part1(test=False):
    reg = Register()
    input_ = get_input(test)
    keys = []
    instruction = 0
    sound = None
    recovered = None
    while True:
        inp = input_[instruction]
        re_match = re.match(match, inp)
        
        if not hasattr(reg, re_match.group(2)):
            setattr(reg, re_match.group(2), 0)
        if not hasattr(reg, re_match.group(2)):
            setattr(reg, re_match.group(2), 0)
            
        if re_match.group(1) == "set":
            setter(reg, re_match.group(2), re_match.group(3))
            if not re_match.group(2) in keys:
                keys.append(re_match.group(2))
                
        if re_match.group(1) == "add":
            try:
                test_value = int(re_match.group(3))
            except:
                setattr(reg, re_match.group(2), getattr(reg, re_match.group(2)) + getattr(reg, re_match.group(3)))
            else:
                setattr(reg, re_match.group(2), getattr(reg, re_match.group(2)) + int(re_match.group(3)))
                
        if re_match.group(1) == "mul":
            try:
                test_value = int(re_match.group(3))
            except:
                setattr(reg, re_match.group(2), getattr(reg, re_match.group(2)) * getattr(reg, re_match.group(3)))
            else:
                setattr(reg, re_match.group(2), getattr(reg, re_match.group(2)) * int(re_match.group(3)))
            
        if re_match.group(1) == "mod":
            try:
                test_value = int(re_match.group(3))
            except ValueError:
                setattr(reg, re_match.group(2), getattr(reg, re_match.group(2)) % getattr(reg, re_match.group(3)))
            else:
                setattr(reg, re_match.group(2), getattr(reg, re_match.group(2)) % int(re_match.group(3)))
                
        if re_match.group(1) == "snd":
            sound = getattr(reg, re_match.group(2))
            
        if re_match.group(1) == "rcv":
            try:
                test_value = int(re_match.group(2))
            except:
                if not re_match.group(2) == 0:
                    recovered = sound
                    break                    
            else:
                if not getattr(reg, re_match.group(2)) == 0:
                    recovered = sound
                    break

        if re_match.group(1) == "jgz":
            if not getattr(reg, re_match.group(2)) == 0:
                instruction += int(re_match.group(3))
                continue

        if instruction >= len(input_):
            break

        instruction += 1
    return recovered

if __name__ == '__main__':
    print(part1(False))
