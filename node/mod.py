#!/usr/bin/env python

from nodes import Node

class Mod(Node):
    char = "%"
    args = 2
    results = 1
    def func(self, a,b):
        return a%b