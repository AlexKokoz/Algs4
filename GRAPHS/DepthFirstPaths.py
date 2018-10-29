import Graph

"""
Dependencies: Graph.py
Execution:
V = 6
G = Graph.Graph(6)

G.addEdge(0, 2)
G.addEdge(0, 1)
G.addEdge(0, 5)
G.addEdge(1, 2)
G.addEdge(3, 2)
G.addEdge(4, 2)
G.addEdge(3, 4)
G.addEdge(3, 5)

bfs = DepthFirstPaths(G, 0)

for w in range(1, V):
    print(bfs.pathTo(w))
"""

"""
The DepthFirstPaths class represents a data type for finding
paths from a source vertex s to every other vertex in an 
undirected graph.

This implementation uses depth-first search.
The constructor takes time proportional to V + E, where V is 
the number of vertices and E is the number of edges.
Each call to #hasPathTo(int) takes constant time;
each call to #pathTo(int) takes time proportional to the length
of the path.
It uses extra space (not including the graph) proportional to V.
"""
class DepthFirstPaths:

    """
    Computes a path between s and every other vertex in graph G.
    :param G: the graph
    :param s: the source vertex
    :raises IndexError unless 0 <= s < V
    """
    def __init__(self, G: Graph, s: int):        
        self.s = s # source vertex
        self.edgeTo = [0 for i in range(G.V)]     # edgeTo[v] = last edge on s-v path
        self.marked = [False for i in range(G.V)] # marked[v] = is there an s-v path?
        self.validateVertex(s)
        self._dfs(G, s)

    # depth first search from v
    def _dfs(self, G: Graph, v: int):
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self.edgeTo[w] = v
                self._dfs(G, w)

    """
    Is there a path between the source vertex {@code s} and vertex {@code v}?
    :param v: the vertex
    :returns: True if there is a path, False otherwise
    :raises IndexError unless 0 <= s < V
    """
    def hasPathTo(self, v: int):
        self.validateVertex(v)
        return self.marked[v]

    """
    Returns a path between the source vertex s and vertex v, or None if no 
    such path.
    :param  v: the vertex
    :returns: the sequence of vertices on a path between the source vertex
           s and vertex v, as a list
    :raises IndexError unless 0 <= s < V
    """
    def pathTo(self, v: int):
        self.validateVertex(v)
        if  not self.hasPathTo(v):
            return None
        path = []
        x = v
        while x != self.s:
            path.append(x)
            x = self.edgeTo[x]
        path.append(x)
        path.reverse()
        return path

    # :raises IndexError unless 0 <= s < V
    def validateVertex(self, v: int):
        V = len(self.marked)
        if v < 0 or v >= V:
            raise IndexError("vertex ", v, " is not between 0 and ", (V-1))
