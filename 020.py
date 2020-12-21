import math
import time
from copy import deepcopy
from functools import reduce



sea_monster_mask = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.split('\n')


def sea_monster_at(map_data, x, y):
    for y_mod, row in enumerate(sea_monster_mask):
        for x_mod, char in enumerate(row):
            if char == "#" and map_data[(y + y_mod) * map_side + (x + x_mod)] != "#":
                return False
    return True

def get_all_sides(layout, side):
    top = get_top(layout, side)
    right = get_right(layout, side)
    bottom = get_bottom(layout, side)
    left = get_left(layout, side)
    return set([top, right, bottom, left, ''.join(reversed(top)), ''.join(reversed(right)), ''.join(reversed(bottom)), ''.join(reversed(left))])

def print_puzzle(puzzle, puzzle_side):
    print('')
    for y in range(puzzle_side):
        out = []
        for x in range(puzzle_side):
        
            idx = y * puzzle_side + x
            if t := puzzle[idx]:
                out.append(f"{t['tile_no']} R{str(t['rotation'])} F{str(t['flip'])}")
            else:
                out.append('**********')
        print(' | '.join(out))
    print('')

def get_left(layout, side):
    return layout[0::side]

def get_top(layout, side):
    return layout[0:side]

def get_right(layout, side):
    return layout[side-1::side]

def get_bottom(layout, side):
    return layout[-side:]

def flip(layout, side):
    return ''.join(reversed([layout[row_no*side:(row_no+1)*side] for row_no in range(side)]))

def rotate(layout, side): 
    return ''.join([layout[(side*(side-1)) + row_no::-side] for row_no in range(side)])

def solve(puzzle, available_tiles, puzzle_side, tile_side):
    # if puzzle is full, return puzzle
    if puzzle.count(None) == 0:
        return puzzle

    # find the first empty spot in the puzzle
    target = puzzle.index(None)

    desired_left = get_right(puzzle[target - 1]['layout'], tile_side) if (target - 1) > 0 and (target % puzzle_side) != 0 else None
    desired_top = get_bottom(puzzle[target - puzzle_side]['layout'], tile_side) if (target - puzzle_side) >= 0 else None

    left_tile_no = puzzle[target - 1]['tile_no'] if (target - 1) > 0 and (target % puzzle_side) != 0 else None
    top_tile_no = puzzle[target - puzzle_side]['tile_no'] if (target - puzzle_side) >= 0 else None

    # for each available tiles
    for tile in available_tiles:

        if left_tile_no and left_tile_no not in tile['candidates']:
            continue
        
        if top_tile_no and top_tile_no not in tile['candidates']:
            continue

        # for each flip
        for _ in range(2):
            # flip
            tile['layout'] = flip(tile['layout'], tile_side)
            tile['flip'] = (tile['flip'] + 1) % 2

            # for each rotation
            for _ in range(4):
                # rotate it
                tile['layout'] = rotate(tile['layout'], tile_side)
                tile['rotation'] = (tile['rotation'] + 1) % 4

                # does this fit with the left?
                if desired_left and desired_left != get_left(tile['layout'], tile_side):
                    # print(f"{tile_no} doesn't fit with left ({puzzle[target - 1]['tile_no']})")
                    continue

                # does it fit with above?
                if desired_top and desired_top != get_top(tile['layout'], tile_side):
                    # print(f"doesn't fit with top {puzzle[target - puzzle_side]['tile_no']}")
                    continue
                
                # put it in the grid
                new_puzzle = puzzle[:]
                new_puzzle[target] = tile

                # remove tile from available tiles
                new_av = deepcopy(available_tiles)
                new_av.remove(tile)

                # print(f'---> {tile_no} fits, going deeper')
                # print_puzzle(new_puzzle, puzzle_side)
                # print([k for k in new_av])
                # time.sleep(0.25)

                if res := solve(new_puzzle, new_av, puzzle_side, tile_side):
                    return res
    else:
        return None


assert flip('123456789', 3) == '789456123'
assert rotate(rotate(flip('123456789', 3), 3), 3) == '321654987'
assert flip(flip('123456789', 3), 3) == '123456789'
assert rotate('123456789', 3) == '741852963'
assert rotate(rotate('123456789', 3), 3) == '987654321'
assert rotate(rotate(rotate('123456789', 3), 3), 3) == '369258147'
assert rotate(rotate(rotate(rotate('123456789', 3), 3), 3), 3) == '123456789'

print('preprocessing..')

with open('020.txt') as input_file:
    tiles = { content.split('\n')[0][5:-1] : { 'tile_no': content.split('\n')[0][5:-1], 'layout': ''.join(content.split('\n')[1:]), 'rotation': 0, 'flip': 0 } for content in [tile.strip() for tile in input_file.read().split('\n\n')]}
    puzzle_side = math.isqrt(len(tiles))
    tile_side = math.isqrt(len(tiles[list(tiles.keys())[0]]['layout']))

    # get sides
    for tile_no, tile in tiles.items():
        tile['sides'] = get_all_sides(tile['layout'], tile_side)
        tile['candidates'] = set()

    for tile_no, tile in tiles.items():
        for other_tile_no, other_tile in tiles.items():
            if tile_no == other_tile_no:
                continue
            
            if tile['sides'].intersection(other_tile['sides']):
                tile['candidates'].add(other_tile_no)
                other_tile['candidates'].add(tile_no)

    # create a new grid
    puzzle = [None] * puzzle_side**2

    available_tiles = sorted([val for _, val in tiles.items()], key=lambda t: len(t['candidates']))

    print('solving...')
    layout = solve(puzzle, available_tiles, puzzle_side, tile_side)
    print_puzzle(layout, puzzle_side)
    part_one = reduce(lambda x, y: x * y, [int(tile['tile_no']) for pos, tile in enumerate(layout) if pos in [0, puzzle_side-1, puzzle_side**2 - puzzle_side, puzzle_side**2 - 1]])
    print(f'Sum for part one: {part_one}')

    map_data = ''.join([layout[y * puzzle_side + x]['layout'][r*tile_side + 1:(r+1)*tile_side - 1]
        for y in range(puzzle_side)
        for r in range(1,tile_side - 1)
        for x in range(puzzle_side)
    ])

    map_side = math.isqrt(len(map_data))

    count = 0
    for _ in range(2):
        map_data = flip(map_data, map_side)
        for _ in range(4):
            map_data = rotate(map_data, map_side)
            for y in range(map_side - len(sea_monster_mask)):
                for x in range(map_side - len(sea_monster_mask[0])):
                    if sea_monster_at(map_data, x, y):
                        count += 1

    print(f'Part two: {map_data.count("#") - (count * 15)}')




