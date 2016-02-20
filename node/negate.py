#!/usr/bin/env python

from nodes import Node

class Negate(Node):
    char = "_"
    args = 1
    results = 1
    
    def reverse(self, sequence: Node.indexable):
        return a[::-1]
    
    def func(self, a):
        return -a