from functools import lru_cache
with open(r'input_07.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '16,1,2,0,4,2,7,1,2,14'

inputs = [int(x) for x in raw_inputs.split(',')]
inputs.sort()
mean = inputs[len(inputs)//2]
mean_adjusted = [abs(x - mean) for x in inputs]
print('Day 1:', sum(mean_adjusted))

@lru_cache(maxsize=None)
def running_sum(nr):
    if nr == 1:
        return 1
    else:
        return running_sum(nr-1)+nr

average = int(sum(inputs) / len(inputs))
average_adjusted = [running_sum(abs(x - average)) for x in inputs]
print('Day 2:',sum(average_adjusted))