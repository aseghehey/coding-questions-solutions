# The brute force approach is: 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range (i, len(prices)): # starts at i, since you cannot back in days
                  profit = max(profit, prices[j]-prices[i])
        return profit
      
# The improvement from the 1st approach:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        profit = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = max(profit, prices[r]-prices[l])
            else:
                l=r
            r+=1
        return profit
