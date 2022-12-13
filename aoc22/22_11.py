import re

with open(r'22_11.txt', 'r') as f:
    raw_lines = f.read().strip()

re_full_info = re.compile('Monkey (\d+).*?items: (.+?)\n.*?old ([\+\*]\s[\dold]+).*?divisible by (\d+).*?true.*?monkey (\d+).*?false.*?monkey (\d+)', flags=re.S)

full_divisor = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19

def operate(operation, item):
    operator, operand = operation.split(' ')

    match operator, operand:
        case '*', 'old':
            return item * item
        case '+', 'old':
            return item + item
        case '*', _:
            return item * int(operand)
        case '+', _:
            return item + int(operand)

class Monkey:
    def __init__(self, number, starting_items, operation, test, if_true, if_false, day_2=False):
        self.number    = number
        self.items     = starting_items
        self.operation = operation
        self.test      = test
        self.if_true   = if_true
        self.if_false  = if_false
        self.inspects  = 0
        self.day_2     = day_2

    def __repr__(self):
        return f'{self.number}: {self.items}'

    def receive_item(self, item):
        self.items.append(item)

    def throw_item(self, item, target):
        target.receive_item(item)

    def take_turn(self):
        while True:
            if len(self.items) == 0:
                break
            current_item = self.items.pop(0)

            # print(f'{self.number} inspects {current_item}')

            self.inspects += 1
            current_item = operate(self.operation, current_item)

            # print(f'{current_item=}')

            if not self.day_2:
                current_item = current_item // 3
                # print(f'monkey is bored; item is now {current_item}')

            if self.day_2 and current_item >= full_divisor:
                current_item %= full_divisor
                # print(f'too big, reducing by {full_divisor=}, now {current_item=}')

            if (current_item // self.test) * self.test == current_item:
                # print(f'divisible by {self.test}, throwing to {self.if_true.number}')
                self.throw_item(current_item, self.if_true)
            else:
                # print(f'not divisible by {self.test}, throwing to {self.if_false.number}')
                self.throw_item(current_item, self.if_false)

# Creating Monkey items
monkeys = []
for monkey in raw_lines.split('\n\n'):
    match_obj = re_full_info.match(monkey)

    monkeys.append(Monkey(
        number=int(match_obj.group(1)), starting_items=[int(x) for x in match_obj.group(2).split(', ')],
        operation=match_obj.group(3), test=int(match_obj.group(4)), if_true=int(match_obj.group(5)),
        if_false=int(match_obj.group(6)),
    ))

# Setting if_true, if_false connection
for monkey in monkeys:
    monkey.if_true  = [m for m in monkeys if m.number == monkey.if_true][0]
    monkey.if_false = [m for m in monkeys if m.number == monkey.if_false][0]

# Going 20 rounds
for _ in range(20):
    for monkey in monkeys:
        monkey.take_turn()

sorted_monkeys = [m for m in monkeys]
sorted_monkeys.sort(key=lambda x: x.inspects, reverse=True)

print('Part 1:', sorted_monkeys[0].inspects * sorted_monkeys[1].inspects)

## Part 2
# resetting monkeys
monkeys = []
for monkey in raw_lines.split('\n\n'):
    match_obj = re_full_info.match(monkey)

    monkeys.append(Monkey(
        number=int(match_obj.group(1)), starting_items=[int(x) for x in match_obj.group(2).split(', ')],
        operation=match_obj.group(3), test=int(match_obj.group(4)), if_true=int(match_obj.group(5)),
        if_false=int(match_obj.group(6)), day_2=True,
    ))

# Setting if_true, if_false connection
for monkey in monkeys:
    monkey.if_true  = [m for m in monkeys if m.number == monkey.if_true][0]
    monkey.if_false = [m for m in monkeys if m.number == monkey.if_false][0]

# Going 10000 rounds
# After every turn, all items reduced by product of every divisor (prime for convenience)
for i in range(10000):
    for monkey in monkeys:
        monkey.take_turn()

sorted_monkeys = [m for m in monkeys]
sorted_monkeys.sort(key=lambda x: x.inspects, reverse=True)

print('Part 2:', sorted_monkeys[0].inspects * sorted_monkeys[1].inspects)
