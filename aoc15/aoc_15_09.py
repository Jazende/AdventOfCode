import re
from itertools import permutations

with open(r'aoc_15_09.txt', 'r') as f:
    inputs = f.read().strip().split('\n')

re_route = re.compile('^(\w+) to (\w+) = (\d+)$')
get_routes = lambda x: (re_route.match(x)[1], re_route.match(x)[2], int(re_route.match(x)[3]))
routes = [get_routes(x) for x in inputs]

nodes = {}
for route in routes:
    if not route[0] in nodes.keys():
        nodes[route[0]] = {}
    if not route[1] in nodes.keys():
        nodes[route[1]] = {}

    nodes[route[0]][route[1]] = route[2]
    nodes[route[1]][route[0]] = route[2]

def traverse_tree(nodes):
    keys = nodes.keys()
    perms = permutations(keys, len(keys))
    print("Min:", length_of_route(min(perms, key=length_of_route)))
    perms = permutations(keys, len(keys))
    print("Max:", length_of_route(max(perms, key=length_of_route)))

def length_of_route(route):
    global nodes
    # Voor alle lengtes ( 0 - 1, 1- 2, len(route)-1 - len(route) ) neem lengte tussen de twee
    return sum([nodes[route[position]][route[position+1]] for position in range(len(route)-1)])

# def length_of_route(route):
#     global nodes
#     length = 0
#     for position in range(len(route)-1):
#         length += nodes[route[position]][route[position+1]]
#     return length


traverse_tree(nodes)
