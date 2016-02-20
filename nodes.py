#!/usr/bin/env python

import glob, os, imp
import node as _
import eval as safe_eval
import settings
import collections
import types

nodes = {}

class Node(object):
    char = ""
    func = lambda self: None
    args = 0
    results = 0
    sequence = (list, tuple)
    number = (int, float)
    indexable = (list, tuple, str)
    
    def __repr__(self):
        return self.__class__.__name__
        
    def __call__(self, args):
        while len(args) != self.args:
            if settings.WARNINGS: print("Missing arg to %r, evaling input."%self)
            args.append(safe_eval.evals[settings.SAFE](input()))
        func = self.choose_function(args)
        if args == []:
            ret = func()
        else:
            try:
                ret = func(*args)
            except:
                print("%r failed func %r with args %r"%(self, func.__name__, args))
                raise
        if self.results == 0: return []
        if not (isinstance(ret, list) or
                isinstance(ret, tuple)): ret = [ret]
        if self.results != None:
            if len(ret) != self.results:
                print("%r failed with args %r, returned %r"%(self, args, ret))
                raise AssertionError("Function didn't return correct number of things")
        return ret

    def choose_function(self, args):
        funcs = {0: self.func}
        for k, cur_func in self.__class__.__dict__.items():
            if isinstance(cur_func, types.FunctionType):
                cur_func = getattr(self, k)
                arg_types = cur_func.__annotations__
                if arg_types == {}: continue
                func_arg_names = cur_func.__code__.co_varnames[1:cur_func.__code__.co_argcount]
                arg_types = [arg_types[arg] for arg in func_arg_names if arg in arg_types]
                possible = True
                priority = 0
                for arg in zip(args, arg_types):
                    if not isinstance(*arg): possible = False
                    if not isinstance(arg[1], tuple):length = 1
                    else: length = len(arg[1])
                    priority += 1/length
                if possible:
                    funcs[priority] = cur_func
        func = funcs[max(funcs.keys())]
        return func

    def prepare(self, stack):
        pass

    @classmethod
    def accepts(cls, code):
        if code.startswith(cls.char):
            return code[len(cls.char):], cls()
        return None, None


def load_node(node, file_path):
    path_var = "node.%s"%node
    main_module = imp.load_source(path_var, file_path)
    for c in main_module.__dict__.values():
        try:
            if issubclass(c, Node) and c.__module__ is main_module.__name__:
                nodes[node] = c
                return c
        except TypeError: pass
      
for node in glob.glob("node/*.py"):
    load_node(node[5:-3], node)