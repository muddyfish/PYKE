#!/usr/bin/env python

from nodes import Node

class PrintFunc(Node):
    char = "\n"
    args = 1
    results = 1
    def func(self, arg):
        """print arg
return arg"""
        print(arg)
        return [arg]