class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res, prev = [],[] 
        for n in range(1,numRows+1): # ignore the '0' slot
            lst = [1]*n # each time make an array of size n for the triangle
            if len(lst)>2: # past the first 2
                for i in range(1, len(lst)-1):  # both the first and last slots are always 1
                    lst[i] = prev[i-1] + prev[i] 
            prev = lst 
            res.append(lst)
        return res
