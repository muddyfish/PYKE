#!/usr/bin/env python

from nodes import Node

class Negate(Node):
    char = "_"
    args = 1
    results = 1
    
    def reverse(self, sequence: Node.indexable):
        """sequence[::-1]"""
        return sequence[::-1]
    
    def func(self, a):
        """-a"""
        return -a