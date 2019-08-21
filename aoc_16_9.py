import re

with open("aoc_16_9.txt", "r") as file:
    raw_input = file.read()

raw_input = raw_input.replace(" ", "")

def parser(input_text):
    text = input_text + ""
    response = ""
    reply = ""
    while True:
        if len(text) == 0:
            break
        match_obj = re.match("\((\d{1,4})x(\d{1,4})\)", text[:min(len(text), 10)])
        if not match_obj is None:
            skip_tekens = len(match_obj[1]) + len(match_obj[2]) + 3
            tekens = int(match_obj[1])
            maal = int(match_obj[2])
            reply += (text[skip_tekens:skip_tekens+tekens]) * maal
            text = text[skip_tekens+tekens:]
        else:
            reply += text[0]
            text = text[1:]
    return reply


# print(parser("ADVENT"))
# print(parser("A(1x5)BC"))
# print(parser("A(2x2)BCD(2x2)EFG"))
# print(parser("(6x1)(1x3)A"))
# print(parser("X(8x2)(3x3)ABCY"))
print(len(parser(raw_input)))

class Token:
    def __init__(self, count):
        self.count = 1
        self.chars = 1

    def __repr__(self):
        return "_ (" + str(self.count) + ")"

class Mark:
    def __init__(self, text):
        # aantal tekens in de chain
        self.chars = len(text)
        # aantal tekens te multiplien, aantal keer die tekens te multiplien
        self.amount_mul, self.times_mul = text[1:-1].split("x")
        self.amount_mul = int(self.amount_mul)
        self.times_mul = int(self.times_mul)
        # aantal keer zelf te telen
        self.count = 1

    def __repr__(self):
        return "(" + str(self.amount_mul) + "x" + str(self.times_mul) + ")"

def prepare(raw_input):
    prepared = []
    found = re.findall("(\(\d+x\d+\)|\w)", raw_input)
    for x in found:
        if x.startswith("("):
            prepared.append(Mark(x))
        else:
            prepared.append(Token(x))
        # prepared.append(x)
    return prepared

def parser_two(input_text):
    prepared = prepare(input_text)
    for idx, char in enumerate(prepared):
        if type(char) == Mark:
            prepared = increase_count(prepared, idx+1, char.amount_mul, char.times_mul)
    return sum([x.count for x in prepared if type(x) == Token])

def increase_count(prepared, start, amount, mul):
    counter = 0
    while amount > 0:
        prepared[start+counter].count *= mul
        amount -= prepared[start+counter].chars
        counter += 1
    return prepared

print(parser_two("(3x3)XYZ"))
print(parser_two("X(8x2)(3x3)ABCY"))
print(parser_two("(27x12)(20x12)(13x14)(7x10)(1x12)A"))
print(parser_two("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"))
print(parser_two(raw_input))
