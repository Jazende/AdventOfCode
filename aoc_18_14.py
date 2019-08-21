def day_1(input_):
    recipies = [3, 7]
    elf_0 = 0
    elf_1 = 1
    while True:
        new_recipe = recipies[elf_0] + recipies[elf_1]
        for score in str(new_recipe):
            recipies.append(int(score))
            if len(recipies) == (input_+10):
                break
        if len(recipies) == (input_+10):
            break
        elf_0 = (elf_0 + recipies[elf_0] + 1) % (len(recipies))
        elf_1 = (elf_1 + recipies[elf_1] + 1) % (len(recipies))
    return "".join([str(x) for x in recipies[-10:]])

print(day_1(9))
print(day_1(5))
print(day_1(18))
print(day_1(2018))
print(day_1(360781))

def day_2(input_):
    recipies = [3, 7]
    elf_0 = 0
    elf_1 = 1
    to_find = [int(x) for x in str(input_)]
    len_to_find = len(to_find)
    while True:
        new_recipe = recipies[elf_0] + recipies[elf_1]
        for score in str(new_recipe):
            recipies.append(int(score))
            if recipies[-len_to_find:] == to_find:
                break
        if recipies[-len_to_find:] == to_find:
            break
        elf_0 = (elf_0 + recipies[elf_0] + 1) % (len(recipies))
        elf_1 = (elf_1 + recipies[elf_1] + 1) % (len(recipies))
    return len(recipies)-len_to_find

print(day_2("51589"))
print(day_2("01245"))
print(day_2("92510"))
print(day_2("59414"))
print(day_2("360781"))
