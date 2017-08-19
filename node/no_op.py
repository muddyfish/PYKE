#!/usr/bin/env python

import lang_ast
from nodes import Node


class NoOp(Node):
    char = " "
    contents = " "
    args = 1
    results = 1

    def func(self, arg):
        """Does nothing"""
        return [arg]
    
    @classmethod
    def accepts(cls, code):
        if code[:1] in cls.char+lang_ast.AST.END_CHARS:
            return code[1:], cls()
        return None, None
