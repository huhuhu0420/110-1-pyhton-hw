

def getQualifyNum(data, need):
    flag = 0
    num = 0
    for n in need:
        flag = 1
        for i in n:
            if i[0] == '!':
                if i[1:] in data:
                    flag = 0
            else:
                if i not in data:
                    flag = 0
        if flag == 1:
            num += 1
    return num


def getNeed(_input):
    need = []
    data = []
    for i in _input:
        if i != '+':
            data.append(i)
        if i == '+':
            need.append(data)
            data = []
    need.append(data)
    return need


def sortList(ans: list):
    for i in range(len(ans)):
        for j in range(len(ans)-i-1):
            if ans[j][1] > ans[j+1][1]:
                ans[j], ans[j+1] = ans[j+1], ans[j]
    return ans


def process():
    school = {}
    n = int(input())
    for i in range(n):
        _input = input().split()
        data = _input[1:]
        school[_input[0]] = data
    _input = input().split()
    print(school)
    need = getNeed(_input)
    print(need)
    ans = []
    for name, data in school.items():
        num = getQualifyNum(data, need)
        if num != 0:
            ans.append([name, str(num)])
    ans = sortList(ans)
    print(ans)
    for a in ans:
        print(':'.join(a))


process()
