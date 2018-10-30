"""
The Digraph class represents a directed graph of vertices
named 0 through V - 1.
It supports the following two primary operations: add an edge to the digraph,
iterate over all of the vertices adjacent from a given vertex.
Parallel edges and self-loops are permitted.

This implementation uses a list of lists representation, which 
is a vertex-indexed array of lists.
All operations take constant time (in the worst case) except
iterating over the vertices adjacent from a given vertex, which takes
time proportional to the number of such vertices.
"""

class Digraph:

    """
    Initializes an empty digraph with V vertices.
    
    :param  V: the number of vertices
    raises ValueError: if V < 0
    """
    def __init__(self, V: int):
        if V < 0:
            raise ValueError("Number of vertices in a Digraph must be nonnegative")
        self.V = V # number of vertices in this digraph
        self.E = 0 # number of edges in this digraph
        self.indegree = [0 for _ in range(V)] # indegree[v] = indegree of vertex v
        self.adj = [[] for _ in range(V)] # adj[v] = adjacency list for vertex v
        
    

    """
    Initializes a new digraph that is a deep copy of the specified digraph.
    
    :param  G the digraph to copy
    """
    def copy(self, G):
        if not isinstance(G, Digraph):
            raise TypeError("G is not a Digraph instance")
        self.V = G.V
        self.E = G.E
        self.adj = []
        self.indegree = map(lambda x: x, G.indegree)
        self.adj = map(lambda x: x, G.adj)

    # throw an IndexError unless 0 <= v < V
    def validateVertex(self, v: int):
        if v < 0 or v >= self.V:
            raise IndexError("vertex ", v, " is not between 0 and ", (self.V-1))
    

    """
    Adds the directed edge v→w to this digraph.
    
    :param  v: the tail vertex
    :param  w: the head vertex
    :raises IndexError unless both 0 <= v < V and 0 <= w < V
    """
    def addEdge(self, v: int, w: int):
        self.validateVertex(v)
        self.validateVertex(w)
        self.adj[v].append(w)
        self.indegree[w] += 1
        self.E += 1
    
    """
    Returns the number of directed edges incident from vertex v.
    This is known as the outdegree of vertex v.
    
    :param  v: the vertex
    :returns: the outdegree of vertex v               
    :raises IndexError unless 0 <= v < V
    """
    def outdegree(self, v: int):
        self.validateVertex(v)
        return len(self.adj[v])    

    """
    Returns the reverse of the digraph.
    
    :return the reverse of the digraph
    """
    def reverse(self): 
        reverse = Digraph(self.V)
        for v in range(self.V):
            for w in self.adj[v]:
                reverse.addEdge(w, v)
        return reverse
    

    """
    Returns a string representation of the graph.
    
    :return the number of vertices V, followed by the number of edges E,  
           followed by the V adjacency lists
    """
    def toString(self):
        s = ""
        s += str(self.V) + " vertices, " + str(self.E) + " edges " + "\n"
        for v in range(self.V):
            s += str(v) + ": "
            for w in self.adj[v]:
                s += str(w) + " "            
            s += "\n"        
        return s
        