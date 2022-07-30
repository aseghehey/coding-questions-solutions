# Initial solution:
# Runs in O(n) but its brute force
# I wanted to use the two pointers in this approach 

def isPalindrome(self, s: str) -> bool:   
    if not s: # if string is empty
        return True
    
    d = ''
    for c in s.lower(): # we iterate through the string and pass it to d without spaces or punctuation 
        if c.isalpha() or c.isdigit():
            d+=c

    l,r = 0,len(d)-1 # our two pointers, the two opposite characters
    while l <= r:
        if d[l] != d[r]: # the instance they do not match, we return False
            return False
        l+=1
        r-=1
        
    return True
   
# My second solution which runs much more fast    
def isPalindrome(self, s: str) -> bool:   
    ans = ''
    for c in s.lower():
        if c.isalnum():
            ans+=c
    return ans == ans[::-1]

# Neetcode's solution:

