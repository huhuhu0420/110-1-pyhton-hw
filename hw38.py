def isCanBack(_child:str):
    l=len(_child)
    for i in range(l):
        if _child[i]!=_child[l-i-1]:
            return 0
    return 1

def findChild(data:str ,n:int)->list:
    child=[]
    _child=''
    for i in range(len(data)+1-n):
        _child=''
        for j in range(n):
            _child+=data[i+j]
        if isCanBack(_child)==1 and _child not in child:
            child.append(_child)
        #print(_child)
    #print(child)
    return child

def process():
    data=input()
    child=[]
    for i in range(1,len(data)):
        child.append(findChild(data ,i))
    #print(child)
    
    final=[]
    for i in child:
        for j in i:
            final.append(j)
    #print(final)
    final=sorted(final)
    #print(final)
    print('#'.join(final))

process()