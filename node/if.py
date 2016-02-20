#!/usr/bin/env python

import lang_ast
from nodes import Node

class For(Node):
    char = "I"
    args = 1
    results = None
    
    def __init__(self, ast):
        self.ast = ast
        
    def prepare(self, stack):
        self.args = len(stack)
            
    def func(self, *args):
        args = list(args)
        if args[0]:
            args = args[1:]
            stack = self.ast.run(args)
            return stack
        return args[1:]
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.args)
        
    @classmethod
    def accepts(cls, code):
        if cls.char != code[0]: return None, None
        ast = lang_ast.AST()
        code = ast.setup(code[1:])
        return code, cls(ast)