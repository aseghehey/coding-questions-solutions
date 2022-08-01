# Initial solution:
# Runs in O(n) but is brute force
# I wanted to use the two pointers in this approach 

# My second solution which runs faster:    
def isPalindrome(self, s: str) -> bool:   
    ans = ''
    for c in s.lower(): # convert it all to lowercase and go through it
        if c.isalnum():
            ans+=c # append it if its alpha numeric
    return ans == ans[::-1] # if they are the same front and back then its a palindrome



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

