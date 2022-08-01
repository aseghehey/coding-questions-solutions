# runs in O(klogn)
import heapq as hq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1: # if the length is 1, no need to run the rest of the code
            return nums
        
        frequency = Counter(nums) # frequency is a map that stores the number (in nums) and its frequency
        heap = [] # need a max heap
        hq.heapify(heap) 
        for num, freq in frequency.items(): # unpack the map
            hq.heappush(heap, (-freq, num)) # pass it to the heap
        ans = [] # initialize result array
        for x in range(k): # loop until k, to find the top "k" frequent elements
            ans.append(hq.heappop(heap)[1]) # append the elements in the range k, to the array
        return ans