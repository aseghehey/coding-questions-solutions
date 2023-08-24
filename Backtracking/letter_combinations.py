class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        digitsLength = len(digits)
        
        buttons = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def combinations(index, current):
            if index == digitsLength:
                res.append(current)
                return
            
            for letter in buttons[digits[index]]:
                combinations(index + 1, current + letter)
        
        combinations(0, '')
        return res
