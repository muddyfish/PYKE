#!/usr/bin/env python

from nodes import Node
import lang_ast

class NodeSingle(Node):
    args = 0
    results = 1
    ignore = True

    def __init__(self, value):
        self.value = value
        
    def func(self):
        return self.value

    def __repr__(self):
        return "%s: %d"%(self.__class__.__name__, self.func())
        
    @classmethod
    def accepts(cls, code, accept = False):
        if not accept: return None, None
        if code == "": return None, None
        code, node = lang_ast.AST._add_node(code)
        assert(node is not None)
        return code, cls(node)