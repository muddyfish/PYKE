#!/usr/bin/env python

from nodes import Node

class Duplicate(Node):
    char = "D"
    args = 1
    results = 2
    def func(self, a):
        return [a,a]