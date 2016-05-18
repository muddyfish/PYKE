#!/usr/bin/env python

from nodes import Node
from nodes import nodes as all_nodes

import copy

class GetVar(Node):
    char = "~"
    args = 0
    results = 1
    
    def __init__(self, node:Node.NodeClass):
        self.node = node

    def func(self):
        """return the contents of `node`"""
        return [getattr(self.node, "contents")]
    
    @classmethod
    def run_tests(cls):
        cls.func.tests = []
        for node_name in all_nodes:
            node_cls = all_nodes[node_name]
            if hasattr(node_cls, "contents"):
                cls.func.tests.append(([], [node_cls.contents], node_cls.char))
        super(GetVar, cls).run_tests()
    