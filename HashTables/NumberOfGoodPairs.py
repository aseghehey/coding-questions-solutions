# I make a dictionary that stores the count of how many times a number appears. 
# Since we iterating from left to right, we are sure that the i < j condition is validated.
# I checked the Hint and got the formula n(n-1)//2 to get the number of good pairs, with n = # of times that number appears

def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n in d:
                d[n]+=1
            else:
                d[n]=1
        ans = 0    
        for k,v in d.items():
            if v > 1: # to make sure we only get repeated numbers
                ans+=((v*(v-1))//2)
        return ans
