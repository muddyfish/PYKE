#!/usr/bin/env python

from nodes import Node

class Subtract(Node):
    char = "-"
    args = 2
    results = 1
    def func(self, a,b):
        """a-b. Vanilla subraction."""
        return a-b
    
    def sub_str(self, a:str, b:str):
        """Remove all instances of b from a."""
        out = a[:]
        for i in b:
            out = out.replace(i,"")
        return out