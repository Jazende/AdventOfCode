class Bot:
    def __init__(self, number):
        self.number = number
        self.input = None
        self.output = None
        self.chips = []
    
    def can_perform_action(self):
        inp = 0 if self.input is None else 1
        out = 0 if self.output is None else 1
        if len(self.chips) + inp + out >= 2:
            return True
        return False

    def get_chips_and_keep(self):
        chips = self.chips
        if not self.input is None:
            chips.append(self.input)
        if not self.output is None:
            chips.append(self.output)
        return chips

    def get_and_remove_both_chips(self):
        chips = self.chips
        if not self.input is None:
            chips.append(self.input)
        if not self.output is None:
            chips.append(self.output)
        
        self.input = None
        self.output = None
        self.chips = []

        return chips

    def give_chip(self, chip):
        self.chips.append(chip)
        self.chips.sort()
    
    def set_output(self, chip):
        self.output = chip

    def __repr__(self):
        chips = self.get_chips_and_keep()
        return f'Bot {self.number:>3}: {", ".join([str(x) for x in chips])}'

class Chip:
    def __init__(self, number):
        self.number = number
    
    def __repr__(self):
        return f'Chip {self.number}'

    def __lt__(self, other):
        if self.number < other.number:
            return True
        return False

with open(r'aoc_16_10.txt', 'r') as f:
    raw_input = f.read().strip()

test_info = {
    'raw_input': "value 5 goes to bot 2\nbot 2 gives low to bot 1 and high to bot 0\nvalue 3 goes to bot 1\nbot 1 gives low to output 1 and high to bot 0\nbot 0 gives low to output 2 and high to output 0\nvalue 2 goes to bot 2",
    'find_low_value': 2,
    'find_high_value': 5,
}

real_info = {
    'raw_input': raw_input,
    'find_low_value': 17,
    'find_high_value': 61,
}

def solution(raw_input, find_low_value, find_high_value):
    bots = {}
    chips = {}

    instructions = [line.split(" ") for line in raw_input.strip().split('\n')]

    while True:
        if len(instructions) == 0:
            break

        instruction = instructions.pop(0)

        if instruction[0] == "value":
            bot_number = int(instruction[5])
            if not bot_number in bots.keys():
                bots[bot_number] = Bot(bot_number)

            chip_number = int(instruction[1])
            if not chip_number in chips.keys():
                chips[chip_number] = Chip(chip_number)
            
            bots[bot_number].give_chip(chips[chip_number])

        else:
            _, bot_number, _, _, _, low_bot_type, low_bot_recipient, _, _, _, high_bot_type, high_bot_recipient = instruction
            bot_number = int(bot_number)
            low_bot_recipient = int(low_bot_recipient)
            high_bot_recipient = int(high_bot_recipient)

            if not bot_number in bots.keys():
                bots[bot_number] = Bot(bot_number)

            if bots[bot_number].can_perform_action() == True:
                bot = bots[bot_number]
                bot_chips = bot.get_and_remove_both_chips()

                if bot_chips[0].number == find_low_value and bot_chips[1].number == find_high_value:
                    print(f"Bot {bot_number} is comparing {find_low_value} and {find_high_value}.")

                if low_bot_type == "bot":
                    bots[low_bot_recipient].give_chip(bot_chips.pop(0))
                elif low_bot_type == "output":
                    bots[low_bot_recipient].set_output(bot_chips.pop(0))
                
                if high_bot_type == "bot":
                    bots[high_bot_recipient].give_chip(bot_chips.pop(0))
                elif high_bot_type == "output":
                    bots[high_bot_recipient].set_output(bot_chips.pop(0))

            else:
                instructions.append(instruction)

    number = bots[0].output.number * bots[1].output.number * bots[2].output.number
    print(f'{bots[0].output} * {bots[1].output} * {bots[2].output} = {number}')

solution(**test_info)
solution(**real_info)