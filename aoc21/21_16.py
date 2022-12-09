with open(r'input_16.txt', 'r') as f:
    raw_inputs = f.read().strip()

# raw_inputs = 'A0016C880162017C3686B18A3D4780'
# raw_inputs = 'C0015000016115A2E0802F182340'
# raw_inputs = '620080001611562C8802118E34'
# raw_inputs = '8A004A801A8002F478'
# raw_inputs = 'EE00D40C823060'
# raw_inputs = '38006F45291200'
# raw_inputs = 'D2FE28'

binary = bin(int(raw_inputs, 16))[2:].zfill(len(raw_inputs)*4) # fill up bits with 0s

def flattener(inputs):
    list_ = []
    for obj in inputs:
        if isinstance(obj, list):
            for x in flattener(obj):
                list_.append(x)
        else:
            list_.append(obj)
    return list_

def parser(inputs):
    versions = []
    data_sets = []
    bits_used = 0

    version = int(inputs[:3], 2)
    # print(inputs[:3], ' #V', version)
    versions.append(version)
    type_id = int(inputs[3:6], 2)
    # print(inputs[3:6], ' #T', type_id)
    bits_used = 6

    if type_id == 4:
        data = []
        offset = 6
        idx = 0
        while True:
            data.append(inputs[6+1+idx*5:6+5+idx*5])
            # print(inputs[6+idx*5:6+5+idx*5], ' # Data ', end="")
            if inputs[6+idx*5] in ["0", 0]:
                # print('0, end')
                break
            # else:
                # print('1, continue')
            idx += 1

        data_sets.append(data)
        bits_used += len(data)*5

    elif inputs[6] == "0":
        # print(inputs[6], '   #I 0')
        bits_used += 1
        l = int(inputs[bits_used:bits_used+15], 2)
        # print(inputs[bits_used:bits_used+15], ' #L', l)
        bits_used += 15

        while l > 0:
            # print('')
            subpacket = parser(inputs[bits_used:bits_used+l])
            versions.append(subpacket['versions'])
            data_sets.append(subpacket['data_sets'])
            bits_used += subpacket['bits_used']
            l -= subpacket['bits_used']

    elif inputs[6] == "1":
        # print(inputs[6], '   #I 1')
        l = int(inputs[7:18], 2)
        # print(inputs[7:18], ' #L', l)
        bits_used += 1 + 11
        for i in range(l):
            subpacket = parser(inputs[bits_used:])
            versions.append(subpacket['versions'])
            data_sets.append(subpacket['data_sets'])
            bits_used += subpacket['bits_used']

    return {'versions': versions, 'data_sets': data_sets, 'bits_used': bits_used}

def product(values):
    result = 1
    for val in values:
        result *= val
    return result

day_1 = parser(binary)
print(sum(flattener(day_1['versions'])))

def parser(inputs):
    versions = []
    data_sets = []
    values = []
    bits_used = 0

    version = int(inputs[0:3], 2)
    versions.append(version)
    type_id = int(inputs[3:6], 2)
    bits_used += 6

    if type_id == 4:
        data = []
        offset = 6
        idx = 0
        while True:
            data.append(inputs[6+1+idx*5:6+5+idx*5])
            if inputs[6+idx*5] in ["0", 0]:
                break
            idx += 1

        string_bin = "".join(data)
        value = int(string_bin, 2)
        values.append(value)

        data_sets.append(data)
        bits_used += len(data)*5

    else:
        bits_used += 1
        l_mod = 11 if inputs[6] == "1" else 15
        l = int(inputs[bits_used:bits_used+l_mod], 2)
        bits_used += l_mod

        while l > 0:
            if inputs[6] == "0":
                subpacket = parser(inputs[bits_used:bits_used+l])
                l -= subpacket['bits_used']
            elif inputs[6] == "1":
                subpacket = parser(inputs[bits_used:])
                l -= 1
            versions.append(subpacket['versions'])
            bits_used += subpacket['bits_used']
            data_sets.append(subpacket['data_sets'])
            values.append(subpacket["values"])
        
        vals = flattener(values)
        if type_id == 0:
            return {'versions': versions, 'data_sets': data_sets, 'bits_used': bits_used, 'values': sum(vals)}
        if type_id == 1:
            return {'versions': versions, 'data_sets': data_sets, 'bits_used': bits_used, 'values': product(vals)}
        if type_id == 2:
            return {'versions': versions, 'data_sets': data_sets, 'bits_used': bits_used, 'values': min(vals)}
        if type_id == 3:
            return {'versions': versions, 'data_sets': data_sets, 'bits_used': bits_used, 'values': max(vals)}
        if type_id == 5:
            result = 1 if vals[0] > vals[1] else 0
            return {'versions': versions, 'data_sets': data_sets, 'bits_used': bits_used, 'values': result}
        if type_id == 6:
            result = 1 if vals[0] < vals[1] else 0
            return {'versions': versions, 'data_sets': data_sets, 'bits_used': bits_used, 'values': result}
        if type_id == 7:
            result = 1 if vals[0] == vals[1] else 0
            return {'versions': versions, 'data_sets': data_sets, 'bits_used': bits_used, 'values': result}

    # print(type_id, values)

    return {'versions': versions, 'data_sets': data_sets, 'bits_used': bits_used, 'values': values}

day_2 = parser(binary)
# print(sum(flattener(day_2['versions'])))
print(day_2['values'])