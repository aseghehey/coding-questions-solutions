"""

Consider the array [7, 8, 6, 5] base 10 = [0111, 1000, 0110, 0101] base 2. 
First, group the items by number of binary digits equal to 1: [[1000}, [0101, 0110),
[011112. The elements with two 1's now must
be ordered: (0110, 0101] = [6, 5] base 10. Sort those
two elements in ascending order by value
making the final array [1000, 0101, 0110, 0111]
= [8, 5, 6, 7]

"""
import heapq
def dec_to_bin(n):
    count = 0
    while n > 0:
        count += n % 2
        n = n // 2
    return count

def rearrange(elements):
    res = []
    heap = []
    heapq.heapify(heap)
    for elem in elements:
        heapq.heappush(heap, (dec_to_bin(elem), elem))

    while heap:
        res.append(heapq.heappop(heap)[1])
    
    return res

print(rearrange([7,8,6,5]))