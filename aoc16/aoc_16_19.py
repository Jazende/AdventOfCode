def day_one(amount_elves_to_get_to):
    """
    Start at 1 - > 1
    for each +1 nr -> solution +2
    if nr = 2^n -> solution = 1
    """

    elves = 0
    answer = -1
    while True:
        elves += 1
        answer += 2
        if answer > elves:
            answer = 1

        if elves == amount_elves_to_get_to:
            break

    return answer

print(day_one(3018458))

def day_two(amount_elves_to_get_to):
    lower_bound = 1
    higher_bound = 3

    while True:
        lower_bound *= 3
        higher_bound *= 3

        if lower_bound <= amount_elves_to_get_to <= higher_bound:
            break

    breakpoint = higher_bound - lower_bound
    count = lower_bound
    number = 0

    while True:
        count += 1
        number += 1 if count <= breakpoint else 2

        if count == amount_elves_to_get_to:
            break

    return number

print(day_two(3018458))