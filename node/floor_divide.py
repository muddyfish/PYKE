#!/usr/bin/env python

from nodes import Node

class FloorDiv(Node):
    char = "f"
    args = 2
    results = 1
    def func(self, a,b):
        return a//b