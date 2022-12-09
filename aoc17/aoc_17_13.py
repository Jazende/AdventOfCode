import copy

class FW:
    def __init__(self, positie, grootte, scanner):
        self.positie = positie
        self._grootte = grootte
        self.scanner = scanner
        self.direction = 0

    @property
    def grootte(self):
        return self._grootte

    @grootte.setter
    def grootte(self, value):
        if value > 0:
            self.direction = 1
        if value <= 0:
            self.direction = 0
        self._grootte = value

    def tick(self):
        if self.scanner + self.direction > self.grootte - 1:
            self.direction *= -1
        if self.scanner + self.direction < 0:
            self.direction *= -1
        self.scanner += self.direction        
    
    def __repr__(self):
        #return "<P:{}, G: {}, S: {}>".format(
        return "({},{},{})".format(
            self.positie, self.grootte, self.scanner
            )

test = ["0: 3", "1: 2", "4: 4", "6: 4"]
real = []
with open("adventofcode_13.txt", 'r') as f:
    for line in f:
        real.append(line.strip())

def create_firewall(input_):
    input_ = [[int(x.strip().split(": ")[0]), int(x.strip().split(": ")[1])] for x in input_]
    max_ = input_[len(input_)-1][0]
    firewall = [FW(x, 0, 0) for x in range(max_+1)]

    for value in input_:
        firewall[value[0]].grootte = value[1]
        
    return firewall

def move_through(firewall):
    positie = -1
    score = 0
    for x in range(len(firewall)):
        positie += 1
        if firewall[x].grootte > 0:
            if firewall[x].scanner == 0:
                score += (firewall[x].grootte) * firewall[x].positie
        for item in firewall:
            item.tick()
    return score

def moving_firewall(firewall):
    while True:
        yield firewall
        for item in firewall:
            item.tick()

def caught(firewall, delay=0):
    positie = -1 - delay
    caught = 0
    for x in range(delay):
        for item in firewall:
            item.tick()
    for x in range(len(firewall)):
        positie += 1
        if firewall[x].grootte > 0:
            if firewall[x].scanner == 0:
                caught += 1
        for item in firewall:
            item.tick()
    return caught

def delay_needed(input_):
    delay = 0
    while True:
        new_fw = create_firewall(input_) 
        times_caught = caught(new_fw, delay)
        if times_caught == 0:
            break
        delay += 1
        if delay % 10 == 0:
            print(delay)
    return delay

def caught_2(fw):
    positie = -1
    caught = 0
    firewall = copy.deepcopy(fw)
    for x in range(len(firewall)):
        positie += 1
        if firewall[x].grootte > 0:
            if firewall[x].scanner == 0:
                caught += 1
        for item in firewall:
            item.tick()
    return caught

def delay_needed_2(input_):
    count = 0
    fw = create_firewall(input_)
    fw_iter = iter(moving_firewall(fw))
    while True:
        new_fw = next(fw_iter)
        if caught_2(new_fw) == 0:
            break
        count += 1
        if count % 100 == 0:
            print(count)
    print("Done: ", end = "")
    return count
    
#print(move_through(create_firewall(test)))
print(delay_needed_2(test))
#x = input("???")
