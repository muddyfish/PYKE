#!/usr/bin/env python

from nodes import Node

import copy
import settings

class AutoAssignVar(Node):
    char = ""
    args = 0
    results = None
    ignore = True
    
    def func(self):
        """If has contents, return contents.
Otherwise set contents to stack[0] and return"""
        pass
    
    def prepare(self, stack):
        self.args |= not hasattr(self.__class__, "contents")
        self.func = (self.retrieve, self.store)[self.args]
            
    def retrieve(self):
        return copy.deepcopy(self.__class__.contents)
    
    def store(self, arg):
        self.__class__.contents = [arg]
        if settings.WARNINGS: print("Stored %r in %s"%(arg, self.char))
        return [arg]

    @classmethod
    def accepts(cls, code):
        if cls is AutoAssignVar: return None, None
        if code[0] == cls.char:
            return code[1:], cls()
        return None, None