import re
from operator import attrgetter
from itertools import permutations
from functools import partial
from copy import deepcopy
import cProfile

with open(r'22_16.txt', 'r') as f:
    raw_lines = f.read().strip()

re_valve = re.compile('Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z\, ]+)')

def calculate_paths(valves, start_valve):
    for valve in valves:
        valve.reset_path()

    start_valve.shortest_path = [start_valve]

    valves_to_test = [start_valve, ]

    while True:
        if len(valves_to_test) == 0:
            break

        next_test = valves_to_test.pop(0)

        for connection in next_test.connections:
            path = [node for node in next_test.shortest_path] + [connection]

            if connection.shortest_path is None:
                connection.shortest_path = path
                valves_to_test.append(connection)

            elif len(path) < len(connection.shortest_path):
                connection.shortest_path = path
                valves_to_test.append(connection)

    return valves

class Valve:
    def __init__(self, name, rate, connections):
        self.name = name
        self.rate = rate
        self.open = False
        self.connections = []
        self.shortest_path = None
        self.connections_str = connections
        self.shortest_paths = {}

    def reset_path(self):
        self.shortest_path = None

    def __repr__(self):
        return f'{self.name} @ {self.rate}'

valves = [Valve(valve[0], int(valve[1]), valve[2].split(', ')) for valve in re_valve.findall(raw_lines)]
for valve in valves:
    valve.connections = [[v for v in valves if v.name == connection_str][0] for connection_str in valve.connections_str]
start_valve = [valve for valve in valves if valve.name == 'AA'][0]
for idx in range(len(valves)):
    ref_valve = valves[idx]
    valves = calculate_paths(valves, ref_valve)

    for valve in valves:
        if valve.rate == 0 and not valve == start_valve:
            continue
        if valve == ref_valve:
            continue
        ref_valve.shortest_paths[valve.name] = valve.shortest_path[1:] # This only counts path
interesting_valves = [valve for valve in valves if valve.rate > 0 or valve.name == 'AA']

def routing(valves, start_valve, max_time):
    all_open_valves_rate = sum(valve.rate for valve in valves)
    routes = [{'path': [start_valve], 'steps': 0, 'open_valves': [], 'pressure_relieved': 0}]
    max_pressure = 0
    max_pressure_route = None

    while True:
        try:
            route = routes.pop(0)
        except IndexError:
            return (max_pressure, max_pressure_route['path'])

        # If all valves with rates are open (+ 1 to account for AA); calculate remaining pressure and find max
        if len(route['open_valves']) + 1 == len(valves):
            if route['steps'] < max_time:
                steps_remaining = max_time - route['steps']
                route['pressure_relieved'] += sum(valve.rate for valve in route['open_valves']) * steps_remaining
                route['steps'] += steps_remaining
            if route['pressure_relieved'] > max_pressure:
                max_pressure = route['pressure_relieved']
                max_pressure_route = route
            continue

        # Calculate if this current route can ever still go over the current max pressure:
        max_remaining_pressure = (max_time - route['steps']) * all_open_valves_rate
        if (max_remaining_pressure + route['pressure_relieved']) < max_pressure:
            continue

        for valve in valves:
            if valve in route['path']:
                continue
            steps_taken = len(valve.shortest_paths[route['path'][-1].name]) + 1
            rate_open_valves = sum(valve.rate for valve in route['open_valves'])
            # If this next step goes over max_time; yield the route while calculating remaining pressure release
            if route['steps'] + steps_taken > max_time:
                new_route = {
                    'path': [v for v in route['path']], 
                    'steps': max_time,
                    'open_valves': route['open_valves'],
                    'pressure_relieved': route['pressure_relieved'] + ((max_time - route['steps']) * rate_open_valves),
                }
                if new_route['pressure_relieved'] > max_pressure:
                    max_pressure = new_route['pressure_relieved']
                    max_pressure_route = route
                continue
            else: # If not next step goes over max time:
                new_route = {
                    'path': [v for v in route['path']] + [valve], 
                    'steps': route['steps'] + steps_taken,
                    'open_valves': route['open_valves'] + [valve],
                    'pressure_relieved': route['pressure_relieved'] + steps_taken * rate_open_valves,
                }
                routes.append(new_route)

TIME = 30

best_pressure, best_route = routing(interesting_valves, start_valve, TIME)
print('Part 1: ', best_pressure)


# def double_routing(valves, start_valve, max_time, best_routing):
#     new_valves = [deepcopy(valve) for valve in valves if not valve in best_routing]
    
#     all_open_valves_rate = sum(valve.rate for valve in new_valves)
#     routes = [{'path': [start_valve], 'steps': 0, 'open_valves': [], 'pressure_relieved': 0}]
#     max_pressure = 0
#     max_pressure_route = None

#     while True:
#         try:
#             route = routes.pop(0)
#         except IndexError:
#             return (max_pressure, max_pressure_route['path'])

#         # If all valves with rates are open (+ 1 to account for AA); calculate remaining pressure and find max
#         if len(route['open_valves']) + 1 == len(new_valves):
#             if route['steps'] < max_time:
#                 steps_remaining = max_time - route['steps']
#                 route['pressure_relieved'] += sum(valve.rate for valve in route['open_valves']) * steps_remaining
#                 route['steps'] += steps_remaining
#             if route['pressure_relieved'] > max_pressure:
#                 max_pressure = route['pressure_relieved']
#                 max_pressure_route = route
#             continue

#         # Calculate if this current route can ever still go over the current max pressure:
#         max_remaining_pressure = (max_time - route['steps']) * all_open_valves_rate
#         if (max_remaining_pressure + route['pressure_relieved']) < max_pressure:
#             continue

#         for valve in new_valves:
#             if valve in route['path']:
#                 continue
#             steps_taken = len(valve.shortest_paths[route['path'][-1].name]) + 1
#             rate_open_valves = sum(valve.rate for valve in route['open_valves'])
#             # If this next step goes over max_time; yield the route while calculating remaining pressure release
#             if route['steps'] + steps_taken > max_time:
#                 new_route = {
#                     'path': [v for v in route['path']], 
#                     'steps': max_time,
#                     'open_valves': route['open_valves'],
#                     'pressure_relieved': route['pressure_relieved'] + ((max_time - route['steps']) * rate_open_valves),
#                 }
#                 if new_route['pressure_relieved'] > max_pressure:
#                     max_pressure = new_route['pressure_relieved']
#                     max_pressure_route = route
#                 continue
#             else: # If not next step goes over max time:
#                 new_route = {
#                     'path': [v for v in route['path']] + [valve], 
#                     'steps': route['steps'] + steps_taken,
#                     'open_valves': route['open_valves'] + [valve],
#                     'pressure_relieved': route['pressure_relieved'] + steps_taken * rate_open_valves,
#                 }
#                 routes.append(new_route)

#     return max_pressure, max_pressure_route

# TIME = 26
# first_pressure, first_route = routing(interesting_valves, start_valve, TIME)
# second_pressure, second_route = double_routing(interesting_valves, start_valve, TIME, first_route)

# print('Part 2:', first_pressure, second_pressure, first_pressure + second_pressure)


def second_routing(valves, start_valve, max_time):
    all_open_valves_rate = sum(valve.rate for valve in valves)
    routes = [{
        'path_a': [start_valve], 'steps_a': 0, 'open_valves_a': [], 'pressure_relieved_a': 0,
        'path_b': [start_valve], 'steps_b': 0, 'open_valves_b': [], 'pressure_relieved_b': 0,
    }]
    max_pressure = 0
    max_pressure_route = None
    count = 0

    while True:
        count += 1
        if count % 100 == 0:
            list_to_remove = []
            for idx, route in enumerate(routes):
                top_valves_left = [valve for valve in valves if not valve in route['path_a'] and not valve in route['path_b']]
                realistic_pathing_left_a = (max_time - route['steps_a']) // 2
                realistic_pressure_left_a = sum(valve.rate for valve in valves[:realistic_pathing_left_a]) * realistic_pathing_left_a
                realistic_pathing_left_b = (max_time - route['steps_b']) // 2
                realistic_pressure_left_b = sum(valve.rate for valve in valves[:realistic_pathing_left_b]) * realistic_pathing_left_b
                
                estimated_pressure_max = route['pressure_relieved_a'] + route['pressure_relieved_b'] + realistic_pressure_left_a + realistic_pressure_left_b

                if estimated_pressure_max < max_pressure:
                    list_to_remove.append(idx)
            print(f'Removing {len(list_to_remove)} possible routes')
            for index in list_to_remove[::-1]:
                del routes[index]
            routes.sort(key=lambda x: x['steps_a'] + x['steps_b'], reverse=True)

        try:
            route = routes.pop(0)
        except IndexError:
            return (max_pressure, max_pressure_route)

        # max_remaining_pressure = (2 * max_time - route['steps_a'] - route['steps_b'] - 1) * all_open_valves_rate
        # if max_remaining_pressure + route['pressure_relieved_a'] + route['pressure_relieved_b'] < max_pressure:
        #     continue

        for valve in valves:
            if route['steps_a'] < max_time:
                if valve in route['path_a']:
                    continue
                steps_taken = len(valve.shortest_paths[route['path_a'][-1].name]) + 1
                rate_open_valves = sum(valve.rate for valve in route['open_valves_a'])
                if route['steps_a'] + steps_taken > max_time:
                    new_route = {
                        'path_a': route['path_a'],
                        'steps_a': max_time,
                        'open_valves_a': route['open_valves_a'],
                        'pressure_relieved_a': route['pressure_relieved_a'] + ((max_time - route['steps_a']) * rate_open_valves),
                        'path_b': route['path_b'],
                        'steps_b': route['steps_b'],
                        'open_valves_b': route['open_valves_b'],
                        'pressure_relieved_b': route['pressure_relieved_b'],
                    }
                else:
                    new_route = {
                        'path_a': route['path_a'] + [valve],
                        'steps_a': route['steps_a'] + steps_taken,
                        'open_valves_a': route['open_valves_a'] + [valve],
                        'pressure_relieved_a': route['pressure_relieved_a'] + steps_taken * rate_open_valves,
                        'path_b': route['path_b'],
                        'steps_b': route['steps_b'],
                        'open_valves_b': route['open_valves_b'],
                        'pressure_relieved_b': route['pressure_relieved_b'],
                    }
                routes.append(new_route)
            else:
                if valve in route['path_a'] or valve in route['path_b']:
                    continue
                steps_taken = len(valve.shortest_paths[route['path_b'][-1].name]) + 1
                rate_open_valves = sum(valve.rate for valve in route['open_valves_b'])
                if route['steps_b'] + steps_taken > max_time:
                    new_route_press = route['pressure_relieved_a'] + route['pressure_relieved_b'] + ((max_time - route['steps_b']) * rate_open_valves)
                    if new_route_press > max_pressure:
                        new_route = {
                            'path_a': route['path_a'],
                            'steps_a': route['steps_a'],
                            'open_valves_a': route['open_valves_a'],
                            'pressure_relieved_a': route['pressure_relieved_a'],
                            'path_b': route['path_b'],
                            'steps_b': max_time,
                            'open_valves_b': route['open_valves_b'],
                            'pressure_relieved_b': route['pressure_relieved_b'] + ((max_time - route['steps_b']) * rate_open_valves),
                        }
                        max_pressure = new_route['pressure_relieved_a'] + new_route['pressure_relieved_b']
                        max_pressure_route = new_route
                    continue
                else:
                    new_route = {
                        'path_a': route['path_a'],
                        'steps_a': route['steps_a'],
                        'open_valves_a': route['open_valves_a'],
                        'pressure_relieved_a': route['pressure_relieved_a'],
                        'path_b': route['path_b'] + [valve],
                        'steps_b': route['steps_b'] + steps_taken,
                        'open_valves_b': route['open_valves_b'] + [valve],
                        'pressure_relieved_b': route['pressure_relieved_b'] + steps_taken * rate_open_valves,
                    }
                    routes.append(new_route)

TIME = 26
best_pressure, best_route = second_routing(interesting_valves, start_valve, TIME)
print(best_pressure, best_route)