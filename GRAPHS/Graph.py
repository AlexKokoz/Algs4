
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
class Graph(object):

    """
    Initializes an empty graph with V vertices and 0 edges.

    :param  V: number of vertices
    :raises ValueError: if V < 0
    """
    def __init__(self, V: int):
        if V < 0:
            raise ValueError("number of vertices must be nonnegative")
        self.V = V # number of vertices in this digraph
        self.E = 0 # number of edges in this digraph
        self.adj = [[] for _ in range(V)] # adj[v] = adjacency list for vertex v

    """
    Initializes a new graph that is a deep copy of G.    

    :param  G: the graph to copy \
    :raises TypeError: if G is not a Graph instance
    """   
    def copy(self, G):
        if not isinstance(G, Graph):
            raise TypeError("G is not a Graph instance")
        self.V = G.V
        self.E = G.E
        self.adj = []
        for _ in range(G.V):
            self.adj.append([])
        for v in range(G.V):
            for w in G.adj[v]:
                self.adj[v].append(w)
    
    
    # raise a IndexError unless 0 <= v < V
    def validateVertex(self, v: int):
        if v < 0 or v >= self.V:
            raise IndexError("vertex ", v, " is not between 0 and ", (self.V-1))

    """
    Adds the undirected edge v-w to this graph.
    
    :param  v: one vertex in the edge
    :param  w: the other vertex in the edge
    :raises IndexError: unless both 0 <= v < V and 0 <= w < V
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
    :raises IndexError: unless 0 <= v < V
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
