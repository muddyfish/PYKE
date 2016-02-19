#!/usr/bin/env python

from nodes import Node

class Sort(Node):
    char = "S"
    args = 1
    results = 1
    def func(self, a):
        return [sorted(a)]