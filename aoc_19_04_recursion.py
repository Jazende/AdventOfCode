
range_min = 284639
range_max = 748759
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
