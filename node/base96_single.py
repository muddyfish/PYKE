#!/usr/bin/env python

from nodes import Node

class Base96Single(Node):
    char = "w"
    args = 0
    results = 1
    
    def __init__(self, value):
        """ord(`arg1`)-32"""
        self.value = value
        
    @Node.test_func([], [0], " ")
    @Node.test_func([], [1], "!")
    @Node.test_func([], [-32], "\x00")
    def func(self):
        """Return ord(const_arg)-32"""
        return self.value
    
    def __repr__(self):
        return "%s: %d"%(self.__class__.__name__, self.func())
        
    @classmethod
    def accepts(cls, code, accept=False):
        if accept:
            code = b"w"+code
        if not code:
            return None, None
        if code[0] != cls.char[0]:
            return None, None
        value = 0
        new = code[1]
        code = code[2:]
        while new & 0x80:
            value |= (new & 0x7F)
            value <<= 7
            new = code[0]
        value |= new
        value -= 32
        return code, cls(value)
