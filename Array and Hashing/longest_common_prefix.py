class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def common_prefix(s1, s2):
            i = 0
            while i < len(s1) and i < len(s2):
                if s1[i] != s2[i]:
                    return s1[:i]
                i += 1
            return s1[:i]

        prefix = strs[0]
        for i in range(1, len(strs)):
            curr = common_prefix(prefix, strs[i])
            prefix = curr
        return prefix
