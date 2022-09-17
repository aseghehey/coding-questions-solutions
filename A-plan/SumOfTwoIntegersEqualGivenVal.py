"""
Given an array of integers and a value, 
determine if there are any two integers in the array whose sum is equal to the given value.
"""

# spin off two sum

def sum_of_two(arr, val):
    dic = {}
    for i, num in enumerate(arr):
        dic[(val - num)] = i
        if num in dic:
            return [arr[dic[num]], arr[i]]

print(sum_of_two([1,2,4,6,10], 11))