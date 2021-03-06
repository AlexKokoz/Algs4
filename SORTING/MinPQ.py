
"""
The MinPQ class represents a priority queue of keys.
This class does not permit None elements.
It supports the usual insert and delete-the-minimum
operations, along with methods for peeking at the minimum key,
testing if the priority queue is empty, and getting all the keys
in ascending order.

This implementation uses a binary heap.
The insert and delete-the-minimum operations take logarithmic 
time.
The min, size, and is-empty operations take constant time.
Construction takes time proportional to the specified number of 
items used to initialize the data structure.
"""

class MinPQ(object):

    """
    Initializes a priority queue from the list of keys.
    Takes time proportional to the number of keys, using sink-based heap construction.
    
    :param  keys: the list of keys
    :raises TypeError: if the key is None
    :raises AssertionError: if new key's type differs from the
    priority queue's elements' type
    :raises AssertionError: if the priority queue after this 
    operation is not a min heap
    """
    def __init__(self, keys: list):
        self.n = 0
        self.pq = [None]
        for x in keys:
            self.insert(x)
        assert self._isMinHeap(), "Priority Queue is not a Min Heap"

    """
    Returns true if this priority queue is empty.
    
    :returns: true if this priority queue is empty
           false otherwise
    """
    def isEmpty(self):
        return self.n == 0
    

    """
    Returns the number of keys on this priority queue.
    
    :returns: the number of keys on this priority queue
    """
    def size(self):
        return self.n
    

    """
    Returns a smallest key on this priority queue.
    
    :returns: a smallest key on this priority queue
    :raises AssertionError: if this priority queue is empty
    """
    def min(self):
        if self.isEmpty():
            raise AssertionError("Priority queue underflow")
        return self.pq[1]

    """
    Adds a new key to this priority queue.
    
    :param  x: the key to add to this priority queue
    :raises TypeError: if the key is None
    :raises AssertionError: if new key's type differs from the
    priority queue's elements' type
    :raises AssertionError: if the priority queue after this 
    operation is not a min heap
    """
    def insert(self, x):
        # check if x has the same type with the rest priority queue's elements' type
        assert self._hasValidType(x), "Key to be inserted has not the same type as the existing PQ elements"

        # add x, and percolate it up to maintain heap invariant
        self.n += 1
        self.pq.append(x)
        self._swim(self.n)
        assert self._isMinHeap(), "Priority Queue is not a Min Heap"
    
    def _hasValidType(self, x):
        if x is None:
            raise TypeError("key is None")
        if self.n > 0:
            pqType = type(self.pq[1]).__name__
            xType = type(x).__name__
            if (pqType != xType):
                return False
        return True

    """
    Removes and returns a smallest key on this priority queue.
    
    :returns: a smallest key on this priority queue
    :raises KeyError: if this priority queue is empty
    :raises AssertionError: if the priority queue after this 
    operation is not a min heap
    """
    def delMin(self):
        if self.isEmpty():
            raise KeyError("Priority queue underflow")
        min = self.pq[1]
        self._exch(1, self.n)
        self.n -= 1
        self._sink(1)
        self.pq.pop()
        assert self._isMinHeap(), "Priority Queue is not a Min Heap"
        return min

    
    """
    Returns a list that contains the keys on this priority queue
    in ascending order.
    
    :returns: a list that contains the keys on this priority queue
    in ascending order
    """
    def keysAsc(self):
        copy = MinPQ(self.pq[1:len(self.pq)])
        keys = []
        while not copy.isEmpty():
            keys.append(copy.delMin())
        return keys

    ########################################################################
    # Helper functions to restore the heap invariant.
    ########################################################################

    def _swim(self, k: int):
        while k > 1 and self._greater(k // 2, k):
            self._exch(k, k // 2)
            k = k // 2
        
    

    def _sink(self, k: int):
        while 2 * k <= self.n:
            j = 2 * k
            if j < self.n and self._greater(j, j + 1):
                j += 1
            if not self._greater(k, j):
                break
            self._exch(k, j)
            k = j
        
    

    ########################################################################
    # Helper functions for compares and swaps.
    ########################################################################

    def _greater(self, i: int, j: int):
        return self.pq[i].__gt__(self.pq[j])
        
    

    def _exch(self, i: int, j: int):
        swap = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = swap
    

    # is pq[1..N] a min heap?
    def _isMinHeap(self):
        return self.__isMinHeap(1)
    

    # is subtree of pq[1..n] rooted at k a min heap?
    def __isMinHeap(self, k: int):
        if k > self.n:
            return True
        left = 2*k
        right = 2*k + 1
        if left  <= self.n and self._greater(k, left):
            return False
        if right <= self.n and self._greater(k, right):
            return False
        return self.__isMinHeap(left) and self.__isMinHeap(right)
    


