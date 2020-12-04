import re

def part_one(content):
    cnt = 0
    for line in content:
        # break up the line
        if res := re.match(r'^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$', line):
            min_num = int(res.group(1))
            max_num = int(res.group(2))
            letter = res.group(3)
            password = res.group(4)

            # count instances
            actual_num = list(password).count(letter)

            # check it
            if min_num <= actual_num <= max_num:
                cnt += 1
    return cnt

def part_two(content):
    cnt = 0
    for line in content:
        # break up the line
        if res := re.match(r'^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$', line):
            first_pos = int(res.group(1)) - 1
            second_pos = int(res.group(2)) - 1
            letter = res.group(3)
            password = res.group(4)

            # if there is one and only one instance of letter, valid!
            if [password[first_pos], password[second_pos]].count(letter) == 1:
                cnt += 1
            
    return cnt

if __name__ == "__main__":
    with open('002.txt', 'r') as inp:
        content = inp.readlines()
        print(part_one(content))
        print(part_two(content))
