def steps(data):
    return data + "0" + data[::-1].replace('0', '2').replace('1', '0').replace('2', '1')

def create_data(input, length):
    input = str(input)
    while True:
        if len(input) >= length:
            return input
        input = steps(input)

def checksum(data, length):
    data = data[:length]
    while True:
        if len(data) % 2 == 1:
            return data
        
        new_data = ""
        for idx in range(len(data)//2):
            if data[idx*2] == data[idx*2 + 1]:
                new_data += "1"
            else:
                new_data += "0"
        data = new_data


def day_one(input, length):
    print("Creating Data")
    data = create_data(str(input), length)
    print("Creating Checksum")
    check_sum = check_sum(data, length)
    print("Result:")
    return check_sum


# print(day_one(10000, 20))
print(day_one(11011110011011101, 272))
print(day_one(11011110011011101, 35651584))