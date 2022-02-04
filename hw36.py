def a(n:int):
    if n==1:
        return 2
    else:
        return a(n-1)+n

def process():
    n=int(input())
    print(a(n))

process()