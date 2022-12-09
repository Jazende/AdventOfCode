def get_weights_2_ingr():
    for i in range(1, 100):
        yield [i, 100-i]
    return

def get_weights_3_ingr():
    for i in range(1, 100):
        for j in range(i, 100-i):
            yield [i, j, 100-i-j]
    return

def get_weights_4_ingr():
    for i in range(1, 98):
        for j in range(1, 99-i):
            for h in range(1, 100-i-j):
                yield [i, j, h, 100-i-j-h]
    return

def highest_score(cookie, weights_generator, count_calories=True):
    test_weights = weights_generator()
    max_ = 0
    properties = 4

    while True:
        try:
            weights = next(test_weights)
        except StopIteration:
            break
        # print(weights, sum(weights))

        if count_calories:
            cal = 0
            for idx, value in enumerate(weights):
                cal += cookie[idx][4] * value
            if not cal == 500:
                continue

        cur = 1
        for prop in range(properties):
            val = 0
            for idx, value in enumerate(weights):
                val += cookie[idx][prop] * value
                # print(cookie[idx][prop] * value, end=" ")
            val = max(0, val)
            cur *= val
        # print(cur)
        if cur > max_:
            max_ = cur
        
    return max_

test_cookie = [[-1, -2, 6, 3, 8], [2, 3, -2, -1, 3]]
print(highest_score(test_cookie, get_weights_2_ingr, False))
day_one_cookie = [[3, 0, 0, -3, 2], [-3, 3, 0, 0, 9], [-1, 0, 4, 0, 1], [0, 0, -2, 2, 8]]
print(highest_score(day_one_cookie, get_weights_4_ingr, False))
print(highest_score(day_one_cookie, get_weights_4_ingr, True))