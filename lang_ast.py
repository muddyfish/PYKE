#!/usr/bin/env python

import nodes

class AST(object):
    END_CHARS = ")("
    MAX_RECURSE = 0
    def setup(self, code, first = False):
        self.first = first
        self.nodes = []
        self.restore_point = None
        while code != "" and (self.first or code[0] not in AST.END_CHARS):
            code, node = AST.add_node(code)
            self.nodes.append(node)
        #print self.nodes
        if code != "" and code[0] != "(":
            code = code[1:]
        return code
    
    def run(self, stack = None):
        if stack == None:
            stack = []
        if self.first:
            retries = 0
        counter = 0
        while counter != len(self.nodes):
            cur_node = self.nodes[counter]
            counter += 1
            #print(cur_node)
            #print(stack)
            try:
                cur_node.prepare(stack)
                no_args = cur_node.args
                stack, args = stack[no_args:], stack[:no_args]
                stack = cur_node(args) + stack
            except GotoStart as goto:
                if not self.first: raise
                stack = goto.stack
                self.restore_point = [stack, counter]
                counter = 0
                retries += 1
                if retries == AST.MAX_RECURSE:
                    if self.restore_point is not None:
                        stack, counter = self.restore_point
                        self.restore_point = None
                    else:
                        counter = len(self.nodes)
            except:
                if self.restore_point is not None:
                    stack, counter = self.restore_point
                    self.restore_point = None
                else:
                    raise
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

class GotoStart(RuntimeError):
    def __init__(self, stack):
        self.stack = stack

def test_code(code, out_stack):
    ast = AST()
    ast.setup(code, first = True)
    rtn_stack = ast.run()
    assert(rtn_stack == out_stack)