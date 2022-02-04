import numpy as np
import functools as ft
import math


def mut(x):
    return x*x


def adder(x, y, z):
    return x+y+z


def test03():
    x1 = [1, 3, 5, 7]
    for x in map(mut, x1):
        print(x, end='')
    x2 = [2, 4, 6, 8]
    x3 = [100, 100, 100]
    print(zip(x1, x2, x3))
    print([adder(x, y, z) for x, y, z in zip(x1, x2, x3)])
# test03()


def test06():
    x = [4, 3, 1, 2, 5]
    a = ft.reduce(lambda s, e: s+e, x, 0)
    print(a)
    a = ft.reduce(lambda x, y: x*y, x, 0.5)
    print(a)

# test06()


def test05():
    r = range(1, 5)
    a = list(filter(lambda x: x % 2 == 1, r))
    print(a)
    a = list(filter(lambda x: math.sqrt(x) % 1 == 0, r))
    print(a)
# test05()


def test9():
    s = "apple"
    s1 = s.rjust(9, '3')
    s2 = s.ljust(9, '2')
    s3 = s.center(9, '4')
    print(s1, "ya")
    print(s2, "go")
    print(s3, "ok")


# test9()


def test07():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9, 10]
    print([x for x in zip(a, b)])
    print([x for x in zip(a, c)])


# test07()


def test13(x):
    d = [[i]*x for i in range(x)]
    a = np.array(d)
    print(a[2])
    for i in range(x):
        print((a[:, i] == 2).sum(), end='')
    print('\n', np.sum(a, axis=0))
    print(np.sum(a))


# test13(4)


def test14():
    score = int(input('請輸入分數:'))
    level = score // 10
    {
        10: lambda: print('Perfect'),
        9: lambda: print('A'),
        8: lambda: print('B'),
        7: lambda: print('C'),
        6: lambda: print('D')
    }.get(level, lambda: print('E'))()


# test14()

def test15():

    data = [[1, 0, 1],
            [1, 0, 1],
            [0, 1, 0]]
    a = np.array(data)
    for i in range(3):
        temp: np.ndarray = a[:, i] == 0
        print(temp.sum())

# test15()


def test12(x):
    a = np.arange(1, x*x+1).reshape(x, x)
    print(a)
    print(a[1:4, 0])
    # (1)
    print(a[1:2:, ::2])
    # (2)
    print(a[:, 1])


# test12(4)

def test16(x):
    a = np.linspace(0, 11, 12).reshape([3, x])
    # print(a)
    print(a[1:2, 2:3])
    print(np.sum(a, axis=0))
    print(np.sum(a, axis=1))
    print(np.sum(a))


# test16(4)


def test17():
    data = {'rid_1': [['cid1', 60, 1, 2, 3],
                      ['cid2', 70, 1, 2, 3],
                      ['cid3', 80, 1, 2, 3]]}
    ans = 0
    ans2 = 0
    for i in range(3):
        ans += data['rid_1'][i][1]
        ans2 = ans2 + data['rid_1'][i][2] + \
            data['rid_1'][i][3] + data['rid_1'][i][4]
    print(ans)
    print(ans2)


test17()
