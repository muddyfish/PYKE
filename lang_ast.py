#!/usr/bin/env python

import nodes
from nodes import Node
import eval as safe_eval
import settings


class AST(object):
    END_CHARS = ")("
    MAX_RECURSE = 0
    
    def setup(self, code, first=False):
        self.first = first
        self.nodes = []
        self.restore_point = None
        self.uses_i = False
        while code != "" and (self.first or code[0] not in AST.END_CHARS):
            code, node = self.add_node(code)
            if node.uses_i:
                self.uses_i = True
                if node.char == "i":
                    self.i_node = node.__class__
                else:
                    self.i_node = node.ast.i_node
        if code != "" and code[0] != "(":
            code = code[1:]
        if len(self.nodes) > 1:
            if isinstance(self.nodes[-1], nodes.nodes[nodes.Node.StringLiteral]):
                self.nodes[-2], self.nodes[-1] = self.nodes[-1], self.nodes[-2]
        return code
    
    def run(self, stack=None):
        if stack is None:
            stack = []
        if self.first:
            retries = 0
        elif self.uses_i:
            if hasattr(self.i_node, "contents"):
                old_i = self.i_node.contents
            if stack:
                self.i_node.contents = [stack[0]]
        counter = 0
        while counter != len(self.nodes):
            cur_node = self.nodes[counter]
            counter += 1
            try:
                cur_node.prepare(stack)
                no_args = cur_node.args
                stack, args = stack[no_args:], stack[:no_args]
                stack = cur_node(args) + stack
            except GotoStart as goto:
                if not self.first:
                    raise
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
        try:
            self.i_node.contents = old_i
        except NameError:
            pass
        if self.first:
            stack = self.implicit_complete(stack)
        return stack
      
    def __repr__(self):
        return str(self.nodes)
    
    def add_node(self, code):
        code, node = AST._add_node(code)
        self.nodes.append(node)
        return code, node
    
    @staticmethod
    def _add_node(code):
        accepting = []
        for name in nodes.nodes:
            node = nodes.nodes[name]
            new_code, new_node = node.accepts(code)
            if new_code is not None:
                assert(new_node is not None)
                accepting.append((node.char, new_code, new_node))
        if not accepting:
            raise SyntaxError("No nodes will accept code: %r"%(code))
        return sorted(accepting, key = lambda node:-len(node[0]))[0][1:]

    def implicit_complete(self, stack):
        stack_types = {Node.infinite: self.strip_infinite}
        for i, value in enumerate(stack):
            for type in stack_types:
                if isinstance(value, type):
                    stack[i] = stack_types[type](stack[i])
        return stack

    def strip_infinite(self, infinite):
        try:
            arg = safe_eval.evals[settings.SAFE](input())
        except EOFError:
            return infinite
        if arg == "":
            return infinite
        if isinstance(arg, str) and arg.isnumeric():
            arg = int(arg)
            return "\n".join(map(str, infinite[:arg]))
        elif isinstance(arg, int):
            return infinite[arg]
        elif isinstance(arg, Node.sequence):
            sequence = infinite[:max(arg)+1]
            return "\n".join(str(sequence[i]) for i in arg)
        return infinite


class GotoStart(RuntimeError):
    def __init__(self, stack):
        self.stack = stack


def test_code(code, out_stack):
    ast = AST()
    ast.setup(code, first = True)
    rtn_stack = ast.run()
    assert rtn_stack == out_stack, "rtn: %s, wanted: %s (code: %s)" % (rtn_stack, out_stack, code)
