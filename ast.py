#!/usr/bin/env python

import nodes

class AST(object):
    def __init__(self, code):
        self.nodes = []
        while code != "":
            code = self.add_node(code)
        print self.nodes
        
    def add_node(self, code):
        for name in nodes.nodes:
            node = nodes.nodes[name]
            new_code, new_node = node.accepts(code)
            if new_code is not None:
                assert(new_node is not None)
                self.nodes.append(new_node)
                return new_code
        raise SyntaxError("No nodes will accept code: %s"%(code))