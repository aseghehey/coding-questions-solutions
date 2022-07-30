# Came up with this solution
# Since they basically just need to have the same number of characters this is one way to do it

# Another way is to count the frequency of every character in both strings and compare them

def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

