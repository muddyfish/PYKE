#!/usr/bin/env python

from nodes import Node

class And(Node):
    char = "&"
    args = 2
    results = 1
    def func(self, a,b):
        return a and b