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
    ignore = False
    reverse_first = False
    default_arg = None
    overwrote_default = False
    
    sequence = (list, tuple)
    number = (int, float)
    indexable = (list, tuple, str)
    
    Base10Single = "base10_single"
    Base36Single = "base36_single"
    Base96Single = "base96_single"
    NumericLiteral = "numeric_literal"
    StringLiteral = "string_literal"
    EvalLiteral = "eval_literal"
    
    def __init__(self):pass
    
    def __repr__(self):
        return self.__class__.__name__
        
    def __call__(self, args):
        if self.__class__.reverse_first:
            args = args[::-1]
        while len(args) != self.args:
            if settings.WARNINGS: print("Missing arg to %r, evaling input."%self)
            args.append(safe_eval.evals[settings.SAFE](input()))
        if not self.__class__.reverse_first:
            args = args[::-1]
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
        funcs = {}
        for cur_func in self.get_functions(self):
            arg_types_dict = cur_func.__annotations__
            func_arg_names = cur_func.__code__.co_varnames[1:cur_func.__code__.co_argcount]
            arg_types = []
            for arg in func_arg_names:
                if arg in arg_types_dict:
                    arg_types.append(arg_types_dict[arg])
                else:
                    arg_types.append(object)
            possible = True
            priority = 0
            for arg in zip(args, arg_types):
                if not isinstance(*arg): possible = False
                if not isinstance(arg[1], tuple):length = 1
                else: length = len(arg[1])
                priority += 1/length
                if arg[1] is object: priority -= 1
                if hasattr(cur_func, "prefer") and cur_func.prefer:
                    priority += 1000
            if possible:
                funcs[priority] = cur_func
        func = funcs[max(funcs.keys())]
        return func
    
    @classmethod
    def get_functions(cls, ins = None):
        items = cls.__dict__.items()
        if ins is not None:
            cls = ins
        funcs = [cls.func]
        for k, cur_func in items:
            if isinstance(cur_func, types.FunctionType):
                if k == "__init__": continue
                cur_func = getattr(cls, k)
                if cur_func.__annotations__ != {}:
                    funcs.append(cur_func)
        return funcs
        

    def prepare(self, stack):
        pass

    @classmethod
    def accepts(cls, code):
        if code.startswith(cls.char):
            code = code[len(cls.char):]
            annotations = cls.__init__.__annotations__
            args = []
            if annotations:
                assert(len(annotations) == 1)
                const_arg = list(annotations.values())[0]
                node = nodes[const_arg]
                accept_args = []
                if const_arg == "string_literal":
                    code = '"'+ code
                accept_args.append(code)
                if const_arg in (Node.Base36Single,
                                 Node.Base10Single,
                                 Node.Base96Single,
                                 Node.EvalLiteral,
                                 Node.NumericLiteral):
                    accept_args.append(True)
                new_code, results = node.accepts(*accept_args)
                if new_code is None:
                    results = cls.default_arg
                else:
                    cls.overwrote_default = True
                    code = new_code
                    results = results([])[0]
                args.append(results)
            return code, cls(*args)
        return None, None

    @classmethod
    def update_contents(cls, new_var):
        cls.contents = new_var
        
    @staticmethod
    def test(code, input_stack, output_stack):
        def inner(node_cls):
            if not settings.DEBUG: return node_cls
            rtn_code, node = node_cls.accepts(code)
            assert(rtn_code == "")
            assert(node is not None)
            node.prepare(input_stack)
            rtn_stack = node(input_stack)
            if rtn_stack != output_stack:
                raise AssertionError(node_cls.__name__+": %r returned %r"%(input_stack, rtn_stack))
            return node_cls
        return inner
    
    def prefer(func):
        func.prefer = True
        return func

def load_node(node, file_path):
    path_var = "node.%s"%node
    main_module = imp.load_source(path_var, file_path)
    for c in main_module.__dict__.values():
        try:
            if issubclass(c, Node) and c.__module__ is main_module.__name__:
                nodes[node] = c
                return c
        except TypeError: pass
      
def get_nodes():
    nodes = glob.glob("node/*.py")
    return sorted(nodes, key = lambda node: node[5:-3] in
                 (Node.Base10Single,
                  Node.Base36Single,
                  Node.Base96Single,
                  Node.NumericLiteral,
                  Node.StringLiteral,
                  Node.EvalLiteral), reverse = True)
      
for node in get_nodes():
    load_node(node[5:-3], node)