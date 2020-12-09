file_name = '009.txt'

def find_sum(num, content):

    for outer_idx, outer_num in enumerate(content):
        if outer_num >= num:
            continue
        
        total = num
        for inner_idx, inner_num in enumerate(content[outer_idx:]):
            total -= inner_num

            if (total < 0):
                break
            if (total == 0):
                return content[outer_idx:outer_idx + inner_idx + 1]

with open(file_name, 'r') as f:
    content = [int(line.strip()) for line in f.readlines()]

    for idx, num in enumerate(content[25:]):
        seen = set()
        possible = [x for x in content[idx:25+idx] if x < num]
        for option in possible:
            if (num - option) in seen:
                break
            seen.add(option)
        else:
            print(f'found bad number: {num}')
            values = find_sum(num, content)
            print(f'sum was found: {min(values) + max(values)}')
