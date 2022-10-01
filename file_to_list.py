

def read_file(file):
    file = open(file, 'r', encoding='utf-8')
    lines = file.readlines()
    lines = [int(line.rstrip('\n')) for line in lines]
    file.close()
    return lines


def multiplication(list, a, b):
    mult = int(list[a])*(int(list[b]))
    return mult


lines = read_file('date.txt')
print(lines)
print(multiplication(lines, 5, 4))
