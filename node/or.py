#!/usr/bin/env python

from nodes import Node

class Or(Node):
    char = "|"
    args = 2
    results = 1
    def func(self, a,b):
        """a or b. Short circuiting.
if a: return a
if b: return b
return 0"""
        if a: return a
        if b: return b
        return 0