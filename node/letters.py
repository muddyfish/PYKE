#!/usr/bin/env python

from nodes import Node
from node.base10_single import Base10Single
import string

class Letters(Node):
    char = "l"
    args = 1
    results = 1
    
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
    
    def __init__(self, config):
        self.config = config
        
    def func(self, x):
        if self.config == 0:
            return self.len(x)
        return Letters.settings[self.config](x-1)
    
    def len(self, x):
        if isinstance(x, Node.number):
            return len(str(x)) - isinstance(x, float)
        return len(x)
    
    def __repr__(self):
        return "%s: %d"%(self.__class__.__name__, self.results)
        
    @classmethod
    def accepts(cls, code):
        if code[0] == cls.char:
            new_code, digits = Base10Single.accepts(code[1:], accept = True)
            if new_code is None:
                digits = 0
                code = code[1:]
            else:
                digits = digits([])[0]
                code = new_code
            return code, cls(digits)
        return None, None