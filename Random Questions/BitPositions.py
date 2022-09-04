"""

Given integers n, p1, and p2, determine if the bits of n in position p1 and p2 are the same.
Positions p1, p2 are 1 based with 1 being the least significant bit.

"""


def bitpositions(n, p1, p2):
    # print((((n >> (p1 - 1))), (n >> (p2 - 1))))
    # print(((n >> (p1 - 1)) & 1), ((n >> (p2 - 1)) & 1))

    # n >> (p1 - 1) gives the pisition of n at p1. bits at n will be shifted to the right by (p1-1) places
    # ((n >> (p1 - 1)) & 1) gives it's least significant bit

    if ((n >> (p1 - 1)) & 1) == ((n >> (p2 - 1)) & 1):
        return True
    return False

print(bitpositions(86, 4, 3))