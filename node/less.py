#!/usr/bin/env python

from nodes import Node

class Less(Node):
    char = "<"
    args = 2
    results = 1
    
    @Node.test_func([4,2], [0])  
    @Node.test_func([0,0], [0])  
    @Node.test_func([4,5], [1])  
    def func(self, a,b):
        """a<b"""
        return (a<b)+0
    
    @Node.test_func(["test",2], ["te"])  
    def indexable_1(self, a:Node.indexable, b:int):
        """a[:b]"""
        return [a[:b]]
    
    @Node.test_func([1,"test"], ["tes"])  
    def indexable_2(self, a:int, b:Node.indexable):
        """b[:-a]"""
        return [b[:-a]]

    def inf_over_n(self, n: int, inf: Node.infinite):
        return inf.modify(inf.filter_code, "{}>".format(n))

    def inf_under_n(self, inf: Node.infinite, n: int):
        return inf.modify(inf.filter_code, "{}<".format(n))
