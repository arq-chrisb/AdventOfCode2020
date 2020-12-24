def play(in_cups, biggest=9, times=100):
    curr_val, *to_move, next_val = in_cups[:5]
    cups = { in_cups[i]: in_cups[(i+1)%biggest] for i in range(biggest) }

    for _ in range(times):
        target = curr_val - 1 if curr_val > 1 else biggest
        while target in to_move:
            target = target - 1 if target > 1 else biggest

        cups[curr_val] = next_val
        cups[to_move[2]] = cups[target]
        cups[target] = to_move[0]
        curr_val = next_val

        to_move  = [cups[next_val], cups[cups[next_val]], cups[cups[cups[next_val]]]]
        next_val = cups[cups[cups[cups[next_val]]]]
    return cups

orig_cups = [int(x) for x in '463528179']
part_one_dep = play(orig_cups)
part_one = []
curr = 1
for _ in range(len(part_one_dep) - 1):
    curr = part_one_dep[curr]
    part_one.append(str(curr))

print(f"Part one: {''.join(part_one)}")

biggest = 1000000
part_two_cups = orig_cups + list(range(max(orig_cups) + 1, biggest + 1))
part_two_dep = play(part_two_cups, biggest, 10000000)

print(f"Part two: {part_two_dep[1] * part_two_dep[part_two_dep[1]]}")

