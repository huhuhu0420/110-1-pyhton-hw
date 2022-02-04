def check(M, N, data, code):
    sec = []
    timeCount = []
    for i in range(len(data)):
        if code[i] == '1':
            sec = sec + data[i]
    # print(sec)
    timeCount = [sec.count(i) for i in range(24)]
    if max(timeCount) > M:
        return False, 0
    else:
        return True, sum(timeCount)


def getCode(x, N):
    code = ''
    for i in range(N):
        if x > 0:
            code = code + str(x % 2)
            x = x//2
        else:
            code = code + str('0')
    return code


def gen(M: int, N: int, data: list):
    maxValue = 0
    for x in range(2**N):
        code = getCode(x, N)
        flag, count, = check(M, N, data, code)
        #print(flag, count)
        if flag == True and count > maxValue:
            maxValue = count
    print(maxValue)


def process():
    x = input().split()
    M, N = int(x[0]), int(x[1])
    data = []
    for i in range(N):
        x = input().split()
        s, n = int(x[1]), int(x[2])
        data.append([s, n])
    td = [[t for t in range(d[0], d[1])] for d in data]
    print(td)
    gen(M, N, td)


process()
#data = [[1,3], [1, 3], [3, 4], [1, 5]]
#data = [[1,2], [1,2], [3], [1,2,3,4]]
