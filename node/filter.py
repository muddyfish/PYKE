#!/usr/bin/env python

from nodes import Node

class Filter(Node):
    char = "#"
    args = 1
    results = 1
    
    def __init__(self, ast: Node.EvalLiteral):
        self.ast = ast

    @Node.test_func([[1,2,3,0]], [[1,2,3]], "")
    @Node.test_func([[1,2,3,4,5]], [[2,3,5]], "Plt!")
    def func(self, seq: Node.indexable):
        """filter seq on Truthiness - returns the same type as given"""
        rtn = []
        for i in seq:
            val = self.ast.run([i])
            if val[-1]:
                rtn.append(i)
        if isinstance(seq, str):
            return "".join(rtn)
        return [type(seq)(rtn)]
    
    @Node.test_func([10], [[0,2,4,6,8,10]], "}")
    def up_to(self, up_to: Node.number):
        """Repeat until return is bigger than up_to"""
        rtn = []
        val = up_to-1
        i = 0
        while val < up_to:
            val = self.ast.run([i])[-1]
            rtn.append(val)
            i+=1
            if not isinstance(val, (int, float)):
                val = bool(val)
        return [rtn]