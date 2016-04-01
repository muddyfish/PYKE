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
        return [rtn]