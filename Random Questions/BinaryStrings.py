"""

Given an array of requests ['count', 'flip', 'flip', 'count'] and a binary string '01100110'
If requests[i] == 'count', then count the number of 1s in the string

If it's flip, then find the index of the first 0, and flip everything from [0...index]

"""

def binaryStrings(binarystring, requests):
    res = [0] * len(requests)
    for i, req in enumerate(requests):
        if req == 'count':
            count = 0
            for b in binarystring:
                if b == '1':
                    count += 1
            res[i] = count
        else:
            idx, cnt = -1, 0
            for j, binary in enumerate(binarystring):
                if binary == '0':
                    idx = j
                    break
                cnt += 1

            if idx != -1:
                newStr = ''
                for j in range(cnt + 1):
                    if binarystring[j] == '1':
                        newStr += '0'
                    else:
                        newStr += '1'
                newStr += binarystring[idx + 1:]
                binarystring = newStr
            res[i] = idx
    return res

print(binaryStrings('11001101', ['count', 'count', 'flip','flip', 'flip', 'count']))