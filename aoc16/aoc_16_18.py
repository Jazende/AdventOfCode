from collections import Counter

input_ = "...^^^^^..^...^...^^^^^^...^.^^^.^.^.^^.^^^.....^.^^^...^^^^^^.....^.^^...^^^^^...^.^^^.^^......^^^^"

def expand(start, rows, log=False):
    traps = [start]
    while True:
        old_traps = "." + traps[-1] + "."
        new_traps = ""
        for idx, trap in enumerate(old_traps[1:-1]):
            above = old_traps[idx:idx+3]
            if above in ["^^.", ".^^", "^..", "..^"]:
                new_traps += "^"
            else:
                new_traps += "."
        traps.append(new_traps)

        if len(traps) == rows:
            break

    if log: 
        for trap in traps:
            print(trap)
        print("")
    
    return traps

def count_safe_tiles(rows):
    return sum([len(row.replace('^', '')) for row in rows])

expand("..^^.", 3, True)
expand('.^^.^.^^^^', 10, True)
print(count_safe_tiles(expand(input_, 40)))
print(count_safe_tiles(expand(input_, 400000)))
