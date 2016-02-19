#!/usr/bin/env python

from nodes import Node

class Splice(Node):
    char = ":"
    args = 3
    results = 1
    def func(self, a,b,c):
        return a[b:c]