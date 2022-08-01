# Runs in O(nlogn)
def maxArea(self, height: List[int]) -> int:
    maxarea = 0
    left, right = 0, len(height)-1 # comparing the two bounds as they have the greatest distance apart
    while left < right:
        area = min(height[left],height[right])* (right-left)
        maxarea = max(area,maxarea)
        # Move the iterator if one of them is smaller, so we can find the next highest value
        if height[left] >= height[right]:
            right-=1
        else:
            left+=1
    return maxarea