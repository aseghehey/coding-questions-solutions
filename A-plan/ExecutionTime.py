import math
def executionTime(execution):
    output = 0
    newexecution = {e:e for e in execution}

    print(newexecution)

    for e in execution:
        output += newexecution[e]
        newexecution[e] = math.ceil(newexecution[e] / 2)
    return output

print(executionTime([5,5,3,6,5,3]))