#!/usr/bin/env python

nodes = {}

class MetaNode(type):
    def __new__(cls, name, bases, attrs):
        new = super(MetaNode, cls).__new__(cls, name, bases, attrs)
        if bases[0] is not object:
            nodes[name] = new
        return new
    
class Node(object):
    __metaclass__ = MetaNode
    char = ""
    func = lambda: None
    args = 0
    results = 0
    
    def __init__(self):
        print self
        
    def __repr__(self):
        return self.__class__.__name__
        
    def __call__(self, *args):
        assert(len(args) == self.args)
        ret = func(*args)
        assert(len(ret) == self.results)
        return ret

    @classmethod
    def accepts(cls, code):
        if code[0] == cls.char:
            return code[1:], cls()
        return None, None

class PrintFunc(Node):
    char = "p"
    args = 1
    results = 1
    def func(arg):
        print arg
        return arg
    
class NumericLiteral(Node):
    args = 0
    results = 1

    def __init__(self, digits):
        self.func = lambda: digits

    def __repr__(self):
        return "%s: %d"%(self.__class__.__name__, self.func())
        
    @classmethod
    def accepts(cls, code):
        digits = ""
        while code[0].isdigit():
            digits += code[0]
            code = code[1:]
        if digits:
            return code, cls(int(digits))
        return None, None
    
class StringLiteral(Node):
    args = 0
    results = 1

    def __init__(self, string):
        self.func = lambda: string

    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.func())
        
    @classmethod
    def accepts(cls, code):
        string = None
        if code[0] == '"':
            string = ""
            if len(code) != 1: 
                code = code[1:]
                while len(code) != 0 and code[0] != '"':
                    string += code[0]
                    code = code[1:]
            if len(code) != 0: code = code[1:]
        if string is not None:
            return code, cls(string)
        return None, None