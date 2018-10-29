import math
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

bfs = BreadthFirstPaths(G, 0)

for w in range(1, V):
    print(bfs.pathTo(w))

"""

"""
The BreadthFirstPaths class represents a data type for finding
shortest paths (number of edges) from a source vertex s (or a set 
of source vertices) to every other vertex in an undirected graph.

This implementation uses breadth-first search.
The constructor takes time proportional to V + E, where V is the 
number of vertices and E is the number of edges.
Each call to #distTo(int) and #hasPathTo(int) takes constant time;
each call to #pathTo(int) takes time proportional to the length
of the path.
It uses extra space (not including the graph) proportional to V.
"""
class BreadthFirstPaths:
    # private static final int INFINITY = Integer.MAX_VALUE;
    # private boolean[] marked;  // marked[v] = is there an s-v path
    # private int[] edgeTo;      // edgeTo[v] = previous edge on shortest s-v path
    # private int[] distTo;      // distTo[v] = number of edges shortest s-v path

    """
    Computes the shortest path between the source vertex s
    and every other vertex in the graph G.
    :param G: the graph
    :param s: the source vertex
    :raises IndexError: unless 0 <= s < V
    :raises IndexError: unless 0 <= s < V
    """
    def __init__(self, G: Graph, s: int):
        self.marked = [False for i in range(G.V)]
        self.distTo = [0 for i in range(G.V)]
        self.edgeTo = [0 for i in range(G.V)]
        self.validateVertex(s)
        self._bfs(G, s)

        assert self.check(G, s)



    # breadth-first search from a single source
    def _bfs(self, G: Graph, s: int):
        q = []
        for v in range(G.V):
            self.distTo[v] = math.inf
        self.distTo[s] = 0
        self.marked[s] = True
        q.append(s)

        while q:
            v = q.pop(0)
            for w in G.adj[v]:
                if not self.marked[w]:
                    self.edgeTo[w] = v
                    self.distTo[w] = self.distTo[v] + 1
                    self.marked[w] = True
                    q.append(w)


    """
    Is there a path between the source vertex s and vertex v?
    :param v: the vertex
    :returns: True if there is a path, and False otherwise
    :raises IndexError unless 0 <= v < V
    """
    def hasPathTo(self, v: int):
        self.validateVertex(v)
        return self.marked[v]

    """
    Returns the number of edges in a shortest path between the source vertex s 
    and vertexv?
    :param v: the vertex
    :returns: the number of edges in a shortest path
    :throws IndexError: unless 0 <= v < V
    """
    def distanceTo(self, v: int):
        self.validateVertex(v)
        return self.distTo[v]

    """
    Returns a shortest path between the source vertex s
    and v, or None if no such path.
    :param  v: the vertex
    :returns: the sequence of vertices on a shortest path, as a list
    :throws IndexError: unless 0 <= v < V
    """
    def pathTo(self, v: int):
        self.validateVertex(v)
        if not self.hasPathTo(v):
             return None
        path = []
        x = v
        while self.distTo[x] != 0:
            path.append(x)
            x = self.edgeTo[x]
        path.append(x)
        path.reverse()
        return path

    # check optimality conditions for single source
    def check(self, G: Graph, s: int):
        # check that the distance of s = 0
        if self.distTo[s] != 0:
            print("distance of source ", s, " to itself = ", self.distTo[s])
            return False

        # check that for each edge v-w dist[w] <= dist[v] + 1
        # provided v is reachable from s
        for v in range(G.V):
            for w in  G.adj[v]:
                if self.hasPathTo(v) != self.hasPathTo(w):
                    print("edge ", v, "-", w)
                    print("hasPathTo(", v, ") = ", self.hasPathTo(v))
                    print("hasPathTo(", w, ") = ", self.hasPathTo(w))
                    return False
                if self.hasPathTo(v) and (self.distTo[w] > self.distTo[v] + 1):
                    print("distTo[", v, "] = ", self.distTo[v])
                    print("distTo[", w, "] = ", self.distTo[w])
                    return False

        # check that v = edgeTo[w] satisfies distTo[w] = distTo[v] + 1
        # provided v is reachable from s
        for w in range(G.V):
            if not self.hasPathTo(w) or w == s:
                 continue
            v = self.edgeTo[w]
            if self.distTo[w] != self.distTo[v] + 1:
                print("shortest path edge ", v, "-", w)
                print("distTo[", v, "] = ", self.distTo[v])
                print("distTo[", w, "] = ", self.distTo[w])
                return False
        return True


    # raise an IndexError unless 0 <= v < V
    def validateVertex(self, v: int):
        V = len(self.marked)
        if v < 0 or v >= V:
            raise IndexError("vertex " + v + " is not between 0 and " + (V-1))