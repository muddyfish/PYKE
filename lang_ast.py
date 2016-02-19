#!/usr/bin/env python

import nodes

class AST(object):
    def __init__(self, code):
        self.nodes = []
        while code != "":
            code, node = AST.add_node(code)
            self.nodes.append(node)
        print self.nodes
        
    def run(self):
        stack = []
        counter = 0
        while counter != len(self.nodes):
            cur_node = self.nodes[counter]
            print cur_node, stack
            cur_node.prepare(stack)
            no_args = cur_node.args
            stack, args = stack[no_args:], stack[:no_args]
            stack = cur_node(args) + stack
            counter += 1
        for obj in stack[::-1]:
            print obj
        
    @staticmethod
    def add_node(code):
        for name in nodes.nodes:
            node = nodes.nodes[name]
            new_code, new_node = node.accepts(code)
            if new_code is not None:
                assert(new_node is not None)
                return new_code, new_node
        raise SyntaxError("No nodes will accept code: %s"%(code))