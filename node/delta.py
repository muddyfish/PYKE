#!/usr/bin/env python

from nodes import Node

class Delta(Node):
    char = "$"
    args = 1
    results = 1
    
    def delta(self, seq:Node.sequence):
        """Return the difference in terms in the input sequence.
Returns a sequence of the same type of length n-1."""
        deltas = []
        for i in range(len(seq)-1):
            deltas.append(seq[i+1]-seq[i])
        return[type(seq)(deltas)]