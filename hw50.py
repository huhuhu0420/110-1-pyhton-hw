
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


def putInRoom(roomTime: list, rooms: list, people: int, meeting: list):
    flag = 0
    thisRoom = -1
    for i in range(len(rooms)):
        flag = 1
        if rooms[i] < people:
            flag = 0
            continue
        for j in range(int(meeting[0]), int(meeting[1])):
            if roomTime[i][j] == 1:
                flag = 0
        if flag == 1:
            thisRoom = i
            break
    if flag == 0:
        return flag, roomTime
    for j in range(int(meeting[0]), int(meeting[1])):
        roomTime[thisRoom][j] = 1
    return flag, roomTime


def getTime(roomTime: list, rooms: list, peoples: list, meetings: list, arrangeCode: str):
    flag = 0
    for i in range(len(arrangeCode)):
        if arrangeCode[i] == '1':
            flag, roomTime = putInRoom(
                roomTime, rooms, peoples[i], meetings[i])
    if flag == 0:
        return -1
    counter = 0
    print(arrangeCode)
    print(roomTime)
    for i in roomTime:
        for j in i:
            if j == 1:
                counter += 1
    return counter


def arrangeMeeting(rooms: list, peoples: list, meetings: list, n: int, m: int):
    arrangeCodes = getArrangeCode(n)
    print(arrangeCodes)
    roomTime = []
    hour = 0
    maxHour = -1
    for i in range(m):
        time = [0]*24
        roomTime.append(time)
    for arrangeCode in arrangeCodes:
        roomTime_cpy = roomTime.copy()
        hour = getTime(roomTime_cpy, rooms, peoples, meetings, arrangeCode)
        if maxHour < hour:
            maxHour = hour
    print(maxHour)
    #print(putInRoom(roomTime, rooms, peoples[0], meetings[0]))
    #print(getTime(roomTime, rooms, peoples, meetings, '1111'))


def sortlist(peoples: list, meetings: list):
    for i in range(len(peoples)):
        for j in range(len(peoples)-i-1):
            if peoples[j] < peoples[j+1]:
                peoples[j], peoples[j+1] = peoples[j+1], peoples[j]
                meetings[j], meetings[j+1] = meetings[j+1], meetings[j]


def process():
    _input = input().split()
    m = int(_input[0])
    n = int(_input[1])
    rooms = []
    peoples = []
    meetings = []
    for i in range(m):
        _input = input().split()
        rooms.append(int(_input[1]))
    for i in range(n):
        _input = input().split()
        peoples.append(int(_input[1]))
        meetings.append(_input[2:])
    room = sorted(rooms)
    sortlist(peoples, meetings)
    print(room)
    print(peoples)
    print(meetings)
    #arrangeMeeting(room, peoples, meetings, n, m)


process()
