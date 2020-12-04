def part_one(content):
    content.sort()
    for i, num_a in enumerate(content):
        for num_b in content[i + 1:]:
            if num_a + num_b == 2020:
                return num_a * num_b
            elif num_a + num_b > 2020:
                break

def part_two(content):
    content.sort()
    for i, num_a in enumerate(content):
        for j, num_b in enumerate(content[i + 1:]):
            for num_c in content[i + j + 1:]:
                if num_a + num_b + num_c == 2020:
                    return num_a * num_b * num_c
                elif num_a + num_b + num_c > 2020:
                    break

if __name__ == "__main__":
    with open('001.txt', 'r') as inp:
        content = [int(line.strip()) for line in inp]
        print(part_one(content))
        print(part_two(content))