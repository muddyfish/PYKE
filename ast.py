#!/usr/bin/env python

import nodes

class AST(object):
    def __init__(self, code):
        self.nodes = []
        while code != "":
            code = self.add_node(code)
        print self.nodes
        
    def run(self):
        stack = []
        counter = 0
        while counter != len(self.nodes):
            cur_node = self.nodes[counter]
            #print cur_node, stack
            no_args = cur_node.args
            stack, args = stack[no_args:], stack[:no_args]
            stack = cur_node(args) + stack
            counter += 1
        for obj in stack[::-1]:
            print obj
        
    def add_node(self, code):
        for name in nodes.nodes:
            node = nodes.nodes[name]
            new_code, new_node = node.accepts(code)
            if new_code is not None:
                assert(new_node is not None)
                self.nodes.append(new_node)
                return new_code
        raise SyntaxError("No nodes will accept code: %s"%(code))