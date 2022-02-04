def findGCD(a ,b):
    if b==0:
        return a
    return findGCD(b ,a%b)

def process():
    while(1):
        _input=input().split()
        if _input[0]=='-1':
            break
        x=int(_input[0])
        y=int(_input[1])
        z=int(_input[2])
        a1=findGCD(x ,y)
        a2=findGCD(a1 ,z)
        print(a2)


process()