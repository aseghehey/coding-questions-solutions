start = 1
end = 100

def primenumbers(start, end):
    res = []
    for i in range(start + 1, end + 1):
        res.append(i)
        for j in range(start + 1, i - 1):
            if i % j == 0:
                res.remove(i)
                break
    return res

def primenumbers2(start, end):
    res = [2]
    for i in range(start + 2, end + 1):
        if i % 2 == 0: continue
        res.append(i)
        for j in range(start + 1, i//2 + 1):
            if i % j == 0: 
                res.remove(i)
                break
    return res

print(primenumbers2(1, 100) == primenumbers(1,100))