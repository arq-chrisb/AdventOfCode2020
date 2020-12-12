direction = {
    0: (1, 0),
    90: (0, 1),
    180: (-1, 0),
    270: (0, -1),
}

turn = {
    'L': -1,
    'R': 1
}

def part_one(instructions):
    heading, north, east = 90, 0, 0
    
    for instruction, attribute in instructions:
        if instruction in 'LR':
            heading = (heading + (turn[instruction] * attribute) + 360) % 360
        elif instruction in 'NS':
            north += attribute * (1 if instruction == 'N' else -1)
        elif instruction in 'EW':
            east += attribute * (1 if instruction == 'E' else -1)
        elif instruction == 'F':
            north_mod, east_mod = direction[heading]
            north += (attribute * north_mod)
            east += (attribute * east_mod)
    print(f'part one: {abs(east) + abs(north)}')

def part_two(instructions):
    waypoint_east, waypoint_north = 10, 1
    heading, east, north = 90, 0, 0
    for instruction, attribute in instructions:
        if instruction in 'LR':
            new_heading = (heading + (turn[instruction] * attribute) + 360) % 360
            while heading != new_heading:
                waypoint_east, waypoint_north = waypoint_north, -waypoint_east
                heading = (heading + 90) % 360
        elif instruction in 'NS':
            waypoint_north += attribute * (1 if instruction == 'N' else -1)
        elif instruction in 'EW':
            waypoint_east += attribute * (1 if instruction == 'E' else -1)
        elif instruction == 'F':
            north += (attribute * waypoint_north)
            east += (attribute * waypoint_east)
    print(f'part two: {abs(east) + abs(north)}')

with open('012.txt') as f:
    instructions = [(line.strip()[0], int(line.strip()[1:])) for line in f.readlines()]
    part_one(instructions)
    part_two(instructions)






