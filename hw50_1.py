import copy


def transBinary(i: int, n: int):
    code = ''
    while i != 0:
        remain = i % 2
        code = str(remain)+code
        i = i//2
    while len(code) < n:
        code = '0' + code
    return code


def getArrangeCode(n: int):
    arrangeCode = []
    for i in range(2**n):
        code = transBinary(i, n)
        arrangeCode.append(code)
    return arrangeCode


def getNextIndex(arrangeCode: str, nowIndex: int):
    for i in range(nowIndex+1, len(arrangeCode)):
        if arrangeCode[i] == '1':
            return i
    return -1


def getFirstIndex(arrangeCode: str):
    for i in range(len(arrangeCode)):
        if arrangeCode[i] == '1':
            return i
    return -1


def isQualify(path_cpy: list, meetings: list, rooms_time: list):
    rooms_time_cpy = copy.deepcopy(rooms_time)
    for i in path_cpy:
        meetIndex = i[0]
        roomIndex = i[1]
        start = int(meetings[meetIndex][0])
        end = int(meetings[meetIndex][1])
        for j in range(start, end):
            if rooms_time_cpy[roomIndex][j] == 1:
                return 0
            else:
                rooms_time_cpy[roomIndex][j] = 1
    return 1


def getTime(path: list, meetings: list, rooms_time: list):
    time = 0
    rooms_time_cpy = copy.deepcopy(rooms_time)
    for i in path:
        meetIndex = i[0]
        roomIndex = i[1]
        start = int(meetings[meetIndex][0])
        end = int(meetings[meetIndex][1])
        for j in range(start, end):
            time += 1
    return time


def findCodeMaxTime(arrangeCode: str, peoples: list, meetings: list, rooms_people: list, canPutIn: list, rooms_time: list):
    queue = []
    path = []
    finalPath = []
    currentIndex = getFirstIndex(arrangeCode)  # 找到第一個為1（有被選擇的）的 index
    for i in canPutIn[currentIndex]:
        path = []
        path.append([currentIndex, i])
        queue.append(path)
    while len(queue) > 0:
        path = queue.pop(0)
        currentIndex = path[-1][0]
        nextIndex = getNextIndex(arrangeCode, currentIndex)  # 找到下一個為-1的index
        if nextIndex == -1:
            finalPath.append(path)  # 若下一個index 回傳為-1 表示已找完
            continue
        for m in canPutIn[nextIndex]:
            path_cpy = path.copy()
            path_cpy.append([nextIndex, m])
            if isQualify(path_cpy, meetings, rooms_time) == 1:  # 如果此會議可以成功排進的話,則加進queue裡
                queue.append(path_cpy)
    time = 0
    maxTime = 0
    for _path in finalPath:
        time = getTime(_path, meetings, rooms_time)
        if time > maxTime:
            maxTime = time
    return (maxTime)


def arrangeMeeting(peoples: list, meetings: list, rooms_people: list, canPutIn: list, rooms_time: list, n: list):
    arrangeCodes = getArrangeCode(n)  # 產生排列編碼
    maxTime = 0
    time = 0
    for arrangeCode in arrangeCodes:
        time = findCodeMaxTime(arrangeCode, peoples,  # 找出此會議編碼可排列出的最大時數
                               meetings, rooms_people, canPutIn, rooms_time)
        if time > maxTime:
            maxTime = time
    print(maxTime)


def getCanPutIn(rooms_people: list, peoples: list):
    canPutIn = []
    l = len(peoples)
    for i in range(len(peoples)):
        temp = []
        for j in range(len(rooms_people)):
            if rooms_people[j] >= peoples[i]:
                temp.append(j)
        canPutIn.append(temp)
    return canPutIn


def process():
    _input = input().split()
    m = int(_input[0])
    n = int(_input[1])
    if m == 0 or n == 0:
        print('0')
        return
    rooms_people = []  # 會議室可容納人數
    peoples = []  # 會議人數
    meetings = []  # 會議時段
    canPutIn = []  # 會議可被放進哪幾間會議室
    for i in range(m):
        _input = input().split()
        rooms_people.append(int(_input[1]))
    for i in range(n):
        _input = input().split()
        peoples.append(int(_input[1]))
        meetings.append(_input[2:])
    canPutIn = getCanPutIn(rooms_people, peoples)  # 判斷會議可被安排至哪幾間會議室
    rooms_time = []
    for i in range(m):
        t = [0]*24
        rooms_time.append(t)
    arrangeMeeting(peoples, meetings, rooms_people, canPutIn, rooms_time, n)


process()
