import copy
import time
import math

with open('input_20.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = r'''broadcaster -> a
# %a -> inv, con
# &inv -> b
# %b -> con
# &con -> output'''

# raw_inputs = r'''broadcaster -> a, b, c
# %a -> b
# %b -> c
# %c -> inv
# &inv -> a'''

########################## DAY 20  PREP  ########################## 

object_creation = { 
    '%': { 'icon': '%', 'connections': [], 'status': 0,  },
    '&': { 'icon': '&', 'connections': [], 'inputs': [], 'prev_inputs': { }, 'latest_inputs': [] },
    'b': { 'icon': 'b', 'connections': [] }
}

base_objects = {}

for inp in raw_inputs.strip().split('\n'):
    name = "".join(inp.split(' ->')[0][1:])
    base_values = copy.deepcopy(object_creation[inp[0]])
    for connection in inp.split('-> ')[1].split(', '):
        base_values['connections'].append(connection)
    base_objects[name] = base_values

for obj in base_objects:
    if not base_objects[obj]['icon'] == '&':
        continue
    
    for other_obj in base_objects:
        if obj in base_objects[other_obj]['connections']:
            base_objects[obj]['inputs'].append(other_obj)
            base_objects[obj]['prev_inputs'][other_obj] = 0

########################## DAY 20 PART 1 ########################## 

objects = copy.deepcopy(base_objects)

starting_obj = 'roadcaster'

count = 1_000
pulse_count_lo = 0
pulse_count_hi = 0

list_shown = []

for _ in range(count):
    # start each round with low pulse sent to [b]roadcaster, which sends the same pulse to all connected 
    pulses = [(starting_obj, 0, None)]
    while True:
        if len(pulses) == 0:
            break
        pulse_tar, pulse_strength, pulse_origin = pulses.pop(0)

        if pulse_strength == 0:
            pulse_count_lo += 1
        else:
            pulse_count_hi += 1

        if not pulse_tar in objects:
            if not pulse_tar in list_shown:
                print(f'{pulse_tar=} not in objects')
                list_shown.append(pulse_tar)
            continue

        match objects[pulse_tar]['icon']:
            case 'b':
                for connection in objects[pulse_tar]['connections']:
                    pulses.append( (connection, pulse_strength, pulse_tar) )

            case '%': 
                if pulse_strength == 0:
                    # TODO: rewrite this concise
                    if objects[pulse_tar]['status'] == 0:
                        objects[pulse_tar]['status'] = 1
                        for connection in objects[pulse_tar]['connections']:
                            pulses.append( (connection, 1, pulse_tar) )
                    elif objects[pulse_tar]['status'] == 1:
                        objects[pulse_tar]['status'] = 0
                        for connection in objects[pulse_tar]['connections']:
                            pulses.append( (connection, 0, pulse_tar) )

            case '&':
                objects[pulse_tar]['prev_inputs'][pulse_origin] = pulse_strength

                if not pulse_origin in objects[pulse_tar]['latest_inputs']:
                    if len(objects[pulse_tar]['latest_inputs']) == 2 or len(objects[pulse_tar]['latest_inputs']) == 1:
                        objects[pulse_tar]['latest_inputs'] = [pulse_origin, objects[pulse_tar]['latest_inputs'][0]]
                    else:
                        objects[pulse_tar]['latest_inputs'] = [pulse_origin]
                else:
                    if len(objects[pulse_tar]['latest_inputs']) == 2:
                        if pulse_tar == objects[pulse_tar]['latest_inputs'][0]:
                            pass
                        else:
                            objects[pulse_tar]['latest_inputs'] = [pulse_origin, objects[pulse_tar]['latest_inputs'][0]]
                    elif len(objects[pulse_tar]['latest_inputs']) == 1:
                        pass
                    else:
                        objects[pulse_tar]['latest_inputs'] = [pulse_origin]

                if all(value == 1 for value in objects[pulse_tar]['prev_inputs'].values()):
                    for connection in objects[pulse_tar]['connections']:
                        pulses.append( (connection, 0, pulse_tar) )
                else:
                    for connection in objects[pulse_tar]['connections']:
                        pulses.append( (connection, 1, pulse_tar) )

print(f'\nAfter {count} button presses have {pulse_count_lo=} and {pulse_count_hi=} for total: {max(pulse_count_lo, 1) * max(pulse_count_hi, 1)}')

########################## DAY 20 PART 2 ########################## 

objects = copy.deepcopy(base_objects)

# 1- Figure out what needs tracking
target = [obj for obj in objects if 'rx' in objects[obj]['connections']][0]
    # Sources are double-layered as to partition off the input binaries
sources = {inp: objects[objects[inp]['inputs'][0]]['inputs'] for inp in objects[target]['inputs']}

tracking_objs = {}
for value in sources.values():
    for v in value:
        tracking_objs[v] = { 0: None, 1: None }

# 2- Track nrs until 1 cycle

starting_obj = 'roadcaster'
count = 0
rx_0_pulses = 0
while True:
    for obj in tracking_objs:
        if tracking_objs[obj][1] is None:
            if objects[obj]['status'] == 1:
                tracking_objs[obj][1] = count
        elif tracking_objs[obj][0] is None:
            if objects[obj]['status'] == 0:
                tracking_objs[obj][0] = count

    # start each round with low pulse sent to [b]roadcaster, which sends the same pulse to all connected 
    pulses = [(starting_obj, 0, None)]
    while True:
        if len(pulses) == 0:
            break
        pulse_tar, pulse_strength, pulse_origin = pulses.pop(0)

        if pulse_strength == 0:
            pulse_count_lo += 1
        else:
            pulse_count_hi += 1

        if pulse_tar == 'rx' and pulse_count_lo:
            rx_0_pulses += 1
            continue

        match objects[pulse_tar]['icon']:
            case 'b':
                for connection in objects[pulse_tar]['connections']:
                    pulses.append( (connection, pulse_strength, pulse_tar) )

            case '%': 
                if pulse_strength == 0:
                    # TODO: rewrite this concise
                    if objects[pulse_tar]['status'] == 0:
                        objects[pulse_tar]['status'] = 1
                        for connection in objects[pulse_tar]['connections']:
                            pulses.append( (connection, 1, pulse_tar) )
                    elif objects[pulse_tar]['status'] == 1:
                        objects[pulse_tar]['status'] = 0
                        for connection in objects[pulse_tar]['connections']:
                            pulses.append( (connection, 0, pulse_tar) )

            case '&':
                objects[pulse_tar]['prev_inputs'][pulse_origin] = pulse_strength

                if not pulse_origin in objects[pulse_tar]['latest_inputs']:
                    if len(objects[pulse_tar]['latest_inputs']) == 2 or len(objects[pulse_tar]['latest_inputs']) == 1:
                        objects[pulse_tar]['latest_inputs'] = [pulse_origin, objects[pulse_tar]['latest_inputs'][0]]
                    else:
                        objects[pulse_tar]['latest_inputs'] = [pulse_origin]
                else:
                    if len(objects[pulse_tar]['latest_inputs']) == 2:
                        if pulse_tar == objects[pulse_tar]['latest_inputs'][0]:
                            pass
                        else:
                            objects[pulse_tar]['latest_inputs'] = [pulse_origin, objects[pulse_tar]['latest_inputs'][0]]
                    elif len(objects[pulse_tar]['latest_inputs']) == 1:
                        pass
                    else:
                        objects[pulse_tar]['latest_inputs'] = [pulse_origin]

                if all(value == 1 for value in objects[pulse_tar]['prev_inputs'].values()):
                    for connection in objects[pulse_tar]['connections']:
                        pulses.append( (connection, 0, pulse_tar) )
                else:
                    for connection in objects[pulse_tar]['connections']:
                        pulses.append( (connection, 1, pulse_tar) )

    count += 1

    if count >= (2048 * 2):
        break

# 3- Multiply cycles

cycles = []
for source in sources:
    source_cycle = 0
    for source_obj in sources[source]:
        source_cycle = max(source_cycle, tracking_objs[source_obj][0])
    
    print(f'{source=} {sources[source]=} {source_cycle=}')

    cycles.append(source_cycle)

print(math.lcm(*cycles))
