
def f(a:list):
    if len(a)==1:
        return a
    else:
        result=[]
        temp=[]
        for i in range(len(a)):
            x=a[i]
            y=a[0:i]+a[i+1:len(a)]
            result+=[x + j for j in f(y)]
        temp.append(result)
        #print(result)
        return(result)

def processs():
    _input=input().split()
    a=''.join(_input)
    #a='1234'

    result=[]
    result=f(a)
    #print(result)
    for i in result:
        _i = list(i)
        q=[]
        for j in _i:
            j = int(j)
            q.append(j)
        print(q ,end='')
        #print(i)
        if i != result[-1]:
            print(",")


processs()