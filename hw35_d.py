def isNum(i):
    try:
        int(i)
        return 1
    except ValueError:
        return 0

def getS(s:list)->list:
    a=''
    b=''
    i=0
    while len(s)!=1:
        if s[i]=='*':
            j=i-1
            s.pop(i)
            a=''
            while isNum(s[j])!=1:
                a+=s[j]
                s.pop(j)
                j-=1
            #print(s)
            a=int(s[j])*a
            b+=a
            s.pop(j)
            s.insert(j ,a)
            i=0
            if '*' not in s:
                break
        i+=1
    return s

def postFix(_input:str):
    stack=[]
    top=-1
    s=''
    for i in _input:
        if i==']':
            s+='*'
        else:
            if i!='[' and i!='*':
                s+=i
    return s

def process():
    s=[]
    _input=input()
    _input=_input.replace('[' ,'*[')
    s=postFix(_input)
    s=list(s)
    #print(s)
    s=getS(s)
    for i in s:
        print(i[::-1] ,end='')

process()