import re

re_rule = re.compile(r'"([a-z])"')

with open('019.txt') as input_file:
    rules, tests = input_file.read().split('\n\n')

    raw_rules = {int(rule_no): rule for rule_no, rule in [rule.strip().split(': ') for rule in rules.split('\n')]}
    part_one_rules = {}
    part_two_rules = {}
    while raw_rules:
        for rule_no, rule in raw_rules.items():
            if m := re_rule.match(rule):
                part_one_rules[rule_no] = m.group(1)
                part_two_rules[rule_no] = m.group(1)
                del(raw_rules[rule_no])
                break
            else:
                required_rules = set([int(char) for char in rule.split(' ') if char not in '|'])
                if set(part_one_rules.keys()).intersection(required_rules) == required_rules:
                    options = rule.split(' | ')
                    # part one
                    part_one_rules[rule_no] = '(' + '|'.join([''.join([part_one_rules[int(sub_rule_no)] for sub_rule_no in option.split(' ')]) for option in options]) + ')'

                    # part two
                    if rule_no == 8:
                        part_two_rules[rule_no] = '(' + '|'.join([''.join([part_two_rules[int(sub_rule_no)] for sub_rule_no in option.split(' ')]) for option in options]) + ')+'
                    elif rule_no == 11:
                        first = part_two_rules[42]
                        second = part_two_rules[31]
                        part_two_rules[rule_no] = f'({first}{second}|{first}{first}{second}{second}|{first}{first}{first}{second}{second}{second}|{first}{first}{first}{first}{second}{second}{second}{second})'
                    else:
                        part_two_rules[rule_no] = '(' + '|'.join([''.join([part_two_rules[int(sub_rule_no)] for sub_rule_no in option.split(' ')]) for option in options]) + ')'

                    del(raw_rules[rule_no])
                    break
    
    re_rule_zero = re.compile('^' + part_one_rules[0] + '$')
    pass_count = 0
    for test in tests.split('\n'):
        if re_rule_zero.match(test):
            pass_count += 1
    
    print(pass_count)

    re_rule_zero = re.compile('^' + part_two_rules[0] + '$')
    pass_count = 0
    for test in tests.split('\n'):
        if re_rule_zero.match(test):
            pass_count += 1
    
    print(pass_count)