

def findFriend(friends:dict ,t1:str ,t2:str):
    queue = []
    visit = set()
    for i in friends[t1]:
        queue.append(i)
    #print(queue)
    while len(queue)>0:
        current = queue.pop(0)
        visit.add(current)
        #print(current)
        for f in friends[current]:
            if f == t1 or f == current:
                continue
            if f == t2:
                return 1
            if f not in visit:
                queue.append(f)
        #print(queue)
    return 0
    
def process():
    _input = input().split()
    n = int(_input[0])
    t1 = _input[1]
    t2 = _input[2]
    friends = dict()
    data = set()
    queue = []
    for i in range(n):
        _input = input().split()
        try:
            data = friends[_input[0]]
            data.add(_input[1])
        except KeyError:
            friends[_input[0]] = {_input[1]}
        try:
            data = friends[_input[1]]
            data.add(_input[0])
        except KeyError:
            friends[_input[1]] = {_input[0]}

    #print(friends)

    ans = findFriend(friends ,t1 ,t2)
    if ans == 1:
        print('Yes!')
    else:
        print('No!')

process()