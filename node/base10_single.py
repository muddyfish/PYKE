#!/usr/bin/env python

from nodes import Node


class Base10Single(Node):
    char = ""
    args = 0
    results = 1
    ignore = True

    def __init__(self, value):
        self.value = value
        
    def func(self):
        return self.value

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.func())
        
    @classmethod
    def accepts(cls, code, accept=False):
        if not accept:
            return None, None
        if not code:
            return None, None
        try:
            value = int(chr(code[0]))
        except ValueError:
            return None, None
        return code[1:], cls(value)
