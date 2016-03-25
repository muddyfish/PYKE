#!/usr/bin/env python

from nodes import Node

class Str(Node):
    char = "X"
    args = 1
    results = None
    def func(self, lst):
        return list(lst)