#!/usr/bin/env python

from nodes import Node

class Head(Node):
    char = "h"
    args = 1
    results = 1
    def func(self, inp):
        if isinstance(inp, int): return inp+1
        return inp[0]