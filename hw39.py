def isQualify(temp:str ,n:int):
    count = 0
    for i in range(len(temp)):
        if temp[i]=='1':
            count+=1
    if count==n:
        return 1
    return 0

def putInResult(qualified:list ,data:str):
    result = []
    for q in qualified:
        temp =''
        for j in range(len(q)):
            if q[j]=='1':
                temp+=data[j]
        result.append(temp)
    return result

def process():
    _input = input().split()
    data = _input[0]
    n = int(_input[1])
    result = []
    qualified=[]
    for i in range(2**len(data)):
        temp=''
        temp = format(i ,'b')
        while len(temp)!=len(data):
            temp = '0'+temp
        if isQualify(temp ,n)==1:
            qualified.append(temp)
         #print(temp)
    #print(qualified)
    result = putInResult(qualified ,data)
    result = sorted(result)
    #print(result)
    for i in result:
        if i!=result[-1]:
            print(i ,end=' ')
    print(result[-1] ,end='')

process()