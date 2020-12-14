import re, itertools, math
test = False

filename = '014.test.txt' if test else '014.txt'

def part_one(pairs):
    memory = {}
    for instr, value in pairs:
        if instr == "mask":
            mask = value
        else:
            if m := re.match(r'.+\[([0-9]+)\]', instr):
                pos = int(m.group(1))
                num_list = list(("0" * len(mask) + "{0:b}".format(int(value)))[-len(mask):])

                for idx, char in enumerate(mask):
                    if char == 'X':
                        continue
                    num_list[idx] = char
                memory[pos] = int("".join(num_list), 2)

    print(sum(memory.values()))

def part_two(pairs):
    memory = {}
    for instr, value in pairs:
        if instr == "mask":
            mask = value
        else:
            if m := re.match(r'.+\[([0-9]+)\]', instr):
                pos = int(m.group(1))
                num_list = list(("0" * len(mask) + "{0:b}".format(pos))[-len(mask):])

                for idx, char in enumerate(mask):
                    if char == '0':
                        continue
                    else:
                        num_list[idx] = char

                for p in itertools.product('01', repeat=num_list.count('X')):
                    combos = list(p)
                    new_num = int("".join([combos.pop(0) if num == "X" else num for num in num_list]), 2)
                    memory[new_num] = int(value)

    print(sum(memory.values()))

with open(filename) as f:
    pairs = [line.strip().split(' = ') for line in f.readlines()]
    part_one(pairs)
    part_two(pairs)