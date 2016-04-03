#!/usr/bin/env python

import nodes

class AST(object):
    END_CHARS = ")("
    def setup(self, code, first = False):
        self.nodes = []
        while code != "" and (first or code[0] not in AST.END_CHARS):
            code, node = AST.add_node(code)
            self.nodes.append(node)
        #print self.nodes
        if code != "" and code[0] != "(": code = code[1:]
        return code
    
    def run(self, stack = None):
        if stack is None:
            stack = []
        counter = 0
        while counter != len(self.nodes):
            cur_node = self.nodes[counter]
            #print(cur_node, stack)
            cur_node.prepare(stack)
            no_args = cur_node.args
            stack, args = stack[no_args:], stack[:no_args]
            stack = cur_node(args) + stack
            counter += 1
        return stack
        
    @staticmethod
    def add_node(code):
        accepting = []
        for name in nodes.nodes:
            node = nodes.nodes[name]
            new_code, new_node = node.accepts(code)
            if new_code is not None:
                assert(new_node is not None)
                accepting.append((node.char, new_code, new_node))
        if accepting == []:
            raise SyntaxError("No nodes will accept code: %r"%(code))
        return sorted(accepting, key = lambda i:len(i[0]))[0][1:]
        
def test_code(code, out_stack):
    ast = AST()
    ast.setup(code, first = True)
    rtn_stack = ast.run()
    assert(rtn_stack == out_stack)