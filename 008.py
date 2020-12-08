file_name = '008.txt'

def validate(content):
    current_line, accumulator, visited = 0, 0, []
    
    while True:
        visited.append(current_line)
        new_line = current_line + 1
        (instruction, argument) = content[current_line]

        if instruction == 'acc':
            accumulator += argument
        elif instruction == 'jmp':
            new_line = current_line + argument

        if new_line in visited:
            return (False, accumulator, visited)
        elif new_line >= len(content):
            return (True, accumulator, visited)

        current_line = new_line

with open(file_name, 'r') as f:
    content = [(instruction, int(argument)) for instruction, argument in (line.strip().split(' ') for line in f.readlines())]
    
    completed, accumulator, visited = validate(content)
    print(f'accumulator value at end: {accumulator}\n{"-".join([str(v) for v in visited])}')

    potentials = [(idx, 'jmp' if instruction == 'nop' else 'nop' ) for idx, (instruction, argument) in enumerate(content) if instruction in ['jmp', 'nop']]

    # try flipping each potentials
    for idx, new_instruction in potentials:
        new_content = content[:]
        new_content[idx] = (new_instruction, new_content[idx][1])

        completed, accumulator, visited = validate(new_content)

        if completed:
            print(f'successful run, accumulator value at end: {accumulator}\n{"-".join([str(v) for v in visited])}')
            break



