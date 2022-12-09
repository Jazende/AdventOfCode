prog_0 = {'id': 0, 'p': 0, 'instruction': 0, 'queue': [], 'send_instructions': 0}
prog_1 = {'id': 1, 'p': 1, 'instruction': 1, 'queue': [], 'send_instructions': 0}

from adventofcode_18 import get_input

input_ = get_input()
count = -1
while True:
    count += 1
    if count % 10000 == 0:
        print("Another ten thousand")
    #print(prog_0, prog_1)
    deadlock = [False, False]
    for idx, prog in enumerate([prog_0, prog_1]):
        no_action = False

        if prog['instruction'] >= len(input_) or prog['instruction'] < 0:
            no_action = True
            deadlock[idx] = True
            print("closing ", idx)
        
        instructie = input_[prog['instruction']]

        func = instructie.split(" ")[0]
        slot = instructie.split(" ")[1]
        if len(instructie.split(" ")) == 3:
            set_ = instructie.split(" ")[2]
        else:
            set_ = None

        if not slot in prog:
            prog[slot] = 0
        if set_:
           if not set_ in prog:
               prog[set_] = 0

        if func == 'set':
            try:
                value = int(set_)
            except:
                value = prog[set_]
            prog[slot] = value

        elif func == 'add':
            try:
                value = int(set_)
            except:
                value = prog[set_]
            prog[slot] += value

        elif func == 'jgz':
            try:
                check_value = int(instructie.split(" ")[1])
            except:
                check_value = prog[slot]
            try:
                value_to_add = int(set_)
            except:
                value_to_add = prog[set_]
            if check_value > 0:
                prog['instruction'] += value_to_add - 1

        elif func == 'mod':
            try:
                value_to_mod = int(set_)
            except:
                value_to_mod = prog[set_]
            prog[slot] = prog[slot] % value_to_mod

        elif func == 'mul':
            try:
                value_to_mul = int(set_)
            except:
                value_to_mul = prog[set_]
            prog[slot] *= value_to_mul

        elif func == 'rcv':
            if len(prog['queue']) > 0:
                prog[slot] = prog['queue'].pop(0)
            else:
                no_action = True
                deadlock[idx] = True
                print("closing ", idx)

        elif func == 'snd':
            prog['send_instructions'] += 1
            [prog_0, prog_1][(idx+1)%2]['queue'].append(prog[slot])

        else:
            print(func)
            
        if not no_action:
            prog['instruction'] += 1
                
    if deadlock == [True, True]:
        break

print(prog_1['send_instructions'])

##from adventofcode_18 import match, get_input
##import copy
##import re
##import time
##
##class prog:
##    def __init__(self, id_, input_):
##        self.id_ = id_
##        self.input_ = copy.copy(input_)
##        setattr(self, 'p', id_)
##        self.instruction = 0
##        self.other = None
##        self.queue = []
##        self.count_sends = 0
##
##    def check_action(self):
##        if self.terminate:
##            return False
##        
##        no_action = False
##        
##        if self.instruction == len(self.input_) or self.instruction < 0:
##            self.terminate = True
##            print("End of the line")
##            return False
##        
##        instruc = self.input_[self.instruction].split(" ")
##        func = instruc[0]
##        attr = getattr(self, instruc[1], 0)
##                    
##        if func == "add":
##            try:
##                add_value = int(instruc[2])
##            except:
##                add_value = getattr(self, instruc[2], 0)
##                
##            old_value = attr
##            new_value = old_value + add_value
##            setattr(self, instruc[1], new_value)
##
##        elif func == "mul":
##            try:
##                add_value = int(instruc[2])
##            except:
##                add_value = getattr(self, instruc[2], 0)
##                
##            old_value = attr
##            new_value = old_value * add_value
##            setattr(self, instruc[1], new_value)
##
##        elif func == "mod":
##            try:
##                add_value = int(instruc[2])
##            except:
##                add_value = getattr(self, instruc[2], 0)
##                
##            old_value = attr
##            new_value = old_value % add_value
##            setattr(self, instruc[1], new_value)
##
##        elif func == "jgz":
##            if attr > 0:
##                try:
##                    add_value = int(instruc[2])
##                except:
##                    add_value = getattr(self, instruc[2], 0)
##                self.instruction += add_value
##                return True
##
##        elif func == "set":
##            try:
##                set_value = int(instruc[2])
##            except:
##                set_value = getattr(self, instruc[2], 0)
##            setattr(self, instruc[1], set_value)
##
##        elif func == "snd":
##            self.count_sends += 1
##            self.other.queue.append(attr)
##
##        elif func == "rcv":
##            if not len(self.queue) > 0:
##                no_action = True
##            else:
##                val = self.queue.pop(0)
##                setattr(self, instruc[1], val)
##
##        if no_action:
##            return False
##        
##        self.instruction += 1
##        return True
##
##
##test_2 = ['snd 1', 'snd 2', 'snd p', 'rcv a', 'rcv b', 'rcv c', 'rcv d']
##
##p0 = prog(0, get_input())
##p1 = prog(1, get_input())
##p0.other = p1
##p1.other = p0
##
##while True:
##    zero = p0.check_action()
##    one = p1.check_action()
##    if not zero and not one:
##        print("Deadlock")
##        break
##
##print(p1.count_sends)
