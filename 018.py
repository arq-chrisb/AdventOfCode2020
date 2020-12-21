
def parse_one(equation):
    tokens = []
    word = ''
    paren_count = 0

    for chr in equation:

        if chr == "(":
            if paren_count != 0:
                word += chr
            paren_count += 1

        elif chr == ")":
            paren_count -= 1
            if paren_count != 0:
                word += chr

        elif chr == ' ' and paren_count == 0:
            if ' ' in word:
                tokens.append(parse_one(word))
            else:
                tokens.append(word)
            word = ''

        else:
            word += chr

    if word != '':
        if ' ' in word:
            tokens.append(parse_one(word))
        else:
            tokens.append(word)
    
    last = int(tokens.pop(0))

    while tokens:
        operation = tokens.pop(0)
        this = int(tokens.pop(0))
        if operation == '+':
            last += this
        elif operation == '*':
            last *= this

    return last

def parse_two(equation):
    tokens = []
    word = ''
    paren_count = 0

    for chr in equation:

        if chr == "(":
            if paren_count != 0:
                word += chr
            paren_count += 1

        elif chr == ")":
            paren_count -= 1
            if paren_count != 0:
                word += chr

        elif chr == ' ' and paren_count == 0:
            if ' ' in word:
                tokens.append(parse_two(word))
            else:
                tokens.append(word)
            word = ''

        else:
            word += chr

    if word != '':
        if ' ' in word:
            tokens.append(parse_two(word))
        else:
            tokens.append(word)
    
    # preprocess '+'
    while '+' in tokens:
        pos = tokens.index('+')
        tokens.pop(pos)
        other = int(tokens.pop(pos-1))
        tokens[pos-1] = int(tokens[pos-1]) + other

    last = int(tokens.pop(0))

    while tokens:
        operation = tokens.pop(0)
        this = int(tokens.pop(0))
        if operation == '+':
            last += this
        elif operation == '*':
            last *= this

    return last

with open('018.txt') as input:
    data = [eq.strip() for eq in input.read().split('\n') if eq.strip() != '']
    print(sum([parse_one(eq) for eq in data]))
    print(sum([parse_two(eq) for eq in data]))