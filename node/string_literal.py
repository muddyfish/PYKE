#!/usr/bin/env python

from nodes import Node

class StringLiteral(Node):
    args = 0
    results = 1
    char = '"'

    def __init__(self, string):
        self.string = string


    @Node.test_func([], ["World"], "World\"")
    @Node.test_func([], ["Hello"], "Hello")
    def func(self):
        """String literal. Ends with " """
        return self.string

    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.string)
        
    @classmethod
    def accepts(cls, code):
        if code == "": return None, None
        string = None
        if code[0] == StringLiteral.char:
            string = ""
            if len(code) != 1: 
                code = code[1:]
                while len(code) != 0 and code[0] != StringLiteral.char:
                    string += code[0]
                    code = code[1:]
            if len(code) != 0: code = code[1:]
        if string is not None:
            return code, cls(string)
        return None, None