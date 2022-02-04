

def process():
    _input=input().split()
    #print(_input)
    x1=int(_input[0])
    y1=int(_input[1])
    x2=int(_input[2])
    y2=int(_input[3])
    x3=int(_input[4])
    y3=int(_input[5])
    for i in range(1000):
        if i%x1==y1 and i%x2==y2 and i%x3==y3:
            break
    print(i)
    
process()