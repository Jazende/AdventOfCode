import hashlib
from functools import partial
from functools import lru_cache

@lru_cache(maxsize=None)
def has_x_in_a_row(text, x):
    for idx in range(len(text)-x):
        if all([text[idx+i] == text[idx] for i in range(1, x)]):
            return True, text[idx]
    return False, None

@lru_cache(maxsize=1005)
def salted_md5_hash(index, salt):
    return hashlib.md5(f'{salt}{index}'.encode()).hexdigest()

test = partial(salted_md5_hash, salt="abc")
real = partial(salted_md5_hash, salt="zpqevtbw")
has_3_in_a_row = partial(has_x_in_a_row, x=3)

def solution(func, log = False):
    index = 0
    found = 0
    while True:
        hash_ = func(index)
        has_3, char_3 = has_3_in_a_row(hash_)
        if has_3:
            for idx in range(index+1, index+1002):
                new_hash = func(idx)
                if char_3*5 in new_hash:
                    found += 1
                    if log:
                        print(found, index, idx, hash_, new_hash)
        if found == 64:
            break
        index += 1
    return index

print("Day One:", solution(real))

@lru_cache(maxsize=1005)
def stretched_salted_md5_hash(index, salt):
    text = f'{salt}{index}'
    for _ in range(2016+1):
        text = hashlib.md5(text.encode()).hexdigest()
    return text

test = partial(stretched_salted_md5_hash, salt="abc")
real = partial(stretched_salted_md5_hash, salt="zpqevtbw")

print("Day Two:", solution(test, log=True))