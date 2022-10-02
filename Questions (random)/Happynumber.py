n = 19

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