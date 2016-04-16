#!/usr/bin/env python

from nodes import Node

class Delta(Node):
    char = "$"
    args = 1
    results = 1
    
    @Node.test_func([[1,2,3,5]], [[1,1,2]])
    def delta(self, seq:Node.sequence):
        """Return the difference in terms in the input sequence.
Returns a sequence of the same type, one shorter."""
        deltas = []
        for i in range(len(seq)-1):
            deltas.append(seq[i+1]-seq[i])
        return[type(seq)(deltas)]
    
    def float(self, inp:int):
        """float(inp)"""
        return float(inp)
    