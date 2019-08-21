import re

input_7 = '''pbga (66)\nxhth (57)\nebii (61)\nhavc (66)\nktlj (57)
fwft (72) -> ktlj, cntj, xhth\nqoyq (66)\npadx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft\njptl (61)\nugml (68) -> gyxo, ebii, jptl
gyxo (61)\ncntj (57)'''.split("\n")

day_7_input = []
with open("adventofcode_input_7.txt", 'r') as input7:
    for line in input7:
        day_7_input.append(line.strip())

def read_file(input_):
    programs = []
    for line in input_:
        match = re.findall("^(\w{1,10})\s\((\d{1,10})\)(?:\s->\s)?([\w,\s]*)$", line)
        if len(match[0][2]) > 0:
            programs.append([match[0][0], int(match[0][1]), match[0][2].split(", ")])
        else:
            programs.append([match[0][0], int(match[0][1]), []])

    programs.sort(key=lambda y: (y[2], y[1]*-1))
    return programs

def build_tree(input_):
    programs = read_file(input_)
    tree = []
    for x in programs:
        value = {'name': x[0], 'children': x[2], 'weight': x[1], 'parent': None, 'total_weight': 0}
        tree.append(value)
    for node in tree:
        for all_other_nodes in tree:
            if node['name'] in all_other_nodes['children']:
                node['parent'] = all_other_nodes['name']
                break
    #print([x for x in tree if x['parent'] == None][0]['name'])
    return tree

def weight_tree(input_):
    tree = build_tree(input_)
    def weight(node):
        if node['children'] == []:
            return node['weight']
        else:
            sum_ = 0
            for name in node['children']:
                child = [x for x in tree if x['name'] == name][0]
                sum_ += weight(child)
            return node['weight'] + sum_
        
    for node in tree:
        node['total_weight'] = weight(node)
    return tree

def print_tree(tree):
    parent = [x for x in tree if x['parent'] == None][0]
    levels = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    def print_node_and_children(node, offset = 0):
        # print("\t"*offset, node['name'], node['total_weight'], node['weight'])
        levels[offset].append(node)
        for child in node['children']:
            child_node = [x for x in tree if x['name'] == child][0]
            print_node_and_children(child_node, offset+1)
    print_node_and_children(parent)
    return levels
        
if __name__ == '__main__':
    # input_7
    # day_7_input
    a = weight_tree(day_7_input)
    b = print_tree(a)
    problem_node = []
    for node in a:
        if not node['children'] == []:
            children = []
            for child in node['children']:
                child_node = [x for x in a if x['name'] == child][0]
                children.append(child_node['total_weight'])
            if len(list(set(children))) > 1:
                print(node, children)
