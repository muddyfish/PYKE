#!/usr/bin/env python

from nodes import Node

class StringLiteral(Node):
    args = 0
    results = 1
    char = '"'

    def __init__(self, string):
        self.string = string

    @Node.test_func([], [""], "")
    @Node.test_func([], ["World"], "World\"")
    @Node.test_func([], ["Hello"], "Hello")
    def func(self):
        """String literal. Ends with " """
        return self.string

    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.string)
        
    @classmethod
    def accepts(cls, code, accept = False):
        if accept: code = '"'+code
        if code == "": return None, None
        if code[0] != StringLiteral.char:return None, None
        code = code[1:]
        string, sep, code = code.partition(StringLiteral.char)
        if sep == "":
            code = "+"
        return code, cls(string)