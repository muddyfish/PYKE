#!/usr/bin/env python

from nodes import Node
import eval as safe_eval
import settings

import copy

class EvalInput(Node):
    char = "Q"
    args = 0
    results = 1
    func = lambda self: [copy.deepcopy(self.inp)]
        
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.func())
        
    @classmethod
    def accepts(cls, code):
        if code[0] != cls.char: return None, None
        if hasattr(cls, "inp"): return code[1:], cls()
        if settings.WARNINGS: print("Q: ", end = "")
        cls.inp = safe_eval.evals[settings.SAFE](input())
        return code[1:], cls()