def oneaway(string1, string2):
    if len(string1) == len(string2):
        return oneeditreplace(string1, string2)
    elif len(string1) + 1 == len(string2):
        return oneeditinsert(string1, string2)
    elif len(string1) - 1 == len(string2):
        return oneeditinsert(string2, string1)
    return False

def oneeditreplace(s1, s2):
    foundDifference = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if foundDifference:
                return False
            foundDifference = True
    return True

def oneeditinsert(s1, s2):
    index1 = 0
    index2 = 0
    while index2 < len(s2) and index1 < len(s1):
        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True

def oneaway2(string1, string2):
    if abs(len(string1) - len(string2)) > 1:
        return False
    if len(string1) == len(string2):
        return oneeditreplace(string1, string2)
    elif len(string1) + 1 == len(string2):
        return oneeditinsert(string1, string2)
    elif len(string1) - 1 == len(string2):
        return oneeditinsert(string2, string1)
    return False