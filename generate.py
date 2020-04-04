
base_path = ''

ext = ['a', 'i', 'o', 'k', 't', 'd', 'p', 'n', 'b']
end = bytes('\n', encoding='utf-8')


def get_lines(filename):
    lines = []
    with open(filename, 'r') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            lines.append(line.strip())
    file.close()
    return lines


def save(filename, data):
    with open(filename, 'wb') as file:
        for domain in data:
            b = bytes(domain, encoding='utf-8')
            file.write(b)
            file.write(end)
    file.close()


def pinyin5():
    data2 = get_lines(base_path + '2py')
    data3 = get_lines(base_path + '3py')

    domains = set()
    for p1 in data2:
        for p2 in data2:
            for o in ext:
                domains.add(p1 + p2 + o)

        for y1 in data3:
            domains.add(p1 + y1)
            domains.add(y1 + p1)

    save(base_path + '5ch', domains)


def pinyin6():
    data2 = get_lines(base_path + '2py')
    data3 = get_lines(base_path + '3py')

    domains = set()
    for p1 in data2:
        for p2 in data2:
            for p3 in data2:
                domains.add(p1 + p2 + p3)

            for o1 in ext:
                for o2 in ext:
                    domains.add(p1 + o1 + p2 + o2)

        for y1 in data3:
            for o in ext:
                domains.add(p1 + y1 + o)
                domains.add(p1 + o + y1)

    for y1 in data3:
        for y2 in data3:
            domains.add(y1 + y2)

    save(base_path + '6ch', domains)


if __name__ == '__main__':
    pinyin5()
    pinyin6()
