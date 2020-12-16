import functools

field_numbers = {}

with open ('016.txt') as src_file:
    field_text, ticket_text, nearby_tickets_text = src_file.read().split('\n\n')

    fields = [field_text_line.split(': ') for field_text_line in field_text.split('\n')]
    fields = [(field_name, rule_text.split(' or ')) for field_name, rule_text in fields]
    for name, rule_list in fields:
        for rule in rule_list:
            min, max = map(lambda val: int(val), rule.split('-'))
            current_set = field_numbers.get(name, set())
            field_numbers[name] = current_set.union(set(range(min, max+1)))
    
    my_ticket = [int(item.strip()) for item in ticket_text.split('\n')[1].split(',')]
    nearby_tickets = [list(map(int, ticket.split(','))) for ticket in nearby_tickets_text.split('\n')[1:] if ticket]

    # initialise the total set of fields this can be
    possible_fields = [set([field for field, values in field_numbers.items() if num in values]) for num in my_ticket]

    bad_numbers = []
    # go through nearby tickets
    for ticket in nearby_tickets:
        # verify all numbers
        good = True
        for num in ticket:
            if len([field for field, values in field_numbers.items() if num in values]) == 0:
                bad_numbers.append(num)
                good = False
        # if there were no bad numbers..
        if good:
            for idx, num in enumerate(ticket):
                # for each field, find what fields fit (that already exist in the possible fields)
                possible_fields[idx].intersection_update(set([field for field, values in field_numbers.items() if num in values]))

    print(sum(bad_numbers))
    
    # get all fields
    remaining = list(field_numbers.keys())

    while remaining:
        for idx, field_set in enumerate(possible_fields):
            # if there is only one possibility..
            if (len(field_set) == 1) and list(field_set)[0] in remaining:
                this_field = list(field_set)[0]
                #remove from the list of remaining - to top an infinite loop
                remaining.remove(this_field)

                # go through and remove it from all other possibilities/
                for chg_idx, chg_field_set in enumerate(possible_fields):
                    if chg_idx != idx and this_field in field_set:
                        possible_fields[chg_idx].difference_update(field_set)
                break
    
    # convert from sets containing one object to a list of only values
    field_map = [list(field_set)[0] for field_set in possible_fields]

    # filter the nums based on departure
    dep_nums = [num for num, field in zip(my_ticket, field_map) if field.startswith('departure')]

    # multiply them all together
    print(functools.reduce(lambda x,y: x*y, dep_nums))
    
     
