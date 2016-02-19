#!/usr/bin/env python

from nodes import Node

class Tail(Node):
    char = "t"
    args = 1
    results = 1
    def func(self, inp):
        if isinstance(inp, int): return inp-1
        return inp[1:]