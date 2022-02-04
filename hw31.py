def computeCover(start  ,end ,cover):
    for i in range(start ,end ,1):
        cover[i]=1

def process():
    n=int(input())
    count=0
    data=[]
    cover=[0]*60000
    
    for i in range(n):
        start ,end=input().split()
        computeCover(int(start), int(end), cover)
    #print(cover)
    
    for i in range(60000):
        if cover[i]==1:
            count+=1
    print(count)

process()