#!/usr/bin/env python

from nodes import Node

class Sort(Node):
    char = "S"
    args = 1
    results = 1
    def func(self, a: Node.indexable):
        sorted_var = sorted(a)
        if isinstance(a, tuple):
            sorted_var = tuple(sorted_var)
        if isinstance(a, str):
            sorted_var = "".join(sorted_var)
        return [sorted_var]