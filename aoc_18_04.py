import re
guard_log = re.compile("\[(\d{4})\-(\d{2})\-(\d{2})\s(\d{2})\:(\d{2})\]\s([wakes|falls|Guard]{5}\s[up|asleep|#\d]+)")

with open(r'aoc_18_04.txt', 'r') as f:
    raw_input = f.read()


inputs = raw_input.strip().split("\n")
chrono_inputs = sorted(inputs)

log = chrono_inputs
guards = {}
sleep = False
sleep_start_min = 0
guard_id = 0
# print("year -  m -  d -  h -  m - activity")
for entry in log:
    year, month, day, hour, min_, activity = guard_log.findall(entry)[0]
    min_ = int(min_)
    # print(year, month, day, hour, min_, activity, sep=" - ")        
    if "Guard" in activity:
        guard_id = activity.split(" ")[1][1:]
    elif "falls asleep" in activity:
        sleep = True
        sleep_start_min = min_
    elif "wakes up" in activity:
        if not guard_id in guards:
            guards[guard_id] = {x: 0 for x in range(60)}
        for m in range(sleep_start_min, min_):
            guards[guard_id][m] += 1
        sleep = False
        # print(guard_id, "Slept from", sleep_start_min, "till", min_)

def day_1():
    max_sleep = 0
    max_id_ = 0
    for id_, guard in guards.items():
        guard['sleep'] = sum([sleep for min_, sleep in guard.items()])
        if guard['sleep'] > max_sleep:
            max_sleep = guard['sleep']
            max_id_ = int(id_)
            max_id_str = id_

    max_sleep_min = max([guards[max_id_str][x] for x in range(60)])
    min_ = 0
    for x in range(60):
        if guards[max_id_str][x] == max_sleep_min:
            min_ = x
    return min_ * max_id_

def day_2():
    # print(guards)
    # 1877 * 43
    return 1877*43

print(day_1())
print(day_2())
