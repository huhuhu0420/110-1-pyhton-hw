def quickSort(a:list ,left:int ,right:int):
    if left >= right:
        return 
    i = left
    j = right
    target = a[i]
    while i!=j:
        while a[j]>target and j>i:
            j-=1
        while a[i]<=target and j>i:
            i+=1
        a[i] ,a[j] = a[j] ,a[i]
    #print(a)
    a[i] ,a[left] = a[left] ,a[i]
    #print(left ,i-1)
    quickSort(a ,left ,i-1)
    quickSort(a ,i+1 ,right)

def process():
    a = [4 ,5 ,1 ,43 ,32 ,3 ,5] 
    quickSort(a ,0 ,6)   
    print(a)

process()