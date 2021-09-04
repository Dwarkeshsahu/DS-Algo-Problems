"""
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.


Solution Summary:-
Using BFS

add  element first vertex and color it 1
Now all the neighbour vertex of queue.pop will have different colour.
While adding vertex in queue lets check whether it is altready visited and coloured.
If coloured then this colour should be different from its source colour.

For more explaination :
https://www.youtube.com/watch?v=y22G2QXwpiI
"""

from collections import deque
class Solution:
    def isBipartiteHelper(self, graph , src, visited) -> bool:
        queue = deque()
        queue.append(src)
        while queue:
            currVtx = queue.popleft()
            for nbr in graph[currVtx]:
                if visited[nbr] == 0:
                    visited[nbr] =  -visited[currVtx]
                    queue.append(nbr)
                else:
                    if visited[nbr] == visited[currVtx]:
                        return False
        return True
                          
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [0 for _ in range(n)]
        
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                ans = self.isBipartiteHelper(graph, i, visited)
                if ans is False:
                    return False
        return True        
