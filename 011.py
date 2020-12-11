adjacent_seats = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if not (x == 0 and y == 0)]

def count_adjacent(x,y, waiting_area):
    len_x = len(waiting_area[0])
    len_y = len(waiting_area)
    return (len(
        [diff_x for diff_x, diff_y in adjacent_seats 
            if (0 <= (x + diff_x) < len_x) 
            and (0 <= (y + diff_y) < len_y) 
            and waiting_area[y + diff_y][x + diff_x] == '#'
        ]))

def count_line_of_sight(x,y, waiting_area):
    len_x = len(waiting_area[0])
    len_y = len(waiting_area)

    count = 0
    for diff_x, diff_y in adjacent_seats:
        new_x, new_y = x + diff_x, y + diff_y
        # while it's valid
        while (0 <= new_x < len_x) and (0 <= new_y < len_y):
            if waiting_area[new_y][new_x] == '#':
                count += 1
                break
            elif waiting_area[new_y][new_x] == 'L':
                break
            new_x += diff_x
            new_y += diff_y
    return count

def cycle(waiting_area, seat_amt, leave_amt, adj_func):
    new_waiting_area = [line[:] for line in waiting_area]

    for y, row in enumerate(waiting_area):
        for x, seat in enumerate(row):
            adj = adj_func(x, y, waiting_area)
            if seat == 'L' and adj == seat_amt:
                new_waiting_area[y][x] = '#'
            elif seat == "#" and adj >= leave_amt:
                new_waiting_area[y][x] = 'L'

    return new_waiting_area

def print_waiting_area(waiting_area):
    for row in waiting_area:
        print(''.join(row))
    print('')

def complete(waiting_area, seat_amt, leave_amt, adj_func, output):
    last_waiting_area, waiting_area = waiting_area, cycle(waiting_area, seat_amt, leave_amt, adj_func)

    while last_waiting_area != waiting_area:
        if output:
            print_waiting_area(waiting_area)
        last_waiting_area, waiting_area = waiting_area, cycle(waiting_area, seat_amt, leave_amt, adj_func)

    return(len([seat for row in waiting_area for seat in row if seat == "#"]))

with open('011.txt') as f:
    first_waiting_area = [list(line.strip()) for line in f.readlines()]
   
    print(complete(first_waiting_area, 0, 4, count_adjacent, False))
    print(complete(first_waiting_area, 0, 5, count_line_of_sight, False))