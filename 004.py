import re

passport_fields = {
    'byr': r'^(19[2-9][0-9]|200[0-2])$',
    'iyr': r'^(201[0-9]|2020)$',
    'eyr': r'^(202[0-9]|2030)$',
    'hgt': r'^(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)$',
    'hcl': r'^#[a-f0-9]{6}$',
    'ecl': r'^(amb|blu|brn|gry|grn|hzl|oth)$',
    'pid': r'^[0-9]{9}$'
}

required_keys = set(passport_fields.keys())

file_name = '004.txt'

def validate(content):
    exists, valid = 0, 0
    for line in content:
        pairs = dict([pair.split(':') for pair in line.split(' ') if ':' in pair])

        if required_keys.intersection(pairs.keys()) == required_keys:
            exists += 1
            for key in required_keys:
                if not(re.match(passport_fields[key], pairs[key])):
                    break
            else:
                valid += 1

    return (exists, valid)

if __name__ == "__main__":
    with open(file_name, 'r') as inp:
        raw = inp.read()
        content = [record.replace('\n', ' ').strip() for record in raw.split('\n\n')]
        print(validate(content))