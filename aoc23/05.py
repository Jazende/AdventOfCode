with open('input_05.txt', 'r') as f:
    raw_inputs = f.read()

# raw_inputs = '''seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4'''

def get_values(line):
    return sorted([list(int(x) for x in y.split(' ')) for y in line.split(':')[1].strip().split('\n')], key=lambda x: x[1])

raw_data = raw_inputs.split('\n\n')

########################## DAY 5 PART 1 ########################## 

seeds       = get_values(raw_data[0])[0]
seeds_soil  = get_values(raw_data[1])
soil_fert   = get_values(raw_data[2])
fert_water  = get_values(raw_data[3])
water_light = get_values(raw_data[4])
light_temp  = get_values(raw_data[5])
temp_humid  = get_values(raw_data[6])
humid_loc   = get_values(raw_data[7])

for conversions in [ seeds_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc, ]:
    new_seeds = [None for i in range(len(seeds))]

    for conversion in conversions:
        dest_start, source_start, range_ = conversion
        for idx, seed in enumerate(seeds):
            if not new_seeds[idx] is None:
                continue
            if source_start <= seed < (source_start + range_):
                new_seeds[idx] = dest_start + seed - source_start
    
    for idx, new_seed in enumerate(new_seeds):
        if new_seeds[idx] is None:
            new_seeds[idx] = seeds[idx]
    
    seeds = new_seeds

# print(f'{min(seeds)=}')

########################## DAY 5 PART 2 ########################## 

seeds       = get_values(raw_data[0])[0]
seeds_soil  = get_values(raw_data[1])
soil_fert   = get_values(raw_data[2])
fert_water  = get_values(raw_data[3])
water_light = get_values(raw_data[4])
light_temp  = get_values(raw_data[5])
temp_humid  = get_values(raw_data[6])
humid_loc   = get_values(raw_data[7])

seed_ranges = []

for idx in range(0, len(seeds), 2):
    seed_ranges.append(
        (seeds[idx], seeds[idx] + seeds[idx + 1])
    )

seed_ranges.sort()

for seed_range in seed_ranges:
    print(f'{seed_range[0]:>11} -> {seed_range[1]:>11}')