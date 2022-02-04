
def putInTarget(_input: list, targets: list):
    data = []
    for i in _input:
        if i == '+':
            targets.append(data)
            data = []
        else:
            data.append(i)
    targets.append(data)
    print(targets)


def isMatch(target: list, school: list):
    for t in target:
        if '!' in t:
            # print(t[1:])
            if t[1:] in school:
                return 0
        else:
            if t not in school:
                return 0
    return 1


def getMatchNum(targets: list, school: list):
    count = 0
    for target in targets:
        if isMatch(target, school) == 1:
            count += 1
    return count


def sortFinal(final: list):
    for i in range(len(final)):
        for j in range(0, len(final)-i-1):
            #print(final[j][-1], final[j+1][-1])
            if final[j][-1] < final[j+1][-1]:
                final[j], final[j+1] = final[j+1], final[j]


def process():
    n = int(input())
    count = 0
    schools = dict()
    for i in range(n):
        _input = input().split()
        schools[_input[0]] = _input[1:]
    print(schools)
    targets = []
    _input = input().split()
    putInTarget(_input, targets)
    temp = ''
    final = []
    for name, school in schools.items():
        count = getMatchNum(targets, school)
        temp = name+','+str(count)
        print(temp)
        if count != 0:
            final.append(temp)
    sortFinal(final)
    print(' '.join(final))


process()
