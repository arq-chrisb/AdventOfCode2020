import math

file_name = '010.txt'

def search(starting, adapters, path):
    if not adapters:
        # return the path with the 3 jolt built-in
        return path + [starting + 3]
    for adapter in adapters:
        if adapter - starting <= 3:
            return search(adapter, [a for a in adapters if a > adapter], path + [adapter])
        # gap too big
        else:
            # return the path with the 3 jolt built-in
            return path + [starting + 3]

with open(file_name, 'r') as f:
    # read file
    adapters = sorted([int(line.strip()) for line in f.readlines()])

    # search it
    path = search(0, adapters, [0])

    diffs, essentials = [], [0]
    
    for prev, this in zip(path[:-1], path[1:]):
        diffs.append(this - prev)
        if this - prev == 3:
            if prev not in essentials:
                essentials.append(prev)
            if this not in essentials:
                essentials.append(this)

    print(f'part one answer: {diffs.count(1) * diffs.count(3)}')

    combos = 1
    for prev, this in zip(essentials[:-1], essentials[1:]):
        
        possibilities = 2**len([a for a in adapters if prev < a < this])

        # if over 3 gap, remove the "empty" combo for each 3
        if (this-prev > 3):
            possibilities -= ((this-prev) // 3)

        combos *= possibilities

    print(len(path), len(essentials))


    print(f'part two: {combos}')