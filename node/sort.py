#!/usr/bin/env python

from nodes import Node

class Sort(Node):
    char = "S"
    args = 1
    results = 1
    def func(self, a: Node.indexable):
        if isinstance(a, tuple):
            return [tuple(sorted(a))]
        if isinstance(a, str):
            return "".join(sorted(a))
        return [sorted(a)]