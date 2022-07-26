# Graphs are not my strong suit so this question took me a while. And this is not even the solution I came up with.
# My solution was super long and I'm not even sure it works. It only passed some of the cases. Even though this is the most basic Graph question anyone can ask.

# Anyways, the trick to this question is to convert the edges list to a hash map where the key is the vertex, while the value is the list of edges. An adjacency list.
# Once that's done, we proceed to do a BFS traversal and compare each node that we're on with the destination. If they are the same, True. If we exit the loop, false.

def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        for edge in edges:
            graph[edge[0]] = graph.get(edge[0], []) + [edge[1]]
            graph[edge[1]] = graph.get(edge[1], []) + [edge[0]]
        print(graph)
        queue, visited = deque(), set()
        queue.append(source)
        visited.add(source)
        
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            
            for adjacent_node in graph[node]:
                if adjacent_node not in visited:
                    queue.append(adjacent_node)
                    visited.add(adjacent_node)
                    
        return False
