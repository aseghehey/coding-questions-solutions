class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strh = ''
        res = []
        for d in digits:
            strh+=str(d)
        strh = str(int(strh)+1)
        for c in strh:
            res.append(c)
            
        return res
