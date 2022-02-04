
def isNum(i):
    try:
        int(i)
        return 1
    except ValueError:
        return 0


def getLevel(i: str):
    if i == '+' or i == '-':
        return 1
    if i == '*' or i == '/' or i == '%':
        return 2


def transData(data: list):
    stack = []
    newdata = []
    temp = ''
    for i in data:
        if isNum(i) == 1:
            newdata.append(i)
        elif i == '+' or i == '-':
            if len(stack) != 0:
                temp = stack[-1]
                if getLevel(temp) >= getLevel(i):
                    temp = stack.pop(-1)
                    newdata.append(temp)
            stack.append(i)
        elif i == '*' or i == '/' or i == '%':
            if len(stack) != 0:
                temp = stack[-1]
                if getLevel(temp) >= getLevel(i):
                    temp = stack.pop(-1)
                    newdata.append(temp)
            stack.append(i)

    while len(stack) != 0:
        temp = stack.pop(-1)
        newdata.append(temp)
    return newdata


def compute(stack: list, symbol: str):
    back = stack.pop(-1)
    front = stack.pop(-1)
    if symbol == '+':
        return back + front
    if symbol == '-':
        return front - back
    if symbol == '*':
        return front * back
    if symbol == '/':
        return front // back
    if symbol == '%':
        return front % back


def getAnwser(data: list):
    stack = []
    temp = 0
    for i in data:
        if isNum(i) == 1:
            stack.append(int(i))
        else:
            temp = compute(stack, i)
            stack.append(temp)
        # print(stack)
    return stack[0]


def process():
    data = input().split()
    # print(data)
    data = transData(data)
    # print(data)
    print(getAnwser(data))


process()
