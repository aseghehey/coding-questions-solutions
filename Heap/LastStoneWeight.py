'''
My thought process was to make a max heap. I loop until the length of the heap is not greater than 1. 
Inside the loop, I pop the max 2 elements and compare them. Depending on the comparison, I perform the necessary operations.
At the end, I check to see if the heap contains anything. 
If it does, return that one element. Else, return 0 (meaning that there’s no stone left).
''' 
  
# This solution is not the most optimal. It is slow. But it is what I first came up with.
  def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        heapify(heap)
        for s in stones:
            heappush(heap, s *-1)
                
        while len(heap) > 1:
            stone1 = heappop(heap) * -1
            stone2 = heappop(heap) * -1
            if stone1 != stone2:
                toadd = max(stone1,stone2) - min(stone1,stone2)
                heappush(heap,toadd *-1)

        if heap:   
            return heap[0]*-1
        else:
            return 0
         
#Optimal solution (with explanation)
# It's the same idea, except optimized.

def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = heappop(stones) 
            stone2 = heappop(stones) 
            if stone1 != stone2:
                heappush(stones, stone1 - stone2)

        if stones:   
            return -heapq.heappop(stones)
        else:
            return 0
