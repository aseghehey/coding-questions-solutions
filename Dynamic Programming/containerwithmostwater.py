# My first attempt was this:
# It passed 49/60 cases. It's too slow.

# Here is my thinking behind it though:
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        l,r = 0,1
        for l in range(len(height)):
            for r in range (l+1, len(height)):
                cur_area = min(height[l],height[r]) * abs(r-l) # calculate every possible area
                maxarea= max(cur_area,maxarea) # save the max area once we find one thats bigger than the one we have saved
        return maxarea
