import math

def find_with_offset(x, y, y_offset):
    x_mod = 1
    y_mod = 1
    while True:
        net_val = ((x_mod * x))  - ((y_mod * y) - y_offset)
        if net_val < 0:
            x_mod += 1
        elif net_val > 0:
            y_mod += 1
        else:
            return (x_mod * x)

with open('013.txt') as f:
    earliest_time = int(f.readline().strip())
    all_buses = [bus for bus in f.readline().strip().split(',')]
    working_buses = [int(bus) for bus in all_buses if bus != 'x']
    times = [-(earliest_time % bus) + bus for bus in working_buses]

    # part one
    wait_time = min(times)
    bus = working_buses[times.index(wait_time)]
    print(wait_time * bus)

    # part two
    bus_list = ((offset, int(bus)) for offset, bus in enumerate(all_buses) if bus != 'x')
    
    processed = [next(bus_list), next(bus_list)]
    first, second = processed

    # initialise
    time = find_with_offset(first[1], second[1], second[0])
    increment = first[1] * second[1]

    for bus in bus_list:
        processed.append(bus)
        while True:
            if all([(time + offset) % bus == 0 for offset, bus in processed]):
                break
            time = time + increment
        increment *= bus[1]
    
    print(time)
    