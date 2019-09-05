from itertools import combinations

test_packages = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
real_packages = [1, 3, 5, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

def get_smallest_possible(packages, groups, total, equal_size):
    for idx in range(len(packages)):
        if sum(packages[len(packages)-idx:len(packages)]) >= equal_size:
            return idx

def product(packages):
    prod = 1
    for package in packages:
        prod *= package
    return prod

def smallest_group_driver_seat(packages, groups):
    total = sum(packages)
    equal_size = total // groups

    # Find the smallest amount of packages needed to get the partial size.
    for idx in range(len(packages)):
        if sum(packages[len(packages)-idx:len(packages)]) >= equal_size:
            smallest_poss = idx
            break

    found = False
    minimum = product(packages[:smallest_poss+1:-1])
    while True:
        for combination in combinations(packages, smallest_poss):
            if sum(combination) == equal_size:
                found = True
                minimum = min(minimum, product(combination))
        if found:
            break
        else:
            smallest_poss += 1
    return minimum

print("Day One (3 groups):", smallest_group_driver_seat(real_packages, 3))
print("Day Two (4 groups):", smallest_group_driver_seat(real_packages, 4))