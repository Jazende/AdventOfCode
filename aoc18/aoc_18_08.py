#node:
# header
  # - child nodes
  # - metadata
# 0+ child nodes
# 1+ metadata

with open(r'aoc_18_08.txt', 'r') as f:
    raw_input = f.read()

#raw_input = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
inputs = [int(x) for x in raw_input.strip().split(" ")]
metadata = 0

def node(inputs, positie):
    global metadata
    this_node = {'amount_of_children': 0, 'amount_of_metadata': 0,
                 'children': [], 'meta-data': [], 'value': 0}
    this_node['amount_of_children'] = inputs[positie]
    positie += 1
    this_node['amount_of_metadata'] = inputs[positie]
    positie += 1
    for nr in range(this_node['amount_of_children']):
        new_position, child = node(inputs, positie)
        positie = new_position
        this_node['children'].append(child)
    for nr in range(this_node['amount_of_metadata']):
        this_node['meta-data'].append(inputs[positie])
        metadata += inputs[positie]
        positie += 1
    if this_node['amount_of_children'] == 0:
        this_node['value'] = sum(this_node['meta-data'])
    else:
        for meta in this_node['meta-data']:
            try:
                this_node['value'] += this_node['children'][meta-1]['value']
            except IndexError:
                continue
    return positie, this_node

# print(node(inputs, 0))
print(node(inputs, 0)[1]['value'])
