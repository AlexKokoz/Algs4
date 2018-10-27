
"""
The Graph class represents an undirected graph of vertices
named 0 through V – 1.
It supports the following two primary operations: add an edge to the graph,
iterate over all of the vertices adjacent to a vertex. It also provides
methods for returning the number of vertices V and the number
of edges E. Parallel edges and self-loops are permitted.
By convention, a self-loop v-v appears in the
adjacency list of v twice and contributes two to the degree
of v.

This implementation uses an list of lists representation, which 
is a vertex-indexed list of lists.
All operations take constant time (in the worst case) except
iterating over the vertices adjacent to a given vertex, which takes
time proportional to the number of such vertices.
"""
class Graph:

    """
    Initializes an empty graph with V vertices and 0 edges.
    param V the number of vertices
    
    :param  V: number of vertices
    :raises TypeError: if V < 0
    """
    def __init__(self, V: int):
        if V < 0:
            raise TypeError("number of vertices must be nonnegative")
        self.V = V
        self.E = 0
        self.adj = []
        for _ in range(V):
            self.adj.append([])

    """
    Initializes a new graph that is a deep copy of G.
    
    :param  G: the graph to copy 
    """   
    def copy(self, G: Graph):
        self.V = G.V
        self.E = G.E
        self.adj = []
        for _ in range(G.V):
            self.adj.append([])
        for v in range(G.V):
            for w in G.adj[v]:
                self.adj[v].append(w)
    
    
    # raise a TypeError unless 0 <= v < V
    def validateVertex(self, v: int):
        if v < 0 or v >= self.V:
            raise TypeError("vertex ", v, " is not between 0 and ", (self.V-1))

    """
    Adds the undirected edge v-w to this graph.
    
    :param  v: one vertex in the edge
    :param  w: the other vertex in the edge
    :raises TypeError: unless both 0 <= v < V and 0 <= w < V
    """
    def addEdge(self, v: int, w:int):
        self.validateVertex(v)
        self.validateVertex(w)
        self.E += 1
        self.adj[v].append(w)
        self.adj[w].append(v)
    
    """
    Returns the degree of vertex v.
    
    :param  v: the vertex
    :returns: the degree of vertex v
    :raises TypeError: unless 0 <= v < V
    """
    def degree(self, v: int):
        self.validateVertex(v)
        return len(self.adj[v])


    """
    Returns a string representation of this graph.
    
    :returns: the number of vertices V, followed by the number of edges E,
    followed by the V adjacency lists
    """
    def toString(self):
        s = str(self.V) + " vertices, " + str(self.E) + " edges\n"
        for v in range(self.V):
            s += str(v) + ": "
            for w in self.adj[v]:
                s += str(w) + ", "
            
            s += "\n"
        return s
