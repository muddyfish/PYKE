#!/usr/bin/env python

from nodes import Node

class Str(Node):
    char = "`"
    args = 1
    results = 1
    def func(self, a):
        """str(a)"""
        return [str(a)]