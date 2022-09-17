import math
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = [['I', 1], ['IV', 4], ['V', 5], ['IX', 9], ['X', 10], ['XL', 40], ['L', 50], ['XC', 90], ['C',100], ['CD', 400], ['D', 500], ['CM', 900], ['M', 1000]]
        
        output = ''
        for w, n in roman[::-1]:
            if num == 0:
                return output
            
            count = math.floor(num / n)
            if count:
                num = num % n
                
            for i in range(count):
                output += w
            
        return output