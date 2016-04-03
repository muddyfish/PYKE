#!/usr/bin/env python

from nodes import Node
import lang_ast

class NoOp(Node):
    char = " "
    contents = " "
    
    def func(self):
        """Does nothing"""
        pass
    
    @classmethod
    def accepts(cls, code):
        if code[0] in cls.char+lang_ast.AST.END_CHARS:
            return code[1:], cls()
        return None, None