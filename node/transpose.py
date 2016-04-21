#!/usr/bin/env python

from nodes import Node

class Transpose(Node):
    char = ","
    args = 1
    results = 1
    
    @Node.test_func([[[1,2,3],[4,5,6]]], [[[1,4],[2,5],[3,6]]])
    def transpose(self, inp: Node.sequence):
        """zip(*inp)"""
        if all(isinstance(i,str)for i in inp):
            return[["".join(s)for s in zip(*inp)]]
        return[list(map(list,zip(*inp)))]
    
    @Node.test_func([4], [2])
    @Node.test_func([9], [3])
    def sqrt(self, inp):
        sqrt = inp ** 0.5
        if sqrt%1:
            return sqrt
        return int(sqrt)