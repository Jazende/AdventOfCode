from math import sqrt

# def get_proper_divisors(number):
#     divisors = [1, number]
#     for i in range(2, int(sqrt(number))+1):
#         if number % i == 0:
#             divisors.append(i)
#             divisors.append(number//i)
#     return set(divisors)

# def get_sum_proper_divisors(number):
#     return sum([x*10 for x in get_proper_divisors(number)])

# count = 0
# for i in range(600000, 666000)[::-1]:
#     divs = get_sum_proper_divisors(i)
#     if divs > 29000000:
#         print(i, get_proper_divisors(i), get_sum_proper_divisors(i))
#         count += 1

#     if count == 10:
#         break

def get_proper_divisors(number):
    divisors = [1, number]
    for i in range(2, 51):
        if number % i == 0:
            div = number // i
            if div < 51 or i < 51:
                divisors.append(i)
                divisors.append(number//i)
    return set(divisors)

def get_sum_proper_divisors(number):
    return sum([x*11 for x in get_proper_divisors(number)])

count = 0
for i in range(700000, 720000)[::-1]:
    divs = get_sum_proper_divisors(i)
    if divs > 29000000:
        print(i, get_proper_divisors(i), get_sum_proper_divisors(i))
        count += 1

    if count == 10:
        break

