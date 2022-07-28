# This is very slow, however, it's the first solution I came up with.
# Made helper function to count the "one" bits. Made array of the desired size. Converted each index to binary, then did a count
# on the 1s and passed it to ith slot of the res array.

def countBits(self, n: int) -> List[int]:
    def count_ones(b):
        counter = 0
        while b:
            counter += b%2
            b = b>>1
        return counter

    res = [0]*(n+1)
    for i in range(len(res)):
        x = format(i,"b")
        count = count_ones(int(x,2))
        res[i] = count
    return res

# Optimal solution
# To me, that is just beautiful:
# I didn't come up with this, but whoever did, you are a genius.

# This approach combines dynamic programming with bit manipulation.
def countBits(self, n: int) -> List[int]:
    dp = [0]*(n+1) 
    offset = 1
    for i in range(1,n+1):
        if offset*2==i:
            offset = i # offset becomes the last seen significant bit
        dp[i] = 1 + dp[i-offset] 
    return dp

# For a detailed explanation, go to:
# https://www.youtube.com/watch?v=RyBM56RIWrM&ab_channel=NeetCode
