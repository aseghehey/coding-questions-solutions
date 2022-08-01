# The brute force approach is: 
# Runs in O(n^2) ... bad

def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    for i in range(len(prices)):
        for j in range (i, len(prices)): # starts at i, since you cannot back in days
              profit = max(profit, prices[j]-prices[i])
    return profit
      
# O(n) solutions:

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

# Other solution that works just as fine
def maxProfit(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit
