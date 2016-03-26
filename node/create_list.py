#!/usr/bin/env python

from nodes import Node

class Join(Node):
    char = "]"
    args = 0
    results = 1
    default_arg = 2
    
    def __init__(self, size: Node.Base36Single):
        self.args = size
        
    def prepare(self, stack):
        if self.args == 0:
            self.args = len(stack)

    def func(self, *inp):
        """Take the top `amount` items from the stack and turn them into a list.
Defaults to the whole stack"""
        return [inp]
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.args)
        