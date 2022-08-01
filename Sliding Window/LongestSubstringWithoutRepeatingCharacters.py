class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set() # to determine duplicates
        left = 0 # for substring
        ans = 0 # the result
        
        for right in range(len(s)): # right pointer
            while s[right] in seen: 
                seen.remove(s[left])
                left+=1 # increment left pointer to decrease length of substring
            seen.add(s[right]) # add the characters not in the set already
            ans = max(ans, right - left + 1) # right - left +1 indicates length of substring
            
        return ans