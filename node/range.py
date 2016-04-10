#!/usr/bin/env python

from nodes import Node
import itertools

class Range(Node):
    char = "U"
    args = 1
    results = 1
    contents = ["second", "minute", "hour", "day", "week", "month", "year", "decade", "century", "millennium"]
    
    @Node.test_func([4], [[0,1,2,3]])
    def func(self, num:int):
        """range(num)"""
        return [list(range(num))]

    #@Node.test_func([[2,2]], [[[0, 1], [0, 1], [1, 0], [1, 1]]])
    def nd_range(self, seq:Node.sequence):
        """Return a n dimensional range where n = len(seq).
Each dimension's length is equal to the current item in the seq.
Each item in the returned list is a list with it's coords."""
        values = list(itertools.product(*map(range,seq)))
        return [self.split(values, seq)]
        
    def split(self, values, seq):
        if len(seq) == 1:
            return [list(i)for i in values]
        cur = seq[0]
        len_values = 1
        for i in seq: len_values *= i
        chunk_size = int(len_values/cur)
        array = []
        for i in range(0, len_values, chunk_size):
            array.append(self.split(values[i:i+chunk_size], seq[1:]))
        return array