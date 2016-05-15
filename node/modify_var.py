#!/usr/bin/env python

from nodes import Node
from nodes import nodes as all_nodes

import copy

class ModifyVar(Node):
    char = "?"
    args = None
    results = 1
    
    def __init__(self, op_node:Node.NodeSingle, mod_node:Node.NodeClass):
        self.op_node = op_node
        self.mod_node = mod_node
        self.args = op_node.args - 1
        assert(self.args != -1)

    def func(self, *args):
        """Takes 2 nodes as fixed args.
Modifies the contents of node_B to node_A(inp, node_B.contents).
This can also affect how the node behaves"""
        old = getattr(self.mod_node, "contents")
        args = [*args, old]
        new = self.op_node(args)
        self.mod_node.update_contents(new)
        return new
    
    def __repr__(self):
        return "%s: (%s) %s"%(self.__class__.__name__, self.op_node, self.mod_node.__name__)