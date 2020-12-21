options = {}
all_ingredients = []

with open ('021.txt') as input_file:
    labels = [(ingredients.split(' '), allergins.strip(')').split(', ')) for ingredients, allergins in [line.strip().split(' (contains ') for line in input_file.read().split('\n')]]
    
    # work out which are options
    for ingredients, allergins in labels:
        all_ingredients += ingredients
        for allergin in allergins:
            current_options = options.get(allergin, set(ingredients))
            options[allergin] = current_options.intersection(ingredients)

    confirmed = {}
    # if there is only one option, it is confirmed. Remove it from other options and repeat
    while options:
        for allergin, ingredients in options.items():
            if len(ingredients) == 1:
                confirmed[allergin] = list(ingredients)[0]
                del options[allergin]
                for i in options.values():
                    i.difference_update(ingredients)
                break

    print(f'part one: {len([i for i in all_ingredients if i not in confirmed.values()])}')
    print(f"part two: {','.join([ingredient for _, ingredient in sorted(confirmed.items(), key=lambda a: a[0])])}")



