#!/usr/bin/env python

from nodes import Node
import copy

class Splice(Node):
    char = ":"
    args = 3
    results = 1
    contents = "+-*/"
    
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
        if isinstance(step, float):
            r = float(r)
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
    def multi_assign(self, seq:Node.indexable, indecies: Node.sequence, values: Node.indexable):
        """for i in indecies:
    seq[i] = values[i]
return seq"""
        if len(values) == 1:
            return self.multi_assign_generic(seq,indecies,values)
        rtn = list(seq)
        for i in indecies:
            rtn[i] = values[i]
        if isinstance(seq, str):
            return "".join(rtn)
        return [type(seq)(rtn)]
    
    @Node.test_func([[0,0,0,0], [0,3], 1], [[1,0,0,1]])
    def multi_assign_generic(self, seq:Node.indexable, indecies: Node.sequence, obj):
        """for index in indecies:
    seq[index] = obj
return seq"""
        rtn = list(copy.deepcopy(seq))
        for index in indecies:
            rtn[index] = copy.deepcopy(obj)
        if isinstance(seq, str):
            return "".join(rtn)
        return [type(seq)(rtn)]
    
    @Node.test_func(["test", -3, "a"], ["teast"])
    @Node.test_func(["test", -1, "y"], ["testy"])
    @Node.test_func(["test", 0, "un"], ["untest"])
    def insert(self, seq:Node.indexable, index:int, obj):
        """Insert obj into seq at index.
If obj is an int convert it to a float first"""
        if isinstance(obj, float) and obj%1 == 0:
            obj = int(obj)
        rtn = list(seq)
        if index == -1:
            rtn.append(obj)
        elif index < -1:
            rtn.insert(index+1, obj)
        else:
            rtn.insert(index, obj)
        if isinstance(seq, str):
            return "".join(map(str,rtn))
        return [type(seq)(rtn)]