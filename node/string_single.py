#!/usr/bin/env python

from nodes import Node


class StringSingle(Node):
    args = 0
    results = 1
    char = "\\"

    def __init__(self, string):
        self.string = string

    @Node.test_func([], ["!"], "!")
    def func(self):
        """Add a single char onto the stack"""
        return self.string
    
    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.func())
        
    @classmethod
    def accepts(cls, code, accept=False):
        if not code:
            return None, None
        if accept:
            return code[1:], cls(code[1:].decode())
        if code[:1] != b'\\':
            return None, None
        string = code[1:2].decode()
        code = code[2:]
        return code, cls(string)
