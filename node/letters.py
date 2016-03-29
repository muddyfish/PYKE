#!/usr/bin/env python

from nodes import Node
import string

class Letters(Node):
    char = "l"
    args = 1
    results = 1
    default_arg = 0
    contents = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    settings = [lambda x: x.lower(),
                lambda x: x.upper(),
                lambda x: x.swapcase(),
                lambda x: x.title(),
                lambda x: x.capitalize(),
                lambda x: string.capwords(x),
                lambda x: x.strip(),
                lambda x: x.lstrip(),
                lambda x: x.rstrip()
                ]
    
    def __init__(self, config:Node.Base10Single):
        self.config = config
        
    @Node.test_func([[3,2]], [2], "0")
    @Node.test_func(["Hi!"], ["hi!"], "1")
    @Node.test_func(["Hi!"], ["HI!"], "2")
    @Node.test_func(["Hi!"], ["hI!"], "3")
    @Node.test_func(["hello world"], ["Hello World"], "4")
    @Node.test_func(["hello world"], ["Hello world"], "5")
    @Node.test_func(["hello world"], ["Hello World"], "6")
    @Node.test_func(["  world  "], ["world"], "7")
    @Node.test_func(["  world  "], ["world  "], "8")
    @Node.test_func(["  world  "], ["  world"], "9")
    def func(self, x):
        """0 - len
1 - lower
2 - upper
3 - swapcase
4 - title
5 - capitalize
6 - capwords
7 - strip
8 - lstrip
9 - rstrip"""
        if self.config == 0:
            return self.len(x)
        return Letters.settings[self.config-1](x)
    
    def len(self, x):
        if isinstance(x, Node.number):
            return len(str(x)) - isinstance(x, float)
        return len(x)
    
    def __repr__(self):
        return "%s: %d"%(self.__class__.__name__, self.results)