# [1,2,3,2] 4

def eff(arr):
    dic = set()

    if len(arr) % 2 != 0:
        return -1

    target = sum(arr)/(len(arr)/2)
    
    if ((target * 10) % 10) != 0: return -1
    target = int(target)

    res = []
    # print(target)
    for n in arr:
        cmp = target - n
        if cmp in dic:
            res.append([n, cmp])
            dic.remove(cmp)
        else:
            dic.add(n)

    return sum([start*end for start, end in res]) if not dic else -1

print(eff([1,2,3,2]))

    
