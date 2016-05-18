#!/usr/bin/env python

import lang_ast
from nodes import Node

class IfKill(Node):
    char = ".I"
    args = 1
    results = None
    
    def __init__(self, ast: Node.EvalLiteral):
        self.ast = ast
        if self.ast.nodes == []:
            self.ast.add_node("\n")
        
    def prepare(self, stack):
        self.args = max(len(stack), 1)
            
    @Node.test_func([5,1], [10], "}")
    @Node.test_func([5,0], [], "}")
    def func(self, *args):
        """Takes stack.
if arg1: stack = eval_literal(stack[:-1]) (extend mode)
else: stack = []"""
        args = list(args)
        if args[-1]:
            args = args[:-1]
            stack = self.ast.run(args)
            return stack
        return []