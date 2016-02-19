#!/usr/bin/env python

from nodes import Node

class End(Node):
    char = "e"
    args = 1
    results = 1
    def func(self, a):
        if isinstance(a, int): return ~a
        return a[-1]