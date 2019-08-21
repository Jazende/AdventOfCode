import re

with open(r'aoc_18_07.txt', 'r') as f:
    raw_input = f.read()

##raw_input = """Step C must be finished before step A can begin.
##Step C must be finished before step F can begin.
##Step A must be finished before step B can begin.
##Step A must be finished before step D can begin.
##Step B must be finished before step E can begin.
##Step D must be finished before step E can begin.
##Step F must be finished before step E can begin.
##"""

step_req = re.compile("Step ([A-Z]) must be finished before step ([A-Z]) can begin.")
steps = step_req.findall(raw_input.strip())

def letter_to_number(letter, extra_time=60):
    return ord(letter) - 4 - 60 + extra_time


class UniqueClass:
    @classmethod
    def new(cls, *args, **kwargs):
        if not hasattr(cls, '_unique_set'):
            setattr(cls, '_unique_set', set())
        new_obj = cls(*args, **kwargs)
        if not new_obj in cls._unique_set:
            cls._unique_set.add(new_obj)
            return new_obj
        else:
            return [x for x in cls._unique_set if x == new_obj][0]

class Step(UniqueClass):
    def __init__(self, name):
        self.name = name
        self._reqs = []
        self.completed = False
        self.in_progress = False
        
    def __repr__(self):
        return f"Step {self.name}"

    def __eq__(self, other):
        if type(self) == type(other) and self.name == other.name:
            return True
        return False

    def __hash__(self):
        return hash(self.name)

    @property
    def reqs(self):
        return self._reqs

    def link(self, step):
        self._reqs.append(step)

    @property
    def active(self):
        if all([x.completed for x in self.reqs]):
            # self.complete = True
            return True
        return False

class Build:
    def __init__(self):
        self._steps = []

    @property
    def steps(self):
        return self._steps

    @steps.setter
    def steps(self, value):
        self._steps = value

    def append(self, step):
        if step in self.steps:
            return
        else:
            self.steps.append(step)
            self.steps = sorted(self.steps, key=lambda x: x.name)

    def get_step(self, name):
        return [x for x in self.steps if x.name == name][0]

    def link(self, step, req):
        step = self.get_step(step)
        req = self.get_step(req)
        if not type(step) == Step or not type(req) == Step:
            raise ValueError
        step.link(req)

    @property
    def links(self):
        re = ""
        for step in self.steps:
            r = ", ".join([str(x) for x in step.reqs])
            re += f"{step} requires {step.reqs}."+"\n"
        return re[:-1]

    @property
    def run_through(self):
        run = ""
        while True:
            active_steps = sorted([x for x in self.steps if x.active and not x.completed], key=lambda x: x.name)
            # print("Active steps:", active_steps)
            if len(active_steps) == 0:
                break
            next_step = active_steps[0]
            next_step.completed = True
            run += str(next_step.name)
            # print("Completed", next_step)
        return run

    def walk_through(self, nr_workers, duration):
        workers = [Worker(x, duration) for x in range(nr_workers)]
        ticks = 0
        print("Tick  " + "    ".join(["W{}".format(x) for x in range(nr_workers)]))
        while True:
            # print(f"Tick {ticks}")
            print(ticks, *[worker.step for worker in workers], sep="\t")
            for worker in workers:
                worker.tick()
            if all([x.completed for x in self.steps]):
                break
            while True:
                active_steps = sorted([x for x in self.steps if x.active and not x.completed and not x.in_progress], key=lambda x: x.name)
                if len(active_steps) == 0:
                    break
                free_workers = [worker for worker in workers if not worker.working]
                if len(free_workers) == 0:
                    break
                # print("Active step:", active_steps[0], "Free worker:", free_workers[0]) 
                free_workers[0].work(active_steps[0])
            ticks += 1
        return ticks

class Worker:
    def __init__(self, id, extra_time):
        self.id = id+1
        self.working = False
        self.time_left = 0
        self.callback = None
        self.extra_time = extra_time
        self.step = " "

    def tick(self):
        if self.working:
            self.time_left -= 1
            if self.time_left == 0:
                # print(f"Worker {self.id} finished {self.callback}")
                self.callback.completed = True
                self.callback.in_progress = False
                self.working = False
                self.callback = None
                self.step = " "

    def work(self, step):
        self.working = True
        self.time_left = letter_to_number(step.name, self.extra_time)
        self.callback = step
        step.in_progress = True
        self.step = step.name
        # print(f"Worker {self.id} started {self.callback}")

    def __repr__(self):
        return f"Worker {self.id}"
  

sleigh = Build()
for step in steps:
    for s in step:
        new_step = Step.new(s)
        sleigh.append(new_step)

for step in steps:
    sleigh.link(step[1], step[0])

def day_1():
    return sleigh.run_through

def day_2():
    return sleigh.walk_through(5, 60)

print(day_2())
