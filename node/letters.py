#!/usr/bin/env python

from nodes import Node
import string

class Letters(Node):
    char = "l"
    args = 1
    results = 1
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
        
    def func(self, x):
        if self.config == 0:
            return self.len(x)
        return Letters.settings[self.config-1](x)
    
    def len(self, x):
        if isinstance(x, Node.number):
            return len(str(x)) - isinstance(x, float)
        return len(x)
    
    def __repr__(self):
        return "%s: %d"%(self.__class__.__name__, self.results)