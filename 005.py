file_name = '005.txt'

def convert_boarding_pass(code):
    bin_code = list(['0' if char in ['F', 'L'] else '1' for char in list(code)])
    row = int(''.join(bin_code[:7]), 2)
    seat = int(''.join(bin_code[7:]), 2)
    return (row, seat)

if __name__ == "__main__":
    with open(file_name, 'r') as f:
        passes = [convert_boarding_pass(line.strip()) for line in f.readlines()]
        ids = sorted([b[0] * 8 + b[1] for b in passes])

        # largest id
        print(f'largest id: {ids[-1]}')

        # get the last and the seat after, if they aren't consecutive then that's it.
        for prev, this in zip(ids[:-1], ids[1:]):
            if (prev + 1) != this:
                print(f'first non-consecutive: {prev + 1}')
                break
