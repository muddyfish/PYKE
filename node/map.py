#!/usr/bin/env python

import lang_ast
from nodes import Node

class Map(Node):
    char = "m"
    args = 0
    results = None
    contents = 1000
    
    def __init__(self, node):
        self.node = node
        self.args = node.args
        
    def func(self, *args):
        args = list(args)
        max_len = len(args[0])
        for i, arg in enumerate(args):
            if i == 0: continue
            args[i] = [arg]*max_len
        results = []
        for i in zip(*args):
            rtn = self.node(i)
            if len(rtn) == 1: rtn = rtn[0]
            results.append(rtn)
        return results
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.args)
        
    @classmethod
    def accepts(cls, code):
        if code[0] == cls.char:
            code, node = lang_ast.AST.add_node(code[1:])
            assert(node is not None)
            return code, cls(node)
        return None, None