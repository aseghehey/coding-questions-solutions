# Bellman ford:
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = {i: float("inf") for i in range(1, n + 1)}
        distances[k] = 0
        
        for i in range(n + 1):
            tmp = distances.copy()
            for src, dst, w in times:
                if distances[src] == float("inf"):
                    continue
                tmp[dst] = min(tmp[src] + w, tmp[dst])
            distances = tmp
        
        return max(distances.values()) if max(distances.values()) != float("inf") else -1


# Dijkstra
import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, w in times:
            graph[s].append((d,w))
        
        minHeap = [(0, k)]
        result = 0
        visit = set()
        
        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            result = max(result, weight)
            for n2, w2 in graph[node]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w2 + weight, n2))
                    
        return result if len(visit) == n else -1