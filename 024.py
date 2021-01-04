offsets = {
    'nw': (-0.5, -0.5),
    'ne': (0.5, -0.5),
    'w': (-1, 0),
    'e': (1, 0),
    'sw': (-0.5, 0.5),
    'se': (0.5, 0.5)
}

def get_neighbours(x, y, black_tiles):
    return [(x + x_offset, y + y_offset) for x_offset, y_offset in offsets.values()]

def count_neighbours(x, y, black_tiles):
    return len([1 for x_offset, y_offset in offsets.values() if (x + x_offset, y + y_offset) in black_tiles])

def split_directions(in_directions):
    directions = []
    remaining_directions = list(in_directions)

    while remaining_directions:
        direction = remaining_directions.pop(0)
        if direction in 'ns':
            direction += remaining_directions.pop(0)
        directions.append(direction)
    return directions


black_tiles = set()
with open('024.txt') as input_file:
    all_directions = [split_directions(x) for x in input_file.read().split('\n')]

    for direction_list in all_directions:
        x, y = 0, 0

        for direction in direction_list:
            x_offset, y_offset = offsets[direction]
            x += x_offset
            y += y_offset

        if (x,y) in black_tiles:
            black_tiles.remove((x,y))
        else:
            black_tiles.add((x,y))

    print(f'Part one: {len(black_tiles)}')
    
    for day in range(100):
        new_black_tiles = black_tiles.copy()
        for x, y in black_tiles:
            to_check = set(get_neighbours(x, y, black_tiles))
            
            if count_neighbours(x, y, black_tiles) not in [1,2]:
                new_black_tiles.remove((x, y))

            for n_x, n_y in to_check:
                cnt = count_neighbours(n_x, n_y, black_tiles)

                if cnt == 2:
                    new_black_tiles.add((n_x, n_y))

        black_tiles = new_black_tiles
        print(f'Day {day + 1}: {len(black_tiles)}')