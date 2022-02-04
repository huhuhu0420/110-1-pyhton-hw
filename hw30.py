

def lineSort(line ,num):
    for i in range (len(line)-1):
        for j in range(len(line)-1-i):
            if num[j]>num[j+1]:
                num[j] ,num[j+1]=num[j+1] ,num[j]
                line[j] ,line[j+1]=line[j+1] ,line[j]
        

def process():
    line=input().split()
    num=input().split()
    lineSort(line ,num)
    #print(num)
#print(line)
    
    for i in line:
        print(i ,end='')


    


process()