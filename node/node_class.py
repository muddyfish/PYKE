#!/usr/bin/env python

from nodes import Node
import nodes

class NodeClass(Node):
    args = 0
    results = 1
    ignore = True

    def __init__(self, value):
        self.value = value
        
    def func(self):
        return self.value

    def __repr__(self):
        return "%s: %s"%(self.__class__.__name__, self.func())
        
    @classmethod
    def accepts(cls, code, accept = False):
        if not accept: return None, None
        if code == "": return None, None
        for name in nodes.nodes:
            node = nodes.nodes[name]
            if code.startswith(node.char) and node.char:
                return code[len(node.char):], cls(node)
        return None, None