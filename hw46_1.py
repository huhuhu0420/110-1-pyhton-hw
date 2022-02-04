
def transBinary(i: int, n: int):
    newNum = []
    while(1):
        remain = i % 2
        newNum.insert(0, str(remain))
        i = i // 2
        if i == 0:
            break
    while (1):
        if len(newNum) == n:
            break
        newNum.insert(0, '0')
    return newNum


def getArrangeNum(n: int):
    arrangeNum = []
    newNum = []
    for i in range(2**(n)):
        newNum = transBinary(i, n)
        arrangeNum.append(newNum)
    return arrangeNum


def putInRoom(roomTime: list, meet: list, m: int):
    flag = 0
    thisRoom = -1
    for i in range(m):
        flag = 0
        for j in range(int(meet[0]), int(meet[1])):
            if roomTime[i][j] == '1':
                flag = (-1)
        if flag == -1:
            continue
        if flag == 0:
            thisRoom = i
            break
    if flag == -1:
        return 0, roomTime
    for j in range(int(meet[0]), int(meet[1])):
        roomTime[thisRoom][j] = '1'
    return 1, roomTime


def arrangeMeeting(meeting: list, m: int, n: int, arrangeNum: list):
    roomTime = []
    flag = 0
    for i in range(m):
        time = [0]*24
        roomTime.append(time)
    # print(arrangeNum)
    for i in range(n):
        if arrangeNum[i] == '1':
            flag, roomTime = putInRoom(roomTime, meeting[i], m)
            if flag == 0:
                return -1
    # print(roomTime)
    hour = 0
    for time in roomTime:
        for t in time:
            if t == '1':
                hour += 1
    return hour


def getTime(meeting: list, m: int, n: int):
    arrangeNums = getArrangeNum(n)
    # print(arrangeNums)
    maxHour = -10
    #print(arrangeMeeting(meeting, m, n, '11111'))
    for arrangeNum in arrangeNums:
        hour = arrangeMeeting(meeting, m, n, arrangeNum)
        # print(hour)
        if hour > maxHour:
            maxHour = hour
    # print(maxHour)
    return maxHour


def process():
    _input = input().split()
    m = int(_input[0])
    n = int(_input[1])
    if n == 0:
        print('0')
        return
    meeting = []
    for i in range(n):
        _input = input().split()
        meeting.append(_input[1:])
    print(meeting)
    time = getTime(meeting, m, n)
    print(time)


process()
