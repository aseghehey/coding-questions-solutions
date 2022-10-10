class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = {f: float("inf") for f in range(n)}
        cost[src] = 0
        
        for i in range(k + 1):
            tmp = cost.copy()
            for frm, to, cst in flights:
                if cost[frm] == float("inf"):
                    continue
                if cost[frm] + cst < tmp[to]:
                    tmp[to] = cst + cost[frm]
            cost = tmp
        
        return cost[dst] if cost[dst] != float("inf") else -1