#!/usr/bin/env python

from nodes import Node
from nodes import nodes as all_nodes

import copy

class AssignVar(Node):
    char = "="
    args = 1
    results = 1
    
    def __init__(self, node:Node.NodeClass):
        self.node = node

    def func(self, x):
        """Takes a node as a fixed arg.
Sets the contents of the node to x.
This can also affect how the node behaves"""
        self.node.update_contents(x)
        return x
    
    def __repr__(self):
        return "%s: %s"%(self.__class__.__name__, self.node.__name__)