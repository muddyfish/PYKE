#!/usr/bin/env python

from nodes import Node

class BitOr(Node):
    char = ".|"
    args = 2
    results = 1
    
    def prepare(self, stack):
        if len(stack) == 0:
            self.add_arg(stack)
        if isinstance(stack[0], Node.sequence):
                self.args = 1
    
    @Node.test_func([4,1], [5])
    def func(self, a:int,b:int):
        """a|b"""
        return a|b
    
    def or_seq(self, seqs:Node.sequence):
        """Setwise or of sequences"""
        if len(seqs)==0: return seqs
        rtn = []
        for seq in seqs:
            for i in seq:
                if i not in rtn:
                    rtn.append(i)
        return [rtn]