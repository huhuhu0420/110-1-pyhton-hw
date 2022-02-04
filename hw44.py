def isSame(data:str ,target:list ,n:int):
    for t in target:
        l = len(t)
        #print(data[8-n:] ,t[l-n:])
        if data[8-n:]==t[l-n:]:
            return 1
    return 0

def getMoney(data:str ,s_special:str ,special:str ,head:list ,six:list):
    if data==s_special:
        return 10000000
    elif data==special:
        return 2000000
    for i in range(3):
        if data==head[i]:
            return 200000
    if isSame(data ,head ,7)==1:
        return 40000
    elif isSame(data ,head ,6)==1:
        return 10000
    elif isSame(data ,head ,5)==1:
        return 4000
    elif isSame(data ,head ,4)==1:
        return 1000   
    elif isSame(data ,head ,3)==1:
        return 200
    elif isSame(data ,six ,3)==1:
        return 200
    return 0

def process():
    s_special = input()
    special = input()
    _input = input().split()
    head = [0]*3 
    head[0] = _input[0]
    head[1] = _input[1]
    head[2] = _input[2]
    _input = input().split()
    six = [0]*3
    six[0] = _input[0]
    six[1] = _input[1]
    six[2] = _input[2]
    n = int(input())
    datas = [0]*n
    money = 0
    for i in range(n):
        datas[i] = input()
        money += getMoney(datas[i] ,s_special ,special ,head ,six) 
   
    print(money)


process()