class Container(int):
    id = 0
    container = {}
    def __init__(self, *args, **kwargs):
        super().__init__()
        Container.id += 1
        self.id = Container.id
        if not int(self) in Container.container.keys():
            Container.container[int(self)] = []
        self.new_id = len(Container.container[int(self)])
        Container.container[int(self)].append(self)

    # def __gt__(self, other):
    #     if int(self) > int(other):
    #         return True
    #     return False

    # def __eq__(self, other):
    #     if not int(self) == int(other):
    #         return False
    #     if not self.new_id == other.new_id:
    #         return False
    #     return True

    # def __lte__(self, other):
    #     if int(self) < int(other):
    #         return True
    #     if int(self) == int(other):
    #         if self.new_id > other.new_id:
    #             return True
    #     return False

def filling(available_containers, liters_left, current_containers=None):
    if not current_containers:
        current_containers = []
    if liters_left == 0:
        yield current_containers
        return
    possible_choices = [x for x in available_containers if x <= liters_left]
    for container in possible_choices:
        new_liters_left = liters_left - container
        choices = possible_choices.copy()
        choices.remove(container)
        choices = [x for x in choices if x <= container and x.id > container.id]
        current = current_containers.copy()
        current.append(container)
        yield from filling(choices, new_liters_left, current)

def fill_containers(liters, containers):
    sorted_list = sorted(containers, reverse=True)
    actual_containers = [Container(x) for x in sorted_list]
    gen = filling(actual_containers, liters)
    count = 0
    while True:
        try:
            x = next(gen)
        except StopIteration:
            break
        
        if sum(x) == liters:
            count += 1
        
    print(count)
    return count

def minimum_containers(liters, containers):
    sorted_list = sorted(containers, reverse=True)
    actual_containers = [Container(x) for x in sorted_list]
    gen = filling(actual_containers, liters)
    lengths = {}
    count = 0
    while True:
        try:
            x = next(gen)
        except StopIteration:
            break
        l = len(x)
        if not l in lengths.keys():
            lengths[l] = 0
        lengths[l] += 1
    print(lengths[min(lengths.keys())])

test_containers = [5, 10, 15, 20, 5]
fill_containers(25, test_containers)

day_one_containers = [11, 30, 47, 31, 32, 36, 3, 1, 5, 3, 32, 36, 15, 11, 46, 26, 28, 1, 19, 3]
fill_containers(150, day_one_containers)

day_two_containers = [11, 30, 47, 31, 32, 36, 3, 1, 5, 3, 32, 36, 15, 11, 46, 26, 28, 1, 19, 3]
minimum_containers(150, day_one_containers)
