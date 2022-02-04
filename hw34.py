def f(k:list ,i:int ,n:int):
    if i==n:
        return 2*k[i-1]+3*k[i-2]
    else:
        k.append(2*k[i-1]+3*k[i-2])
        return f(k ,i+1 ,n)

def process():
    k=[0 ,1]
    n=input()
    
    try:
        int(n)
    except ValueError:
        print('Error')
        return
    
    if n=='0' or n=='1' or int(n)<0:
        print('Error')
    else:
        print(f(k ,2 ,int(n)))


    

process()