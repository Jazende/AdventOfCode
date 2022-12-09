with open(r'aoc_19_02.txt', 'r') as f:
    raw_inputs = f.read()

base_noun = 12
base_verb = 2

def day_one(raw_inputs, noun=base_noun, verb=base_verb):
    inputs = [int(x) for x in raw_inputs.split(',')]

    inputs[1] = noun
    inputs[2] = verb

    index = 0
    while True:
        cur_code = inputs[index]
        if cur_code == 1:
            inputs[inputs[index+3]] = inputs[inputs[index+1]] + inputs[inputs[index+2]]
        elif cur_code == 2:
            inputs[inputs[index+3]] = inputs[inputs[index+1]] * inputs[inputs[index+2]]
        elif cur_code == 99:
            break
        index += 4

    return inputs[0]

def day_two(raw_inputs, target):
    verb_offset = day_one(raw_inputs, verb=base_verb+1) - day_one(raw_inputs)
    noun_offset = day_one(raw_inputs, noun=base_noun+1) - day_one(raw_inputs)
    noun = base_noun
    verb = base_verb

    while day_one(raw_inputs, noun, verb) + noun_offset <= target:
        noun += 1
    while day_one(raw_inputs, noun, verb) + verb_offset <= target:
        verb += 1

    return (noun*100 + verb)

print(day_one(raw_inputs))
print(day_two(raw_inputs, target=19690720))
