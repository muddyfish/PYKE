#!/usr/bin/env python

from nodes import Node

class Head(Node):
    char = "h"
    args = 1
    results = 1
    
    def add_one(self, inp: Node.number):
        """inp+1"""
        return inp+1
    
    def first(self, inp: Node.indexable):
        """inp[0]"""
        return inp[0]