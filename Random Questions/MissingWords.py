# missing words

"""
Problem description:
Given two strings, one is a subsequence if all of the elements of the first string occur in the same order within the second string.
They do not have to be contiguous in the second string, but order must be maintained. For example, given the string 'I like cheese', the words ('I','cheese') are one possible subsequence of that string.
Words are space delimited.

Given two strings, s and t, where t is a subsequence of s, report the words of s, missing in t (case sensitive), in the order they are missing.

Inputs: 

# s = "Python is an easy to learn powerful programming language It has efficient high-level data structures and a simple but effective approach to objectoriented programming Python elegant syntax and dynamic typing"
# t = "Python is an easy to learn powerful programming language"

# result = ['It', 'has', 'efficient', 'high-level', 'data', 'structures', 'and', 'a', 'simple', 'but', 'effective', 'approach', 'to', 'objectoriented', 'programming', 'Python', 'elegant', 'syntax', 'and', 'dynamic', 'typing']

# s = 'I love programming'
# t = 'love'

# result = ['I','programming']

s = 'I love programming with a passion, programming is the beszt thing ever'
t = 'programming'

# result = ['I', 'love', 'with', 'a', 'passion,', 'programming', 'is', 'the', 'beszt', 'thing', 'ever']

"""

def missingWords(s, t):
    i, j = 0,0 
    res = ''
    while i < len(s):
        while (j < len(t) and i < len(s)) and (s[i] == t[j]):
            j += 1
            i += 1
        res += s[i]
        i += 1
    return res.split()

# print(missingWords(s,t))

