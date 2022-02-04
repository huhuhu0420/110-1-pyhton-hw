def f(n:int ,a:list):
    if n<=3:
        return a[n]
    return f(n-1 ,a)+f(n-2 ,a)+f(n-3 ,a)

def process():
    n=int(input())
    a=[0,0,1,1]
    print(f(n-1 ,a))

process()