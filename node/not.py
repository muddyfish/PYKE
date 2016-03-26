#!/usr/bin/env python

from nodes import Node

class Not(Node):
    char = "!"
    args = 1
    results = 1
    def func(self, a):
        """not a. Returns an int"""
        return (not a)+0