# This is the solution I came up with:
# The thought behind it is the following:

# Base case is fairly easy to understand. If the length is 1 or 0, then we return the given arr
# Make a map that will store the sorted word. I check if it's on the map already, and if it is,
# then we append it to that sorted word (which gives us a list of all the anagrams for it)
# Else we define it on the map

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    if len(strs) <= 1:
        return [strs]

    res = defaultdict(list)
    for w in strs:
        x = sorted_word = ''.join(sorted(w))
        if x not in res.keys():
            res[x] = [w]
        else:
            res[x].append(w)
    
    ans = []
    for k,v in res.items():
        ans.append(v)
    return ans