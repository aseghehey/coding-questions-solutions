def minSubArraylen(target, nums):
    current, l = 0,0
    minSize = float('inf')

    for r in range(len(nums)):
        current += nums[r]
        while current >= target:
            minSize = min(minSize, r - l + 1)
            current -= nums[l]
            l += 1
    
    return minSize if minSize != float('inf') else 0

print(minSubArraylen(10,[1,2,3,4,5,5,6,7,9]))