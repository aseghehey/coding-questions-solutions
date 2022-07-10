class Solution(object):
    # first solution
    # runtime: 44ms, memory usage: 13.4

    def isValid(self, s):
        valid = {']':'[', '}':'{', ')':'('}
        stack = []
        
        for ch in s:
            if ch in valid.values():
                stack.append(ch)
            else:
                if (stack == []) or valid[ch] != stack.pop():
                    return False
        
        return stack == []

    #optimized solution
    # runtime: 20ms, memory usage: 13.8
    def isValid(self, s):
        valid = {']':'[', '}':'{', ')':'('}
        stack = []
        
        for ch in s:
            if ch in valid.values():
                stack.append(ch)
            else:
                if (stack == []) or valid[ch] != stack.pop():
                    return False
        
        return stack == []