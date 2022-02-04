def listCopy(a: list):
    b = [0]*len(a)
    for i in range(len(a)):
        b[i] = a[i]
    return b


def findEnd(spot: dict, start: str, mid: str, end: str):
    queue = []
    queue.append([start])
    # print(queue)
    path = []
    while len(queue) > 0:
        path = queue.pop(0)
        current = path[-1]
        # print(current)
        for f in spot[current]:
            if f == end and mid in path:
                path.append(f)
                return path
            if f not in path:
                path_cpy = listCopy(path)
                path_cpy.append(f)
                #print('p =' ,path)
                queue.append(path_cpy)
        print('q = ', queue)
    return 0


def process():
    _input = input().split()
    n = int(_input[0])
    start = _input[1]
    mid = _input[2]
    end = _input[3]
    spot = dict()
    visit = []
    for i in range(n):
        data = set()
        _input = input().split()
        try:
            data = spot[_input[0]]
            data.add(_input[1])
        except KeyError:
            data.add(_input[1])
            spot[_input[0]] = data
        data = set()
        try:
            data = spot[_input[1]]
            data.add(_input[0])
        except KeyError:
            data.add(_input[0])
            spot[_input[1]] = data
    print(spot)
    visit = findEnd(spot, start, mid, end)
    final = []
    if visit == 0:
        print('No way!')
    else:
        for v in visit:
            final.append(v)
        print(len(final)-1)
        print('-'.join(final))


process()
