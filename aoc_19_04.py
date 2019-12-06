import time

range_min = 284639
range_max = 748759

# Iteration
def solutions(range_min, range_max):
    day_one_count, day_two_count = 0, 0
    for dig_1 in range(2, 8):
        for dig_2 in range(dig_1, 10):
            for dig_3 in range(dig_2, 10):
                for dig_4 in range(dig_3, 10):
                    for dig_5 in range(dig_4, 10):
                        for dig_6 in range(dig_5, 10):
                            next_nr = ((((((dig_1 * 10) + dig_2) * 10 + dig_3) * 10 + dig_4) * 10 + dig_5) * 10 + dig_6)

                            if next_nr < range_min or next_nr > range_max:
                                continue
                            if not (dig_1 == dig_2 or dig_2 == dig_3 or dig_3 == dig_4 or dig_4 == dig_5 or dig_5 == dig_6):
                                continue
                            
                            day_one_count += 1

                            if not (
                                                       (dig_1 == dig_2 and not dig_2 == dig_3) or \
                                (not dig_1 == dig_2 and dig_2 == dig_3 and not dig_3 == dig_4) or \
                                (not dig_2 == dig_3 and dig_3 == dig_4 and not dig_4 == dig_5) or \
                                (not dig_3 == dig_4 and dig_4 == dig_5 and not dig_5 == dig_6) or \
                                (not dig_4 == dig_5 and dig_5 == dig_6)
                                ):
                                continue

                            day_two_count += 1

    print(f'Day One: {day_one_count}\tDay Two: {day_two_count}')

solutions(range_min, range_max)

# Recursion
def returning_digits(cur=None):
    cur = 0 if cur is None else cur
    last_digit = max(cur%10, 1) # als cur = 0 dan is last_digit = 0, mag niet, daarom altijd minstens last_digit = 1

    if not len(str(cur)) == 6:
        for dig in range(last_digit, 10):
            yield from returning_digits(cur*10+dig)
    else:
        yield cur

def solutions(range_min, range_max):
    gen = returning_digits()
    day_one_count, day_two_count = 0, 0
    nr_count = 0
    while True:
        try:
            next_nr = next(gen)
            nr_count += 1

            dig_1, dig_2, dig_3, dig_4, dig_5, dig_6 = [int(x) for x in str(next_nr)]
            digits = [int(x) for x in str(next_nr)]
                    
            if next_nr < range_min or next_nr > range_max:
                continue
            # if not (dig_1 == dig_2 or dig_2 == dig_3 or dig_3 == dig_4 or dig_4 == dig_5 or dig_5 == dig_6):
                # continue
            for i in range(len(digits) - 1):
                if digits[i] == digits[i+1]:
                    day_one_count += 1
                    break
                
            # day_one_count += 1
            
            if not (
                                    (dig_1 == dig_2 and not dig_2 == dig_3) or \
                (not dig_1 == dig_2 and dig_2 == dig_3 and not dig_3 == dig_4) or \
                (not dig_2 == dig_3 and dig_3 == dig_4 and not dig_4 == dig_5) or \
                (not dig_3 == dig_4 and dig_4 == dig_5 and not dig_5 == dig_6) or \
                (not dig_4 == dig_5 and dig_5 == dig_6)
                ):
                continue

            day_two_count += 1

        except StopIteration:
            break
    print(f'Day One: {day_one_count}\tDay Two: {day_two_count}\tNr Count: {nr_count}')

solutions(range_min, range_max)

# Recursion Any Digits
def recursion_gen_any_digits(cur=None, min_len=None, max_len=None):
    min_len = 6 if min_len is None else min_len
    max_len = 6 if max_len is None else max_len
    cur = 0 if cur is None else cur
    last_digit = max(cur%10, 1) # als cur = 0 dan is last_digit = 0, mag niet, daarom altijd minstens last_digit = 1


    if not len(str(cur)) == max_len:
        if not min_len == max_len and len(str(cur)) >= min_len:
            yield cur

        for dig in range(last_digit, 10):
            yield from recursion_gen_any_digits(cur*10+dig, min_len=min_len, max_len=max_len)
        
    else:
        yield cur

def recursion_solutions(range_min, range_max, min_len=None, max_len=None):
    min_len = len(str(range_min)) if min_len is None else min_len
    max_len = len(str(range_max)) if max_len is None else max_len
    gen = recursion_gen_any_digits(min_len=min_len, max_len=max_len)
    day_one_count, day_two_count = 0, 0
    nr_count = 0
    while True:
        try:
            next_nr = next(gen)

            nr_count += 1

            digits = [int(x) for x in str(next_nr)]
                    
            if next_nr < range_min or next_nr > range_max:
                continue

            if not any([digits[i] == digits[i+1] for i in range(len(digits)-1)]):
                continue

            day_one_count += 1

            if digits[0] == digits[1] and not digits[1] == digits[2]:
                day_two_count += 1
                continue
            if digits[-1] == digits[-2] and not digits[-2] == digits[-3]:
                day_two_count += 1
                continue
            
            for i in range(1, len(digits)-2):
                if (not digits[i-1] == digits[i]) and (digits[i] == digits[i+1]) and (not digits[i+1] == digits[i+2]):
                    day_two_count += 1
                    break

        except StopIteration:
            break

    print(f'Day One: {day_one_count}\tDay Two: {day_two_count}\tNr Count: {nr_count}')

recursion_solutions(284639, 748759)

