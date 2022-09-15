"""

A triangle formed by the three points a(x1, y1), b(x2,y2) and c(x3,y3) is a non-degenerate triangle if the following rules
are respected

ab + bc > ac
bc + ac > ab
ab + ac > bc

A point belongs to a triangle if it lies somewhere on or inside the triangle. Given two points p = (xp, yp)
and q = (xq, yq), return the correct scenario number:

0: abc not degenerate
1: p belongs but not q
2: q belongs, not p
3: both p and q belong
4: neither belong

"""
import math

def distance(x1,y1,x2,y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def area(x1,y1,x2,y2,x3,y3):
    area = abs((x1 * (y2 - y3) + x2 + (y3 - y1) + x3 * (y1 - y2)) / 2.0)
    return area

def pointsBelong(x1,y1,x2,y2,x3,y3,xp,yp,xq,yq):
    ab = distance(x1,y1,x2,y2)
    bc = distance(x2, y2, x3, y3)
    ac = distance(x1, y1, x3, y3)

    if not (ab + bc > ac and bc + ac > ab and ab + ac > bc):
        return 0

    abc = area(x1,y1,x2,y2,x3,y3)

    # variations of p
    pbc = area(xp, yp, x2, y2, x3, y3)
    apc = area(x1, y1, xp, yp, x3, y3)
    abp = area(x1, y1, x2, y2, xp, yp)

    # variations of q
    qbc = area(xq, yq, x2, y2, x3, y3)
    aqc = area(x1, y1, xq, yq, x3, y3)
    abq = area(x1, y1, x2, y2, xq, yq)

    psum, qsum = pbc + apc + abp, qbc + aqc + abq
    if (abc == psum) and (abc == qsum):
        return 3
    elif abc == psum:
        return 1
    elif abc == qsum:
        return 2
    else:
        return 4
