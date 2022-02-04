import copy


def travel(spot: dict, start: str, mid: str, end: str):
    queue = []
    finalPath = []
    path = []
    queue.append([start])
    while len(queue) > 0:
        path = queue.pop(0)
        current = path[-1]
        for s in spot[current]:
            if s == end:
                path_cpy = copy.deepcopy(path)
                path_cpy.append(s)
                finalPath.append(path_cpy)
                continue
            if s not in path:
                path_cpy = copy.deepcopy(path)
                path_cpy.append(s)
                queue.append(path_cpy)
    print(finalPath)
    return finalPath


def process():
    _input = input().split()
    n = int(_input[0])
    start = _input[1]
    mid = _input[2]
    end = _input[3]
    spot = {}
    for i in range(n):
        _input = input().split()
        try:
            data = spot[_input[0]]
            data.append(_input[1])
        except KeyError:
            spot[_input[0]] = [_input[1]]
        try:
            data = spot[_input[1]]
            data.append(_input[0])
        except KeyError:
            spot[_input[1]] = [_input[0]]
    print(spot)
    finalPath = []
    answer = []
    max = -1
    finalPath = travel(spot, start, mid, end)
    if len(finalPath) == 0:
        print('no')
        return
    for path in finalPath:
        if mid in path and len(path) > max:
            answer = path
            max = len(path)
    print(answer)


process()
