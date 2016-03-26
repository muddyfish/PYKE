#!/usr/bin/env python

from nodes import Node

class In(Node):
    char = "{"
    args = 2
    results = 1
    def func(self, a,b:Node.indexable):
        """a in b"""
        return a in b