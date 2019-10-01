#dijkstra: https://github.com/mburst/dijkstras-algorithm/blob/master/dijkstras.py
import heapq
import sys
from itertools import permutations

class Graph:
    
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, name, edges):
        self.vertices[name] = edges
    
    def shortest_path(self, start, finish):
        distances = {} # Distance from start to node
        previous = {}  # Previous node in optimal path from source
        nodes = [] # Priority queue of all nodes in Graph

        for vertex in self.vertices:
            if vertex == start: # Set root node as distance of 0
                distances[vertex] = 0
                heapq.heappush(nodes, [0, vertex])
            else:
                distances[vertex] = sys.maxsize
                heapq.heappush(nodes, [sys.maxsize, vertex])
            previous[vertex] = None
        
        while nodes:
            smallest = heapq.heappop(nodes)[1] # Vertex in nodes with smallest distance in distances
            if smallest == finish: # If the closest node is our target we're done so print the path
                path = []
                while previous[smallest]: # Traverse through nodes til we reach the root which is 0
                    path.append(smallest)
                    smallest = previous[smallest]
                return path
            if distances[smallest] == sys.maxsize: # All remaining vertices are inaccessible from source
                break
            
            for neighbor in self.vertices[smallest]: # Look at all the nodes that this vertex is attached to
                alt = distances[smallest] + self.vertices[smallest][neighbor] # Alternative path distance
                if alt < distances[neighbor]: # If there is a new shortest path update our priority queue (relax)
                    distances[neighbor] = alt
                    previous[neighbor] = smallest
                    for n in nodes:
                        if n[1] == neighbor:
                            n[0] = alt
                            break
                    heapq.heapify(nodes)
        return distances
        
    def __str__(self):
        return str(self.vertices)

raw_input = """
########### 
#0.1.....2#
#.#######.#
#4.......3#
###########
"""

with open(r'aoc_16_24.txt', 'r') as f:
    raw_input = f.read() 

def adjecant(key_one, key_two):
    if key_one[0] == key_two[0]:
        if (key_one[1] - key_two[1]) in [1, -1]:
            return True
    if key_one[1] == key_two[1]:
        if (key_one[0] - key_two[0]) in [1, -1]:
            return True
    return False

def create_representation_of_distances(raw_input):
    expanded = [[char for char in line] for line in raw_input.strip().split('\n')]
    all_keys_grids = {(idx_x, idx_y): None for idx_y, line in enumerate(expanded) for idx_x, char in enumerate(line) if char == "." or char in "0123456789"}
    positional_grid = {key: [adjecant_key for adjecant_key in all_keys_grids.keys() if adjecant(adjecant_key, key)] for key in all_keys_grids.keys()}
    letters_locations = {char: (idx_x, idx_y) for idx_y, line in enumerate(expanded) for idx_x, char in enumerate(line) if char in "0123456789"}

    g = Graph()
    for key, value in positional_grid.items():
        g.add_vertex(key, {v: 1 for v in value})

    distances = {}

    for letter in letters_locations.keys():
        distances[letter] = {}
        for other_letter in [l for l in letters_locations.keys() if not l == letter]:
            distances[letter][other_letter] = len(g.shortest_path(letters_locations[letter], letters_locations[other_letter]))

    return distances

def find_shortest_path(distances, start, day=1):
    g = Graph()
    for key, values in distances.items():
        g.add_vertex(key, values)

    solutions = []
    current_solution = [1_000_000_000]

    keys_for_permutations = "".join([key for key in distances.keys() if not key == start])

    for perm in permutations(keys_for_permutations, len(keys_for_permutations)):
        if day == 1:
            path = [start] + [x for x in perm]
        elif day == 2:
            path = [start] + [x for x in perm] + [start]
        directions = [path[0]]
        for idx in range(len(path)-1):
            directions += g.shortest_path(path[idx], path[idx+1])[::-1]
        lengths = []

        for idx in range(len(directions)-1):
            lengths.append(distances[directions[idx]][directions[idx+1]])

        solutions.append([sum(lengths), path, directions, lengths])
        if sum(lengths) < current_solution[0]:
            current_solution = [sum(lengths), path, directions, lengths]
            print("new shortest:", path, sum(lengths))

    return current_solution

print(find_shortest_path(create_representation_of_distances(raw_input), '0', day=1))
print(find_shortest_path(create_representation_of_distances(raw_input), '0', day=2))