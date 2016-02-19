#!/usr/bin/env python

from nodes import Node

class Negate(Node):
    char = "_"
    args = 1
    results = 1
    def func(self, a):
        if isinstance(a, basestring):
            return a[::-1]
        return -a