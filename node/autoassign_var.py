#!/usr/bin/env python

from nodes import Node

import copy
import settings

class AutoAssignVar(Node):
    char = "i"
    args = 0
    results = 1
    
    def prepare(self, stack):
        if hasattr(self.__class__, "contents"):
            self.func = self.retrieve
        else:
            self.args = 1
            self.func = self.store
            
    def retrieve(self):
        return copy.deepcopy(self.__class__.contents)
    
    def store(self, arg):
        self.__class__.contents = arg
        if settings.WARNINGS: print "Stored %r in i"%arg
        return arg

    @classmethod
    def accepts(cls, code):
        if cls is AutoAssignVar: return None, None
        if code[0] == cls.char:
            return code[1:], cls()
        return None, None