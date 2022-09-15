"""
You are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. 
Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, 
find the missing number.

"""

def missingnumber(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] - 1 != arr[i - 1]:
            return arr[i] - 1

def missingnumber_optimal(arr):
    expected = [i for i in range(1, len(arr) + 2)]
    return sum(expected) - sum(arr)
    # return sum(arr) - sum()

# print(missingnumber([1,2,4,5,6,7,8,9,10]))
# print(missingnumber([1,2,3,4,5,6,7,8,10]))
print(missingnumber_optimal([3,7,1,2,8,4,5]))