input = """.#.
..#
###
"""

class Grid:
    def __init__(self, x, y, z, default_value):
        self.grid = [[[default_value for _ in range(x)] for _ in range(y)] for _ in range(z)]
        self.x_len = x
        self.y_len = y
        self.z_len = z
        self.default_value = default_value
    
    def add_x(self):
        for slc in self.grid:
            for row in slc:
                row.insert(0, self.default_value)
                row.append(self.default_value)
        self.x_len += 2

    def add_y(self):
        for slc in self.grid:
            slc.insert(0, [self.default_value] * self.x_len)
            slc.append([self.default_value] * self.x_len)
        self.y_len += 2

    def add_z(self):
        self.grid.insert(0, [[self.default_value for _ in range(self.x_len)] for _ in range(self.y_len)])
        self.grid.append([[self.default_value for _ in range(self.x_len)] for _ in range(self.y_len)])
        self.z_len += 2

    def convert_to_physical(self, x, y, z):
        return self.x_len//2 + x, self.y_len//2 + y, self.z_len//2 + z
    
    def convert_to_logical(self, x, y, z):
        return -(self.x_len//2) + x, -(self.y_len//2) + y, -(self.z_len//2) + z

    def set_cell(self, x, y, z, value):
        # check for overruns
        if (self.x_len < (abs(x) * 2 + 1)):
            self.add_x()
        
        if (self.y_len < (abs(y) * 2 + 1)):
            self.add_y()

        if (self.z_len < (abs(z) * 2 + 1)):
            self.add_z()

        real_x, real_y, real_z = self.convert_to_physical(x, y, z)
        self.grid[real_z][real_y][real_x] = value

    def get_cell(self, x, y, z):
        # print(f'get_cell({x}, {y}, {z})')

        if (self.x_len < (abs(x) * 2 + 1)) or (self.y_len < (abs(y) * 2 + 1)) or (self.z_len < (abs(z) * 2 + 1)):
            return self.default_value

        real_x, real_y, real_z = self.convert_to_physical(x, y, z)
        return self.grid[real_z][real_y][real_x]
    
    def get_neighbours(self, ref_x, ref_y, ref_z):
        # print(f'get_neighbours({ref_x}, {ref_y}, {ref_z})')
        check_dims = range(-1, 2)
        # for x, y, z in [(ref_x + x, ref_y + y, ref_z + z) for z in check_dims for y in check_dims for x in check_dims if not(x == 0 and y == 0 and z == 0)]:
        #     print(x,y,z,self.get_cell(x, y, z))
        return [self.get_cell(ref_x + x, ref_y + y, ref_z + z) for z in check_dims for y in check_dims for x in check_dims if not(x == 0 and y == 0 and z == 0)]

    def print(self):
        print('************************')
        for z, slc in enumerate(self.grid):
            print(f'Slice {-(self.z_len // 2) + z}')
            for row in slc:
                print("".join(row))
            print("")

    def values(self):
        return [cell for z, slc in enumerate(self.grid) for y, row in enumerate(slc) for x, cell in enumerate(row)]
    
    def copy(self):
        new_grid = Grid(self.x_len, self.y_len, self.z_len, self.default_value)

        for z, slc in enumerate(self.grid):
            for y, row in enumerate(slc):
                for x, cell in enumerate(row):
                    logical_x = x - self.x_len//2
                    logical_y = y - self.y_len//2
                    logical_z = z - self.z_len//2
                    new_grid.set_cell(logical_x, logical_y, logical_z, cell)

        return new_grid
    
    def cycle(self):
        new_grid = self.copy()

        for z in range(-(self.z_len//2) - 1, -(self.z_len//2) + self.z_len + 1):
            for y in range(-(self.y_len//2) - 1, -(self.y_len//2) + self.y_len + 1):
                for x in range(-(self.x_len//2) - 1, -(self.x_len//2) + self.x_len + 1):
                    neighbours = self.get_neighbours(x, y, z)
                    active_count = neighbours.count('#')
                    # print(x, y, z,self.get_cell(x, y, z),active_count)
                    if self.get_cell(x, y, z) == '#' and not (2 <= active_count <= 3):
                        # print(f'processing cell {x}, {y}, {z}, setting to inactive')
                        new_grid.set_cell(x, y, z,'.')
                    elif self.get_cell(x, y, z) == '.' and 3 <= active_count <= 3:
                        # print(f'processing cell {x}, {y}, {z}, setting to active')
                        new_grid.set_cell(x, y, z,'#')
        return new_grid

face = input.split('\n')

len_x = len(face[0])
len_y = len(face)

grid = Grid(len_x, len_y, 1, '.')

# set values
for y, row in enumerate(face):
    for x, cell in enumerate(row):
        if cell != '.':
            grid.set_cell(-(len_x//2) + x, -(len_y//2) + y, 0, cell)

grid = grid.cycle()
grid = grid.cycle()
grid = grid.cycle()
grid = grid.cycle()
grid = grid.cycle()
grid = grid.cycle()
print(grid.values().count("#"))




