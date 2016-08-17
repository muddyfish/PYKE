#!/usr/bin/env python

from nodes import Node
from math import ceil

import settings

class Multiply(Node):
    char = "*"
    args = 2
    results = 1
    
    @Node.test_func([4,5], [20])
    def num_mult(self, a:Node.number,b:Node.number):
        """a*b"""
        return a*b
    
    @Node.test_func([["a",2],3], [["a",2,"a",2,"a",2]])
    def seq_mult(self, a:Node.indexable, b:Node.number):
        """Repeat sequence a b times"""
        if isinstance(b, float):
            rtn = a*int(b)
            rtn += a[:ceil((b%1)*len(a))]
            return [rtn]
        return[a*b]
    
    @Node.test_func([2, [1,2,3]], [[1,2,3,1,2,3]])
    def seq_mult_2(self, a:Node.number, b:Node.indexable):
        """Repeat sequence b a times"""
        return self.seq_mult(b,a)
    
    def func(self, a,b):
        """Deprecated, warns if ever used"""
        if settings.WARNINGS: print("Bad mult func")
        return[a*b]