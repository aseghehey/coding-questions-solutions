# Make hash map
# Calculate remaining = target - nums[i]
# if it is on the map, return [i, map[nums[i]]]
# else add it to the map

# O(N)

def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}
    for i in range(len(nums)):
        rem = target - nums[i]
        if rem in seen:
            return [i,seen[rem]]
        else:
            seen[nums[i]] = i 