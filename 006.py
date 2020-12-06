import functools

file_name = '006.txt'

if __name__ == "__main__":
    with open(file_name, 'r') as f:
        data = [line.strip() for line in f.read().split('\n\n')]
        unique_set = [set(line.replace('\n', ' ').replace(' ', '')) for line in data]
        print(f'total questions with at least one yes: {sum([len(s) for s in unique_set])}')

        intersections = [functools.reduce(lambda a, b: a.intersection(b), [set(item.strip()) for item in group.split('\n')]) for group in data]
        # print('\n'.join([''.join(sorted(i)) for i in intersections]))
        print(f'total questions with all yes: {sum([len(i) for i in intersections])}')