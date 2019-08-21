with open(r'aoc_15_14.txt', 'r') as f:
    raw_input = f.read().strip()
    
class Reindeer:
    def __init__(self, speed, duration, cooldown):
        self.speed = speed
        self.duration = duration
        self.cooldown = cooldown

        self.cycle = self.duration + self.cooldown

        self.points = 0
    
    def distance(self, time):
        distance = (time // self.cycle) * self.duration * self.speed
        remaining = time % self.cycle
        distance += min(self.duration, remaining) * self.speed
        self._last_known_distance = distance
        return distance
    
    def __repr__(self):
        return f"Reindeer: {self.points} points, {self._last_known_distance} km"


reindeers = []
for line in raw_input.split("\n"):
    x = line.split(" ")
    reindeers.append(Reindeer(int(x[3]), int(x[6]), int(x[13])))

print(max([reindeer.distance(2503) for reindeer in reindeers]))

### --- ### --- ### --- ### --- ### --- ### --- ### --- ###
#                       Day Two
### --- ### --- ### --- ### --- ### --- ### --- ### --- ###

reindeers = []
for line in raw_input.split("\n"):
    x = line.split(" ")
    reindeers.append(Reindeer(int(x[3]), int(x[6]), int(x[13])))


# reindeers = [Reindeer(14, 10, 127), Reindeer(16, 11, 162)]

for second in range(2503):
# for second in range(1000):
    top = max(reindeers, key=lambda x: x.distance(second+1))._last_known_distance
    for reindeer in reindeers:
        if reindeer.distance(second+1) == top:
            reindeer.points += 1

print(max(reindeers, key=lambda x: x.points).points)