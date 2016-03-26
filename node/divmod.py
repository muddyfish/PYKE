#!/usr/bin/env python

from nodes import Node

class DivMod(Node):
    char = ".D"
    args = 2
    results = 2
    def func(self, a,b):
        """Returns a//b and a%b."""
        return list(divmod(a,b))