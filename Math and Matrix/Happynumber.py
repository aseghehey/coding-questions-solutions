# optimal
def isHappy(n) -> bool:
    seen = set()
    while n != 1 and not (n in seen):
        seen.add(n)
        currSum = 0
        while n > 0:
            # grabbing each decimal
            curr = n % 10
            n = n // 10 # next number
            currSum += curr * curr # current val to the power of 2
        n = currSum # new n for the next iteration
    return n == 1

print(isHappy(116))

# brute force
'''
def happynum(n):
    cycle = set()
    current = 0
    while True:
        n = str(n)
        for digit in n:
            current += int(digit) ** 2
        
        if current == 1:
            return True
        
        if current in cycle:
            return False
        
        n = current
        cycle.add(current)
        current = 0

print(happynum(19))
print(happynum(82))
print(happynum(89))
print(happynum(1))
print(happynum(10))
print(happynum(9))
'''