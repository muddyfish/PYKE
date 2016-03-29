#!/usr/bin/env python

from nodes import Node

class Join(Node):
    char = "J"
    args = 2
    results = 1
    contents = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
    def prepare(self, stack):
        try:
            if isinstance(stack[0], (list,tuple)):
                if not hasattr(self, "sep"):
                    self.sep = ""
                self.args = 1
            elif isinstance(stack[0], str):
                if not hasattr(self, "sep"):
                    self.sep = stack.pop(0)
                self.args = max(1,len(stack))
                if len(stack) == 0:
                    self.add_arg(stack)
                if isinstance(stack[0], (list,tuple)):
                    self.args = 1
            else:
                if not hasattr(self, "sep"):
                    self.sep = ""
                self.args = len(stack)
        except IndexError:
            while len(stack) < self.args:
                self.add_arg(stack)
                self.prepare(stack)
    
    @Node.test_func([1,5], ["15"])
    @Node.test_func([[1,5]], ["15"])
    @Node.test_func([[1,5], " "], ["1 5"])
    @Node.test_func(["Hello", "World!", ", "], ["Hello, World!"])
    @Node.test_func([1,2,3,4, "."], ["1.2.3.4"])
    def func(self, *inp):
        """If arg1 is a list or tuple, args = arg1
Else: args = stack.
return `fixed_arg`.join(args)"""
        if len(inp) == 1:
            inp = inp[0]
        return self.sep.join(map(str, inp))
        