data = "6,3,15,13,1,0"

numbers = list(map(lambda num: int(num), data.split(',')))

def iterate(numbers, iterations):
    history = {}
    turn = 1
    # if there wasn't an answer for the last one?
    if numbers[-1] not in numbers[:-1]:
        # add 0
        numbers.append(0)

    while turn <= iterations:
        this_number = numbers.pop(0)
        if this_number in history:
            numbers.append(turn - history[this_number])
        elif not numbers:
            numbers.append(0)

        history[this_number] = turn
        turn += 1

    print(this_number)

iterate(numbers[:], 2020)
iterate(numbers[:], 30000000)
