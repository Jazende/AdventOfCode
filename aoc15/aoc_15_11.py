import re

re_nonoverlapping_consecutive_pairs = re.compile(r'(.*)([a-z])(\2)(.*)')

def two_nonoverlapping_pairs(text):
    match = re_nonoverlapping_consecutive_pairs.match(text)
    if not match:
        return False
    for group in [match.group(1), match.group(4)]:
        if re_nonoverlapping_consecutive_pairs.match(group):
            return True
    return False

def three_consecutive_increasing_in_text(text):
    for char in range(0, 26 + 1 - 3):
        if "".join([chr(i+97) for i in range(char, char+3)]) in text:
            return True
    return False

class BaseTwentySix:
    def __init__(self, number):
        self._number = number
        self.representation = self._to_password()

    @staticmethod
    def from_string(text):
        number = 0
        for idx, char in enumerate(text[::-1]):
            number += (ord(char) - 97) * (26**idx)
        return BaseTwentySix(number)

    def _to_password(self):
        representation = ""
        calculation_number = self._number
        for exponent in range(0, 8)[::-1]:
            divisor = 26 ** exponent
            result = calculation_number // divisor
            calculation_number = calculation_number % divisor
            representation += chr(result + 97)
        return representation
    
    def _get_next(self):
        new = BaseTwentySix(self._number)
        while True:
            new += 1
            if new.is_valid():
                return new

    def __repr__(self):
        return self.representation

    def __iadd__(self, other):
        self._number += other
        self.representation = self._to_password()
        return self

    def is_valid(self):
        """
        Passwords may not contain the letters i, o, or l, 
            as these letters can be mistaken for other characters and are therefore confusing.
        """
        for token in ["i", "o", "l"]:
            if token in self.representation:
                return False

        """
        Passwords must include one increasing straight of at least three letters, 
            like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
        """
        if not three_consecutive_increasing_in_text(self.representation):
            return False

        """
        Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
        """
        if not two_nonoverlapping_pairs(self.representation):
            return False
        return True

    def next_password(self):
        while True:
            self += 1
            if self.is_valid():
                return self

# example = BaseTwentySix.from_string('abcdefgh')
# print(example.next_password())

solution_one = BaseTwentySix.from_string('cqjxjnds').next_password()
print(solution_one)

solution_two = solution_one.next_password()
print(solution_two)