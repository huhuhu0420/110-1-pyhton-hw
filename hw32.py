def f(n:int ,fib:list):
    if n==1 or n==2:
        return 1
    else:
        if fib[n]>0:
            return fib[n]
        else:
            fib[n]=f(n-1 ,fib)+f(n-2 ,fib)
            return fib[n] 

def process():
    fib=[0]*1000
    while(1):
        n=input()
        if n=='-1':
            break
        else:
            print(f(int(n),fib))

process()