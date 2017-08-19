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
        if accept:
            code = b'"'+code
        if not code:
            return None, None
        if code[0] != StringLiteral.char[0]:
            return None, None
        code = code[1:]
        rtn = ""
        end = False
        while code and not end:
            rtn += chr(code[0])
            code = code[1:]
            if rtn.endswith('"'):
                if rtn.endswith(r'\"') and not rtn.endswith(r'\\"'):
                    continue
                end = True
                if rtn.endswith(r'\\"'):
                    rtn = rtn[:-1]
                rtn = rtn[:-1]
        if rtn.endswith('"') and not rtn.endswith(r'\"'):
            rtn = rtn[:-1]
        rtn = rtn.replace(r'\"', '"')
        return code, cls(rtn)
