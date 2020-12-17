input = """.#.#..##
..#....#
##.####.
...####.
#.##..##
#...##..
...##.##
#...#.#."""

face = input.split('\n')

x_limits = 0,0
y_limits = 0,0
z_limits = 0,0
w_limits = 0,0

def count_neighbours(ref_x, ref_y, ref_z, ref_w):
    check_dims = range(-1, 2)
    return len([f'{ref_x + x},{ref_y + y},{ref_z + z},{ref_w + w}' for w in check_dims for z in check_dims for y in check_dims for x in check_dims if not(x == 0 and y == 0 and z == 0 and w==0) and f'{ref_x + x},{ref_y + y},{ref_z + z},{ref_w + w}' in values])


def cycle():
    global values, x_limits, y_limits, z_limits, w_limits

    new_values = values.copy()
    new_x_limits = x_limits
    new_y_limits = y_limits
    new_z_limits = z_limits
    new_w_limits = w_limits

    for w in range(w_limits[0] - 1, w_limits[1] + 2):
        for z in range(z_limits[0] - 1, z_limits[1] + 2):
            for y in range(y_limits[0] - 1, y_limits[1] + 2):
                for x in range(x_limits[0] - 1, x_limits[1] + 2):
                    active_count = count_neighbours(x, y, z, w)
                    if f'{x},{y},{z},{w}' in values and not (2 <= active_count <= 3):
                        new_values.remove(f'{x},{y},{z},{w}')
                    elif f'{x},{y},{z},{w}' not in values and active_count == 3:
                        new_values.add(f'{x},{y},{z},{w}')
                        new_x_limits = (min(x, new_x_limits[0]), max(x, new_x_limits[1]))
                        new_y_limits = (min(y, new_y_limits[0]), max(y, new_y_limits[1]))
                        new_z_limits = (min(z, new_z_limits[0]), max(z, new_z_limits[1]))
                        new_w_limits = (min(w, new_w_limits[0]), max(w, new_w_limits[1]))
    
    # flip
    values = new_values.copy()
    x_limits = new_x_limits
    y_limits = new_y_limits
    z_limits = new_z_limits
    w_limits = new_w_limits

# set values
values = set()

for y, row in enumerate(face):
    for x, cell in enumerate(row):
        if cell == '#':
            values.add(f'{x},{y},{0},{0}')
            x_limits = (min(x, x_limits[0]), max(x, x_limits[0]))
            y_limits = (min(y, y_limits[0]), max(y, y_limits[0]))
            # z_limits = (min(z, z_limits[0]), max(z, z_limits[0]))

cycle()
cycle()
cycle()
cycle()
cycle()
cycle()
print(len(values))

