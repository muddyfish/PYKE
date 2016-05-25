#!/usr/bin/env python

import glob, os, imp
import node as _
import eval as safe_eval
from type.type_time import TypeTime
import lang_ast
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
    clock = TypeTime
    
    Base10Single = "base10_single"
    Base36Single = "base36_single"
    Base96Single = "base96_single"
    IntList = "int_list"
    NumericLiteral = "numeric_literal"
    StringLiteral = "string_literal"
    EvalLiteral = "eval_literal"
    NodeSingle = "node_single"
    NodeClass = "node_class"
    
    def __init__(self):pass
    
    def __repr__(self):
        return self.__class__.__name__

    #def __str__(self):
    #    cls = self.__class__
    #    string = cls.__name__
    #    assert(hasattr(self, "init_args"))
    #    if self.init_args:
    #        return [type(i)for i in self.init_args]
    #    return string
        
    def __call__(self, args):
        self.added_args = 0
        if self.__class__.reverse_first:
            args = args[::-1]
        if self.args is not None:
            if len(args) > self.args:
                raise AssertionError("%s (%d args) got called with %r"%(self.__class__.__name__, self.args, args))
            while len(args) != self.args:
                self.add_arg(args)
                self.added_args += 1
        if not self.__class__.reverse_first:
            args = args[::-1]
        func = self.choose_function(args)
        if args == []:
            ret = func()
        else:
            try:
                ret = func(*args)
            except lang_ast.GotoStart:
                raise
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
            has_star_args = cur_func.__code__.co_flags & 4
            if len(func_arg_names) != self.args and not has_star_args:
                continue
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
        try:
            func = funcs[max(funcs.keys())]
        except ValueError:
            raise AssertionError("No valid func for node %r, args: %r"%(self.__class__.__name__, args))
        return func
    
    @classmethod
    def get_functions(cls, ins = None):
        items = cls.__dict__.items()
        if ins is not None:
            cls = ins
        funcs = [cls.func]
        for k, cur_func in items:
            if isinstance(cur_func, types.FunctionType):
                if k in ["__init__", "func"]: continue
                cur_func = getattr(cls, k)
                if cur_func.__annotations__ != {}:
                    funcs.append(cur_func)
                elif hasattr(cur_func, "is_func") and cur_func.is_func:
                    funcs.append(cur_func)
        if funcs == [cls.func] and cls.func is Node.func:
            print(cls, "No funcs?")
        return funcs
        

    def prepare(self, stack):
        pass

    def add_arg(self, args):
        if settings.WARNINGS: print("Missing arg to %r, evaling input."%self)
        arg = safe_eval.evals[settings.SAFE](input())
        if self.__class__.reverse_first:
            args.insert(0, arg)
        else:
            args.append(arg)
    

    @classmethod
    def accepts(cls, code, args = None):
        if code.startswith(cls.char):
            code = code[len(cls.char):]
            func = cls.__init__
            annotations = func.__annotations__
            arg_names = func.__code__.co_varnames[1:func.__code__.co_argcount]            
            if args == None: args = []
            for arg in arg_names:
                if arg in annotations:
                    #print(arg, annotations[arg])
                    const_arg = annotations[arg]
                    node = nodes[const_arg]
                    accept_args = []
                    accept_args.append(code)
                    if const_arg in (Node.StringLiteral,
                                     Node.Base36Single,
                                     Node.Base10Single,
                                     Node.Base96Single,
                                     Node.IntList,
                                     Node.EvalLiteral,
                                     Node.NumericLiteral,
                                     Node.NodeSingle,
                                     Node.NodeClass):
                        accept_args.append(True)
                    new_code, results = node.accepts(*accept_args)
                    if new_code is None:
                        results = cls.default_arg
                    else:
                        cls.overwrote_default = True
                        code = new_code
                        results = results([])[0]
                    args.append(results)
                #print(code, cls, args)
            obj = cls(*args)
            obj.setup_repr(args)
            return code, obj
        return None, None

    @classmethod
    def update_contents(cls, new_var):
        cls.contents = new_var

    @staticmethod
    def test_func(input_stack, output_stack, args = ""):
        def inner(func):
            if not hasattr(func, "tests"):
                func.tests = []
            func.tests.append((input_stack, output_stack, args))
            return func
        return inner
    
    @classmethod
    def run_tests(cls):
        for func in cls.get_functions():
            if hasattr(func, "tests"):
                for test in func.tests[:]:
                    in_stack, out_stack, args = test
                    args = cls.char + args
                    code, node = cls.accepts(args)
                    in_stack = in_stack[::-1]
                    node.prepare(in_stack)
                    in_stack = in_stack[::-1]
                    assert(code == "")
                    assert(node is not None)
                    if node.choose_function(in_stack).__func__ is not func:
                        raise AssertionError(cls.__name__+"(%r): %r chose %r instead of %r"%(in_stack, out_stack, node.choose_function(in_stack).__name__, func.__name__))
                    rtn_stack = node(in_stack[::-1])
                    for val in rtn_stack:
                        if val is True or val is False:
                            raise(AssertionError(cls.__name__+"(%r): returned %r. Has True/False"%(in_stack, rtn_stack)))
                    if rtn_stack != out_stack:
                        raise AssertionError(cls.__name__+"(%r): %r returned %r"%(in_stack, out_stack, rtn_stack))
    
    def setup_repr(self, args):
        self.init_args = args
       
    def prefer(func):
        func.prefer = True
        return func
    
    def is_func(func):
        func.is_func = True
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
                  Node.IntList,
                  Node.NumericLiteral,
                  Node.StringLiteral,
                  Node.EvalLiteral,
                  Node.NodeSingle), reverse = True)
      
for node in get_nodes():
    load_node(node[5:-3], node)