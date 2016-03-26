#!/usr/bin/env python

from nodes import Node
import math

class End(Node):
    char = "e"
    args = 1
    results = 1
    contents = math.e
    
    def complement(self, inp: Node.number):
        """-(inp+1)"""
        return ~inp
    
    def end(self, inp: Node.indexable):
        """inp[-1]"""
        return inp[-1]