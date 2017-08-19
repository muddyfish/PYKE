#!/usr/bin/env python

from nodes import Node


class List(Node):
    char = "]"
    args = 0
    results = 1
    default_arg = 2
    contents = []
    
    def __init__(self, size: Node.Base10Single):
        self.args = size
        
    def prepare(self, stack):
        if self.args == 0:
            self.args = len(stack)

    @Node.test_func([5, 6, 1, 2], [[5, 6, 1, 2]], "4")
    @Node.test_func(["Hello", "World"], [["Hello", "World"]])
    def func(self, *inp):
        """Take the top `amount` items from the stack and turn them into a list.
Defaults to the whole stack"""
        return [list(inp)]
