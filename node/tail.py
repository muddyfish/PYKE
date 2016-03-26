#!/usr/bin/env python

from nodes import Node

class Tail(Node):
    char = "t"
    args = 1
    results = 1
    
    def sub_one(self, inp: Node.number):
        """inp-1"""
        return inp-1
    
    def first(self, inp: Node.indexable):
        """inp[1:]"""
        return [inp[1:]]