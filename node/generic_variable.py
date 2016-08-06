#!/usr/bin/env python

from nodes import Node

import copy

class Variable(Node):
    char = ""
    args = 0
    results = 1

    def func(self):
        return copy.deepcopy(self.__class__.contents)
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.__class__.contents)
    
    @classmethod
    def run_tests(cls):
        try:
            cls.func.tests
        except AttributeError:
            cls.func.tests = []
        #cls.func.tests.append(([], [cls.contents], ""))
        super().run_tests()