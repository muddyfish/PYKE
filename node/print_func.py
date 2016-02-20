#!/usr/bin/env python

from nodes import Node

class PrintFunc(Node):
    char = "p"
    args = 1
    results = 1
    def func(self, arg):
        print(arg)
        return arg