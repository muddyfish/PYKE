#!/usr/bin/env python

import nodes

class AST(object):
    END_CHARS = ");"
    def setup(self, code):
        self.nodes = []
        while code != "" and code[0] not in AST.END_CHARS:
            code, node = AST.add_node(code)
            self.nodes.append(node)
        #print self.nodes
        if code != "": code = code[1:]
        return code
    
    def run(self, stack = None):
        if stack is None:
            stack = []
        counter = 0
        while counter != len(self.nodes):
            cur_node = self.nodes[counter]
            #print cur_node, stack
            cur_node.prepare(stack)
            no_args = cur_node.args
            stack, args = stack[no_args:], stack[:no_args]
            stack = cur_node(args) + stack
            counter += 1
        return stack
        
    @staticmethod
    def add_node(code):
        for name in nodes.nodes:
            node = nodes.nodes[name]
            new_code, new_node = node.accepts(code)
            if new_code is not None:
                assert(new_node is not None)
                return new_code, new_node
        raise SyntaxError("No nodes will accept code: %s"%(code))