#!/usr/bin/env python

from nodes import Node

class DivMod(Node):
    char = ".D"
    args = 2
    results = 2
    
    @Node.test_func([5,4], [1,1])
    @Node.test_func([20,7], [2,6])
    def func(self, a,b):
        """Returns a//b and a%b."""
        return list(divmod(a,b))