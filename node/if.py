#!/usr/bin/env python

from nodes import Node
from type.type_infinite_list import IntegerList


class If(Node):
    char = "I"
    args = 1
    results = None
    contents = IntegerList()
    
    def __init__(self, ast: Node.EvalLiteral):
        self.ast = ast
        self.uses_i = self.ast.uses_i
        self.ast.uses_i = False
        if self.ast.nodes == []:
            self.ast.add_node("\n")
        
    def prepare(self, stack):
        self.args = max(len(stack), 1)
        if isinstance(stack[0], Node.infinite):
            self.ast.uses_i = self.uses_i
            
    @Node.test_func([5, 1], [10], "}")
    @Node.test_func([5, 0], [5], "}")
    def func(self, *args):
        """Takes stack.
if arg1: stack = eval_literal(stack[:-1]) (extend mode)
else: stack = stack[:-1]"""
        args = list(args)
        if args[-1]:
            if self.uses_i:
                if hasattr(self.ast.i_node, "contents"):
                    old_i = self.ast.i_node.contents
                if args:
                    self.ast.i_node.contents = [args[-1]]
            args = args[:-1]
            stack = self.ast.run(args)
            try:
                self.ast.i_node.contents = old_i
            except (NameError, UnboundLocalError):
                pass
            return stack
        return args[:-1]

    def not_filter_infinite(self, inf: Node.infinite):
        return inf.modify(inf.not_filter, self.ast)
