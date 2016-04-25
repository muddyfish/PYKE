#!/usr/bin/env python

from nodes import Node

class Iterator(Node):
    char = "o"
    args = 0
    results = 1
    contents = 0
    
    def iterate(self):
        """contents += 1
return contents-1"""
        Iterator.contents += 1
        return Iterator.contents-1