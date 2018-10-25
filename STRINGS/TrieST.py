# A string symbol table for extended ASCII strings, implemented
# dictionary based trie.
# 
# The TrieST class represents an symbol table of key-value
# pairs, with string keys and generic values.
# 
# It supports the usual methods:
#  put, 
#  get, 
#  contains, 
#  delete, 
#  size,
#  is-empty
# 
# It also provides methods for:
#  finding the string in the symbol table that is the longest prefix of a given prefix,
#  finding all strings in the symbol table that start with a given prefix,
#  finding all strings in the symbol table that match a given pattern.
# 
# A symbol table implements the associative array abstraction:
# when associating a value with a key that is already in the symbol table,
# the convention is to replace the old value with the new value.
# This class uses the convention that values cannot be None; setting the
# value associated with a key to None is equivalent to deleting the key
# from the symbol table.
#
# This implementation uses a dictionary based trie.
# The put, contains, delete, and longest prefix operations take time proportional 
# to the length of the key (in the worst case). Construction takes constant time.
# The size, and is-empty operations take constant time.
# Construction takes constant time.




class TrieST:

    # trie node
    class Node:
        def __init__(self):
            self.val = None
            self.next = {}

    # Initializes an empty string symbol table.
    def __init__(self):
        self.root = None # root of trie
        self.n = 0       # number of keys in trie

    # Returns the value associated with the given key.
    # :param key: the key
    # :returns: the value associated with the given key if the key is in the symbol table
    # and None if the key is not in the symbol table
    def get(self, key: str):
        if key is None:
            raise TypeError("argument to get() is null")
        x = self._get(self.root, key, 0)
        if x is None:
            return None
        return x.val
    
    def _get(self, x: Node, key: str, d: int):
        if x is None:
            return None
        if d == len(key):
            return x
        c = key[d]
        if c in x.next:
            return self._get(x.next[c], key, d + 1)
        else: 
            return None

    # Does this symbol table contain the given key?
    # :param key: the key
    # :returns: true if this symbol table contains key and
    # false otherwise
    def contains(self, key: str):
        if key is None:
            raise TypeError("argument to contains() is null")
        return self.get(key) is not None

    # Inserts the key-value pair into the symbol table, overwriting the old value
    # with the new value if the key is already in the symbol table.
    # If the value is {@code null}, this effectively deletes the key from the symbol table.
    # :param key: the key 
    # :param val: the val
    def put(self, key: str, val):
        if key is None:
            raise TypeError("first argument to put() is null")
        if val is None:
            self.delete(key)
        else:
            self.root = self._put(self.root, key, val, 0)
    
    def _put(self, x: Node, key: str, val, d: int):
        if x is None:
            x = self.Node()
        if d == len(key):
            if x.val is None:
                self.n += 1
            x.val = val
            return x
        c = key[d]
        if c not in x.next:
            x.next[c] = None
        x.next[c] = self._put(x.next[c], key, val, d + 1)
        return x

    # Returns the number of key-value pairs in this symbol table.
    # :returns: the number of key-value pairs in this symbol table
    def size(self):
        return self.n

    # Is this symbol table empty?
    # :returns: true if this symbol table is empty and false otherwise
    def isEmpty(self):
        return self.size() == 0


    # Removes the key from the set if the key is present.
    # :param key: the key
    def delete(self, key: str):
        if key is None:
            raise TypeError("argument of delete() is null")
        self.root = self._delete(self.root, key, 0)
    
    def _delete(self, x: Node, key: str, d: int):
        if x is None:
            return None
        if d == len(key):
            if x.val is not None:
                self.n -= 1
            x.val = None
        else:
            c = key[d]
            if c not in x.next:
                x.next[c] = None
            x.next[c] = self._delete(x.next[c], key, d + 1)

        # remove subtrie rooted at x if it is completely empty
        if x.val is not None:
            return x
        for c in x.next.keys():
            if x.next[c] is not None:
                return x
        return None

    #  Returns the string in the symbol table that is the longest prefix of {@code query},
    #  or {@code null}, if no such string.
    #  :param query: the query string
    #  :returns: the string in the symbol table that is the longest prefix of {@code query},
    #  or {@code null} if no such string
    def longestPrefixOf(self, query: str):
        if query is None:
            raise TypeError("argument of longestPrefixOf() is None")
        length = self._longestPrefixOf(self.root, query, 0, -1)
        if length == -1:
            return None
        else:
            return query[0:length]

    # returns the length of the longest string key in the subtrie
    # rooted at x that is a prefix of the query string,
    # assuming the first d character match and we have already
    # found a prefix match of given length (-1 if no such match)


    def _longestPrefixOf(self, x: Node, query: str, d: int, length: int):
        if x is None: 
            return length
        if x.val is not None:
            length = d
        if d == len(query):
            return length
        c = query[d]
        if c not in x.next:
            x.next[c] = None
        return self._longestPrefixOf(x.next[c], query, d+1, length)

    # Returns all keys in the symbol table as an list.
    # :returns: all keys in the symbol table as an {@code Iterable}
    def keys(self):
        return self.keysWithPrefix("")

    # Returns all of the keys in the set that start with a given prefix.
    # :param prefix: the prefix
    # :returns: all of the keys in the set that start with a given prefix,
    # as a list
    def keysWithPrefix(self, prefix: str):
        results = []
        x = self._get(self.root, prefix, 0)
        self._collect(x, prefix, results)
        return results


    def _collect(self, x: Node, prefix: str, results: list):
        if x is None:
            return
        if x.val is not None:
            results.append(prefix)
        for c in x.next.keys():
            prefix = prefix + c
            self._collect(x.next[c], prefix, results)
            prefix = prefix[0:len(prefix) - 1]



    # Returns all of the keys in the symbol table that match specified pattern,
    # where . symbol is treated as a wildcard character.
    # :param pattern: the pattern
    # :returns: all of the keys in the symbol table that match specified pattern,
    # as a list, where . is treated as a wildcard character.

    def keysThatMatch(self, pattern: str):
        results = []
        self._collectPattern(self.root, "", pattern, results)
        return results

    def _collectPattern(self, x: Node, prefix: str, pattern: str, results: list):
        if x is None:
            return
        d = len(prefix)
        if d == len(pattern) and x.val is not None:
            results.append(prefix)
        if d == len(pattern):
            return
        c = pattern[d]
        if c == ".":
            for ch in x.next.keys():
                prefix = prefix + ch
                self._collectPattern(x.next[ch], prefix, pattern, results)
                prefix = prefix[0:len(prefix) - 1]
        else:
            prefix = prefix + c
            if c not in x.next:
                x.next[c] = None
            self._collectPattern(x.next[c], prefix, pattern, results)
            prefix = prefix[0:len(prefix) - 1]
