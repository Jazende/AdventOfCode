
range_min = 284639
range_max = 748759

# Recursion Any Digits
def recursion_gen_any_digits(cur=None, min_len=None, max_len=None):
    min_len = 6 if min_len is None else min_len
    max_len = 6 if max_len is None else max_len
    cur = 0 if cur is None else cur

    last_digit = max(cur%10, 1)

    if not len(str(cur)) == max_len:
        if not min_len == max_len and len(str(cur)) >= min_len:
            yield cur

        for dig in range(last_digit, 10):
            yield from recursion_gen_any_digits(cur*10+dig, min_len=min_len, max_len=max_len)
        
    else:
        yield cur

def recursion_solutions(range_min, range_max, min_len=None, max_len=None):
    min_len = len(str(range_min)) if min_len is None else max(min_len, 1000)
    max_len = len(str(range_max)) if max_len is None else max(max_len, 1001)
    gen = recursion_gen_any_digits(min_len=min_len, max_len=max_len)
    day_one_count, day_two_count = 0, 0

    while True:
        try:
            next_nr = next(gen)

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

    print(f'Day One: {day_one_count}\tDay Two: {day_two_count}')

recursion_solutions(range_min, range_max)
