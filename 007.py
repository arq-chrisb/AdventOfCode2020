import re

file_name = '007.txt'

def parse_bags(input):
    input = input.strip('.')
    if input == 'no other bags':
        return []
    
    contents = []
    for bag in input.split(', '):
        if res := re.match(r'([0-9]+) (.+) bags*', bag):
            contents += [res.group(2)] * int(res.group(1))
    return contents

if __name__ == "__main__":
    with open(file_name, 'r') as f:
        contents = [row.strip().split(' bags contain ') for row in f.readlines()]
        bags = [(target, parse_bags(contains)) for target, contains in contents]

        found, remaining = set(), set(['shiny gold'])

        while remaining:
            new_remaining = set()
            for colour, children in bags:
                if set(children).intersection(remaining):
                    found.add(colour)
                    new_remaining.add(colour)
            
            remaining = new_remaining

        print(f'number containing shiny gold: {len(found)}')
        
        bag_dict = dict(bags)
        found, remaining = [], ['shiny gold']
        while remaining:
            search = remaining.pop(0)
            found = found + bag_dict[search]
            remaining = remaining + bag_dict[search]
        
        print(f'number of bags inside shiny gold: {len(found)}')
