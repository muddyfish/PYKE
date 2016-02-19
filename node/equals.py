#!/usr/bin/env python

from nodes import Node

class Equals(Node):
    char = "q"
    args = 2
    results = 1
    def func(self, a,b):
        return a==b