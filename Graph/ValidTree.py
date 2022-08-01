#This is the optimal solution with comments    
def validTree(self, n: int, edges: List[List[int]]) -> bool:
    if not n: # still considered valid
        return True
    
    graph = {i:[] for i in range(n)} # converting to adjacency list
    for n1, n2 in edges: # undirected graph so it goes both ways
        graph[n1].append(n2)
        graph[n2].append(n1)
        
    visit = set() 
    def dfs(i, prev):
        if i in visit: # meaning its a loop
            return False
        visit.add(i) 
        for v in graph[i]:
            if v == prev:
                continue # ignoring the last visited since its an undirected graph
            if not dfs(v, i):
                return False
        return True
    
    return dfs(0, -1) and len(visit) == n # need to make sure there's no loops and that its visited all the nodes
