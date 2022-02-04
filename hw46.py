

def trans(num: int, g: int, n: int):
    newNum = []
    while(1):
        remain = num % g
        newNum.insert(0, str(remain))
        num = num // g
        if num == 0:
            break
    while (1):
        if len(newNum) == n:
            break
        newNum.insert(0, '0')
    return newNum


def isQualify(time: list, meet: list):
    timeCpy = [0]*len(time)
    for i in range(len(time)):
        timeCpy[i] = time[i]
    for i in range(int(meet[0]), int(meet[1])):
        if time[i] == 0:
            time[i] = 1
        else:
            return 0
    return time


def getTime(meeting: list, num: str, m: int, n: int):
    room = []
    # num = str(num)
    for i in range(m+1):
        time = [0]*24
        room.append(time)
    for i in range(n):
        roomNum = int(num[i])
        if roomNum != 0:
            room[roomNum] = isQualify(room[roomNum], meeting[i])
            if room[roomNum] == 0:
                return -1
            # print(room[roomNum])
    # print(room)
    hour = 0
    for r in room:
        for j in r:
            if j == 1:
                hour += 1
    return hour


def isZeroTooMuch(num: str, m: int):
    notZero = set()
    countN = 0
    for i in num:
        if i != '0':
            countN += 1
            notZero.add(i)
    if len(notZero) < m or countN < m:
        return 1
    return 0


def arrange(meeting: list, m: int, n: int):
    num = []
    for i in range((m+1)**n):
        newNum = trans(i, m+1, n)
        num.append(newNum)
    # for _num in num:
    #    print(_num)
    for i in range(len(num)-1, -1, -1):
        if isZeroTooMuch(num[i], m) == 1:
            # print(num[i])
            num.pop(i)
    # for _num in num:
    #    print(_num)
    maxHour = -100
    hour = 0
    maxi = -1
    for i in num:
        hour = getTime(meeting, i, m, n)
        if hour > maxHour:
            maxHour = hour
            maxi = i
    print(maxi)
    return maxHour


def computeTime(meeting: list):
    sum = 0
    for s, t in meeting:
        sum += (int(t)-int(s))
    return sum


def process():
    _input = input().split()
    m = int(_input[0])
    n = int(_input[1])
    meeting = []
    for i in range(n):
        _input = input().split()
        meeting.append(_input[1:])
    if m >= n:
        print(computeTime(meeting))
        return
    # print(meeting)
    print(arrange(meeting, m, n))


process()
