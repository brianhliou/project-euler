def parse_namnes_from_file(filename):
    names = []
    with open(filename) as f:
        for line in f:
            names.extend(line.replace('"', '').split(','))
    return names

def name_score(name):
    return sum(ord(c) - ord('A') + 1 for c in name)

def name_scores(names):
    names.sort()
    return sum((i + 1) * name_score(name) for i, name in enumerate(names))

if __name__ == '__main__':
    print(name_scores(parse_namnes_from_file('0022_names.txt')))
