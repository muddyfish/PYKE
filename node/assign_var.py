#!/usr/bin/env python

from nodes import Node
from nodes import nodes as all_nodes

import copy

class AssignVar(Node):
    char = "="
    args = 1
    results = 0
    
    def __init__(self, node_class):
        self.node_class = node_class

    def func(self, x):
        """Takes a node as a fixed arg.
Sets the contents of the node to x.
This can also affect how the node behaves"""
        self.node_class.update_contents(x)
    
    def __repr__(self):
        return "%s: %s"%(self.__class__.__name__, self.node_class.__name__)
        
    @classmethod
    def accepts(cls, code):
        if code[0] != cls.char: return None, None
        for node_name in all_nodes:
            node = all_nodes[node_name]
            if code[1:].startswith(node.char) and node.char != "":
                return code[1+len(node.char):], cls(node)