#!/usr/bin/env python

from nodes import Node

class HeadEnd(Node):
    char = "}"
    args = 1
    results = 2
    
    def double(self, inp: Node.number):
        """inp*2"""
        self.results = 1
        return inp*2
        
    def head_end(self, inp:Node.indexable):
        """inp[0], inp[-1]"""
        return [inp[0], inp[-1]]