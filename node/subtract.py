#!/usr/bin/env python

from nodes import Node

class Subtract(Node):
    char = "-"
    args = 2
    results = 1
    
    
    @Node.test_func([4,5], [-1])
    @Node.test_func([42,7], [35])
    def func(self, a,b):
        """a-b. Vanilla subraction."""
        return a-b
    
    @Node.test_func(["test","te"], ["s"])
    @Node.test_func(["test","ts"], ["e"])
    def sub_str(self, a:str, b:str):
        """Remove all characters in b from a."""
        out = a[:]
        for i in b:
            out = out.replace(i,"")
        return out