#!/usr/bin/env python

from nodes import Node

class Splice(Node):
    char = ":"
    args = 3
    results = 1
    
    @Node.test_func(["test", 1, 3], ["es"])
    @Node.test_func(["test", 0, -2], ["te"])
    @Node.test_func(["test", 3, 0], ["tse"])
    def splice(self, a:Node.indexable, b:int, c:int):
        """a[b:c] or a[b:c:-1]"""
        return [a[b:c] or a[b:c:-1]]
    
    @Node.test_func([1, 6, 2], [[1,3,5]])
    @Node.test_func([1.5, 3.5, .5], [[1.5,2.0,2.5,3.0]])
    def range(self, start:Node.number, stop:Node.number, step:Node.number):
        """range(start,stop,step)"""
        rtn = []
        r=start
        while r < stop:
            rtn.append(r)
            r += step
        return [rtn]
    
    @Node.test_func(["test", "t", "."], [".es."])
    def replace(self, a:str, b:str, c:str):
        """a.replace(b,c)"""
        return [a.replace(b,c)]
    
    @Node.test_func(["test", [1,2], "pies"], ["tiet"])
    @Node.test_func([[1,2,3], [0,2], "pies"], [["p",2,"e"]])
    def multi_assign(self, a:Node.indexable, b: Node.sequence, c: Node.indexable):
        """for i in b:
    a[i] = c[i]
return a"""
        if len(c) == 1:
            return self.multi_assign_generic(a,b,c)
        rtn = list(a)
        for i in b:
            rtn[i] = c[i]
        if isinstance(a, str):
            return "".join(rtn)
        return [type(a)(rtn)]
    
    @Node.test_func([[0,0,0,0], [0,3], 1], [[1,0,0,1]])
    def multi_assign_generic(self, a:Node.indexable, b: Node.sequence, c):
        """for i in b:
    a[i] = c
return a"""
        a = a[:]
        for i in b:
            a[i] = c
        return [a]