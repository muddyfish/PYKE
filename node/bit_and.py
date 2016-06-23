#!/usr/bin/env python

from nodes import Node

class BitAnd(Node):
    char = ".&"
    args = 2
    results = 1
    
    def prepare(self, stack):
        if len(stack) == 0:
            self.add_arg(stack)
        if isinstance(stack[0], Node.sequence):
                self.args = 1
            
    @Node.test_func([4,5], [4])
    def func(self, a:int,b:int):
        """a&b"""
        return a&b

    def and_seq(self, seq:Node.sequence):
        """Setwise and of sequences"""
        if len(seq)==0: return seq
        rtn = []
        for i in seq[0]:
            if False not in [i in sub for sub in seq]:
                rtn.append(i)
        return [rtn]