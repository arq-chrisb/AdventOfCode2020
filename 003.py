import functools

# right/down
part_two = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

def part_one(content, right, down):
    tree_count, index, row = 0, 0, 0
    row_len = len(content[row].strip())

    while row < len(content):
        # check for tree
        if content[row][index] == '#':
            tree_count = tree_count + 1
        
        # inc counters
        index = (index + right) % row_len
        row = row + down
    
    return tree_count

if __name__ == "__main__":
    with open('003.txt', 'r') as inp:
        content = inp.readlines()

        # part one
        print(part_one(content, 3, 1))

        # part two
        part_two_counts = [part_one(content, right, down) for right, down in part_two]
        print(functools.reduce(lambda a,b: a*b, part_two_counts))


