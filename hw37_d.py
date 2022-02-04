def putInLine(line:list ,start:int ,end:int):
    for i in range(start ,end):
        line[i]=1

def f(line:list):
    flag=1
    for i in range(len(line)):
        if line[i]==flag:
            if flag==1:
                print(i ,end='')
            elif flag==0:
                print(',' ,end='')
                print(i)
            flag = (flag+1)%2
            

def process():
    line = [0]*20
    n=int(input())
    for i in range(n):
        _input = input().split(',')
        putInLine(line ,int(_input[0]) ,int(_input[1]))
    #print(line)
    f(line)

process()