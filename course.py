# 產生【某一課程組合】編碼  code
# N = 3，000 100 010 110 001 101 011 111
# 1 代表選取此課程排入教室
def genCoursesCode(x: int, N: int):
    code = ''
    for i in range(N):
        if x > 0:
            code = code + str(x % 2)
            x = x//2
        else:
            code = code + str('0')
    return code

# sections={節次0:[[課程人數1,課程編號1],[課程人數,課程編號], ..], 節次1:[]}
# 加入【某一課程組合 code】的一個課程資訊 course 到節數 (sections)
# course = [編號,人數,節數, ...]
# 最後排序，將人數多的放前面


def addCourse(sections, course):
    for i in range(2, len(course)):
        s = sections.get(course[i], [])
        sections[course[i]] = s + [[course[1], course[0]]]
    for k, v in sections.items():
        v.sort(reverse=True)

# 產生【某一課程組合】編碼 code 之課程節數資料 sections
# code = 1100
# sections={節次0:[[課程人數1,課程編號1],[課程人數2,課程編號2]], 節次1:[...], ...}


def genSections(courses: list, code: str):
    sections = {}  # 所有使用節數時段
    for i in range(len(code)):
        if code[i] == '1':
            addCourse(sections, courses[i])
    return sections

# 檢查某一個節數(0, 1, 2, ...)【某一課程組合】section 是否可排入教室 rooms
# code = 1100
# sections={節次0:[[課程人數1,課程編號1],[課程人數2,課程編號2]], 節次1:[...], ...}
# 若可以排入，則記錄配對資訊
#match=[節次課程編號1, 教室編號1,節次課程編號2, 教室編號2,...]
# 人數多的課程先排入教室容量大的，依序往下排，人數不足則 False


def checkOneSectionValid(section, rooms):
    match = []
    lenS, lenR = len(section), len(rooms)
    if lenS > lenR:
        return False, match
    for i in range(lenS):
        if section[i][0] > rooms[i][1]:
            return False, match
        else:
            match += [section[i][1], rooms[i][0]]
    return True, match

# 檢查所有節數【某一課程組合】sections 是否可排入教室rooms
# 若沒有 False，則記錄配對資訊


def checkAllSectionsValid(sections: list, rooms: list):
    matches = {}
    match = []
    for k, v in sections.items():
        flag, match = checkOneSectionValid(v, rooms)
        if flag == False:
            return False, matches
        elif len(match) > 0:
            matches[k] = match
    return True, matches

# 產生【某一課程組合】合法的排程資訊，data=[[code1, match1, sections1], ...]
# 1~2**N LOOP
  # 產生【某一課程組合】編碼 code
  # 產生【某一課程組合】編碼 code，其節次資訊
  # 檢查 該節次資訊是否合法(能排入教室)，若合法則紀錄配對資訊
  # 將合法排程資訊 [code1, match1, sections1] 加入 data


def genAllValidData(N: int, courses: list, rooms: list):
    data = []
    for x in range(2**N):
        code = genCoursesCode(x, N)
        sections = genSections(courses, code)
        flag, matches = checkAllSectionsValid(sections, rooms)
        if flag == True:
            data.append([code, matches, sections])
    return data

# 計算【某一課程組合】所有節次 sections 可排入的總課程時數 count


def computeHours(sections):
    count = 0
    for k, v in sections.items():
        if len(v) > 0:
            count = count + len(v)
    return count


def computeNum(code):
    return code.count('1')

# 計算【所有課程組合】所有節次可排入的總課程時數，最大值、最大值排程資訊
#data = [code, matches, section]


def computeMaxHours(data: list):
    hour, maxHours = 0, 0
    num, maxNum = 0, 0
    hourKey, numKey = [], []
    for d in data:
        hour = computeHours(d[2])
        if hour > maxHours:
            maxHours = hour
            hourKey = d
        num = computeNum(d[0])
        if num > maxNum:
            maxNum = num
            numKey = d
    return maxHours, hourKey, maxNum, numKey

# course = [編號,人數,節數, ...]


def process():
    rooms = []
    courses = []
    x = input().split()
    M, N = int(x[0]), int(x[1])
    for i in range(M):
        r = input().split()
        rooms += [[int(r[0]), int(r[1])]]
    rooms.sort(key=lambda s: s[1], reverse=True)
    print(rooms)
    for i in range(N):
        x = input().split()
        courses.append([int(x[0]), int(x[1]), int(x[2]), int(x[3])])
    courses = [[d[0], d[1]]+[t for t in range(d[2], d[3])] for d in courses]
    print(courses)
    data = genAllValidData(N, courses, rooms)
    print(data)
    maxHours, hourKey, maxNum, numKey = computeMaxHours(data)
    print(maxHours)
    print(hourKey[0])
    print(hourKey[1])
    print(hourKey[2])
    print(maxNum)
    print(numKey[0])
    print(numKey[1])
    print(numKey[2])


process()
