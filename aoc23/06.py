with open('input_06.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '''Time:      7  15   30
# Distance:  9  40  200'''

########################## DAY 6 PART 1 ########################## 

raw_times, raw_distances = raw_inputs.split('\n', 2)
times = [int(x) for x in raw_times.split(':')[1].replace('  ', ' ').split(' ') if not x == '']
distances = [int(x) for x in raw_distances.split(':')[1].replace('  ', ' ').split(' ') if not x == '']


def distance(held, max_time):
    return (max_time - held) * held

total = 1
for time, distance in zip(times, distances):
    race_score = 0
    for i in range(time):
        if ((time-i) * i) > distance:
            race_score += 1
    total *= race_score
print(total)

########################## DAY 6 PART 2 ########################## 

raw_times, raw_distances = raw_inputs.split('\n', 2)
times = int(''.join(raw_times.split(':')[1].split(' ')))
distances = int(''.join(raw_distances.split(':')[1].split(' ')))

start = 0
end = times

# Get first one where it's true
time = 0
while True:
    if ((times - time) * time) > distances:
        start = time
        break
    time += 1


time = times
while True:
    if ((times - time) * time) > distances:
        end = time
        break
    time -= 1
    
print(end+1-start)
