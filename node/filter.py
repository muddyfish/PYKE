#!/usr/bin/env python

from nodes import Node

class Filter(Node):
    char = "#"
    args = 1
    results = None
    
    def __init__(self, ast: Node.EvalLiteral):
        self.ast = ast

    def prepare(self, stack):
        self.args = max(len(stack), 1)
        stack.reverse()
        
    @Node.test_func([[1,2,3,0]], [[1,2,3]], "")
    @Node.test_func([[1,2,3,4,5]], [[2,3,5]], "Plt!")
    @Node.test_func([2,[1,2,3,4,5]], [[2],2], "q")
    def func(self, seq: Node.indexable, *args):
        """filter seq on Truthiness - returns the same type as given"""
        rtn = []
        for i in seq:
            val = self.ast.run([i, *args])
            if val and val[0]:
                rtn.append(i)
        if isinstance(seq, str):
            return ["".join(rtn), *args]
        return [type(seq)(rtn), *args]
    
    @Node.test_func([10], [[0,2,4,6,8,10]], "}")
    def up_to(self, up_to: Node.number, *args):
        """Repeat until return is bigger or equal to up_to"""
        rtn = []
        val = up_to-1
        i = 0
        while val < up_to:
            val = self.ast.run([i, *args])
            if val != []: val = val[0]
            rtn.append(val)
            i+=1
            if not isinstance(val, (int, float)):
                val = bool(val)
        return [rtn, *args]
    
    def filter_values(self, dic:dict, *args):
        rtn = {}
        for key in dic:
            val = self.ast.run([dic[key], key, *args])
            if val and val[0]:
                rtn[key] = val[0]
        return [rtn, *args]