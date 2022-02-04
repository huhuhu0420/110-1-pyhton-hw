

def process():
    odd=[]
    even=[]
    _input=input().split()
    for i in _input:
        i=int(i)
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    even=sorted(even ,reverse=True)
    odd=sorted(odd)
    print(odd+even)

process()