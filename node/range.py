#!/usr/bin/env python

from nodes import Node
import itertools

class Range(Node):
    char = "U"
    args = 1
    results = 1
    
    @Node.test_func([4], [[0,1,2,3]])
    def func(self, num:int):
        """range(num)"""
        return [list(range(num))]

    #@Node.test_func([[2,2]], [[[0, 1], [0, 1], [1, 0], [1, 1]]])
    def nd_range(self, seq:Node.sequence):
        values = list(itertools.product(*map(range,seq)))
        return [self.split(values, seq)]
        
    def split(self, values, seq):
        if len(seq) == 1:
            return values
        cur = seq[0]
        len_values = 1
        for i in seq: len_values *= i
        chunk_size = int(len_values/cur)
        array = []
        for i in range(0, len_values, chunk_size):
            array.append(self.split(values[i:i+chunk_size], seq[1:]))
        return array