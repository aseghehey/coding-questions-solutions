def countBinarySubstrings(self, s: str) -> int:
    N = len(s)
    prev, cur = 0, 1
    res = 0
    
    for i in range(1, N):
        if s[i] != s[i-1]:
            res += min(prev, cur)
            prev = cur
            cur = 1
        else:
            cur += 1
    
    return res + min(prev, cur)


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        q = deque()
        output = 0
        for c in s:
            while q and q[-1] == c and q[0] != c:
                q.pop()
            
            if q and q[-1] != c:
                q.pop()
                output += 1
                
            q.appendleft(c)
        return output