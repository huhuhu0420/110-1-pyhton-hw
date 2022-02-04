import copy


def AddWFront(article: list, instruct: list):
    i = int(instruct[1])-1
    n = int(instruct[2])-1
    w = instruct[3]
    article[i].insert(n, w)


def AddWAfter(article: list, instruct: list):
    i = int(instruct[1])-1
    n = int(instruct[2])-1
    w = instruct[3]
    article[i].insert(n+1, w)


def AddSFront(article: list, instruct: list):
    i = int(instruct[1])-1
    s = instruct[2:]
    for j in s[::-1]:
        article[i].insert(0, j)


def AddSAfter(article: list, instruct: list):
    i = int(instruct[1])-1
    s = instruct[2:]
    for j in s:
        article[i].append(j)


def insertFront(article: list, instruct: list):
    key = instruct[1]
    w = instruct[2]
    for sentence in range(len(article)):
        for i in range(len(article[sentence])-1, -1, -1):
            if article[sentence][i] == key:
                #print(article[sentence][i], sentence, i)
                AddWFront(article, ['', sentence+1, i+1, w])


def insertAfter(article: list, instruct: list):
    key = instruct[1]
    w = instruct[2]
    for sentence in range(len(article)):
        for i in range(len(article[sentence])-1, -1, -1):
            if article[sentence][i] == key:
                #print(article[sentence][i], sentence, i)
                AddWAfter(article, ['', sentence+1, i+1, w])


def delW(article: list, instruct: list):
    i = int(instruct[1])-1
    n = int(instruct[2])-1
    article[i].pop(n)


def delL(article: list, instruct: list):
    i = int(instruct[1])-1
    article.pop(i)


def replaceOld(article: list, instruct: list):
    old = instruct[1]
    new = instruct[2]
    for i in range(len(article)):
        for j in range(len(article[i])):
            if article[i][j] == old:
                article[i][j] = new


def copyL(article: list, instruct: list):
    i = int(instruct[1])-1
    copyWord = []
    copyWord = copy.deepcopy(article[i])
    return copyWord


def copyi(article: list, instruct: list):
    i = int(instruct[1])-1
    n = int(instruct[2])-1
    copyWord = []
    copyWord = [copy.deepcopy(article[i][n])]
    return copyWord


def countArticle(article: list):
    counter = 0
    for i in article:
        for j in i:
            counter += 1
    return counter


def pasteFront(article: list, instruct: list, copyWord: list):
    i = int(instruct[1])-1
    n = int(instruct[2])-1
    for j in range(len(copyWord)-1, -1, -1):
        article[i].insert(n, copyWord[j])


def pasteAfter(article: list, instruct: list, copyWord: list):
    i = int(instruct[1])-1
    n = int(instruct[2])-1
    for j in range(len(copyWord)-1, -1, -1):
        article[i].insert(n+1, copyWord[j])


def printArticle(article: list):
    for sentence in article:
        # print(type(sentence))
        print(' '.join(sentence))


def editArticle(article: list, instruct: list, copyWord: list):
    # print(copyWord)
    if instruct[0] == 'ADD_W_FRONT':
        AddWFront(article, instruct)
    elif instruct[0] == 'ADD_W_AFTER':
        AddWAfter(article, instruct)
    elif instruct[0] == 'ADD_S_FRONT':
        AddSFront(article, instruct)
    elif instruct[0] == 'ADD_S_AFTER':
        AddSAfter(article, instruct)
    elif instruct[0] == 'INSERT_FRONT':
        insertFront(article, instruct)
    elif instruct[0] == 'INSERT_AFTER':
        insertAfter(article, instruct)
    elif instruct[0] == 'DEL_W':
        delW(article, instruct)
    elif instruct[0] == 'DEL_L':
        delL(article, instruct)
    elif instruct[0] == 'REPLACE':
        replaceOld(article, instruct)
    elif instruct[0] == 'COPY_L':
        copyWord = copyL(article, instruct)
    elif instruct[0] == 'COPY':
        copyWord = copyi(article, instruct)
    elif instruct[0] == 'PASTE_FRONT':
        pasteFront(article, instruct, copyWord)
    elif instruct[0] == 'PASTE_AFTER':
        pasteAfter(article, instruct, copyWord)
    return copyWord


def process():
    _input = input().split()
    n = int(_input[0])
    m = int(_input[1])
    article = []
    flag = 0
    instruction = []
    copyWord = []
    for i in range(n):
        _input = input().split()
        article.append(_input)
    # printArticle(article)
    for i in range(m):
        _input = input().split()
        instruction.append(_input)
    # print(instruction)
    for instruct in instruction:
        copyWord = editArticle(article, instruct, copyWord)
        # print(instruct)
        # printArticle(article)
        # print()
        if instruct[0] == 'COUNT':
            flag = 1
    if flag == 1:
        print(countArticle(article))
    printArticle(article)


def test():
    article = [['Morning', 'is', 'mom'], ['Morning', 'dear'], ['What', 'is', 'for', 'breakfast'], [
        'Here', 'are', 'your', 'eggs', 'and', 'milk'], ['Looks', 'is', 'good']]
    #AddWFront(article, ['', 3, 2, 'www'])
    AddSFront(article, ['', 1, 'aaa', 'bbb', 'ccc'])
    #insertFront(article, ['', 'Morning', 'MMM'])
    #delW(article, ['', 2, 3])
    #delL(article, ['', 5])
    #replaceOld(article, ['', 'is', 'was'])
    copyWord = copyi(article, ['', 3, 4])
    # print(copyWord)
    pasteFront(article, ['', 4, 3], copyWord)
    copyWord = copyL(article, ['', 2])
    # print(copyWord)
    pasteAfter(article, ['', 5, 1], copyWord)
    printArticle(article)


# process()
test()
