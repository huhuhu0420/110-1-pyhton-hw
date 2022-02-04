def add_w_front(article: list, instruct: list):
    i = int(instruct[1])-1
    n = int(instruct[2])-1
    w = instruct[3]
    article[i].insert(n, w)


def add_w_after(article: list, instruct: list):
    i = int(instruct[1])-1
    n = int(instruct[2])-1
    w = instruct[3]
    article[i].insert(n+1, w)


def add_s_front(article: list, instruct: list):
    i = int(instruct[1])-1
    s = instruct[2:]
    for j in s:
        article[i].insert(0, j)


def add_s_after(article: list, instruct: list):
    i = int(instruct[1])-1
    s = instruct[2:]
    # print(s)
    for j in s:
        article[i].append(j)


def del_w(article: list, instruct: list):
    i = int(instruct[1])-1
    n = int(instruct[2])-1
    article[i].pop(n)


def del_l(article: list, instruct: list):
    i = int(instruct[1])-1
    article.pop(i)


def insert_front(article: list, instruct: list):
    key = instruct[1]
    w = instruct[2]
    for i in range(len(article)):
        index = []
        for j in range(len(article[i])):
            if article[i][j] == key:
                index.append(j)
        # print(index)
        for ix in index[::-1]:
            add_w_front(article, ['', i+1, ix+1, w])


def insert_after(article: list, instruct: list):
    key = instruct[1]
    w = instruct[2]
    for i in range(len(article)):
        index = []
        for j in range(len(article[i])):
            if article[i][j] == key:
                index.append(j)
        # print(index)
        for ix in index[::-1]:
            add_w_after(article, ['', i+1, ix+1, w])


def replaceOld(article: list, instruct: list):
    old = instruct[1]
    new = instruct[2]
    for i in range(len(article)):
        for j in range(len(article[i])):
            if article[i][j] == old:
                article[i][j] = new


def countArticle(article: list):
    count = 0
    for i in article:
        for j in i:
            count += 1
    return count


def printArticle(article: list):
    for i in article:
        print(' '.join(i))


def edit(article: list, instruct: list):
    if instruct[0] == 'ADD_W_FRONT':
        add_w_front(article, instruct)
    elif instruct[0] == 'ADD_W_AFTER':
        add_w_after(article, instruct)
    elif instruct[0] == 'ADD_S_FRONT':
        add_s_front(article, instruct)
    elif instruct[0] == 'ADD_S_AFTER':
        add_s_after(article, instruct)
    elif instruct[0] == 'INSERT_FRONT':
        insert_front(article, instruct)
    elif instruct[0] == 'INSERT_AFTER':
        insert_after(article, instruct)
    elif instruct[0] == 'DEL_W':
        del_w(article, instruct)
    elif instruct[0] == 'REPLACE':
        replaceOld(article, instruct)
    elif instruct[0] == 'DEL_L':
        del_l(article, instruct)


def process():
    _input = input().split()
    n = int(_input[0])
    m = int(_input[1])
    article = []
    instruct = []
    flag = 0
    count = 0
    a = []
    for i in range(n):
        _input = input().split()
        article.append(_input)
    # print(article)
    for i in range(m):
        instruct = []
        instruct = input().split()
        # print(instruct)
        if instruct[0] == 'COUNT':
            flag = 1
        else:
            edit(article, instruct)
    if flag == 1:
        count = countArticle(article)
        print(count)
    printArticle(article)


def test():
    article = [['Morning', 'mom'], ['Morning', 'dear'], ['What', 'is', 'for', 'breakfast'], [
        'Here', 'are', 'your', 'eggs', 'and', 'milk'], ['Looks', 'good']]
    # print(article)
    add_w_front(article, ['add', '3', '2', 'www'])
    add_w_after(article, ['add', '4', '6', 'uu'])
    add_s_front(article, ['add', '1', 'uu pp ii uu eee'])
    add_s_after(article, ['add', '3', 'fjiro uu jifow'])
    del_w(article, ['del', '4', '1'])
    del_l(article, ['del', '6'])
    insert_front(article, ['ins', 'uu', 'xxx'])
    insert_after(article, ['ins', 'Morning', 'ioio'])
    replaceOld(article, ['rep', 'ioio', 'oio'])
    count = countArticle(article)
    print(count)
    print(article)
    printArticle(article)


# test()
process()
