#!/usr/bin/env python

import os
import signal

import eval as safe_eval
import nodes
import settings
from nodes import Node

is_windows = hasattr(os.sys, 'winver')


class AST(object):
    END_CHARS = ")("
    run = True
    
    def setup(self, code, first=False):
        self.first = first
        self.nodes = []
        self.uses_i = False
        self.uses_j = False
        while code != "" and (self.first or code[0] not in AST.END_CHARS):
            code, node = self.add_node(code)
            if node.uses_i:
                self.uses_i = True
                if node.char == "i":
                    self.i_node = node.__class__
                else:
                    self.i_node = node.ast.i_node
            if node.uses_j:
                self.uses_j = True
                if node.char == "j":
                    self.j_node = node.__class__
                else:
                    self.j_node = node.ast.j_node
        if code != "" and code[0] != "(":
            code = code[1:]
        if len(self.nodes) > 1:
            if isinstance(self.nodes[-1], nodes.nodes[nodes.Node.StringLiteral]):
                self.nodes[-2], self.nodes[-1] = self.nodes[-1], self.nodes[-2]
        return code
    
    def run(self, stack=None):
        if stack is None:
            stack = []
        if self.uses_i:
            if hasattr(self.i_node, "contents"):
                old_i = self.i_node.contents
            if stack:
                self.i_node.contents = [stack[0]]
        counter = 0
        while counter != len(self.nodes) and AST.run:
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
                restore_point = [stack, counter]
                counter = 0
            except:
                if restore_point is not None:
                    stack, counter = restore_point
                    restore_point = None
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
            raise SyntaxError("No nodes will accept code: {}".format(repr(code)))
        return sorted(accepting, key=lambda node:-len(node[0]))[0][1:]

    def implicit_complete(self, stack):
        stack_types = {Node.infinite: self.strip_infinite}
        for i, value in enumerate(stack):
            for stack_type, func in stack_types.items():
                if isinstance(value, stack_type):
                    stack[i] = func(stack[i])
        return stack

    def strip_infinite(self, infinite):
        infinite.prepend(next(infinite))
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


if is_windows:
    signal.signal(signal.SIGBREAK, lambda: setattr(AST, "run", False))
else:
    signal.signal(signal.SIGTERM, lambda: setattr(AST, "run", False))


class GotoStart(RuntimeError):
    def __init__(self, stack):
        self.stack = stack


def test_code(code, out_stack):
    ast = AST()
    ast.setup(code, first=True)
    rtn_stack = ast.run()
    assert rtn_stack == out_stack, "rtn: %s, wanted: %s (code: %s)" % (rtn_stack, out_stack, code)
