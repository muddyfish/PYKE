#!/usr/bin/env python

import glob, os, imp
import node as _

nodes = {}
    
class Node(object):
    char = ""
    func = lambda self: None
    args = 0
    results = 0
    
    def __repr__(self):
        return self.__class__.__name__
        
    def __call__(self, args):
        assert(len(args) == self.args)
        if args == []:
            ret = self.func()
        else:
            ret = self.func(*args)
        if self.results == 0: return []
        if not (isinstance(ret, list) or
                isinstance(ret, tuple)): ret = [ret]
        assert(len(ret) == self.results)
        return ret

    @classmethod
    def accepts(cls, code):
        if code[0] == cls.char:
            return code[1:], cls()
        return None, None


def load_node(node, file_path):
    path_var = "node.%s"%node
    main_module = imp.load_source(path_var, file_path)
    for c in main_module.__dict__.values():
        try:
            if issubclass(c, Node) and c is not Node:
                nodes[node] = c
                return c
        except TypeError: pass
      
for node in glob.glob("node/*.py"):
    load_node(node[5:-3], node)