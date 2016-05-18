#!/usr/bin/env python

from nodes import Node
from nodes import nodes as all_nodes

import copy

class ModifyVar(Node):
    char = "?"
    args = None
    results = None
    
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
        args = list(args)+[old]
        new = self.op_node(args)
        if len(new) == 1:
            self.mod_node.update_contents(new[0])
        else:
            self.mod_node.update_contents(new)
        return new
    