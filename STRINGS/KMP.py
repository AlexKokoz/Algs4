"""
The KMP class finds the first occurrence of a pattern string
in a text string.

This implementation uses a version of the Knuth-Morris-Pratt substring search
algorithm. The version takes time proportional to n + mR
in the worst case, where n is the length of the text string,
m is the length of the pattern, and R is the alphabet size.
It uses extra space proportional to mR.
"""
class KMP(object):

    """
    Preprocesses the pattern string.
    
    :param pat: the pattern string
    """
    def __init__(self, pat: str):
        self.R = 256
        self.pat = pat 

        # build DFA from pattern
        m = len(pat)
        self.dfa = [[0 for i in range(m)] for j in range(self.R)]
        self.dfa[ ord(pat[0]) ][0] = 1  
        x = 0
        for j in range(1, m):
            for c in range(self.R):
                self.dfa[c][j] = self.dfa[c][x] # Copy mismatch cases. 
            self.dfa[ ord(pat[j]) ][j] = j+1    # Set match case. 
            x = self.dfa[ ord(pat[j]) ][x]      # Update restart state. 


    """
    Returns the index of the first occurrrence of the pattern string
    in the text string.

    :param  txt: the text string
    :returns: the index of the first occurrence of the pattern string
    in the text string;  n if no such match
    """
    def search(self, txt: str):

        # simulate operation of DFA on text
        m = len(self.pat)
        n = len(txt) 
        i = j = 0
        while i < n and j < m:
            j = self.dfa[ ord(txt[i]) ][j] 
            i += 1
        if j == m:
            return i - m     # found
        return n             # not found