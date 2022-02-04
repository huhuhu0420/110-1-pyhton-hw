def isLetter(i:str):
    if 'a'<=i<='z' or 'A'<=i<='Z':
        return 1
    return 0

def change(data:list):
    for i in range(len(data)):
        if 'a'<=data[i]<='z':
            data[i] = data[i].upper()
        elif 'A'<=data[i]<='Z':
            data[i] = data[i].lower()
    return data
        

def process():
    _input=input().split()
    data = _input[0]
    n = int(_input[1])
    data = [i for i in data if isLetter(i)==1]
    data=change(data)
    #print(data)
    d=[]
    _d=''
    start=0
    end=n
    while(1):
        _d=''
        if start==end:
            break
        for i in data[start:end]:
            _d+=i
        d.append(_d)
        start = end
        end = start+n
        if end>len(data):
            end=len(data)
    #print(d)
    print('/'.join(d[::-1]))
process()