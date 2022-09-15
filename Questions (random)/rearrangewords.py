
"""
Given a word, return the next alphabetically greater string in all permutations of that word.
If there is no greater permutation, return the string "no answer" instead

word = "baca
The string "baca' has the following permutations in alphabetical order: aabc', 'aacb', 'abac', 'abca",
'acab", 'acba", 'baac;, "baca', 'bcaa', 'caab', 'caba', and 'chaa': The next alphabetically greater
permutation of the original string is "bcaa'.

"""

from audioop import reverse


def rearrangeWord(word):
    wrd = list(word)
    i = len(wrd) - 1
    
    while i > 0 and wrd[i - 1] >= wrd[i]:
        i -= 1
    if i <= 0:
        return "no answer"

    j = len(wrd) - 1
    while wrd[j] <= wrd[i - 1]:
        j -= 1
    wrd[i - 1], wrd[j] = wrd[j], wrd[i - 1]
    wrd[i:] = reversed(wrd[i:])

    return ' '.join(wrd)
