def classify(requires:str):
    elements = []
    element = []
    e = ''
    for i in range(len(requires)):
        #print(requires[i])
        if requires[i] == ' ' and len(e)>0:
            element.append(e)
            e = ''
            #print(element)
        elif requires[i] == '+':
            elements.append(element)
            element = []
            #print(elements)
        elif 'A'<=requires[i]<='Z' or requires[i]=='!':
            e += requires[i]
    element.append(e)
    elements.append(element)
    return elements

def isQualify(school:list ,element:list):
    flag=1
    for e in element:
        if e[0]=='!':
            if e[1:] in school:
                flag=0
        else:
            if e not in school:
                flag=0
    return flag
    

def getNum(school:list ,elements:list):
    num = 0
    for element in elements:
        q = isQualify(school ,element)
        if(q==1):
            num+=1
            #print(num)
        #print(element)
    return num

def sortList(finalNum:list ,finalName:list):
    for i in range(len(finalName)):
        for j in range(len(finalName)-i-1):
            if finalNum[j]<finalNum[j+1]:
                finalNum[j] ,finalNum[j+1] = finalNum[j+1] ,finalNum[j]
                finalName[j] ,finalName[j+1] = finalName[j+1] ,finalName[j]

def process():
    n=int(input())
    schools = dict()
    for i in range(n):
        _input = input().split()
        schools[_input[0]] = _input[1:]
    requires = input()
    #print(schools)
    elements = classify(requires)
    #print(elements)
    flag=0
    finalNum=[]
    finalName = []
    for name ,school in schools.items():
        num = getNum(school ,elements)
        if num != 0:
            finalName.append(name)
            finalNum.append(num)
    #print(finalNum)
    #print(finalName)
    sortList(finalNum ,finalName)
    #print(finalName)
    #print(finalNum)
    l = len(finalNum)
    for i in range(l-1):
        print(finalName[i]+','+str(finalNum[i]) ,end=' ')
    print(finalName[l-1]+','+str(finalNum[l-1]) ,end='')
    

process()