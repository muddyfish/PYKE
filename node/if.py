#!/usr/bin/env python

import lang_ast
from nodes import Node

class If(Node):
    char = "I"
    args = 1
    results = None
    
    def __init__(self, ast: Node.EvalLiteral):
        self.ast = ast
        
    def prepare(self, stack):
        self.args = max(len(stack), 1)
            
    def func(self, *args):
        """Takes stack.
if arg1: stack = eval_literal(stack[1:]) (extend mode)
else: stack = stack[1:]"""
        args = list(args)
        if args[0]:
            args = args[1:]
            stack = self.ast.run(args)
            return stack
        return args[1:]
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.args)
        