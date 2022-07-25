# Not my particular solution nor my initial approach.
# I attempted to do a linear scan but gave up as my linear scan approach was far too complicated. This approach is intuitive and I prefer it in comparison to the linear one.

# suppose we have "00011", we can only make 2 groups. "0011" and "01". There's a pattern.
# The smallest size of contiguous bits is the number of substrings for the whole combination of two bits.

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1] # initially the group of contiguous bits will be set to 1, since we are sure to always have at least one bit.
        for i in range(1, len(s)): # traversing the array to find the other bits
            if s[i-1] != s[i]: # if the bits differ, like 01 or 10, then we start another group, since the bits arent contiguous anymore.
                groups.append(1) # initialize a group of size 1
            else: # if they do not differ, like 00 or 11, then we proceed to increment it.
                groups[-1] += 1 # increment group
        ans = 0 # initially it is 0. Since we do not know of any groups before we traverse the group array.
        for i in range(1, len(groups)):
            ans += min(groups[i-1], groups[i]) # we increment ans by the minimum size of two given bits.
        return ans
