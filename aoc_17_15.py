from jaz_funcs import time_it, print_result

def generator(start, multiplier, picky_generator=1):
    value = start+0
    while True:
        value *= multiplier
        value %= 2147483647
        if not value % picky_generator == 0:
            continue
        yield value

@print_result
def part1(test=False):
    remainder = 2147483647
    gen_a_start = 289
    gen_b_start = 629
    if test:
        gen_a_start = 65
        gen_b_start = 8921
    gen_a_mul = 16807
    gen_b_mul = 48271

    gen_a = generator(gen_a_start, gen_a_mul)
    gen_b = generator(gen_b_start, gen_b_mul)

    count = 0
    for i in range(40000000):
        a = next(gen_a)
        b = next(gen_b)
        if bin(a)[-16:] == bin(b)[-16:]:
            count += 1
        #print(i, "\n", format(a, '016b')[-16:], "\n", format(b, '016b')[-16:], "\n")
    return count

@print_result
def part2(test=False):
    remainder = 2147483647
    
    gen_a_start = 289
    gen_b_start = 629
    
    if test:
        gen_a_start = 65
        gen_b_start = 8921
        
    gen_a_mul = 16807
    gen_b_mul = 48271

    gen_a_picky = 4
    gen_b_picky = 8

    gen_a = generator(gen_a_start, gen_a_mul, gen_a_picky)
    gen_b = generator(gen_b_start, gen_b_mul, gen_b_picky)

    count = 0
    for i in range(5000000):
        a = next(gen_a)
        b = next(gen_b)
        if bin(a)[-16:] == bin(b)[-16:]:
            count += 1
        #print(i, "\n", format(a, '016b')[-16:], "\n", format(b, '016b')[-16:], "\n")
    return count
