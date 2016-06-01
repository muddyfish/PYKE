#!/usr/bin/env python

from nodes import Node

class Sum(Node):
    char = "s"
    args = 0
    results = 1
    default_arg = None
    
    def __init__(self, args: Node.Base10Single):
        if args == 0:
            args = 36
        self.args = args
        
    def prepare(self, stack):
        if len(stack) == 0:
            self.add_arg(stack)
        if self.args == Sum.default_arg:
            if isinstance(stack[0], (list,tuple)):
                self.args = 1
            else:
                self.args = len(stack)
        if self.args == 1 and isinstance(stack[0], (str,int)):
            self.func = self.digital_root
    
    @Node.test_func([1,2], [3])
    @Node.test_func([[3,4]], [7])
    @Node.test_func(["t","e","s","t"], ["test"])
    def func(self, *inp):
        """If no `amount`: return sum(stack)
Else if arg1 is a list, return sum(arg1)
Else return sum(stack[:`amount`])"""
        if self.args == 1:
            inp = inp[0]
        if str in map(type, inp):
            inp = [str(i)for i in inp]
        current = inp[0]
        for val in inp[1:]:
            current += val
        return [current]
    
    def digital_root(self, inp:(str, int)):
        inp = str(inp)
        rtn = 0
        for i in inp:
            rtn += int(i, 36)
        return rtn
    