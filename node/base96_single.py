#!/usr/bin/env python

from nodes import Node

class Base96Single(Node):
    char = "w"
    args = 0
    results = 1
    
    def __init__(self, value):
        self.value = value
        
    def func(self):
        return self.value
    
    def __repr__(self):
        return "%s: %d"%(self.__class__.__name__, self.func())
        
    @classmethod
    def accepts(cls, code, accept = False):
        if accept: code = "w"+code
        if code == "" or\
           (code[0] != cls.char): return None, None
        value = ord(code[1])-32
        return code[2:], cls(value)
    