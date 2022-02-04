
def transBinary(i: int, n: int):
    num = ''
    while i != 0:
        remain = i % 2
        num = str(remain) + num
        i = i//2
    while len(num) < n:
        num = '0'+num
    return num


def getArrangeCode(n: int):
    arrangeCodes = []
    for i in range(2**n):
        code = transBinary(i, n)
        arrangeCodes.append(code)
    # print(arrangeCodes)
    return arrangeCodes


def isQualify(time: list, m: int):
    # print(time)
    for i in range(25):
        counter = 0
        for t in time:
            counter += t.count(i)
        if counter > m:
            #print(counter, i)
            return 0
    return 1


def computeHour(time: list):
    hour = 0
    for t in time:
        hour += len(t)
    return hour


def getTime(meeing: list, m: int, n: int):
    time = []
    maxHour = -1
    arrangeCode = getArrangeCode(n)
    for code in arrangeCode:
        time = []
        for c in range(n):
            if code[c] == '1':
                time.append(meeing[c])
        if isQualify(time, m) == 1:
            # print(time)
            hour = computeHour(time)
            # print(hour)
            if hour > maxHour:
                maxHour = hour
    return maxHour


def process():
    _input = input().split()
    m = int(_input[0])
    n = int(_input[1])
    meeting = []
    for i in range(n):
        temp = []
        _input = input().split()
        for j in range(int(_input[1]), int(_input[2])):
            temp.append(j)
        meeting.append(temp)
    # print(meeting)
    print(getTime(meeting, m, n))


process()
