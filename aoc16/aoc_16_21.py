class EnhancedString(str):
    def __init__(self, text):
        self._text = text

    def swap_letter(self, x, y):
        """ swap letter X with letter Y means that the letters X and Y should be swapped (regardless of where they appear in the string). """

        first_index = self._text.find(x)
        second_index = self._text.find(y)
        x_index = min(first_index, second_index)
        y_index = max(first_index, second_index)

        new_string = self._text[:x_index] + self._text[y_index] + self._text[x_index+1:y_index] + self._text[x_index] + self._text[y_index+1:]
        self._text = new_string

    def swap_position(self, x, y):
        """ swap position X with position Y means that the letters at indexes X and Y (counting from 0) should be swapped. """
        x, y = min(x, y), max(x, y)
        new_string = self._text[:x] + self._text[y] + self._text[x+1:y] + self._text[x] + self._text[y+1:]
        self._text = new_string

    def move_position(self, x, y):
        """ move position X to position Y means that the letter which is at index X should be removed from the string, then inserted such that it ends up at index Y. """
        char_at_x = self._text[x]
        intermediate_string = self._text[:x] + self._text[x+1:]
        new_string = intermediate_string[:y] + char_at_x + intermediate_string[y:]
        self._text = new_string

    def reverse_positions(self, x, y):
        """ reverse positions X through Y means that the span of letters at indexes X through Y (including the letters at X and Y) should be reversed in order. """
        x, y = min(x, y), max(x, y)

        new_string = self._text[:x] + self._text[x:y+1][::-1]  + self._text[y+1:]
        self._text = new_string
    
    def rotate_position(self, x):
        """ rotate based on position of letter X means that the whole string should be rotated to the right 
        based on the index of letter X (counting from 0) as determined before this instruction does any rotations. 

        Once the index is determined, rotate the string to the right one time, plus a number of times equal to that index, 
        plus one additional time if the index was at least 4. """
        index_of_x = self._text.find(x)

        rotate_rights = 1 + index_of_x
        if index_of_x >= 4:
            rotate_rights += 1
        rotate_rights = rotate_rights % len(self._text)

        self.rotate_left_right('right', rotate_rights)
    
    def rotate_left_right(self, direction, x):
        """ rotate left/right X steps means that the whole string should be rotated; for example, one right rotation would turn abcd into dabc. """
        if direction == "left":
            new_string = self._text[x:] + self._text[:x]

        elif direction == "right":
            new_string = self._text[-x:] + self._text[:-x]

        else:
            print("Direction", direction, "not supported")
            new_string = self._text

        self._text = new_string

    def reverse_rotate_positions(self, x):
        list_of_rotation_lenghts = [x for x in range(1, len(self._text)+1)]
        if 4 in list_of_rotation_lenghts:
            list_of_rotation_lenghts.pop(4)
        list_of_rotations = [(EnhancedString(self._text[i:] + self._text[:i]), self._text[i:] + self._text[:i])  for i in list_of_rotation_lenghts]

        for idx, rotation in enumerate(list_of_rotations):
            rotation[0].rotate_position(x)
            if rotation[0]._text == self._text:
                self._text = rotation[0]
                break

    def __str__(self):
        return self._text
    
    def __repr__(self):
        return self._text

line = EnhancedString('abcdefgh')

with open(r'aoc_16_21.txt', 'r') as f:
    raw_input = f.read().strip()

instructions = raw_input.split('\n')

def day_one(line, instructions):
    for instruction in instructions:
        parts = instruction.split(' ')
        action = parts[0]

        if action == "swap" and parts[1] == "letter":
            line.swap_letter(parts[2], parts[5])

        elif action == "swap" and parts[1] == "position":
            line.swap_position(int(parts[2]), int(parts[5]))
        
        elif action == "reverse":
            line.reverse_positions(int(parts[2]), int(parts[4]))

        elif action == "move":
            line.move_position(int(parts[2]), int(parts[5]))

        elif action == "rotate" and parts[1] == "left" or parts[1] == "right":
            line.rotate_left_right(parts[1], int(parts[2]))

        elif action == "rotate" and parts[3] == "position":
            line.rotate_position(parts[6])

        else:
            print(action, "not handled")

    return line

print(day_one(line, instructions))


def day_two(line, instructions):
    for instruction in instructions[::-1]:
        parts = instruction.split(' ')
        action = parts[0]
        if action == "swap" and parts[1] == "letter":
            line.swap_letter(parts[2], parts[5])

        elif action == "swap" and parts[1] == "position":
            line.swap_position(int(parts[2]), int(parts[5]))
        
        elif action == "reverse":
            line.reverse_positions(int(parts[2]), int(parts[4]))

        elif action == "move":
            line.move_position(int(parts[5]), int(parts[2]))

        elif action == "rotate" and parts[1] == "left":
            line.rotate_left_right("right", int(parts[2]))

        elif action == "rotate" and parts[1] == "right":
            line.rotate_left_right("left", int(parts[2]))

        elif action == "rotate" and parts[3] == "position":
            line.reverse_rotate_positions(parts[6])

        else:
            print(action, "not handled")

    return line

line = EnhancedString('fbgdceah')
print(day_two(line, instructions))
