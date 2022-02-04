import copy


def travel(spot, start, mid, end):
    queue = []
    path = []
    final_path = []
    current = ''
    path.append(start)
    queue.append(path)
    while len(queue) > 0:
        path = queue.pop(0)
        current = path[-1]
        for f in spot[current]:
            if f == end:
                path_cpy = copy.deepcopy(path)
                path_cpy.append(f)
                final_path.append(path_cpy)
                continue
            if f not in path:
                path_cpy = copy.deepcopy(path)
                path_cpy.append(f)
                queue.append(path_cpy)
    return final_path


def process():
    n, start, mid, end = input().split()
    spot = {}
    for i in range(int(n)):
        data = []
        temp = input().split()
        try:
            data = spot[temp[0]]
            data.append(temp[1])
        except KeyError:
            data = [temp[1]]
            spot[temp[0]] = data
        try:
            data = spot[temp[1]]
            data.append(temp[0])
        except KeyError:
            data = [temp[0]]
            spot[temp[1]] = data

    print(spot)
    path = travel(spot, start, mid, end)
    print(path)


process()
