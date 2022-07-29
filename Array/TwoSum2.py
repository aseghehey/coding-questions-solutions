# Optimal solution
# I knew this problem had something to do with a binary search, it just took a while for it to click to me and see how it
# works for the optimal solution

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers)-1
    while left <= right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left+1,right+1]
        else:
            if total > target:
                right-=1
            else:
                left+=1



# I came up with this solution which is extremely slow but passes all the test cases

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    def bsearch(numArr, num):
        if len(numArr) == 0:
            return False
        else:
            middle = len(numArr)//2
            if numArr[middle] == num:
                return True
            else:
                if num > numArr[middle]:
                    return bsearch(numArr[middle+1:], num)
                else:
                    return bsearch(numArr[:middle],num)
    
    vals = {n: i for i, n in enumerate(numbers)}
    for i,num in enumerate(numbers):
        remaining = target - num
        if bsearch(numbers, remaining):
            return [i+1,vals[remaining]+1]

